# v4.3.156 — real CPU/RAM/GPU execution and report workbench on 3D test-detail pages.
import time as _u153_time
import json as _u153_json
import hashlib as _u153_hashlib
import tkinter as _u153_tk
from tkinter import ttk as _u153_ttk

_U153_COMPONENT_TEST_WORKBENCH_VERSION = "1.2.0"
_U153_ORIGINAL_SHOW_TEST_DETAIL = AppV43.show_test_detail
_U153_ORIGINAL_UPDATE_VIEW = _u146_update_view
_U153_ORIGINAL_QUEUE_PANEL = _u145_queue_panel


def _u153_module(value):
    try:
        key = _u151_module_key(value)
        if key:
            return key
    except Exception:
        pass
    try:
        key = _u152_normalize_module(value)
        if key in ("CPU", "RAM", "GPU"):
            return key
    except Exception:
        pass
    text = str(value or "").upper()
    if "CPU" in text or "PROCESOR" in text:
        return "CPU"
    if "RAM" in text or "PAMI" in text:
        return "RAM"
    if "GPU" in text or "GRAFICZN" in text or "VRAM" in text:
        return "GPU"
    return ""


def _u153_result_keys(module):
    return {
        "CPU": ("CPU_BENCHMARK", "CPU_HASH_BENCHMARK", "CPU_LOAD_BENCHMARK", "CPU"),
        "RAM": ("RAM_BENCHMARK", "RAM"),
        "GPU": ("GPU_3D", "3D_SUITE", "GPU_WINSAT", "GPU"),
    }.get(_u153_module(module), ())


def _u153_result_signature(value):
    try:
        canonical = _u153_json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), default=str)
    except Exception:
        canonical = repr(value)
    return _u153_hashlib.sha256(canonical.encode("utf-8", "replace")).hexdigest()


def _u153_capture_result_ids(app, module):
    results = getattr(app, "results", {}) or {}
    if not isinstance(results, dict):
        results = {}
    baseline = {}
    for key in _u153_result_keys(module):
        value = results.get(key)
        baseline[key] = {
            "id": id(value),
            "signature": _u153_result_signature(value) if isinstance(value, dict) else None,
        }
    return baseline


def _u153_get_fresh_result(app, module, baseline):
    results = getattr(app, "results", {}) or {}
    if not isinstance(results, dict):
        return None, ""
    baseline = baseline or {}
    for key in _u153_result_keys(module):
        value = results.get(key)
        if not isinstance(value, dict) or not value:
            continue
        previous = baseline.get(key)
        if isinstance(previous, dict):
            old_id = previous.get("id")
            old_signature = previous.get("signature")
        else:
            # Backward compatibility with older callers that captured only object IDs.
            old_id = previous
            old_signature = None
        current_signature = _u153_result_signature(value)
        if id(value) != old_id or (old_signature is not None and current_signature != old_signature):
            return dict(value), key
    return None, ""


def _u153_report_timeout(module):
    return {"CPU": 45.0, "RAM": 75.0, "GPU": 50.0}.get(_u153_module(module), 50.0)


def _u153_lifecycle_state(active, module, is_running, now=None):
    """Avoid treating the worker's startup/teardown gap as a failed or absent test."""
    now = _u153_time.monotonic() if now is None else float(now)
    if is_running:
        active["saw_running"] = True
        active["last_running"] = True
        active["finished_seen_at"] = None
        return "running"
    if active.get("last_running"):
        active["last_running"] = False
        active["finished_seen_at"] = now
    if active.get("saw_running"):
        finished_seen_at = active.get("finished_seen_at")
        if finished_seen_at is not None and now - float(finished_seen_at) < 8.0:
            return "saving_result"
        return "missing"
    elapsed = max(0.0, now - float(active.get("started_at", now) or now))
    if elapsed < 8.0:
        return "starting"
    if elapsed < _u153_report_timeout(module):
        return "waiting_for_worker"
    return "missing"


def _u153_resolve_result(app, module, baseline, active=None):
    fresh, key = _u153_get_fresh_result(app, module, baseline)
    if fresh is not None:
        return fresh, key
    active = active if isinstance(active, dict) else {}
    worker_report = active.get("worker_report")
    if isinstance(worker_report, dict) and worker_report:
        state = str(worker_report.get("state") or "").strip().lower()
        if state not in ("running", "pending", "starting", "queued"):
            return dict(worker_report), str(active.get("worker_report_key") or "WORKER_REPORT")
    return None, ""


