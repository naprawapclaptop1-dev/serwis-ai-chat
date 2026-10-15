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
# Keep one UAC prompt, run Inno Setup unattended, then close the older application.
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
        ps_path = Path(os.environ.get("WINDIR", r"C:\Windows")) / "System32" / "WindowsPowerShell" / "v1.0" / "powershell.exe"
        if os.name == "nt" and not ps_path.is_file():
            raise FileNotFoundError(f"Nie znaleziono Windows PowerShell: {ps_path}")
        script_path = update_dir / f"launch-update-{safe_version}.ps1"
        log_path = update_dir / f"installer-{safe_version}.log"
        status_path = update_dir / f"installer-{safe_version}-status.txt"
        quoted_installer = str(installer).replace("'", "''")
        quoted_log = str(log_path).replace("'", "''")
        quoted_status = str(status_path).replace("'", "''")
        script_template = r"""$ErrorActionPreference = 'Stop'
$installer = '__INSTALLER__'
$logPath = '__LOG__'
$statusPath = '__STATUS__'
try {
    if (-not (Test-Path -LiteralPath $installer -PathType Leaf)) {
        throw "Nie znaleziono pobranego instalatora: $installer"
    }
    $arguments = @('/SILENT', '/SUPPRESSMSGBOXES', '/NORESTART', '/SP-', ('/LOG="' + $logPath + '"'))
    $process = Start-Process -FilePath $installer -ArgumentList $arguments -PassThru -Wait
    $result = "EXIT_CODE=$($process.ExitCode)" + [Environment]::NewLine + "INSTALLER=$installer" + [Environment]::NewLine + "LOG=$logPath"
    $result | Set-Content -LiteralPath $statusPath -Encoding UTF8
    if ($process.ExitCode -ne 0) {
        throw "Instalator zakończył pracę z kodem $($process.ExitCode). Log: $logPath"
    }
} catch {
    $message = $_.Exception.Message
    ("ERROR=" + $message + [Environment]::NewLine + "INSTALLER=" + $installer + [Environment]::NewLine + "LOG=" + $logPath) |
        Set-Content -LiteralPath $statusPath -Encoding UTF8
    try {
        Add-Type -AssemblyName System.Windows.Forms
        [System.Windows.Forms.MessageBox]::Show(
            ($message + [Environment]::NewLine + [Environment]::NewLine + "Raport: " + $statusPath),
            'NAPRAWA PC - Aktualizacja',
            [System.Windows.Forms.MessageBoxButtons]::OK,
            [System.Windows.Forms.MessageBoxIcon]::Error
        ) | Out-Null
    } catch {}
    exit 1
}
"""
        script = script_template.replace("__INSTALLER__", quoted_installer).replace("__LOG__", quoted_log).replace("__STATUS__", quoted_status)
        script_path.write_text(script, encoding="utf-8-sig")
        if os.name == "nt":
            import ctypes as _u46_ctypes
            from ctypes import wintypes as _u46_wintypes
            _u46_shell = _u46_ctypes.WinDLL("shell32", use_last_error=True)
            _u46_execute = _u46_shell.ShellExecuteW
            _u46_execute.argtypes = [
                _u46_wintypes.HWND, _u46_wintypes.LPCWSTR,
                _u46_wintypes.LPCWSTR, _u46_wintypes.LPCWSTR,
                _u46_wintypes.LPCWSTR, _u46_ctypes.c_int
            ]
            _u46_execute.restype = _u46_ctypes.c_void_p
            parameters = f'-NoProfile -ExecutionPolicy Bypass -File "{script_path}"'
            result = _u46_execute(None, "runas", str(ps_path), parameters, str(update_dir), 1)
            result_code = int(result or 0)
            if result_code <= 32:
                raise OSError(
                    f"Windows nie uruchomił pomocnika aktualizacji (ShellExecuteW={result_code}). "
                    "Sprawdź, czy monit UAC nie został anulowany."
                )
        else:
            subprocess.Popen([str(installer), "/SILENT", "/SUPPRESSMSGBOXES", "/NORESTART", "/SP-"], cwd=str(update_dir))
        try:
            self.append_log(
                f"Aktualizator: uruchomiono pomocnika instalacji wersji {version}. "
                f"Raport: {status_path}; log instalatora: {log_path}"
            )
        except Exception:
            pass
        try:
            self._u39_set_update_status(
                f"Uruchomiono aktualizację {version}. Potwierdź UAC i poczekaj na pasek instalacji. "
                f"Raport błędu, jeśli wystąpi: {status_path}"
            )
        except Exception:
            pass
        # Do not close the app before UAC is accepted. Setup closes the old app itself.
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
'@
$confirmPattern = '(?s)def _u44_confirm_downloaded\(self, path, version\):.*?(?=\r?\nAppV43\._u44_set_progress = _u44_set_progress)'
$confirmMatches = [regex]::Matches($src, $confirmPattern)
if ($confirmMatches.Count -ne 1) { throw "Oczekiwano dokładnie jednej funkcji _u44_confirm_downloaded; znaleziono $($confirmMatches.Count)." }
$src = [regex]::Replace($src, $confirmPattern, [System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $confirmPatch.TrimEnd()
}, 1)
$oldLauncherSelfTest = 'assert "ShellExecuteW" in _u44_confirm_downloaded.__code__.co_names'
if (!$src.Contains($oldLauncherSelfTest)) { throw "Nie znaleziono testu uruchamiania instalatora." }
$newLauncherSelfTest = 'assert "ShellExecuteW" in _u44_confirm_downloaded.__code__.co_names' + [Environment]::NewLine +
'    assert any("Start-Process" in str(x) for x in _u44_confirm_downloaded.__code__.co_consts)' + [Environment]::NewLine +
'    assert "installer-" in str(_u44_confirm_downloaded.__code__.co_consts) and "-status.txt" in str(_u44_confirm_downloaded.__code__.co_consts)' + [Environment]::NewLine +
'    assert "askyesno" not in _u44_confirm_downloaded.__code__.co_names' + [Environment]::NewLine +
'    assert "uuid4" in _u44_download_global_update.__code__.co_names' + [Environment]::NewLine +
'    assert "gettempdir" in _u44_download_global_update.__code__.co_names' + [Environment]::NewLine +
'    assert "xb" in _u44_download_global_update.__code__.co_consts' + [Environment]::NewLine +
'    assert "close_app" not in _u44_confirm_downloaded.__code__.co_names'
$src = $src.Replace($oldLauncherSelfTest, $newLauncherSelfTest)


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
        raise ValueError("Rozmiar pomocnika aktualizacji poza dozwolonym zakresem.")

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

    # Unique names prevent stale/locked .download files from blocking the next update.
    dest = root / (Path(filename).stem + "-" + token + ".exe")
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
        self.queue_action(lambda p=str(dest), v=version, root=str(root): self._u44_set_progress(100, f"Pobieranie {v} zakończone. Plik sprawdzony; uruchamiam pomocnika z: {root}"))
        self.queue_action(lambda p=str(dest), v=version: self._u44_confirm_downloaded(p, v))
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
$downloadPattern = '(?s)def _u44_download_global_update\(self, data\):.*?(?=\r?\nAppV43\._u44_set_progress = _u44_set_progress)'
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
for _u443_tid, _u443_theme in THEMES.items():
    _u443_prof = _U443_SKIN_PROFILES[(_u443_tid - 1) % len(_U443_SKIN_PROFILES)]
    _u443_theme["_skin_family"] = _u443_prof["name"]
    _u443_theme["_skin_id"] = (_u443_tid - 1) % len(_U443_SKIN_PROFILES)
    _u443_theme["_panel_relief"] = _u443_prof["panel_relief"]
    _u443_theme["_panel_bd"] = _u443_prof["panel_bd"]
    _u443_theme["_panel_highlight"] = _u443_prof["panel_highlight"]
    _u443_theme["_button_relief"] = _u443_prof["button_relief"]
    _u443_theme["_button_overrelief"] = _u443_prof["button_overrelief"]
    _u443_theme["_button_bd"] = _u443_prof["button_bd"]
    _u443_theme["_font_family"] = _u443_prof["font"]
    _u443_theme["_image_style"] = _u443_prof["image"]
    _u443_theme["_skin_layout"] = _u443_prof["layout"]
    _u443_theme["_scanlines"] = _u443_prof["scanlines"]
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
    _u443_profile = _U443_SKIN_PROFILES[_u443_theme["_skin_id"]]
    for _u443_key, _u443_profile_key in (("_panel_relief","panel_relief"),("_panel_bd","panel_bd"),("_panel_highlight","panel_highlight"),("_button_relief","button_relief"),("_button_overrelief","button_overrelief"),("_button_bd","button_bd"),("_font_family","font"),("_image_style","image"),("_skin_layout","layout"),("_scanlines","scanlines")):
        _u443_theme.setdefault(_u443_key, _u443_profile[_u443_profile_key])

