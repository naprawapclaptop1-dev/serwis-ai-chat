# v4.3.163 — evidence-based CPU/RAM/GPU diagnosis and same-test regression comparison.
import os as _u163_os, sys as _u163_sys, json as _u163_json, html as _u163_html, math as _u163_math
import datetime as _u163_datetime, webbrowser as _u163_webbrowser
from pathlib import Path as _u163_Path
import tkinter as _u163_tk
from tkinter import ttk as _u163_ttk, messagebox as _u163_messagebox

_U163_BENCHMARK_DIAGNOSIS_VERSION = "1.0.0"
_U163_ORIGINAL_ATTACH_CONSOLE = _u151_attach_console

def _u163_num(value):
    if value is None or isinstance(value, bool): return None
    try:
        number = float(value)
        return number if _u163_math.isfinite(number) else None
    except Exception: return None

def _u163_pick(report, keys):
    if not isinstance(report, dict): return None
    for key in keys:
        value = _u163_num(report.get(key))
        if value is not None: return value
    return None

def _u163_module(value):
    text = str(value or "").strip().upper()
    if "CPU" in text or "PROCESOR" in text: return "CPU"
    if "RAM" in text or "PAMI" in text or "MEMORY" in text: return "RAM"
    if "GPU" in text or "GRAFICZ" in text or "VRAM" in text or "3D" in text: return "GPU"
    return ""

def _u163_test_id(report, fallback=""):
    if isinstance(report, dict):
        value = report.get("test_id") or report.get("test") or report.get("test_key")
        if value: return str(value)
    return str(fallback or "N/D")

def _u163_hardware_identity(report):
    hardware = report.get("hardware") if isinstance(report, dict) else {}
    if not isinstance(hardware, dict): hardware = {}
    computer = str(hardware.get("computer_name") or report.get("computer_name") or "").strip().casefold()
    platform = str(hardware.get("platform") or "").strip().casefold()
    if not computer or not platform: return None
    return {"computer_name":computer,"platform":platform,
            "cpu_logical_processors":_u163_num(hardware.get("cpu_logical_processors")),
            "cpu_physical_cores":_u163_num(hardware.get("cpu_physical_cores")),
            "ram_total_mb":_u163_num(hardware.get("ram_total_mb"))}

def _u163_settings(report):
    settings = report.get("test_settings") if isinstance(report, dict) else {}
    return settings if isinstance(settings, dict) else {}

