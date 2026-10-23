# v4.3.150: explicit result console for the real CPU/RAM/GPU pages.
import os as _u151_os
import sys as _u151_sys
import time as _u151_time
import tkinter as _u151_tk
from tkinter import messagebox as _u151_messagebox

_U151_HARDWARE_RESULT_CONSOLE_VERSION = "1.3.0"
_U151_ORIGINAL_SHOW_MODULE = AppV43.show_module


def _u151_module_key(value):
    text = str(value or "").strip().upper()
    text = text.replace("Ę", "E").replace("Ć", "C").replace("Ł", "L")
    if "GPU" in text or "VRAM" in text or "GRAFICZN" in text:
        return "GPU"
    if "RAM" in text or "PAMI" in text or "MEMORY" in text:
        return "RAM"
    if "CPU" in text or "PROCESOR" in text:
        return "CPU"
    return ""


def _u151_number(value):
    try:
        number = float(value)
        return number if _u145_math.isfinite(number) else None
    except Exception:
        return None


def _u151_last_result(app, module):
    results = getattr(app, "results", {}) or {}
    if not isinstance(results, dict):
        results = {}
    keys = {
        "CPU": ("CPU_BENCHMARK", "CPU_HASH_BENCHMARK", "CPU_LOAD_BENCHMARK"),
        "RAM": ("RAM_BENCHMARK",),
        "GPU": ("GPU_3D", "3D_SUITE"),
    }.get(module, ())
    if module == "GPU":
        dynamic = []
        for result_key, payload in results.items():
            text_key = str(result_key)
            if not isinstance(payload, dict) or not payload:
                continue
            for prefix in ("3D_SCENE_", "GPU_SCENE_"):
                suffix = text_key[len(prefix):] if text_key.startswith(prefix) else ""
                if suffix.isdigit():
                    dynamic.append(text_key)
                    break
        dynamic.sort(key=lambda item: int(item.rsplit("_", 1)[-1]))
        keys = tuple(keys) + tuple(dynamic)
    candidates = []
    for rank, key in enumerate(keys):
        item = results.get(key)
        if isinstance(item, dict) and item:
            stamp = str(item.get("finished_at") or item.get("created_at") or item.get("sampled_at") or "")
            candidates.append((stamp, -rank, item, key))
    if candidates:
        _stamp, _rank, result, key = max(candidates, key=lambda row: (row[0], row[1]))
        return dict(result), key

    # On a fresh app start, rehydrate the last locally saved report for this module.
    # The file scan is throttled so it does not run on every one-second UI refresh.
    now = _u151_time.monotonic()
    cache = getattr(app, "_u151_history_fallback", {}) or {}
    cached = cache.get(module) if isinstance(cache, dict) else None
    if isinstance(cached, dict) and now - float(cached.get("read_at", 0.0) or 0.0) < 10.0:
        entry = cached.get("entry")
        if isinstance(entry, dict):
            return dict(entry.get("payload") or {}), str(entry.get("test_id") or "SAVED_REPORT")
        return {}, ""
    entry = None
    try:
        history_reader = globals().get("_u149_read_history")
        if callable(history_reader):
            for candidate in history_reader(limit=80):
                if str(candidate.get("module", "")).upper() == module and isinstance(candidate.get("payload"), dict):
                    entry = candidate
                    break
    except Exception:
        entry = None
    try:
        if not isinstance(cache, dict):
            cache = {}
        cache[module] = {"read_at": now, "entry": entry}
        app._u151_history_fallback = cache
    except Exception:
        pass
    if isinstance(entry, dict):
        return dict(entry.get("payload") or {}), str(entry.get("test_id") or "SAVED_REPORT")
    return {}, ""


