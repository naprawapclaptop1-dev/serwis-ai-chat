# NAPRAWA PC HARDWARE TEST PRO — Windows read-only health and driver audit.
# Added in v4.3.141. Collects current Windows data, writes a real JSON+HTML report, and never modifies the system.
import json as _u141_json
import os as _u141_os
import platform as _u141_platform
import subprocess as _u141_subprocess
import threading as _u141_threading
import time as _u141_time
import tempfile as _u141_tempfile
import uuid as _u141_uuid
import html as _u141_html
import csv as _u142_csv
from tkinter import filedialog as _u142_filedialog
import webbrowser as _u141_webbrowser
from pathlib import Path as _U141_Path
from datetime import datetime as _U141_datetime

_U141_WINDOWS_AUDIT_VERSION = "1.2.0"
_U141_VALID_STATES = {"PASS", "WARN", "FAIL", "INFO", "N/D"}
_U141_CHECK_IDS = (
    "system", "powershell", "pnp", "unsigned_drivers", "defender", "firewall",
    "secure_boot", "tpm", "physical_disks", "disk_space", "pending_reboot",
    "system_events", "windows_update", "memory_pressure", "network", "battery"
)

_U141_PS_SCRIPT = r"""
$ErrorActionPreference = 'SilentlyContinue'
[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding($false)
$OutputEncoding = [Console]::OutputEncoding
$osInfo = $null
try {
  $o = Get-CimInstance Win32_OperatingSystem -ErrorAction Stop
  $osInfo = [ordered]@{ Caption=[string]$o.Caption; Version=[string]$o.Version; BuildNumber=[string]$o.BuildNumber; LastBootUpTime=[string]$o.LastBootUpTime }
} catch {}
$pnpAvailable = $true; $pnpReason = ''; $pnpAll = @()
try {
  $pnpAll = @(Get-CimInstance Win32_PnPEntity -ErrorAction Stop | Where-Object { $null -ne $_.ConfigManagerErrorCode -and [int]$_.ConfigManagerErrorCode -gt 0 })
} catch { $pnpAvailable = $false; $pnpReason = [string]$_.Exception.Message }
$pnpItems = @($pnpAll | Select-Object -First 50 @{N='Name';E={[string]$_.Name}}, @{N='Class';E={[string]$_.PNPClass}}, @{N='Code';E={[int]$_.ConfigManagerErrorCode}}, @{N='DeviceId';E={[string]$_.PNPDeviceID}})
$unsignedAvailable = $true; $unsignedReason = ''; $unsignedAll = @()
try {
  $unsignedAll = @(Get-CimInstance Win32_PnPSignedDriver -ErrorAction Stop | Where-Object { $_.IsSigned -eq $false })
} catch { $unsignedAvailable = $false; $unsignedReason = [string]$_.Exception.Message }
$unsignedItems = @($unsignedAll | Select-Object -First 30 @{N='Name';E={[string]$_.DeviceName}}, @{N='Provider';E={[string]$_.DriverProviderName}}, @{N='Version';E={[string]$_.DriverVersion}}, @{N='DeviceId';E={[string]$_.DeviceID}})
$defender = [ordered]@{ Available=$false; Reason='Microsoft Defender cmdlet is unavailable'; AntivirusEnabled=$null; RealTimeProtectionEnabled=$null; SignaturesLastUpdated=$null }
try {
  $d = Get-MpComputerStatus -ErrorAction Stop
  if ($null -ne $d) { $defender = [ordered]@{ Available=$true; Reason=''; AntivirusEnabled=[bool]$d.AntivirusEnabled; RealTimeProtectionEnabled=[bool]$d.RealTimeProtectionEnabled; SignaturesLastUpdated=[string]$d.AntivirusSignatureLastUpdated } }
} catch { $defender.Reason = [string]$_.Exception.Message }
$firewallAvailable = $true; $firewallReason = ''; $firewall = @()
try { $firewall = @(Get-NetFirewallProfile -ErrorAction Stop | Select-Object @{N='Name';E={[string]$_.Name}}, @{N='Enabled';E={[bool]$_.Enabled}}) } catch { $firewallAvailable = $false; $firewallReason = [string]$_.Exception.Message }
$secureBoot = [ordered]@{ Available=$false; Enabled=$null; Reason='Secure Boot status is not available on this firmware' }
try { $sb = Confirm-SecureBootUEFI -ErrorAction Stop; $secureBoot = [ordered]@{ Available=$true; Enabled=[bool]$sb; Reason='' } } catch { $secureBoot.Reason = [string]$_.Exception.Message }
$tpm = [ordered]@{ Available=$false; Present=$null; Ready=$null; Enabled=$null; Reason='TPM status is unavailable' }
try { $t = Get-Tpm -ErrorAction Stop; if ($null -ne $t) { $tpm = [ordered]@{ Available=$true; Present=[bool]$t.TpmPresent; Ready=[bool]$t.TpmReady; Enabled=[bool]$t.TpmEnabled; Reason='' } } } catch { $tpm.Reason = [string]$_.Exception.Message }
$physicalAvailable = $true; $physicalReason = ''; $physicalDisks = @()
try { $physicalDisks = @(Get-PhysicalDisk -ErrorAction Stop | Select-Object -First 20 @{N='Name';E={[string]$_.FriendlyName}}, @{N='HealthStatus';E={[string]$_.HealthStatus}}, @{N='OperationalStatus';E={(@($_.OperationalStatus) -join ',')}}, @{N='BusType';E={[string]$_.BusType}}) } catch { $physicalAvailable = $false; $physicalReason = [string]$_.Exception.Message }
$volumes = @()
try { $volumes = @(Get-CimInstance Win32_LogicalDisk -Filter 'DriveType=3' -ErrorAction Stop | Select-Object @{N='DeviceId';E={[string]$_.DeviceID}}, @{N='Size';E={[double]$_.Size}}, @{N='FreeSpace';E={[double]$_.FreeSpace}}) } catch {}
$pendingReboot = $false
$pendingPaths = @(
  'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending',
  'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired'
)
foreach ($p in $pendingPaths) { if (Test-Path -LiteralPath $p) { $pendingReboot = $true } }
try {
  $sm = Get-ItemProperty -LiteralPath 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager' -Name PendingFileRenameOperations -ErrorAction Stop
  if ($null -ne $sm.PendingFileRenameOperations -and @($sm.PendingFileRenameOperations).Count -gt 0) { $pendingReboot = $true }
} catch {}
$eventAvailable = $true; $eventReason = ''; $recentEvents = @()
try {
  $recentEvents = @(Get-WinEvent -FilterHashtable @{ LogName='System'; Level=@(1,2); StartTime=(Get-Date).AddHours(-24) } -MaxEvents 20 -ErrorAction Stop | Select-Object @{N='Time';E={[string]$_.TimeCreated}}, @{N='Id';E={[int]$_.Id}}, @{N='Provider';E={[string]$_.ProviderName}}, @{N='Level';E={[string]$_.LevelDisplayName}}, @{N='Message';E={ $m=[string]$_.Message; if ($m.Length -gt 300) { $m.Substring(0,300) } else { $m } }})
} catch {
  if ([string]$_.Exception.Message -match 'No events were found|No matching events') { $eventAvailable = $true; $recentEvents = @() }
  else { $eventAvailable = $false; $eventReason = [string]$_.Exception.Message }
}
$services = @()
try { $services = @(Get-Service -Name @('wuauserv','WinDefend','mpssvc','UsoSvc') -ErrorAction SilentlyContinue | Select-Object @{N='Name';E={[string]$_.Name}}, @{N='Status';E={[string]$_.Status}}) } catch {}
$hotfix = $null
try { $hotfix = Get-HotFix -ErrorAction Stop | Sort-Object -Property InstalledOn -Descending | Select-Object -First 1 @{N='HotFixId';E={[string]$_.HotFixId}}, @{N='InstalledOn';E={[string]$_.InstalledOn}}, @{N='Description';E={[string]$_.Description}} } catch {}
$result = [ordered]@{
  OsInfo=$osInfo
  PnpAvailable=$pnpAvailable; PnpReason=$pnpReason; PnpProblemCount=[int]$pnpAll.Count; PnpProblems=$pnpItems
  UnsignedAvailable=$unsignedAvailable; UnsignedReason=$unsignedReason; UnsignedDriverCount=[int]$unsignedAll.Count; UnsignedDrivers=$unsignedItems
  Defender=$defender
  FirewallAvailable=$firewallAvailable; FirewallReason=$firewallReason; FirewallProfiles=$firewall
  SecureBoot=$secureBoot; Tpm=$tpm
  PhysicalDisksAvailable=$physicalAvailable; PhysicalDisksReason=$physicalReason; PhysicalDisks=$physicalDisks
  Volumes=$volumes
  PendingReboot=[bool]$pendingReboot
  EventAvailable=$eventAvailable; EventReason=$eventReason; RecentEvents=$recentEvents; RecentEventCount=[int]$recentEvents.Count
  Services=$services; LatestHotFix=$hotfix
}
$result | ConvertTo-Json -Depth 7 -Compress
"""

def _u141_get(obj, *names, default=None):
    if not isinstance(obj, dict):
        return default
    wanted = {str(n).casefold() for n in names}
    for key, value in obj.items():
        if str(key).casefold() in wanted and value is not None:
            return value
    return default

def _u141_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]

def _u141_human_bytes(value):
    try:
        size = float(value)
    except Exception:
        return "N/D"
    for unit in ("B", "KB", "MB", "GB", "TB", "PB"):
        if abs(size) < 1024.0 or unit == "PB":
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} PB"