def _u163_comparability(newer, older):
    if not isinstance(newer, dict) or not isinstance(older, dict): return False, "Brak pełnego raportu."
    module = _u163_module(newer.get("module"))
    if not module or module != _u163_module(older.get("module")): return False, "Inny moduł sprzętowy."
    new_id, old_id = _u163_test_id(newer), _u163_test_id(older)
    if new_id == "N/D" or new_id != old_id: return False, "Inny identyfikator testu."
    hn, ho = _u163_hardware_identity(newer), _u163_hardware_identity(older)
    if hn is None or ho is None: return False, "Brakuje identyfikacji komputera lub platformy."
    for key in ("computer_name", "platform"):
        if hn[key] != ho[key]: return False, "Inny komputer lub system."
    for key in ("cpu_logical_processors", "cpu_physical_cores", "ram_total_mb"):
        if hn[key] is not None and ho[key] is not None and hn[key] != ho[key]:
            return False, "Zmieniła się konfiguracja sprzętu: " + key + "."
    sn, so = _u163_settings(newer), _u163_settings(older)
    keys = {"CPU":("cpu_mode","algorithm","duration","workers"),
            "RAM":("memory_mb","buffer_mb","patterns","duration","test"),
            "GPU":("scene_id","duration_seconds","resolution","resolution_requested")}[module]
    for key in keys:
        a, b = sn.get(key), so.get(key)
        if a is not None and b is not None and str(a) != str(b): return False, "Inne ustawienie testu: " + key + "."
        if key in ("cpu_mode","algorithm","memory_mb","buffer_mb","scene_id") and (a is None) != (b is None):
            return False, "Nie da się potwierdzić ustawienia: " + key + "."
    if module == "CPU":
        nw, ow = _u163_pick(newer, ("workers",)), _u163_pick(older, ("workers",))
        if nw is not None and ow is not None and nw != ow: return False, "Inna liczba wątków CPU."
    if module == "RAM":
        ns = _u163_pick(newer, ("tested_mb","size_mb","buffer_mb"))
        osize = _u163_pick(older, ("tested_mb","size_mb","buffer_mb"))
        if ns is None or osize is None or ns != osize: return False, "Rzeczywiście sprawdzony bufor RAM różni się lub jest nieznany."
    if module == "GPU":
        ns, osize = _u163_pick(newer, ("scene_id",)), _u163_pick(older, ("scene_id",))
        if ns is None or osize is None or ns != osize: return False, "Nie potwierdzono tej samej sceny GPU."
        nr = str(newer.get("renderer") or "").strip().casefold()
        oldr = str(older.get("renderer") or "").strip().casefold()
        if not nr or not oldr or nr != oldr: return False, "Renderer OpenGL zmienił się lub jest nieznany."
        nres = str(newer.get("resolution_rendered") or newer.get("resolution") or "").strip()
        ores = str(older.get("resolution_rendered") or older.get("resolution") or "").strip()
        if not nres or not ores or nres != ores: return False, "Rozdzielczość renderowania różni się lub jest nieznana."
    return True, "Ten sam komputer, test i potwierdzone ustawienia."

def _u163_evidence(module, report):
    item = report if isinstance(report, dict) else {}
    if module == "CPU":
        operations = _u163_pick(item, ("operations","operations_completed"))
        rate = _u163_pick(item, ("operations_per_second",))
        valid = operations is not None and operations > 0 and rate is not None and rate > 0
        return valid, {"SHA-256 operacje":operations,"SHA-256/s":rate,
            "Przepustowość MiB/s":_u163_pick(item,("throughput_mib_s",)),
            "Wątki":_u163_pick(item,("workers","logical_processors")),
            "Temperatura szczytowa °C":_u163_pick(item,("cpu_temp_peak_c",))}
    if module == "RAM":
        verified = _u163_pick(item,("bytes_verified",))
        tested = _u163_pick(item,("tested_mb","size_mb","buffer_mb"))
        patterns = _u163_pick(item,("patterns_completed",))
        valid = verified is not None and verified > 0 and tested is not None and tested > 0 and (patterns is None or patterns > 0)
        return valid, {"Sprawdzony bufor MB":tested,"Zweryfikowane bajty":verified,
            "Wzorce ukończone":patterns,"Wzorce łącznie":_u163_pick(item,("patterns_total",)),
            "Zapis MiB/s":_u163_pick(item,("write_MiBps","write_mib_s_overall")),
            "Weryfikacja MiB/s":_u163_pick(item,("verify_MiBps","verify_mib_s_overall"))}
    if module == "GPU":
        frames = _u163_pick(item,("frames",)); fps = _u163_pick(item,("average_fps","mean_fps"))
        renderer = str(item.get("renderer") or "").strip()
        return frames is not None and frames > 0 and fps is not None and fps > 0 and bool(renderer), {
            "Scena":_u163_pick(item,("scene_id",)),"Średni FPS":fps,
            "Szczyt FPS":_u163_pick(item,("peak_fps_1s","peak_fps")),"Klatki":frames,
            "Renderer":renderer or "N/D","Rozdzielczość":str(item.get("resolution_rendered") or item.get("resolution") or "N/D"),
            "Temperatura GPU °C":_u163_pick(item,("gpu_temp_peak_c","temperature_c"))}
    return False, {}

