# NAPRAWA PC HARDWARE TEST PRO — selectable real CPU/RAM/GPU benchmark profiles.
# A profile runs the existing test handlers; it does not substitute graphics or sample data for measured results.
import os as _u154_os
import sys as _u154_sys
import time as _u154_time
import json as _u154_json
import csv as _u154_csv
import html as _u154_html
import socket as _u154_socket
import platform as _u154_platform
import datetime as _u154_datetime
from pathlib import Path as _u154_Path
import tkinter as _u154_tk
from tkinter import ttk as _u154_ttk, messagebox as _u154_messagebox

_U154_HARDWARE_PROFILE_VERSION = "1.0.0"
_U154_PROFILES = {
    "SZYBKI": {
        "cpu_seconds": 15, "ram_mb": 256, "gpu_scenes": (1,), "gpu_scene_seconds": 10,
        "description": "CPU 15 s • RAM 256 MB • 1 scena OpenGL × 10 s",
    },
    "STANDARD": {
        "cpu_seconds": 60, "ram_mb": 512, "gpu_scenes": (1, 37, 73), "gpu_scene_seconds": 10,
        "description": "CPU 60 s • RAM 512 MB • 3 różne sceny OpenGL × 10 s",
    },
    "ROZSZERZONY": {
        "cpu_seconds": 180, "ram_mb": 1024, "gpu_scenes": (1, 22, 43, 64, 85, 110), "gpu_scene_seconds": 15,
        "description": "CPU 180 s • RAM do 1024 MB • 6 różnych scen OpenGL × 15 s",
    },
}
_U154_ORIGINAL_UPDATE_VIEW = _u146_update_view
_U154_ORIGINAL_QUEUE_PANEL = _u145_queue_panel
_U154_ORIGINAL_SHOW_MODULE = AppV43.show_module
_U154_ORIGINAL_SHOW_TEST_DETAIL = AppV43.show_test_detail
_U154_ORIGINAL_SHOW_TESTS_HUB = AppV43.show_tests_hub


def _u154_plan(profile):
    key = str(profile or "SZYBKI").strip().upper()
    if key not in _U154_PROFILES:
        key = "SZYBKI"
    item = dict(_U154_PROFILES[key])
    item["profile"] = key
    item["gpu_scenes"] = tuple(int(s) for s in item["gpu_scenes"])
    item["estimated_seconds"] = int(item["cpu_seconds"] + item["ram_mb"] / 256 * 4 +
                                     len(item["gpu_scenes"]) * item["gpu_scene_seconds"])
    return item


def _u154_num(value):
    try:
        number = float(value)
        return number if number == number and abs(number) != float("inf") else None
    except Exception:
        return None


def _u154_slug(value):
    import re as _u154_re
    return (_u154_re.sub(r"[^A-Za-z0-9_-]+", "-", str(value or "profile")).strip("-_") or "profile")[:64]


def _u154_csv_cell(value):
    text = "" if value is None else str(value)
    text = text.replace("\x00", " ")
    if text[:1] in ("=", "+", "-", "@", "\t", "\r"):
        text = "'" + text
    return text


def _u154_profile_root():
    root = _u154_os.environ.get("LOCALAPPDATA") or str(_u154_Path.home())
    return _u154_Path(root) / "NaprawaPC" / "Raporty" / "HardwareProfiles"


