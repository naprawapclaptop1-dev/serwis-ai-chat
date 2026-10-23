# v4.3.160 — attach the actual-result workbench to the main CPU/RAM/GPU module pages too.
import sys as _u160_sys

_U160_MAIN_COMPONENT_HANDOFF_VERSION = "1.0.0"
_U160_ORIGINAL_SHOW_MODULE = AppV43.show_module


def _u160_main_module_key(value):
    try:
        key = _u153_module(value)
        if key in ("CPU", "RAM", "GPU"):
            return key
    except Exception:
        pass
    text = str(value or "").upper()
    if "CPU" in text or "PROCESOR" in text:
        return "CPU"
    if "RAM" in text or "PAMI" in text or "MEMORY" in text:
        return "RAM"
    if "GPU" in text or "GRAFICZN" in text or "VRAM" in text:
        return "GPU"
    return ""


def _u160_show_module_with_execution_workbench(app, module):
    result = _U160_ORIGINAL_SHOW_MODULE(app, module)
    key = _u160_main_module_key(module)
    if key in ("CPU", "RAM", "GPU"):
        attach = globals().get("_u153_attach_component_workbench")
        if callable(attach):
            attach(app, key, "MAIN_MODULE_" + key, "main_module")
    return result


AppV43.show_module = _u160_show_module_with_execution_workbench


def _u160_selftest_main_component_handoff():
    global _U160_ORIGINAL_SHOW_MODULE
    assert _U160_MAIN_COMPONENT_HANDOFF_VERSION == "1.0.0"
    assert _u160_main_module_key("CPU — PROCESOR") == "CPU"
    assert _u160_main_module_key("RAM — PAMIĘĆ") == "RAM"
    assert _u160_main_module_key("GPU — KARTA GRAFICZNA") == "GPU"
    assert _u160_main_module_key("DYSKI — SSD / HDD") == ""
    assert callable(globals().get("_u153_attach_component_workbench")), "component execution workbench helper missing"
    assert callable(AppV43.show_module) and AppV43.show_module is _u160_show_module_with_execution_workbench
    names = set(_u160_show_module_with_execution_workbench.__code__.co_names)
    constants = set(_u160_show_module_with_execution_workbench.__code__.co_consts)
    assert "_U160_ORIGINAL_SHOW_MODULE" in names
    # The helper is intentionally looked up by string through globals(); its symbol
    # belongs to co_consts, not co_names. Test the call behavior as well as its wiring.
    assert "_u153_attach_component_workbench" in constants, "main component pages do not reference the live workbench helper"
    assert "MAIN_MODULE_" in constants

    original_show = _U160_ORIGINAL_SHOW_MODULE
    original_attach = globals().get("_u153_attach_component_workbench")
    calls = []
    class _U160FakeApp:
        pass
    def _u160_fake_show(app, module):
        return ("original-view", module)
    def _u160_fake_attach(app, module, test_id="", kind=""):
        calls.append((module, test_id, kind))
        return True
    try:
        _U160_ORIGINAL_SHOW_MODULE = _u160_fake_show
        globals()["_u153_attach_component_workbench"] = _u160_fake_attach
        fake = _U160FakeApp()
        for module in ("CPU", "RAM", "GPU"):
            result = _u160_show_module_with_execution_workbench(fake, module)
            assert result == ("original-view", module), "original main view was not preserved for " + module
        assert calls == [
            ("CPU", "MAIN_MODULE_CPU", "main_module"),
            ("RAM", "MAIN_MODULE_RAM", "main_module"),
            ("GPU", "MAIN_MODULE_GPU", "main_module"),
        ], "opening main CPU/RAM/GPU pages must attach exactly one workbench per module"
        calls.clear()
        _u160_show_module_with_execution_workbench(fake, "DYSKI")
        assert not calls, "non-CPU/RAM/GPU views must not receive the component workbench"
    finally:
        _U160_ORIGINAL_SHOW_MODULE = original_show
        if original_attach is None:
            globals().pop("_u153_attach_component_workbench", None)
        else:
            globals()["_u153_attach_component_workbench"] = original_attach
    print("MAIN_COMPONENT_HANDOFF_SELFTEST_OK: actual CPU/RAM/GPU page calls attach live execution workbench; other modules unchanged")


if __name__ == "__main__" and "--selftest-main-component-handoff" in _u160_sys.argv:
    try:
        _u160_selftest_main_component_handoff()
        raise SystemExit(0)
    except Exception as _u160_exc:
        import traceback as _u160_traceback
        print("MAIN_COMPONENT_HANDOFF_SELFTEST_FAILED:", type(_u160_exc).__name__, str(_u160_exc))
        _u160_traceback.print_exc()
        raise SystemExit(1)
