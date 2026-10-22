# Quality core: full-buffer RAM verification and live CPU measurement.
import os as _u146_os
import time as _u146_time
import ctypes as _u146_ctypes
import hashlib as _u146_hashlib
import threading as _u146_threading
import json as _u146_json
from pathlib import Path as _u146_Path

_U146_QUALITY_PATCH_VERSION = "1.0.0"
_U146_RAM_PATTERNS = (0x00, 0xFF, 0xAA, 0x55)
_U40_RAM_PATTERN_LIST = _U146_RAM_PATTERNS
_U146_EXPECTED_DIGESTS = {}

def _u146_stopped(check):
    if not callable(check):
        return False
    try:
        return bool(check())
    except Exception:
        return False

def _u146_progress(callback, percent, message):
    if callable(callback):
        try:
            callback(max(0, min(100, int(percent))), str(message))
        except Exception:
            pass

def _u146_expected_digest(size, pattern, stop_check=None):
    key = (int(size), int(pattern))
    if key in _U146_EXPECTED_DIGESTS:
        return _U146_EXPECTED_DIGESTS[key]
    digest = _u146_hashlib.sha256()
    block_size = min(8 * 1024 * 1024, max(1, int(size)))
    block = bytes((int(pattern),)) * block_size
    offset = 0
    while offset < size:
        if _u146_stopped(stop_check):
            raise InterruptedError("Test RAM zatrzymany podczas przygotowania wzorca.")
        length = min(block_size, size - offset)
        digest.update(block[:length])
        offset += length
    result = digest.digest()
    if len(_U146_EXPECTED_DIGESTS) >= 24:
        _U146_EXPECTED_DIGESTS.clear()
    _U146_EXPECTED_DIGESTS[key] = result
    return result