def _u154_render_html(report):
    safe_report = _u154_html.escape(_u154_json.dumps(report, ensure_ascii=False, indent=2, default=str))
    state = str(report.get("state", "warn")).upper()
    color = "#16884a" if state == "GOOD" else "#b42332" if state == "BAD" else "#9a6700"
    stages = report.get("stages") if isinstance(report.get("stages"), list) else []
    rows = []
    for item in stages:
        if not isinstance(item, dict):
            continue
        rows.append(
            "<tr><td>" + _u154_html.escape(str(item.get("module", "N/D"))) + "</td><td>" +
            _u154_html.escape(str(item.get("test", "N/D"))) + "</td><td>" +
            _u154_html.escape(str(item.get("state", "N/D")).upper()) + "</td><td>" +
            _u154_html.escape(str(item.get("duration_seconds", "N/D"))) + "</td><td>" +
            _u154_html.escape(str(item.get("summary", ""))) + "</td></tr>"
        )
    return (
        "<!doctype html><html lang='pl'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
        "<title>Raport profilu CPU RAM GPU</title><style>"
        "body{background:#091321;color:#eaf3ff;font:14px Segoe UI,Arial;margin:24px}"
        "main{max-width:1200px;margin:auto}section{background:#111f31;border:1px solid #27435f;border-radius:10px;padding:18px;margin:12px 0}"
        "h1{color:#53cfff}.state{display:inline-block;background:" + color + ";padding:7px 14px;border-radius:5px;font-weight:bold}"
        "table{width:100%;border-collapse:collapse}td,th{padding:9px;border-bottom:1px solid #27435f;text-align:left;vertical-align:top}"
        "pre{white-space:pre-wrap;overflow-wrap:anywhere;font:12px Consolas,monospace}</style></head><body><main>"
        "<section><h1>NAPRAWA PC HARDWARE TEST PRO — PROFIL CPU / RAM / GPU</h1>"
        "<p>Profil: " + _u154_html.escape(str(report.get("profile", "N/D"))) + "</p>"
        "<p>Komputer: " + _u154_html.escape(str((report.get("hardware") or {}).get("computer_name", "N/D"))) + "</p>"
        "<p class='state'>" + _u154_html.escape(state) + "</p>"
        "<p>To raport rzeczywistych uruchomień. RAM oznacza sprawdzony bufor procesu, a FPS pochodzi z raportów renderera OpenGL. N/D nie oznacza PASS.</p></section>"
        "<section><h2>Podsumowanie etapów</h2><table><thead><tr><th>Moduł</th><th>Test</th><th>Stan</th><th>Czas (s)</th><th>Wynik</th></tr></thead><tbody>"
        + "".join(rows) + "</tbody></table></section>"
        "<section><h2>Pełne dane diagnostyczne</h2><pre>" + safe_report + "</pre></section>"
        "</main></body></html>"
    )


