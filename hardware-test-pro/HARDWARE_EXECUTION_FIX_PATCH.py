# Final UI execution fixes for main RAM report refresh and OpenGL camera framing.
import time as _u148_time
import inspect as _u148_inspect
import tkinter as _u148_tk

_U148_HARDWARE_EXECUTION_PATCH_VERSION = "1.0.0"
_U148_ORIGINAL_UPDATE_VIEW = _u146_update_view
_U148_ORIGINAL_RAM_TEST = AppV43._ram_test


def _u148_refresh_main_ram(app, force=False, message=None):
    if str(getattr(app, "current_view", "")) != "RAM":
        return False
    try:
        now = _u148_time.monotonic()
        previous = float(getattr(app, "_u148_ram_refresh_at", 0.0) or 0.0)
        if not force and now - previous < 0.40:
            return False
        app._u148_ram_refresh_at = now
    except Exception:
        pass

    def apply():
        if str(getattr(app, "current_view", "")) != "RAM":
            return
        refresh = getattr(app, "_update_ram_module_live", None)
        if callable(refresh):
            try:
                refresh()
            except Exception as exc:
                try:
                    app.append_log("RAM: odświeżenie głównego raportu: " + repr(exc))
                except Exception:
                    pass

        results = getattr(app, "results", {}) or {}
        bench = results.get("RAM_BENCHMARK") if isinstance(results, dict) else None
        ram = results.get("RAM") if isinstance(results, dict) else None
        record = bench if isinstance(bench, dict) else {}
        if not record and isinstance(ram, dict):
            record = ram.get("benchmark") if isinstance(ram.get("benchmark"), dict) else ram
        state = str(record.get("state") or (ram or {}).get("state") or "N/D").upper()
        detail = str(message or record.get("message") or (ram or {}).get("message") or "Test RAM nie zwrócił wyniku.")
        if bool(getattr(app, "running", False)) and message:
            status_text = "RAM — TEST W TOKU • " + str(message)
        else:
            tested = record.get("size_mb", record.get("tested_mb", (ram or {}).get("size_mb", "N/D")))
            status_text = f"RAM — {state} • {tested} MB • {detail}"

        theme = {}
        try:
            theme = app.colors()
        except Exception:
            pass
        colour = theme.get("good", "#26cf88") if state in ("GOOD", "PASS") else (
            theme.get("bad", "#ff5d68") if state in ("BAD", "ERROR", "FAIL") else theme.get("warn", "#ffbd45")
        )
        for attr in ("_module_status_label", "_simple_status_label", "_ram_status_label", "_ram_test_status_label"):
            widget = getattr(app, attr, None)
            try:
                if widget is not None and widget.winfo_exists():
                    widget.configure(text=status_text, fg=colour)
            except Exception:
                pass

        # Replace only known stale placeholders in the visible RAM page.
        root = getattr(app, "content", None)
        stack = [root] if root is not None else []
        while stack:
            widget = stack.pop()
            try:
                stack.extend(list(widget.winfo_children()))
            except Exception:
                pass
            try:
                if isinstance(widget, _u148_tk.Label) and widget.winfo_exists():
                    old_text = str(widget.cget("text") or "")
                    lower = old_text.casefold()
                    stale = (
                        "test nie został jeszcze uruchomiony" in lower
                        or "test nie zostal jeszcze uruchomiony" in lower
                        or ("wybierz" in lower and "pełny test ram" in lower)
                        or ("wybierz" in lower and "pelny test ram" in lower)
                    )
                    if stale:
                        widget.configure(text=status_text, fg=colour)
            except Exception:
                pass
            try:
                if isinstance(widget, _u148_tk.Text) and widget.winfo_exists():
                    old_text = str(widget.get("1.0", "end-1c") or "")
                    lower = old_text.casefold()
                    stale = (
                        "test nie został jeszcze uruchomiony" in lower
                        or "test nie zostal jeszcze uruchomiony" in lower
                    )
                    if stale:
                        try:
                            widget.configure(state="normal")
                            widget.delete("1.0", "end")
                            widget.insert("1.0", status_text + "\n\n" + _u146_json.dumps(record, ensure_ascii=False, indent=2, default=str))
                            widget.configure(state="disabled")
                        except Exception:
                            pass
            except Exception:
                pass

    try:
        queue = getattr(app, "queue_action", None)
        if callable(queue):
            queue(apply)
        else:
            apply()
        return True
    except Exception as exc:
        try:
            app.append_log("RAM: kolejka synchronizacji UI: " + repr(exc))
        except Exception:
            pass
        return False