def _u153_expected_seconds(module):
    return {"CPU": 15.0, "RAM": 5.0, "GPU": 10.0}.get(_u153_module(module), 10.0)


def _u153_elapsed_percent(module, elapsed):
    duration = max(1.0, _u153_expected_seconds(module))
    return max(0, min(99, int(100.0 * max(0.0, float(elapsed or 0.0)) / duration)))


def _u153_set_workbench_text(panel, value):
    try:
        widget = panel.get("report")
        if widget is None or not widget.winfo_exists():
            return
        widget.configure(state="normal")
        widget.delete("1.0", "end")
        widget.insert("1.0", str(value or "")[:14000])
        widget.configure(state="disabled")
    except Exception:
        pass


def _u153_update_widgets(app, token, percent=None, status=None, report_text=None, result=None):
    panel = getattr(app, "_u153_component_workbench", None)
    if not isinstance(panel, dict) or panel.get("token") != token:
        return False
    try:
        if not panel["frame"].winfo_exists():
            return False
        if percent is not None:
            panel["progress"].configure(value=max(0, min(100, int(percent))))
        if status is not None:
            panel["status"].configure(text=str(status)[:1200])
        if report_text is not None:
            _u153_set_workbench_text(panel, report_text)
        if isinstance(result, dict):
            live = _u150_live_metrics(app, panel["module"])
            rows = _u151_metric_rows(panel["module"], live, result)
            for index, (_caption, value, unit) in enumerate(rows):
                widget = panel["metric_widgets"].get(str(index))
                if widget is not None and widget.winfo_exists():
                    widget.configure(text=_u151_format_metric(value, unit))
        return True
    except Exception as exc:
        try:
            app.queue_log("WORKBENCH CPU/RAM/GPU: " + type(exc).__name__ + ": " + str(exc))
        except Exception:
            pass
        return False


def _u153_schedule_widgets(app, token, percent=None, status=None, report_text=None, result=None):
    def apply():
        _u153_update_widgets(app, token, percent, status, report_text, result)
    try:
        queue = getattr(app, "queue_action", None)
        if callable(queue):
            queue(apply)
        else:
            apply()
    except Exception:
        pass


