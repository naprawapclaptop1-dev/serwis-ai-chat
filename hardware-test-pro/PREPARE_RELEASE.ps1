# Prepare a new globally distributable build: version bump, 125 themes, icon hover glow.
$ErrorActionPreference = "Stop"
$sourcePath = Join-Path $PSScriptRoot "NaprawaPC_Hardware_Test_PRO.pyw"
$setupPath = Join-Path $PSScriptRoot "SUITE_SETUP.iss"
$manifestPath = Join-Path $PSScriptRoot "..\updates\hardware-test-pro\latest.json"
foreach ($p in @($sourcePath,$setupPath,$manifestPath)) { if (!(Test-Path -LiteralPath $p)) { throw "Missing required file: $p" } }
$manifest = [IO.File]::ReadAllText($manifestPath,[Text.Encoding]::UTF8) | ConvertFrom-Json
if (!$manifest.release_ready -or [string]$manifest.version -notmatch '^\d+\.\d+\.\d+$') { throw "Latest update manifest is not a valid published release." }
$v = [version]$manifest.version
$next = "{0}.{1}.{2}" -f $v.Major,$v.Minor,($v.Build+1)
$setupName = "NAPRAWA-PC-HARDWARE-TEST-PRO-Setup-$next.exe"
$src = [IO.File]::ReadAllText($sourcePath,[Text.Encoding]::UTF8)
$vm = [regex]::Matches($src,'(?m)^VERSION = "(?<v>\d+\.\d+\.\d+) (?<d>[^"]*)"$')
if ($vm.Count -eq 0) { throw "Cannot find application VERSION assignment." }
$last = $vm[$vm.Count-1]
$newLine = 'VERSION = "' + $next + ' ' + $last.Groups["d"].Value + '"'
$src = $src.Substring(0,$last.Index) + $newLine + $src.Substring($last.Index+$last.Length)

# Make global updates install automatically after SHA-256 and PE verification.
# Keep one UAC prompt and show the Inno Setup wizard so update failures never stay invisible.
$confirmPatch = @'
def _u44_confirm_downloaded(self, path, version):
    try:
        installer = Path(path).resolve(strict=True)
        if not installer.is_file():
            raise FileNotFoundError(f"Nie znaleziono instalatora: {installer}")
        if installer.suffix.lower() != ".exe":
            raise ValueError("Pobrany plik nie jest instalatorem EXE.")
        safe_version = re.sub(r"[^0-9A-Za-z._-]", "_", str(version or "update"))
        update_dir = installer.parent
        log_path = update_dir / f"installer-{safe_version}.log"

        # ShellExecuteEx returns Win32 error details and a handle to the actual installer process.
        # This avoids reporting a successful handoff just because ShellExecuteW returned a value.
        if os.name == "nt":
            import ctypes as _u49_ctypes
            from ctypes import wintypes as _u49_wintypes

            class _U49_SHELLEXECUTEINFOW(_u49_ctypes.Structure):
                _fields_ = [
                    ("cbSize", _u49_wintypes.DWORD),
                    ("fMask", _u49_wintypes.ULONG),
                    ("hwnd", _u49_wintypes.HWND),
                    ("lpVerb", _u49_wintypes.LPCWSTR),
                    ("lpFile", _u49_wintypes.LPCWSTR),
                    ("lpParameters", _u49_wintypes.LPCWSTR),
                    ("lpDirectory", _u49_wintypes.LPCWSTR),
                    ("nShow", _u49_ctypes.c_int),
                    ("hInstApp", _u49_wintypes.HINSTANCE),
                    ("lpIDList", _u49_wintypes.LPVOID),
                    ("lpClass", _u49_wintypes.LPCWSTR),
                    ("hkeyClass", _u49_wintypes.HANDLE),
                    ("dwHotKey", _u49_wintypes.DWORD),
                    ("hIcon", _u49_wintypes.HANDLE),
                    ("hProcess", _u49_wintypes.HANDLE),
                ]

            _u49_shell = _u49_ctypes.WinDLL("shell32", use_last_error=True)
            _u49_execute = _u49_shell.ShellExecuteExW
            _u49_execute.argtypes = [_u49_ctypes.POINTER(_U49_SHELLEXECUTEINFOW)]
            _u49_execute.restype = _u49_wintypes.BOOL

            params = f'/NORESTART /SP- /LOG="{log_path}"'
            info = _U49_SHELLEXECUTEINFOW()
            info.cbSize = _u49_ctypes.sizeof(info)
            info.fMask = 0x00000040  # SEE_MASK_NOCLOSEPROCESS
            info.hwnd = None
            info.lpVerb = "runas"
            info.lpFile = str(installer)
            info.lpParameters = params
            info.lpDirectory = str(update_dir)
            info.nShow = 5  # SW_SHOW

            if not _u49_execute(_u49_ctypes.byref(info)):
                err = _u49_ctypes.get_last_error()
                raise OSError(err, _u49_ctypes.FormatError(err).strip(), str(installer))
            if not info.hProcess:
                raise RuntimeError(
                    "Windows accepted ShellExecuteEx, but returned no installer process handle. "
                    "The installer launch could not be confirmed."
                )

            _u49_kernel = _u49_ctypes.WinDLL("kernel32", use_last_error=True)
            _u49_getpid = _u49_kernel.GetProcessId
            _u49_getpid.argtypes = [_u49_wintypes.HANDLE]
            _u49_getpid.restype = _u49_wintypes.DWORD
            pid = int(_u49_getpid(info.hProcess))
            _u49_kernel.CloseHandle.argtypes = [_u49_wintypes.HANDLE]
            _u49_kernel.CloseHandle.restype = _u49_wintypes.BOOL
            _u49_kernel.CloseHandle(info.hProcess)
            if pid <= 0:
                raise RuntimeError("The installer process started, but Windows did not return a valid PID.")
        else:
            proc = subprocess.Popen(
                [str(installer), "/NORESTART", "/SP-"],
                cwd=str(update_dir)
            )
            pid = int(proc.pid)

        details = (
            f"WINDOWS_LAUNCH_ACCEPTED=1\\nVERSION={version}\\nPID={pid}\\n"
            f"INSTALLER={installer}\\nLOG={log_path}\\n"
        )
        (update_dir / f"installer-{safe_version}-launch.txt").write_text(details, encoding="utf-8")
        try:
            self.append_log(
                f"Aktualizator: Windows przyjął uruchomienie instalatora {version}; PID={pid}; log={log_path}"
            )
        except Exception:
            pass
        try:
            self._u39_set_update_status(
                f"Windows uruchomił proces instalatora {version} (PID {pid}). "
                f"Jeśli nie widać kreatora/UAC, sprawdź raport: {update_dir / f'installer-{safe_version}-launch.txt'}"
            )
        except Exception:
            pass
    except Exception as exc:
        msg = f"Nie udało się uruchomić aktualizacji: {type(exc).__name__}: {exc}"
        try:
            self._u39_set_update_status(msg)
        except Exception:
            pass
        try:
            self.append_log("Aktualizator globalny: " + msg)
        except Exception:
            pass
        messagebox.showerror("Aktualizacja globalna", msg)


def _u44_dispatch_confirm_downloaded(self, path, version):
    # Called through the UI event queue, but uses module functions directly rather than fragile instance aliases.
    try:
        self._u39_set_update_status(f"Uruchamiam zweryfikowany instalator {version} przez Windows/UAC...")
    except Exception:
        pass
    try:
        _u44_confirm_downloaded(self, path, version)
    except Exception as exc:
        msg = f"Nie udało się uruchomić instalatora {version}: {type(exc).__name__}: {exc}"
        try:
            self._u39_set_update_status(msg)
        except Exception:
            pass
        try:
            self.append_log(msg)
        except Exception:
            pass
        try:
            messagebox.showerror("Aktualizacja globalna — błąd uruchamiania", msg)
        except Exception:
            pass
'@
$confirmPattern = '(?s)def _u44_confirm_downloaded\(self, path, version\):.*?(?=\r?\nAppV43\._u44_set_progress = _u44_set_progress)'
$confirmMatches = [regex]::Matches($src, $confirmPattern)
if ($confirmMatches.Count -ne 1) { throw "Oczekiwano dokładnie jednej funkcji _u44_confirm_downloaded; znaleziono $($confirmMatches.Count)." }
$src = [regex]::Replace($src, $confirmPattern, [System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $confirmPatch.TrimEnd()
}, 1)
$oldLauncherSelfTest = 'assert "ShellExecuteW" in _u44_confirm_downloaded.__code__.co_names'
$newLauncherSelfTest = 'assert "ShellExecuteExW" in _u44_confirm_downloaded.__code__.co_names' + [Environment]::NewLine +
'    assert "runas" in _u44_confirm_downloaded.__code__.co_consts' + [Environment]::NewLine +
'    assert "GetProcessId" in _u44_confirm_downloaded.__code__.co_names' + [Environment]::NewLine +
'    assert "WINDOWS_LAUNCH_ACCEPTED=1" in str(_u44_confirm_downloaded.__code__.co_consts)' + [Environment]::NewLine +
'    assert "ShellExecuteW" not in _u44_confirm_downloaded.__code__.co_names' + [Environment]::NewLine +
'    assert "/SILENT" not in str(_u44_confirm_downloaded.__code__.co_consts)' + [Environment]::NewLine +
'    assert "/SUPPRESSMSGBOXES" not in str(_u44_confirm_downloaded.__code__.co_consts)' + [Environment]::NewLine +
'    assert "/NORESTART" in str(_u44_confirm_downloaded.__code__.co_consts)' + [Environment]::NewLine +
'    assert "ExecutionPolicy Bypass" not in str(_u44_confirm_downloaded.__code__.co_consts)' + [Environment]::NewLine +
'    assert "Start-Process" not in str(_u44_confirm_downloaded.__code__.co_consts)' + [Environment]::NewLine +
'    assert "installer-" in str(_u44_confirm_downloaded.__code__.co_consts) and ".log" in str(_u44_confirm_downloaded.__code__.co_consts)' + [Environment]::NewLine +
'    assert "askyesno" not in _u44_confirm_downloaded.__code__.co_names' + [Environment]::NewLine +
'    assert "uuid4" in _u44_download_global_update.__code__.co_names' + [Environment]::NewLine +
'    assert "_u44_dispatch_confirm_downloaded" in _u44_download_global_update.__code__.co_names' + [Environment]::NewLine +
'    assert "startfile" not in _u44_download_global_update.__code__.co_names' + [Environment]::NewLine +
'    assert "NaprawaPC-Update-" in _u44_download_global_update.__code__.co_consts' + [Environment]::NewLine +
'    assert not re.match(r"^NAPRAWA-PC-HARDWARE-TEST-PRO-.*\.exe$", "NaprawaPC-Update-NAPRAWA-PC-HARDWARE-TEST-PRO-Setup-4.3.140-deadbeef.exe", re.I)' + [Environment]::NewLine +
'    assert "explorer.exe" not in _u44_download_global_update.__code__.co_consts' + [Environment]::NewLine +
'    assert "_u39_confirm_downloaded" not in _u44_download_global_update.__code__.co_names' + [Environment]::NewLine +
'    assert "_u44_confirm_downloaded" not in _u44_download_global_update.__code__.co_names' + [Environment]::NewLine +
'    assert "_u44_confirm_downloaded" in _u44_dispatch_confirm_downloaded.__code__.co_names' + [Environment]::NewLine +
'    assert "gettempdir" in _u44_download_global_update.__code__.co_names' + [Environment]::NewLine +
'    assert "xb" in _u44_download_global_update.__code__.co_consts' + [Environment]::NewLine +
'    assert "close_app" not in _u44_confirm_downloaded.__code__.co_names'
if ($src.Contains($oldLauncherSelfTest)) {
    $src = $src.Replace($oldLauncherSelfTest, $newLauncherSelfTest)
} elseif (!$src.Contains('assert "ShellExecuteExW" in _u44_confirm_downloaded.__code__.co_names')) {
    throw "Nie znaleziono ani starego, ani poprawionego testu uruchamiania instalatora."
} else {
    # Make patching idempotent when the asset source already contains the new launcher assertion.
    $assertions = @(
        '    assert "GetProcessId" in _u44_confirm_downloaded.__code__.co_names',
        '    assert "WINDOWS_LAUNCH_ACCEPTED=1" in str(_u44_confirm_downloaded.__code__.co_consts)',
        '    assert "ShellExecuteW" not in _u44_confirm_downloaded.__code__.co_names'
    )
    $anchor = 'assert "ShellExecuteExW" in _u44_confirm_downloaded.__code__.co_names'
    foreach ($assertion in $assertions) {
        if (!$src.Contains($assertion)) {
            $src = $src.Replace($anchor, $anchor + [Environment]::NewLine + $assertion)
        }
    }
}


$downloadPatch = @'
def _u44_download_global_update(self, data):
    import uuid as _u47_uuid
    import tempfile as _u47_tempfile
    import os as _u47_os
    import re as _u47_re
    import hashlib as _u47_hashlib
    import urllib.parse as _u47_urlparse
    import urllib.request as _u47_request
    version = str(data.get("version") or "update")
    filename = str(data.get("filename") or "")
    if not _u47_re.fullmatch(r"[A-Za-z0-9._-]+\.exe", filename, _u47_re.I):
        raise ValueError("Nieprawidlowa nazwa pliku aktualizacji.")
    url = str(data.get("download_url") or "")
    parsed = _u47_urlparse.urlparse(url)
    if parsed.scheme != "https" or (parsed.hostname or "").lower() != "github.com":
        raise ValueError("Adres aktualizacji nie jest dozwolonym HTTPS GitHub.")
    expected_hash = str(data.get("sha256") or "").lower()
    if not _u47_re.fullmatch(r"[0-9a-f]{64}", expected_hash):
        raise ValueError("Manifest nie zawiera prawidlowego SHA-256.")
    expected_size = int(data.get("size") or 0)
    if expected_size < 1024 * 1024 or expected_size > _U39_MAX_INSTALLER_BYTES:
        raise ValueError("Rozmiar instalatora aktualizacji poza dozwolonym zakresem.")

    token = f"{_u47_os.getpid()}-{_u47_uuid.uuid4().hex}"
    candidates = []
    local_root = Path(os.environ.get("LOCALAPPDATA") or Path.home()) / "NaprawaPC" / "Updates"
    temp_root = Path(_u47_tempfile.gettempdir()) / "NaprawaPC" / "Updates"
    candidates.extend([local_root, temp_root])
    root = None
    errors = []
    for candidate in candidates:
        probe = candidate / (".write-test-" + token + ".tmp")
        try:
            candidate.mkdir(parents=True, exist_ok=True)
            with open(probe, "xb") as probe_file:
                probe_file.write(b"ok")
            probe.unlink()
            root = candidate
            break
        except OSError as exc:
            errors.append(f"{candidate}: {type(exc).__name__}: {exc}")
            try:
                probe.unlink(missing_ok=True)
            except Exception:
                pass
    if root is None:
        msg = "Brak dostepnego folderu do zapisu aktualizacji. " + " | ".join(errors)
        self.queue_action(lambda m=msg: self._u39_set_update_status(m))
        self.queue_action(lambda m=msg: messagebox.showerror("Aktualizacja globalna", m))
        return

    # Prefix local EXE with NaprawaPC-Update- so Setup's legacy taskkill image-name filter
    # cannot kill the installer itself while closing the older application process.
    dest = root / ("NaprawaPC-Update-" + Path(filename).stem + "-" + token + ".exe")
    tmp = root / ("." + filename + "-" + token + ".download")
    self.queue_action(lambda v=version: self._u44_set_progress(0, f"Przygotowuje bezpieczne pobieranie aktualizacji {v}..."))
    try:
        req = _u47_request.Request(url, headers={
            "User-Agent": f"NAPRAWA-PC-HARDWARE-TEST-PRO/{str(VERSION).split()[0]}",
            "Cache-Control": "no-cache"
        })
        hasher = _u47_hashlib.sha256()
        total = 0
        last = -1
        with _u47_request.urlopen(req, timeout=60) as response:
            final = _u47_urlparse.urlparse(response.geturl())
            if final.scheme != "https" or (final.hostname or "").lower() not in _U39_ALLOWED_DOWNLOAD_HOSTS:
                raise ValueError("Przekierowanie pobierania trafiło na niedozwolony adres.")
            with open(tmp, "xb") as out:
                while True:
                    chunk = response.read(512 * 1024)
                    if not chunk:
                        break
                    total += len(chunk)
                    if total > expected_size or total > _U39_MAX_INSTALLER_BYTES:
                        raise ValueError("Pobrany plik przekracza zadeklarowany rozmiar.")
                    hasher.update(chunk)
                    out.write(chunk)
                    p = min(100, int(total * 100 / max(1, expected_size)))
                    if p >= last + 2 or p == 100:
                        last = p
                        msg = f"Pobieranie {version}: {p}% ({total / 1048576:.1f}/{expected_size / 1048576:.1f} MB)"
                        self.queue_action(lambda p=p, m=msg: self._u44_set_progress(p, m))
        if total != expected_size:
            raise ValueError(f"Niepełny plik: pobrano {total} B, manifest podaje {expected_size} B.")
        actual = hasher.hexdigest()
        if actual != expected_hash:
            raise ValueError(f"SHA-256 niezgodne: {actual}; aktualizacja odrzucona.")
        with open(tmp, "rb") as verified:
            if verified.read(2) != b"MZ":
                raise ValueError("Pobrany plik nie jest plikiem wykonywalnym Windows PE.")
        os.replace(tmp, dest)

        # Automatic update: do not send the user to Explorer; queue the verified Setup with normal Windows UAC.
        self.queue_action(lambda p=str(dest), v=version: self._u44_set_progress(100, f"Pobrano {v}; rozmiar, PE i SHA-256 są poprawne. Uruchamiam instalator przez Windows UAC."))
        self.queue_action(lambda p=str(dest), v=version: _u44_dispatch_confirm_downloaded(self, p, v))
    except Exception as exc:
        try:
            tmp.unlink(missing_ok=True)
        except Exception:
            pass
        msg = f"Blad pobierania aktualizacji: {type(exc).__name__}: {exc}"
        if isinstance(exc, PermissionError):
            msg += " Sprawdz historie ochrony Bitdefender/Windows oraz uprawnienia folderu. Program nie wylacza ochrony i nie dodaje wyjatkow."
        self.queue_action(lambda m=msg: self._u39_set_update_status(m))
        self.queue_action(lambda m=msg: messagebox.showerror("Aktualizacja globalna", m))
'@
$downloadPattern = '(?s)def _u44_download_global_update\(self, data\):.*?(?=\r?\ndef _u44_confirm_downloaded\(self, path, version\):)'
$downloadMatches = [regex]::Matches($src, $downloadPattern)
if ($downloadMatches.Count -ne 1) { throw "Oczekiwano jednej funkcji pobierania _u44_download_global_update; znaleziono $($downloadMatches.Count)." }
$src = [regex]::Replace($src, $downloadPattern, [System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $downloadPatch.TrimEnd()
}, 1)