def _u163_metric_deltas(newer, older):
    module = _u163_module(newer.get("module"))
    defs = {"CPU":(("SHA-256/s",("operations_per_second",)),),
            "RAM":(("Zapis RAM MiB/s",("write_MiBps","write_mib_s_overall")),
                   ("Weryfikacja RAM MiB/s",("verify_MiBps","verify_mib_s_overall"))),
            "GPU":(("Średni FPS",("average_fps","mean_fps")),)}.get(module,())
    rows=[]
    for label,keys in defs:
        old=_u163_pick(older,keys); new=_u163_pick(newer,keys)
        if old is None or new is None: continue
        if old <= 0:
            rows.append({"metric":label,"older":old,"newer":new,"delta":new-old,"percent":None,
                         "classification":"NO_BASELINE","message":"Wartość bazowa nie jest większa od zera; nie można obliczyć procentowej zmiany."})
            continue
        delta=new-old; percent=100.0*delta/abs(old)
        if percent <= -15.0: kind,msg="REGRESSION",f"Spadek o {abs(percent):.1f}% względem poprzedniego, porównywalnego testu."
        elif percent >= 15.0: kind,msg="IMPROVEMENT",f"Wzrost o {percent:.1f}% względem poprzedniego, porównywalnego testu."
        else: kind,msg="STABLE",f"Zmiana {percent:+.1f}%; mieści się w pasmie ±15% i nie przesądza o stanie sprzętu."
        rows.append({"metric":label,"older":old,"newer":new,"delta":delta,"percent":percent,"classification":kind,"message":msg})
    return rows

def _u163_find_baseline(module,current,history_entries=None):
    if history_entries is None:
        reader=globals().get("_u149_read_history")
        try: history_entries=reader(limit=500) if callable(reader) else []
        except Exception: history_entries=[]
    current_path=str(current.get("report_path") or "")
    current_time=str(current.get("finished_at") or current.get("created_at") or "")
    candidates=[]
    for entry in history_entries or []:
        if not isinstance(entry,dict): continue
        payload=entry.get("payload")
        if not isinstance(payload,dict): continue
        if current_path and str(entry.get("path") or "") == current_path: continue
        if _u163_module(entry.get("module") or payload.get("module")) != module: continue
        if _u163_test_id(payload) != _u163_test_id(current): continue
        created=str(entry.get("created_at") or payload.get("finished_at") or payload.get("created_at") or "")
        if current_time and created and created >= current_time: continue
        if not _u163_evidence(module,payload)[0]: continue
        ok,reason=_u163_comparability(current,payload)
        if ok: candidates.append((created,str(entry.get("path") or ""),payload,reason))
    if not candidates: return None
    candidates.sort(key=lambda row:(row[0],row[1]),reverse=True)
    created,path,payload,reason=candidates[0]
    return {"created_at":created,"path":path,"payload":payload,"reason":reason}

