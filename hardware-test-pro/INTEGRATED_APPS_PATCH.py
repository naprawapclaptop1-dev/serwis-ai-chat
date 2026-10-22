import os as _u144_os
import sys as _u144_sys
import json as _u144_json
import hashlib as _u144_hashlib
import re as _u144_re
from pathlib import Path as _u144_Path
import tkinter as _u144_tk
from tkinter import ttk as _u144_ttk, messagebox as _u144_messagebox

_U144_INTEGRATED_APPS_VERSION = "1.0.0"
_U144_COMPANION_VERSION = "5.6.16"
_U144_COMPANION_RELATIVE = ("Companions", "SystemRepairPRO", "NAPRAWA-PC-SYSTEM-REPAIR-PRO.exe")
_U144_COMPANION_MANIFEST = "companion-manifest.json"

def _u144_app_root():
    return _u144_Path(_u144_sys.executable).resolve().parent if getattr(_u144_sys, "frozen", False) else _u144_Path(__file__).resolve().parent

def _u144_companion_path(base_dir=None):
    root = _u144_Path(base_dir).resolve() if base_dir is not None else _u144_app_root()
    return root.joinpath(*_U144_COMPANION_RELATIVE)

def _u144_companion_manifest(path=None):
    exe = _u144_Path(path) if path is not None else _u144_companion_path()
    manifest_path = exe.parent / _U144_COMPANION_MANIFEST
    if not exe.is_file() or not manifest_path.is_file():
        return None
    try:
        data = _u144_json.loads(manifest_path.read_text(encoding="utf-8-sig"))
        if not isinstance(data, dict) or data.get("app") != "NAPRAWA PC SYSTEM REPAIR PRO":
            return None
        if data.get("exe") != exe.name or str(data.get("version", "")) != _U144_COMPANION_VERSION:
            return None
        if not _u144_re.fullmatch(r"[0-9a-fA-F]{64}", str(data.get("sha256", ""))):
            return None
        size = int(data.get("size_bytes", 0))
        if size <= 32_768 or size != exe.stat().st_size:
            return None
        # A WPF self-contained publish can use a small native apphost plus a managed DLL and runtime files.
        prefix = "NAPRAWA-PC-SYSTEM-REPAIR-PRO"
        required = (
            exe.parent / (prefix + ".dll"),
            exe.parent / (prefix + ".runtimeconfig.json"),
            exe.parent / (prefix + ".deps.json"),
        )
        if not all(item.is_file() for item in required):
            return None
        return data
    except Exception:
        return None

def _u144_companion_status():
    exe = _u144_companion_path()
    data = _u144_companion_manifest(exe)
    if not data:
        return False, "PEŁNY SYSTEM REPAIR PRO 5.6.16 NIE JEST ZAINSTALOWANY LUB NIE PRZESZEDŁ KONTROLI"
    return True, f"System Repair PRO {data['version']} • dołączony • {exe.stat().st_size/1048576:.1f} MB • SHA-256 OK"

def _u144_launch_system_repair(app=None):
    exe = _u144_companion_path()
    data = _u144_companion_manifest(exe)
    if data is None:
        _u144_messagebox.showerror("System Repair PRO", "Nie znaleziono pełnego programu 5.6.16 albo plik nie zgadza się z manifestem. Uruchom ponownie instalator aktualizacji.")
        return False
    if _u144_os.name != "nt":
        _u144_messagebox.showerror("System Repair PRO", "Pełny program WPF jest dostępny tylko w Windows x64.")
        return False
    try:
        digest = _u144_hashlib.sha256()
        with exe.open("rb") as stream:
            for block in iter(lambda: stream.read(1048576), b""):
                digest.update(block)
        if digest.hexdigest().lower() != str(data["sha256"]).lower():
            raise RuntimeError("Suma SHA-256 nie zgadza się z companion-manifest.json.")
        import ctypes as _u144_ctypes
        shell_execute = _u144_ctypes.windll.shell32.ShellExecuteW
        shell_execute.argtypes = [_u144_ctypes.c_void_p, _u144_ctypes.c_wchar_p, _u144_ctypes.c_wchar_p, _u144_ctypes.c_wchar_p, _u144_ctypes.c_wchar_p, _u144_ctypes.c_int]
        shell_execute.restype = _u144_ctypes.c_void_p
        code = int(shell_execute(None, "open", str(exe), None, str(exe.parent), 1) or 0)
        if code <= 32:
            raise OSError(f"ShellExecuteW zwrócił kod {code}.")
        try:
            if app is not None:
                app.append_log("System Repair PRO 5.6.16: uruchomiono pełny program; SHA-256 sprawdzony.")
        except Exception:
            pass
        return True
    except Exception as exc:
        _u144_messagebox.showerror("System Repair PRO", f"Nie udało się uruchomić pełnego programu:\n{type(exc).__name__}: {exc}")
        return False