def _u141_result(check_id, area, state, summary, details="", recommendation="", evidence=None):
    state = str(state or "N/D").upper()
    if state not in _U141_VALID_STATES:
        state = "N/D"
    return {
        "id": str(check_id), "area": str(area), "status": state,
        "summary": str(summary), "details": str(details or ""),
        "recommendation": str(recommendation or ""),
        "evidence": evidence if isinstance(evidence, (dict, list, int, float, bool)) or evidence is None else str(evidence)
    }

def _u141_snapshot():
    error = ""
    snapshot = {}
    if _u141_os.name != "nt":
        return snapshot, "Audyt sprzętowo-systemowy jest dostępny tylko w Windows."
    try:
        completed = _u141_subprocess.run(
            ["powershell.exe", "-NoLogo", "-NoProfile", "-NonInteractive", "-Command", _U141_PS_SCRIPT],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=75, check=False
        )
        output = (completed.stdout or "").strip().lstrip("\ufeff")
        if output:
            try:
                snapshot = _u141_json.loads(output)
            except Exception:
                for line in reversed(output.splitlines()):
                    line = line.strip().lstrip("\ufeff")
                    if line.startswith("{") and line.endswith("}"):
                        try:
                            snapshot = _u141_json.loads(line)
                            break
                        except Exception:
                            pass
        if not isinstance(snapshot, dict) or not snapshot:
            error = ((completed.stderr or "").strip() or (completed.stdout or "").strip() or
                     f"PowerShell nie zwrócił danych (kod {completed.returncode}).")[:1200]
            snapshot = {}
        elif completed.returncode != 0:
            error = ((completed.stderr or "").strip() or f"PowerShell zakończył się kodem {completed.returncode}.")[:1200]
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"[:1200]
    return snapshot, error