def _u163_analyze_report(module,report,test_id="",history_entries=None):
    canonical=_u163_module(module) or "N/D"
    current=dict(report) if isinstance(report,dict) else {}
    if test_id and not current.get("test_id"): current["test_id"]=str(test_id)
    current.setdefault("module",canonical)
    if not isinstance(current.get("hardware"),dict):
        hwfn=globals().get("_u149_hardware")
        if callable(hwfn):
            try: current["hardware"]=hwfn()
            except Exception: pass
    name=_u163_test_id(current,test_id)
    valid,metrics=_u163_evidence(canonical,current)
    raw=str(current.get("state") or "N/D").strip().upper()
    findings=[]
    if not current:
        state="WARN"
        findings.append({"severity":"WARN","check":"Świeży raport","detail":"Nie znaleziono raportu z ukończonego testu "+canonical+".",
            "action":"Uruchom test CPU SHA-256, RAM z weryfikacją lub scenę GPU OpenGL. Podgląd 3D nie jest wynikiem testu."})
    else:
        if raw in ("BAD","FAIL","FAILED","ERROR"):
            state="FAIL"
            findings.append({"severity":"FAIL","check":"Stan testu","detail":"Silnik zapisał status "+raw+".",
                "action":str(current.get("error") or current.get("message") or "Otwórz raport źródłowy i dziennik testu.")})
        elif not valid:
            state="WARN"
            findings.append({"severity":"WARN","check":"Dowód pomiarowy","detail":"Raport nie zawiera wymaganych rzeczywistych metryk dla testu "+canonical+".",
                "action":"Sprawdź błąd silnika, sterownik lub log. Brak metryk nie jest wynikiem PASS."})
        elif raw not in ("GOOD","PASS","OK","COMPLETED","SUCCESS"):
            state="WARN"
            findings.append({"severity":"WARN","check":"Stan testu","detail":"Pomiar ma dane, ale silnik nie potwierdził poprawnego ukończenia ("+raw+").",
                "action":str(current.get("message") or current.get("note") or "Przejrzyj raport przed wyciąganiem wniosków.")})
        else:
            state="PASS"
            findings.append({"severity":"PASS","check":"Wymagane metryki","detail":"Raport zawiera mierzalny dowód wykonania testu "+canonical+".",
                "action":"To potwierdza wykonanie tego pomiaru, nie gwarantuje pełnej sprawności każdego elementu."})
        if canonical=="RAM":
            mismatch=_u163_pick(current,("mismatch_count","mismatches","error_count","errors_found"))
            if mismatch is not None and mismatch>0:
                state="FAIL"
                findings.append({"severity":"FAIL","check":"Niezgodności RAM","detail":f"Raport wskazuje {int(mismatch)} niezgodności zapisu/weryfikacji.",
                    "action":"Zapisz raport, przywróć stabilne ustawienia pamięci i powtórz test. Wynik wymaga dalszej weryfikacji."})
        if canonical=="GPU":
            renderer=str(current.get("renderer") or "").casefold()
            if any(token in renderer for token in ("microsoft basic render driver","gdi generic","llvmpipe","software rasterizer","swiftshader")):
                if state=="PASS": state="WARN"
                findings.append({"severity":"WARN","check":"Renderer GPU","detail":"Wykryto renderer programowy/podstawowy: "+str(current.get("renderer")),
                    "action":"Sprawdź sterownik producenta i aktywny adapter. FPS z renderera programowego nie jest porównywalny z FPS sprzętowego GPU."})
        temp=_u163_pick(current,("cpu_temp_peak_c",)) if canonical=="CPU" else (_u163_pick(current,("gpu_temp_peak_c","temperature_c")) if canonical=="GPU" else None)
        threshold=95.0 if canonical=="CPU" else 90.0
        if temp is not None and temp>=threshold:
            if state=="PASS": state="WARN"
            findings.append({"severity":"WARN","check":"Temperatura pod obciążeniem","detail":f"{temp:.1f}°C; orientacyjny próg ostrzeżenia {threshold:.0f}°C zależy od modelu.",
                "action":"Sprawdź specyfikację producenta, chłodzenie i temperaturę w dłuższym obciążeniu. Sam próg nie przesądza o awarii."})
        if current.get("error"):
            if state=="PASS": state="WARN"
            findings.append({"severity":"WARN","check":"Komunikat silnika","detail":str(current.get("error"))[:1000],"action":"Otwórz raport źródłowy i sprawdź ten komunikat."})
    baseline=_u163_find_baseline(canonical,current,history_entries) if current and valid else None
    trend=[]
    if baseline:
        trend=_u163_metric_deltas(current,baseline["payload"])
        for row in trend:
            if row["classification"]=="REGRESSION":
                if state=="PASS": state="WARN"
                findings.append({"severity":"WARN","check":"Trend: "+row["metric"],"detail":row["message"],
                    "action":"Powtórz test w podobnych warunkach; sprawdź procesy w tle, temperatury i plan zasilania. Spadek sam nie rozpoznaje awarii."})
            elif row["classification"]=="IMPROVEMENT":
                findings.append({"severity":"INFO","check":"Trend: "+row["metric"],"detail":row["message"],"action":"Porównano te same testy i potwierdzone ustawienia."})
            elif row["classification"]=="STABLE":
                findings.append({"severity":"INFO","check":"Trend: "+row["metric"],"detail":row["message"],"action":"Kontynuuj pomiary w podobnych warunkach."})
    elif current and valid:
        findings.append({"severity":"INFO","check":"Historia porównawcza","detail":"Brak wcześniejszego raportu z potwierdzoną zgodnością testu i konfiguracji.",
            "action":"Uruchom dokładnie ten sam test ponownie na tym samym komputerze, aby utworzyć bazę porównawczą."})
    return {"app":"NAPRAWA PC HARDWARE TEST PRO","diagnosis_version":_U163_BENCHMARK_DIAGNOSIS_VERSION,
        "created_at":_u163_datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
        "module":canonical,"test_id":name,"state":state,"measurement_verified":bool(valid),
        "source_report_path":str(current.get("report_path") or ""),
        "source_report_created_at":str(current.get("finished_at") or current.get("created_at") or "N/D"),
        "hardware":current.get("hardware") if isinstance(current.get("hardware"),dict) else {},
        "metrics":metrics,"baseline":({"created_at":baseline["created_at"],"path":baseline["path"],"reason":baseline["reason"]} if baseline else None),
        "trend":trend,"findings":findings,
        "scope_note":"Analiza korzysta z lokalnego raportu i historii. Brak danych nie oznacza PASS; różnice wskazują kierunek dalszej diagnostyki, a nie automatycznie rozpoznaną awarię."}