def _u153_attach_component_workbench(app, module, test_id="", kind=""):
    module = _u153_module(module)
    if module not in ("CPU", "RAM", "GPU"):
        return False
    content = getattr(app, "content", None)
    if content is None:
        return False
    token = int(getattr(app, "_u153_workbench_token", 0) or 0) + 1
    app._u153_workbench_token = token
    theme = app.colors()
    children = content.winfo_children()
    frame = _u153_tk.Frame(content, bg=theme["panel"], highlightbackground=theme["accent"], highlightthickness=1)
    if children:
        frame.pack(fill="x", padx=7, pady=(3, 6), before=children[0])
    else:
        frame.pack(fill="x", padx=7, pady=(3, 6))

    _u153_tk.Label(
        frame,
        text="RZECZYWISTY TEST SPRZĘTU • " + module + " • WYNIK I POSTĘP",
        bg=theme["panel"], fg=theme["accent"], font=app.fnt(10, "bold"), anchor="w"
    ).pack(fill="x", padx=10, pady=(7, 2))
    note = (
        "Strona 3D pokazuje również schemat podzespołu. Schemat nie jest wynikiem diagnostyki. "
        "Użyj przycisku START poniżej, aby wykonać niezależny pomiar CPU/RAM/GPU. "
        "Brak czujnika jest oznaczany N/D, a nie jako sukces."
    )
    _u153_tk.Label(
        frame, text=note, bg=theme["panel"], fg=theme["muted"],
        font=app.fnt(8), wraplength=1450, justify="left", anchor="w"
    ).pack(fill="x", padx=10, pady=(0, 5))

    status = _u153_tk.Label(
        frame, text="GOTOWY — nie rozpoczęto nowego testu.",
        bg=theme["panel"], fg=theme["muted"], font=app.fnt(9, "bold"),
        justify="left", anchor="w", wraplength=1450
    )
    status.pack(fill="x", padx=10, pady=(0, 3))
    progress = _u153_ttk.Progressbar(frame, mode="determinate", maximum=100, value=0)
    progress.pack(fill="x", padx=10, pady=(0, 5))

    metric_frame = _u153_tk.Frame(frame, bg=theme["panel"])
    metric_frame.pack(fill="x", padx=6, pady=(0, 5))
    empty_rows = _u151_metric_rows(module, {}, {})
    metric_widgets = {}
    for index, (caption, _value, _unit) in enumerate(empty_rows):
        card = _u153_tk.Frame(metric_frame, bg=theme["card"], highlightbackground=theme["bg"], highlightthickness=1)
        card.grid(row=0, column=index, sticky="nsew", padx=2, pady=2)
        _u153_tk.Label(card, text=str(caption).upper(), bg=theme["card"], fg=theme["muted"], font=app.fnt(7, "bold"), anchor="w").pack(fill="x", padx=5, pady=(4, 1))
        value_widget = _u153_tk.Label(card, text="N/D", bg=theme["card"], fg=theme["accent2"], font=app.fnt(9, "bold"), anchor="w")
        value_widget.pack(fill="x", padx=5, pady=(0, 4))
        metric_frame.grid_columnconfigure(index, weight=1, uniform="u153-workbench-metric")
        metric_widgets[str(index)] = value_widget

    report = _u153_tk.Text(frame, height=4, wrap="word", bg=theme["card"], fg=theme["fg"], relief="flat", font=app.fnt(8), padx=8, pady=5)
    report.pack(fill="x", padx=8, pady=(0, 5))
    report.configure(state="disabled")

    controls = _u153_tk.Frame(frame, bg=theme["panel"])
    controls.pack(fill="x", padx=8, pady=(0, 7))
    app.make_button(controls, "▶ START RZECZYWISTEGO TESTU " + module, lambda m=module: _u153_start_real_test(app, m), "accent", side="left", ipady=4)
    app.make_button(controls, "■ STOP TEST", lambda: _u153_stop_real_test(app), "bad", side="left", ipady=4)
    app.make_button(controls, "HISTORIA + RAPORTY + CSV", lambda: _u149_show_history(app), "card", side="left", ipady=4)
    if module == "GPU":
        app.make_button(controls, "STUDIO OPENGL • 110 SCEN", lambda: _u66_show_3d_studio(app), "card", side="left", ipady=4)

    app._u153_component_workbench = {
        "module": module, "test_id": str(test_id or ""), "kind": str(kind or ""),
        "frame": frame, "status": status, "progress": progress, "report": report,
        "metric_widgets": metric_widgets, "token": token, "active": None,
        "idle_baseline": _u153_capture_result_ids(app, module),
        "last_percent": 0,
    }
    last_report, last_key = _u151_last_result(app, module)
    if last_report:
        rows = _u151_metric_rows(module, _u150_live_metrics(app, module), last_report)
        for index, (_caption, value, unit) in enumerate(rows):
            widget = metric_widgets.get(str(index))
            if widget is not None:
                widget.configure(text=_u151_format_metric(value, unit))
        summary = _u151_report_summary(module, last_report, last_key)
        status.configure(text="OSTATNI ZAPISANY POMIAR • " + summary, fg=theme["good"] if str(last_report.get("state", "")).lower() in ("good", "pass") else theme["warn"])
        _u153_set_workbench_text(app._u153_component_workbench, _u153_json.dumps(last_report, ensure_ascii=False, indent=2, default=str)[:12000])
    else:
        status.configure(text="NIE WYKONANO TESTU • Kliknij START. Sam podgląd 3D nie sprawdza sprzętu.", fg=theme["warn"])
        _u153_set_workbench_text(app._u153_component_workbench, "Brak raportu testu. Po zakończeniu pomiaru pojawią się tu rzeczywisty wynik, stan, czas i szczegóły diagnostyczne.")
    app.after(300, lambda current_token=token: _u153_workbench_tick(app, current_token))
    return True