if (!$src.Contains("# _U443_THEME_PACK")) {
$theme = @'
# _U443_THEME_PACK — 115 additional selectable palettes
import colorsys as _u443_cs
_U443_PREFIX = ("NEON","DARK","DEEP","ULTRA","FUTURE","CYBER","LASER","ARCTIC","NIGHT","TITAN","QUANTUM","COSMIC","STEALTH","PRO","ELECTRIC","SILK","NOVA","NEXUS","ORBIT","PHOTON","TURBO","HYPER","AURORA")
_U443_SUFFIX = ("OCEAN BLUE","VIOLET","MATRIX GREEN","BLACK GOLD","CRIMSON")
_U443_HUES = (0.56,0.76,0.36,0.12,0.99)
_U443_SKIN_PROFILES = (
    {"name":"NEON GLASS","panel_relief":"flat","panel_bd":0,"panel_highlight":2,"button_relief":"flat","button_overrelief":"ridge","button_bd":0,"font":"Segoe UI","image":"neon","layout":"sidebar","scanlines":False},
    {"name":"CARBON LAYER","panel_relief":"groove","panel_bd":2,"panel_highlight":1,"button_relief":"raised","button_overrelief":"ridge","button_bd":1,"font":"Bahnschrift","image":"carbon","layout":"topbar","scanlines":False},
    {"name":"CYBER ANGULAR","panel_relief":"solid","panel_bd":1,"panel_highlight":2,"button_relief":"flat","button_overrelief":"raised","button_bd":1,"font":"Segoe UI","image":"angular","layout":"grid","scanlines":False},
    {"name":"MATRIX TERMINAL","panel_relief":"ridge","panel_bd":1,"panel_highlight":1,"button_relief":"raised","button_overrelief":"ridge","button_bd":1,"font":"Consolas","image":"matrix","layout":"terminal","scanlines":True},
    {"name":"ICE MINIMAL","panel_relief":"flat","panel_bd":0,"panel_highlight":1,"button_relief":"flat","button_overrelief":"raised","button_bd":0,"font":"Segoe UI","image":"ice","layout":"topbar","scanlines":False},
    {"name":"VIOLET HOLOGRAM","panel_relief":"ridge","panel_bd":2,"panel_highlight":2,"button_relief":"raised","button_overrelief":"ridge","button_bd":1,"font":"Bahnschrift","image":"hologram","layout":"sidebar","scanlines":False},
    {"name":"RED GAMING","panel_relief":"solid","panel_bd":2,"panel_highlight":2,"button_relief":"raised","button_overrelief":"raised","button_bd":2,"font":"Segoe UI","image":"redline","layout":"grid","scanlines":False},
    {"name":"AMBER INDUSTRIAL","panel_relief":"groove","panel_bd":2,"panel_highlight":1,"button_relief":"groove","button_overrelief":"raised","button_bd":1,"font":"Consolas","image":"amber","layout":"terminal","scanlines":True},
    {"name":"STEEL PRO","panel_relief":"ridge","panel_bd":2,"panel_highlight":1,"button_relief":"ridge","button_overrelief":"raised","button_bd":1,"font":"Segoe UI","image":"steel","layout":"topbar","scanlines":False},
    {"name":"CARBON SCANLINE","panel_relief":"sunken","panel_bd":1,"panel_highlight":1,"button_relief":"raised","button_overrelief":"ridge","button_bd":1,"font":"Consolas","image":"carbon","layout":"terminal","scanlines":True},
    {"name":"AURORA LAYER","panel_relief":"flat","panel_bd":0,"panel_highlight":3,"button_relief":"flat","button_overrelief":"ridge","button_bd":0,"font":"Bahnschrift","image":"aurora","layout":"sidebar","scanlines":False},
    {"name":"RETRO HUD","panel_relief":"groove","panel_bd":2,"panel_highlight":1,"button_relief":"raised","button_overrelief":"sunken","button_bd":2,"font":"Consolas","image":"retro","layout":"grid","scanlines":True},
)
def _u443_hex(h,l,s):
    rgb = _u443_cs.hls_to_rgb(h % 1.0,l,s)
    return "#" + "".join(f"{round(x*255):02x}" for x in rgb)
for _u443_tid in range(11,126):
    _u443_i = _u443_tid-11
    _u443_family = _u443_i // 5
    _u443_group = _u443_i % 5
    _u443_hue = (_U443_HUES[_u443_group] + _u443_family*0.0137) % 1.0
    _u443_light = (_u443_i % 17 == 0)
    if _u443_light:
        _u443_bg = _u443_hex(_u443_hue,0.965,0.16)
        _u443_panel = "#ffffff"
        _u443_card = _u443_hex(_u443_hue,0.925,0.22)
        _u443_fg,_u443_muted = "#152033","#5e6d80"
        _u443_accent = _u443_hex(_u443_hue,0.39,0.88)
        _u443_accent2 = _u443_hex(_u443_hue,0.53,0.82)
    else:
        _u443_bg = _u443_hex(_u443_hue,0.055+(_u443_family%3)*0.012,0.48)
        _u443_panel = _u443_hex(_u443_hue,0.085+(_u443_family%3)*0.012,0.50)
        _u443_card = _u443_hex(_u443_hue,0.125+(_u443_family%3)*0.012,0.52)
        _u443_fg,_u443_muted = "#edf7ff","#93a9bd"
        _u443_accent = _u443_hex(_u443_hue,0.60,0.98)
        _u443_accent2 = _u443_hex(_u443_hue,0.77,0.90)
    THEMES[_u443_tid] = {
        "name": f"{_U443_SKIN_PROFILES[_u443_family % len(_U443_SKIN_PROFILES)]['name']} • {_U443_SUFFIX[_u443_group]} • {_u443_tid:03d}",
        "bg": _u443_bg,"panel": _u443_panel,"card": _u443_card,
        "fg": _u443_fg,"muted": _u443_muted,
        "accent": _u443_accent,"accent2": _u443_accent2,
        "good": _u443_hex(0.37,0.55,0.78),
        "warn": _u443_hex(0.12,0.60,0.86),
        "bad": _u443_hex(0.99,0.59,0.88),
    }
_U443_LAYOUTS = ("sidebar","topbar","grid","terminal","split","compact","wide","instrument","radial","stacked","cards","dock","hybrid")
_U443_SHAPES = ("angular","rounded","bevel","double","corners","notched","outline","inset","circuit","hex","technical","minimal","glass")
_U443_TEXTURES = ("grid","diagonal","dots","circuit","wave","radial","hex","scanline","dash","matrix","crosshair","rings","stars")
_U443_CHARTS = ("line","area","bars","steps","spectrum","radial","wave","candles","dots","dual")
_U443_FONTS = ("Segoe UI","Bahnschrift","Consolas","Arial","Georgia","Courier New","Trebuchet MS","Tahoma","Verdana","Calibri","Cambria","Lucida Console")
_U443_PANEL_RELIEFS = ("flat","groove","solid","ridge","raised","sunken")
_U443_BUTTON_RELIEFS = ("flat","raised","groove","ridge","solid","sunken")
_U443_IMAGE_STYLES = ("neon","carbon","angular","matrix","ice","hologram","redline","amber","steel","retro","aurora","glass","wave","blueprint","plasma")
_U443_PANEL_FILLS = ("panel","card","panel","bg","card")
for _u443_tid, _u443_theme in THEMES.items():
    _u443_n = _u443_tid - 1
    _u443_prof = _U443_SKIN_PROFILES[_u443_n % len(_U443_SKIN_PROFILES)]
    _u443_layout = _U443_LAYOUTS[(_u443_n * 7 + _u443_n // 11) % len(_U443_LAYOUTS)]
    _u443_shape = _U443_SHAPES[(_u443_n * 5 + _u443_n // 13) % len(_U443_SHAPES)]
    _u443_texture = _U443_TEXTURES[(_u443_n * 7 + _u443_n // 9) % len(_U443_TEXTURES)]
    _u443_chart = _U443_CHARTS[(_u443_n * 3 + _u443_n // 7) % len(_U443_CHARTS)]
    _u443_font = _U443_FONTS[(_u443_n * 5 + _u443_n // 13) % len(_U443_FONTS)]
    _u443_theme["_skin_variant"] = _u443_n
    _u443_theme["_skin_id"] = _u443_n
    _u443_theme["_skin_family"] = f"{_u443_prof['name']} / {_u443_layout.upper()} / {_u443_shape.upper()} / {_u443_tid:03d}"
    _u443_theme["name"] = f"{_u443_prof['name']} • {_u443_layout.upper()} • {_u443_shape.upper()} • {_u443_chart.upper()} • {_u443_tid:03d}"
    _u443_theme["_skin_layout"] = _u443_layout
    _u443_theme["_skin_shape"] = _u443_shape
    _u443_theme["_skin_texture"] = _u443_texture
    _u443_theme["_skin_chart_style"] = _u443_chart
    _u443_theme["_panel_relief"] = _U443_PANEL_RELIEFS[(_u443_n * 5 + _u443_n // 4) % len(_U443_PANEL_RELIEFS)]
    _u443_theme["_panel_bd"] = _u443_n % 4
    _u443_theme["_panel_highlight"] = 1 + (_u443_n % 4)
    _u443_theme["_button_relief"] = _U443_BUTTON_RELIEFS[(_u443_n * 3 + _u443_n // 5) % len(_U443_BUTTON_RELIEFS)]
    _u443_theme["_button_overrelief"] = _U443_BUTTON_RELIEFS[(_u443_n * 5 + 1) % len(_U443_BUTTON_RELIEFS)]
    _u443_theme["_button_bd"] = _u443_n % 3
    _u443_theme["_font_family"] = _u443_font
    _u443_theme["_font_scale"] = round(0.86 + (_u443_n % 13) * 0.024, 3)
    _u443_theme["_font_slant"] = "italic" if _u443_n % 9 == 0 else "roman"
    _u443_theme["_font_underline"] = _u443_n % 19 == 0
    _u443_theme["_image_style"] = _U443_IMAGE_STYLES[(_u443_n * 5 + _u443_n // 9) % len(_U443_IMAGE_STYLES)]
    _u443_theme["_scanlines"] = (_u443_n % 5 == 0) or _u443_texture == "scanline"
    _u443_theme["_skin_density"] = _u443_n % 5
    _u443_theme["_skin_spacing"] = 4 + (_u443_n % 9)
    _u443_theme["_skin_corner"] = 2 + ((_u443_n * 7) % 22)
    _u443_theme["_skin_nav_width"] = 92 + ((_u443_n * 5) % 83)
    _u443_theme["_skin_card_count"] = 3 + (_u443_n % 4)
    _u443_theme["_skin_chart_variant"] = _u443_n % len(_U443_CHARTS)
    _u443_theme["_skin_panel_fill"] = _U443_PANEL_FILLS[(_u443_n // 3) % len(_U443_PANEL_FILLS)]
    _u443_theme["_skin_button_padx"] = 4 + ((_u443_n * 3) % 9)
    _u443_theme["_skin_button_pady"] = 2 + ((_u443_n * 5) % 7)
    _u443_theme["_skin_border_mode"] = ("line","double","corners","notched","dots")[_u443_n % 5]
    _u443_theme["_skin_background_alpha"] = 12 + ((_u443_n * 7) % 34)
    _u443_theme["_skin_visual_seed"] = (_u443_n * 7919 + 104729) % 1000003
'@
    $pattern = '(?m)^\}\r?\n\r?\nMODULES = \['
    if ($src -notmatch $pattern) { throw "Cannot find base theme palette insertion point." }
    $src = [regex]::Replace($src,$pattern,[System.Text.RegularExpressions.MatchEvaluator]{
        param($m)
        return "}" + [Environment]::NewLine + [Environment]::NewLine + $theme + [Environment]::NewLine + "MODULES = ["
    },1)
}
$src = [regex]::Replace($src,'range\(\s*1\s*,\s*11\s*\)','range(1,126)')
$src = $src.Replace("10 STYLOW","125 STYLOW").Replace("10 STYLI","125 STYLI")

if (!$src.Contains("# _U443_ICON_HOVER_GLOW")) {
$hover = @'
# _U443_ICON_HOVER_GLOW — bind glow to real controls each time a view is rebuilt
def _u443_bind_hover_glow(root, app):
    try:
        t=app.colors(); accent=t.get("accent","#1aa7ff"); accent2=t.get("accent2","#55d8ff")
        widgets=root.winfo_children()
    except Exception:
        return
    for w in widgets:
        try:
            if not getattr(w,"_u443_hover_bound",False):
                if isinstance(w,tk.Button):
                    normal={"bg":w.cget("bg"),"fg":w.cget("fg"),"highlightthickness":w.cget("highlightthickness"),"highlightbackground":w.cget("highlightbackground"),"highlightcolor":w.cget("highlightcolor")}
                    def enter(event,ww=w,aa=accent,aa2=accent2):
                        try:
                            if str(ww.cget("state"))!="disabled": ww.configure(bg=aa,fg="#ffffff",highlightbackground=aa2,highlightcolor=aa2,highlightthickness=2)
                        except Exception: pass
                    def leave(event,ww=w,nn=normal):
                        try: ww.configure(**nn)
                        except Exception: pass
                    w.bind("<Enter>",enter,add="+"); w.bind("<Leave>",leave,add="+"); w._u443_hover_bound=True
                elif isinstance(w,ttk.Button):
                    oldstyle=w.cget("style"); st=ttk.Style(app)
                    st.configure("NaprawaPCHover.TButton",background=accent,foreground="#ffffff")
                    st.map("NaprawaPCHover.TButton",background=[("active",accent2),("pressed",accent)])
                    w.bind("<Enter>",lambda e,ww=w: ww.configure(style="NaprawaPCHover.TButton"),add="+")
                    w.bind("<Leave>",lambda e,ww=w,ss=oldstyle: ww.configure(style=ss),add="+"); w._u443_hover_bound=True
                elif isinstance(w,tk.Label):
                    txt=str(w.cget("text") or "").strip()
                    is_icon=bool(txt) and len(txt)<=4 and any(ord(ch)>=0x2300 for ch in txt)
                    if is_icon or str(w.cget("cursor")) in ("hand","hand2"):
                        fg,bg=w.cget("fg"),w.cget("bg")
                        def enter_label(e,ww=w,aa=accent2,bb=accent):
                            try:
                                ww.configure(fg=aa)
                                if str(ww.cget("cursor")) in ("hand","hand2"): ww.configure(bg=bb)
                            except Exception: pass
                        def leave_label(e,ww=w,ff=fg,bbg=bg):
                            try: ww.configure(fg=ff,bg=bbg)
                            except Exception: pass
                        w.bind("<Enter>",enter_label,add="+"); w.bind("<Leave>",leave_label,add="+"); w._u443_hover_bound=True
                elif isinstance(w,tk.Canvas) and str(w.cget("cursor")) in ("hand","hand2"):
                    thick,bg=w.cget("highlightthickness"),w.cget("highlightbackground")
                    w.bind("<Enter>",lambda e,ww=w,aa=accent2: ww.configure(highlightbackground=aa,highlightcolor=aa,highlightthickness=2),add="+")
                    w.bind("<Leave>",lambda e,ww=w,tt=thick,bb=bg: ww.configure(highlightthickness=tt,highlightbackground=bb,highlightcolor=bb),add="+"); w._u443_hover_bound=True
        except Exception: pass
        try: _u443_bind_hover_glow(w,app)
        except Exception: pass

def _u443_schedule_hover(app):
    try: app.after_idle(lambda: _u443_bind_hover_glow(app,app))
    except Exception: pass
_U443_OLD_CLEAR=getattr(AppV43,"clear",None)
if callable(_U443_OLD_CLEAR):
    def _u443_clear_hook(self,*args,**kwargs):
        result=_U443_OLD_CLEAR(self,*args,**kwargs)
        _u443_schedule_hover(self)
        return result
    AppV43.clear=_u443_clear_hook
_U443_OLD_INIT=AppV43.__init__
def _u443_init_hook(self,*args,**kwargs):
    _U443_OLD_INIT(self,*args,**kwargs)
    try: self.after(350,lambda:_u443_bind_hover_glow(self,self))
    except Exception: pass
AppV43.__init__=_u443_init_hook

# Dashboard controls can be recreated on resize; rebind hover glow on each re-creation.
def _u443_wrap_hover_refresh(original):
    def _wrapped(self,*args,**kwargs):
        result=original(self,*args,**kwargs)
        _u443_schedule_hover(self)
        return result
    _wrapped._u443_hover_wrapper=True
    return _wrapped

for _u443_method_name in ("_install_dashboard_controls","_v4321_bind_canvas_router","_v4323_bind_canvas_router","_v4325_install_dashboard_controls"):
    _u443_method=getattr(AppV43,_u443_method_name,None)
    if callable(_u443_method) and not getattr(_u443_method,"_u443_hover_wrapper",False):
        setattr(AppV43,_u443_method_name,_u443_wrap_hover_refresh(_u443_method))

# _U443_TRUE_SKINS — panel shape/depth, typography, real dashboard filters and hover-image controls.
for _u443_tid, _u443_theme in THEMES.items():
    _u443_theme.setdefault("_skin_family", _U443_SKIN_PROFILES[(_u443_tid-1)%len(_U443_SKIN_PROFILES)]["name"])
    _u443_theme.setdefault("_skin_id", (_u443_tid-1)%len(_U443_SKIN_PROFILES))
    _u443_profile = _U443_SKIN_PROFILES[(_u443_tid-1)%len(_U443_SKIN_PROFILES)]
    for _u443_key, _u443_profile_key in (("_panel_relief","panel_relief"),("_panel_bd","panel_bd"),("_panel_highlight","panel_highlight"),("_button_relief","button_relief"),("_button_overrelief","button_overrelief"),("_button_bd","button_bd"),("_font_family","font"),("_image_style","image"),("_skin_layout","layout"),("_scanlines","scanlines")):
        _u443_theme.setdefault(_u443_key, _u443_profile[_u443_profile_key])

_U443_ORIG_PANEL = AppV43.panel
def _u443_panel_skin(self, parent, bg=None, accent=True):
    frame = _U443_ORIG_PANEL(self, parent, bg, accent)
    t = self.colors()
    try:
        n=int(t.get("_skin_variant",0))
        relief=t.get("_panel_relief","flat")
        border=int(t.get("_panel_bd",0))
        border_mode=t.get("_skin_border_mode","line")
        if border_mode=="double": border=max(1,border)
        elif border_mode=="corners": border=max(1,border)
        elif border_mode=="notched": relief="solid"
        thickness=max(1,int(t.get("_panel_highlight",1)))
        frame.configure(relief=relief, bd=border,
            highlightthickness=thickness,
            highlightbackground=t.get("accent","#1aa7ff") if accent else t.get("accent2",t.get("panel","#0b1c30")),
            highlightcolor=t.get("accent2","#55d8ff"),
            cursor="arrow")
        # Give each theme its own frame fill and relief combination, while child controls keep their semantic colours.
        if t.get("_skin_panel_fill") in ("panel","card","bg"):
            frame.configure(background=t.get(t.get("_skin_panel_fill","panel"),t.get("panel","#0b1c30")))
    except Exception: pass
    return frame
AppV43.panel = _u443_panel_skin

_U443_ORIG_MAKE_BUTTON = AppV43.make_button
def _u443_make_button_skin(self, parent, text, command, kind="card", side=None, fill=None, ipady=8):
    button = _U443_ORIG_MAKE_BUTTON(self, parent, text, command, kind, side, fill, ipady)
    t = self.colors()
    try:
        relief=t.get("_button_relief","flat")
        over=t.get("_button_overrelief","raised")
        border=int(t.get("_button_bd",0))
        scale=float(t.get("_font_scale",1.0))
        padx=int(t.get("_skin_button_padx",7)); pady=int(t.get("_skin_button_pady",3))
        button.configure(relief=relief, overrelief=over, bd=border,
            highlightthickness=1 if border else 0,
            highlightbackground=t.get("accent","#1aa7ff"), highlightcolor=t.get("accent2","#55d8ff"),
            activebackground=t.get("accent2","#55d8ff"), activeforeground="#ffffff", cursor="hand2",
            padx=padx, pady=pady,
            font=self.fnt(max(7,round(9*scale)), "bold" if int(t.get("_skin_density",0))%2==0 else "normal"))
    except Exception: pass
    return button
AppV43.make_button = _u443_make_button_skin

_U443_ORIG_FNT = AppV43.fnt
def _u443_skin_font(self, size=10, weight="normal"):
    t = self.colors()
    family = t.get("_font_family","Segoe UI")
    scale=float(t.get("_font_scale",1.0))
    actual_size=max(7,min(28,round(int(size)*scale)))
    slant=t.get("_font_slant","roman")
    underline=bool(t.get("_font_underline",False))
    key = ("_u443_skin_font", actual_size, str(weight), family, slant, underline)
    try:
        if key not in self.fonts:
            self.fonts[key] = tkfont.Font(family=family, size=actual_size, weight=str(weight),
                                         slant=slant, underline=underline)
        return self.fonts[key]
    except Exception:
        return _U443_ORIG_FNT(self, size, weight)
AppV43.fnt = _u443_skin_font

def _u443_apply_ttk_skin(self):
    try:
        t=self.colors()
        st=ttk.Style(self)
        try: st.theme_use("clam")
        except Exception: pass
        scale=float(t.get("_font_scale",1.0)); spacing=int(t.get("_skin_spacing",8)); density=int(t.get("_skin_density",0))
        font_family=t.get("_font_family","Segoe UI")
        rowheight=max(20,min(40,round((24+density*2)*scale)))
        st.configure("TCombobox",fieldbackground=t["card"],background=t["panel"],foreground=t["fg"],arrowcolor=t["accent"],bordercolor=t["accent"],padding=(max(2,spacing//2),max(2,spacing//3)),font=(font_family,max(8,round(9*scale))))
        st.map("TCombobox",fieldbackground=[("readonly",t["card"]),("focus",t["panel"])],foreground=[("readonly",t["fg"])],background=[("active",t["accent"])])
        st.configure("TNotebook",background=t["bg"],borderwidth=int(t.get("_panel_bd",0)))
        st.configure("TNotebook.Tab",background=t["card"],foreground=t["fg"],padding=(max(6,spacing+4),max(4,spacing//2+3)),borderwidth=int(t.get("_button_bd",0)),font=(font_family,max(8,round(9*scale))))
        st.map("TNotebook.Tab",background=[("selected",t["accent"]),("active",t["accent2"])],foreground=[("selected","#ffffff"),("active","#ffffff")])
        st.configure("Treeview",background=t["card"],fieldbackground=t["card"],foreground=t["fg"],borderwidth=int(t.get("_panel_bd",0)),rowheight=rowheight,font=(font_family,max(8,round(9*scale))))
        st.map("Treeview",background=[("selected",t["accent"])],foreground=[("selected","#ffffff")])
        st.configure("Treeview.Heading",background=t["panel"],foreground=t["accent"],relief=t.get("_panel_relief","flat"),borderwidth=int(t.get("_panel_bd",0)),font=(font_family,max(8,round(9*scale)),"bold"))
        st.map("Treeview.Heading",background=[("active",t["accent"])],foreground=[("active","#ffffff")])
        st.configure("Horizontal.TProgressbar",background=t["accent"],troughcolor=t["card"],bordercolor=t["accent"],lightcolor=t["accent2"],darkcolor=t["panel"],thickness=max(9,min(24,round((11+density*2)*scale))))
    except Exception: pass

_U443_ORIG_BUILD_SHELL = AppV43._build_shell
def _u443_build_shell_skin(self,*args,**kwargs):
    result=_U443_ORIG_BUILD_SHELL(self,*args,**kwargs)
    _u443_apply_ttk_skin(self)
    try: self.after_idle(lambda:_u443_bind_hover_glow(self,self))
    except Exception: pass
    return result
AppV43._build_shell = _u443_build_shell_skin

# Render different dashboard treatments: duotone, scanlines, contrasting card frames and alternate header treatments.
def _u443_skin_dashboard_image(app):
    try:
        from PIL import Image as _I, ImageOps as _IO, ImageEnhance as _IE, ImageDraw as _ID
        base=app._load_reference_base()
        if base is None: return None
        t=app.colors(); style=t.get("_image_style","neon")
        key=(int(app.theme_id),base.size)
        cache=getattr(app,"_u443_skin_image_cache",{})
        if key in cache: return cache[key]
        im=base.convert("RGB")
        gray=_IO.autocontrast(_IO.grayscale(im))
        if style=="matrix":
            im=_IO.colorize(gray,black="#020b05",mid="#12451c",white="#90ffab")
        elif style=="ice":
            im=_IO.colorize(gray,black="#071b36",mid="#6faddb",white="#f0fbff")
        elif style=="hologram":
            im=_IO.colorize(gray,black="#140626",mid="#542c85",white="#e5d7ff")
        elif style=="redline":
            im=_IO.colorize(gray,black="#16060a",mid="#7b1024",white="#ffb2bd")
        elif style=="amber":
            im=_IO.colorize(gray,black="#1b1104",mid="#845018",white="#ffe5a0")
        elif style=="steel":
            im=_IO.colorize(gray,black="#06121c",mid="#526a7d",white="#edf5fc")
        elif style=="retro":
            im=_IO.colorize(gray,black="#1b0b02",mid="#8a3d08",white="#ffdf9a")
        elif style=="carbon":
            im=_IE.Contrast(_IE.Color(im).enhance(0.22)).enhance(1.28)
            im=_I.blend(im,_I.new("RGB",im.size,"#101720"),0.18)
        elif style=="aurora":
            im=_I.blend(_IE.Color(im).enhance(1.3),_I.new("RGB",im.size,t.get("accent2","#55d8ff")),0.14)
        elif style=="glass":
            im=_I.blend(_IE.Contrast(im).enhance(1.35),_I.new("RGB",im.size,"#9adfff"),0.19)
        elif style=="wave":
            im=_I.blend(_IO.colorize(gray,black="#071427",mid=t.get("accent","#1aa7ff"),white="#e7f8ff"),_I.new("RGB",im.size,t.get("accent2","#55d8ff")),0.11)
        elif style=="blueprint":
            im=_IO.colorize(gray,black="#06152c",mid="#174775",white="#c3eaff")
        elif style=="plasma":
            im=_IO.colorize(gray,black="#10051d",mid="#6f238c",white="#ffd7ff")
        elif style=="angular":
            im=_I.blend(_IE.Contrast(im).enhance(1.18),_I.new("RGB",im.size,t.get("accent","#1aa7ff")),0.13)
        else:
            im=_I.blend(_IE.Color(im).enhance(1.18),_I.new("RGB",im.size,t.get("accent2","#55d8ff")),0.12)
        rgba=im.convert("RGBA")
        overlay=_I.new("RGBA",rgba.size,(0,0,0,0))
        d=_ID.Draw(overlay,"RGBA")
        accent=tuple(int(t.get("accent","#1aa7ff").lstrip("#")[i:i+2],16) for i in (0,2,4))
        accent2=tuple(int(t.get("accent2","#55d8ff").lstrip("#")[i:i+2],16) for i in (0,2,4))
        boxes=[(263,78,963,219),(972,78,1567,219),(263,221,1567,290),(257,386,831,539),(836,386,1567,539),(255,661,666,911),(671,661,1237,911),(1242,661,1567,911)]
        sid=int(t.get("_skin_id",0)); shape=t.get("_skin_shape","rounded")
        texture=t.get("_skin_texture","grid"); layout=t.get("_skin_layout","sidebar")
        seed=int(t.get("_skin_visual_seed",sid)); step=max(14,int(t.get("_skin_spacing",8))*4)
        bg_alpha=max(8,min(52,int(t.get("_skin_background_alpha",24))))
        for idx,box in enumerate(boxes):
            x0,y0,x1,y1=box
            cut=5+((seed+idx*7)%22)
            width=1+((seed+idx)%3)
            if shape in ("angular","notched","hex","technical"):
                if shape=="hex":
                    points=[x0+cut,y0,(x0+x1)//2,y0+cut,x1-cut,y0,x1,y0+cut,(x0+x1)//2,y1-cut,x0,y1-cut]
                else:
                    points=[x0+cut,y0,x1-cut,y0,x1,y0+cut,x1,y1-cut,x1-cut,y1,x0+cut,y1,x0,y1-cut,x0,y0+cut]
                d.line(points+[points[0]],fill=(*accent2,210),width=width+1,joint="curve")
                if shape=="technical":
                    d.line((x0+cut+4,y0+4,x0+min(x1-x0-4,cut+90),y0+4),fill=(*accent,220),width=2)
                for xx,yy in ((x0+5,y0+5),(x1-5,y0+5),(x0+5,y1-5),(x1-5,y1-5)):
                    d.ellipse((xx-2,yy-2,xx+2,yy+2),fill=(*accent,210))
            elif shape in ("corners","circuit"):
                arm=max(12,min(42,(x1-x0)//5))
                for ax,ay,dx,dy in ((x0,y0,1,1),(x1,y0,-1,1),(x0,y1,1,-1),(x1,y1,-1,-1)):
                    d.line((ax,ay,ax+dx*arm,ay),fill=(*accent2,220),width=width+1)
                    d.line((ax,ay,ax,ay+dy*arm),fill=(*accent2,220),width=width+1)
                if shape=="circuit":
                    d.line((x0+arm,y0+5,(x0+x1)//2,y0+5,(x0+x1)//2,y0+14),fill=(*accent,bg_alpha+75),width=2)
            elif shape in ("double","bevel","inset","outline"):
                d.rectangle(box,outline=(*accent,210),width=width)
                inset=3+seed%7
                d.rectangle((x0+inset,y0+inset,x1-inset,y1-inset),outline=(*accent2,120+seed%65),width=1)
                if shape=="bevel":
                    d.line((x0+inset,y0+inset,x1-inset,y0+inset),fill=(255,255,255,90),width=1)
                    d.line((x0+inset,y1-inset,x1-inset,y1-inset),fill=(0,0,0,100),width=1)
            elif shape=="minimal":
                d.line((x0,y0,x1,y0),fill=(*accent2,220),width=width+1)
                d.line((x0,y0,x0,y1),fill=(*accent,160),width=1)
            elif shape=="glass":
                radius=max(3,int(t.get("_skin_corner",12)))
                d.rounded_rectangle(box,radius=radius,outline=(*accent2,180),width=width)
                d.line((x0+radius,y0+2,x1-radius,y0+2),fill=(*accent,120),width=1)
            elif style in ("matrix","retro"):
                d.rectangle(box,outline=(*accent,220),width=2)
                d.line((x0+8,y0+5,x0+min(100,x1-x0-8),y0+5),fill=(*accent2,245),width=2)
            elif style=="carbon":
                d.rectangle(box,outline=(165,185,205,180),width=1)
                d.line((x0+7,y0+7,x1-7,y0+7),fill=(235,245,255,70),width=1)
            else:
                radius=max(3,int(t.get("_skin_corner",12)))
                d.rounded_rectangle(box,radius=radius,outline=(*accent,150+seed%70),width=width)
                if idx%2==sid%2:
                    d.line((x0+radius,y0+2,x1-radius,y0+2),fill=(*accent2,90+seed%90),width=1)
        # A per-skin texture layer makes the dashboard composition distinct beyond hue: grid, circuit, radial, dots, waves, hex, dashes and more.
        start_x=255+(seed%step); start_y=70+((seed//7)%step); tex_col=(*accent2,bg_alpha)
        if texture=="grid":
            for xx in range(start_x,rgba.width,step): d.line((xx,72,xx,rgba.height-8),fill=tex_col,width=1)
            for yy in range(start_y,rgba.height,step): d.line((255,yy,rgba.width-8,yy),fill=tex_col,width=1)
        elif texture=="diagonal":
            for offset in range(-rgba.height,rgba.width,step):
                d.line((max(255,offset),max(70,-offset),min(rgba.width-8,offset+rgba.height),min(rgba.height-8,rgba.height-offset)),fill=tex_col,width=1)
        elif texture=="dots":
            dot=1+(seed%3)
            for yy in range(start_y,rgba.height-8,step):
                for xx in range(start_x,rgba.width-8,step):
                    d.ellipse((xx-dot,yy-dot,xx+dot,yy+dot),fill=tex_col)
        elif texture=="circuit":
            for yy in range(start_y,rgba.height-12,step*2):
                xx=start_x
                while xx<rgba.width-24:
                    span=min(18+((xx+yy+seed)%50),rgba.width-8-xx)
                    d.line((xx,yy,xx+span,yy),fill=tex_col,width=1)
                    d.line((xx+span,yy,xx+span,yy+max(4,step//2)),fill=tex_col,width=1)
                    d.ellipse((xx+span-2,yy+max(4,step//2)-2,xx+span+2,yy+max(4,step//2)+2),outline=tex_col,width=1)
                    xx+=max(20,span+step)
        elif texture=="wave":
            import math as _u443_math
            for row in range(0,5):
                pts=[]
                for xx in range(255,rgba.width-8,8):
                    yy=start_y+row*step*2+int(_u443_math.sin((xx+seed+row*31)/(18.0+seed%13))*max(2,step//3))
                    pts.extend((xx,yy))
                if len(pts)>=4:d.line(pts,fill=tex_col,width=1)
        elif texture=="radial" or texture=="rings":
            cx=1120+(seed%140)-70;cy=450+((seed//3)%80)-40
            maxrad=min(rgba.width-cx-8,cy-75,rgba.height-cy-8)
            for radius in range(step,max(1,maxrad),step):
                if texture=="rings": d.ellipse((cx-radius,cy-radius,cx+radius,cy+radius),outline=tex_col,width=1)
                else: d.arc((cx-radius,cy-radius,cx+radius,cy+radius),start=(seed%170),end=180+(seed%160),fill=tex_col,width=1)
        elif texture=="hex":
            hexw=step;hexh=max(10,int(step*0.86))
            row=0
            for yy in range(start_y,rgba.height-hexh,hexh):
                row+=1
                for xx in range(start_x+(row%2)*(hexw//2),rgba.width-hexw,hexw):
                    pts=[xx+hexw//4,yy,xx+3*hexw//4,yy,xx+hexw,yy+hexh//2,xx+3*hexw//4,yy+hexh,xx+hexw//4,yy+hexh,xx,yy+hexh//2]
                    d.line(pts+[pts[0],pts[1]],fill=tex_col,width=1)
        elif texture=="scanline" or texture=="dash":
            dash=step if texture=="dash" else 2
            for yy in range(start_y,rgba.height-4,dash):
                d.line((255,yy,rgba.width-8,yy),fill=tex_col,width=1)
        elif texture=="matrix":
            for col in range(start_x,rgba.width-8,step):
                for k in range(2+(seed+col)%7):
                    yy=start_y+k*(4+seed%5)
                    if yy<rgba.height-8:d.line((col,yy,col,yy+2+((seed+k)%7)),fill=tex_col,width=1)
        elif texture=="crosshair":
            for yy in range(start_y,rgba.height-8,step*2):
                for xx in range(start_x,rgba.width-8,step*2):
                    arm=max(2,step//7);d.line((xx-arm,yy,xx+arm,yy),fill=tex_col,width=1);d.line((xx,yy-arm,xx,yy+arm),fill=tex_col,width=1)
        else: # stars / technical markers
            for yy in range(start_y,rgba.height-8,step):
                for xx in range(start_x,rgba.width-8,step):
                    arm=2+(seed+xx+yy)%4
                    d.line((xx-arm,yy,xx+arm,yy),fill=tex_col,width=1)
                    d.line((xx,yy-arm,xx,yy+arm),fill=tex_col,width=1)
        if t.get("_scanlines"):
            for yy in range(2,rgba.height,3+(sid%4)): d.line((0,yy,rgba.width,yy),fill=(0,0,0,22+sid%22),width=1)
        if layout=="topbar":
            d.rectangle((255,0,rgba.width-1,71),fill=(*accent,bg_alpha))
            d.line((255,70,rgba.width-1,70),fill=(*accent2,200),width=2+sid%3)
        elif layout=="terminal":
            for xx in range(260,rgba.width,18+(sid%28)): d.line((xx,75,xx,rgba.height-2),fill=(*accent,16+sid%22),width=1)
        elif layout=="split":
            split_x=880+(sid%81)-40
            d.line((split_x,72,split_x,rgba.height-8),fill=(*accent2,130),width=2)
            d.line((split_x+4,72,split_x+4,rgba.height-8),fill=(*accent,bg_alpha),width=1)
        elif layout=="radial":
            d.ellipse((900+(sid%70),230,1450+(sid%70),780),outline=(*accent2,bg_alpha+30),width=2)
            d.ellipse((980+(sid%70),310,1370+(sid%70),700),outline=(*accent,bg_alpha),width=1)
        elif layout=="dock":
            d.rectangle((255,rgba.height-72,rgba.width-1,rgba.height-1),fill=(*accent,bg_alpha))
            d.line((255,rgba.height-73,rgba.width-1,rgba.height-73),fill=(*accent2,200),width=3)
        elif layout=="instrument":
            for j in range(3):
                cx=305+j*150;cy=480+(sid%31)
                d.ellipse((cx-42,cy-42,cx+42,cy+42),outline=(*accent2,120+sid%90),width=2)
                d.arc((cx-33,cy-33,cx+33,cy+33),start=190,end=350,fill=(*accent,bg_alpha+30),width=3)
        elif layout=="wide":
            d.rectangle((255,75,rgba.width-8,300),outline=(*accent2,bg_alpha+45),width=2)
            d.line((255,302,rgba.width-8,302),fill=(*accent,120+sid%80),width=2)
        elif layout=="stacked":
            for yy in (300,470,640,810):
                if yy<rgba.height-10:d.line((255,yy,rgba.width-8,yy),fill=(*accent2,bg_alpha),width=2)
        out=_I.alpha_composite(rgba,overlay).convert("RGB")
        if len(cache)>24: cache={}
        cache[key]=out
        app._u443_skin_image_cache=cache
        return out
    except Exception:
        return None

_U443_ORIG_THEME_REFERENCE = AppV43._theme_reference
def _u443_theme_reference_skin(self):
    im=_u443_skin_dashboard_image(self)
    if im is not None: return im
    return _U443_ORIG_THEME_REFERENCE(self)
AppV43._theme_reference = _u443_theme_reference_skin

# The dashboard uses native Tk buttons containing image crops. The hover overlay is baked into each crop so it remains visible even above the image.
def _u443_bind_dashboard_button_hover(app):
    try:
        from PIL import Image as _I, ImageDraw as _ID, ImageEnhance as _IE
        image=getattr(app,"_dash_img",None)
        controls=getattr(app,"_dash_control_widgets",{}) or {}
        specs=getattr(app,"_dash_control_specs",[]) or []
        if image is None or not controls or not specs: return
        token=(int(app.theme_id),id(image),image.size,tuple(sorted(controls.keys())))
        if getattr(app,"_u443_dashboard_hover_token",None)!=token:
            app._u443_dashboard_hover_photos={}
            app._u443_dashboard_base_photos=dict(getattr(app,"_dash_control_photos",{}) or {})
            t=app.colors(); ac=t.get("accent2","#55d8ff"); ac_rgb=tuple(int(ac.lstrip("#")[i:i+2],16) for i in (0,2,4))
            for key,rect,_action in specs:
                btn=controls.get(key)
                if btn is None: continue
                x0,y0,x1,y1=rect; sx=image.width/1586.0; sy=image.height/960.0
                ix0=max(0,min(image.width-1,round(x0*sx))); iy0=max(0,min(image.height-1,round(y0*sy)))
                ix1=max(ix0+1,min(image.width,round(x1*sx))); iy1=max(iy0+1,min(image.height,round(y1*sy)))
                crop=image.crop((ix0,iy0,ix1,iy1))
                crop=_IE.Brightness(crop).enhance(1.24)
                crop=_IE.Color(crop).enhance(1.30)
                rgba=crop.convert("RGBA")
                halo=_I.new("RGBA",rgba.size,(0,0,0,0)); hd=_ID.Draw(halo)
                w,h=rgba.size; line=max(2,min(5,round(min(w,h)*0.055)))
                hd.rectangle((0,0,w-1,h-1),outline=(*ac_rgb,255),width=line)
                if w>8 and h>8: hd.rectangle((line+1,line+1,w-line-2,h-line-2),outline=(255,255,255,255),width=1)
                for inset,alpha in ((1,35),(2,22)):
                    hd.rectangle((inset,inset,w-1-inset,h-1-inset),outline=(*ac_rgb,alpha),width=1)
                app._u443_dashboard_hover_photos[key]=ImageTk.PhotoImage(_I.alpha_composite(rgba,halo),master=btn)
            app._u443_dashboard_hover_token=token
        for key,_rect,_action in specs:
            btn=controls.get(key)
            if btn is None or getattr(btn,"_u443_dashboard_hover_bound",False): continue
            try:
                def _enter(event,control_key=key,control=btn):
                    photo=(getattr(app,"_u443_dashboard_hover_photos",{}) or {}).get(control_key)
                    if photo is not None:
                        control.configure(image=photo,relief="solid",borderwidth=1,highlightthickness=2,
                                          highlightbackground=app.colors().get("accent2","#55d8ff"),
                                          highlightcolor=app.colors().get("accent2","#55d8ff"))
                    app._u443_hovered_dashboard_control=control_key
                def _leave(event,control_key=key,control=btn):
                    photo=(getattr(app,"_dash_control_photos",{}) or {}).get(control_key) or (getattr(app,"_u443_dashboard_base_photos",{}) or {}).get(control_key)
                    if photo is not None:
                        control.configure(image=photo,relief="flat",borderwidth=0,highlightthickness=0,
                                          highlightbackground=app.colors().get("bg","#07111f"),
                                          highlightcolor=app.colors().get("bg","#07111f"))
                    app._u443_hovered_dashboard_control=None
                btn.bind("<Enter>",_enter,add="+")
                btn.bind("<Leave>",_leave,add="+")
                btn._u443_dashboard_hover_bound=True
            except Exception: pass
    except Exception: pass

_U443_ORIG_INSTALL_DASHBOARD = AppV43._install_dashboard_controls
def _u443_install_dashboard_with_hover(self,*args,**kwargs):
    result=_U443_ORIG_INSTALL_DASHBOARD(self,*args,**kwargs)
    try: self.after_idle(lambda: (_u443_bind_dashboard_button_hover(self),_u443_bind_hover_glow(self,self)))
    except Exception: pass
    return result
AppV43._install_dashboard_controls = _u443_install_dashboard_with_hover

_U443_ORIG_CLEAR_ALL = AppV43.clear
def _u443_clear_all_with_hover(self,*args,**kwargs):
    result=_U443_ORIG_CLEAR_ALL(self,*args,**kwargs)
    try: self.after_idle(lambda:_u443_bind_hover_glow(self,self))
    except Exception: pass
    return result
AppV43.clear = _u443_clear_all_with_hover

# The theme preview changes navigation arrangement, panel silhouettes, density and charting—not only the color.
def _u443_draw_theme_preview(self,canvas):
    t=self.colors()
    try:
        from math import sin, cos, pi
        canvas.delete("all"); canvas.update_idletasks()
        w=max(660,canvas.winfo_width()); h=max(190,canvas.winfo_height())
        variant=int(t.get("_skin_variant",0)); layout=t.get("_skin_layout","sidebar"); relief=t.get("_panel_relief","flat")
        shape=t.get("_skin_shape","rounded"); chart=t.get("_skin_chart_style","line"); texture=t.get("_skin_texture","grid")
        density=int(t.get("_skin_density",0)); spacing=int(t.get("_skin_spacing",8)); scale=float(t.get("_font_scale",1.0))
        canvas.configure(bg=t["bg"])
        borderw=max(1,int(t.get("_panel_highlight",1)))
        canvas.create_rectangle(4,4,w-4,h-4,fill=t["bg"],outline=t["accent"],width=borderw)
        if texture in ("grid","blueprint","crosshair"):
            step=max(8,spacing*2)
            for xx in range(6+(variant%step),w-6,step):canvas.create_line(xx,6,xx,h-6,fill=t["panel"],width=1)
            for yy in range(6+((variant//5)%step),h-6,step):canvas.create_line(6,yy,w-6,yy,fill=t["panel"],width=1)
        elif texture in ("scanline","matrix","dash"):
            for yy in range(6,h-6,max(2,2+spacing//2)):canvas.create_line(6,yy,w-6,yy,fill=t["panel"],width=1)
        if layout=="topbar":
            canvas.create_rectangle(16,14,w-16,49,fill=t["panel"],outline=t["accent"],width=max(1,int(t.get("_panel_bd",0))))
            canvas.create_text(28,31,text="NAPRAWA PC / HARDWARE TEST PRO",fill=t["accent"],anchor="w",font=self.fnt(10,"bold"))
            for i,name in enumerate(("PULPIT","TESTY","RAPORTY","USTAWIENIA")):
                canvas.create_text(round(w*.56)+i*75,31,text=name,fill=t["accent2"] if i==0 else t["fg"],font=self.fnt(7,"bold"))
            main_x=16; y_cards=61
        elif layout=="terminal":
            navw=max(125,int(t.get("_skin_nav_width",145)))
            canvas.create_rectangle(16,14,navw,h-14,fill=t["panel"],outline=t["accent"],width=2)
            canvas.create_text(28,31,text="> SYSTEM / STATUS",fill=t["accent"],anchor="w",font=self.fnt(9,"bold"))
            for i,name in enumerate(("CPU","GPU","RAM","NVME","SECURITY")):
                canvas.create_text(30,53+i*22,text="[+] "+name,fill=t["accent2"] if i==0 else t["fg"],anchor="w",font=self.fnt(8,"normal"))
            main_x=navw+14; y_cards=71
        elif layout=="grid":
            main_x=16;y_cards=22
        elif layout=="wide":
            main_x=16;y_cards=64
        elif layout=="radial":
            main_x=16;y_cards=57
            cx=w-100;cy=h*.47
            for r in (24,38,52,66):
                canvas.create_oval(cx-r,cy-r,cx+r,cy+r,outline=t["accent2"] if r==38 else t["panel"],width=2 if r==38 else 1)
            canvas.create_line(cx-67,cy,cx+67,cy,fill=t["accent"],width=1)
            canvas.create_line(cx,cy-67,cx,cy+67,fill=t["accent"],width=1)
        elif layout=="instrument":
            navw=125
            canvas.create_rectangle(16,14,navw,h-14,fill=t["panel"],outline=t["accent"],width=2)
            for i in range(3):
                cy=55+i*53; r=17
                canvas.create_oval(37,cy-r,37+2*r,cy+r,outline=t["accent2"],width=2)
                canvas.create_line(37+r,cy,37+r+7,cy-7-i*2,fill=t["accent"],width=2)
            main_x=navw+12;y_cards=25
        elif layout=="split":
            main_x=16;y_cards=60
            split=round(w*.51)
            canvas.create_rectangle(16,14,split-6,h-14,fill=t["panel"],outline=t["accent"],width=1)
            canvas.create_rectangle(split+2,14,w-16,h-14,fill=t["bg"],outline=t["accent2"],width=1)
        elif layout=="compact":
            navw=max(82,int(t.get("_skin_nav_width",110)))
            canvas.create_rectangle(16,14,navw,h-14,fill=t["panel"],outline=t["accent"],width=1)
            for i,name in enumerate(("PC","CPU","GPU","RAM","SSD","TEST","LOG")):
                y=35+i*19;canvas.create_rectangle(21,y,navw-6,y+14,fill=t["accent"] if i==0 else t["card"],outline=t["panel"])
                canvas.create_text(28,y+7,text=name,fill=t["fg"],anchor="w",font=self.fnt(7,"bold"))
            main_x=navw+10;y_cards=37
        elif layout=="dock":
            main_x=16;y_cards=24
            dock_y=h-33
            for i,name in enumerate(("PULPIT","CPU","GPU","RAM","DYSKI","RAPORTY")):
                x=20+i*((w-40)//6)
                canvas.create_rectangle(x,dock_y,x+(w-40)//6-4,h-12,fill=t["panel"],outline=t["accent"],width=1)
                canvas.create_text(x+8,dock_y+9,text=name,fill=t["accent2"] if i==0 else t["fg"],anchor="w",font=self.fnt(7,"bold"))
        elif layout=="stacked":
            main_x=16;y_cards=25
            for i in range(3):
                yy=18+i*52
                canvas.create_rectangle(16,yy,w-16,yy+43,fill=t["panel"],outline=t["accent"],width=1)
                canvas.create_text(28,yy+12,text=("SYSTEM / HARDWARE","LIVE METRICS","TEST QUEUE")[i],fill=t["accent2"],anchor="w",font=self.fnt(8,"bold"))
        elif layout=="cards":
            main_x=16;y_cards=22
        elif layout=="hybrid":
            main_x=125;y_cards=48
            canvas.create_rectangle(16,14,112,h-14,fill=t["panel"],outline=t["accent"],width=1)
            for i in range(5):canvas.create_line(25,43+i*27,102,43+i*27,fill=t["accent2"] if i==0 else t["card"],width=3)
        else:
            navw=max(110,int(t.get("_skin_nav_width",145)))
            canvas.create_rectangle(16,14,navw,h-14,fill=t["panel"],outline=t["accent"],width=borderw)
            canvas.create_text(27,32,text="NAPRAWA PC",fill=t["accent"],anchor="w",font=self.fnt(10,"bold"))
            for i,name in enumerate(("PULPIT","CPU","GPU","RAM","DYSK","TESTY","RAPORTY")):
                y=55+i*22
                canvas.create_rectangle(22,y,navw-10,y+17,fill=t["accent"] if i==0 else t["card"],outline=t["accent2"] if i==0 else t["panel"])
                canvas.create_text(30,y+8,text=name,fill="#ffffff" if i==0 else t["fg"],anchor="w",font=self.fnt(7,"bold"))
            main_x=navw+10;y_cards=71
        available=max(360,w-main_x-18); hero_h=max(34,int(h*(.16+(variant%5)*.015)))
        if layout not in ("topbar","grid","cards","radial","dock","stacked","split","compact"):
            canvas.create_rectangle(main_x,15,main_x+available,15+hero_h,fill=t["panel"],outline=t["accent"],width=max(1,int(t.get("_panel_bd",0))+1))
            canvas.create_text(main_x+12,28,text=t.get("_skin_family","DIAGNOSTYKA"),fill=t["accent"],anchor="w",font=self.fnt(10,"bold"))
            canvas.create_text(main_x+12,45,text="MONITORING NA ŻYWO • TESTY • WYNIKI",fill=t["muted"],anchor="w",font=self.fnt(7,"bold"))
        count=max(3,min(6,int(t.get("_skin_card_count",3+(variant%4)))))
        gap=max(4,min(13,spacing)); cw=max(48,(available-gap*(count-1))//count)
        for i in range(count):
            if layout in ("grid","cards","stacked"):
                row=i//3; col=i%3
                x=main_x+col*(cw+gap); y=y_cards+row*(49+gap)
            else:
                x=main_x+i*(cw+gap); y=y_cards
            x1=min(w-17,x+cw); y1=min(h-14,y+43+((variant+i)%3)*5)
            if shape in ("angular","notched","hex","technical") or layout=="grid":
                cut=min(8,max(3,spacing//2))
                pts=[x+cut,y,x1-cut,y,x1,y+cut,x1,y1-cut,x1-cut,y1,x+cut,y1,x,y1-cut,x,y+cut]
                canvas.create_polygon(pts,fill=t["card"] if layout=="grid" else t["panel"],outline=t["accent"],width=1+variant%2)
                if shape=="technical":canvas.create_line(x+7,y+4,min(x1-6,x+35+variant%30),y+4,fill=t["accent2"],width=2)
            elif shape in ("double","bevel","inset") or relief in ("ridge","raised","groove"):
                canvas.create_rectangle(x,y,x1,y1,fill=t["panel"],outline=t["accent"],width=max(1,int(t.get("_panel_bd",0))+1))
                inset=2+variant%5
                if shape=="double":canvas.create_rectangle(x+inset,y+inset,x1-inset,y1-inset,outline=t["accent2"],width=1)
                else:canvas.create_line(x+3,y+3,x1-3,y+3,fill=t["accent2"],width=1)
            elif shape=="glass":
                canvas.create_oval(x,y,x1,y1,fill=t["panel"],outline=t["accent"],width=2)
            else:
                canvas.create_rectangle(x,y,x1,y1,fill=t["panel"],outline=t["accent"],width=1+variant%2)
            label=("CPU","GPU","RAM","SSD","VRAM","NET")[i%6]
            value=(12+i*13+variant*3)%100
            canvas.create_text(x+7,y+12,text=label,fill=t["accent"],anchor="w",font=self.fnt(7,"bold"))
            canvas.create_text((x+x1)//2,(y+y1)//2+4,text=f"{value:02d}%",fill=t["good"] if i%2==0 else t["fg"],font=self.fnt(max(10,round(14*scale)),"bold"))
        chart_y=min(h-15,y_cards+(2*(49+gap) if layout in ("grid","cards","stacked") else 53)+max(43,hero_h//2))
        if layout not in ("radial","dock","stacked"):
            canvas.create_rectangle(main_x,chart_y,w-18,h-14,fill=t["panel"],outline=t["accent"],width=max(1,int(t.get("_panel_bd",0))+1))
            for n in range(1,4):
                yy=chart_y+(h-chart_y-18)*n/4
                canvas.create_line(main_x+8,yy,w-25,yy,fill=t["card"],dash=(2,2+(variant%4)))
            points=[]
            for xx in range(main_x+10,w-25,6):
                phase=(xx-main_x)/(13+variant%23)+variant*.25
                yy=chart_y+int((h-chart_y-18)*(0.5+0.20*sin(phase)+0.10*sin(phase*0.43)))
                points.append((xx,yy))
            if chart=="bars":
                for idx,(xx,yy) in enumerate(points[::3]):
                    canvas.create_rectangle(xx,yy,xx+max(2,spacing//2),h-16,fill=t["accent2"] if idx%2 else t["accent"],outline="")
            elif chart=="area" and len(points)>1:
                canvas.create_polygon(points+[(points[-1][0],h-15),(points[0][0],h-15)],fill=t["panel"],outline=t["accent2"],width=2)
            elif chart in ("steps","spectrum","candles","dots","dual"):
                for idx,(xx,yy) in enumerate(points):
                    if chart=="dots":canvas.create_oval(xx-2,yy-2,xx+2,yy+2,fill=t["accent2"],outline="")
                    elif chart=="candles" and idx%3==0:canvas.create_line(xx,yy-4,xx,yy+6,fill=t["accent2"],width=2)
                    elif chart=="spectrum":canvas.create_rectangle(xx,yy,xx+2,h-18,fill=t["accent2"],outline="")
                    elif chart=="dual":canvas.create_line(xx,yy,xx,min(h-18,yy+8+int(4*sin(idx))),fill=t["good"],width=1)
                    else:
                        if idx>0:
                            prev=points[idx-1];canvas.create_line(prev[0],prev[1],xx,prev[1],fill=t["accent2"],width=2)
                            canvas.create_line(xx,prev[1],xx,yy,fill=t["accent2"],width=2)
            else:
                canvas.create_line(*[v for pt in points for v in pt],fill=t["accent2"],width=1+variant%3,smooth=True)
        canvas.create_text(main_x+10,h-22,text=f"SKÓRKA {self.theme_id}/125 • {t.get('_skin_family','STYL')} • {shape.upper()} / {layout.upper()} / {chart.upper()}",fill=t["fg"],anchor="w",font=self.fnt(8,"bold"))
    except Exception as exc:
        try: canvas.delete("all"); canvas.create_text(12,12,text=f"Błąd podglądu skórki: {exc}",fill=t.get("bad","#ff5063"),anchor="nw")
        except Exception: pass
AppV43.draw_theme_preview = _u443_draw_theme_preview

# _U443_THEME_PROFILE_ENRICH_V2 — make every legacy and generated theme safe for structured rendering.
if len(THEMES) < 125 or any(_u443_i not in THEMES for _u443_i in range(1,126)):
    raise RuntimeError(f"Theme profile restore requires ids 1..125; found {len(THEMES)} entries")
_U443_PROFILE_LAYOUTS_V2 = ("sidebar","topbar","grid","terminal","split","compact","wide","instrument","radial","stacked","cards","dock","hybrid")
_U443_PROFILE_SHAPES_V2 = ("angular","rounded","bevel","double","corners","notched","outline","inset","circuit","hex","technical","minimal","glass")
_U443_PROFILE_TEXTURES_V2 = ("grid","diagonal","dots","circuit","wave","radial","hex","scanline","dash","matrix","crosshair","rings","stars")
_U443_PROFILE_CHARTS_V2 = ("line","area","bars","steps","spectrum","radial","wave","candles","dots","dual")
_U443_PROFILE_FONTS_V2 = ("Segoe UI","Bahnschrift","Consolas","Arial","Georgia","Courier New","Trebuchet MS","Tahoma","Verdana","Calibri","Cambria","Lucida Console")
_U443_PROFILE_PANEL_RELIEFS_V2 = ("flat","groove","solid","ridge","raised","sunken")
_U443_PROFILE_BUTTON_RELIEFS_V2 = ("flat","raised","groove","ridge","solid","sunken")
_U443_PROFILE_IMAGE_STYLES_V2 = ("neon","carbon","angular","matrix","ice","hologram","redline","amber","steel","retro","aurora","glass","wave","blueprint","plasma")
_U443_PROFILE_PANEL_FILLS_V2 = ("panel","card","panel","bg","card")
_U443_PROFILE_BORDER_MODES_V2 = ("line","double","corners","notched","dots")
for _u443_tid_v2 in range(1,126):
    _u443_n_v2 = _u443_tid_v2 - 1
    _u443_theme_v2 = THEMES[_u443_tid_v2]
    _u443_layout_v2 = _U443_PROFILE_LAYOUTS_V2[(_u443_n_v2*7 + _u443_n_v2//11) % len(_U443_PROFILE_LAYOUTS_V2)]
    _u443_shape_v2 = _U443_PROFILE_SHAPES_V2[(_u443_n_v2*5 + _u443_n_v2//13) % len(_U443_PROFILE_SHAPES_V2)]
    _u443_texture_v2 = _U443_PROFILE_TEXTURES_V2[(_u443_n_v2*7 + _u443_n_v2//9) % len(_U443_PROFILE_TEXTURES_V2)]
    _u443_chart_v2 = _U443_PROFILE_CHARTS_V2[(_u443_n_v2*3 + _u443_n_v2//7) % len(_U443_PROFILE_CHARTS_V2)]
    _u443_theme_v2["_skin_variant"] = _u443_n_v2
    _u443_theme_v2["_skin_id"] = _u443_n_v2
    _u443_theme_v2["_skin_layout"] = _u443_layout_v2
    _u443_theme_v2["_skin_shape"] = _u443_shape_v2
    _u443_theme_v2["_skin_texture"] = _u443_texture_v2
    _u443_theme_v2["_skin_chart_style"] = _u443_chart_v2
    _u443_theme_v2["_panel_relief"] = _U443_PROFILE_PANEL_RELIEFS_V2[(_u443_n_v2*5 + _u443_n_v2//4) % len(_U443_PROFILE_PANEL_RELIEFS_V2)]
    _u443_theme_v2["_panel_bd"] = _u443_n_v2 % 4
    _u443_theme_v2["_panel_highlight"] = 1 + (_u443_n_v2 % 4)
    _u443_theme_v2["_button_relief"] = _U443_PROFILE_BUTTON_RELIEFS_V2[(_u443_n_v2*3 + _u443_n_v2//5) % len(_U443_PROFILE_BUTTON_RELIEFS_V2)]
    _u443_theme_v2["_button_overrelief"] = _U443_PROFILE_BUTTON_RELIEFS_V2[(_u443_n_v2*5 + 1) % len(_U443_PROFILE_BUTTON_RELIEFS_V2)]
    _u443_theme_v2["_button_bd"] = _u443_n_v2 % 3
    _u443_theme_v2["_font_family"] = _U443_PROFILE_FONTS_V2[(_u443_n_v2*5 + _u443_n_v2//13) % len(_U443_PROFILE_FONTS_V2)]
    _u443_theme_v2["_font_scale"] = round(0.86 + (_u443_n_v2 % 13)*0.024, 3)
    _u443_theme_v2["_font_slant"] = "italic" if _u443_n_v2 % 9 == 0 else "roman"
    _u443_theme_v2["_font_underline"] = _u443_n_v2 % 19 == 0
    _u443_theme_v2["_image_style"] = _U443_PROFILE_IMAGE_STYLES_V2[(_u443_n_v2*5 + _u443_n_v2//9) % len(_U443_PROFILE_IMAGE_STYLES_V2)]
    _u443_theme_v2["_scanlines"] = (_u443_n_v2 % 5 == 0) or _u443_texture_v2 == "scanline"
    _u443_theme_v2["_skin_density"] = _u443_n_v2 % 5
    _u443_theme_v2["_skin_spacing"] = 4 + (_u443_n_v2 % 9)
    _u443_theme_v2["_skin_corner"] = 2 + ((_u443_n_v2*7) % 22)
    _u443_theme_v2["_skin_nav_width"] = 92 + ((_u443_n_v2*5) % 83)
    _u443_theme_v2["_skin_card_count"] = 3 + (_u443_n_v2 % 4)
    _u443_theme_v2["_skin_chart_variant"] = _u443_n_v2 % len(_U443_PROFILE_CHARTS_V2)
    _u443_theme_v2["_skin_panel_fill"] = _U443_PROFILE_PANEL_FILLS_V2[(_u443_n_v2//3) % len(_U443_PROFILE_PANEL_FILLS_V2)]
    _u443_theme_v2["_skin_button_padx"] = 4 + ((_u443_n_v2*3) % 9)
    _u443_theme_v2["_skin_button_pady"] = 2 + ((_u443_n_v2*5) % 7)
    _u443_theme_v2["_skin_border_mode"] = _U443_PROFILE_BORDER_MODES_V2[_u443_n_v2 % len(_U443_PROFILE_BORDER_MODES_V2)]
    _u443_theme_v2["_skin_background_alpha"] = 12 + ((_u443_n_v2*7) % 34)
    _u443_theme_v2["_skin_visual_seed"] = (_u443_n_v2*7919 + 104729) % 1000003
    if not str(_u443_theme_v2.get("_skin_family", "")).endswith(f"{_u443_tid_v2:03d}"):
        _u443_theme_v2["_skin_family"] = f"STRUCTURED / {_u443_layout_v2.upper()} / {_u443_shape_v2.upper()} / {_u443_tid_v2:03d}"
# Validate profile uniqueness before exposing the theme catalog.
_U443_PROFILE_FIELDS_V2 = ("_skin_layout","_skin_shape","_skin_texture","_skin_chart_style","_panel_relief","_panel_bd","_button_relief","_button_bd","_font_family","_font_scale","_skin_density","_skin_spacing","_skin_card_count","_skin_border_mode")
_U443_PROFILE_SIGNATURES_V2 = {tuple(THEMES[_u443_i][_u443_field] for _u443_field in _U443_PROFILE_FIELDS_V2) for _u443_i in range(1,126)}
if len(_U443_PROFILE_SIGNATURES_V2) != 125:
    raise RuntimeError(f"Structured theme profiles must be unique: {len(_U443_PROFILE_SIGNATURES_V2)}/125")

def _u443_selftest_visual_skins():
    assert len(THEMES)>=125,len(THEMES)
    assert len(set(THEMES[i]["name"] for i in range(1,126)))==125
    required=("name","bg","panel","card","fg","muted","accent","accent2","good","warn","bad","_skin_family","_skin_id","_panel_relief","_button_relief","_font_family","_image_style","_skin_layout")
    assert all(all(k in THEMES[i] for k in required) for i in range(1,126))
    design_fields=("_skin_layout","_skin_shape","_skin_texture","_skin_chart_style","_panel_relief","_panel_bd","_button_relief","_button_bd","_font_family","_font_scale","_skin_density","_skin_spacing","_skin_card_count","_skin_border_mode")
    signatures={tuple(THEMES[i][field] for field in design_fields) for i in range(1,126)}
    assert len(signatures)==125, f"Każda skórka musi mieć własny profil strukturalny: {len(signatures)}"
    for i in range(1,126):
        assert THEMES[i]["_skin_variant"]==i-1
        assert THEMES[i]["_skin_family"].endswith(f"{i:03d}")
    assert len(set(THEMES[i]["_skin_layout"] for i in range(1,126)))>=10
    assert len(set(THEMES[i]["_skin_shape"] for i in range(1,126)))>=10
    assert len(set(THEMES[i]["_skin_chart_style"] for i in range(1,126)))>=8
    assert len(set(THEMES[i]["_font_family"] for i in range(1,126)))>=10
    assert callable(_u443_bind_dashboard_button_hover)
    assert callable(AppV43.panel) and callable(AppV43.make_button)
    assert callable(AppV43._theme_reference)
    assert callable(AppV43.draw_theme_preview)
    print("[OK] 125 distinct skin names")
    print("[OK] 125 unique structural profiles: layout, shape, texture, chart, typography, density, spacing, buttons and panels")
    print("[OK] dedicated hover image overlays for image-backed dashboard buttons")
    print("VISUAL_SKINS_AND_HOVER_OK")
def _u443_selftest_themes():
    _u443_selftest_visual_skins()
    assert len(THEMES)>=125,len(THEMES)
    assert all(i in THEMES for i in range(1,126))
    keys=("name","bg","panel","card","fg","muted","accent","accent2","good","warn","bad")
    assert all(all(k in THEMES[i] for k in keys) for i in range(1,126))
    print("[OK] 125 selectable themes; buttons and icon widgets have hover bindings")
    print("THEMES_125_HOVER_GLOW_OK")
def _u443_selftest_dispatch(flag):
    if flag=="--selftest-themes":
        _u443_selftest_themes()
    elif flag=="--selftest-antivirus":
        result=_u37_get_defender_status() if "_u37_get_defender_status" in globals() else _v4326_get_defender_status()
        assert isinstance(result,dict) and "DetectionAvailable" in result
        print("ANTIVIRUS_SELFTEST_OK")
    elif flag=="--selftest-update-flow":
        _u39_selftest_global()
        assert _u37_version_tuple("4.3.45")>_u37_version_tuple("4.3.44")
        print("UPDATE_FLOW_SELFTEST_OK")
    elif flag=="--selftest-launcher":
        assert "_U39_GLOBAL_MANIFEST_URL" in globals()
        assert callable(globals().get("_u39_confirm_downloaded"))
        print("LAUNCHER_SELFTEST_OK")
if __name__=="__main__" and any(f in sys.argv for f in ("--selftest-themes","--selftest-antivirus","--selftest-update-flow","--selftest-launcher")):
    for _f in ("--selftest-themes","--selftest-antivirus","--selftest-update-flow","--selftest-launcher"):
        if _f in sys.argv: _u443_selftest_dispatch(_f)
    raise SystemExit(0)
'@
    $canvasHover = @'
# _U443_CANVAS_HOVER — dashboard is image-backed, so highlight clickable hit rectangles.
def _u443_draw_dashboard_canvas_hover(app):
    try:
        canvas=getattr(app,"dash_canvas",None)
        if canvas is None or not canvas.winfo_exists(): return
        canvas.delete("_u443_canvas_hover")
        rect=getattr(app,"_u443_canvas_hover_rect",None)
        if not rect: return
        t=app.colors(); sx=max(1,canvas.winfo_width())/1586.0; sy=max(1,canvas.winfo_height())/960.0
        x0,y0,x1,y1=rect
        for pad,col,width in ((4,t.get("accent","#1aa7ff"),3),(1,t.get("accent2","#55d8ff"),2)):
            canvas.create_rectangle((x0-pad)*sx,(y0-pad)*sy,(x1+pad)*sx,(y1+pad)*sy,
                                    outline=col,width=width,tags="_u443_canvas_hover")
        canvas.create_line((x0+5)*sx,(y0+3)*sy,min(x0+34,x1-3)*sx,(y0+3)*sy,
                           fill="#ffffff",width=2,tags="_u443_canvas_hover")
    except Exception: pass

def _u443_dashboard_canvas_motion(app,event):
    try:
        canvas=getattr(app,"dash_canvas",None)
        if canvas is None or event.widget is not canvas: return
        if getattr(app,"current_view","dashboard")!="dashboard": return
        sx=max(1,canvas.winfo_width())/1586.0; sy=max(1,canvas.winfo_height())/960.0
        x=float(event.x)/sx; y=float(event.y)/sy
        hit=None
        specs_fn=globals().get("_v4319_dashboard_control_specs")
        specs=specs_fn(app) if callable(specs_fn) else []
        for spec in specs or []:
            if len(spec)<2 or len(spec[1])!=4: continue
            key,rect=spec[0],spec[1]
            x0,y0,x1,y1=rect
            if x0<=x<=x1 and y0<=y<=y1:
                hit=(str(key),tuple(rect)); break
        if hit is None:
            fallback=(
                ("PULPIT",(12,8,258,40)),("CPU",(12,142,242,180)),("GPU",(12,181,242,219)),
                ("RAM",(12,220,242,257)),("DYSK",(12,258,242,294)),("MATRYCA",(12,295,242,332)),
                ("ODSWIEZ",(1442,87,1556,126)),("START_TESTU",(875,861,1233,902)),
                ("USTAWIENIA",(760,43,875,73)),("RAPORT",(1125,922,1350,959))
            )
            for key,rect in fallback:
                x0,y0,x1,y1=rect
                if x0<=x<=x1 and y0<=y<=y1:
                    hit=(key,rect); break
        key=hit[0] if hit else None
        if key==getattr(app,"_u443_canvas_hover_key",None): return
        app._u443_canvas_hover_key=key
        app._u443_canvas_hover_rect=hit[1] if hit else None
        _u443_draw_dashboard_canvas_hover(app)
    except Exception: pass

def _u443_dashboard_canvas_leave(app,event=None):
    try:
        app._u443_canvas_hover_key=None
        app._u443_canvas_hover_rect=None
        _u443_draw_dashboard_canvas_hover(app)
    except Exception: pass

def _u443_bind_dashboard_canvas_hover(app):
    try:
        canvas=getattr(app,"dash_canvas",None)
        if canvas is None or not canvas.winfo_exists() or getattr(canvas,"_u443_canvas_hover_bound",False): return
        canvas.bind("<Motion>",lambda e,a=app:_u443_dashboard_canvas_motion(a,e),add="+")
        canvas.bind("<Leave>",lambda e,a=app:_u443_dashboard_canvas_leave(a,e),add="+")
        canvas._u443_canvas_hover_bound=True
        _u443_draw_dashboard_canvas_hover(app)
    except Exception: pass

'@
$canvasHoverMarker = '_U443_ORIG_INSTALL_DASHBOARD = AppV43._install_dashboard_controls'
if (!$hover.Contains($canvasHoverMarker)) { throw "Nie znaleziono punktu podłączenia podświetlania pulpitu." }
$hover = $hover.Replace($canvasHoverMarker, $canvasHover + [Environment]::NewLine + $canvasHoverMarker)
$hover = $hover.Replace('lambda: (_u443_bind_dashboard_button_hover(self),_u443_bind_hover_glow(self,self))','lambda: (_u443_bind_dashboard_button_hover(self),_u443_bind_dashboard_canvas_hover(self),_u443_bind_hover_glow(self,self))')
$hover = $hover.Replace('    assert callable(_u443_bind_dashboard_button_hover)','    assert callable(_u443_bind_dashboard_button_hover)' + [Environment]::NewLine + '    assert callable(_u443_bind_dashboard_canvas_hover) and callable(_u443_dashboard_canvas_motion)')
$main = '(?m)^if __name__ == "__main__":'
    if ($src -notmatch $main) { throw "Cannot find app entry point to install hover effects." }
    $src = [regex]::Replace($src,$main,[System.Text.RegularExpressions.MatchEvaluator]{
        param($m)
        return $hover + [Environment]::NewLine + $m.Value
    },1)
}
# _U55_INTEGRATED_SERVICE_REPAIR_CENTER — add service and Windows repair workspace to the existing Hardware Test PRO UI.
if (!$src.Contains("# _U55_INTEGRATED_SERVICE_REPAIR_CENTER")) {
$integration = @'
# _U55_INTEGRATED_SERVICE_REPAIR_CENTER
import base64 as _u55_base64
import hashlib as _u55_hashlib
import hmac as _u55_hmac
import json as _u55_json
import uuid as _u55_uuid
from tkinter import simpledialog as _u55_simpledialog
try:
    from cryptography.fernet import Fernet as _u55_Fernet
    from cryptography.hazmat.primitives import hashes as _u55_hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC as _u55_PBKDF2HMAC
except Exception:
    _u55_Fernet = _u55_hashes = _u55_PBKDF2HMAC = None

# Only a salted PBKDF2 verifier is embedded. The password is never stored in clear text.
_U55_AUTH_SALT_HEX = "ed3d25b1b698c7a0f6aacf6c26be9010"
_U55_AUTH_VERIFIER_HEX = "6d7bb55afdd8df9fccbaffe909b27a427654a54686afd7f87494709c159094d7"
_U55_STORE_SALT_HEX = "4ba031ee5be9863b484ba928153aab0e"
_U55_PBKDF2_ITERATIONS = 600000

def _u55_ticket_path():
    root = Path(os.environ.get("LOCALAPPDATA") or Path.home()) / "NaprawaPC" / "PrivateServiceData"
    return root / "zgloszenia.npcdata"

def _u55_verify_service_password(password):
    actual = _u55_hashlib.pbkdf2_hmac("sha256", str(password).encode("utf-8"), bytes.fromhex(_U55_AUTH_SALT_HEX), _U55_PBKDF2_ITERATIONS, dklen=32)
    return _u55_hmac.compare_digest(actual, bytes.fromhex(_U55_AUTH_VERIFIER_HEX))

def _u55_derive_service_key(password):
    if _u55_Fernet is None or _u55_PBKDF2HMAC is None or _u55_hashes is None:
        raise RuntimeError("Brakuje modułu szyfrowania cryptography. Zbuduj aplikację ponownie z pełnymi zależnościami.")
    kdf = _u55_PBKDF2HMAC(algorithm=_u55_hashes.SHA256(), length=32, salt=bytes.fromhex(_U55_STORE_SALT_HEX), iterations=_U55_PBKDF2_ITERATIONS)
    return _u55_base64.urlsafe_b64encode(kdf.derive(str(password).encode("utf-8")))

def _u55_load_tickets(self):
    key = getattr(self, "_u55_service_key", None)
    if not key:
        raise PermissionError("Panel zgłoszeń jest zablokowany.")
    path = _u55_ticket_path()
    if not path.exists():
        return []
    try:
        raw = _u55_Fernet(key).decrypt(path.read_bytes())
        value = _u55_json.loads(raw.decode("utf-8"))
        return value if isinstance(value, list) else []
    except Exception as exc:
        raise RuntimeError("Nie można odszyfrować pliku zgłoszeń. Hasło może być nieprawidłowe albo plik został uszkodzony.") from exc

def _u55_save_tickets(self, items):
    key = getattr(self, "_u55_service_key", None)
    if not key:
        raise PermissionError("Panel zgłoszeń jest zablokowany.")
    path = _u55_ticket_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    encrypted = _u55_Fernet(key).encrypt(_u55_json.dumps(items, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
    temp = path.with_name(path.name + "." + _u55_uuid.uuid4().hex + ".tmp")
    try:
        with open(temp, "xb") as stream:
            stream.write(encrypted)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, path)
    finally:
        try:
            temp.unlink(missing_ok=True)
        except Exception:
            pass

def _u55_render_private_tickets(self, parent):
    for child in parent.winfo_children():
        child.destroy()
    t = self.colors()
    key = getattr(self, "_u55_service_key", None)
    if not key:
        panel = self.panel(parent); panel.pack(fill="x", padx=12, pady=12)
        tk.Label(panel, text="PRYWATNE ZGŁOSZENIA SERWISOWE", bg=t["panel"], fg=t["accent"], font=self.fnt(13,"bold")).pack(anchor="w", padx=14, pady=(14,4))
        tk.Label(panel, text="Panel jest zabezpieczony hasłem. Zgłoszenia są szyfrowane lokalnie i nie są wysyłane do Internetu.", bg=t["panel"], fg=t["fg"], wraplength=1050, justify="left", font=self.fnt(9)).pack(anchor="w", padx=14, pady=4)
        tk.Label(panel, text="Dane są przechowywane w profilu bieżącego użytkownika Windows.", bg=t["panel"], fg=t["muted"], font=self.fnt(8)).pack(anchor="w", padx=14, pady=4)
        self.make_button(panel, "ODBLOKUJ PANEL ZGŁOSZEŃ", lambda:_u55_unlock_service_tickets(self, parent), "accent", side="left", ipady=8)
        return
    try:
        items = _u55_load_tickets(self)
    except Exception as exc:
        messagebox.showerror("Prywatne zgłoszenia", str(exc), parent=self)
        self._u55_service_key = None
        _u55_render_private_tickets(self, parent)
        return
    t = self.colors()
    top = tk.Frame(parent, bg=t["bg"]); top.pack(fill="x", padx=8, pady=(8,2))
    tk.Label(top, text="PRYWATNE ZGŁOSZENIA SERWISOWE", bg=t["bg"], fg=t["accent"], font=self.fnt(12,"bold")).pack(side="left", anchor="w")
    self.make_button(top, "WYLOGUJ", lambda:_u55_logout_service_tickets(self, parent), "card", side="right", ipady=5)
    form = self.panel(parent); form.pack(fill="x", padx=8, pady=5)
    labels = ("Tytuł zgłoszenia", "Klient", "Komputer / laptop", "Kontakt")
    vars_ = []
    row = tk.Frame(form, bg=t["panel"]); row.pack(fill="x", padx=8, pady=5)
    for label in labels:
        cell = tk.Frame(row, bg=t["panel"]); cell.pack(side="left", fill="x", expand=True, padx=4)
        tk.Label(cell, text=label, bg=t["panel"], fg=t["muted"], font=self.fnt(8)).pack(anchor="w")
        var = tk.StringVar(value="")
        tk.Entry(cell, textvariable=var, bg=t["card"], fg=t["fg"], insertbackground=t["fg"], relief="flat", font=self.fnt(9)).pack(fill="x", ipady=6)
        vars_.append(var)
    tk.Label(form, text="Opis usterki / ustaleń", bg=t["panel"], fg=t["muted"], font=self.fnt(8)).pack(anchor="w", padx=12, pady=(4,1))
    desc = tk.Text(form, height=3, bg=t["card"], fg=t["fg"], insertbackground=t["fg"], relief="flat", font=self.fnt(9), wrap="word")
    desc.pack(fill="x", padx=12, pady=(0,6))
    table_wrap = self.panel(parent); table_wrap.pack(fill="both", expand=True, padx=8, pady=5)
    columns = ("created", "title", "device", "customer", "status")
    tree = ttk.Treeview(table_wrap, columns=columns, show="headings", height=8)
    for col, title, width in (("created","Data",145),("title","Zgłoszenie",270),("device","Urządzenie",230),("customer","Klient",180),("status","Status",150)):
        tree.heading(col, text=title); tree.column(col, width=width, anchor="w")
    scroll = ttk.Scrollbar(table_wrap, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    tree.pack(side="left", fill="both", expand=True, padx=(6,0), pady=6); scroll.pack(side="right", fill="y", padx=(0,6), pady=6)
    self._u55_ticket_tree = tree
    def refresh():
        tree.delete(*tree.get_children())
        for item in reversed(_u55_load_tickets(self)):
            tree.insert("", "end", iid=str(item.get("id","")), values=(item.get("created",""),item.get("title",""),item.get("device",""),item.get("customer",""),item.get("status","Nowe")))
    def save_ticket():
        title = vars_[0].get().strip()
        device = vars_[2].get().strip()
        description = desc.get("1.0","end").strip()
        if not title or not device or not description:
            messagebox.showwarning("Zgłoszenie", "Uzupełnij tytuł, urządzenie oraz opis usterki.", parent=self); return
        all_items = _u55_load_tickets(self)
        all_items.insert(0, {"id":_u55_uuid.uuid4().hex,"created":datetime.now().strftime("%Y-%m-%d %H:%M"),"title":title,"customer":vars_[1].get().strip(),"device":device,"contact":vars_[3].get().strip(),"description":description,"status":"Nowe"})
        _u55_save_tickets(self, all_items)
        for var in vars_: var.set("")
        desc.delete("1.0","end"); refresh()
        self.queue_log("SERWIS ULTIMATE: zapisano prywatne zgłoszenie (szyfrowane).")
    def change_status():
        selected = tree.selection()
        if not selected: return
        items = _u55_load_tickets(self)
        target = next((item for item in items if str(item.get("id")) == str(selected[0])), None)
        if not target: return
        choice = _u55_simpledialog.askstring("Status zgłoszenia", "Podaj nowy status (Nowe / W toku / Oczekuje / Zakończone):", initialvalue=target.get("status","Nowe"), parent=self)
        if choice is None: return
        status_map = {"nowe":"Nowe","w toku":"W toku","oczekuje":"Oczekuje","zakończone":"Zakończone","zakonczone":"Zakończone"}
        normalized = choice.strip().casefold()
        if normalized not in status_map:
            messagebox.showwarning("Status", "Dostępne statusy: Nowe, W toku, Oczekuje, Zakończone.", parent=self); return
        target["status"] = status_map[normalized]
        _u55_save_tickets(self, items); refresh()
    def delete_ticket():
        selected = tree.selection()
        if not selected: return
        if not messagebox.askyesno("Usuń zgłoszenie", "Usunąć wybrane prywatne zgłoszenie?", parent=self): return
        all_items = [item for item in _u55_load_tickets(self) if str(item.get("id")) != str(selected[0])]
        _u55_save_tickets(self, all_items); refresh()
    actions = tk.Frame(form, bg=t["panel"]); actions.pack(fill="x", padx=8, pady=4)
    self.make_button(actions, "ZAPISZ ZGŁOSZENIE", save_ticket, "accent", side="left", ipady=5)
    self.make_button(actions, "ZMIEN STATUS", change_status, "card", side="left", ipady=5)
    self.make_button(actions, "USUŃ ZGŁOSZENIE", delete_ticket, "bad", side="left", ipady=5)
    refresh()

def _u55_unlock_service_tickets(self, parent):
    password = _u55_simpledialog.askstring("Autoryzacja serwisanta", "Podaj hasło do prywatnych zgłoszeń:", show="*", parent=self)
    if password is None:
        return
    if not _u55_verify_service_password(password):
        messagebox.showerror("Autoryzacja", "Nieprawidłowe hasło.", parent=self)
        self.queue_log("SERWIS ULTIMATE: odmowa dostępu do prywatnych zgłoszeń.")
        return
    try:
        self._u55_service_key = _u55_derive_service_key(password)
    except Exception as exc:
        messagebox.showerror("Szyfrowanie zgłoszeń", str(exc), parent=self); return
    _u55_render_private_tickets(self, parent)
    self.queue_log("SERWIS ULTIMATE: odblokowano prywatne zgłoszenia.")

def _u55_logout_service_tickets(self, parent):
    self._u55_service_key = None
    _u55_render_private_tickets(self, parent)
    self.queue_log("SERWIS ULTIMATE: wylogowano z prywatnych zgłoszeń.")

def _u55_run_repair(self, label, exe, args=(), timeout=3600):
    def job():
        if not is_windows():
            self.queue_log(f"{label}: ta operacja jest dostępna tylko w Windows."); return
        safe = re.sub(r"[^A-Za-z0-9_-]+", "_", str(label))[:48] or "naprawa"
        roots = [Path(os.environ.get("LOCALAPPDATA") or Path.home()) / "NaprawaPC" / "RepairReports", Path(tempfile.gettempdir()) / "NaprawaPC" / "RepairReports"]
        report_root = None
        for candidate in roots:
            try:
                candidate.mkdir(parents=True, exist_ok=True)
                probe = candidate / ("probe-" + _u55_uuid.uuid4().hex + ".tmp")
                with open(probe, "xb") as stream: stream.write(b"ok")
                probe.unlink()
                report_root = candidate
                break
            except Exception:
                try: probe.unlink(missing_ok=True)
                except Exception: pass
        if report_root is None:
            self.queue_log(f"{label}: brak zapisywalnego folderu raportów."); return
        token = datetime.now().strftime("%Y%m%d-%H%M%S") + "-" + _u55_uuid.uuid4().hex[:6]
        report = report_root / f"{token}-{safe}.log"
        if not is_admin():
            script = report_root / f"{token}-{safe}.ps1"
            status = report_root / f"{token}-{safe}.status"
            stdout = report_root / f"{token}-{safe}.out.txt"
            stderr = report_root / f"{token}-{safe}.err.txt"
            def q(value): return "'" + str(value).replace("'","''") + "'"
            arr = ",".join(q(x) for x in list(args))
            script_text = (
                "$ErrorActionPreference='Stop'\n"
                f"$exe={q(exe)}\n$procArgs=@({arr})\n"
                f"$stdout={q(stdout)}\n$stderr={q(stderr)}\n$status={q(status)}\n$report={q(report)}\n"
                "try { $p=Start-Process -FilePath $exe -ArgumentList $procArgs -PassThru -Wait -RedirectStandardOutput $stdout -RedirectStandardError $stderr; "
                "$out='';$err='';if(Test-Path -LiteralPath $stdout){$out=Get-Content -LiteralPath $stdout -Raw};if(Test-Path -LiteralPath $stderr){$err=Get-Content -LiteralPath $stderr -Raw}; "
                "('NARZĘDZIE='+$exe+[Environment]::NewLine+'ARGUMENTY='+($procArgs -join ' ')+[Environment]::NewLine+'KOD='+$p.ExitCode+[Environment]::NewLine+$out+[Environment]::NewLine+$err) | Set-Content -LiteralPath $report -Encoding UTF8; "
                "('DONE='+$p.ExitCode) | Set-Content -LiteralPath $status -Encoding UTF8 } "
                "catch { ('ERROR='+$_.Exception.Message) | Set-Content -LiteralPath $report -Encoding UTF8; 'DONE=1' | Set-Content -LiteralPath $status -Encoding UTF8; exit 1 }\n"
            )
            script.write_text(script_text, encoding="utf-8-sig")
            powershell = Path(os.environ.get("WINDIR",r"C:\Windows")) / "System32" / "WindowsPowerShell" / "v1.0" / "powershell.exe"
            if not powershell.is_file():
                self.queue_log(f"{label}: nie znaleziono Windows PowerShell."); return
            try:
                import ctypes as _u55_ctypes
                result = _u55_ctypes.windll.shell32.ShellExecuteW(None,"runas",str(powershell),f'-NoProfile -ExecutionPolicy Bypass -File "{script}"',str(report_root),0)
                if int(result or 0) <= 32:
                    self.queue_log(f"{label}: nie uruchomiono podwyższonego procesu (ShellExecuteW={result}); być może anulowano UAC."); return
            except Exception as exc:
                self.queue_log(f"{label}: nie udało się wyświetlić UAC: {type(exc).__name__}: {exc}"); return
            deadline = time.monotonic() + max(30, int(timeout))
            while time.monotonic() < deadline and not status.exists():
                time.sleep(0.75)
            if not status.exists():
                self.queue_log(f"{label}: przekroczono limit czasu. Raport: {report}")
                return
            try: status_text = status.read_text(encoding="utf-8",errors="replace").strip()
            except Exception: status_text = "DONE=?"
            try: output = report.read_text(encoding="utf-8",errors="replace")[-12000:]
            except Exception: output = status_text
            self.queue_log(f"{label}: zakończono ({status_text}). Raport: {report}")
            self.queue_log(output or "Narzędzie nie zwróciło tekstowego wyniku.")
        else:
            self.queue_log(f"{label}: START")
            out, err, rc = run_process([str(exe)] + list(args), timeout)
            output = (out or "") + ("\n" + err if err else "")
            try: report.write_text(f"NARZĘDZIE={exe}\nARGUMENTY={' '.join(args)}\nKOD={rc}\n\n{output}",encoding="utf-8",errors="replace")
            except Exception: pass
            self.queue_log(f"{label}: kod {rc}. Raport: {report}")
            self.queue_log(output[-12000:] if output else "Narzędzie nie zwróciło tekstowego wyniku.")
        self.queue_action(lambda:self._u39_set_update_status("Gotowe — zakończono: "+label) if hasattr(self,"_u39_set_update_status") else None)
    try:
        self.worker(job)
    except Exception as exc:
        messagebox.showerror("Naprawa Windows", f"{label}: {type(exc).__name__}: {exc}", parent=self)

def _u55_open_windows_tool(self, target):
    try:
        if str(target).startswith(("ms-settings:","windowsdefender:")):
            os.startfile(target)
        else:
            subprocess.Popen(str(target), shell=True, creationflags=getattr(subprocess,"CREATE_NO_WINDOW",0))
        self.queue_log("Narzędzie systemowe: " + str(target))
    except Exception as exc:
        messagebox.showerror("Narzędzia Windows", f"Nie udało się uruchomić {target}: {exc}", parent=self)

def _u107_detect_windows_installations():
    """Find Windows installations by marker files; never modify discovered volumes."""
    results=[]
    try:
        if os.name!="nt":
            return results
        current=Path(os.environ.get("WINDIR",r"C:\Windows")).resolve()
        import string as _u107_string
        for letter in _u107_string.ascii_uppercase:
            root=Path(letter+":\\")
            try:
                marker=root/"Windows"/"System32"/"config"/"SOFTWARE"
                if not marker.is_file():
                    continue
                try:
                    resolved=(root/"Windows").resolve()
                except Exception:
                    resolved=root/"Windows"
                try:
                    is_current=str(resolved).casefold()==str(current).casefold()
                except Exception:
                    is_current=False
                results.append({
                    "root":str(root),
                    "windows_dir":str(root/"Windows"),
                    "registry_hive":str(marker),
                    "is_current":is_current
                })
            except Exception:
                continue
    except Exception:
        return results
    return results

def _u107_repair_report_root():
    roots=[
        Path(os.environ.get("LOCALAPPDATA") or Path.home())/"NaprawaPC"/"RepairReports",
        Path(tempfile.gettempdir())/"NaprawaPC"/"RepairReports"
    ]
    for root in roots:
        try:
            root.mkdir(parents=True,exist_ok=True)
            probe=root/("probe-"+_u55_uuid.uuid4().hex+".tmp")
            with open(probe,"xb") as f:
                f.write(b"ok")
            probe.unlink()
            return root
        except Exception:
            try:probe.unlink(missing_ok=True)
            except Exception:pass
    raise OSError("Brak zapisywalnego folderu raportów naprawy.")

def _u107_confirm_and_run(self,label,exe,args,timeout=900,warning=None):
    text_value=(warning or "Operacja może zmienić stan systemu. Przed uruchomieniem przeczytaj nazwę i parametry.")
    if not messagebox.askyesno(label,text_value,parent=self):
        self.queue_log(label+": anulowano przez użytkownika.")
        return
    _u55_run_repair(self,label,exe,args,timeout)

def _u107_bcd_backup_path():
    root=_u107_repair_report_root()
    return str(root/("BCD-backup-"+_U66_datetime.now().strftime("%Y%m%d-%H%M%S")+"-"+_u55_uuid.uuid4().hex[:6]+".bcd"))

def _u107_open_windows_catalog(self):
    try:
        import webbrowser as _u107_webbrowser
        if not _u107_webbrowser.open("https://www.catalog.update.microsoft.com/"):
            raise RuntimeError("Nie udało się przekazać adresu do domyślnej przeglądarki.")
        self.queue_log("Katalog Microsoft Update: otwarto stronę pobierania sterowników i aktualizacji.")
    except Exception as exc:
        messagebox.showerror("Katalog Microsoft Update",f"{type(exc).__name__}: {exc}",parent=self)

def _u107_add_offline_tab(self,notebook,t,add_row,add_btn):
    offline=tk.Frame(notebook,bg=t["bg"])
    notebook.add(offline,text="OFFLINE / BCD / WINRE")
    intro=self.panel(offline);intro.pack(fill="x",padx=10,pady=8)
    tk.Label(intro,text="OFFLINE WINDOWS • ROZRUCH • ŚRODOWISKO ODZYSKIWANIA",
        bg=t["panel"],fg=t["accent"],font=self.fnt(11,"bold")).pack(anchor="w",padx=12,pady=(9,3))
    tk.Label(intro,text="Wykrywanie jest tylko odczytem. Skan DISM jest oddzielony od napraw. SFC /RestoreHealth i eksport BCD są opisane i wymagają osobnego potwierdzenia.",
        bg=t["panel"],fg=t["muted"],font=self.fnt(8),wraplength=1250,justify="left").pack(anchor="w",padx=12,pady=(0,8))
    select_frame=tk.Frame(offline,bg=t["bg"]);select_frame.pack(fill="x",padx=12,pady=(0,5))
    tk.Label(select_frame,text="Instalacja Windows:",bg=t["bg"],fg=t["fg"],font=self.fnt(9,"bold")).pack(side="left",padx=(0,8))
    choices=_u107_detect_windows_installations()
    labels=[f'{x["root"]}  {"(aktualny system)" if x["is_current"] else "(instalacja offline)"}' for x in choices]
    root_var=tk.StringVar(value=labels[0] if labels else "Nie znaleziono instalacji Windows")
    picker=ttk.Combobox(select_frame,textvariable=root_var,values=labels,state="readonly",width=42)
    picker.pack(side="left",padx=(0,6))
    state_label=tk.Label(select_frame,text=f"Wykryto: {len(choices)}",bg=t["bg"],fg=t["muted"],font=self.fnt(8))
    state_label.pack(side="left",padx=4)

    def selected():
        text_value=str(root_var.get() or "")
        for item,label in zip(choices,labels):
            if label==text_value:
                return item
        return None

    def refresh():
        nonlocal choices,labels
        choices=_u107_detect_windows_installations()
        labels=[f'{x["root"]}  {"(aktualny system)" if x["is_current"] else "(instalacja offline)"}' for x in choices]
        picker.configure(values=labels)
        root_var.set(labels[0] if labels else "Nie znaleziono instalacji Windows")
        state_label.config(text=f"Wykryto: {len(choices)}")
        self.queue_log("Offline Windows: wykryto "+str(len(choices))+" instalacji; tylko odczyt.")
    add_btn(select_frame,"WYKRYJ WINDOWS",refresh,"card")

    for specs in [
        [
            ("BCD / ROZRUCH — ODCZYT",lambda:_u55_run_repair(self,"BCDEdit /enum all","bcdedit.exe",["/enum","all"],120)),
            ("WINRE — STATUS",lambda:_u55_run_repair(self,"WinRE status","reagentc.exe",["/info"],120)),
            ("WINDOWS MEMORY DIAGNOSTIC",lambda:_u55_open_windows_tool(self,"mdsched.exe"))
        ],
        [
            ("ZAPISZ KOPIĘ BCD",lambda:_u107_confirm_and_run(self,"Eksport BCD",
                "bcdedit.exe",["/export",_u107_bcd_backup_path()],120,
                "Zostanie zapisany plik kopii magazynu BCD w folderze raportów. Ta operacja nie zmienia konfiguracji rozruchu. Kontynuować?")),
            ("PRZYWRACANIE SYSTEMU",lambda:_u55_open_windows_tool(self,"rstrui.exe")),
            ("OCHRONA SYSTEMU / PUNKTY",lambda:_u55_open_windows_tool(self,"SystemPropertiesProtection.exe"))
        ],
        [
            ("MICROSOFT UPDATE CATALOG",lambda:_u107_open_windows_catalog(self)),
            ("STEROWNIKI / WINDOWS UPDATE",lambda:_u55_open_windows_tool(self,"ms-settings:windowsupdate")),
            ("MENEDŻER URZĄDZEŃ",lambda:_u55_open_windows_tool(self,"devmgmt.msc"))
        ]
    ]:
        row=add_row(offline)
        for caption,action in specs:
            add_btn(row,caption,action,"card" if "UPDATE" in caption or "PRZYWRACANIE" in caption else "accent")

    scan=self.panel(offline);scan.pack(fill="x",padx=10,pady=8)
    tk.Label(scan,text="DIAGNOSTYKA OBRAZU OFFLINE — ODCZYT PRZED NAPRAWĄ",
        bg=t["panel"],fg=t["accent"],font=self.fnt(10,"bold")).pack(anchor="w",padx=12,pady=(9,3))
    tk.Label(scan,text="Wybierz wykrytą instalację. DISM /CheckHealth i /ScanHealth są skanami. /RestoreHealth oraz SFC /scannow mogą zmieniać pliki wybranego Windows i wymagają potwierdzenia.",
        bg=t["panel"],fg=t["muted"],font=self.fnt(8),wraplength=1250,justify="left").pack(anchor="w",padx=12,pady=(0,7))
    def dism_offline(mode):
        item=selected()
        if not item:
            messagebox.showwarning("Offline Windows","Najpierw wykryj i wybierz instalację Windows.",parent=self);return
        if item["is_current"] and mode=="RestoreHealth":
            messagebox.showwarning("Offline Windows","Wybrano aktualnie uruchomiony Windows. Ten przycisk obsługuje tylko obraz wskazany jako instalacja offline; użyj zakładki SYSTEM REPAIR PRO dla bieżącego systemu.",parent=self);return
        args=["/Image:"+item["root"],"/Cleanup-Image","/"+mode]
        if mode=="RestoreHealth":
            _u107_confirm_and_run(self,"DISM Offline /RestoreHealth","DISM.exe",args,5400,
                "To naprawa obrazu Windows na "+item["root"]+". Może zmienić pliki instalacji; potrzebne jest zasilanie i kopia danych. Kontynuować?")
        else:
            _u55_run_repair(self,"DISM Offline /"+mode,"DISM.exe",args,1800)
    def sfc_offline():
        item=selected()
        if not item:
            messagebox.showwarning("Offline Windows","Najpierw wykryj i wybierz instalację Windows.",parent=self);return
        if item["is_current"]:
            messagebox.showwarning("Offline Windows","Wybrano aktualnie uruchomiony system. Dla niego użyj SFC /SCANNOW w zakładce SYSTEM REPAIR PRO.",parent=self);return
        root=item["root"]
        args=["/scannow","/offbootdir="+root,"/offwindir="+str(Path(root)/"Windows")]
        _u107_confirm_and_run(self,"SFC Offline /scannow","sfc.exe",args,5400,
            "SFC spróbuje naprawić chronione pliki instalacji "+root+". Jeśli pliki rozruchowe są na osobnej partycji, /offbootdir może wymagać innego woluminu. Kontynuować?")
    row=add_row(offline)
    add_btn(row,"DISM OFFLINE /CHECKHEALTH",lambda:dism_offline("CheckHealth"),"card")
    add_btn(row,"DISM OFFLINE /SCANHEALTH",lambda:dism_offline("ScanHealth"),"card")
    add_btn(row,"DISM OFFLINE /RESTOREHEALTH",lambda:dism_offline("RestoreHealth"),"accent")
    add_btn(row,"SFC OFFLINE /SCANNOW",sfc_offline,"accent")
    return offline

def _u55_show_service_center(self):
    self.current_view = "SERVICE_CENTER"
    self.clear()
    t = self.colors()
    self.header_title.config(text="CENTRUM SERWISU ULTIMATE + SYSTEM REPAIR PRO")
    top = self.panel(self.content); top.pack(fill="x", padx=10, pady=(8,6))
    tk.Label(top, text="NAPRAWA PC — CENTRUM SERWISU I NAPRAW", bg=t["panel"], fg=t["accent"], font=self.fnt(14,"bold")).pack(anchor="w", padx=14, pady=(10,3))
    tk.Label(top, text="Diagnostyka sprzętu, narzędzia Windows i prywatne zgłoszenia serwisowe. Zgłoszenia są szyfrowane lokalnie.", bg=t["panel"], fg=t["muted"], font=self.fnt(9), wraplength=1250, justify="left").pack(anchor="w", padx=14, pady=(0,8))
    notebook = ttk.Notebook(self.content)
    notebook.pack(fill="both", expand=True, padx=10, pady=(0,8))
    service = tk.Frame(notebook, bg=t["bg"])
    repair = tk.Frame(notebook, bg=t["bg"])
    tickets = tk.Frame(notebook, bg=t["bg"])
    tools = tk.Frame(notebook, bg=t["bg"])
    notebook.add(service, text="SERWIS ULTIMATE")
    notebook.add(repair, text="SYSTEM REPAIR PRO")
    notebook.add(tickets, text="ZGŁOSZENIA PRYWATNE")
    notebook.add(tools, text="NARZĘDZIA SERWISOWE")
    def add_row(parent):
        row = tk.Frame(parent, bg=t["bg"]); row.pack(fill="x", padx=12, pady=4); return row
    def add_btn(row, caption, action, kind="accent"):
        self.make_button(row, caption, action, kind, side="left", ipady=6)
    _u107_add_offline_tab(self,notebook,t,add_row,add_btn)
    sp = self.panel(service); sp.pack(fill="x", padx=10, pady=8)
    tk.Label(sp, text="SZYBKIE TESTY I DIAGNOSTYKA", bg=t["panel"], fg=t["accent"], font=self.fnt(11,"bold")).pack(anchor="w", padx=12, pady=(10,4))
    for labels in [
        [("CPU / PROCESOR",lambda:self.show_module("CPU")),("GPU / VRAM",lambda:self.show_module("GPU")),("RAM",lambda:self.show_module("RAM")),("SSD / HDD",lambda:self.show_module("DYSK"))],
        [("MATRYCA",lambda:self.show_module("EKRAN")),("BATERIA",self.show_battery),("BEZPIECZEŃSTWO",lambda:self.show_module("SECURITY")),("PEŁNY RAPORT",self.show_report)],
        [("ODŚWIEŻ SPRZĘT",self.refresh_hardware_async),("PEŁNA DIAGNOSTYKA",self.full_test),("RAPORT BATERII",lambda:_u55_run_repair(self,"Raport baterii","powercfg.exe",["/batteryreport","/output",str((Path(os.environ.get("LOCALAPPDATA") or Path.home())/"NaprawaPC"/"RepairReports")/"battery-report.html")],120))]
    ]:
        row=add_row(sp)
        for caption,action in labels: add_btn(row,caption,action)
    rp = self.panel(repair); rp.pack(fill="x", padx=10, pady=8)
    tk.Label(rp, text="NAPRAWA SYSTEMU WINDOWS — OPERACJE MOGĄ WYŚWIETLIĆ MONIT UAC", bg=t["panel"], fg=t["accent"], font=self.fnt(11,"bold")).pack(anchor="w", padx=12, pady=(10,4))
    repair_rows = [
        [("SFC /SCANNOW",lambda:_u55_run_repair(self,"SFC","sfc.exe",["/scannow"])),("DISM /CHECKHEALTH",lambda:_u55_run_repair(self,"DISM CheckHealth","DISM.exe",["/Online","/Cleanup-Image","/CheckHealth"])),("DISM /SCANHEALTH",lambda:_u55_run_repair(self,"DISM ScanHealth","DISM.exe",["/Online","/Cleanup-Image","/ScanHealth"]))],
        [("DISM /RESTOREHEALTH",lambda:_u55_run_repair(self,"DISM RestoreHealth","DISM.exe",["/Online","/Cleanup-Image","/RestoreHealth"],5400)),("CHKDSK /SCAN",lambda:_u55_run_repair(self,"CHKDSK","chkdsk.exe",[os.environ.get("SystemDrive","C:"),"/scan"],1800)),("ODŚWIEŻ DNS",lambda:_u55_run_repair(self,"Flush DNS","ipconfig.exe",["/flushdns"],120))],
        [("RESET WINSOCK",lambda:_u55_run_repair(self,"Winsock reset","netsh.exe",["winsock","reset"],120)),("RAPORT BATERII",lambda:_u55_run_repair(self,"Raport baterii","powercfg.exe",["/batteryreport","/output",str(_u55_ticket_path().parent/"battery-report.html")],120)),("WINDOWS UPDATE",lambda:_u55_open_windows_tool(self,"ms-settings:windowsupdate"))],
        [("ZABEZPIECZENIA WINDOWS",lambda:_u55_open_windows_tool(self,"windowsdefender:")),("PODGLĄD ZDARZEŃ",lambda:_u55_open_windows_tool(self,"eventvwr.msc")),("MONITOR NIEZAWODNOŚCI",lambda:_u55_open_windows_tool(self,"perfmon /rel"))],
    ]
    for specs in repair_rows:
        row=add_row(rp)
        for caption,action in specs: add_btn(row,caption,action,"card" if "UPDATE" in caption or "ZABEZPIECZENIA" in caption else "accent")
    tp = self.panel(tools); tp.pack(fill="x", padx=10, pady=8)
    tk.Label(tp, text="DIAGNOSTYKA I NARZĘDZIA SYSTEMOWE", bg=t["panel"], fg=t["accent"], font=self.fnt(11,"bold")).pack(anchor="w", padx=12, pady=(10,4))
    for specs in [
        [("MENEDŻER URZĄDZEŃ","devmgmt.msc"),("ZARZĄDZANIE DYSKAMI","diskmgmt.msc"),("USŁUGI WINDOWS","services.msc")],
        [("INFORMACJE O SYSTEMIE","msinfo32.exe"),("MONITOR ZASOBÓW","resmon.exe"),("MENEDŻER ZADAŃ","taskmgr.exe")],
        [("HARMONOGRAM ZADAŃ","taskschd.msc"),("OCZYSZCZANIE DYSKU","cleanmgr.exe"),("MONITOR WYDAJNOŚCI","perfmon.exe")],
    ]:
        row=add_row(tp)
        for caption,target in specs: add_btn(row,caption,lambda target=target:_u55_open_windows_tool(self,target),"card")
    _u55_render_private_tickets(self, tickets)
    back = tk.Frame(self.content, bg=t["bg"]); back.pack(fill="x", padx=10, pady=(0,8))
    self.make_button(back, "← POWRÓT DO PULPITU", self.show_dashboard, "card", side="left", ipady=6)

AppV43.show_service_center = _u55_show_service_center

def _u55_selftest_service_center():
    assert callable(AppV43.show_service_center)
    assert callable(_u55_verify_service_password) and callable(_u55_derive_service_key)
    assert len(bytes.fromhex(_U55_AUTH_SALT_HEX)) == 16
    assert len(bytes.fromhex(_U55_AUTH_VERIFIER_HEX)) == 32
    assert len(bytes.fromhex(_U55_STORE_SALT_HEX)) == 16
    assert _U55_PBKDF2_ITERATIONS >= 600000
    assert _u55_Fernet is not None and _u55_PBKDF2HMAC is not None, "cryptography must be installed in the build environment"
    key = _u55_derive_service_key("service-center-selftest-only")
    token = _u55_Fernet(key).encrypt(b'{"selftest":true}')
    assert _u55_Fernet(key).decrypt(token) == b'{"selftest":true}'
    assert _u55_ticket_path().name == "zgloszenia.npcdata"
    assert callable(_u107_detect_windows_installations)
    assert callable(_u107_confirm_and_run) and callable(_u107_bcd_backup_path)
    center_constants=repr(AppV43.show_service_center.__code__.co_consts)
    offline_constants=repr(_u107_add_offline_tab.__code__.co_consts)
    assert "_u107_add_offline_tab" in AppV43.show_service_center.__code__.co_names
    assert "OFFLINE / BCD / WINRE" in offline_constants
    assert "DISM OFFLINE /RESTOREHEALTH" in offline_constants
    assert "SYSTEM REPAIR PRO" in center_constants and "SERWIS ULTIMATE" in center_constants
    # The Windows discovery routine is read-only and searches for the SOFTWARE hive marker.
    assert "System32" in repr(_u107_detect_windows_installations.__code__.co_consts)
    print("SERVICE_REPAIR_CENTER_SELFTEST_OK: encrypted tickets, repair tools, offline DISM/SFC, BCD backup and WinRE")
if __name__ == "__main__" and "--selftest-service-center" in sys.argv:
    try:
        _u55_selftest_service_center()
        raise SystemExit(0)
    except Exception as _u55_exc:
        print("SERVICE_REPAIR_CENTER_SELFTEST_FAILED:", type(_u55_exc).__name__, str(_u55_exc))
        raise SystemExit(1)
'@
$hubButton = '        self.make_button(p,"← PULPIT",self.show_dashboard,"card",side="left",ipady=8)'
if (!$src.Contains($hubButton)) { throw "Nie znaleziono przycisku pulpitu w show_tests_hub; integracja przerwana bez zapisania źródła." }
if (!$src.Contains('self.make_button(p,"CENTRUM SERWISU / NAPRAWA PRO",self.show_service_center,"accent",side="left",ipady=8)')) {
    $src = $src.Replace($hubButton, $hubButton + [Environment]::NewLine + '        self.make_button(p,"CENTRUM SERWISU / NAPRAWA PRO",self.show_service_center,"accent",side="left",ipady=8)')
}
$mainPattern = '(?m)^if __name__ == "__main__":'
if ($src -notmatch $mainPattern) { throw "Nie znaleziono punktu wejścia aplikacji do dołączenia centrum serwisu." }
$src = [regex]::Replace($src,$mainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $integration + [Environment]::NewLine + $m.Value
},1)
}
if (!$src.Contains("_U55_INTEGRATED_SERVICE_REPAIR_CENTER") -or !$src.Contains("SERVICE_REPAIR_CENTER_SELFTEST_OK") -or !$src.Contains("self.show_service_center")) { throw "Integracja Serwis Ultimate / System Repair PRO nie została prawidłowo dołączona." }

if ($src -notmatch 'range\(1,\s*126\)' -or !$src.Contains("_U443_ICON_HOVER_GLOW")) { throw "Theme/hover patch verification failed." }
# Advanced diagnostics upgrade: AI reader, live metrics, Cloudflare speed test and sequential 20-scene 3D studio.
$advancedPatchPath = Join-Path $PSScriptRoot "ADVANCED_MODULES_PATCH.py"
if (!(Test-Path -LiteralPath $advancedPatchPath)) { throw "Missing advanced feature patch: $advancedPatchPath" }
$advancedPatch = [IO.File]::ReadAllText($advancedPatchPath,[Text.Encoding]::UTF8)
# Add a real Windows read-only audit to the existing Test Center and route it through the app.
$routeAnchor = '      "USB_LIST":lambda:self._start_module_test("USB")'
$itemAnchor = '      ("RAPORT I HISTORIA","Wyniki faktycznie zapisanych pomiarów, nie przykładowe wartości.","RAPORT")'
if (!$advancedPatch.Contains('"AUDYT_WINDOWS":lambda:self.show_windows_audit(),')) {
  if (!$advancedPatch.Contains($routeAnchor)) { throw "Missing test-center route for Windows Audit." }
  $advancedPatch = $advancedPatch.Replace($routeAnchor, $routeAnchor + ',' + [Environment]::NewLine + '      "AUDYT_WINDOWS":lambda:self.show_windows_audit(),')
}
if (!$advancedPatch.Contains('("AUDYT WINDOWS / STEROWNIKI"')) {
  if (!$advancedPatch.Contains($itemAnchor)) { throw "Missing test-center card insertion point for Windows Audit." }
  $newItem = $itemAnchor + ',' + [Environment]::NewLine + '      ("AUDYT WINDOWS / STEROWNIKI","16 rzeczywistych kontroli Windows: PnP, sterowniki, Defender, zapora, UEFI/TPM, dyski, wolne miejsce, restart, zdarzenia, RAM, sieć i bateria. Tworzy raport HTML + JSON.","AUDYT_WINDOWS")'
  $advancedPatch = $advancedPatch.Replace($itemAnchor,$newItem)
}
if (!$advancedPatch.Contains('"AUDYT_WINDOWS":lambda:self.show_windows_audit(),') -or !$advancedPatch.Contains('("AUDYT WINDOWS / STEROWNIKI"')) { throw "Windows Audit route/card integration failed." }
$oldGpuDispatch = '            _u37_gpu_benchmark_child(_u37_output, 30)'
$newGpuDispatch = @'
            _u66_scene = int(sys.argv[_u37_index + 2]) if _u37_index + 2 < len(sys.argv) else 1
            _u66_seconds = int(sys.argv[_u37_index + 3]) if _u37_index + 3 < len(sys.argv) else 30
            _u66_resolution = sys.argv[_u37_index + 4] if _u37_index + 4 < len(sys.argv) else "1920x1080"
            _u37_gpu_benchmark_child(_u37_output, _u66_seconds, _u66_scene, _u66_resolution)
'@
if (!$src.Contains($oldGpuDispatch)) { throw "Nie znaleziono punktu wejścia dla scen 3D z parametrem sceny." }
$src = $src.Replace($oldGpuDispatch,$newGpuDispatch.TrimEnd())
$advancedMainPattern = '(?m)^if __name__ == "__main__":'
if ($src -notmatch $advancedMainPattern) { throw "Nie znaleziono głównego punktu wejścia dla modułów zaawansowanych." }
$src = [regex]::Replace($src,$advancedMainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $advancedPatch + [Environment]::NewLine + $m.Value
},1)
if (!$src.Contains("_U66_SCENES") -or !$src.Contains("ADVANCED_MODULES_SELFTEST_OK") -or !$src.Contains("_u66_web_search") -or !$src.Contains("Cloudflare") -or !$src.Contains("_u88_selftest_final_wiring") -or !$newGpuDispatch.Contains("_u66_resolution")) {
    throw "Weryfikacja wstawek AI Reader / Speed Test / 3D Studio / testów niezależnych nie powiodła się."
}
if (($src | Select-String -Pattern 'ADVANCED_MODULES_PATCH' -AllMatches).Matches.Count -gt 0) {
    # The patch source itself is external; only its contents are added to the generated main program.
    throw "Wykryto błędny marker nazwy pliku patcha w źródle aplikacji."
}

$windowsAuditPatchPath = Join-Path $PSScriptRoot "WINDOWS_AUDIT_MODULE_PATCH.py"
if (!(Test-Path -LiteralPath $windowsAuditPatchPath)) { throw "Missing Windows Audit module patch: $windowsAuditPatchPath" }
$windowsAuditPatch = [IO.File]::ReadAllText($windowsAuditPatchPath,[Text.Encoding]::UTF8)
$src = [regex]::Replace($src,$advancedMainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $windowsAuditPatch + [Environment]::NewLine + $m.Value
},1)
if (!$src.Contains("_U141_WINDOWS_AUDIT_VERSION") -or !$src.Contains("WINDOWS_AUDIT_SELFTEST_OK") -or !$src.Contains("AUDYT_WINDOWS")) { throw "Windows Audit integration markers are missing." }

$suitePatchPath = Join-Path $PSScriptRoot "INTEGRATED_APPS_PATCH.py"
if (!(Test-Path -LiteralPath $suitePatchPath)) { throw "Missing integrated apps patch: $suitePatchPath" }
$suitePatch = [IO.File]::ReadAllText($suitePatchPath,[Text.Encoding]::UTF8)
$src = [regex]::Replace($src,$advancedMainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $suitePatch + [Environment]::NewLine + $m.Value
},1)
if (!$src.Contains("_U144_INTEGRATED_APPS_VERSION") -or !$src.Contains("INTEGRATED_APPS_SELFTEST_OK") -or !$src.Contains("show_integrated_apps_hub") -or !$src.Contains("ShellExecuteW")) {
    throw "Integrated apps hub / System Repair PRO companion wiring is incomplete."
}
$testUpgradePath = Join-Path $PSScriptRoot "CPU_RAM_GPU_UPGRADE_PATCH.py"
if (!(Test-Path -LiteralPath $testUpgradePath)) { throw "Missing CPU/RAM/GPU upgrade patch: $testUpgradePath" }
$testUpgrade = [IO.File]::ReadAllText($testUpgradePath,[Text.Encoding]::UTF8)
$src = [regex]::Replace($src,$advancedMainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $testUpgrade + [Environment]::NewLine + $m.Value
},1)
if (!$src.Contains("_U145_CPU_RAM_GPU_PATCH_VERSION") -or !$src.Contains("CPU_RAM_GPU_LIVE_SELFTEST_OK") -or !$src.Contains("DIAGNOSTYKA NA ŻYWO")) {
    throw "CPU/RAM/GPU live-test patch verification failed."
}

# Quality/regression fixes: correct full-buffer RAM patterns, sample CPU during load,
# and route actual OpenGL FPS into the component report.
$qualityCorePath = Join-Path $PSScriptRoot "QUALITY_TESTS_CORE_PATCH.py"
$qualityAliasesPath = Join-Path $PSScriptRoot "QUALITY_TESTS_ALIASES_PATCH.py"
$qualityWiringPath = Join-Path $PSScriptRoot "QUALITY_TESTS_WIRING_PATCH.py"
foreach ($qualityPath in @($qualityCorePath,$qualityAliasesPath,$qualityWiringPath)) {
    if (!(Test-Path -LiteralPath $qualityPath)) { throw "Missing quality-test patch file: $qualityPath" }
}
$qualityPatch = [IO.File]::ReadAllText($qualityCorePath,[Text.Encoding]::UTF8).TrimEnd() + [Environment]::NewLine +
    [IO.File]::ReadAllText($qualityAliasesPath,[Text.Encoding]::UTF8).TrimEnd() + [Environment]::NewLine +
    [IO.File]::ReadAllText($qualityWiringPath,[Text.Encoding]::UTF8).TrimEnd()
$src = [regex]::Replace($src,$advancedMainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $qualityPatch + [Environment]::NewLine + $m.Value
},1)
if (!$src.Contains("_U146_QUALITY_PATCH_VERSION") -or !$src.Contains("QUALITY_TESTS_SELFTEST_OK") -or !$src.Contains("ram_pattern_test")) {
    throw "Full-buffer RAM / CPU live / GPU result quality fixes were not included in the generated application."
}

$executionFixPath = Join-Path $PSScriptRoot "HARDWARE_EXECUTION_FIX_PATCH.py"
if (!(Test-Path -LiteralPath $executionFixPath)) { throw "Missing hardware execution fix patch: $executionFixPath" }
$executionFix = [IO.File]::ReadAllText($executionFixPath,[Text.Encoding]::UTF8)
$src = [regex]::Replace($src,$advancedMainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $executionFix + [Environment]::NewLine + $m.Value
},1)
if (!$src.Contains("_U148_HARDWARE_EXECUTION_PATCH_VERSION") -or !$src.Contains("HARDWARE_EXECUTION_FIX_SELFTEST_OK") -or !$src.Contains("_u148_refresh_main_ram")) {
    throw "Hardware execution/UI report synchronization patch did not get integrated."
}

$benchmarkHistoryPath = Join-Path $PSScriptRoot "HARDWARE_BENCHMARK_HISTORY_PATCH.py"
if (!(Test-Path -LiteralPath $benchmarkHistoryPath)) { throw "Missing hardware benchmark history patch: $benchmarkHistoryPath" }
$benchmarkHistoryPatch = [IO.File]::ReadAllText($benchmarkHistoryPath,[Text.Encoding]::UTF8)
$src = [regex]::Replace($src,$advancedMainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $benchmarkHistoryPatch + [Environment]::NewLine + $m.Value
},1)
if (!$src.Contains("_U149_BENCHMARK_HISTORY_VERSION") -or !$src.Contains("HARDWARE_BENCHMARK_HISTORY_SELFTEST_OK")) { throw "Benchmark history integration missing." }
$gpuStart = $src.IndexOf("def _u114_gpu_benchmark_child(")
$gpuEnd = if ($gpuStart -ge 0) { $src.IndexOf("_u37_gpu_benchmark_child=_u114_gpu_benchmark_child",$gpuStart) } else { -1 }
if ($gpuStart -lt 0 -or $gpuEnd -le $gpuStart) { throw "Final OpenGL renderer not found." }
$gpuFunction = $src.Substring($gpuStart,$gpuEnd-$gpuStart)
$oldCamera = "GL.glTranslatef(0,-.10,-7.0)"
$cameraCount = [regex]::Matches($gpuFunction,[regex]::Escape($oldCamera)).Count
if ($cameraCount -ne 1) { throw "Expected one original GPU camera transform, found $cameraCount." }
$gpuFunction = $gpuFunction.Replace($oldCamera,"GL.glTranslatef(0,-.10,-5.25)")
$oldFov = "_u114_perspective(52.0,width/height,.1,240.0)"
if (!$gpuFunction.Contains($oldFov)) { throw "GPU perspective/FOV not found." }
$gpuFunction = $gpuFunction.Replace($oldFov,"_u114_perspective(45.0,width/height,.1,240.0)")
$src = $src.Substring(0,$gpuStart) + $gpuFunction + $src.Substring($gpuEnd)

$componentSimPatchPath = Join-Path $PSScriptRoot "COMPONENT_SPECIFIC_SIMULATORS_PATCH.py"
if (!(Test-Path -LiteralPath $componentSimPatchPath)) { throw "Missing component-specific simulator patch: $componentSimPatchPath" }
$componentSimPatch = [IO.File]::ReadAllText($componentSimPatchPath,[Text.Encoding]::UTF8)
$src = [regex]::Replace($src,$advancedMainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $componentSimPatch + [Environment]::NewLine + $m.Value
},1)
if (!$src.Contains("_U150_COMPONENT_SIMULATORS_VERSION") -or !$src.Contains("COMPONENT_SPECIFIC_SIMULATORS_SELFTEST_OK")) {
    throw "Component-specific simulator patch was not included."
}

$hardwareResultConsolePath = Join-Path $PSScriptRoot "HARDWARE_RESULT_CONSOLE_PATCH.py"
if (!(Test-Path -LiteralPath $hardwareResultConsolePath)) { throw "Missing hardware result console patch: $hardwareResultConsolePath" }
$hardwareResultConsolePatch = [IO.File]::ReadAllText($hardwareResultConsolePath,[Text.Encoding]::UTF8)
$src = [regex]::Replace($src,$advancedMainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $hardwareResultConsolePatch + [Environment]::NewLine + $m.Value
},1)
if (!$src.Contains("_U151_HARDWARE_RESULT_CONSOLE_VERSION") -or !$src.Contains("HARDWARE_RESULT_CONSOLE_SELFTEST_OK") -or !$src.Contains("MONITOR SPRZĘTU + OSTATNI WYNIK")) {
    throw "CPU/RAM/GPU actual-result console integration failed."
}

# v4.3.151: dedicated GPU FurMark-style stress and 13 non-repeating component schematics.
$gpuStart = $src.IndexOf("def _u114_gpu_benchmark_child(")
$gpuEnd = if ($gpuStart -ge 0) { $src.IndexOf("_u37_gpu_benchmark_child=_u114_gpu_benchmark_child",$gpuStart) } else { -1 }
if ($gpuStart -lt 0 -or $gpuEnd -le $gpuStart) { throw "Final OpenGL renderer not found for anti-duplicate scene fix." }
$gpuFunction = $src.Substring($gpuStart,$gpuEnd-$gpuStart)
$oldOverlay = @'
            if sid!=1:
                draw_scene_signature(elapsed)
                # The scene-specific FurMark stress object is deliberately layered on top of
                # each non-base layout; its seeded geometry differs for every scene ID.
                _u119_draw_furmark(elapsed)
'@
if (!$gpuFunction.Contains($oldOverlay)) { throw "Could not locate the repeated FurMark overlay on the other 109 scenes." }
$newOverlay = @'
            if sid!=1:
                draw_scene_signature(elapsed)
'@
$gpuFunction = $gpuFunction.Replace($oldOverlay,$newOverlay)
$oldHairCount = '        _u119_hair_count=_u119_profile["hair_count"]'
if (!$gpuFunction.Contains($oldHairCount)) { throw "FurMark hair-count setup not found." }
$gpuFunction = $gpuFunction.Replace($oldHairCount,'        _u119_hair_count=_u119_profile["hair_count"] if sid == 1 else 0')
$oldDrawBlock = @'
            GL.glRotatef(9.0+5.0*_u114_math.sin(elapsed*.7),1,0,0)
            draw_scene(elapsed)
'@
$newDrawBlock = @'
            GL.glRotatef(9.0+5.0*_u114_math.sin(elapsed*.7),1,0,0)
            if sid == 1:
                GL.glScalef(2.1,2.1,2.1)
            else:
                GL.glScalef(1.35,1.35,1.35)
            draw_scene(elapsed)
'@
if (!$gpuFunction.Contains($oldDrawBlock)) { throw "GPU scene camera/draw anchor missing." }
$gpuFunction = $gpuFunction.Replace($oldDrawBlock,$newDrawBlock)
$oldMetadata = '"furmark_overlay":True,"furmark_profile":_u119_profile,"furmark_hair_count":len(_u119_furmark_hairs),'
$newMetadata = '"furmark_overlay":(sid==1),"furmark_profile":(_u119_profile if sid==1 else None),"furmark_hair_count":len(_u119_furmark_hairs),'
if (!$gpuFunction.Contains($oldMetadata)) { throw "FurMark metadata anchor missing." }
$gpuFunction = $gpuFunction.Replace($oldMetadata,$newMetadata)
$src = $src.Substring(0,$gpuStart) + $gpuFunction + $src.Substring($gpuEnd)
if ($src.Contains($oldOverlay.Trim())) { throw "Repeated FurMark overlay still appears in generated source." }

$furmarkPatchPath = Join-Path $PSScriptRoot "FURMARK_UNIQUE_SIMULATORS_PATCH.py"
if (!(Test-Path -LiteralPath $furmarkPatchPath)) { throw "Missing FurMark / unique simulators patch: $furmarkPatchPath" }
$furmarkPatch = [IO.File]::ReadAllText($furmarkPatchPath,[Text.Encoding]::UTF8)
# Correct a defensive closing-parenthesis typo before embedding and syntax-checking the patch.
$badProgress = 'progress.configure(value=max(0.0,min(99.0,100.0*(_u152_time.monotonic()-started)/duration))'
$goodProgress = 'progress.configure(value=max(0.0,min(99.0,100.0*(_u152_time.monotonic()-started)/duration)))'
$furmarkPatch = $furmarkPatch.Replace($badProgress,$goodProgress)
$src = [regex]::Replace($src,$advancedMainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $furmarkPatch + [Environment]::NewLine + $m.Value
},1)
if (!$src.Contains("_U152_FURMARK_UNIQUE_SIMULATORS_VERSION") -or !$src.Contains("FURMARK_AND_UNIQUE_SIMULATORS_SELFTEST_OK") -or !$src.Contains("FURMARK_STYLE_GPU_STRESS") -or !$src.Contains("13 UNIKALNYCH SYMULATORÓW")) {
    throw "FurMark stress page / 13 unique simulators were not integrated."
}
$workbenchPatchPath = Join-Path $PSScriptRoot "COMPONENT_TEST_WORKBENCH_PATCH.py"
if (!(Test-Path -LiteralPath $workbenchPatchPath)) { throw "Missing CPU/RAM/GPU component test workbench patch." }
$workbenchPatch = [IO.File]::ReadAllText($workbenchPatchPath,[Text.Encoding]::UTF8)
$src = [regex]::Replace($src,$advancedMainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $workbenchPatch + [Environment]::NewLine + $m.Value
},1)
if (!$src.Contains("_U153_COMPONENT_TEST_WORKBENCH_VERSION") -or !$src.Contains("COMPONENT_TEST_WORKBENCH_SELFTEST_OK") -or !$src.Contains("START RZECZYWISTEGO TESTU") -or !$src.Contains("BRAK NOWEGO RAPORTU")) {
    throw "CPU/RAM/GPU test workbench is incomplete or was not integrated into the generated application."
}

$profilePatchPath = Join-Path $PSScriptRoot "HARDWARE_PROFILE_SUITE_PATCH.py"
if (!(Test-Path -LiteralPath $profilePatchPath)) { throw "Missing CPU/RAM/GPU benchmark profile suite patch." }
$profilePatch = [IO.File]::ReadAllText($profilePatchPath,[Text.Encoding]::UTF8)
$src = [regex]::Replace($src,$advancedMainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $profilePatch + [Environment]::NewLine + $m.Value
},1)
if (!$src.Contains("_U154_HARDWARE_PROFILE_VERSION") -or !$src.Contains("HARDWARE_PROFILE_SUITE_SELFTEST_OK") -or !$src.Contains("PROFIL RZECZYWISTEGO BENCHMARKU") -or !$src.Contains("URUCHOM PROFIL CPU + RAM + GPU")) {
    throw "Selectable CPU/RAM/GPU benchmark profiles were not integrated into the generated application."
}
$mainComponentPatchPath = Join-Path $PSScriptRoot "HARDWARE_MAIN_COMPONENT_HANDOFF_PATCH.py"
if (!(Test-Path -LiteralPath $mainComponentPatchPath)) { throw "Missing main CPU/RAM/GPU execution handoff patch." }
$mainComponentPatch = [IO.File]::ReadAllText($mainComponentPatchPath,[Text.Encoding]::UTF8)
$src = [regex]::Replace($src,$advancedMainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $mainComponentPatch + [Environment]::NewLine + $m.Value
},1)
if (!$src.Contains("_U160_MAIN_COMPONENT_HANDOFF_VERSION") -or !$src.Contains("MAIN_COMPONENT_HANDOFF_SELFTEST_OK") -or !$src.Contains("AppV43.show_module = _u160_show_module_with_execution_workbench")) {
    throw "Main CPU/RAM/GPU execution handoff was not integrated."
}

$diagnosisPatchPath = Join-Path $PSScriptRoot "HARDWARE_BENCHMARK_DIAGNOSIS_PATCH.py"
if (!(Test-Path -LiteralPath $diagnosisPatchPath)) { throw "Missing hardware benchmark diagnosis patch." }
$diagnosisPatch = [IO.File]::ReadAllText($diagnosisPatchPath,[Text.Encoding]::UTF8)
$src = [regex]::Replace($src,$advancedMainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $diagnosisPatch + [Environment]::NewLine + $m.Value
},1)
if (!$src.Contains("_U163_BENCHMARK_DIAGNOSIS_VERSION") -or !$src.Contains("HARDWARE_BENCHMARK_DIAGNOSIS_SELFTEST_OK") -or !$src.Contains("ANALIZA WYNIKU + TREND Z POPRZEDNIM TESTEM") -or !$src.Contains("_u163_comparability")) {
    throw "Evidence-based CPU/RAM/GPU diagnosis was not integrated."
}

# v4.3.159 — automatic global update after a newer stable release is detected.
# The file is downloaded by the existing SHA-256/size/PE-verified worker; Windows UAC remains mandatory.
$autoUpdatePatch = @'
_U159_AUTO_UPDATE_VERSION = "1.0.0"

def _u159_update_decision(current, latest, release_ready=True):
    if not release_ready:
        return "not_ready"
    current_tuple = _u37_version_tuple(str(current or ""))
    latest_tuple = _u37_version_tuple(str(latest or ""))
    if latest_tuple == (0, 0, 0):
        return "invalid"
    return "update" if latest_tuple > current_tuple else "current"


def _u159_auto_update_worker(app, data, version):
    try:
        downloader = getattr(app, "_u39_download_global_update", None)
        if not callable(downloader):
            raise RuntimeError("Brak zweryfikowanego mechanizmu pobierania aktualizacji.")
        downloader(data)
    except Exception as exc:
        try:
            app._u159_auto_update_target = ""
        except Exception:
            pass
        message = f"Automatyczna aktualizacja {version} nie powiodła się: {type(exc).__name__}: {exc}"
        try:
            app.queue_action(lambda m=message: app._u39_set_update_status(m))
            app.queue_action(lambda m=message: messagebox.showerror("Aktualizacja globalna", m))
        except Exception:
            pass
        try:
            app.queue_log(message)
        except Exception:
            pass


def _u159_auto_offer_global_update(self, data):
    if not isinstance(data, dict):
        self._u39_set_update_status("Automatyczna aktualizacja: manifest nie jest poprawnym obiektem.")
        return False
    version = str(data.get("version") or "").strip()
    decision = _u159_update_decision(
        str(VERSION).split()[0], version, bool(data.get("release_ready"))
    )
    if decision == "not_ready":
        self._u39_set_update_status("Kanał odpowiada, ale nowy instalator nie jest jeszcze gotowy.")
        return False
    if decision == "invalid":
        self._u39_set_update_status("Automatyczna aktualizacja zatrzymana: manifest ma nieprawidłową wersję.")
        return False
    if decision != "update":
        return False

    previous_target = str(getattr(self, "_u159_auto_update_target", "") or "")
    previous_status = str(getattr(self, "_u39_last_update_status", "") or "").casefold()
    if previous_target == version:
        # Allow another manual check to retry after an explicit download/verification error.
        if any(marker in previous_status for marker in (
            "błąd pobierania", "blad pobierania", "nie udało się pobrać",
            "sha-256 niezgodne", "niepełny plik", "niepelny plik",
            "nie można pobrać", "nie mozna pobrac"
        )):
            self._u159_auto_update_target = ""
        else:
            return False

    self._u159_auto_update_target = version
    message = (
        f"Wykryto nową stabilną wersję {version}. Automatycznie pobieram instalator, "
        "sprawdzę rozmiar i SHA-256, a następnie uruchomię instalację. "
        "Windows może poprosić o zgodę UAC."
    )
    self._u39_set_update_status(message)
    try:
        self.append_log("AKTUALIZATOR AUTO: " + message)
    except Exception:
        pass
    try:
        thread = threading.Thread(
            target=_u159_auto_update_worker,
            args=(self, dict(data), version),
            name="NaprawaPCAutomaticGlobalUpdate",
            daemon=True,
        )
        thread.start()
        return True
    except Exception as exc:
        self._u159_auto_update_target = ""
        error = f"Nie udało się rozpocząć automatycznej aktualizacji: {type(exc).__name__}: {exc}"
        self._u39_set_update_status(error)
        try:
            messagebox.showerror("Aktualizacja globalna", error, parent=self)
        except Exception:
            pass
        return False


AppV43._u39_offer_global_update = _u159_auto_offer_global_update


def _u159_selftest_auto_update():
    assert _U159_AUTO_UPDATE_VERSION == "1.0.0"
    assert _u159_update_decision("4.3.158", "4.3.159", True) == "update"
    assert _u159_update_decision("4.3.159", "4.3.158", True) == "current"
    assert _u159_update_decision("4.3.159", "4.3.159", True) == "current"
    assert _u159_update_decision("4.3.158", "4.3.159", False) == "not_ready"
    assert _u159_update_decision("4.3.158", "not-a-version", True) == "invalid"
    assert AppV43._u39_offer_global_update is _u159_auto_offer_global_update
    offer_names = set(_u159_auto_offer_global_update.__code__.co_names)
    worker_names = set(_u159_auto_update_worker.__code__.co_names)
    assert "askyesno" not in offer_names, "update discovery must not stop at a manual Yes/No prompt"
    assert "threading" in offer_names and "_u159_auto_update_worker" in offer_names
    assert "_u39_download_global_update" in _u159_auto_update_worker.__code__.co_consts, "auto update must use the SHA-256 verified downloader"
    download_code = globals().get("_u44_download_global_update")
    assert callable(download_code)
    assert "startfile" not in download_code.__code__.co_names
    assert "explorer.exe" not in download_code.__code__.co_consts
    launch = globals().get("_u44_confirm_downloaded")
    assert callable(launch) and "ShellExecuteExW" in launch.__code__.co_names
    assert "runas" in launch.__code__.co_consts and "askyesno" not in launch.__code__.co_names
    print("AUTO_UPDATE_SELFTEST_OK: newer stable release triggers verified download and UAC installer without extra confirmation or Explorer detour")
'@
$src = [regex]::Replace($src,$advancedMainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $autoUpdatePatch + [Environment]::NewLine + $m.Value
},1)
if (!$src.Contains("_U159_AUTO_UPDATE_VERSION") -or !$src.Contains("AUTO_UPDATE_SELFTEST_OK") -or !$src.Contains("AppV43._u39_offer_global_update = _u159_auto_offer_global_update")) {
    throw "Automatic update patch was not integrated into the generated source."
}

$mainAutoTest = @'
    elif "--selftest-auto-update" in sys.argv:
        try:
            _u159_selftest_auto_update()
            raise SystemExit(0)
        except Exception as _u159_exc:
            print("AUTO_UPDATE_SELFTEST_FAILED:", type(_u159_exc).__name__, str(_u159_exc))
            raise SystemExit(1)
    elif "--selftest-main-component-handoff" in sys.argv:
        try:
            _u160_selftest_main_component_handoff()
            raise SystemExit(0)
        except Exception as _u160_exc:
            print("MAIN_COMPONENT_HANDOFF_SELFTEST_FAILED:", type(_u160_exc).__name__, str(_u160_exc))
            raise SystemExit(1)
'@
$mainPattern = '(?m)^    else:\r?\n        app = AppV43\(\)\r?\n        app\.protocol\("WM_DELETE_WINDOW", app\.close_app\)\r?\n        app\.mainloop\(\)$'
$mainMatches = [regex]::Matches($src,$mainPattern)
if ($mainMatches.Count -ne 1) { throw "Could not find exactly one original app startup block for the auto-update selftest; found $($mainMatches.Count)." }
$src = [regex]::Replace($src,$mainPattern,[System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $mainAutoTest + [Environment]::NewLine + $m.Value
},1)
if (!$src.Contains("_U159_AUTO_UPDATE_VERSION") -or !$src.Contains("AUTO_UPDATE_SELFTEST_OK") -or !$src.Contains("elif ""--selftest-auto-update"" in sys.argv")) {
    throw "Automatic updater or its CLI selftest was not integrated."
}
[IO.File]::WriteAllText($sourcePath,$src,[Text.UTF8Encoding]::new($false))

# Keep the user-facing documentation aligned with the generated build.
$readmePath = Join-Path $PSScriptRoot "README_PL.txt"
if (Test-Path -LiteralPath $readmePath) {
    $readme = [IO.File]::ReadAllText($readmePath,[Text.Encoding]::UTF8)
    if (!$readme.Contains("CENTRUM SERWISU ULTIMATE + SYSTEM REPAIR PRO")) {
        $readme += @"

CENTRUM SERWISU ULTIMATE + SYSTEM REPAIR PRO
-------------------------------------------
W wersji budowanej z aktualnego źródła dostępna jest dodatkowa sekcja CENTRUM SERWISU / NAPRAWA PRO w ekranie TESTY:
- zakładki Serwis Ultimate, System Repair PRO, Zgłoszenia prywatne i Narzędzia serwisowe;
- prywatne zgłoszenia z weryfikacją PBKDF2 i szyfrowaniem danych lokalnych;
- SFC, DISM, CHKDSK, odświeżanie DNS, reset Winsock, raport baterii oraz skróty do narzędzi Windows;
- automatyczny aktualizator z nazwami tymczasowymi i kontrolą SHA-256; po wykryciu nowej stable uruchamia pobieranie i instalację przez Windows UAC.
Zgłoszenia nie są wysyłane do Internetu. Operacje wymagające administratora wyświetlają monit UAC.
"@
        [IO.File]::WriteAllText($readmePath,$readme,[Text.UTF8Encoding]::new($false))
    }
}

$setup=[IO.File]::ReadAllText($setupPath,[Text.Encoding]::UTF8)
$setup=[regex]::Replace($setup,'(?m)^(\s*#define AppVersion\s+")\d+\.\d+\.\d+(".*)$',[System.Text.RegularExpressions.MatchEvaluator]{param($m) $m.Groups[1].Value+$next+$m.Groups[2].Value},1)
$setup=[regex]::Replace($setup,'(?m)^(\s*#define ExeName\s+"NAPRAWA-PC-HARDWARE-TEST-PRO-)\d+\.\d+\.\d+(\.exe".*)$', [System.Text.RegularExpressions.MatchEvaluator]{param($m) $m.Groups[1].Value+$next+$m.Groups[2].Value},1)
$oldRunFlags = 'Flags: postinstall nowait skipifsilent'
if (!$setup.Contains($oldRunFlags)) { throw "Nie znaleziono wpisu uruchamiania programu po instalacji." }
$setup = $setup.Replace($oldRunFlags, 'Flags: nowait runasoriginaluser')
if ($setup.Contains('postinstall nowait skipifsilent')) { throw "Instalator nadal pomija ponowne uruchomienie w trybie cichym." }
[IO.File]::WriteAllText($setupPath,$setup,[Text.UTF8Encoding]::new($false))
$nl=[Environment]::NewLine
[IO.File]::AppendAllText($env:GITHUB_ENV,("APP_VERSION=$next"+$nl+"SETUP_FILENAME=$setupName"+$nl),[Text.UTF8Encoding]::new($false))
[IO.File]::AppendAllText($env:GITHUB_OUTPUT,("app_version=$next"+$nl+"setup_filename=$setupName"+$nl),[Text.UTF8Encoding]::new($false))
Write-Host "AUTO_RELEASE_VERSION=$next"
Write-Host "NEXT_VERSION=$next"
Write-Host "THEMES=125 (115 added)"
Write-Host "HOVER_GLOW=patched"