def _u163_report_root(base_dir=None):
    if base_dir is not None:return _u163_Path(base_dir)
    root=_u163_os.environ.get("LOCALAPPDATA") or str(_u163_Path.home())
    return _u163_Path(root)/"NaprawaPC"/"Raporty"/"BenchmarkDiagnostics"

def _u163_render_html(report):
    esc=_u163_html.escape; rows=[]; metrics=[]
    for item in report.get("findings") or []:
        rows.append("<tr><td>"+esc(str(item.get("severity","INFO")))+"</td><td>"+esc(str(item.get("check","")))+
            "</td><td>"+esc(str(item.get("detail","")))+"</td><td>"+esc(str(item.get("action","")))+"</td></tr>")
    for label,value in (report.get("metrics") or {}).items():
        shown="N/D" if value is None else (f"{value:,.2f}" if isinstance(value,(int,float)) else str(value))
        metrics.append("<tr><th>"+esc(str(label))+"</th><td>"+esc(shown)+"</td></tr>")
    state=str(report.get("state","WARN")).upper()
    color="#12824a" if state=="PASS" else "#b42332" if state=="FAIL" else "#9a6700"
    data=esc(_u163_json.dumps(report,ensure_ascii=False,indent=2,default=str))
    return ("<!doctype html><html lang='pl'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
        "<title>Analiza wyniku CPU/RAM/GPU</title><style>body{background:#091321;color:#eaf3ff;font:14px Segoe UI,Arial;margin:24px}"
        "main{max-width:1250px;margin:auto}section{background:#111f31;border:1px solid #27435f;border-radius:10px;padding:18px;margin:12px 0}"
        "h1{color:#53cfff}table{width:100%;border-collapse:collapse}td,th{padding:8px;border-bottom:1px solid #27435f;text-align:left;vertical-align:top}"
        "th{color:#8fdcff}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:12px Consolas;color:#dce8ff}.state{display:inline-block;background:"+color+";padding:7px 14px;border-radius:6px;font-weight:700}"
        "</style></head><body><main><section><h1>ANALIZA POMIARU — NAPRAWA PC HARDWARE TEST PRO</h1><p>Moduł: "+
        esc(str(report.get("module","N/D")))+" • test: "+esc(str(report.get("test_id","N/D")))+"</p><p class='state'>"+esc(state)+
        "</p><p>"+esc(str(report.get("scope_note","")))+"</p></section><section><h2>Zmierzona telemetria</h2><table>"+"".join(metrics)+
        "</table></section><section><h2>Wnioski i następne kroki</h2><table><thead><tr><th>Poziom</th><th>Kontrola</th><th>Wynik</th><th>Zalecenie</th></tr></thead><tbody>"+
        "".join(rows)+"</tbody></table></section><section><h2>Raport JSON</h2><details><summary>Pokaż dane</summary><pre>"+data+"</pre></details></section></main></body></html>")

