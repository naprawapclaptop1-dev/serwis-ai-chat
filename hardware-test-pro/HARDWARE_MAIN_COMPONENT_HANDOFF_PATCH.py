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
    assert _U160_MAIN_COMPONENT_HANDOFF_VERSION == "1.0.0"
    assert _u160_main_module_key("CPU — PROCESOR") == "CPU"
    assert _u160_main_module_key("RAM — PAMIĘĆ") == "RAM"
    assert _u160_main_module_key("GPU — KARTA GRAFICZNA") == "GPU"
    assert _u160_main_module_key("DYSKI — SSD / HDD") == ""
    assert callable(globals().get("_u153_attach_component_workbench")), "component execution workbench helper missing"
    assert callable(AppV43.show_module) and AppV43.show_module is _u160_show_module_with_execution_workbench
    names = set(_u160_show_module_with_execution_workbench.__code__.co_names)
    assert "_U160_ORIGINAL_SHOW_MODULE" in names
    assert "_u153_attach_component_workbench" in names, "main component pages do not attach live result workbench"
    assert "MAIN_MODULE_" in _u160_show_module_with_execution_workbench.__code__.co_consts
    print("MAIN_COMPONENT_HANDOFF_SELFTEST_OK: main CPU/RAM/GPU pages attach live execution, progress and fresh-report panels")


if __name__ == "__main__" and "--selftest-main-component-handoff" in _u160_sys.argv:
    try:
        _u160_selftest_main_component_handoff()
        raise SystemExit(0)
    except Exception as _u160_exc:
        import traceback as _u160_traceback
        print("MAIN_COMPONENT_HANDOFF_SELFTEST_FAILED:", type(_u160_exc).__name__, str(_u160_exc))
        _u160_traceback.print_exc()
        raise SystemExit(1)