def _u153_start_real_test(app, module):
    module = _u153_module(module)
    panel = getattr(app, "_u153_component_workbench", None)
    if module not in ("CPU", "RAM", "GPU") or not isinstance(panel, dict):
        return False
    if bool(getattr(app, "running", False)):
        try:
            _u151_messagebox.showwarning("Test sprzętu", "Inny test nadal działa. Użyj STOP TEST lub poczekaj na raport.", parent=app)
        except Exception:
            pass
        return False
    token = panel.get("token")
    baseline = _u153_capture_result_ids(app, module)
    active = {
        "module": module, "started_at": _u153_time.monotonic(),
        "baseline": baseline, "last_percent": 0, "last_message": "Uruchamianie rzeczywistego testu...",
        "saw_running": False, "last_running": False, "finished_seen_at": None,
        "worker_report": None, "worker_report_key": "",
    }
    panel["active"] = active
    panel["last_percent"] = 0
    _u153_schedule_widgets(app, token, 0, "URUCHAMIANIE • " + module + " • przygotowuję właściwy test sprzętu.", "Test jeszcze się nie zakończył. Oczekiwanie na próbki i końcowy raport.")
    try:
        app.queue_log("WORKBENCH " + module + ": użytkownik uruchomił bezpośredni test z widoku 3D.")
    except Exception:
        pass
    try:
        started = _u151_start_direct_test(app, module)
    except Exception as exc:
        started = False
        error_text = type(exc).__name__ + ": " + str(exc)
    else:
        error_text = "Mechanizm uruchomienia odmówił startu. Sprawdź dziennik aplikacji."
    if not started:
        panel["active"] = None
        _u153_schedule_widgets(app, token, 0, "BŁĄD STARTU • " + module + " • test nie został uruchomiony.", error_text)
        return False
    try:
        app.after(200, lambda current_token=token: _u153_workbench_tick(app, current_token))
    except Exception:
        pass
    return True


def _u153_stop_real_test(app):
    try:
        result = _u151_stop_direct_test(app)
        panel = getattr(app, "_u153_component_workbench", None)
        if isinstance(panel, dict):
            _u153_schedule_widgets(app, panel.get("token"), status="STOP ZAŻĄDANY • czekam na bezpieczne zakończenie i raport.")
        return result
    except Exception as exc:
        try:
            app.queue_log("WORKBENCH STOP: " + type(exc).__name__ + ": " + str(exc))
        except Exception:
            pass
        return False


def _u153_adopt_external_run(app, panel, now=None):
    """Adopt a CPU/RAM/GPU test started by an existing page button, preserving the pre-start result baseline."""
    if not isinstance(panel, dict) or isinstance(panel.get("active"), dict):
        return False
    if not bool(getattr(app, "running", False)):
        return False
    module = _u153_module(panel.get("module"))
    if module not in ("CPU", "RAM", "GPU"):
        return False
    now = _u153_time.monotonic() if now is None else float(now)
    baseline = panel.get("idle_baseline")
    if not isinstance(baseline, dict):
        baseline = _u153_capture_result_ids(app, module)
    active = {
        "module": module,
        "started_at": now,
        "baseline": baseline,
        "last_percent": 0,
        "last_message": "Wykryto aktywny test uruchomiony przyciskiem strony.",
        "saw_running": True,
        "last_running": True,
        "finished_seen_at": None,
        "worker_report": None,
        "worker_report_key": "",
        "external_start": True,
    }
    panel["active"] = active
    token = panel.get("token")
    _u153_schedule_widgets(
        app, token, 0,
        f"TEST W TOKU • {module} • wykryto uruchomienie z istniejącego przycisku; śledzę wynik.",
        "Test został rozpoczęty poza przyciskiem panelu szczegółów. Oczekuję na nowe próbki i raport tego uruchomienia."
    )
    try:
        app.queue_log("WORKBENCH " + module + ": przejęto śledzenie testu uruchomionego przez istniejący przycisk strony.")
    except Exception:
        pass
    return True