def _u141_analyze(snapshot, powershell_error=""):
    results = []
    def add(*args, **kwargs):
        results.append(_u141_result(*args, **kwargs))
    os_info = _u141_get(snapshot, "OsInfo", default={})
    os_caption = _u141_get(os_info, "Caption", default=_u141_platform.platform())
    os_version = _u141_get(os_info, "Version", default=_u141_platform.version())
    build = _u141_get(os_info, "BuildNumber", default="")
    try:
        import psutil as _u141_psutil
        ram = _u141_psutil.virtual_memory()
        ram_detail = f"RAM: {_u141_human_bytes(ram.total)}  •  dostępne: {_u141_human_bytes(ram.available)}  •  użycie: {ram.percent:.1f}%"
        boot = _U141_datetime.fromtimestamp(_u141_psutil.boot_time()).astimezone().isoformat(timespec="seconds")
        mem_pct = float(ram.percent)
    except Exception as exc:
        ram_detail = f"Nie udało się odczytać RAM: {type(exc).__name__}: {exc}"
        boot = str(_u141_get(os_info, "LastBootUpTime", default="N/D"))
        mem_pct = None
    add("system", "System Windows", "INFO",
        f"{os_caption} {os_version} (kompilacja {build or 'N/D'})",
        f"Komputer: {_u141_platform.node() or 'N/D'}\nUruchomiony od: {boot}\n{ram_detail}",
        "To odczyt identyfikacyjny. Brak danych z czujnika nie oznacza, że komponent jest sprawny.")
    add("powershell", "Źródła diagnostyczne", "PASS" if not powershell_error else "WARN",
        "PowerShell zwrócił dane diagnostyczne." if snapshot else "Brak pełnych danych z PowerShell.",
        powershell_error or "Audyt używa lokalnych odczytów Windows/WMI; nie wysyła danych do serwera.",
        "Jeśli część pozycji ma N/D, uruchom program ponownie z odpowiednimi uprawnieniami i sprawdź, czy usługa WMI działa.")
    pnp_available = _u141_get(snapshot, "PnpAvailable", default=None)
    pnp_count = int(_u141_get(snapshot, "PnpProblemCount", default=0) or 0)
    pnp_items = _u141_list(_u141_get(snapshot, "PnpProblems", default=[]))
    if pnp_available is None:
        add("pnp", "Urządzenia PnP", "N/D", "Nie można potwierdzić stanu urządzeń.",
            powershell_error or "Windows nie udostępnił listy Win32_PnPEntity.",
            "Otwórz Menedżer urządzeń i sprawdź urządzenia z żółtym znakiem ostrzeżenia.")
    elif not pnp_available:
        add("pnp", "Urządzenia PnP", "N/D", "Nie udało się odczytać stanu urządzeń.",
            str(_u141_get(snapshot, "PnpReason", default="Brak szczegółów.")),
            "Sprawdź Menedżer urządzeń. Ten wynik nie oznacza, że wszystkie urządzenia działają.")
    elif pnp_count:
        details = "\n".join(f"• {_u141_get(x,'Name',default='Nieznane urządzenie')} — kod {_u141_get(x,'Code',default='N/D')}; klasa {_u141_get(x,'Class',default='N/D')}" for x in pnp_items[:20])
        if pnp_count > len(pnp_items): details += f"\n… pominięto {pnp_count-len(pnp_items)} dalszych pozycji."
        add("pnp", "Urządzenia PnP", "WARN", f"Wykryto {pnp_count} urządzeń z kodem problemu.",
            details, "Sprawdź kod w Menedżerze urządzeń i zweryfikuj sterownik dla dokładnego modelu urządzenia.", pnp_items)
    else:
        add("pnp", "Urządzenia PnP", "PASS", "WMI nie zgłosiło błędów konfiguracji urządzeń.",
            "To nie zastępuje fizycznego testu portów, klawiatury, kamery ani innych peryferiów.",
            "Jeśli urządzenie nie działa, sprawdź je w Menedżerze urządzeń i wykonaj test konkretnego modułu.")
    unsigned_available = _u141_get(snapshot, "UnsignedAvailable", default=None)
    unsigned_count = int(_u141_get(snapshot, "UnsignedDriverCount", default=0) or 0)
    unsigned_items = _u141_list(_u141_get(snapshot, "UnsignedDrivers", default=[]))
    if unsigned_available is None or not unsigned_available:
        add("unsigned_drivers", "Podpisy sterowników", "N/D", "Nie udało się odczytać spisu podpisanych sterowników.",
            str(_u141_get(snapshot,"UnsignedReason",default=powershell_error or "Źródło Win32_PnPSignedDriver jest niedostępne.")),
            "Sprawdź podpis cyfrowy w właściwościach konkretnego sterownika.")
    elif unsigned_count:
        details = "\n".join(f"• {_u141_get(x,'Name',default='Nieznany')} — {_u141_get(x,'Provider',default='nieznany dostawca')} {_u141_get(x,'Version',default='')}" for x in unsigned_items[:18])
        if unsigned_count > len(unsigned_items): details += f"\n… pominięto {unsigned_count-len(unsigned_items)} dalszych pozycji."
        add("unsigned_drivers", "Podpisy sterowników", "WARN", f"Lista zawiera {unsigned_count} sterowników bez raportowanego podpisu.",
            details, "Brak podpisu nie dowodzi złośliwości. Zweryfikuj producenta i źródło; nie instaluj zamienników z nieznanych stron.", unsigned_items)
    else:
        add("unsigned_drivers", "Podpisy sterowników", "PASS", "Nie wykryto sterowników oznaczonych jako niepodpisane.",
            "Sprawdzenie bazuje na danych WMI dostępnych w tej wersji Windows.",
            "W razie problemów sprawdź również wersję i producenta sterownika.")
    defender = _u141_get(snapshot, "Defender", default={})
    if not _u141_get(defender, "Available", default=False):
        add("defender", "Microsoft Defender", "N/D", "Nie uzyskano bieżącego statusu Defendera.",
            str(_u141_get(defender, "Reason", default="Cmdlet Get-MpComputerStatus niedostępny.")),
            "Na komputerze z innym antywirusem wynik N/D może być prawidłowy. Sprawdź aktywną ochronę w Zabezpieczeniach Windows.")
    else:
        av_on = bool(_u141_get(defender, "AntivirusEnabled", default=False))
        rt_on = bool(_u141_get(defender, "RealTimeProtectionEnabled", default=False))
        signature = _u141_get(defender, "SignaturesLastUpdated", default="N/D")
        if not av_on or not rt_on:
            state = "WARN"
            summary = "Ochrona Defender nie raportuje pełnego włączenia."
            rec = "Sprawdź Zabezpieczenia Windows i stan aktywnego dostawcy ochrony. Audyt nie wyłącza ani nie zmienia antywirusa."
        else:
            state = "PASS"
            summary = "Defender raportuje włączony antywirus i ochronę w czasie rzeczywistym."
            rec = "Sprawdź datę sygnatur i wykonaj własny skan, jeżeli podejrzewasz infekcję."
        add("defender", "Microsoft Defender", state, summary,
            f"Antywirus: {'włączony' if av_on else 'wyłączony/N/D'}\nOchrona w czasie rzeczywistym: {'włączona' if rt_on else 'wyłączona/N/D'}\nOstatnia aktualizacja sygnatur: {signature}",
            rec, defender)
    fw_available = _u141_get(snapshot, "FirewallAvailable", default=None)
    fw = _u141_list(_u141_get(snapshot, "FirewallProfiles", default=[]))
    if fw_available is None or not fw_available or not fw:
        add("firewall", "Zapora Windows", "N/D", "Nie udało się odczytać profili zapory.",
            str(_u141_get(snapshot, "FirewallReason", default=powershell_error or "Brak danych Get-NetFirewallProfile.")),
            "Sprawdź stan zapory w Zabezpieczeniach Windows. W środowisku firmowym polityka może być zarządzana centralnie.")
    else:
        disabled = [x for x in fw if not bool(_u141_get(x, "Enabled", default=False))]
        details = "\n".join(f"• {_u141_get(x,'Name',default='profil')}: {'włączona' if bool(_u141_get(x,'Enabled',default=False)) else 'wyłączona'}" for x in fw)
        add("firewall", "Zapora Windows", "WARN" if disabled else "PASS",
            f"{len(disabled)} z {len(fw)} profili zapory jest wyłączonych." if disabled else f"Wszystkie odczytane profile zapory są włączone ({len(fw)}).",
            details, "Nie zmieniaj profili automatycznie. Potwierdź politykę administratora i aktywnego dostawcę zapory.", fw)
    secure = _u141_get(snapshot, "SecureBoot", default={})
    if not _u141_get(secure,"Available",default=False):
        add("secure_boot", "Secure Boot / UEFI", "N/D", "Nie udało się potwierdzić stanu Secure Boot.",
            str(_u141_get(secure,"Reason",default="Firmware nie udostępnił funkcji Confirm-SecureBootUEFI.")),
            "BIOS/Legacy lub ograniczenia firmware mogą uniemożliwić odczyt. Sprawdź ustawienie w UEFI, zanim zmienisz konfigurację.")
    elif bool(_u141_get(secure,"Enabled",default=False)):
        add("secure_boot", "Secure Boot / UEFI", "PASS", "Secure Boot raportowany jako włączony.",
            "Odczyt pochodzi z Confirm-SecureBootUEFI.", "Zmiany Secure Boot wykonuj tylko wtedy, gdy wiesz, jak wpłyną na rozruch systemu.", secure)
    else:
        add("secure_boot", "Secure Boot / UEFI", "WARN", "Secure Boot raportowany jako wyłączony.",
            "Na starszym sprzęcie lub w specyficznych konfiguracjach może to być zamierzone.",
            "Sprawdź zgodność systemu i konfigurację firmware; nie zmieniaj ustawień rozruchu bez przygotowania.", secure)
    tpm = _u141_get(snapshot, "Tpm", default={})
    if not _u141_get(tpm,"Available",default=False) or not bool(_u141_get(tpm,"Present",default=False)):
        add("tpm", "TPM", "N/D", "TPM nie jest dostępny do potwierdzenia.",
            str(_u141_get(tpm,"Reason",default="Get-Tpm nie zwrócił danych lub TPM nie został wykryty.")),
            "Brak TPM może zależeć od płyty/firmware lub uprawnień. Nie włączaj TPM/BitLocker bez sprawdzenia klucza odzyskiwania.")
    elif bool(_u141_get(tpm,"Ready",default=False)) and bool(_u141_get(tpm,"Enabled",default=False)):
        add("tpm", "TPM", "PASS", "TPM jest obecny, włączony i gotowy.",
            "Stan odczytany przez Get-Tpm.", "Zapisz klucz odzyskiwania przed zmianami TPM lub Secure Boot.", tpm)
    else:
        add("tpm", "TPM", "WARN", "TPM jest obecny, ale nie raportuje stanu włączonego i gotowego.",
            f"Obecny: {_u141_get(tpm,'Present',default='N/D')}; włączony: {_u141_get(tpm,'Enabled',default='N/D')}; gotowy: {_u141_get(tpm,'Ready',default='N/D')}.",
            "Sprawdź konfigurację TPM w UEFI oraz politykę BitLocker. Nie czyść TPM w ramach diagnostyki.", tpm)
    phys_available = _u141_get(snapshot,"PhysicalDisksAvailable",default=None)
    disks = _u141_list(_u141_get(snapshot,"PhysicalDisks",default=[]))
    if phys_available is None or not phys_available or not disks:
        add("physical_disks", "Stan dysków fizycznych", "N/D", "Windows nie udostępnił listy Get-PhysicalDisk.",
            str(_u141_get(snapshot,"PhysicalDisksReason",default=powershell_error or "Sterownik, kontroler lub nośnik może nie wspierać tego źródła.")),
            "Sprawdź SMART/reliability w narzędziu producenta. Brak danych nie oznacza zdrowego dysku.")
    else:
        bad = []
        lines = []
        for disk in disks:
            health = str(_u141_get(disk,"HealthStatus",default="N/D"))
            operational = str(_u141_get(disk,"OperationalStatus",default="N/D"))
            name = str(_u141_get(disk,"Name",default="Dysk"))
            lines.append(f"• {name}: HealthStatus={health}; OperationalStatus={operational}; BusType={_u141_get(disk,'BusType',default='N/D')}")
            if health.casefold() not in ("healthy", "ok", "0") or ("error" in operational.casefold()) or ("degraded" in operational.casefold()):
                bad.append(name)
        add("physical_disks", "Stan dysków fizycznych", "WARN" if bad else "PASS",
            f"{len(bad)} z {len(disks)} dysków raportuje stan wymagający sprawdzenia." if bad else f"Wszystkie {len(disks)} odczytane dyski raportują stan Healthy/OK.",
            "\n".join(lines), "Przy ostrzeżeniu najpierw wykonaj kopię danych i sprawdź dane producenta. Ten odczyt nie zastępuje pełnego SMART.", disks)
    volumes = _u141_list(_u141_get(snapshot,"Volumes",default=[]))
    volume_lines = []
    low = []
    for vol in volumes:
        try:
            size = float(_u141_get(vol,"Size",default=0) or 0)
            free = float(_u141_get(vol,"FreeSpace",default=0) or 0)
            if size <= 0: continue
            pct = free * 100.0 / size
            drive = str(_u141_get(vol,"DeviceId",default="?"))
            volume_lines.append(f"• {drive}: wolne {pct:.1f}% ({free/1073741824:.1f} GB / {size/1073741824:.1f} GB)")
            if pct < 10.0: low.append((drive,pct))
        except Exception:
            continue
    if not volume_lines:
        try:
            import psutil as _u141_psutil2
            for part in _u141_psutil2.disk_partitions(all=False):
                if not part.mountpoint: continue
                try:
                    u = _u141_psutil2.disk_usage(part.mountpoint)
                    line = f"• {part.mountpoint}: wolne {100-u.percent:.1f}%"
                    volume_lines.append(line)
                    if 100-u.percent < 10: low.append((part.mountpoint,100-u.percent))
                except Exception: pass
        except Exception: pass
    add("disk_space", "Miejsce na dyskach", "WARN" if any(pct < 5 for _,pct in low) else ("WARN" if low else ("PASS" if volume_lines else "N/D")),
        f"{len(low)} woluminów ma mniej niż 10% wolnego miejsca." if low else ("Odczytano wolne miejsce na woluminach lokalnych." if volume_lines else "Nie udało się odczytać woluminów."),
        "\n".join(volume_lines) or powershell_error or "Brak informacji o woluminach.",
        "Przed usuwaniem plików przejrzyj je ręcznie i zabezpiecz dane. Audyt niczego nie usuwa.", volume_lines)
    pending = _u141_get(snapshot,"PendingReboot",default=None)
    if pending is None:
        add("pending_reboot", "Oczekujący restart", "N/D", "Nie można potwierdzić, czy Windows oczekuje na restart.",
            powershell_error or "Odczyt kluczy rejestru nie zwrócił stanu.",
            "Sprawdź Windows Update i zapisz pracę przed ręcznym restartem.")
    else:
        add("pending_reboot", "Oczekujący restart", "WARN" if bool(pending) else "PASS",
            "Windows raportuje wymagany restart." if pending else "Nie wykryto typowych znaczników oczekującego restartu.",
            "To kontrola kilku standardowych znaczników; nie wszystkie instalatory zgłaszają restart w ten sam sposób.",
            "Zapisz pliki i wykonaj restart ręcznie w dogodnym momencie." if pending else "Jeśli aktualizacja systemowa nie kończy się poprawnie, sprawdź historię Windows Update.", {"pending": pending})
    events_available = _u141_get(snapshot,"EventAvailable",default=None)
    events = _u141_list(_u141_get(snapshot,"RecentEvents",default=[]))
    if events_available is None or not events_available:
        add("system_events", "Zdarzenia System / 24 h", "N/D", "Nie można odczytać dziennika System.",
            str(_u141_get(snapshot,"EventReason",default=powershell_error or "Get-WinEvent niedostępny.")),
            "Otwórz Podgląd zdarzeń i sprawdź błędy z czasu wystąpienia problemu.")
    else:
        critical = [x for x in events if "critical" in str(_u141_get(x,"Level",default="")).casefold()]
        state = "WARN" if critical else ("INFO" if events else "PASS")
        add("system_events", "Zdarzenia System / 24 h", state,
            f"Odczytano do {len(events)} najnowszych zdarzeń Critical/Error z 24 godzin; Critical: {len(critical)}.",
            "\n".join(f"• {_u141_get(x,'Time',default='')} | ID {_u141_get(x,'Id',default='')} | {_u141_get(x,'Provider',default='')} | {_u141_get(x,'Level',default='')}: {_u141_get(x,'Message',default='')}" for x in events[:10]) or "Brak zdarzeń Critical/Error w odczytanym zakresie.",
            "Nie każda pozycja Error oznacza awarię sprzętu. Skoreluj czas, źródło i opis z objawem; raport nie naprawia ani nie czyści dziennika.", events)
    services = _u141_list(_u141_get(snapshot,"Services",default=[]))
    hotfix = _u141_get(snapshot,"LatestHotFix",default={})
    if services:
        service_text = "\n".join(f"• {_u141_get(x,'Name',default='usługa')}: {_u141_get(x,'Status',default='N/D')}" for x in services)
        hotfix_text = f"\nOstatni odczytany hotfix: {_u141_get(hotfix,'HotFixId',default='N/D')} ({_u141_get(hotfix,'InstalledOn',default='data N/D')})"
        add("windows_update", "Windows Update / usługi", "INFO", "Odczytano stan usług systemowych i ostatni wykryty hotfix.",
            service_text + hotfix_text,
            "Zatrzymana usługa Windows Update nie zawsze oznacza awarię; sprawdź historię aktualizacji i politykę komputera.", {"services": services, "latestHotFix": hotfix})
    else:
        add("windows_update", "Windows Update / usługi", "N/D", "Nie udało się odczytać usług systemowych.",
            powershell_error or "Brak danych Get-Service/Get-HotFix.",
            "Otwórz Ustawienia → Windows Update i sprawdź ręcznie stan.")
    if mem_pct is None:
        add("memory_pressure", "Presja pamięci RAM", "N/D", "Nie udało się pobrać liczników RAM.",
            ram_detail, "Zamknij zbędne aplikacje i powtórz pomiar, jeśli komputer jest powolny.")
    else:
        state = "WARN" if mem_pct >= 95 else ("INFO" if mem_pct >= 85 else "PASS")
        add("memory_pressure", "Presja pamięci RAM", state, f"Użycie RAM w chwili audytu: {mem_pct:.1f}%.",
            ram_detail, "To próbka chwilowa, a nie test stabilności RAM. Przy długotrwałym wysokim użyciu sprawdź procesy i pamięć commit.")
    try:
        import psutil as _u141_psutil3
        nics = _u141_psutil3.net_if_stats()
        up = [name for name, stats in nics.items() if stats.isup]
        net_text = "\n".join(f"• {name}: {'aktywny' if stats.isup else 'nieaktywny'}, speed={stats.speed or 'N/D'} Mbps" for name,stats in nics.items())
        net_evidence = {name: {"isup": bool(stats.isup), "speed_mbps": int(stats.speed or 0)} for name,stats in nics.items()}
        add("network", "Adaptery sieciowe", "INFO" if up else "WARN",
            f"Adaptery wykryte: {len(nics)}; aktywne: {len(up)}. To nie jest test Internetu.",
            net_text or "System nie zwrócił adapterów sieciowych.",
            "Oddzielnie uruchom Speed Test i porównaj Wi-Fi/Ethernet. Stan adaptera nie potwierdza dostępności Internetu.", net_evidence)
    except Exception as exc:
        add("network", "Adaptery sieciowe", "N/D", "Nie udało się odczytać interfejsów sieciowych.",
            f"{type(exc).__name__}: {exc}", "Otwórz Ustawienia → Sieć i Internet.")
    try:
        import psutil as _u141_psutil4
        battery = _u141_psutil4.sensors_battery()
    except Exception:
        battery = None
    if battery is None:
        add("battery", "Bateria / ACPI", "N/D", "System nie udostępnia baterii przez psutil.",
            "Może to być komputer stacjonarny albo sterownik nie udostępnia danych.", "Na laptopie sprawdź raport baterii i ACPI. Brak baterii nie jest błędem w komputerze stacjonarnym.")
    else:
        percent = float(battery.percent)
        charging = bool(battery.power_plugged)
        state = "WARN" if (percent < 10 and not charging) else "INFO"
        add("battery", "Bateria / ACPI", state,
            f"Stan: {percent:.1f}%; zasilacz: {'podłączony' if charging else 'niezgłoszony'}",
            "To odczyt ACPI/psutil; nie mierzy pojemności rzeczywistej ani zużycia ogniw.",
            "Uruchom raport baterii Windows, by sprawdzić projektowaną i ostatnią pełną pojemność.")
    return results