def _u144_route_category(title):
    value = str(title).upper()
    if any(x in value for x in ("SYSTEM REPAIR", "CENTRUM NAPRAW", "PROFILE NAPRAW", "BAZA WIEDZY", "AUDYT WINDOWS")):
        return "SYSTEM REPAIR PRO"
    if any(x in value for x in ("SERWIS", "ZLECENIA", "ZASILANIE", "BATERIA", "MENEDŻER PROCESÓW", "DIAGNOSTYKA GIER", "RAPORTY")):
        return "SERWIS ULTIMATE"
    return "HARDWARE TEST PRO"

def _u144_integrated_suite_routes(app):
    installed, status = _u144_companion_status()
    routes = [{
        "category":"SYSTEM REPAIR PRO", "title":"PEŁNY SYSTEM REPAIR PRO 5.6.16",
        "description":"Pełna aplikacja WPF dołączona do wspólnego instalatora. Przed uruchomieniem sprawdzana jest suma SHA-256; Windows może pokazać UAC. " + status,
        "action":lambda:_u144_launch_system_repair(app), "companion":True
    }]
    for title, description, action in _u132_service_dashboard_routes(app):
        routes.append({"category":_u144_route_category(title),"title":str(title),"description":str(description),"action":action,"companion":False})
    return routes