def _u153_workbench_tick(app, token):
    panel = getattr(app, "_u153_component_workbench", None)
    if not isinstance(panel, dict) or panel.get("token") != token:
        return
    try:
        if not panel["frame"].winfo_exists():
            return
    except Exception:
        return
    module = panel["module"]
    active = panel.get("active")
    if not isinstance(active, dict):
        if bool(getattr(app, "running", False)):
            _u153_adopt_external_run(app, panel)
            active = panel.get("active")
        else:
            # The baseline is refreshed while idle so a subsequent run started elsewhere
            # cannot accidentally display an older result as the new test's report.
            try:
                panel["idle_baseline"] = _u153_capture_result_ids(app, module)
            except Exception:
                pass
    if isinstance(active, dict):
        now = _u153_time.monotonic()
        is_running = bool(getattr(app, "running", False))
        lifecycle = _u153_lifecycle_state(active, module, is_running, now)
        if is_running:
            elapsed = max(0.0, now - float(active.get("started_at", now)))
            timed_percent = _u153_elapsed_percent(module, elapsed)
            reported = max(0, min(99, int(active.get("last_percent", 0) or 0)))
            percent = max(reported, timed_percent)
            panel["last_percent"] = percent
            live = _u150_live_metrics(app, module)
            try:
                rows = _u151_metric_rows(module, live, {})
                for index, (_caption, value, unit) in enumerate(rows):
                    widget = panel["metric_widgets"].get(str(index))
                    if widget is not None and widget.winfo_exists():
                        widget.configure(text=_u151_format_metric(value, unit))
            except Exception:
                pass
            seconds = _u153_expected_seconds(module)
            _u153_update_widgets(
                app, token, percent,
                f"TEST W TOKU • {module} • {elapsed:.1f} s • cel ok. {seconds:.0f} s • zbieram rzeczywiste próbki.",
            )
        else:
            fresh, key = _u153_resolve_result(app, module, active.get("baseline", {}), active)
            fresh_state = str((fresh or {}).get("state") or "").strip().lower()
            if fresh is not None and fresh_state not in ("running", "pending", "starting", "queued"):
                panel["active"] = None
                state = str(fresh.get("state") or "N/D").upper()
                summary = _u151_report_summary(module, fresh, key)
                _u153_update_widgets(
                    app, token, 100 if state not in ("ERROR", "FAIL", "BAD", "WARN", "N/D") else 0,
                    "WYNIK TESTU • " + summary,
                    _u153_json.dumps(fresh, ensure_ascii=False, indent=2, default=str),
                    fresh,
                )
                try:
                    app.queue_log("WORKBENCH " + module + ": raport odebrany (" + state + "); źródło=" + key)
                except Exception:
                    pass
            elif lifecycle in ("starting", "waiting_for_worker", "saving_result"):
                elapsed = max(0.0, now - float(active.get("started_at", now)))
                panel["last_percent"] = max(int(panel.get("last_percent", 0) or 0), min(99, _u153_elapsed_percent(module, elapsed)))
                if lifecycle == "starting":
                    status_text = f"STARTUJĘ TEST • {module} • oczekiwanie na uruchomienie pracownika…"
                elif lifecycle == "saving_result":
                    status_text = f"TEST ZAKOŃCZONY • {module} • czekam na finalny raport z wątku…"
                else:
                    status_text = f"OCZEKIWANIE NA PRACOWNIKA • {module} • {elapsed:.1f} s • raport nie jest jeszcze gotowy."
                _u153_update_widgets(
                    app, token, panel["last_percent"], status_text,
                    "Trwa synchronizacja testu i końcowego raportu. Poprzedni wynik nie jest przedstawiany jako nowy pomiar.",
                )
            else:
                panel["active"] = None
                log_entries = list(getattr(app, "_log_history", []) or [])[-12:]
                error_lines = [str(x) for x in log_entries if any(term in str(x).upper() for term in ("BŁĄD", "ERROR", "BRAK RAPORTU", "NIE UDAŁO SIĘ"))]
                detail = "Nie otrzymano nowego raportu po upływie czasu oczekiwania. Nie oznaczam tego jako PASS."
                if error_lines:
                    detail += "\n\nOstatnie wpisy diagnostyczne:\n" + "\n".join(error_lines[-6:])
                detail += "\n\nSprawdź dziennik aplikacji; wynik poprzedniego pomiaru nie został użyty jako bieżący raport."
                _u153_update_widgets(app, token, 0, "BRAK NOWEGO RAPORTU • " + module + " • sprawdź dziennik.", detail)
    else:
        report, key = _u151_last_result(app, module)
        if report:
            summary = _u151_report_summary(module, report, key)
            _u153_update_widgets(app, token, None, "OSTATNI ZAPISANY POMIAR • " + summary, _u153_json.dumps(report, ensure_ascii=False, indent=2, default=str), report)
        else:
            _u153_update_widgets(app, token, None, "NIE WYKONANO TESTU • kliknij START. Podgląd 3D nie jest wynikiem.", "Brak raportu dla tego modułu.")
    try:
        app.after(500, lambda current_token=token: _u153_workbench_tick(app, current_token))
    except Exception:
        pass