def _u163_save_report(report,base_dir=None):
    root=_u163_report_root(base_dir);root.mkdir(parents=True,exist_ok=True)
    stamp=_u163_datetime.datetime.now().astimezone().strftime("%Y%m%d-%H%M%S-%f")
    stem=stamp+"-"+str(report.get("module","N_D")).lower()+"-analysis"
    jp=root/(stem+".json");hp=root/(stem+".html")
    payload=dict(report);payload["diagnosis_json_path"]=str(jp.resolve());payload["diagnosis_html_path"]=str(hp.resolve())
    jt=root/(stem+".json.tmp");ht=root/(stem+".html.tmp")
    jt.write_text(_u163_json.dumps(payload,ensure_ascii=False,indent=2,default=str),encoding="utf-8")
    ht.write_text(_u163_render_html(payload),encoding="utf-8")
    _u163_os.replace(str(jt),str(jp));_u163_os.replace(str(ht),str(hp))
    report["diagnosis_json_path"]=str(jp.resolve());report["diagnosis_html_path"]=str(hp.resolve())
    return report

def _u163_show_diagnosis(app,module):
    canonical=_u163_module(module);report={};test_key=""
    try:
        latest,test_key=_u151_last_result(app,canonical)
        if isinstance(latest,dict):report=dict(latest)
    except Exception as exc:report={"state":"warn","error":type(exc).__name__+": "+str(exc)}
    analysis=_u163_analyze_report(canonical,report,test_key)
    try:_u163_save_report(analysis)
    except Exception as exc:analysis["save_error"]=type(exc).__name__+": "+str(exc)
    t=app.colors();win=_u163_tk.Toplevel(app);win.title("Analiza wyniku — "+canonical+" — HARDWARE TEST PRO")
    win.geometry("1160x650");win.minsize(900,500);win.configure(bg=t["bg"])
    head=_u163_tk.Frame(win,bg=t["panel"],highlightbackground=t["accent"],highlightthickness=1);head.pack(fill="x",padx=12,pady=(12,7))
    color=t["good"] if analysis["state"]=="PASS" else t["bad"] if analysis["state"]=="FAIL" else t["warn"]
    _u163_tk.Label(head,text=f"ANALIZA POMIARU {canonical} • {analysis['state']}",bg=t["panel"],fg=color,font=app.fnt(12,"bold"),anchor="w").pack(fill="x",padx=10,pady=(8,3))
    _u163_tk.Label(head,text=f"Test: {analysis.get('test_id','N/D')} • Raport źródłowy: {analysis.get('source_report_created_at','N/D')}\n{analysis['scope_note']}",
        bg=t["panel"],fg=t["muted"],font=app.fnt(8),anchor="w",justify="left",wraplength=1080).pack(fill="x",padx=10,pady=(0,8))
    shell=_u163_tk.Frame(win,bg=t["bg"]);shell.pack(fill="both",expand=True,padx=12,pady=(0,8))
    cols=("severity","check","detail","action");tree=_u163_ttk.Treeview(shell,columns=cols,show="headings",height=14)
    for key,title,width in (("severity","POZIOM",80),("check","KONTROLA",180),("detail","CO WYKRYTO",430),("action","ZALECENIE",420)):
        tree.heading(key,text=title);tree.column(key,width=width,minwidth=60,stretch=key in ("detail","action"))
    for tag,col in (("FAIL",t["bad"]),("WARN",t["warn"]),("PASS",t["good"]),("INFO",t["muted"])):tree.tag_configure(tag,foreground=col)
    sb=_u163_ttk.Scrollbar(shell,orient="vertical",command=tree.yview);tree.configure(yscrollcommand=sb.set);tree.pack(side="left",fill="both",expand=True);sb.pack(side="right",fill="y")
    for i,item in enumerate(analysis.get("findings") or []):
        sev=str(item.get("severity","INFO")).upper()
        tree.insert("","end",iid=str(i),values=(sev,item.get("check",""),item.get("detail",""),item.get("action","")),tags=(sev,))
    buttons=_u163_tk.Frame(win,bg=t["bg"]);buttons.pack(fill="x",padx=12,pady=(0,12))
    def open_html():
        path=_u163_Path(str(analysis.get("diagnosis_html_path") or ""))
        if not path.is_file():_u163_messagebox.showwarning("Raport analizy","Nie znaleziono pliku HTML.",parent=win);return
        _u163_webbrowser.open(path.resolve().as_uri())
    def open_folder():
        try:
            opener=getattr(app,"open_shell",None)
            if callable(opener):opener(str(_u163_report_root()))
            elif hasattr(_u163_os,"startfile"):_u163_os.startfile(str(_u163_report_root()))
            else:raise OSError("Brak mechanizmu otwierania folderu.")
        except Exception as exc:_u163_messagebox.showerror("Folder raportów",str(exc),parent=win)
    app.make_button(buttons,"OTWÓRZ RAPORT HTML",open_html,"accent",side="left",ipady=4)
    app.make_button(buttons,"FOLDER ANALIZ",open_folder,"card",side="left",ipady=4)
    app.make_button(buttons,"ZAMKNIJ",win.destroy,"card",side="right",ipady=4)
    return analysis