def _u151_metric_rows(module, live, result):
    report = result or {}
    if module == "CPU":
        return [
            ("Obciążenie systemu", _u151_number(live.get("cpu_percent")), "%"),
            ("Taktowanie", _u151_number(live.get("cpu_clock_mhz")), "MHz"),
            ("Temperatura", _u151_number(live.get("cpu_temp_c")), "°C"),
            ("Rdzenie / wątki", len(live.get("per_core_percent") or []) or _u151_os.cpu_count(), ""),
            ("SHA-256 na sekundę", _u151_number(report.get("operations_per_second")), "op/s"),
            ("Przepustowość testu", _u151_number(report.get("throughput_mib_s")), "MiB/s"),
        ]
    if module == "RAM":
        tested = report.get("size_mb", report.get("tested_mb", report.get("buffer_mb")))
        patterns = report.get("patterns_completed")
        patterns_total = report.get("patterns_total")
        pattern_text = f"{patterns}/{patterns_total}" if patterns is not None and patterns_total is not None else None
        write = _u151_number(report.get("write_MiBps", report.get("write_mib_s_overall")))
        verify = _u151_number(report.get("verify_MiBps", report.get("verify_mib_s_overall")))
        throughput = f"{write:.1f} / {verify:.1f}" if write is not None and verify is not None else None
        used = _u151_number(live.get("ram_percent"))
        available = _u151_number(live.get("ram_available_gb"))
        total = _u151_number(live.get("ram_total_gb"))
        avail_text = f"{available:.1f} / {total:.1f}" if available is not None and total is not None else None
        verified_bytes = _u151_number(report.get("bytes_verified"))
        verified_mib = verified_bytes / (1024 * 1024) if verified_bytes is not None else None
        return [
            ("Zajętość RAM", used, "%"),
            ("Dostępne / łącznie", avail_text, "GB"),
            ("Sprawdzony bufor", _u151_number(tested), "MB"),
            ("Wzorce ukończone", pattern_text, ""),
            ("Zapis / weryfikacja", throughput, "MiB/s"),
            ("Zweryfikowane dane", verified_mib, "MiB"),
        ]
    return [
        ("Obciążenie GPU", _u151_number(live.get("gpu_load_percent")), "%"),
        ("Temperatura GPU", _u151_number(live.get("gpu_temp_c")), "°C"),
        ("Zegar GPU", _u151_number(live.get("gpu_clock_mhz")), "MHz"),
        ("Średni FPS", _u151_number(report.get("average_fps", report.get("mean_fps"))), "FPS"),
        ("Szczyt FPS", _u151_number(report.get("peak_fps_1s", report.get("peak_fps"))), "FPS"),
        ("Wyrenderowane klatki", _u151_number(report.get("frames")), ""),
    ]


def _u151_format_metric(value, unit=""):
    if value is None:
        return "N/D"
    if isinstance(value, str):
        return value
    try:
        number = float(value)
        if not _u145_math.isfinite(number):
            return "N/D"
        if unit in ("%", "°C"):
            return f"{number:.1f} {unit}"
        if unit == "MHz":
            return f"{number:.0f} MHz"
        if unit == "FPS":
            return f"{number:.2f} FPS"
        if unit == "MiB/s":
            return f"{number:.1f} MiB/s"
        if unit == "op/s":
            return f"{number:,.1f} op/s"
        if unit == "MB":
            return f"{number:.0f} MB"
        if unit == "MiB":
            return f"{number:,.1f} MiB"
        return f"{number:.1f}" + ((" " + unit) if unit else "")
    except Exception:
        return str(value)


def _u151_report_summary(module, report, test_id=""):
    item = report if isinstance(report, dict) else {}
    if not item:
        return (
            f"{module}: NIE WYKONANO JESZCZE TESTU. Ten ekran pokazuje bieżące odczyty Windows "
            "oraz ostatni faktycznie zapisany wynik. N/D nie oznacza PASS."
        )
    state = str(item.get("state") or "N/D").upper()
    duration = _u151_number(item.get("duration_seconds"))
    duration_text = f"{duration:.1f} s" if duration is not None else "czas N/D"
    if module == "CPU":
        ops = _u151_number(item.get("operations_per_second"))
        load = _u151_number(item.get("cpu_load_avg_percent"))
        workers = item.get("workers", item.get("logical_processors", "N/D"))
        stages = item.get("stages")
        detail = f" • SHA-256/s: {_u151_format_metric(ops, 'op/s')} • obciążenie: {_u151_format_metric(load, '%')} • workerów: {workers}"
        if isinstance(stages, list):
            detail += f" • etapów: {len(stages)}/5"
    elif module == "RAM":
        tested = item.get("size_mb", item.get("tested_mb", item.get("buffer_mb", "N/D")))
        completed = item.get("patterns_completed")
        total = item.get("patterns_total")
        pattern_text = f"{completed}/{total} wzorców" if completed is not None and total is not None else "liczba wzorców N/D"
        write = _u151_number(item.get("write_MiBps", item.get("write_mib_s_overall")))
        verify = _u151_number(item.get("verify_MiBps", item.get("verify_mib_s_overall")))
        throughput = f" • zapis/weryfikacja {write:.1f}/{verify:.1f} MiB/s" if write is not None and verify is not None else ""
        detail = f" • bufor faktyczny: {tested} MB • {pattern_text}{throughput}"
        if item.get("error_offset") is not None:
            detail += f" • błąd przy bajcie {item['error_offset']}"
    else:
        avg = _u151_number(item.get("average_fps", item.get("mean_fps")))
        peak = _u151_number(item.get("peak_fps_1s", item.get("peak_fps")))
        frames = item.get("frames", "N/D")
        renderer = str(item.get("renderer") or item.get("error") or "renderer N/D")[:95]
        detail = f" • FPS: {_u151_format_metric(avg, 'FPS')} • peak: {_u151_format_metric(peak, 'FPS')} • klatki: {frames} • {renderer}"
    message = str(item.get("message") or item.get("note") or item.get("error") or "").strip()
    suffix = (" • " + message[:360]) if message else ""
    return f"OSTATNI TEST {module} • {state} • {duration_text}{detail}{suffix}"