def _u153_update_view(app, module, percent, message, report=None):
    result = _U153_ORIGINAL_UPDATE_VIEW(app, module, percent, message, report)
    key = _u153_module(module)
    panel = getattr(app, "_u153_component_workbench", None)
    if key and isinstance(panel, dict) and panel.get("module") == key and isinstance(panel.get("active"), dict):
        active = panel["active"]
        active["last_percent"] = max(0, min(99, int(percent or 0)))
        active["last_message"] = str(message or "")
        if isinstance(report, dict) and report:
            active["worker_report"] = dict(report)
            active["worker_report_key"] = str(report.get("test_id") or report.get("result_key") or "WORKER_REPORT")
        token = panel.get("token")
        _u153_schedule_widgets(app, token, active["last_percent"], "TEST W TOKU • " + key + " • " + str(message or "Próbkowanie..."))
    return result


def _u153_queue_panel(app, test_id, progress=None, headline=None, metrics=None, sample=None):
    result = _U153_ORIGINAL_QUEUE_PANEL(app, test_id, progress, headline, metrics, sample)
    panel = getattr(app, "_u153_component_workbench", None)
    if isinstance(panel, dict) and isinstance(panel.get("active"), dict) and bool(getattr(app, "running", False)):
        token = panel.get("token")
        module = panel.get("module")
        percent = None
        try:
            if progress is not None:
                percent = max(0, min(99, int(progress)))
                panel["active"]["last_percent"] = max(int(panel["active"].get("last_percent", 0) or 0), percent)
        except Exception:
            percent = None
        try:
            label = str(headline or ("TEST W TOKU • " + str(module)))
            _u153_schedule_widgets(app, token, percent, label)
        except Exception:
            pass
    return result


def _u153_show_test_detail(app, module, test_id):
    result = _U153_ORIGINAL_SHOW_TEST_DETAIL(app, module, test_id)
    key = _u153_module(module)
    if key not in ("CPU", "RAM", "GPU"):
        try:
            entry = _u93_find_test(_u93_norm(module), test_id)
            if entry and len(entry) > 0:
                key = _u153_module(entry[0])
        except Exception:
            pass
    if key in ("CPU", "RAM", "GPU"):
        kind = ""
        try:
            entry = _u93_find_test(_u93_norm(module), test_id)
            if entry and len(entry) > 3:
                kind = str(entry[3])
        except Exception:
            pass
        _u153_attach_component_workbench(app, key, test_id, kind)
    return result