def _u163_attach_diagnosis_button(app,module):
    panel=getattr(app,"_u151_hardware_console",None)
    if not isinstance(panel,dict) or panel.get("module")!=module:return False
    if panel.get("_u163_diagnosis_button_added"):return True
    frame=panel.get("frame")
    try:
        if frame is None or not frame.winfo_exists():return False
        actions=_u163_tk.Frame(frame,bg=app.colors()["panel"]);actions.pack(fill="x",padx=8,pady=(0,7))
        app.make_button(actions,"ANALIZA WYNIKU + TREND Z POPRZEDNIM TESTEM",
            lambda m=module:_u163_show_diagnosis(app,m),"good",side="left",ipady=4)
        panel["_u163_diagnosis_button_added"]=True;panel["_u163_diagnosis_actions"]=actions
        return True
    except Exception as exc:
        try:app.queue_log("Diagnostyka wyniku: "+type(exc).__name__+": "+str(exc))
        except Exception:pass
        return False

def _u163_attach_console(app,module):
    result=_U163_ORIGINAL_ATTACH_CONSOLE(app,module)
    key=_u163_module(module)
    if key in ("CPU","RAM","GPU"):_u163_attach_diagnosis_button(app,key)
    return result

_u151_attach_console=_u163_attach_console
AppV43.show_benchmark_diagnosis=_u163_show_diagnosis

