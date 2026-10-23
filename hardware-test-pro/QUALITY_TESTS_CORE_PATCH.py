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
_U146_RAM_PATTERN_MODES = tuple(_U40_RAM_PATTERN_LIST)
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

def _u146_expected_pattern_chunk(mode, value, start, length, chunk_index, pattern_index):
    if mode == "constant":
        return bytes((int(value) & 0xFF,)) * length
    if mode == "alternate":
        first = int(value) & 0xFF
        pair = bytes((first, (first ^ 0xFF) & 0xFF))
        if start & 1:
            pair = pair[::-1]
        return pair * (length // 2) + (pair[:length % 2] if length % 2 else b"")
    if mode == "address":
        from array import array
        words = array("I")
        if words.itemsize != 4 or start % 4 or length % 4:
            raise RuntimeError("Nieprawidłowa szerokość dla wzorca adresowego RAM.")
        return array("I", range(start // 4, (start + length) // 4)).tobytes()
    if mode == "random":
        seed = (0x4E415052 ^ ((chunk_index + 1) * 0x9E3779B1) ^ (pattern_index * 0x85EBCA6B)) & 0xFFFFFFFF
        return _u40_random.Random(seed).randbytes(length)
    raise ValueError("Nieznany tryb wzorca RAM: " + str(mode))


def _u146_verify_ram_buffer(buffer, seconds=0, progress_callback=None, stop_check=None, stats_out=None):
    started = _u146_time.monotonic()
    view = memoryview(buffer)
    size = len(view)
    if size <= 0:
        raise ValueError("Bufor RAM ma zerowy rozmiar.")
    try:
        _u146_ctypes.addressof(_u146_ctypes.c_ubyte.from_buffer(buffer))
    except Exception as exc:
        raise TypeError(f"Bufor RAM nie udostępnia zapisywalnej pamięci: {exc}") from exc
    patterns = tuple(_U146_RAM_PATTERN_MODES)
    pattern_count = len(patterns)
    chunk_size = 4 * 1024 * 1024
    chunk_count = (size + chunk_size - 1) // chunk_size
    operations_per_pass = max(1, pattern_count * chunk_count * 2)
    duration = max(0.0, min(900.0, float(seconds or 0)))
    stats = {
        "size_mb": round(size / 1048576, 2),
        "patterns_total": pattern_count,
        "patterns_completed": 0,
        "pattern_names": [str(item[0]) for item in patterns],
        "passes": 0,
        "bytes_written": 0,
        "bytes_verified": 0,
        "elapsed_sec": 0.0,
        "stopped": False,
        "allocation_failed": False,
        "error_offset": None,
        "failed_pattern": None
    }
    last_reported_percent = -1
    def emit_progress(percent, message, force=False):
        nonlocal last_reported_percent
        normalized = max(0, min(100, int(percent)))
        if force or normalized != last_reported_percent:
            _u146_progress(progress_callback, normalized, message)
            last_reported_percent = normalized
    try:
        pass_number = 0
        while True:
            pass_number += 1
            completed_operations = 0
            stats["patterns_completed"] = 0
            emit_progress(0, f"Przebieg {pass_number}: przygotowanie pełnego testu RAM.", force=True)
            for pattern_index, (name, mode, value) in enumerate(patterns, start=1):
                if _u146_stopped(stop_check):
                    stats["stopped"] = True
                    stats["elapsed_sec"] = round(_u146_time.monotonic() - started, 3)
                    if stats_out is not None: stats_out.update(stats)
                    return False, f"Test RAM zatrzymany przez użytkownika przed wzorcem {name}."
                expected_digest = _u146_hashlib.sha256()
                write_label = f"{name}: zapis pełnego bufora {size / 1048576:.0f} MB."
                emit_progress(int((pattern_index - 1) * 50 / pattern_count), f"Przebieg {pass_number} • {write_label}")
                for chunk_index in range(chunk_count):
                    if _u146_stopped(stop_check):
                        stats["stopped"] = True
                        stats["patterns_completed"] = pattern_index - 1
                        stats["elapsed_sec"] = round(_u146_time.monotonic() - started, 3)
                        if stats_out is not None: stats_out.update(stats)
                        return False, f"Test RAM zatrzymany podczas zapisu wzorca {name}."
                    offset = chunk_index * chunk_size
                    end = min(size, offset + chunk_size)
                    expected = _u146_expected_pattern_chunk(mode, value, offset, end - offset, chunk_index, pattern_index)
                    view[offset:end] = expected
                    expected_digest.update(expected)
                    stats["bytes_written"] += len(expected)
                    completed_operations += 1
                    percent = int(completed_operations * 100 / operations_per_pass)
                    emit_progress(percent, f"Przebieg {pass_number} • {name}: zapis bloku {chunk_index + 1}/{chunk_count}.")
                actual_digest = _u146_hashlib.sha256()
                for chunk_index in range(chunk_count):
                    if _u146_stopped(stop_check):
                        stats["stopped"] = True
                        stats["patterns_completed"] = pattern_index - 1
                        stats["elapsed_sec"] = round(_u146_time.monotonic() - started, 3)
                        if stats_out is not None: stats_out.update(stats)
                        return False, f"Test RAM zatrzymany podczas weryfikacji wzorca {name}."
                    offset = chunk_index * chunk_size
                    end = min(size, offset + chunk_size)
                    actual_chunk = view[offset:end]
                    actual_digest.update(actual_chunk)
                    stats["bytes_verified"] += len(actual_chunk)
                    completed_operations += 1
                    percent = int(completed_operations * 100 / operations_per_pass)
                    emit_progress(percent, f"Przebieg {pass_number} • {name}: weryfikacja bloku {chunk_index + 1}/{chunk_count}.")
                if actual_digest.digest() != expected_digest.digest():
                    first_bad = None
                    for chunk_index in range(chunk_count):
                        offset = chunk_index * chunk_size
                        end = min(size, offset + chunk_size)
                        expected = _u146_expected_pattern_chunk(mode, value, offset, end - offset, chunk_index, pattern_index)
                        actual = view[offset:end]
                        mismatch = next((idx for idx, (a, b) in enumerate(zip(actual, expected)) if a != b), None)
                        if mismatch is not None:
                            first_bad = offset + mismatch
                            break
                    stats["error_offset"] = first_bad
                    stats["failed_pattern"] = str(name)
                    stats["patterns_completed"] = pattern_index - 1
                    stats["passes"] = pass_number - 1
                    stats["elapsed_sec"] = round(_u146_time.monotonic() - started, 3)
                    if stats_out is not None: stats_out.update(stats)
                    return False, f"Niezgodność wzorca RAM {name}; pierwszy błędny bajt: {first_bad if first_bad is not None else 'N/D'}."
                stats["patterns_completed"] = pattern_index
            stats["passes"] = pass_number
            stats["elapsed_sec"] = round(_u146_time.monotonic() - started, 3)
            if duration <= 0 or _u146_stopped(stop_check) or stats["elapsed_sec"] >= duration:
                break
        stats["stopped"] = bool(_u146_stopped(stop_check))
        stats["elapsed_sec"] = round(_u146_time.monotonic() - started, 3)
        if stats_out is not None: stats_out.update(stats)
        if stats["stopped"]:
            return False, f"Test RAM zatrzymany po {stats['patterns_completed']}/{pattern_count} wzorcach."
        emit_progress(100,
            f"ZAKOŃCZONO • {pattern_count} pełnych wzorców • {stats['passes']} przebieg(ów) • {stats['elapsed_sec']:.1f} s.")
        return True, (
            f"OK — zapis i odczyt całego bufora dla {pattern_count} wzorców RAM (stałe, naprzemienne, adresowe, bity i pseudolosowe); "
            f"{stats['size_mb']:.0f} MB • {stats['passes']} przebieg(ów) • {stats['elapsed_sec']:.1f} s."
        )
    finally:
        try: view.release()
        except Exception: pass


def ram_pattern_test(mb, seconds=0, progress_callback=None, stop_check=None, stats_out=None):
    try:
        requested = max(64, min(2048, int(mb or 512)))
        vm = psutil.virtual_memory() if globals().get("psutil") is not None else None
        available_mb = int(vm.available / 1048576) if vm is not None else 512
        pattern_count = len(_U146_RAM_PATTERN_MODES)
        if vm is not None and available_mb < 192:
            if stats_out is not None:
                stats_out.update({"size_mb": 0, "patterns_total": pattern_count, "patterns_completed": 0,
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
            stats_out.update({"allocation_failed": True, "patterns_total": len(_U146_RAM_PATTERN_MODES),
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
        if module == "CPU":
            try:
                # The CPU module creates these controls, but previously only RAM's
                # branch updated a progressbar. Update the visible CPU bar/label for
                # every worker sample, not just after the final report arrives.
                bar = getattr(app, "_u146_cpu_progressbar", None)
                label = getattr(app, "_u146_cpu_progress_label", None)
                value = max(0, min(100, int(percent)))
                if bar is not None and bar.winfo_exists():
                    bar.configure(value=value)
                if label is not None and label.winfo_exists():
                    label.configure(text=str(message))
            except Exception:
                pass
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