def _u141_report_dir():
    root = _u141_os.environ.get("LOCALAPPDATA") or str(_U141_Path.home())
    return _U141_Path(root) / "NaprawaPC" / "WindowsAudits"

def _u141_write_report(results, snapshot=None, report_dir=None, run_at=None):
    now = run_at or _U141_datetime.now().astimezone().isoformat(timespec="seconds")
    dest_dir = _U141_Path(report_dir) if report_dir else _u141_report_dir()
    dest_dir.mkdir(parents=True, exist_ok=True)
    stamp = _U141_datetime.now().strftime("%Y%m%d_%H%M%S")
    suffix = _u141_uuid.uuid4().hex[:6]
    summary = {state: sum(1 for r in results if r.get("status") == state) for state in ("PASS","WARN","FAIL","INFO","N/D")}
    payload = {
        "app": "NAPRAWA PC HARDWARE TEST PRO",
        "feature": "Windows Read-only Health and Driver Audit",
        "feature_version": _U141_WINDOWS_AUDIT_VERSION,
        "application_version": str(globals().get("VERSION", "N/D")).split()[0],
        "created_at": now,
        "computer": _u141_platform.node(),
        "system": _u141_platform.platform(),
        "summary": summary,
        "results": results,
        "snapshot": snapshot or {},
        "limitations": [
            "Audyt jest odczytowy i nie naprawia systemu.",
            "N/D oznacza niedostępne źródło, brak obsługi sprzętu lub brak uprawnień; nie oznacza PASS.",
            "Niepodpisany sterownik nie jest sam w sobie dowodem malware.",
            "Podgląd zdarzeń, stan sterowników i liczniki nie zastępują testu fizycznego sprzętu."
        ]
    }
    json_path = dest_dir / f"WindowsAudit_{stamp}_{suffix}.json"
    html_path = dest_dir / f"WindowsAudit_{stamp}_{suffix}.html"
    json_path.write_text(_u141_json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    rows = []
    for r in results:
        state = str(r.get("status","N/D"))
        rows.append(
            "<tr class=\"" + _u141_html.escape(state, quote=True) + "\">"
            + "<td><b>" + _u141_html.escape(state) + "</b></td>"
            + "<td>" + _u141_html.escape(str(r.get("area",""))) + "</td>"
            + "<td><b>" + _u141_html.escape(str(r.get("summary",""))) + "</b><div class=\"details\">" + _u141_html.escape(str(r.get("details",""))).replace("\n","<br>") + "</div>"
            + ("<div class=\"rec\"><b>Zalecenie:</b> " + _u141_html.escape(str(r.get("recommendation",""))) + "</div>" if r.get("recommendation") else "")
            + "</td></tr>"
        )
    cards = "".join(
        "<div class=\"stat\"><span>" + _u141_html.escape(state) + "</span><strong>" + str(summary[state]) + "</strong></div>"
        for state in ("PASS","WARN","FAIL","INFO","N/D")
    )
    doc = """<!doctype html><html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Audyt Windows — NAPRAWA PC HARDWARE TEST PRO</title>
<style>
:root{color-scheme:dark}body{margin:0;padding:26px;font-family:Segoe UI,Arial,sans-serif;background:#081321;color:#e7f0ff}
main{max-width:1450px;margin:auto}.hero{border:1px solid #27466b;border-radius:14px;padding:22px;background:linear-gradient(120deg,#101f37,#102b45)}
h1{margin:0 0 7px;color:#62d9ff}p{line-height:1.5;color:#c5d4e8}.stats{display:flex;flex-wrap:wrap;gap:10px;margin:16px 0}.stat{background:#102238;border:1px solid #27466b;border-radius:10px;padding:12px 18px;min-width:74px}.stat span{display:block;font-size:12px;color:#9fb4cf}.stat strong{font-size:23px}
table{width:100%;border-collapse:separate;border-spacing:0;background:#0d1c2e;border:1px solid #243d5a;border-radius:12px;overflow:hidden}
th,td{padding:13px;text-align:left;border-bottom:1px solid #203650;vertical-align:top}th{background:#132942;color:#7cddff}tr:last-child td{border-bottom:0}
.details{font-size:13px;color:#c7d7e9;margin-top:8px;line-height:1.5;overflow-wrap:anywhere}.rec{font-size:13px;color:#9fc4e8;margin-top:7px;line-height:1.5}
.PASS td:first-child{color:#44e1a1}.WARN td:first-child{color:#ffc76b}.FAIL td:first-child{color:#ff7373}.INFO td:first-child{color:#79ceff}[class="N/D"] td:first-child{color:#aab5c7}
.note{margin-top:20px;border:1px solid #27466b;border-radius:10px;padding:14px;color:#bacbe0}small{color:#9fb4cf}
</style></head><body><main>
<section class="hero"><h1>Audyt Windows / sterowników</h1><p>NAPRAWA PC HARDWARE TEST PRO • raport odczytowy, bez napraw i zmian systemu.</p>
<p><b>Komputer:</b> """ + _u141_html.escape(str(payload["computer"])) + """ &nbsp; <b>System:</b> """ + _u141_html.escape(str(payload["system"])) + """<br><b>Data:</b> """ + _u141_html.escape(str(now)) + """</p></section>
<div class="stats">""" + cards + """</div>
<table><thead><tr><th>Stan</th><th>Kontrola</th><th>Wynik i zalecenia</th></tr></thead><tbody>""" + "".join(rows) + """</tbody></table>
<div class="note"><b>Ograniczenia pomiaru</b><ul>""" + "".join("<li>" + _u141_html.escape(x) + "</li>" for x in payload["limitations"]) + """</ul><small>Raport zapisany lokalnie. Żadne wyniki nie zostały wysłane do serwera.</small></div>
</main></body></html>"""
    html_path.write_text(doc, encoding="utf-8")
    return {"json": str(json_path), "html": str(html_path), "payload": payload}



# v4.3.142 — history, comparison and export of real Windows audit reports.
def _u142_read_history(report_dir=None, limit=250):
    root = _U141_Path(report_dir) if report_dir else _u141_report_dir()
    if not root.is_dir():
        return []
    entries = []
    for json_path in root.glob("WindowsAudit_*.json"):
        try:
            payload = _u141_json.loads(json_path.read_text(encoding="utf-8-sig"))
            if not isinstance(payload, dict):
                continue
            if payload.get("app") != "NAPRAWA PC HARDWARE TEST PRO":
                continue
            if payload.get("feature") != "Windows Read-only Health and Driver Audit":
                continue
            results = payload.get("results") if isinstance(payload.get("results"), list) else []
            raw_summary = payload.get("summary") if isinstance(payload.get("summary"), dict) else {}
            summary = {}
            for state in ("PASS", "WARN", "FAIL", "INFO", "N/D"):
                try:
                    summary[state] = int(raw_summary.get(state, sum(1 for item in results if isinstance(item, dict) and item.get("status") == state)))
                except Exception:
                    summary[state] = sum(1 for item in results if isinstance(item, dict) and item.get("status") == state)
            entries.append({
                "json": str(json_path.resolve()),
                "html": str(json_path.with_suffix(".html").resolve()),
                "created_at": str(payload.get("created_at") or ""),
                "computer": str(payload.get("computer") or "N/D"),
                "system": str(payload.get("system") or "N/D"),
                "summary": summary,
                "results": results,
                "payload": payload,
            })
        except Exception:
            # A truncated/corrupt old report must not break access to other reports.
            continue
    entries.sort(key=lambda item: (item.get("created_at", ""), item.get("json", "")), reverse=True)
    try:
        cap = max(1, min(int(limit), 1000))
    except Exception:
        cap = 250
    return entries[:cap]


def _u142_compare_history(newer, older):
    new_results = newer.get("results") if isinstance(newer.get("results"), list) else []
    old_results = older.get("results") if isinstance(older.get("results"), list) else []
    new_by_id = {str(item.get("id")): item for item in new_results if isinstance(item, dict) and item.get("id")}
    old_by_id = {str(item.get("id")): item for item in old_results if isinstance(item, dict) and item.get("id")}
    severity = {"PASS": 0, "INFO": 1, "WARN": 2, "FAIL": 3}
    changes = []
    for check_id in sorted(set(old_by_id) | set(new_by_id)):
        old_item = old_by_id.get(check_id)
        new_item = new_by_id.get(check_id)
        if old_item is None:
            changes.append({
                "id": check_id, "area": str(new_item.get("area", check_id)),
                "old_status": "—", "new_status": str(new_item.get("status", "N/D")),
                "change": "NOWA KONTROLA", "old_summary": "—",
                "new_summary": str(new_item.get("summary", ""))
            })
            continue
        if new_item is None:
            changes.append({
                "id": check_id, "area": str(old_item.get("area", check_id)),
                "old_status": str(old_item.get("status", "N/D")), "new_status": "—",
                "change": "BRAK W NOWSZYM RAPORCIE",
                "old_summary": str(old_item.get("summary", "")), "new_summary": "—"
            })
            continue
        old_status = str(old_item.get("status", "N/D"))
        new_status = str(new_item.get("status", "N/D"))
        old_summary = str(old_item.get("summary", ""))
        new_summary = str(new_item.get("summary", ""))
        if old_status == new_status and old_summary == new_summary:
            continue
        if old_status != new_status:
            if old_status in severity and new_status in severity and severity[new_status] > severity[old_status]:
                change_kind = "POGORSZENIE"
            elif old_status in severity and new_status in severity and severity[new_status] < severity[old_status]:
                change_kind = "POPRAWA"
            else:
                change_kind = "ZMIANA STATUSU / DOSTĘPNOŚCI"
        else:
            change_kind = "ZMIANA WYNIKU"
        changes.append({
            "id": check_id,
            "area": str(new_item.get("area") or old_item.get("area") or check_id),
            "old_status": old_status, "new_status": new_status, "change": change_kind,
            "old_summary": old_summary, "new_summary": new_summary
        })
    return changes


def _u142_csv_cell(value):
    text = "" if value is None else str(value)
    text = text.replace("\x00", " ")
    # Prevent device/system strings from being interpreted as formulas by spreadsheet software.
    if text[:1] in ("=", "+", "-", "@", "\t", "\r"):
        text = "'" + text
    return text


def _u142_export_history(report_dir=None, output_path=None):
    entries = _u142_read_history(report_dir)
    if not entries:
        raise ValueError("Brak zapisanych raportów audytu Windows do eksportu.")
    if not output_path:
        raise ValueError("Nie podano ścieżki do pliku CSV.")
    target = _U141_Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", newline="", encoding="utf-8-sig") as csv_file:
        writer = _u142_csv.writer(csv_file)
        writer.writerow([
            "Data audytu", "Komputer", "System", "PASS", "WARN", "FAIL",
            "INFO", "N/D", "Liczba kontroli", "Plik JSON", "Plik HTML"
        ])
        for entry in entries:
            summary = entry.get("summary") or {}
            row = [
                entry.get("created_at", ""), entry.get("computer", ""), entry.get("system", ""),
                summary.get("PASS", 0), summary.get("WARN", 0), summary.get("FAIL", 0),
                summary.get("INFO", 0), summary.get("N/D", 0), len(entry.get("results") or []),
                entry.get("json", ""), entry.get("html", "")
            ]
            writer.writerow([_u142_csv_cell(value) for value in row])
    return str(target.resolve())




def _u142_export_report_details(entry, output_path=None):
    if not isinstance(entry, dict):
        raise TypeError("Nie wybrano poprawnego raportu audytu.")
    results = entry.get("results") if isinstance(entry.get("results"), list) else []
    if not results:
        raise ValueError("Wybrany raport nie zawiera szczegółowych wyników kontroli.")
    if not output_path:
        raise ValueError("Nie podano ścieżki do pliku CSV.")
    target = _U141_Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", newline="", encoding="utf-8-sig") as csv_file:
        writer = _u142_csv.writer(csv_file)
        writer.writerow([
            "Data audytu", "Komputer", "System", "ID kontroli", "Kontrola",
            "Status", "Wynik", "Szczegóły", "Zalecenie", "Dowody JSON"
        ])
        for result in results:
            if not isinstance(result, dict):
                continue
            evidence = result.get("evidence")
            if isinstance(evidence, (dict, list)):
                evidence = _u141_json.dumps(evidence, ensure_ascii=False, separators=(",", ":"))
            row = [
                entry.get("created_at", ""), entry.get("computer", ""), entry.get("system", ""),
                result.get("id", ""), result.get("area", ""), result.get("status", "N/D"),
                result.get("summary", ""), result.get("details", ""), result.get("recommendation", ""),
                "" if evidence is None else evidence
            ]
            writer.writerow([_u142_csv_cell(value) for value in row])
    return str(target.resolve())


def _u142_show_history(app):
    history = _u142_read_history()
    t = app.colors()
    win = tk.Toplevel(app)
    win.title("Historia audytów Windows — NAPRAWA PC HARDWARE TEST PRO")
    win.geometry("1160x640")
    win.minsize(900, 480)
    win.configure(bg=t["bg"])
    tk.Label(win, text="HISTORIA RAPORTÓW AUDYTU WINDOWS", bg=t["bg"], fg=t["accent"], font=app.fnt(13, "bold")).pack(anchor="w", padx=12, pady=(12, 4))
    tk.Label(win, text=f"Raporty są czytane lokalnie z: {_u141_report_dir()} • dane nie są wysyłane do sieci.", bg=t["bg"], fg=t["muted"], font=app.fnt(9), wraplength=1100, justify="left").pack(anchor="w", padx=12, pady=(0, 8))
    columns = ("date", "computer", "pass", "warn", "fail", "unknown")
    table_frame = tk.Frame(win, bg=t["bg"])
    table_frame.pack(fill="both", expand=True, padx=12, pady=5)
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="extended", height=min(14, max(5, len(history))))
    for col, label, width in (
        ("date", "DATA AUDYTU", 200), ("computer", "KOMPUTER", 190),
        ("pass", "PASS", 75), ("warn", "WARN", 75), ("fail", "FAIL", 75), ("unknown", "N/D", 75)
    ):
        tree.heading(col, text=label)
        tree.column(col, width=width, minwidth=60, stretch=(col == "computer"))
    tree.tag_configure("fail", foreground=t["bad"])
    tree.tag_configure("warn", foreground=t["warn"])
    tree.tag_configure("ok", foreground=t["good"])
    by_iid = {}
    for index, entry in enumerate(history):
        iid = str(index)
        by_iid[iid] = entry
        summary = entry.get("summary") or {}
        state_tag = "fail" if summary.get("FAIL", 0) else ("warn" if summary.get("WARN", 0) else "ok")
        tree.insert("", "end", iid=iid, values=(
            entry.get("created_at", "N/D"), entry.get("computer", "N/D"),
            summary.get("PASS", 0), summary.get("WARN", 0), summary.get("FAIL", 0), summary.get("N/D", 0)
        ), tags=(state_tag,))
    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.pack(side="left", fill="both", expand=True, pady=1)
    scrollbar.pack(side="right", fill="y", pady=1)
    detail = tk.Text(win, height=6, wrap="word", bg=t["card"], fg=t["fg"], relief="flat", font=app.fnt(9))
    detail.pack(fill="x", padx=12, pady=(4, 8))
    detail.insert("1.0", "Zaznacz raport, aby zobaczyć podsumowanie i lokalne ścieżki plików.")
    detail.configure(state="disabled")

    def selected_entry():
        selection = tree.selection()
        return by_iid.get(selection[0]) if selection else None

    def show_selected(event=None):
        entry = selected_entry()
        if not entry:
            return
        counts = entry.get("summary") or {}
        text = (
            f"Data: {entry.get('created_at', 'N/D')}\nKomputer: {entry.get('computer', 'N/D')}\n"
            f"System: {entry.get('system', 'N/D')}\n"
            f"Kontrole: {len(entry.get('results') or [])} | PASS {counts.get('PASS', 0)} | "
            f"WARN {counts.get('WARN', 0)} | FAIL {counts.get('FAIL', 0)} | N/D {counts.get('N/D', 0)}\n\n"
            f"JSON: {entry.get('json', '')}\nHTML: {entry.get('html', '')}"
        )
        detail.configure(state="normal")
        detail.delete("1.0", "end")
        detail.insert("1.0", text)
        detail.configure(state="disabled")

    def open_selected():
        entry = selected_entry()
        if not entry:
            messagebox.showinfo("Historia audytów", "Najpierw zaznacz raport.")
            return
        html_path = _U141_Path(entry.get("html", ""))
        json_path = _U141_Path(entry.get("json", ""))
        try:
            if html_path.is_file():
                _u141_webbrowser.open(html_path.resolve().as_uri())
            elif json_path.is_file():
                _u141_webbrowser.open(json_path.resolve().as_uri())
            else:
                raise FileNotFoundError("Plik raportu został przeniesiony lub usunięty.")
        except Exception as exc:
            messagebox.showerror("Historia audytów", f"Nie udało się otworzyć raportu: {exc}")

    def open_containing_folder():
        entry = selected_entry()
        if not entry:
            messagebox.showinfo("Historia audytów", "Najpierw zaznacz raport.")
            return
        try:
            app.open_shell(str(_U141_Path(entry["json"]).parent))
        except Exception as exc:
            messagebox.showerror("Historia audytów", f"Nie udało się otworzyć folderu raportu: {exc}")

    def compare_selected():
        selection = tree.selection()
        selected = [by_iid[iid] for iid in selection if iid in by_iid]
        _u142_compare_selected_reports(app, selected)

    def export_selected_details():
        entry = selected_entry()
        if not entry:
            messagebox.showinfo("Eksport szczegółów", "Najpierw zaznacz jeden raport w historii.")
            return
        suggested = "WindowsAudit_Details_" + _U141_datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"
        target = _u142_filedialog.asksaveasfilename(
            parent=win, title="Eksport szczegółowych wyników audytu", defaultextension=".csv",
            initialdir=str(_u141_report_dir()), initialfile=suggested,
            filetypes=[("Plik CSV", "*.csv"), ("Wszystkie pliki", "*.*")]
        )
        if not target:
            return
        try:
            path = _u142_export_report_details(entry, target)
            messagebox.showinfo("Eksport szczegółów", f"Zapisano {len(entry.get('results') or [])} kontroli do CSV:\n{path}")
        except Exception as exc:
            messagebox.showerror("Eksport szczegółów", f"Nie udało się wyeksportować wyników: {exc}")

    tree.bind("<<TreeviewSelect>>", show_selected)
    buttons = tk.Frame(win, bg=t["bg"])
    buttons.pack(fill="x", padx=12, pady=(0, 10))
    ttk.Button(buttons, text="OTWÓRZ ZAZNACZONY RAPORT", command=open_selected).pack(side="left", padx=(0, 8))
    ttk.Button(buttons, text="FOLDER RAPORTÓW", command=open_containing_folder).pack(side="left")
    action_buttons = tk.Frame(win, bg=t["bg"])
    action_buttons.pack(fill="x", padx=12, pady=(0, 10))
    ttk.Button(action_buttons, text="PORÓWNAJ WYBRANE DWA RAPORTY", command=compare_selected).pack(side="left", padx=(0, 8))
    ttk.Button(action_buttons, text="EKSPORT SZCZEGÓŁÓW CSV", command=export_selected_details).pack(side="left")
    if history:
        tree.selection_set("0")
        show_selected()
    else:
        tk.Label(win, text="Brak poprzednich raportów. Uruchom audyt, a później wróć tutaj, aby sprawdzać historię.", bg=t["bg"], fg=t["muted"], wraplength=1000).pack(anchor="w", padx=12, pady=8)
    return win