def _u163_selftest_hardware_diagnosis():
    assert _U163_BENCHMARK_DIAGNOSIS_VERSION=="1.0.0"
    hw={"computer_name":"TEST-PC","platform":"Windows-11","cpu_logical_processors":16,"cpu_physical_cores":8,"ram_total_mb":32768}
    old={"module":"CPU","test_id":"CPU_DIRECT_SHA256_MULTI","state":"good","created_at":"2026-01-01T10:00:00+00:00","finished_at":"2026-01-01T10:00:15+00:00",
         "operations":15000,"operations_per_second":1000.0,"throughput_mib_s":62.5,"workers":16,"hardware":dict(hw),
         "test_settings":{"cpu_mode":"multi","algorithm":"SHA-256","duration":15}}
    new={"module":"CPU","test_id":"CPU_DIRECT_SHA256_MULTI","state":"good","created_at":"2026-01-02T10:00:00+00:00","finished_at":"2026-01-02T10:00:15+00:00",
         "operations":12000,"operations_per_second":800.0,"throughput_mib_s":50.0,"workers":16,"hardware":dict(hw),
         "test_settings":{"cpu_mode":"multi","algorithm":"SHA-256","duration":15}}
    assert _u163_evidence("CPU",new)[0]
    assert _u163_comparability(new,old)[0]
    delta=_u163_metric_deltas(new,old)
    assert any(x["metric"]=="SHA-256/s" and x["classification"]=="REGRESSION" and round(x["percent"])==-20 for x in delta)
    entries=[{"module":"CPU","test_id":old["test_id"],"created_at":old["created_at"],"path":"old.json","payload":old}]
    analysis=_u163_analyze_report("CPU",new,new["test_id"],history_entries=entries)
    assert analysis["state"]=="WARN" and any(x["check"]=="Trend: SHA-256/s" for x in analysis["findings"])
    different=dict(old);different["test_settings"]=dict(old["test_settings"],cpu_mode="single")
    assert not _u163_comparability(new,different)[0]
    ram={"module":"RAM","test_id":"RAM_DIRECT_256MB","state":"good","tested_mb":256,"bytes_verified":268435456,
         "patterns_completed":12,"patterns_total":12,"mismatch_count":2,"hardware":dict(hw)}
    ram_result=_u163_analyze_report("RAM",ram,ram["test_id"],history_entries=[])
    assert ram_result["state"]=="FAIL" and any(x["check"]=="Niezgodności RAM" for x in ram_result["findings"])
    gpu={"module":"GPU","test_id":"GPU_DIRECT_OPENGL_SCENE_01","state":"good","frames":0,"average_fps":0}
    assert not _u163_evidence("GPU",gpu)[0] and _u163_analyze_report("GPU",gpu,gpu["test_id"],history_entries=[])["state"]=="WARN"
    with __import__("tempfile").TemporaryDirectory(prefix="npc-hardware-diagnosis-test-") as tmp:
        sample=dict(analysis);sample["findings"]=[{"severity":"WARN","check":"<script>","detail":"<script>alert(1)</script>","action":"Sprawdź raport."}]
        _u163_save_report(sample,tmp);jp=_u163_Path(sample["diagnosis_json_path"]);hp=_u163_Path(sample["diagnosis_html_path"])
        assert jp.is_file() and hp.is_file()
        html_text=hp.read_text(encoding="utf-8")
        assert "<script>alert(1)</script>" not in html_text and "&lt;script&gt;" in html_text
        assert _u163_json.loads(jp.read_text(encoding="utf-8"))["module"]=="CPU"
    assert callable(_u163_show_diagnosis) and callable(_u163_attach_diagnosis_button)
    assert "ANALIZA WYNIKU + TREND Z POPRZEDNIM TESTEM" in _u163_attach_diagnosis_button.__code__.co_consts
    print("HARDWARE_BENCHMARK_DIAGNOSIS_SELFTEST_OK: evidence gates, valid baseline comparison, regression trend, RAM mismatch, GPU no-frame warning, safe JSON/HTML")

if __name__=="__main__" and "--selftest-hardware-diagnosis" in _u163_sys.argv:
    try:
        _u163_selftest_hardware_diagnosis()
        raise SystemExit(0)
    except Exception as _u163_exc:
        import traceback as _u163_traceback
        print("HARDWARE_BENCHMARK_DIAGNOSIS_SELFTEST_FAILED:",type(_u163_exc).__name__,str(_u163_exc))
        _u163_traceback.print_exc()
        raise SystemExit(1)