def _u151_attach_console(app, module):
    if module not in ("CPU", "RAM", "GPU"):
        return False
    content = getattr(app, "content", None)
    if content is None:
        return False
    current = getattr(app, "_u151_hardware_console", None)
    try:
        if isinstance(current, dict) and current.get("module") == module and current["frame"].winfo_exists():
            return True
    except Exception:
        pass
    token = int(getattr(app, "_u151_console_token", 0) or 0) + 1
    app._u151_console_token = token
    t = app.colors()
    frame = _u151_tk.Frame(content, bg=t["panel"], highlightbackground=t["accent"], highlightthickness=1)
    children = content.winfo_children()
    if children:
        frame.pack(fill="x", padx=7, pady=(4, 6), before=children[0])
    else:
        frame.pack(fill="x", padx=7, pady=(4, 6))
    title = _u151_tk.Label(
        frame, text=f"MONITOR SPRZĘTU + OSTATNI WYNIK • {module}",
        bg=t["panel"], fg=t["accent"], font=app.fnt(10, "bold"), anchor="w"
    )
    title.pack(fill="x", padx=10, pady=(7, 2))
    subtitle = _u151_tk.Label(
        frame, text="Odczyty pochodzą z Windows / dostępnych czujników. Wynik benchmarku pochodzi z ukończonego testu, nie z animacji.",
        bg=t["panel"], fg=t["muted"], font=app.fnt(8), anchor="w", justify="left", wraplength=1400
    )
    subtitle.pack(fill="x", padx=10, pady=(0, 5))
    metrics = _u151_tk.Frame(frame, bg=t["panel"])
    metrics.pack(fill="x", padx=6, pady=(0, 5))
    rows = _u151_metric_rows(module, {}, {})
    value_widgets = {}
    for index, (label_text, _value, _unit) in enumerate(rows):
        card = _u151_tk.Frame(metrics, bg=t["card"], highlightbackground=t["bg"], highlightthickness=1)
        card.grid(row=0, column=index, sticky="nsew", padx=2, pady=2)
        _u151_tk.Label(card, text=label_text.upper(), bg=t["card"], fg=t["muted"], font=app.fnt(7, "bold"), anchor="w").pack(fill="x", padx=5, pady=(4, 1))
        value_widget = _u151_tk.Label(card, text="N/D", bg=t["card"], fg=t["accent2"], font=app.fnt(9, "bold"), anchor="w", justify="left")
        value_widget.pack(fill="x", padx=5, pady=(0, 4))
        metrics.grid_columnconfigure(index, weight=1, uniform="actual-hw-result")
        value_widgets[str(index)] = value_widget
    summary = _u151_tk.Text(frame, height=3, wrap="word", bg=t["card"], fg=t["fg"], insertbackground=t["fg"], relief="flat", font=app.fnt(8), padx=8, pady=5)
    summary.pack(fill="x", padx=8, pady=(0, 6))
    controls = _u151_tk.Frame(frame, bg=t["panel"])
    controls.pack(fill="x", padx=8, pady=(0, 7))
    direct_labels = {
        "CPU": "▶ START CPU SHA-256 • MULTI 15 S",
        "RAM": "▶ START RAM 256 MB",
        "GPU": "▶ START GPU OPENGL 10 S",
    }
    app.make_button(
        controls, direct_labels[module],
        lambda m=module: _u151_start_direct_test(app, m), "accent", side="left", ipady=3
    )
    if module == "CPU":
        app.make_button(
            controls, "CPU • 1 WĄTEK 15 S",
            lambda: _u151_start_direct_test(app, "CPU", cpu_mode="single"),
            "card", side="left", ipady=3
        )
    app.make_button(controls, "■ STOP TEST", lambda: _u151_stop_direct_test(app), "card", side="left", ipady=3)
    app.make_button(controls, f"KATALOG TESTÓW {module}", lambda m=module: _u93_show_catalog(app, m), "card", side="left", ipady=3)
    app.make_button(controls, "HISTORIA + PORÓWNANIE + CSV", lambda: _u149_show_history(app), "card", side="left", ipady=3)
    if module == "GPU":
        app.make_button(controls, "STUDIO OPENGL • 110 SCEN", lambda: _u66_show_3d_studio(app), "good", side="left", ipady=3)
    app._u151_hardware_console = {
        "module": module, "frame": frame, "title": title, "subtitle": subtitle,
        "metrics": value_widgets, "summary": summary, "token": token, "last_text": None,
    }
    _u151_refresh_console(app, token)
    try:
        app.after(1000, lambda current_token=token: _u151_tick(app, current_token))
    except Exception:
        pass
    return True