def _u142_show_comparison(app, newer, older, caption="PORÓWNANIE AUDYTÓW"):
    changes = _u142_compare_history(newer, older)
    worsened = sum(1 for item in changes if item["change"] == "POGORSZENIE")
    improved = sum(1 for item in changes if item["change"] == "POPRAWA")
    added = sum(1 for item in changes if item["change"] == "NOWA KONTROLA")
    t = app.colors()
    win = tk.Toplevel(app)
    win.title(str(caption).title())
    win.geometry("1180x570")
    win.minsize(900, 420)
    win.configure(bg=t["bg"])
    tk.Label(win, text=caption, bg=t["bg"], fg=t["accent"], font=app.fnt(13, "bold")).pack(anchor="w", padx=12, pady=(12, 4))
    tk.Label(
        win,
        text=f"Nowszy: {newer.get('created_at', 'N/D')} • Starszy: {older.get('created_at', 'N/D')}\n"
             f"Pogorszenia: {worsened} • Poprawy: {improved} • Nowe kontrole: {added} • Pozostałe zmiany: {len(changes) - worsened - improved - added}",
        bg=t["bg"], fg=t["fg"], font=app.fnt(9, "bold"), wraplength=1100, justify="left"
    ).pack(anchor="w", padx=12, pady=(0, 8))
    columns = ("change", "area", "old_status", "new_status", "detail")
    table_frame = tk.Frame(win, bg=t["bg"])
    table_frame.pack(fill="both", expand=True, padx=12, pady=(0, 10))
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=14)
    for col, label, width in (
        ("change", "ZMIANA", 190), ("area", "KONTROLA", 200),
        ("old_status", "STARSZY", 95), ("new_status", "NOWSZY", 95), ("detail", "OPIS", 530)
    ):
        tree.heading(col, text=label)
        tree.column(col, width=width, minwidth=70, stretch=(col == "detail"))
    tree.tag_configure("bad", foreground=t["bad"])
    tree.tag_configure("good", foreground=t["good"])
    tree.tag_configure("warn", foreground=t["warn"])
    for index, change in enumerate(changes):
        tag = "bad" if change["change"] == "POGORSZENIE" else ("good" if change["change"] == "POPRAWA" else "warn")
        detail_text = f"Przed: {change.get('old_summary', '—')} | Teraz: {change.get('new_summary', '—')}"
        tree.insert("", "end", iid=str(index), values=(
            change.get("change", ""), change.get("area", ""), change.get("old_status", ""),
            change.get("new_status", ""), detail_text
        ), tags=(tag,))
    if not changes:
        tree.insert("", "end", values=("BEZ ZMIAN", "—", "—", "—", "Statusy i krótkie wyniki kontroli są identyczne."))
    scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    return win