def _u144_show_integrated_apps_hub(app):
    app.current_view = "INTEGRATED_APPS_HUB"
    app.clear()
    t = app.colors()
    app.header_title.config(text="ZINTEGROWANA SUITA — HARDWARE TEST PRO • SYSTEM REPAIR PRO • SERWIS ULTIMATE")
    intro = app.panel(app.content)
    intro.pack(fill="x", padx=8, pady=(6,5))
    _u144_tk.Label(intro,text="JEDNO CENTRUM • WSZYSTKIE DOSTĘPNE MODUŁY",bg=t["panel"],fg=t["accent"],font=app.fnt(13,"bold")).pack(anchor="w",padx=12,pady=(9,3))
    _u144_tk.Label(intro,text="110 testów sprzętowych, diagnostyka Windows, profile napraw, baza wiedzy, zlecenia, zasilanie, procesy, gry, raporty i pełny System Repair PRO dostępne z jednego miejsca. Moduły Serwis Ultimate działają wewnątrz Hardware Test PRO. Pełny program WPF otwiera własne okno, a brak czujnika pozostaje N/D.",bg=t["panel"],fg=t["muted"],font=app.fnt(9),wraplength=1500,justify="left").pack(anchor="w",padx=12,pady=(0,7))
    installed,status = _u144_companion_status()
    _u144_tk.Label(intro,text=status,bg=t["panel"],fg=t["good"] if installed else t["warn"],font=app.fnt(9,"bold"),wraplength=1500,justify="left").pack(anchor="w",padx=12,pady=(0,8))
    tools = _u144_tk.Frame(app.content,bg=t["bg"]);tools.pack(fill="x",padx=8,pady=(0,6))
    app.make_button(tools,"URUCHOM PEŁNY SYSTEM REPAIR PRO 5.6.16",lambda:_u144_launch_system_repair(app),"accent",side="left",ipady=6)
    app.make_button(tools,"CENTRUM NAPRAW WINDOWS",lambda:app.show_system_repair_center(),"card",side="left",ipady=6)
    app.make_button(tools,"PULPIT HARDWARE TEST PRO",lambda:app.show_dashboard(),"card",side="left",ipady=6)
    search_row=_u144_tk.Frame(app.content,bg=t["bg"]);search_row.pack(fill="x",padx=8,pady=(0,6))
    _u144_tk.Label(search_row,text="SZUKAJ MODUŁU",bg=t["bg"],fg=t["accent"],font=app.fnt(9,"bold")).pack(anchor="w",pady=(0,3))
    filter_value=_u144_tk.StringVar(master=app,value="")
    _u144_tk.Entry(search_row,textvariable=filter_value,bg=t["card"],fg=t["fg"],insertbackground=t["fg"],relief="flat",font=app.fnt(10)).pack(fill="x",ipady=5)
    body=_u144_tk.Frame(app.content,bg=t["bg"]);body.pack(fill="both",expand=True,padx=8,pady=(0,5))
    canvas=_u144_tk.Canvas(body,bg=t["bg"],highlightthickness=0,bd=0)
    scroll=_u144_ttk.Scrollbar(body,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=scroll.set);canvas.pack(side="left",fill="both",expand=True);scroll.pack(side="right",fill="y")
    inner=_u144_tk.Frame(canvas,bg=t["bg"]);window_id=canvas.create_window((0,0),window=inner,anchor="nw")
    inner.bind("<Configure>",lambda event:canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>",lambda event:canvas.itemconfigure(window_id,width=event.width))
    canvas.bind("<MouseWheel>",lambda event:(canvas.yview_scroll(-1*int(event.delta/120 or (1 if event.delta<0 else -1)),"units"),"break")[1])
    routes=_u144_integrated_suite_routes(app)
    for col in range(3):inner.grid_columnconfigure(col,weight=1,uniform="suite")
    def render_cards(*_args):
        for child in inner.winfo_children(): child.destroy()
        query=str(filter_value.get() or "").strip().casefold()
        visible=[route for route in routes if not query or query in " ".join((route["category"],route["title"],route["description"])).casefold()]
        if not visible:
            _u144_tk.Label(inner,text="Nie znaleziono modułu pasującego do wyszukiwania.",bg=t["bg"],fg=t["muted"],font=app.fnt(10)).grid(row=0,column=0,columnspan=3,sticky="ew",padx=8,pady=20)
        for index,route in enumerate(visible):
            row,col=divmod(index,3)
            card=_u144_tk.Frame(inner,bg=t["card"],highlightbackground=t["panel"],highlightthickness=1)
            card.grid(row=row,column=col,sticky="nsew",padx=4,pady=4)
            _u144_tk.Label(card,text=route["category"],bg=t["card"],fg=t["good"] if route["companion"] and installed else t["accent"],font=app.fnt(8,"bold"),anchor="w").pack(fill="x",padx=9,pady=(8,2))
            _u144_tk.Label(card,text=route["title"],bg=t["card"],fg=t["accent2"],font=app.fnt(10,"bold"),anchor="w",justify="left",wraplength=330).pack(fill="x",padx=9,pady=(0,4))
            _u144_tk.Label(card,text=route["description"],bg=t["card"],fg=t["muted"],font=app.fnt(8),anchor="nw",justify="left",wraplength=330).pack(fill="both",expand=True,padx=9,pady=(0,7))
            app.make_button(card,"URUCHOM PEŁNY PROGRAM" if route["companion"] else "OTWÓRZ MODUŁ",route["action"],"accent" if route["companion"] else "card",fill="x",ipady=4)
        inner.update_idletasks();canvas.configure(scrollregion=canvas.bbox("all"))
    filter_value.trace_add("write",render_cards);render_cards()
    footer=_u144_tk.Frame(app.content,bg=t["bg"]);footer.pack(side="bottom",fill="x",padx=8,pady=(2,7))
    app.make_button(footer,"← PULPIT",app.show_dashboard,"card",side="left",ipady=5)
    app.make_button(footer,"← CENTRUM SERWISU",app.show_service_ultimate_dashboard,"card",side="left",ipady=5)

AppV43.show_integrated_apps_hub = _u144_show_integrated_apps_hub

def _u144_selftest_integrated_apps():
    assert _U144_INTEGRATED_APPS_VERSION == "1.0.0"
    assert callable(AppV43.show_integrated_apps_hub) and callable(_u144_launch_system_repair)
    routes=_u144_integrated_suite_routes(object())
    assert len(routes)==20, "expected 19 internal routes plus full System Repair PRO companion"
    titles=[item["title"] for item in routes]
    assert len(titles)==len(set(titles)) and all(callable(item["action"]) for item in routes)
    assert routes[0]["title"]=="PEŁNY SYSTEM REPAIR PRO 5.6.16" and routes[0]["companion"]
    assert {"HARDWARE TEST PRO","SYSTEM REPAIR PRO","SERWIS ULTIMATE"}.issubset({item["category"] for item in routes})
    assert _u144_companion_path("C:/NaprawaPC-Test").parts[-3:]==("Companions","SystemRepairPRO","NAPRAWA-PC-SYSTEM-REPAIR-PRO.exe")
    assert "ShellExecuteW" in _u144_launch_system_repair.__code__.co_names and "_u144_hashlib" in _u144_launch_system_repair.__code__.co_names
    print("INTEGRATED_APPS_SELFTEST_OK: searchable hub, 19 internal module routes, full WPF companion and SHA-256/UAC launcher")

if __name__ == "__main__" and "--selftest-integrated-apps" in _u144_sys.argv:
    try:
        _u144_selftest_integrated_apps()
        raise SystemExit(0)
    except Exception as _u144_exc:
        import traceback as _u144_traceback
        print("INTEGRATED_APPS_SELFTEST_FAILED:",type(_u144_exc).__name__,str(_u144_exc))
        _u144_traceback.print_exc()
        raise SystemExit(1)