def _u151_refresh_console(app, token):
    panel = getattr(app, "_u151_hardware_console", None)
    if not isinstance(panel, dict) or panel.get("token") != token:
        return False
    frame = panel.get("frame")
    try:
        if frame is None or not frame.winfo_exists():
            return False
    except Exception:
        return False
    module = panel["module"]
    try:
        live = _u150_live_metrics(app, module)
    except Exception:
        live = {}
    report, test_id = _u151_last_result(app, module)
    rows = _u151_metric_rows(module, live, report)
    for index, (_caption, value, unit) in enumerate(rows):
        widget = panel.get("metrics", {}).get(str(index))
        try:
            if widget is not None and widget.winfo_exists():
                widget.configure(text=_u151_format_metric(value, unit))
        except Exception:
            pass
    summary_text = _u151_report_summary(module, report, test_id)
    if bool(getattr(app, "running", False)):
        current_status = ""
        try:
            status_widget = getattr(app, "header_status", None)
            if status_widget is not None and status_widget.winfo_exists():
                current_status = str(status_widget.cget("text") or "").strip()
        except Exception:
            pass
        running_text = f"TEST W TOKU • {current_status}" if current_status else "TEST W TOKU • zbieram próbki, raport pojawi się po zakończeniu."
        summary_text = running_text + "\n\n" + summary_text
    if summary_text != panel.get("last_text"):
        try:
            summary = panel["summary"]
            summary.configure(state="normal")
            summary.delete("1.0", "end")
            summary.insert("1.0", summary_text)
            summary.configure(state="disabled")
            panel["last_text"] = summary_text
        except Exception:
            pass
    state = str(report.get("state") or "").lower() if isinstance(report, dict) else ""
    color = app.colors().get("good", "#26cf88") if state in ("good", "pass", "completed") else (
        app.colors().get("bad", "#ff5d68") if state in ("bad", "fail", "error") else app.colors().get("warn", "#ffbd45")
    )
    try:
        panel["title"].configure(fg=color if state else app.colors().get("accent", "#4cc9ff"))
    except Exception:
        pass
    return True


def _u151_tick(app, token):
    panel = getattr(app, "_u151_hardware_console", None)
    if not isinstance(panel, dict) or panel.get("token") != token:
        return
    if not _u151_refresh_console(app, token):
        return
    try:
        app.after(1000, lambda current_token=token: _u151_tick(app, current_token))
    except Exception:
        pass


def _u151_show_module(app, module):
    result = _U151_ORIGINAL_SHOW_MODULE(app, module)
    key = _u151_module_key(module)
    if key:
        _u151_attach_console(app, key)
    return result


def _u151_wrap_direct_module(name, module):
    original = getattr(AppV43, name, None)
    if not callable(original):
        return False
    def wrapped(app, *args, **kwargs):
        result = original(app, *args, **kwargs)
        _u151_attach_console(app, module)
        return result
    wrapped.__name__ = "_u151_" + name
    setattr(AppV43, name, wrapped)
    return True




def _u151_direct_measurement_valid(module, report):
    """Require measured evidence before a direct hardware test can be marked GOOD."""
    if not isinstance(report, dict) or not report:
        return False
    if module == "CPU":
        operations = _u151_number(report.get("operations"))
        rate = _u151_number(report.get("operations_per_second"))
        return operations is not None and operations > 0 and rate is not None and rate > 0
    if module == "RAM":
        verified = _u151_number(report.get("bytes_verified"))
        tested = _u151_number(report.get("tested_mb", report.get("size_mb", report.get("buffer_mb"))))
        patterns = _u151_number(report.get("patterns_completed"))
        return verified is not None and verified > 0 and tested is not None and tested > 0 and (patterns is None or patterns > 0)
    if module == "GPU":
        frames = _u151_number(report.get("frames"))
        fps = _u151_number(report.get("average_fps", report.get("mean_fps")))
        renderer = str(report.get("renderer") or "").strip()
        return frames is not None and frames > 0 and fps is not None and fps > 0 and bool(renderer)
    return False


def _u151_normalize_direct_result(module, report, test_id, started_at, elapsed, stopped=False):
    data = dict(report) if isinstance(report, dict) else {}
    measured = _u151_direct_measurement_valid(module, data)
    original_state = str(data.get("state") or "warn").strip().lower()
    hard_fail = original_state in ("bad", "fail", "failed", "error")
    stopped = bool(stopped or data.get("cancelled") or data.get("stopped") or data.get("stopped_by_user"))
    if hard_fail:
        final_state = "error" if original_state == "error" else "bad"
    elif stopped:
        final_state = "warn"
    elif not measured:
        final_state = "warn"
    elif original_state in ("good", "pass", "ok", "completed", "success"):
        final_state = "good"
    else:
        final_state = "warn"
    finished = _u149_datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    data.update({
        "app": "NAPRAWA PC HARDWARE TEST PRO",
        "module": module,
        "test_id": test_id,
        "state": final_state,
        "started_at": str(started_at),
        "finished_at": str(data.get("finished_at") or finished),
        "duration_seconds": round(max(0.001, float(elapsed or 0.001)), 2),
        "measurement_verified": bool(measured),
        "cancelled": bool(stopped),
        "entry_point": "main-component-page",
    })
    if not measured and not data.get("error"):
        data["measurement_warning"] = (
            "Brak kompletnych, świeżych danych pomiarowych dla tego testu. "
            "Nie oznaczono go jako PASS; sprawdź dziennik i sterowniki."
        )
    return data