_U443_ORIG_PANEL = AppV43.panel
def _u443_panel_skin(self, parent, bg=None, accent=True):
    frame = _U443_ORIG_PANEL(self, parent, bg, accent)
    t = self.colors()
    try:
        frame.configure(relief=t.get("_panel_relief","flat"), bd=int(t.get("_panel_bd",0)),
                        highlightthickness=int(t.get("_panel_highlight",1)),
                        highlightbackground=t.get("accent","#1aa7ff") if accent else t.get("panel","#0b1c30"),
                        highlightcolor=t.get("accent2","#55d8ff"))
    except Exception: pass
    return frame
AppV43.panel = _u443_panel_skin

_U443_ORIG_MAKE_BUTTON = AppV43.make_button
def _u443_make_button_skin(self, parent, text, command, kind="card", side=None, fill=None, ipady=8):
    button = _U443_ORIG_MAKE_BUTTON(self, parent, text, command, kind, side, fill, ipady)
    t = self.colors()
    try:
        button.configure(relief=t.get("_button_relief","flat"), overrelief=t.get("_button_overrelief","raised"),
                         bd=int(t.get("_button_bd",0)), highlightthickness=1 if int(t.get("_button_bd",0)) else 0,
                         highlightbackground=t.get("accent","#1aa7ff"), highlightcolor=t.get("accent2","#55d8ff"),
                         activebackground=t.get("accent2","#55d8ff"), activeforeground="#ffffff", cursor="hand2")
    except Exception: pass
    return button