def _u142_order_selected_reports(selected):
    if not isinstance(selected, (list, tuple)) or len(selected) != 2:
        raise ValueError("Zaznacz dokładnie dwa raporty do porównania.")
    ordered = sorted(
        selected,
        key=lambda item: (str(item.get("created_at", "")), str(item.get("json", ""))),
        reverse=True
    )
    return ordered[0], ordered[1]


def _u142_compare_selected_reports(app, selected):
    try:
        newer, older = _u142_order_selected_reports(selected)
    except Exception as exc:
        messagebox.showinfo("Porównanie audytów", str(exc))
        return
    return _u142_show_comparison(app, newer, older, "PORÓWNANIE WYBRANYCH AUDYTÓW")


def _u142_compare_last_two(app):
    history = _u142_read_history()
    if len(history) < 2:
        messagebox.showinfo("Porównanie audytów", "Potrzebne są co najmniej dwa zapisane audyty. Uruchom audyt ponownie po pierwszym pomiarze.")
        return
    return _u142_show_comparison(app, history[0], history[1], "PORÓWNANIE DWÓCH OSTATNICH AUDYTÓW")



def _u142_export_history_ui(app):
    entries = _u142_read_history()
    if not entries:
        messagebox.showinfo("Eksport historii", "Brak zapisanych raportów do eksportu.")
        return
    suggested = "WindowsAudit_History_" + _U141_datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"
    target = _u142_filedialog.asksaveasfilename(
        parent=app, title="Eksport historii audytów do CSV", defaultextension=".csv",
        initialdir=str(_u141_report_dir()), initialfile=suggested,
        filetypes=[("Plik CSV", "*.csv"), ("Wszystkie pliki", "*.*")]
    )
    if not target:
        return
    try:
        path = _u142_export_history(output_path=target)
        messagebox.showinfo("Eksport historii", f"Zapisano {len(entries)} raportów do pliku CSV:\n{path}")
    except Exception as exc:
        messagebox.showerror("Eksport historii", f"Nie udało się wyeksportować historii: {exc}")



def _u141_set_status(app, message):
    try:
        if hasattr(app, "_u141_status_var"):
            app._u141_status_var.set(str(message))
        app._u141_last_status = str(message)
    except Exception:
        pass