def _u151_run_direct_measurement(app, module, cpu_mode="multi"):
    """Run the real engine, validate its evidence, then publish the same result to UI and local history."""
    started_mono = _u151_time.perf_counter()
    started_at = _u149_datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    stopped_before = bool(getattr(app, "stop_requested", False))
    cpu_mode = "single" if str(cpu_mode).lower() == "single" else "multi"
    settings = {"entry_point": "main-component-page"}
    if module == "CPU":
        kind = "cpu_single" if cpu_mode == "single" else "cpu_multi"
        test_id = "CPU_DIRECT_SHA256_" + ("SINGLE" if cpu_mode == "single" else "MULTI")
        settings.update({"duration": 15, "cpu_mode": cpu_mode, "algorithm": "SHA-256"})
        app.queue_log("TEST CPU: rzeczywisty benchmark SHA-256, tryb " + cpu_mode + ", 15 s.")
    elif module == "RAM":
        kind = "ram_pattern"
        test_id = "RAM_DIRECT_256MB"
        settings.update({"memory_mb": 256, "test": "wzorce zapisu/odczytu/weryfikacji"})
        app.queue_log("TEST RAM: rzeczywisty test wzorców i weryfikacji bufora 256 MB.")
    else:
        kind = "gpu_scene"
        test_id = "GPU_DIRECT_OPENGL_SCENE_01"
        settings.update({"scene_id": 1, "duration_seconds": 10, "renderer": "OpenGL"})
        app.queue_log("TEST GPU: rzeczywista scena OpenGL 01, pomiar FPS przez 10 s.")

    raw_result = None
    error_text = None
    try:
        if module == "CPU":
            engine = globals().get("_u145_cpu_benchmark")
            if not callable(engine):
                raise RuntimeError("Brak silnika rzeczywistego benchmarku CPU SHA-256.")
            # This is the same measured engine used by the CPU catalog tests, not the old generic CPU-load button.
            raw_result = engine(app, kind, {"duration": 15, "entry_point": "main-page", "cpu_mode": cpu_mode})
        elif module == "RAM":
            engine = getattr(app, "_ram_test", None)
            if not callable(engine):
                raise RuntimeError("Brak silnika rzeczywistego testu RAM.")
            raw_result = engine(256)
        else:
            engine = globals().get("_u66_execute_gpu_scene")
            if not callable(engine):
                raise RuntimeError("Brak silnika renderera GPU/OpenGL.")
            raw_result = engine(app, 1, 10)
    except Exception as exc:
        error_text = type(exc).__name__ + ": " + str(exc)
        app.queue_log("TEST " + module + ": błąd rzeczywistego silnika: " + error_text)

    elapsed = max(0.001, _u151_time.perf_counter() - started_mono)
    if isinstance(raw_result, dict):
        raw = dict(raw_result)
    else:
        raw = {
            "state": "error" if error_text else "warn",
            "message": "Silnik nie zwrócił świeżego słownika raportu; poprzedni raport nie został użyty.",
        }
        if error_text:
            raw["error"] = error_text
    result = _u151_normalize_direct_result(
        module, raw, test_id, started_at, elapsed,
        stopped=bool(getattr(app, "stop_requested", False)) or stopped_before,
    )

    # Persist JSON + HTML locally so the visible result, history and export use one report.
    report_path = result.get("report_path")
    html_path = result.get("html_report_path")
    writer = globals().get("_u149_write_report")
    if not report_path and callable(writer):
        try:
            saved = writer(module, test_id, result, settings=settings)
            if saved:
                report_path = str(saved)
            html_path = result.get("html_report_path")
        except Exception as exc:
            result["report_save_error"] = type(exc).__name__ + ": " + str(exc)
    if report_path:
        result["report_path"] = str(report_path)
    if html_path:
        result["html_report_path"] = str(html_path)
    if not report_path:
        result.setdefault("report_save_error", "Raport nie został potwierdzony przez lokalny zapis JSON/HTML.")

    # Publish the new measurement under the keys read by the existing CPU/RAM/GPU pages.
    results = getattr(app, "results", None)
    if not isinstance(results, dict):
        results = {}
        app.results = results
    if module == "CPU":
        keys = ("CPU_BENCHMARK", "CPU_HASH_BENCHMARK")
    elif module == "RAM":
        keys = ("RAM_BENCHMARK",)
    else:
        keys = ("3D_SCENE_1", "GPU_3D")
    for key in keys:
        results[key] = result
        queue_results = getattr(app, "queue_results", None)
        if callable(queue_results):
            try:
                queue_results(key, result)
            except Exception as exc:
                try:
                    app.queue_log("Publikacja wyniku " + key + ": " + type(exc).__name__ + ": " + str(exc))
                except Exception:
                    pass
    # Explicit final status for the workbench and main result panel.
    state = str(result.get("state", "warn")).upper()
    summary = _u151_report_summary(module, result, test_id)
    lifecycle = "WYNIK TESTU • " + state + " • " + summary
    try:
        app._u151_direct_test_active = {
            "module": module, "test_id": test_id, "state": state,
            "started_at": started_at, "finished_at": result.get("finished_at"),
            "report_path": result.get("report_path"), "html_report_path": result.get("html_report_path"),
        }
    except Exception:
        pass
    try:
        app.queue_log(
            "TEST " + module + " ZAKOŃCZONY: " + state + " • " + summary
            + " • raport=" + str(result.get("html_report_path") or result.get("report_path") or "BRAK")
        )
    except Exception:
        pass

    def refresh_visible_results():
        panel = getattr(app, "_u151_hardware_console", None)
        if isinstance(panel, dict) and panel.get("module") == module:
            try:
                _u151_refresh_console(app, panel.get("token"))
            except Exception:
                pass
        workbench = getattr(app, "_u153_component_workbench", None)
        if isinstance(workbench, dict) and workbench.get("module") == module:
            try:
                _u153_workbench_tick(app, workbench.get("token"))
            except Exception:
                pass
    try:
        queue_action = getattr(app, "queue_action", None)
        if callable(queue_action):
            queue_action(refresh_visible_results)
    except Exception:
        pass
    return result