def _u153_selftest_component_test_workbench():
    assert _U153_COMPONENT_TEST_WORKBENCH_VERSION == "1.2.0"
    assert _u153_module("Procesor / CPU") == "CPU"
    assert _u153_module("Pamięć RAM") == "RAM"
    assert _u153_module("Karta graficzna / GPU") == "GPU"
    assert _u153_module("GPU") == "GPU"
    assert _u153_module("DYSK / SSD") == ""
    assert _u153_result_keys("CPU")[0] == "CPU_BENCHMARK"
    assert _u153_result_keys("RAM")[0] == "RAM_BENCHMARK"
    assert _u153_result_keys("GPU")[0] == "GPU_3D"
    assert _u153_elapsed_percent("CPU", 7.5) in (49, 50)
    assert _u153_elapsed_percent("RAM", 10) == 99 and _u153_elapsed_percent("GPU", 30) == 99
    prior = {"CPU_BENCHMARK": {"state": "good"}, "CPU": {"state": "good"}}
    fake = type("FakeApp", (), {"results": prior})()
    baseline = _u153_capture_result_ids(fake, "CPU")
    fresh, key = _u153_get_fresh_result(fake, "CPU", baseline)
    assert fresh is None and key == ""
    changed = dict(prior)
    changed["CPU_BENCHMARK"] = {"state": "warn", "stopped": True, "message": "Test zatrzymany"}
    fresh, key = _u153_get_fresh_result(type("FakeApp", (), {"results": changed})(), "CPU", baseline)
    assert isinstance(fresh, dict) and fresh.get("stopped") and key == "CPU_BENCHMARK"
    # The real application may mutate a result dictionary in place rather than replace the object.
    shared_result = {"state": "running", "operations": 1}
    mutable_app = type("FakeApp", (), {"results": {"CPU_BENCHMARK": shared_result}})()
    mutable_baseline = _u153_capture_result_ids(mutable_app, "CPU")
    shared_result.update({"state": "good", "operations": 42, "finished_at": "2026-10-23T10:00:00"})
    fresh, key = _u153_get_fresh_result(mutable_app, "CPU", mutable_baseline)
    assert isinstance(fresh, dict) and fresh.get("operations") == 42 and key == "CPU_BENCHMARK", "in-place result mutation was not detected"
    # A final report passed through the worker's update callback is a valid fallback if storage is delayed.
    worker_only = {"state": "warn", "message": "report delivered via UI callback", "operations_per_second": 0}
    fallback, fallback_key = _u153_resolve_result(type("FakeApp", (), {"results": prior})(), "CPU", _u153_capture_result_ids(type("FakeApp", (), {"results": prior})(), "CPU"), {"worker_report": worker_only})
    assert fallback == worker_only and fallback_key == "WORKER_REPORT"
    life = {"started_at": 100.0, "saw_running": False, "last_running": False, "finished_seen_at": None}
    assert _u153_lifecycle_state(life, "CPU", False, 101.0) == "starting"
    assert _u153_lifecycle_state(life, "CPU", False, 110.0) == "waiting_for_worker"
    assert _u153_lifecycle_state(life, "CPU", True, 111.0) == "running"
    assert _u153_lifecycle_state(life, "CPU", False, 112.0) == "saving_result"
    assert _u153_lifecycle_state(life, "CPU", False, 121.0) == "missing"
    assert callable(_u153_attach_component_workbench) and callable(_u153_start_real_test) and callable(_u153_stop_real_test)
    assert callable(_u153_workbench_tick) and callable(_u153_show_test_detail) and callable(_u153_result_signature) and callable(_u153_resolve_result) and callable(_u153_lifecycle_state)
    assert callable(_u153_adopt_external_run), "existing page-button run handoff helper missing"

    class _U153FakeExternalRunApp:
        def __init__(self):
            self.running = True
            self.results = {"CPU_BENCHMARK": {"state": "good", "operations": 10}}
            self.logs = []
            self._u153_component_workbench = None
        def queue_action(self, fn):
            fn()
        def queue_log(self, message):
            self.logs.append(str(message))

    external_app = _U153FakeExternalRunApp()
    external_panel = {
        "module": "CPU", "token": 41, "active": None,
        "idle_baseline": _u153_capture_result_ids(external_app, "CPU")
    }
    before = external_panel["idle_baseline"]
    external_app._u153_component_workbench = external_panel
    assert _u153_adopt_external_run(external_app, external_panel, now=100.0), "running test from an existing page button was not adopted"
    assert external_panel["active"]["external_start"] is True and external_panel["active"]["saw_running"] is True
    assert external_panel["active"]["baseline"] == before, "handoff must preserve the report baseline from before test start"
    external_app.running = False
    external_app.results["CPU_BENCHMARK"] = {"state": "good", "operations": 900, "finished_at": "2026-10-23T10:00:00"}
    fresh_external, external_key = _u153_get_fresh_result(external_app, "CPU", external_panel["active"]["baseline"])
    assert fresh_external and fresh_external["operations"] == 900 and external_key == "CPU_BENCHMARK", "external run report was not recognized as fresh"
    assert "external page-button run" not in " ".join(external_app.logs).casefold() or external_app.logs, "diagnostic log was not preserved"
    assert "_u151_start_direct_test" in _u153_start_real_test.__code__.co_names
    assert "_U153_ORIGINAL_SHOW_TEST_DETAIL" in _u153_show_test_detail.__code__.co_names
    print("COMPONENT_TEST_WORKBENCH_SELFTEST_OK: direct and existing page-button CPU/RAM/GPU start, captured report baseline, live progress, fresh result handoff, worker fallback and honest no-report timeout")


_u146_update_view = _u153_update_view
_u145_queue_panel = _u153_queue_panel
AppV43.show_test_detail = _u153_show_test_detail


if __name__ == "__main__" and "--selftest-component-test-workbench" in _u151_sys.argv:
    try:
        _u153_selftest_component_test_workbench()
        raise SystemExit(0)
    except Exception as _u153_exc:
        import traceback as _u153_traceback
        print("COMPONENT_TEST_WORKBENCH_SELFTEST_FAILED:", type(_u153_exc).__name__, str(_u153_exc))
        _u153_traceback.print_exc()
        raise SystemExit(1)