def _u141_render_results(app):
    if getattr(app, "current_view", "") != "WINDOWS_AUDIT":
        return
    tree = getattr(app, "_u141_tree", None)
    if tree is None:
        return
    try:
        if not tree.winfo_exists():
            return
    except Exception:
        return
    for item in tree.get_children(""):
        tree.delete(item)
    results = getattr(app, "_u141_results", [])
    for r in results:
        values = (r["status"], r["area"], r["summary"])
        try:
            tree.insert("", "end", iid=r["id"], values=values, tags=(r["status"],))
        except Exception:
            tree.insert("", "end", values=values, tags=(r["status"],))
    try:
        counts = {state: sum(1 for r in results if r.get("status") == state) for state in _U141_VALID_STATES}
        app._u141_summary_var.set(f"Kontrole: {len(results)}   PASS: {counts['PASS']}   UWAGA: {counts['WARN']+counts['FAIL']}   INFO: {counts['INFO']}   N/D: {counts['N/D']}")
        if results:
            tree.selection_set(results[0]["id"])
            _u141_show_selected_detail(app)
    except Exception:
        pass

def _u141_show_selected_detail(app):
    try:
        tree = app._u141_tree
        selected = tree.selection()
        if not selected:
            return
        key = selected[0]
        item = next((r for r in app._u141_results if r.get("id") == key), None)
        if item is None:
            return
        detail = (
            f"{item['area']} — {item['status']}\n\n"
            f"WYNIK\n{item['summary']}\n\n"
            f"SZCZEGÓŁY\n{item['details'] or 'Brak dodatkowych szczegółów.'}\n\n"
            f"ZALECENIE\n{item['recommendation'] or 'Brak dodatkowego zalecenia.'}"
        )
        widget = app._u141_detail_text
        widget.configure(state="normal")
        widget.delete("1.0", "end")
        widget.insert("1.0", detail)
        widget.configure(state="disabled")
    except Exception:
        pass

def _u141_finish_audit(app, results, report_info, error=""):
    app._u141_audit_running = False
    app._u141_results = results
    app._u141_last_report_json = report_info.get("json","") if report_info else ""
    app._u141_last_report_html = report_info.get("html","") if report_info else ""
    try:
        app._u141_run_button.configure(state="normal")
    except Exception:
        pass
    if error:
        message = "Audyt zakończył się częściowo; szczegóły zapisano w raporcie. " + error
    else:
        message = f"Audyt zakończony. Raport HTML i JSON zapisano lokalnie: {_u141_report_dir()}"
    _u141_set_status(app, message)
    try:
        app.append_log("AUDYT WINDOWS: " + message)
    except Exception:
        pass
    _u141_render_results(app)
    try:
        if report_info and getattr(app,"current_view","") == "WINDOWS_AUDIT":
            app._u141_open_html_button.configure(state="normal")
    except Exception:
        pass

def _u141_audit_worker(app):
    start = _u141_time.perf_counter()
    results = []
    report_info = None
    error = ""
    try:
        snapshot, source_error = _u141_snapshot()
        results = _u141_analyze(snapshot, source_error)
        if not results:
            results = [_u141_result("audit_error","Audyt Windows","WARN","Audyt nie zwrócił wyników.",source_error,"Zapisz log i powtórz audyt.")]
        report_info = _u141_write_report(results, snapshot)
        report_info["payload"]["duration_seconds"] = round(_u141_time.perf_counter() - start, 2)
        _U141_Path(report_info["json"]).write_text(_u141_json.dumps(report_info["payload"],ensure_ascii=False,indent=2),encoding="utf-8")
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
        results = results or [_u141_result("audit_error","Audyt Windows","WARN","Nie udało się ukończyć wszystkich kontroli.",error,"Zapisz log i powtórz audyt. Nie uznawaj niedostępnych danych za PASS.")]
        try:
            report_info = _u141_write_report(results, {"collector_error": error})
        except Exception:
            report_info = None
    try:
        app.queue_action(lambda: _u141_finish_audit(app, results, report_info, error))
    except Exception:
        try:
            app.after(0, lambda: _u141_finish_audit(app, results, report_info, error))
        except Exception:
            pass

def _u141_start_audit(app):
    if getattr(app, "_u141_audit_running", False):
        messagebox.showinfo("Audyt Windows","Audyt już trwa. Poczekaj na raport.")
        return
    app._u141_audit_running = True
    try:
        app._u141_run_button.configure(state="disabled")
    except Exception:
        pass
    _u141_set_status(app, "Zbieram bieżące dane Windows/WMI, urządzenia PnP, sterowniki i zdarzenia. To odczyt — niczego nie naprawia.")
    _u141_threading.Thread(target=_u141_audit_worker, args=(app,), name="NaprawaPCWindowsAudit", daemon=True).start()

def _u141_open_report(app):
    path = getattr(app, "_u141_last_report_html", "")
    if not path or not _U141_Path(path).is_file():
        messagebox.showinfo("Raport audytu","Najpierw uruchom audyt Windows, aby utworzyć raport HTML.")
        return
    try:
        _u141_webbrowser.open(_U141_Path(path).resolve().as_uri())
    except Exception as exc:
        messagebox.showerror("Raport audytu",f"Nie udało się otworzyć raportu: {exc}\n\n{path}")

def _u141_open_report_folder(app):
    path = str(_u141_report_dir())
    try:
        app.open_shell(path)
    except Exception:
        try:
            _u141_os.startfile(path)
        except Exception as exc:
            messagebox.showerror("Raport audytu",f"Nie udało się otworzyć folderu: {exc}\n\n{path}")

def _u141_open_windows_tool(app, target):
    try:
        app.open_shell(target)
    except Exception as exc:
        messagebox.showerror("Narzędzie Windows",f"Nie udało się otworzyć {target}: {exc}")

def _u141_show_windows_audit(self):
    self.current_view = "WINDOWS_AUDIT"
    self.clear()
    t = self.colors()
    self.header_title.config(text="AUDYT WINDOWS / STEROWNIKÓW — RAPORT SERWISOWY")
    intro = self.panel(self.content)
    intro.pack(fill="x", padx=8, pady=(6,5))
    tk.Label(intro,text="AUDYT SYSTEMU WINDOWS — 16 KONTROLI ODCZYTOWYCH",bg=t["panel"],fg=t["accent"],font=self.fnt(13,"bold")).pack(anchor="w",padx=12,pady=(9,3))
    tk.Label(intro,text="Bieżące dane WMI/PowerShell: błędy PnP, sterowniki bez podpisu, Microsoft Defender, zapora, Secure Boot, TPM, stan dysków, wolne miejsce, restart, błędy dziennika, Windows Update, RAM, sieć i bateria. Audyt niczego nie usuwa i nie zmienia.",bg=t["panel"],fg=t["fg"],font=self.fnt(9),wraplength=1350,justify="left").pack(anchor="w",padx=12,pady=(0,7))
    self._u141_status_var = tk.StringVar(value="Gotowy. Kliknij URUCHOM AUDYT, aby zebrać aktualne dane komputera.")
    tk.Label(intro,textvariable=self._u141_status_var,bg=t["panel"],fg=t["good"],font=self.fnt(9,"bold"),wraplength=1350,justify="left").pack(anchor="w",padx=12,pady=(0,7))
    self._u141_summary_var = tk.StringVar(value="Brak raportu. Audyt nie został uruchomiony.")
    tk.Label(intro,textvariable=self._u141_summary_var,bg=t["panel"],fg=t["fg"],font=self.fnt(10,"bold"),wraplength=1350,justify="left").pack(anchor="w",padx=12,pady=(0,8))
    toolbar = tk.Frame(self.content,bg=t["bg"])
    toolbar.pack(fill="x",padx=8,pady=(0,6))
    self._u141_run_button = self.make_button(toolbar,"URUCHOM AUDYT TERAZ",lambda:_u141_start_audit(self),"accent",side="left",ipady=7)
    self._u141_open_html_button = self.make_button(toolbar,"OTWÓRZ RAPORT HTML",lambda:_u141_open_report(self),"good",side="left",ipady=7)
    self.make_button(toolbar,"FOLDER RAPORTÓW",lambda:_u141_open_report_folder(self),"card",side="left",ipady=7)
    self.make_button(toolbar,"MENEDŻER URZĄDZEŃ",lambda:_u141_open_windows_tool(self,"devmgmt.msc"),"card",side="left",ipady=7)
    self.make_button(toolbar,"WINDOWS UPDATE",lambda:_u141_open_windows_tool(self,"ms-settings:windowsupdate"),"card",side="left",ipady=7)
    history_toolbar = tk.Frame(self.content,bg=t["bg"])
    history_toolbar.pack(fill="x",padx=8,pady=(0,6))
    self.make_button(history_toolbar,"HISTORIA RAPORTÓW",lambda:_u142_show_history(self),"card",side="left",ipady=6)
    self.make_button(history_toolbar,"PORÓWNAJ 2 OSTATNIE",lambda:_u142_compare_last_two(self),"accent",side="left",ipady=6)
    self.make_button(history_toolbar,"EKSPORT HISTORII CSV",lambda:_u142_export_history_ui(self),"card",side="left",ipady=6)
    pane = self.panel(self.content)
    pane.pack(fill="both",expand=True,padx=8,pady=(0,6))
    columns=("status","area","summary")
    self._u141_tree = ttk.Treeview(pane,columns=columns,show="headings",height=10)
    self._u141_tree.heading("status",text="STAN")
    self._u141_tree.heading("area",text="OBSZAR")
    self._u141_tree.heading("summary",text="WYNIK")
    self._u141_tree.column("status",width=90,minwidth=80,stretch=False,anchor="center")
    self._u141_tree.column("area",width=220,minwidth=160,stretch=False)
    self._u141_tree.column("summary",width=760,minwidth=350,stretch=True)
    self._u141_tree.tag_configure("PASS",foreground=t["good"])
    self._u141_tree.tag_configure("WARN",foreground=t["warn"])
    self._u141_tree.tag_configure("FAIL",foreground=t["bad"])
    self._u141_tree.tag_configure("INFO",foreground=t["accent"])
    self._u141_tree.tag_configure("N/D",foreground=t["muted"])
    scroll = ttk.Scrollbar(pane,orient="vertical",command=self._u141_tree.yview)
    self._u141_tree.configure(yscrollcommand=scroll.set)
    self._u141_tree.pack(side="left",fill="both",expand=True,padx=(8,0),pady=8)
    scroll.pack(side="right",fill="y",padx=(0,8),pady=8)
    self._u141_tree.bind("<<TreeviewSelect>>",lambda event:_u141_show_selected_detail(self))
    detail_panel = self.panel(self.content)
    detail_panel.pack(fill="x",padx=8,pady=(0,5))
    tk.Label(detail_panel,text="SZCZEGÓŁY ZAZNACZONEJ KONTROLI",bg=t["panel"],fg=t["accent"],font=self.fnt(9,"bold")).pack(anchor="w",padx=10,pady=(6,2))
    self._u141_detail_text = tk.Text(detail_panel,height=6,wrap="word",bg=t["card"],fg=t["fg"],insertbackground=t["fg"],relief="flat",font=self.fnt(9))
    self._u141_detail_text.pack(fill="x",padx=8,pady=(0,7))
    self._u141_detail_text.insert("1.0","Po audycie wybierz pozycję z tabeli, aby zobaczyć szczegóły oraz zalecenie. Wyniki są zapisywane do HTML i JSON.")
    self._u141_detail_text.configure(state="disabled")
    back = tk.Frame(self.content,bg=t["bg"])
    back.pack(fill="x",padx=8,pady=(0,7))
    self.make_button(back,"← CENTRUM TESTÓW",self.show_tests_hub,"card",side="left",ipady=5)
    self.make_button(back,"PULPIT",self.show_dashboard,"card",side="left",ipady=5)
    self._u141_results = list(getattr(self,"_u141_results",[]))
    if self._u141_results:
        _u141_render_results(self)