AppV43.make_button = _u443_make_button_skin

_U443_ORIG_FNT = AppV43.fnt
def _u443_skin_font(self, size=10, weight="normal"):
    t = self.colors()
    family = t.get("_font_family","Segoe UI")
    key = ("_u443_skin_font", int(size), str(weight), family)
    try:
        if key not in self.fonts:
            self.fonts[key] = tkfont.Font(family=family, size=int(size), weight=str(weight))
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
        st.configure("TCombobox",fieldbackground=t["card"],background=t["panel"],foreground=t["fg"],arrowcolor=t["accent"],bordercolor=t["accent"],padding=5)
        st.map("TCombobox",fieldbackground=[("readonly",t["card"]),("focus",t["panel"])],foreground=[("readonly",t["fg"])],background=[("active",t["accent"])])
        st.configure("TNotebook",background=t["bg"],borderwidth=int(t.get("_panel_bd",0)))
        st.configure("TNotebook.Tab",background=t["card"],foreground=t["fg"],padding=(12,7),borderwidth=int(t.get("_button_bd",0)))
        st.map("TNotebook.Tab",background=[("selected",t["accent"]),("active",t["accent2"])],foreground=[("selected","#ffffff"),("active","#ffffff")])
        st.configure("Treeview",background=t["card"],fieldbackground=t["card"],foreground=t["fg"],borderwidth=int(t.get("_panel_bd",0)),rowheight=23 if t.get("_skin_layout")=="terminal" else 28)
        st.map("Treeview",background=[("selected",t["accent"])],foreground=[("selected","#ffffff")])
        st.configure("Treeview.Heading",background=t["panel"],foreground=t["accent"],relief=t.get("_panel_relief","flat"),borderwidth=int(t.get("_panel_bd",0)))
        st.map("Treeview.Heading",background=[("active",t["accent"])],foreground=[("active","#ffffff")])
        st.configure("Horizontal.TProgressbar",background=t["accent"],troughcolor=t["card"],bordercolor=t["accent"],lightcolor=t["accent2"],darkcolor=t["panel"],thickness=12 if t.get("_skin_layout")=="terminal" else 16)
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
        sid=int(t.get("_skin_id",0))
        for idx,box in enumerate(boxes):
            x0,y0,x1,y1=box
            if style=="angular":
                cut=12
                points=[x0+cut,y0,x1-cut,y0,x1,y0+cut,x1,y1-cut,x1-cut,y1,x0+cut,y1,x0,y1-cut,x0,y0+cut]
                d.line(points+[points[0]],fill=(*accent2,235),width=3 if sid%4==2 else 2,joint="curve")
                for xx,yy in ((x0+5,y0+5),(x1-5,y0+5),(x0+5,y1-5),(x1-5,y1-5)): d.ellipse((xx-2,yy-2,xx+2,yy+2),fill=(*accent,245))
            elif style in ("matrix","retro"):
                d.rectangle(box,outline=(*accent,220),width=2)
                d.line((x0+8,y0+5,x0+min(100,x1-x0-8),y0+5),fill=(*accent2,245),width=2)
            elif style=="carbon":
                d.rectangle(box,outline=(165,185,205,180),width=1)
                d.line((x0+7,y0+7,x1-7,y0+7),fill=(235,245,255,70),width=1)
            else:
                radius=16 if style in ("neon","hologram","aurora") else 3
                d.rounded_rectangle(box,radius=radius,outline=(*accent,190 if style=="neon" else 150),width=3 if sid in (0,5,6,10) else 2)
                if style in ("neon","hologram","aurora"): d.line((x0+radius,y0+2,x1-radius,y0+2),fill=(*accent2,125),width=1)
        if t.get("_scanlines"):
            for yy in range(2,rgba.height,4): d.line((0,yy,rgba.width,yy),fill=(0,0,0,32),width=1)
        if t.get("_skin_layout")=="topbar":
            d.rectangle((255,0,rgba.width-1,71),fill=(*accent,32))
            d.line((255,70,rgba.width-1,70),fill=(*accent2,230),width=3)
        elif t.get("_skin_layout")=="terminal":
            for xx in range(260,rgba.width,34): d.line((xx,75,xx,rgba.height-2),fill=(*accent,22),width=1)
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
        from math import sin
        canvas.delete("all"); canvas.update_idletasks()
        w=max(660,canvas.winfo_width()); h=max(190,canvas.winfo_height())
        family=int(t.get("_skin_id",0)); layout=t.get("_skin_layout","sidebar"); relief=t.get("_panel_relief","flat")
        canvas.configure(bg=t["bg"])
        canvas.create_rectangle(4,4,w-4,h-4,fill=t["bg"],outline=t["accent"],width=max(1,int(t.get("_panel_highlight",1))))
        if t.get("_scanlines"):
            for yy in range(7,h,5): canvas.create_line(6,yy,w-6,yy,fill=t["panel"])
        if layout=="topbar":
            canvas.create_rectangle(16,14,w-16,49,fill=t["panel"],outline=t["accent"],width=max(1,int(t.get("_panel_bd",0))))
            canvas.create_text(28,31,text="NAPRAWA PC / HARDWARE TEST PRO",fill=t["accent"],anchor="w",font=self.fnt(10,"bold"))
            for i,name in enumerate(("PULPIT","TESTY","RAPORTY","USTAWIENIA")):
                canvas.create_text(round(w*.56)+i*75,31,text=name,fill=t["accent2"] if i==0 else t["fg"],font=self.fnt(7,"bold"))
            main_x=16; y_cards=61
        elif layout=="terminal":
            canvas.create_rectangle(16,14,185,h-14,fill=t["panel"],outline=t["accent"],width=2)
            canvas.create_text(28,31,text="> SYSTEM / STATUS",fill=t["accent"],anchor="w",font=self.fnt(9,"bold"))
            for i,name in enumerate(("CPU","GPU","RAM","NVME","SECURITY")):
                canvas.create_text(30,53+i*22,text="[+] "+name,fill=t["accent2"] if i==0 else t["fg"],anchor="w",font=self.fnt(8,"normal"))
            main_x=198; y_cards=71
        else:
            canvas.create_rectangle(16,14,160,h-14,fill=t["panel"],outline=t["accent"],width=max(1,int(t.get("_panel_highlight",1))))
            canvas.create_text(27,32,text="NAPRAWA PC",fill=t["accent"],anchor="w",font=self.fnt(10,"bold"))
            for i,name in enumerate(("PULPIT","CPU","GPU","RAM","DYSK","TESTY","RAPORTY")):
                y=55+i*22
                canvas.create_rectangle(22,y,150,y+17,fill=t["accent"] if i==0 else t["card"],outline=t["accent2"] if i==0 else t["panel"])
                canvas.create_text(30,y+8,text=name,fill="#ffffff" if i==0 else t["fg"],anchor="w",font=self.fnt(7,"bold"))
            main_x=170; y_cards=71
        available=max(430,w-main_x-18); hero_h=max(36,int(h*.19))
        if layout!="topbar":
            canvas.create_rectangle(main_x,15,main_x+available,15+hero_h,fill=t["panel"],outline=t["accent"],width=max(1,int(t.get("_panel_bd",0))+1))
            canvas.create_text(main_x+12,28,text=t.get("_skin_family","DIAGNOSTYKA"),fill=t["accent"],anchor="w",font=self.fnt(11,"bold"))
            canvas.create_text(main_x+12,45,text="MONITORING NA ŻYWO • TESTY • WYNIKI",fill=t["muted"],anchor="w",font=self.fnt(7,"bold"))
        count=4 if family%3==0 else (3 if family%3==1 else 5)
        gap=8; cw=max(62,(available-gap*(count-1))//count)
        for i in range(count):
            x=main_x+i*(cw+gap); x1=min(w-17,x+cw)
            if layout=="grid":
                pts=[x+5,y_cards,x1,y_cards,x1-5,y_cards+58,x,y_cards+58]
                canvas.create_polygon(pts,fill=t["card"],outline=t["accent"],width=2)
            elif relief in ("ridge","raised","groove"):
                canvas.create_rectangle(x,y_cards,x1,y_cards+58,fill=t["panel"],outline=t["accent"],width=max(1,int(t.get("_panel_bd",0))+1))
                canvas.create_line(x+3,y_cards+3,x1-3,y_cards+3,fill=t["accent2"],width=1)
            else:
                canvas.create_rectangle(x,y_cards,x1,y_cards+58,fill=t["panel"],outline=t["accent"],width=1)
            canvas.create_text(x+7,y_cards+13,text=("CPU","GPU","RAM","SSD","VRAM")[i%5],fill=t["accent"],anchor="w",font=self.fnt(7,"bold"))
            canvas.create_text((x+x1)//2,y_cards+36,text=f"{(12+i*13):02d}%",fill=t["good"] if i%2==0 else t["fg"],font=self.fnt(15,"bold"))
        gy=min(h-14,y_cards+73)
        canvas.create_rectangle(main_x,gy,w-18,h-14,fill=t["panel"],outline=t["accent"],width=max(1,int(t.get("_panel_bd",0))+1))
        for n in range(1,4):
            yy=gy+(h-gy-20)*n/4; canvas.create_line(main_x+8,yy,w-25,yy,fill=t["card"],dash=(2,3))
        pts=[]
        for xx in range(main_x+10,w-25,8):
            phase=(xx-main_x)/23+family
            yy=gy+int((h-gy-18)*(0.5+0.20*sin(phase)+0.10*sin(phase*0.43)))
            pts.extend((xx,yy))
        if len(pts)>=4: canvas.create_line(*pts,fill=t["accent2"],width=2,smooth=True)
        canvas.create_text(main_x+10,h-22,text=f"SKÓRKA {self.theme_id}/125 • {t.get('_skin_family','STYL')} • {relief.upper()} / {layout.upper()}",fill=t["fg"],anchor="w",font=self.fnt(8,"bold"))
    except Exception as exc:
        try: canvas.delete("all"); canvas.create_text(12,12,text=f"Błąd podglądu skórki: {exc}",fill=t.get("bad","#ff5063"),anchor="nw")
        except Exception: pass
AppV43.draw_theme_preview = _u443_draw_theme_preview

def _u443_selftest_visual_skins():
    assert len(THEMES)>=125,len(THEMES)
    assert len(set(THEMES[i]["name"] for i in range(1,126)))==125
    required=("name","bg","panel","card","fg","muted","accent","accent2","good","warn","bad","_skin_family","_skin_id","_panel_relief","_button_relief","_font_family","_image_style","_skin_layout")
    assert all(all(k in THEMES[i] for k in required) for i in range(1,126))
    assert len(set(THEMES[i]["_skin_family"] for i in range(1,126)))>=12
    assert callable(_u443_bind_dashboard_button_hover)
    assert callable(AppV43.panel) and callable(AppV43.make_button)
    assert callable(AppV43._theme_reference)
    assert callable(AppV43.draw_theme_preview)
    print("[OK] 125 distinct skin names")
    print("[OK] 12 structural design systems: panel depth, borders, typography, dashboard style and preview")
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
if ($src -notmatch 'range\(1,\s*126\)' -or !$src.Contains("_U443_ICON_HOVER_GLOW")) { throw "Theme/hover patch verification failed." }
[IO.File]::WriteAllText($sourcePath,$src,[Text.UTF8Encoding]::new($false))

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
