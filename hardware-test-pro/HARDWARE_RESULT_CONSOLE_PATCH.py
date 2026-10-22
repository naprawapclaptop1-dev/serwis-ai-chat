# v4.3.150: explicit result console for the real CPU/RAM/GPU pages.
import os as _u151_os
import sys as _u151_sys
import time as _u151_time
import tkinter as _u151_tk

_U151_HARDWARE_RESULT_CONSOLE_VERSION = "1.0.0"
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
    app.make_button(controls, f"KATALOG TESTÓW {module}", lambda m=module: _u93_show_catalog(app, m), "accent", side="left", ipady=3)
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


def _u151_selftest_hardware_result_console():
    assert _U151_HARDWARE_RESULT_CONSOLE_VERSION == "1.0.0"
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
    assert callable(_u151_attach_console) and callable(_u151_refresh_console) and callable(_u151_last_result)
    assert callable(AppV43.show_module)
    print("HARDWARE_RESULT_CONSOLE_SELFTEST_OK: real Windows CPU/RAM/GPU metrics, explicit last benchmark, report/catalog actions, no sample values")


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