def _u151_start_direct_test(app, module, cpu_mode="multi"):
    """Start a bounded real CPU SHA-256, RAM pattern, or OpenGL test from the component page."""
    module = _u151_module_key(module)
    if module not in ("CPU", "RAM", "GPU"):
        return False
    if bool(getattr(app, "running", False)):
        _u151_messagebox.showwarning(
            "Test sprzętu",
            "Inny test już działa. Poczekaj na wynik albo użyj STOP TEST przed uruchomieniem następnego.",
            parent=app,
        )
        return False
    cpu_mode = "single" if str(cpu_mode).lower() == "single" else "multi"
    if module == "CPU":
        label = "CPU SHA-256 — " + ("1 wątek" if cpu_mode == "single" else "wielowątkowo") + " — 15 sekund"
        test_id = "CPU_DIRECT_SHA256_" + ("SINGLE" if cpu_mode == "single" else "MULTI")
    elif module == "RAM":
        label = "RAM — bufor 256 MB, zapis i weryfikacja wzorców"
        test_id = "RAM_DIRECT_256MB"
    else:
        label = "GPU OpenGL — scena 01, 10 sekund"
        test_id = "GPU_DIRECT_OPENGL_SCENE_01"

    worker = getattr(app, "worker", None)
    if not callable(worker):
        _u151_messagebox.showerror(
            "Test sprzętu",
            "Nie znaleziono bezpiecznego mechanizmu pracownika testów. Nie uruchomiono pomiaru.",
            parent=app,
        )
        return False
    try:
        app.stop_requested = False
        app._u151_direct_test_active = {
            "module": module, "test_id": test_id, "state": "STARTING",
            "started_at": _u149_datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        }
        panel = getattr(app, "_u151_hardware_console", None)
        if isinstance(panel, dict) and panel.get("module") == module:
            try:
                summary = panel["summary"]
                summary.configure(state="normal")
                summary.delete("1.0", "end")
                summary.insert("1.0", "STARTUJĘ RZECZYWISTY TEST • " + label + "\nOczekiwanie na pomiary i świeży raport; poprzedni wynik nie jest wynikiem nowego testu.")
                summary.configure(state="disabled")
                panel["last_text"] = None
            except Exception:
                pass
        try:
            app.queue_log("CENTRUM CPU/RAM/GPU: start — " + label)
        except Exception:
            pass
        worker(lambda: _u151_run_direct_measurement(app, module, cpu_mode))
        return True
    except Exception as exc:
        try:
            app.queue_log("Nie udało się uruchomić testu " + module + ": " + type(exc).__name__ + ": " + str(exc))
        except Exception:
            pass
        _u151_messagebox.showerror(
            "Test sprzętu",
            "Uruchomienie rzeczywistego testu nie powiodło się:\n" + type(exc).__name__ + ": " + str(exc),
            parent=app,
        )
        return False


def _u151_stop_direct_test(app):
    stop = getattr(app, "stop_current_test", None)
    if not callable(stop):
        _u151_messagebox.showinfo("STOP TEST", "Ta wersja nie udostępnia kontrolki STOP TEST.", parent=app)
        return False
    try:
        stop()
        return True
    except Exception as exc:
        try:
            app.queue_log("STOP TEST: " + type(exc).__name__ + ": " + str(exc))
        except Exception:
            pass
        _u151_messagebox.showerror("STOP TEST", str(exc), parent=app)
        return False