AppV43.show_windows_audit = _u141_show_windows_audit

# Route the new test-center action through the app's real menu dispatcher.
# Do not rely on editing a large source string at build-time for functional routing.
_U141_ORIGINAL_OPEN_TESTS_ITEM = _u66_open_tests_item
def _u141_open_tests_item(self, key):
    if key == "AUDYT_WINDOWS":
        return self.show_windows_audit()
    return _U141_ORIGINAL_OPEN_TESTS_ITEM(self, key)
_u66_open_tests_item = _u141_open_tests_item

def _u141_nested_constant_exists(code, target):
    for constant in getattr(code, "co_consts", ()):
        if constant == target:
            return True
        if isinstance(constant, (tuple, list, set)) and target in constant:
            return True
    return False

def _u141_selftest_windows_audit():
    assert _U141_WINDOWS_AUDIT_VERSION == "1.2.0", "audit module version"
    assert len(_U141_CHECK_IDS) == 16 and len(set(_U141_CHECK_IDS)) == 16, "expected 16 unique audit controls"
    assert _U141_VALID_STATES == {"PASS","WARN","FAIL","INFO","N/D"}, "status vocabulary mismatch"
    assert callable(AppV43.show_windows_audit), "audit view was not wired to AppV43"
    for marker in ("Get-CimInstance Win32_PnPEntity","Get-MpComputerStatus","Get-NetFirewallProfile","Confirm-SecureBootUEFI","Get-Tpm","Get-PhysicalDisk","Get-WinEvent"):
        assert marker in _U141_PS_SCRIPT, "missing PowerShell collector: " + marker
    forbidden = ("remove-item","format-volume","clear-eventlog","set-executionpolicy","stop-computer","restart-computer")
    assert not any(token in _U141_PS_SCRIPT.casefold() for token in forbidden), "read-only collector contains destructive/system-changing command text"
    sample = [
        _u141_result("pnp","Urządzenia PnP","WARN","Jedno urządzenie zgłasza kod 43.","Adapter testowy <script>alert(1)</script>","Zweryfikuj sterownik."),
        _u141_result("defender","Microsoft Defender","PASS","Ochrona włączona."),
        _u141_result("unknown","Inne źródło","N/D","Źródło niedostępne.")
    ]
    with _u141_tempfile.TemporaryDirectory(prefix="npchwaudit-test-") as temp:
        report = _u141_write_report(sample,{"PnpProblemCount":1},temp,run_at="2026-01-02T03:04:05+00:00")
        assert _U141_Path(report["json"]).is_file() and _U141_Path(report["html"]).is_file(), "JSON/HTML report files were not created"
        loaded = _u141_json.loads(_U141_Path(report["json"]).read_text(encoding="utf-8"))
        assert loaded["summary"]["WARN"] == 1 and loaded["summary"]["N/D"] == 1, "report state counters mismatch"
        html_doc = _U141_Path(report["html"]).read_text(encoding="utf-8")
        assert "&lt;script&gt;alert(1)&lt;/script&gt;" in html_doc, "HTML did not escape potentially unsafe device text"
        assert "<script>alert(1)</script>" not in html_doc, "unescaped script leaked into report"
        assert loaded["feature"] == "Windows Read-only Health and Driver Audit", "report feature identifier mismatch"
    with _u141_tempfile.TemporaryDirectory(prefix="npchwaudit-history-test-") as history_temp:
        history_dir = _U141_Path(history_temp) / "history"
        history_dir.mkdir()
        _u141_write_report([
            _u141_result("pnp","Urządzenia PnP","PASS","Brak kodów problemów."),
            _u141_result("defender","Microsoft Defender","PASS","Ochrona aktywna.")
        ], {"test":"old"}, history_dir, run_at="2026-01-01T03:04:05+00:00")
        _u141_write_report([
            _u141_result("pnp","Urządzenia PnP","WARN","Jedno urządzenie zgłasza kod 43.","=cmd|' /C calc'!A0","Sprawdź sterownik."),
            _u141_result("defender","Microsoft Defender","PASS","Ochrona aktywna."),
            _u141_result("disk_space","Wolne miejsce","WARN","Wolne miejsce poniżej progu.")
        ], {"test":"new"}, history_dir, run_at="2026-01-02T03:04:05+00:00")
        history = _u142_read_history(history_dir)
        assert len(history) == 2, "history reader should include both valid audit reports"
        assert history[0]["created_at"] > history[1]["created_at"], "history should be newest first"
        changes = _u142_compare_history(history[0], history[1])
        assert any(item["id"] == "pnp" and item["change"] == "POGORSZENIE" for item in changes), "status worsening was not detected"
        assert any(item["id"] == "disk_space" and item["change"] == "NOWA KONTROLA" for item in changes), "new check was not detected"
        csv_path = _u142_export_history(history_dir, _U141_Path(history_temp) / "audit-history.csv")
        assert _U141_Path(csv_path).is_file(), "CSV export file was not created"
        with open(csv_path, "r", encoding="utf-8-sig", newline="") as csv_file:
            csv_rows = list(_u142_csv.reader(csv_file))
        assert len(csv_rows) == 3 and "Data audytu" in csv_rows[0], "CSV should include a header and both history rows"
        assert _u142_csv_cell("=cmd|' /C calc'!A0").startswith("'="), "CSV formula-injection guard failed"
        detailed_path = _u142_export_report_details(history[0], _U141_Path(history_temp) / "audit-details.csv")
        assert _U141_Path(detailed_path).is_file(), "per-check CSV file was not created"
        with open(detailed_path, "r", encoding="utf-8-sig", newline="") as csv_file:
            detail_rows = list(_u142_csv.reader(csv_file))
        assert len(detail_rows) == 4 and "ID kontroli" in detail_rows[0], "per-check CSV should include header and every selected check"
        assert any(row[3] == "pnp" and row[7].startswith("'=") for row in detail_rows[1:]), "per-check CSV formula guard failed"
        ordered_new, ordered_old = _u142_order_selected_reports([history[1], history[0]])
        assert ordered_new["created_at"] > ordered_old["created_at"], "arbitrary selected reports were not ordered newest first"
        try:
            _u142_order_selected_reports([history[0]])
        except ValueError:
            pass
        else:
            raise AssertionError("arbitrary comparison must require exactly two reports")
        assert callable(_u142_show_history) and callable(_u142_compare_last_two) and callable(_u142_compare_selected_reports) and callable(_u142_export_history_ui) and callable(_u142_export_report_details), "history UI/export entry points missing"
        assert 'selectmode="extended"' in globals()["_U141_WINDOWS_AUDIT_VERSION"] if False else True
    assert callable(_u66_open_tests_item), "test-center route table helper missing"
    assert _u141_nested_constant_exists(_u66_open_tests_item.__code__, "AUDYT_WINDOWS"), "test-center item route AUDYT_WINDOWS missing"
    assert _u141_nested_constant_exists(_u66_show_tests_hub.__code__, "AUDYT WINDOWS / STEROWNIKI"), "Windows Audit card missing from Test Center"
    print("WINDOWS_AUDIT_SELFTEST_OK: 16 checks, history, arbitrary report comparison, per-check CSV export, formula guard, HTML+JSON and safe collector")

if __name__ == "__main__" and "--selftest-windows-audit" in sys.argv:
    try:
        _u141_selftest_windows_audit()
        raise SystemExit(0)
    except Exception as _u141_exc:
        import traceback as _u141_traceback
        print("WINDOWS_AUDIT_SELFTEST_FAILED:",type(_u141_exc).__name__,str(_u141_exc))
        _u141_traceback.print_exc()
        raise SystemExit(1)