def _u154_save_report(report):
    root = _u154_profile_root()
    root.mkdir(parents=True, exist_ok=True)
    now = _u154_datetime.datetime.now().astimezone()
    stamp = now.strftime("%Y%m%d-%H%M%S-%f")
    stem = stamp + "-hardware-profile-" + _u154_slug(report.get("profile"))
    json_path = root / (stem + ".json")
    html_path = root / (stem + ".html")
    csv_path = root / (stem + ".csv")
    data = dict(report)
    data.update({
        "app": "NAPRAWA PC HARDWARE TEST PRO",
        "created_at": data.get("created_at") or now.isoformat(timespec="seconds"),
        "finished_at": data.get("finished_at") or now.isoformat(timespec="seconds"),
        "report_path": str(json_path.resolve()),
        "html_report_path": str(html_path.resolve()),
        "csv_report_path": str(csv_path.resolve()),
    })
    temp_json = json_path.with_suffix(".json.tmp")
    temp_html = html_path.with_suffix(".html.tmp")
    temp_csv = csv_path.with_suffix(".csv.tmp")
    temp_json.write_text(_u154_json.dumps(data, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    temp_html.write_text(_u154_render_html(data), encoding="utf-8")
    with temp_csv.open("w", newline="", encoding="utf-8-sig") as stream:
        writer = _u154_csv.writer(stream)
        writer.writerow(["Profil", "Moduł", "Test", "Stan", "Czas (s)", "Podsumowanie", "Raport źródłowy"])
        for item in data.get("stages", []):
            if not isinstance(item, dict):
                continue
            row = [data.get("profile"), item.get("module"), item.get("test"), item.get("state"),
                   item.get("duration_seconds"), item.get("summary"), item.get("report_path")]
            writer.writerow([_u154_csv_cell(value) for value in row])
    _u154_os.replace(str(temp_json), str(json_path))
    _u154_os.replace(str(temp_html), str(html_path))
    _u154_os.replace(str(temp_csv), str(csv_path))
    return data


def _u154_stage_state(result):
    if not isinstance(result, dict):
        return "warn"
    state = str(result.get("state", "warn") or "warn").strip().lower()
    if state in ("good", "pass", "ok", "completed", "success"):
        return "good"
    if state in ("bad", "fail", "failed", "error"):
        return "bad"
    return "warn"


def _u154_stage_summary(module, result):
    if not isinstance(result, dict):
        return "Brak raportu zwrotnego; wynik niezaliczony."
    if module == "CPU":
        return (
            "SHA-256/s=" + str(result.get("operations_per_second", "N/D")) +
            "; średnie CPU=" + str(result.get("cpu_load_avg_percent", "N/D")) + "%" +
            "; czas=" + str(result.get("duration_seconds", "N/D")) + " s"
        )
    if module == "RAM":
        return (
            "bufor rzeczywisty=" + str(result.get("size_mb", result.get("tested_mb", "N/D"))) + " MB" +
            "; wzorce=" + str(result.get("patterns_completed", "N/D")) + "/" +
            str(result.get("patterns_total", "N/D")) +
            "; zweryfikowane bajty=" + str(result.get("bytes_verified", "N/D"))
        )
    return (
        "średni FPS=" + str(result.get("average_fps", "N/D")) +
        "; peak FPS=" + str(result.get("peak_fps_1s", result.get("peak_fps", "N/D"))) +
        "; klatki=" + str(result.get("frames", "N/D")) +
        "; renderer=" + str(result.get("renderer", result.get("error", "N/D")))
    )


def _u154_profile_status(app, text, percent=None):
    state = getattr(app, "_u154_profile_state", None)
    if isinstance(state, dict):
        state["last_status"] = str(text)
        if percent is not None:
            state["progress"] = max(0, min(100, float(percent)))
    def apply():
        panel = getattr(app, "_u154_profile_panel", None)
        if not isinstance(panel, dict):
            return
        try:
            if not panel["frame"].winfo_exists():
                return
            panel["status"].configure(text=str(text)[:1200])
            if percent is not None:
                panel["progress"].configure(value=max(0, min(100, float(percent))))
        except Exception:
            pass
    try:
        queue = getattr(app, "queue_action", None)
        if callable(queue):
            queue(apply)
    except Exception:
        pass


def _u154_profile_active(app):
    state = getattr(app, "_u154_profile_state", None)
    return state if isinstance(state, dict) and bool(state.get("active")) else None


def _u154_update_view(app, module, percent, message, report=None):
    result = _U154_ORIGINAL_UPDATE_VIEW(app, module, percent, message, report)
    state = _u154_profile_active(app)
    key = str(module or "").upper()
    if state is not None and key in ("CPU", "RAM"):
        if key == "CPU":
            overall = max(0.0, min(45.0, 45.0 * float(percent or 0) / 100.0))
        else:
            overall = 45.0 + max(0.0, min(30.0, 30.0 * float(percent or 0) / 100.0))
        _u154_profile_status(app, str(state.get("phase_label") or key) + " • " + str(message or ""), overall)
    return result


def _u154_queue_panel(app, test_id, progress=None, headline=None, metrics=None, sample=None):
    result = _U154_ORIGINAL_QUEUE_PANEL(app, test_id, progress, headline, metrics, sample)
    state = _u154_profile_active(app)
    if state is not None and str(state.get("phase") or "").upper() == "GPU":
        scenes = state.get("gpu_scenes") or ()
        index = max(1, int(state.get("gpu_scene_index", 1) or 1))
        local = max(0.0, min(100.0, float(progress if progress is not None else 0)))
        overall = 75.0 + 24.0 * ((index - 1) + local / 100.0) / max(1, len(scenes))
        _u154_profile_status(app, str(headline or state.get("phase_label") or "GPU OpenGL"), overall)
    return result


def _u154_stop_requested(app):
    if bool(getattr(app, "stop_requested", False)):
        return True
    try:
        check = getattr(app, "_test_should_stop", None)
        return bool(check()) if callable(check) else False
    except Exception:
        return False


def _u154_run_profile(app, profile):
    plan = _u154_plan(profile)
    now = _u154_datetime.datetime.now().astimezone()
    state = getattr(app, "_u154_profile_state", None)
    if not isinstance(state, dict):
        state = {}
        app._u154_profile_state = state
    state.update({
        "active": True, "phase": "CPU", "phase_label": "ETAP 1/3 • CPU",
        "gpu_scenes": plan["gpu_scenes"], "gpu_scene_index": 1,
        "progress": 0.0, "last_status": "Start profilu",
    })
    stages = []
    stopped = False
    def run_cpu():
        nonlocal stopped
        _u154_profile_status(app, "ETAP 1/3 • CPU • SHA-256 przez " + str(plan["cpu_seconds"]) + " s", 0)
        started = _u154_time.perf_counter()
        result = None
        error = None
        try:
            result = app._cpu_test(plan["cpu_seconds"])
        except Exception as exc:
            error = type(exc).__name__ + ": " + str(exc)
            try: app.queue_log("PROFIL CPU: " + error)
            except Exception: pass
        result = result if isinstance(result, dict) else {}
        elapsed = max(0.001, _u154_time.perf_counter() - started)
        if error and not result:
            result = {"state": "error", "error": error, "message": error, "duration_seconds": round(elapsed, 2)}
        result.setdefault("duration_seconds", round(elapsed, 2))
        _u154_stage_record(stages, "CPU", "Benchmark SHA-256", result, elapsed, {"seconds": plan["cpu_seconds"]})
        stopped = stopped or _u154_stop_requested(app)
        _u154_profile_status(app, "ETAP 1/3 • CPU • " + _u154_stage_summary("CPU", result), 45 if _u154_stage_state(result) == "good" else 0)
        return result

    def run_ram():
        nonlocal stopped
        if stopped or _u154_stop_requested(app):
            stopped = True
            return None
        state["phase"] = "RAM"
        state["phase_label"] = "ETAP 2/3 • RAM"
        _u154_profile_status(app, "ETAP 2/3 • RAM • zapis i weryfikacja wzorców • do " + str(plan["ram_mb"]) + " MB", 45)
        started = _u154_time.perf_counter()
        result = None
        error = None
        try:
            result = app._ram_test(plan["ram_mb"])
        except Exception as exc:
            error = type(exc).__name__ + ": " + str(exc)
            try: app.queue_log("PROFIL RAM: " + error)
            except Exception: pass
        result = result if isinstance(result, dict) else {}
        elapsed = max(0.001, _u154_time.perf_counter() - started)
        if error and not result:
            result = {"state": "error", "error": error, "message": error, "duration_seconds": round(elapsed, 2)}
        result.setdefault("duration_seconds", round(elapsed, 2))
        _u154_stage_record(stages, "RAM", "Wzorce zapisu / odczytu / weryfikacji", result, elapsed, {"requested_mb": plan["ram_mb"]})
        stopped = stopped or _u154_stop_requested(app)
        _u154_profile_status(app, "ETAP 2/3 • RAM • " + _u154_stage_summary("RAM", result), 75 if _u154_stage_state(result) == "good" else 45)
        return result

    def run_gpu():
        nonlocal stopped
        if stopped or _u154_stop_requested(app):
            stopped = True
            return []
        state["phase"] = "GPU"
        state["phase_label"] = "ETAP 3/3 • GPU OpenGL"
        scene_rows = []
        total = len(plan["gpu_scenes"])
        for index, scene_id in enumerate(plan["gpu_scenes"], 1):
            if _u154_stop_requested(app):
                stopped = True
                break
            state["gpu_scene_index"] = index
            _u154_profile_status(app, f"ETAP 3/3 • GPU • scena {index}/{total} (ID {scene_id}) • OpenGL {plan['gpu_scene_seconds']} s",
                                 75 + 24.0 * (index - 1) / max(1, total))
            started = _u154_time.perf_counter()
            result = None
            error = None
            try:
                result = _u66_execute_gpu_scene(app, scene_id, plan["gpu_scene_seconds"])
            except Exception as exc:
                error = type(exc).__name__ + ": " + str(exc)
                try: app.queue_log("PROFIL GPU scena " + str(scene_id) + ": " + error)
                except Exception: pass
            result = result if isinstance(result, dict) else {}
            elapsed = max(0.001, _u154_time.perf_counter() - started)
            if error and not result:
                result = {"state": "error", "scene_id": scene_id, "error": error, "duration_seconds": round(elapsed, 2)}
            result.setdefault("duration_seconds", round(elapsed, 2))
            result.setdefault("scene_id", scene_id)
            result.setdefault("scene_name", str(scene_id))
            result_path = None
            try:
                saver = globals().get("_u149_write_report")
                if callable(saver):
                    result_path = saver("GPU", "PROFILE_" + plan["profile"] + "_SCENE_" + str(scene_id), result,
                                        settings={"profile": plan["profile"], "scene_seconds": plan["gpu_scene_seconds"]})
            except Exception:
                result_path = None
            _u154_stage_record(stages, "GPU", "OpenGL scena " + str(scene_id), result, elapsed,
                               {"scene_id": scene_id, "seconds": plan["gpu_scene_seconds"]}, result_path)
            scene_rows.append(result)
        average = [_u154_num(row.get("average_fps", row.get("mean_fps"))) for row in scene_rows]
        average = [v for v in average if v is not None]
        peak = [_u154_num(row.get("peak_fps_1s", row.get("peak_fps"))) for row in scene_rows]
        peak = [v for v in peak if v is not None]
        states = [_u154_stage_state(row) for row in scene_rows]
        gpu_state = "good" if scene_rows and len(scene_rows) == total and all(s == "good" for s in states) and not stopped else (
            "bad" if any(s == "bad" for s in states) else "warn"
        )
        aggregate = {
            "state": gpu_state, "test": "GPU multi-scene OpenGL profile",
            "scenes_requested": list(plan["gpu_scenes"]), "scenes_completed": len(scene_rows),
            "scene_seconds": plan["gpu_scene_seconds"],
            "average_fps_mean": round(sum(average) / len(average), 2) if average else None,
            "average_fps_min": min(average) if average else None,
            "average_fps_max": max(average) if average else None,
            "peak_fps_max": max(peak) if peak else None,
            "stopped": stopped,
            "message": "FPS z raportów OpenGL; jeśli scena nie wystartuje, wynik pozostaje WARN/ERROR bez przykładowej wartości.",
        }
        _u154_stage_record(stages, "GPU", "Podsumowanie scen OpenGL", aggregate,
                           sum(float(row.get("duration_seconds", 0) or 0) for row in scene_rows),
                           {"scenes_requested": list(plan["gpu_scenes"])})
        _u154_profile_status(app, "ETAP 3/3 • GPU • " + _u154_stage_summary("GPU", aggregate),
                             99 if gpu_state == "good" else 75)
        return scene_rows, aggregate

    report = {
        "app": "NAPRAWA PC HARDWARE TEST PRO", "module": "CPU+RAM+GPU",
        "profile": plan["profile"], "profile_description": plan["description"],
        "started_at": now.isoformat(timespec="seconds"), "state": "warn",
        "estimated_seconds": plan["estimated_seconds"], "stages": stages, "hardware": _u154_hardware_info(),
    }
    try:
        run_cpu()
        run_ram()
        gpu_scenes = []
        gpu_aggregate = {}
        if not stopped:
            gpu_scenes, gpu_aggregate = run_gpu()
        state["phase"] = "SAVE"
        state["phase_label"] = "ZAPIS RAPORTU"
        states = [_u154_stage_state(item) for item in stages if isinstance(item, dict)]
        if any(s == "bad" for s in states):
            report_state = "bad"
        elif stopped or not stages or any(s != "good" for s in states):
            report_state = "warn"
        else:
            report_state = "good"
        report.update({
            "state": report_state, "stopped": bool(stopped or _u154_stop_requested(app)),
            "finished_at": _u154_datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
            "stages": stages, "gpu_scenes": gpu_scenes if "gpu_scenes" in locals() else [],
            "gpu_aggregate": gpu_aggregate if "gpu_aggregate" in locals() else {},
        })
        try:
            data = _u154_save_report(report)
            report = data
        except Exception as exc:
            report["report_save_error"] = type(exc).__name__ + ": " + str(exc)
        try:
            if not isinstance(getattr(app, "results", None), dict):
                app.results = {}
            app.results["HARDWARE_PROFILE_LATEST"] = dict(report)
        except Exception:
            pass
        try: app.queue_results("HARDWARE_PROFILE_LATEST", report)
        except Exception: pass
        try: app.queue_log("PROFIL CPU/RAM/GPU " + plan["profile"] + ": " + report["state"].upper() +
                           " • etapy=" + str(len(stages)) + " • raport=" + str(report.get("html_report_path") or report.get("report_path") or "N/D"))
        except Exception: pass
        _u154_profile_status(app, "PROFIL ZAKOŃCZONY • " + plan["profile"] + " • " + report["state"].upper() +
                             " • " + str(report.get("html_report_path") or report.get("report_path") or "brak pliku raportu"),
                             100 if report_state == "good" else 0)
        return report
    except Exception as exc:
        report["state"] = "error"
        report["error"] = type(exc).__name__ + ": " + str(exc)
        report["stages"] = stages
        report["finished_at"] = _u154_datetime.datetime.now().astimezone().isoformat(timespec="seconds")
        try:
            report = _u154_save_report(report)
        except Exception:
            pass
        _u154_profile_status(app, "BŁĄD PROFILU • " + type(exc).__name__ + ": " + str(exc), 0)
        try: app.queue_log("PROFIL CPU/RAM/GPU: " + type(exc).__name__ + ": " + str(exc))
        except Exception: pass
        return report
    finally:
        state["active"] = False
        state["finished_at"] = _u154_time.monotonic()


def _u154_stage_record(stages, module, test, result, elapsed, settings=None, report_path=None):
    data = dict(result) if isinstance(result, dict) else {"state": "warn", "message": str(result)}
    state = _u154_stage_state(data)
    data.update({
        "module": module, "test": test, "state": state,
        "duration_seconds": round(float(elapsed or 0), 2),
        "summary": _u154_stage_summary(module, data),
        "settings": dict(settings or {}),
    })
    if report_path:
        data["report_path"] = str(report_path)
    else:
        try:
            saver = globals().get("_u149_write_report")
            if callable(saver):
                data["report_path"] = str(saver(module, "PROFILE_" + str(test).replace(" ", "_"), data, settings=settings) or "")
        except Exception:
            pass
    stages.append(data)
    return data


def _u154_hardware_info():
    data = {
        "computer_name": _u154_socket.gethostname(),
        "platform": _u154_platform.platform(),
        "app_version": str(globals().get("APP_VERSION", "N/D")),
    }
    p = globals().get("psutil")
    if p is not None:
        try:
            vm = p.virtual_memory()
            data["ram_total_mb"] = round(vm.total / 1048576, 1)
        except Exception:
            data["ram_total_mb"] = None
        try:
            data["cpu_logical_processors"] = p.cpu_count(logical=True)
            data["cpu_physical_cores"] = p.cpu_count(logical=False)
        except Exception:
            pass
    return data


def _u154_start_profile(app, profile):
    plan = _u154_plan(profile)
    if bool(getattr(app, "running", False)):
        _u154_messagebox.showwarning(
            "Profil CPU/RAM/GPU", "Inny test jest w toku. Poczekaj na raport albo użyj STOP TEST.", parent=app
        )
        return False
    try:
        app.stop_requested = False
    except Exception:
        pass
    state = {
        "active": True, "profile": plan["profile"], "phase": "CPU",
        "phase_label": "ETAP 1/3 • CPU", "gpu_scenes": plan["gpu_scenes"],
        "gpu_scene_index": 1, "progress": 0.0, "last_status": "Uruchamianie profilu",
        "started_at": _u154_time.monotonic(),
    }
    app._u154_profile_state = state
    _u154_profile_status(app, "PRZYGOTOWANIE PROFILU " + plan["profile"] + " • " + plan["description"], 0)
    try:
        worker = getattr(app, "worker", None)
        if not callable(worker):
            raise RuntimeError("Aplikacja nie udostępnia mechanizmu worker.")
        worker(lambda: _u154_run_profile(app, plan["profile"]))
        return True
    except Exception as exc:
        state["active"] = False
        _u154_profile_status(app, "BŁĄD STARTU PROFILU • " + type(exc).__name__ + ": " + str(exc), 0)
        _u154_messagebox.showerror("Profil CPU/RAM/GPU", str(exc), parent=app)
        return False


def _u154_open_last_report(app):
    state = getattr(app, "_u154_last_profile_report", None)
    root = _u154_profile_root()
    if not root.exists():
        _u154_messagebox.showinfo("Raporty profili", "Nie ma jeszcze raportów profili CPU/RAM/GPU.", parent=app)
        return False
    if not isinstance(state, dict):
        try:
            candidates = sorted(root.glob("*-hardware-profile-*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
            state = _u154_json.loads(candidates[0].read_text(encoding="utf-8-sig")) if candidates else None
        except Exception:
            state = None
    path = _u154_Path(str(state.get("html_report_path") or state.get("report_path") or "")) if isinstance(state, dict) else None
    if path is None or not path.is_file():
        _u154_messagebox.showinfo("Raporty profili", "Nie znaleziono gotowego raportu HTML. Otwórz folder raportów.", parent=app)
        return False
    try:
        import webbrowser as _u154_webbrowser
        _u154_webbrowser.open(path.resolve().as_uri())
        return True
    except Exception as exc:
        _u154_messagebox.showerror("Raporty profili", str(exc), parent=app)
        return False


def _u154_open_report_folder(app):
    root = _u154_profile_root()
    try:
        root.mkdir(parents=True, exist_ok=True)
        if _u154_os.name == "nt":
            _u154_os.startfile(str(root))
        else:
            import webbrowser as _u154_webbrowser
            _u154_webbrowser.open(root.resolve().as_uri())
        return True
    except Exception as exc:
        _u154_messagebox.showerror("Raporty profili", str(exc), parent=app)
        return False


def _u154_attach_profile_controls(app, location="TESTY"):
    key = str(location or "TESTY")
    existing = getattr(app, "_u154_profile_panel", None)
    try:
        if isinstance(existing, dict) and existing.get("location") == key and existing["frame"].winfo_exists():
            return True
    except Exception:
        pass
    content = getattr(app, "content", None)
    if content is None:
        return False
    theme = app.colors()
    panel = _u154_tk.Frame(content, bg=theme["panel"], highlightbackground=theme["accent"], highlightthickness=1)
    children = list(content.winfo_children())
    if children:
        panel.pack(fill="x", padx=7, pady=(3, 6), before=children[0])
    else:
        panel.pack(fill="x", padx=7, pady=(3, 6))
    _u154_tk.Label(
        panel, text="PROFIL RZECZYWISTEGO BENCHMARKU • CPU + RAM + GPU",
        bg=theme["panel"], fg=theme["accent"], font=app.fnt(10, "bold"), anchor="w"
    ).pack(fill="x", padx=10, pady=(7, 2))
    _u154_tk.Label(
        panel,
        text="Jeden przebieg uruchamia rzeczywiste testy CPU SHA-256, zapis/weryfikację bufora RAM oraz kilka scen OpenGL. Raport zbiorczy zapisuje się jako JSON + HTML + CSV. Nie jest to test każdej fizycznej komórki RAM ani gwarancja FPS w grach.",
        bg=theme["panel"], fg=theme["muted"], font=app.fnt(8), wraplength=1500, justify="left", anchor="w"
    ).pack(fill="x", padx=10, pady=(0, 5))
    controls = _u154_tk.Frame(panel, bg=theme["panel"])
    controls.pack(fill="x", padx=8, pady=(0, 4))
    profile_var = _u154_tk.StringVar(master=app, value="SZYBKI")
    combo = _u154_ttk.Combobox(controls, textvariable=profile_var, values=("SZYBKI", "STANDARD", "ROZSZERZONY"), state="readonly", width=16)
    combo.pack(side="left", padx=(0, 6), pady=3)
    status = _u154_tk.Label(panel, text="Gotowy • wybierz profil i uruchom CPU + RAM + GPU.", bg=theme["panel"], fg=theme["muted"], font=app.fnt(8, "bold"), anchor="w")
    status.pack(fill="x", padx=10, pady=(0, 3))
    progress = _u154_ttk.Progressbar(panel, mode="determinate", maximum=100, value=0)
    progress.pack(fill="x", padx=10, pady=(0, 5))
    buttons = _u154_tk.Frame(panel, bg=theme["panel"])
    buttons.pack(fill="x", padx=8, pady=(0, 7))
    app.make_button(buttons, "▶ URUCHOM PROFIL CPU + RAM + GPU", lambda: _u154_start_profile(app, profile_var.get()), "accent", side="left", ipady=4)
    app.make_button(buttons, "■ STOP", lambda: _u154_stop_profile(app), "bad", side="left", ipady=4)
    app.make_button(buttons, "OSTATNI RAPORT HTML", lambda: _u154_open_last_report(app), "card", side="left", ipady=4)
    app.make_button(buttons, "FOLDER / JSON / HTML / CSV", lambda: _u154_open_report_folder(app), "card", side="left", ipady=4)

    app._u154_profile_panel = {
        "frame": panel, "location": key, "profile_var": profile_var,
        "status": status, "progress": progress, "combo": combo,
    }
    state = getattr(app, "_u154_profile_state", None)
    if isinstance(state, dict) and state.get("last_status"):
        _u154_profile_status(app, state["last_status"], state.get("progress"))
    return True


def _u154_stop_profile(app):
    if not _u154_profile_active(app):
        _u154_messagebox.showinfo("STOP PROFILU", "Nie ma aktywnego profilu do zatrzymania.", parent=app)
        return False
    try:
        app.stop_requested = True
        stop = getattr(app, "stop_current_test", None)
        if callable(stop):
            stop()
        _u154_profile_status(app, "STOP ZAŻĄDANY • czekam na bezpieczne zamknięcie bieżącego testu i zapis raportu.",
                             getattr(app, "_u154_profile_state", {}).get("progress", 0))
        return True
    except Exception as exc:
        _u154_messagebox.showerror("STOP PROFILU", str(exc), parent=app)
        return False


def _u154_wrap_show_module(app, module):
    result = _U154_ORIGINAL_SHOW_MODULE(app, module)
    key = str(module or "").upper()
    if "CPU" in key or "PROCESOR" in key or "RAM" in key or "PAMI" in key or "GPU" in key or "GRAFICZ" in key:
        _u154_attach_profile_controls(app, "MODUŁ " + key)
    return result


def _u154_wrap_show_test_detail(app, module, test_id):
    result = _U154_ORIGINAL_SHOW_TEST_DETAIL(app, module, test_id)
    key = str(module or "").upper()
    if "CPU" in key or "PROCESOR" in key or "RAM" in key or "PAMI" in key or "GPU" in key or "GRAFICZ" in key:
        _u154_attach_profile_controls(app, "KATALOG " + key + " " + str(test_id))
    return result


def _u154_wrap_show_tests_hub(app):
    result = _U154_ORIGINAL_SHOW_TESTS_HUB(app)
    _u154_attach_profile_controls(app, "CENTRUM TESTÓW")
    return result


def _u154_selftest_profile_suite():
    quick = _u154_plan("SZYBKI")
    standard = _u154_plan("STANDARD")
    extended = _u154_plan("ROZSZERZONY")
    assert quick["cpu_seconds"] == 15 and quick["ram_mb"] == 256 and quick["gpu_scenes"] == (1,)
    assert standard["cpu_seconds"] == 60 and standard["ram_mb"] == 512 and len(standard["gpu_scenes"]) == 3
    assert extended["cpu_seconds"] == 180 and extended["ram_mb"] == 1024 and len(extended["gpu_scenes"]) == 6
    assert len(set(extended["gpu_scenes"])) == len(extended["gpu_scenes"])
    assert all(1 <= scene <= 110 for scene in quick["gpu_scenes"] + standard["gpu_scenes"] + extended["gpu_scenes"])
    assert standard["estimated_seconds"] > quick["estimated_seconds"]
    assert extended["estimated_seconds"] > standard["estimated_seconds"]
    assert _u154_stage_state({"state": "good"}) == "good"
    assert _u154_stage_state({"state": "bad"}) == "bad"
    assert _u154_stage_state({"state": "warn"}) == "warn"
    assert _u154_csv_cell("=cmd|' /C calc'!A0").startswith("'=")
    html_text = _u154_render_html({
        "profile": "SZYBKI", "state": "warn", "hardware": {"computer_name": "<script>"},
        "stages": [{"module": "GPU", "test": "<script>", "state": "warn", "summary": "<script>alert(1)</script>"}],
    })
    assert "<script>alert(1)</script>" not in html_text and "&lt;script&gt;" in html_text
    assert callable(_u154_run_profile) and callable(_u154_save_report) and callable(_u154_start_profile)
    assert callable(_u154_attach_profile_controls) and callable(_u154_stop_profile)
    print("HARDWARE_PROFILE_SUITE_SELFTEST_OK: quick/standard/extended CPU+RAM+GPU profiles, real handlers, safe CSV, escaped HTML and combined report")


_U146_ORIGINAL_PROFILE_UPDATE_VIEW = _u146_update_view
_u146_update_view = _u154_update_view
_u145_queue_panel = _u154_queue_panel
AppV43.show_module = _u154_wrap_show_module
AppV43.show_test_detail = _u154_wrap_show_test_detail
AppV43.show_tests_hub = _u154_wrap_show_tests_hub


if __name__ == "__main__" and "--selftest-hardware-profile-suite" in _u154_sys.argv:
    try:
        _u154_selftest_profile_suite()
        raise SystemExit(0)
    except Exception as _u154_exc:
        import traceback as _u154_traceback
        print("HARDWARE_PROFILE_SUITE_SELFTEST_FAILED:", type(_u154_exc).__name__, str(_u154_exc))
        raise SystemExit(1)