def _u146_verify_ram_buffer(buffer, seconds=0, progress_callback=None, stop_check=None, stats_out=None):
    started = _u146_time.monotonic()
    view = memoryview(buffer)
    size = len(view)
    if size <= 0:
        raise ValueError("Bufor RAM ma zerowy rozmiar.")
    ptr = _u146_ctypes.addressof(_u146_ctypes.c_ubyte.from_buffer(buffer))
    stats = {"size_mb": round(size / 1048576, 2), "patterns_total": len(_U146_RAM_PATTERNS),
             "patterns_completed": 0, "passes": 0, "bytes_written": 0, "bytes_verified": 0,
             "elapsed_sec": 0.0, "stopped": False, "allocation_failed": False, "error_offset": None}
    chunk_size = 8 * 1024 * 1024
    duration = max(0.0, min(900.0, float(seconds or 0)))
    passes = 0
    try:
        while passes == 0 or (duration > 0 and _u146_time.monotonic() - started < duration):
            for pattern_index, pattern in enumerate(_U146_RAM_PATTERNS):
                if _u146_stopped(stop_check):
                    stats["stopped"] = True
                    stats["elapsed_sec"] = round(_u146_time.monotonic() - started, 3)
                    if stats_out is not None: stats_out.update(stats)
                    return False, "Test RAM zatrzymany przez użytkownika."
                expected = _u146_expected_digest(size, pattern, stop_check)
                _u146_ctypes.memset(ptr, pattern, size)
                stats["bytes_written"] += size
                actual = _u146_hashlib.sha256()
                verified = 0
                while verified < size:
                    if _u146_stopped(stop_check):
                        stats["stopped"] = True
                        stats["elapsed_sec"] = round(_u146_time.monotonic() - started, 3)
                        if stats_out is not None: stats_out.update(stats)
                        return False, "Test RAM zatrzymany podczas weryfikacji."
                    end = min(size, verified + chunk_size)
                    actual.update(view[verified:end])
                    verified = end
                    if verified == size or (verified // chunk_size) % 4 == 0:
                        within = verified / max(1, size)
                        percent = int(((pattern_index + 0.15 + 0.85 * within) / len(_U146_RAM_PATTERNS)) * 100)
                        _u146_progress(progress_callback, percent,
                            f"Wzorzec {pattern:02X}: zweryfikowano {verified / 1048576:.0f}/{size / 1048576:.0f} MB.")
                stats["bytes_verified"] += size
                if actual.digest() != expected:
                    bad_offset = None
                    for scan_start in range(0, size, chunk_size):
                        segment = bytes(view[scan_start:min(size, scan_start + chunk_size)])
                        mismatch = next((i for i, value in enumerate(segment) if value != pattern), None)
                        if mismatch is not None:
                            bad_offset = scan_start + mismatch
                            break
                    stats["error_offset"] = bad_offset
                    stats["failed_pattern"] = f"{pattern:02X}"
                    stats["elapsed_sec"] = round(_u146_time.monotonic() - started, 3)
                    if stats_out is not None: stats_out.update(stats)
                    return False, f"Niezgodność pełnego wzorca 0x{pattern:02X}; błędny bajt: {bad_offset if bad_offset is not None else 'N/D'}."
                stats["patterns_completed"] += 1
            passes += 1
            stats["passes"] = passes
            stats["elapsed_sec"] = round(_u146_time.monotonic() - started, 3)
            if duration <= 0 or _u146_stopped(stop_check):
                break
        stats["stopped"] = bool(_u146_stopped(stop_check))
        stats["elapsed_sec"] = round(_u146_time.monotonic() - started, 3)
        if stats_out is not None: stats_out.update(stats)
        if stats["stopped"]:
            return False, f"Test RAM przerwany po {stats['patterns_completed']} sprawdzonych wzorcach."
        _u146_progress(progress_callback, 100,
            f"ZAKOŃCZONO • {stats['patterns_completed']} kontroli wzorców • {stats['elapsed_sec']:.1f} s.")
        return True, (f"OK — pełny zapis i weryfikacja wzorców 00/FF/AA/55; "
                      f"{stats['size_mb']:.0f} MB • {passes} przebieg(ów) • {stats['elapsed_sec']:.1f} s.")
    finally:
        try: view.release()
        except Exception: pass

def ram_pattern_test(mb, seconds=0, progress_callback=None, stop_check=None, stats_out=None):
    try:
        requested = max(64, min(2048, int(mb or 512)))
        vm = psutil.virtual_memory() if globals().get("psutil") is not None else None
        available_mb = int(vm.available / 1048576) if vm is not None else 512
        if vm is not None and available_mb < 192:
            if stats_out is not None:
                stats_out.update({"size_mb": 0, "patterns_total": len(_U146_RAM_PATTERNS), "patterns_completed": 0,
                    "passes": 0, "bytes_written": 0, "bytes_verified": 0, "allocation_failed": True,
                    "stopped": False, "elapsed_sec": 0.0})
            return False, f"Za mało dostępnej pamięci RAM ({available_mb} MB); test nie wystartował, aby chronić Windows."
        safe_mb = min(requested, max(64, min(1024, int(available_mb * 0.15))))
        buffer = bytearray(safe_mb * 1048576)
        local_stats = {}
        ok, message = _u146_verify_ram_buffer(buffer, seconds, progress_callback, stop_check, local_stats)
        local_stats.update({"requested_mb": requested, "size_mb": safe_mb, "available_mb_at_start": available_mb})
        if stats_out is not None: stats_out.update(local_stats)
        return ok, message
    except MemoryError:
        if stats_out is not None:
            stats_out.update({"allocation_failed": True, "patterns_total": len(_U146_RAM_PATTERNS),
                "patterns_completed": 0, "bytes_written": 0, "bytes_verified": 0, "stopped": False})
        return False, "Nie udało się przydzielić bufora RAM."
    except InterruptedError as exc:
        if stats_out is not None: stats_out.update({"stopped": True, "allocation_failed": False})
        return False, str(exc)
    except Exception as exc:
        if stats_out is not None: stats_out.update({"error": f"{type(exc).__name__}: {exc}"})
        return False, f"{type(exc).__name__}: {exc}"

def _u146_save_quality_report(module, test_id, report):
    try:
        root = _u146_Path(_u146_os.environ.get("LOCALAPPDATA") or _u146_Path.home()) / "NaprawaPC" / "Raporty" / "QualityTests"
        root.mkdir(parents=True, exist_ok=True)
        stamp = _u146_time.strftime("%Y%m%d-%H%M%S")
        path = root / f"{stamp}-{str(module).lower()}-{str(test_id)}.json"
        payload = dict(report)
        payload.setdefault("app", "NAPRAWA PC HARDWARE TEST PRO")
        payload.setdefault("quality_patch_version", _U146_QUALITY_PATCH_VERSION)
        payload["report_path"] = str(path)
        path.write_text(_u146_json.dumps(payload, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        return str(path)
    except Exception:
        return None

def _u146_update_view(app, module, percent, message, report=None):
    def apply():
        try:
            status = getattr(app, "header_status", None)
            if status is not None and status.winfo_exists():
                state = str((report or {}).get("state", "running")).lower()
                colour = app.colors()["good"] if state == "good" else app.colors()["bad"] if state in ("bad", "error") else app.colors()["warn"]
                status.configure(text=f"{module}: {message}", fg=colour)
        except Exception: pass
        if module == "RAM":
            try:
                bar = getattr(app, "_u146_ram_progressbar", None)
                label = getattr(app, "_u146_ram_progress_label", None)
                if bar is not None and bar.winfo_exists(): bar.configure(value=max(0, min(100, int(percent))))
                if label is not None and label.winfo_exists(): label.configure(text=str(message))
            except Exception: pass
        if module == "CPU" and report is not None:
            tree = getattr(app, "_u146_cpu_tree", None)
            try:
                if tree is not None and tree.winfo_exists():
                    for iid in tree.get_children(): tree.delete(iid)
                    for stage in report.get("stages", []):
                        tree.insert("", "end", values=(f"{stage.get('target','N/D')}%",
                            "N/D" if stage.get("load") is None else f"{stage.get('load'):.1f}%",
                            "N/D" if stage.get("freq") is None else f"{stage.get('freq'):.0f} MHz",
                            f"{stage.get('seconds',0):.1f} s"))
            except Exception: pass
        try:
            render = globals().get("_u86_render_component_report")
            if report is not None and callable(render):
                render(app, module)
        except Exception: pass
    try: app.queue_action(apply)
    except Exception:
        try: apply()
        except Exception: pass