def _u148_update_view(app, module, percent, message, report=None):
    result = _U148_ORIGINAL_UPDATE_VIEW(app, module, percent, message, report)
    if str(module).upper() == "RAM":
        _u148_refresh_main_ram(app, force=(int(percent) >= 100 or report is not None), message=message)
    return result


_u146_update_view = _u148_update_view


def _u148_ram_test_with_final_refresh(app, mb=512):
    try:
        return _U148_ORIGINAL_RAM_TEST(app, mb)
    finally:
        # Ensure the main RAM screen reads the same result as the live benchmark panel.
        _u148_refresh_main_ram(app, force=True)


_u148_ram_test_with_final_refresh._u102_ram_guard = True
_u148_ram_test_with_final_refresh._u80_sound_wrapped = bool(getattr(_U148_ORIGINAL_RAM_TEST, "_u80_sound_wrapped", False))
AppV43._ram_test = _u148_ram_test_with_final_refresh


def _u148_selftest_hardware_execution():
    assert _U148_HARDWARE_EXECUTION_PATCH_VERSION == "1.0.0"
    assert callable(_u148_refresh_main_ram) and callable(_u148_update_view)
    assert callable(AppV43._ram_test) and getattr(AppV43._ram_test, "_u102_ram_guard", False)
    assert "_set_stage" not in _u147_cpu_test.__code__.co_names
    assert "_u147_safe_stage_update" in _u147_cpu_test.__code__.co_names

    class _U148FakeApp:
        def __init__(self):
            self.current_view = "RAM"
            self.results = {"RAM_BENCHMARK": {"state": "good", "size_mb": 128, "message": "test zaliczony"}}
            self.refresh_calls = 0
            self.queue_log_messages = []
        def queue_action(self, callback):
            callback()
        def _update_ram_module_live(self):
            self.refresh_calls += 1
        def append_log(self, message):
            self.queue_log_messages.append(str(message))
        def colors(self):
            return {"good": "#00aa00", "warn": "#ffaa00", "bad": "#aa0000"}

    fake = _U148FakeApp()
    assert _u148_refresh_main_ram(fake, force=True, message="Próbka RAM • 50%")
    assert fake.refresh_calls == 1, "main RAM page updater was not called"
    fake.current_view = "GPU"
    assert not _u148_refresh_main_ram(fake, force=True), "RAM page updater must not run on another view"

    renderer_source = _u148_inspect.getsource(_u114_gpu_benchmark_child)
    camera = "GL.glTranslatef(0.0,0.0,-7.0)"
    assert camera in renderer_source, "OpenGL renderer still has no camera distance; scene will remain clipped/small"
    assert "GL.glLoadIdentity();GL.glTranslatef(0.0,0.0,-7.0)" in renderer_source, "camera distance must follow modelview reset"
    assert callable(_u147_execute_gpu_scene)
    print("HARDWARE_EXECUTION_FIX_SELFTEST_OK: main RAM report sync, safe CPU stage callback and visible GPU camera framing")


if __name__ == "__main__" and "--selftest-hardware-execution" in _u145_sys.argv:
    try:
        _u148_selftest_hardware_execution()
        raise SystemExit(0)
    except Exception as _u148_exc:
        import traceback as _u148_traceback
        print("HARDWARE_EXECUTION_FIX_SELFTEST_FAILED:", type(_u148_exc).__name__, str(_u148_exc))
        _u148_traceback.print_exc()
        raise SystemExit(1)