def _u151_selftest_hardware_result_console():
    assert _U151_HARDWARE_RESULT_CONSOLE_VERSION == "1.3.0"
    assert _u151_module_key("PROCESOR / CPU") == "CPU"
    assert _u151_module_key("PAMIĘĆ RAM") == "RAM"
    assert _u151_module_key("KARTA GRAFICZNA / GPU") == "GPU"
    cpu = {
        "state": "good", "operations": 600, "operations_per_second": 120.5, "workers": 8,
        "cpu_load_avg_percent": 82.4, "freq_mhz_last": 4200, "duration_seconds": 5.0,
        "message": "test syntetyczny raportu",
    }
    cpu_rows = _u151_metric_rows("CPU", {"cpu_percent": 75.0, "cpu_clock_mhz": 4200, "cpu_temp_c": None, "per_core_percent": [1, 2, 3]}, cpu)
    assert cpu_rows[0][1] == 75.0 and cpu_rows[4][1] == 120.5 and cpu_rows[3][1] == 3
    ram = {"state": "good", "size_mb": 256, "patterns_completed": 26, "patterns_total": 26,
           "bytes_verified": 268435456, "write_MiBps": 450.0, "verify_MiBps": 420.0, "duration_seconds": 5.0}
    ram_rows = _u151_metric_rows("RAM", {"ram_percent": 40.0, "ram_available_gb": 8.0, "ram_total_gb": 16.0}, ram)
    assert ram_rows[0][1] == 40.0 and ram_rows[2][1] == 256 and ram_rows[3][1] == "26/26" and ram_rows[5][1] == 256.0
    gpu = {"state": "good", "average_fps": 61.25, "peak_fps_1s": 75.0, "frames": 300, "renderer": "OpenGL genuine"}
    gpu_rows = _u151_metric_rows("GPU", {"gpu_load_percent": None, "gpu_temp_c": None, "gpu_clock_mhz": None}, gpu)
    assert gpu_rows[3][1] == 61.25 and gpu_rows[4][1] == 75.0 and gpu_rows[5][1] == 300
    assert "NIE WYKONANO" in _u151_report_summary("RAM", {}) and _u151_format_metric(None, "°C") == "N/D"
    scene_app = type("FakeGPUHistoryApp", (), {"results": {
        "3D_SCENE_17": {"state": "good", "average_fps": 81.5, "finished_at": "2026-10-23T15:08:00+00:00"}
    }})()
    scene_result, scene_key = _u151_last_result(scene_app, "GPU")
    assert scene_key == "3D_SCENE_17" and scene_result.get("average_fps") == 81.5, "main GPU console did not restore the latest scene-specific result"
    assert callable(_u151_attach_console) and callable(_u151_refresh_console) and callable(_u151_last_result)
    assert callable(_u151_start_direct_test) and callable(_u151_stop_direct_test)
    assert "direct_labels" in _u151_attach_console.__code__.co_varnames
    assert "worker" in _u151_start_direct_test.__code__.co_varnames
    class FakeDirectTestApp:
        def __init__(self):
            self.running = False
            self.stop_requested = True
            self.pending = None
            self.calls = []
            self.results = {}
        def worker(self, fn):
            self.pending = fn
        def _cpu_test(self, seconds):
            self.calls.append(("LEGACY_CPU", seconds))
        def _ram_test(self, size_mb):
            self.calls.append(("RAM_ENGINE", size_mb))
            return {"state": "good", "tested_mb": size_mb, "size_mb": size_mb,
                    "patterns_completed": 26, "patterns_total": 26,
                    "bytes_verified": size_mb * 1024 * 1024, "write_MiBps": 420.0,
                    "verify_MiBps": 400.0, "message": "RAM pattern selftest"}
        def queue_results(self, key, report):
            self.results[key] = report
            self.calls.append(("QUEUE_RESULT", key))
        def queue_action(self, fn):
            fn()
        def queue_log(self, text):
            self.calls.append(("LOG", text))
    fake = FakeDirectTestApp()
    original_cpu_engine = globals().get("_u145_cpu_benchmark")
    original_report_writer = globals().get("_u149_write_report")
    original_gpu_scene = globals().get("_u66_execute_gpu_scene")
    saved_reports = []
    def fake_cpu_engine(app, kind, settings):
        app.calls.append(("CPU_ENGINE", kind, dict(settings)))
        return {"state": "good", "operations": 1200, "operations_per_second": 80.0,
                "throughput_mib_s": 160.0, "workers": 4, "duration_seconds": 15.0,
                "cpu_load_avg_percent": 82.0, "message": "CPU SHA-256 measurement"}
    def fake_report_writer(module, test_id, report, base_dir=None, settings=None):
        report.update({"report_path": "SELFTEST/" + test_id + ".json",
                       "html_report_path": "SELFTEST/" + test_id + ".html",
                       "created_at": "2026-10-23T12:00:00+00:00",
                       "finished_at": "2026-10-23T12:00:15+00:00"})
        saved_reports.append((module, test_id, dict(settings or {})))
        return report["report_path"]
    def fake_gpu_scene(app, scene, seconds):
        app.calls.append(("GPU_ENGINE", scene, seconds))
        return {"state": "good", "scene_id": scene, "average_fps": 61.5,
                "peak_fps_1s": 75.0, "frames": 615, "renderer": "OpenGL selftest",
                "duration_seconds": float(seconds)}
    try:
        globals()["_u145_cpu_benchmark"] = fake_cpu_engine
        globals()["_u149_write_report"] = fake_report_writer
        globals()["_u66_execute_gpu_scene"] = fake_gpu_scene
        assert _u151_start_direct_test(fake, "CPU"), "multithread CPU test did not start"
        assert callable(fake.pending), "CPU worker was not created"
        fake.pending()
        cpu_result = fake.results.get("CPU_BENCHMARK", {})
        assert ("CPU_ENGINE", "cpu_multi", {"duration": 15, "entry_point": "main-page", "cpu_mode": "multi"}) in fake.calls, "main-page CPU route must call the real SHA-256 engine"
        assert "LEGACY_CPU" not in [row[0] for row in fake.calls if row], "main-page CPU route still uses the generic legacy CPU test"
        assert cpu_result.get("operations_per_second") == 80.0 and cpu_result.get("measurement_verified"), "CPU result did not map measured throughput"
        assert cpu_result.get("report_path") == "SELFTEST/CPU_DIRECT_SHA256_MULTI.json", "CPU JSON/HTML report was not saved"
        assert any(row[0] == "CPU" and row[1] == "CPU_DIRECT_SHA256_MULTI" for row in saved_reports), "CPU report missing from local history"
        assert _u151_start_direct_test(fake, "CPU", cpu_mode="single"), "single-thread CPU test did not start"
        fake.pending()
        assert any(row[0] == "CPU_ENGINE" and row[1] == "cpu_single" for row in fake.calls), "single-thread CPU route did not select single-thread engine"
        assert fake.results["CPU_BENCHMARK"].get("test_id") == "CPU_DIRECT_SHA256_SINGLE"
        assert _u151_start_direct_test(fake, "RAM"), "RAM test did not start"
        fake.pending()
        ram_result = fake.results.get("RAM_BENCHMARK", {})
        assert ("RAM_ENGINE", 256) in fake.calls, "RAM route did not call the real RAM engine"
        assert ram_result.get("measurement_verified") and ram_result.get("bytes_verified") == 256 * 1024 * 1024, "RAM report missing verified byte count"
        assert ram_result.get("report_path") == "SELFTEST/RAM_DIRECT_256MB.json", "RAM report was not saved"
        assert _u151_start_direct_test(fake, "GPU"), "GPU test did not start"
        fake.pending()
        gpu_result = fake.results.get("GPU_3D", {})
        assert ("GPU_ENGINE", 1, 10) in fake.calls, "GPU route did not call the real OpenGL renderer"
        assert gpu_result.get("measurement_verified") and gpu_result.get("average_fps") == 61.5, "GPU FPS was not validated and published"
        assert gpu_result.get("report_path") == "SELFTEST/GPU_DIRECT_OPENGL_SCENE_01.json", "GPU report was not saved"
        assert fake.stop_requested is False, "starting any test should clear an old stop request"
        assert len(saved_reports) == 4, "each direct CPU/RAM/GPU run should persist its own report"
    finally:
        if original_cpu_engine is None:
            globals().pop("_u145_cpu_benchmark", None)
        else:
            globals()["_u145_cpu_benchmark"] = original_cpu_engine
        if original_report_writer is None:
            globals().pop("_u149_write_report", None)
        else:
            globals()["_u149_write_report"] = original_report_writer
        if original_gpu_scene is None:
            globals().pop("_u66_execute_gpu_scene", None)
        else:
            globals()["_u66_execute_gpu_scene"] = original_gpu_scene
    assert callable(AppV43.show_module)
    print("HARDWARE_RESULT_CONSOLE_SELFTEST_OK: live readings, visible direct CPU/RAM/GPU starters, STOP control, result/history mapping")


_U151_ORIGINAL_SHOW_MODULE_METHOD = AppV43.show_module
AppV43.show_module = _u151_show_module
_u151_wrap_direct_module("module_cpu", "CPU")
_u151_wrap_direct_module("module_ram", "RAM")
_u151_wrap_direct_module("module_gpu", "GPU")


if __name__ == "__main__" and "--selftest-hardware-result-console" in _u151_sys.argv:
    try:
        _u151_selftest_hardware_result_console()
        raise SystemExit(0)
    except Exception as _u151_exc:
        import traceback as _u151_traceback
        print("HARDWARE_RESULT_CONSOLE_SELFTEST_FAILED:", type(_u151_exc).__name__, str(_u151_exc))
        _u151_traceback.print_exc()
        raise SystemExit(1)
