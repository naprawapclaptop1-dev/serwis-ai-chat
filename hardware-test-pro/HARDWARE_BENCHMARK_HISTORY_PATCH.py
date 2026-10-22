# Local persistent CPU/RAM/GPU benchmark history: JSON + HTML + comparison + CSV.
import os as _u149_os, re as _u149_re, csv as _u149_csv, json as _u149_json, html as _u149_html
import socket as _u149_socket, platform as _u149_platform, webbrowser as _u149_webbrowser
import datetime as _u149_datetime, tempfile as _u149_tempfile, math as _u149_math, sys as _u149_sys
from pathlib import Path as _u149_Path
import tkinter as _u149_tk
from tkinter import ttk as _u149_ttk, filedialog as _u149_filedialog, messagebox as _u149_messagebox

_U149_BENCHMARK_HISTORY_VERSION = "1.0.0"
_U149_ORIGINAL_EXECUTE_CATALOG = _u93_execute_catalog_test
_U149_ORIGINAL_SHOW_DETAIL = _u93_show_test_detail
_U149_ORIGINAL_SHOW_MODULE = AppV43.show_module
_U149_ORIGINAL_SHOW_TESTS_HUB = AppV43.show_tests_hub

def _u149_module_key(value):
    text=str(value or "").strip().upper()
    if "GPU" in text or "VRAM" in text or "3D" in text:return "GPU"
    if "RAM" in text or "PAMIĘĆ" in text or "PAMIEC" in text or "MEMORY" in text:return "RAM"
    if "CPU" in text or "PROCESOR" in text:return "CPU"
    return text[:48] or "N/D"

def _u149_report_root(base_dir=None):
    if base_dir is not None:return _u149_Path(base_dir)
    return _u149_Path(_u149_os.environ.get("LOCALAPPDATA") or str(_u149_Path.home()))/"NaprawaPC"/"Raporty"/"QualityTests"

def _u149_number(value):
    if value is None or isinstance(value,bool):return None
    try:
        n=float(value)
        return n if _u149_math.isfinite(n) else None
    except Exception:return None

def _u149_safe_slug(value):
    return (_u149_re.sub(r"[^A-Za-z0-9_-]+","-",str(value or "")).strip("-_") or "test")[:72]

def _u149_hardware():
    result={"computer_name":_u149_socket.gethostname(),"platform":_u149_platform.platform(),
            "cpu_logical_processors":_u149_os.cpu_count(),"cpu_physical_cores":None,"ram_total_mb":None,
            "app_version":str(globals().get("APP_VERSION") or "N/D")}
    p=globals().get("psutil")
    if p is not None:
        try:result["cpu_physical_cores"]=p.cpu_count(logical=False)
        except Exception:pass
        try:result["ram_total_mb"]=round(p.virtual_memory().total/1048576,1)
        except Exception:pass
    return result

def _u149_render_html(payload):
    module=_u149_html.escape(str(payload.get("module","N/D")))
    test_id=_u149_html.escape(str(payload.get("test_id","N/D")))
    state=str(payload.get("state","warn")).upper()
    color="#17884e" if state in ("GOOD","PASS","OK") else "#b42332" if state in ("BAD","FAIL","ERROR") else "#9a6700"
    rows=[]
    for key,value in payload.items():
        shown=_u149_json.dumps(value,ensure_ascii=False,indent=2,default=str) if isinstance(value,(dict,list,tuple)) else str(value)
        rows.append("<tr><th>"+_u149_html.escape(str(key))+"</th><td><pre>"+_u149_html.escape(shown[:12000])+"</pre></td></tr>")
    complete=_u149_html.escape(_u149_json.dumps(payload,ensure_ascii=False,indent=2,default=str))
    return ("""<!doctype html><html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Raport testu sprzętowego</title><style>
body{margin:0;background:#0a1220;color:#e9f0fb;font:14px Segoe UI,Arial,sans-serif}main{max-width:1180px;margin:24px auto;padding:0 18px}
header,section{background:#111d30;border:1px solid #263b57;border-radius:10px;padding:18px;margin-bottom:14px}
h1{font-size:23px;margin:0 0 10px;color:#67d7ff}.badge{display:inline-block;padding:6px 12px;border-radius:6px;background:"""+color+""";font-weight:700}
table{width:100%;border-collapse:collapse}th,td{padding:8px;border-bottom:1px solid #263b57;text-align:left;vertical-align:top}th{width:220px;color:#8fdcff}
pre{white-space:pre-wrap;overflow-wrap:anywhere;margin:0;font:12px Consolas,monospace;color:#dce8ff}small{color:#9eb1cb}
</style></head><body><main><header><h1>NAPRAWA PC HARDWARE TEST PRO — RAPORT POMIARU</h1><h2>"""+module+" • "+test_id+"""</h2>
<p><span class="badge">"""+_u149_html.escape(state)+"""</span></p><small>Raport lokalny. N/D oznacza brak odczytu, a nie wynik pozytywny.</small></header>
<section><h2>Wyniki i konfiguracja</h2><table>"""+ "".join(rows)+"""</table></section>
<section><h2>Pełny JSON</h2><details><summary>Pokaż pełne dane</summary><pre>"""+complete+"""</pre></details></section></main></body></html>""")

def _u149_write_report(module,test_id,report,base_dir=None,settings=None):
    try:
        root=_u149_report_root(base_dir);root.mkdir(parents=True,exist_ok=True)
        canonical=_u149_module_key(module)
        payload=dict(report) if isinstance(report,dict) else {"state":"warn","message":str(report)}
        now=_u149_datetime.datetime.now().astimezone()
        payload.update({"app":"NAPRAWA PC HARDWARE TEST PRO","module":canonical,"test_id":str(test_id or payload.get("test_id") or "N/D")})
        payload.setdefault("quality_patch_version",str(globals().get("_U146_QUALITY_PATCH_VERSION","N/D")))
        payload["created_at"]=str(payload.get("created_at") or now.isoformat(timespec="seconds"))
        payload["finished_at"]=str(payload.get("finished_at") or now.isoformat(timespec="seconds"))
        if not isinstance(payload.get("hardware"),dict):payload["hardware"]=_u149_hardware()
        if settings is not None:payload["test_settings"]=dict(settings) if isinstance(settings,dict) else str(settings)
        stamp=now.strftime("%Y%m%d-%H%M%S-%f")
        stem=stamp+"-"+_u149_safe_slug(canonical.lower())+"-"+_u149_safe_slug(payload["test_id"])
        json_path=root/(stem+".json");html_path=root/(stem+".html")
        payload["report_path"]=str(json_path.resolve());payload["html_report_path"]=str(html_path.resolve())
        tmp_json=root/(stem+".json.tmp");tmp_html=root/(stem+".html.tmp")
        tmp_json.write_text(_u149_json.dumps(payload,ensure_ascii=False,indent=2,default=str),encoding="utf-8")
        tmp_html.write_text(_u149_render_html(payload),encoding="utf-8")
        _u149_os.replace(str(tmp_json),str(json_path));_u149_os.replace(str(tmp_html),str(html_path))
        if isinstance(report,dict):
            report.update({k:payload[k] for k in ("app","module","test_id","created_at","finished_at","report_path","html_report_path")})
        return str(json_path)
    except Exception as exc:
        try:print("Benchmark report save warning:",type(exc).__name__,str(exc))
        except Exception:pass
        return None

def _u149_save_report(module,test_id,report):
    return _u149_write_report(module,test_id,report)

def _u149_infer_module(path):
    name=path.stem.upper()
    if any(x in name for x in ("GPU","VRAM","3D_SCENE")):return "GPU"
    if any(x in name for x in ("RAM","MEMORY")):return "RAM"
    if "CPU" in name:return "CPU"
    return "N/D"

def _u149_read_history(base_dir=None,limit=2000):
    root=_u149_report_root(base_dir)
    if not root.is_dir():return []
    found=[]
    try:paths=sorted(root.glob("*.json"),key=lambda p:p.stat().st_mtime,reverse=True)
    except Exception:return []
    for path in paths[:max(1,min(10000,int(limit or 2000)))]:
        try:
            if path.stat().st_size>50*1024*1024:continue
            payload=_u149_json.loads(path.read_text(encoding="utf-8-sig"))
            if not isinstance(payload,dict) or str(payload.get("app","")).upper()!="NAPRAWA PC HARDWARE TEST PRO":continue
            module=_u149_module_key(payload.get("module") or _u149_infer_module(path))
            if module not in ("CPU","RAM","GPU"):continue
            html_path=_u149_Path(str(payload.get("html_report_path") or path.with_suffix(".html")))
            if not html_path.is_absolute():html_path=path.parent/html_path
            created=str(payload.get("finished_at") or payload.get("created_at") or payload.get("sampled_at") or "")
            if not created:created=_u149_datetime.datetime.fromtimestamp(path.stat().st_mtime).astimezone().isoformat(timespec="seconds")
            hardware=payload.get("hardware") if isinstance(payload.get("hardware"),dict) else {}
            found.append({"path":str(path.resolve()),"html_path":str(html_path.resolve()),"payload":payload,"created_at":created,
                "computer":str(hardware.get("computer_name") or payload.get("computer_name") or "N/D"),"module":module,
                "test_id":str(payload.get("test_id") or payload.get("test") or path.stem),"state":str(payload.get("state") or "N/D").upper(),
                "duration_seconds":payload.get("duration_seconds"),"summary":str(payload.get("message") or payload.get("benchmark") or payload.get("note") or "Brak opisu")})
        except Exception:continue
    found.sort(key=lambda x:(x["created_at"],x["path"]),reverse=True)
    return found

def _u149_csv_cell(value):
    text="" if value is None else str(value).replace("\x00"," ")
    if text[:1] in ("=","+","-","@","\t","\r"):text="'"+text
    return text

def _u149_export_csv(entries,output_path):
    target=_u149_Path(output_path);target.parent.mkdir(parents=True,exist_ok=True)
    with target.open("w",newline="",encoding="utf-8-sig") as stream:
        writer=_u149_csv.writer(stream)
        writer.writerow(["Data","Komputer","Moduł","Test","Status","Czas (s)","CPU SHA-256/s","CPU średnio %","RAM test MB","RAM zapis MiB/s","RAM weryfikacja MiB/s","GPU średni FPS","GPU peak FPS","Renderer","Opis","JSON","HTML"])
        for row in entries:
            p=row.get("payload") or {}
            vals=[row.get("created_at"),row.get("computer"),row.get("module"),row.get("test_id"),row.get("state"),row.get("duration_seconds"),
                p.get("operations_per_second"),p.get("cpu_load_avg_percent"),p.get("size_mb",p.get("tested_mb")),
                p.get("write_MiBps",p.get("write_mib_s_overall")),p.get("verify_MiBps",p.get("verify_mib_s_overall")),
                p.get("average_fps"),p.get("peak_fps_1s"),p.get("renderer"),row.get("summary"),row.get("path"),row.get("html_path")]
            writer.writerow([_u149_csv_cell(v) for v in vals])
    return str(target.resolve())

def _u149_compare(newer,older):
    n=newer.get("payload") or {};o=older.get("payload") or {}
    candidates=[("Czas (s)",("duration_seconds",)),("CPU SHA-256/s",("operations_per_second",)),("CPU średnio %",("cpu_load_avg_percent",)),
        ("CPU przepustowość MiB/s",("throughput_mib_s",)),("RAM bufor MB",("size_mb","tested_mb")),("RAM zapis MiB/s",("write_MiBps","write_mib_s_overall")),
        ("RAM weryfikacja MiB/s",("verify_MiBps","verify_mib_s_overall")),("RAM bajty sprawdzone",("bytes_verified",)),
        ("GPU średni FPS",("average_fps","mean_fps")),("GPU peak FPS",("peak_fps_1s","peak_fps")),("GPU klatki",("frames",))]
    rows=[]
    for label,keys in candidates:
        def get(d):
            for key in keys:
                v=_u149_number(d.get(key))
                if v is not None:return v
            return None
        old,new=get(o),get(n)
        if old is None and new is None:continue
        delta=None if old is None or new is None else new-old
        pct=None if delta is None or old in (None,0) else 100*delta/abs(old)
        rows.append({"metric":label,"older":old,"newer":new,"delta":delta,"percent":pct})
    return rows

def _u149_show_comparison(app,selected):
    if len(selected)!=2:
        _u149_messagebox.showinfo("Porównanie testów","Zaznacz dokładnie dwa raporty.",parent=app);return
    newer,older=sorted(selected,key=lambda x:(x.get("created_at",""),x.get("path","")),reverse=True)
    win=_u149_tk.Toplevel(app);win.title("Porównanie pomiarów CPU/RAM/GPU");win.geometry("900x510");win.minsize(760,380)
    t=app.colors();win.configure(bg=t["bg"])
    _u149_tk.Label(win,text=f"Nowszy: {newer['module']} / {newer['test_id']} • {newer['created_at']}\nStarszy: {older['module']} / {older['test_id']} • {older['created_at']}",bg=t["bg"],fg=t["accent"],font=app.fnt(9,"bold"),justify="left",wraplength=860).pack(anchor="w",padx=12,pady=(12,6))
    _u149_tk.Label(win,text="Różnica nie jest automatyczną oceną sprawności. Porównuj ten sam test, komputer i ustawienia.",bg=t["bg"],fg=t["muted"],font=app.fnt(8),wraplength=860,justify="left").pack(anchor="w",padx=12,pady=(0,6))
    shell=_u149_tk.Frame(win,bg=t["bg"]);shell.pack(fill="both",expand=True,padx=12,pady=(0,12))
    cols=("metric","old","new","delta","pct");tree=_u149_ttk.Treeview(shell,columns=cols,show="headings")
    for key,label,width in (("metric","MIERNIK",250),("old","STARSZY",125),("new","NOWSZY",125),("delta","RÓŻNICA",125),("pct","ZMIANA %",100)):
        tree.heading(key,text=label);tree.column(key,width=width,minwidth=65,stretch=(key=="metric"))
    sb=_u149_ttk.Scrollbar(shell,orient="vertical",command=tree.yview);tree.configure(yscrollcommand=sb.set);tree.pack(side="left",fill="both",expand=True);sb.pack(side="right",fill="y")
    fmt=lambda v:"N/D" if v is None else f"{v:,.2f}"
    rows=_u149_compare(newer,older)
    for i,row in enumerate(rows):tree.insert("","end",iid=str(i),values=(row["metric"],fmt(row["older"]),fmt(row["newer"]),fmt(row["delta"]),"N/D" if row["percent"] is None else f"{row['percent']:+.1f}%"))
    if not rows:tree.insert("","end",values=("Brak wspólnych mierników liczbowych","N/D","N/D","N/D","N/D"))

def _u149_show_history(app):
    app.current_view="HARDWARE_BENCHMARK_HISTORY";app.clear();t=app.colors()
    app.header_title.config(text="HISTORIA TESTÓW SPRZĘTOWYCH — CPU / RAM / GPU")
    head=app.panel(app.content);head.pack(fill="x",padx=4,pady=(4,6))
    _u149_tk.Label(head,text="HISTORIA RZECZYWISTYCH POMIARÓW",bg=t["panel"],fg=t["accent"],font=app.fnt(12,"bold")).pack(anchor="w",padx=12,pady=(8,3))
    _u149_tk.Label(head,text="Raporty JSON/HTML pozostają lokalne. Filtruj wyniki, otwieraj raporty, porównuj dwa pomiary lub eksportuj CSV. N/D nie oznacza PASS.",bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1400,justify="left").pack(anchor="w",padx=12,pady=(0,7))
    sf=_u149_tk.Frame(app.content,bg=t["bg"]);sf.pack(fill="x",padx=8,pady=(0,5))
    _u149_tk.Label(sf,text="SZUKAJ",bg=t["bg"],fg=t["accent"],font=app.fnt(8,"bold")).pack(side="left",padx=(0,7))
    query=_u149_tk.StringVar(master=app,value="")
    _u149_tk.Entry(sf,textvariable=query,bg=t["card"],fg=t["fg"],insertbackground=t["fg"],relief="flat",font=app.fnt(9)).pack(side="left",fill="x",expand=True,ipady=4)
    shell=_u149_tk.Frame(app.content,bg=t["bg"]);shell.pack(fill="both",expand=True,padx=8,pady=(0,4))
    cols=("date","computer","module","test","state","duration","summary");tree=_u149_ttk.Treeview(shell,columns=cols,show="headings",selectmode="extended",height=12)
    for key,label,width in (("date","DATA",165),("computer","KOMPUTER",150),("module","MODUŁ",72),("test","TEST",180),("state","STATUS",75),("duration","SEK.",65),("summary","OSTATNI WYNIK",460)):
        tree.heading(key,text=label);tree.column(key,width=width,minwidth=55,stretch=(key=="summary"))
    sb=_u149_ttk.Scrollbar(shell,orient="vertical",command=tree.yview);tree.configure(yscrollcommand=sb.set);tree.pack(side="left",fill="both",expand=True);sb.pack(side="right",fill="y")
    detail=_u149_tk.Text(app.content,height=4,wrap="word",bg=t["card"],fg=t["fg"],relief="flat",font=("Consolas",8));detail.pack(fill="x",padx=8,pady=(2,5));visible={}
    def chosen():return [visible[i] for i in tree.selection() if i in visible]
    def show_detail(_event=None):
        rows=chosen()
        if not rows:return
        x=rows[0];body=f"{x['module']} / {x['test_id']} • {x['state']} • {x['created_at']}\nKomputer: {x['computer']}\nWynik: {x['summary']}\nJSON: {x['path']}\nHTML: {x['html_path']}"
        detail.configure(state="normal");detail.delete("1.0","end");detail.insert("1.0",body[:10000]);detail.configure(state="disabled")
    def open_html():
        rows=chosen()
        if not rows:_u149_messagebox.showinfo("Raport","Zaznacz raport.",parent=app);return
        x=rows[0];path=_u149_Path(x["html_path"])
        try:
            if not path.is_file():path.write_text(_u149_render_html(x["payload"]),encoding="utf-8")
            _u149_webbrowser.open(path.resolve().as_uri())
        except Exception as exc:_u149_messagebox.showerror("Raport",f"Nie udało się otworzyć: {exc}",parent=app)
    def export():
        reports=_u149_read_history()
        if not reports:_u149_messagebox.showinfo("CSV","Brak raportów CPU/RAM/GPU.",parent=app);return
        path=_u149_filedialog.asksaveasfilename(parent=app,title="Eksport historii",defaultextension=".csv",initialdir=str(_u149_report_root()),initialfile="HardwareBenchmarkHistory_"+_u149_datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+".csv",filetypes=[("CSV","*.csv"),("Wszystkie pliki","*.*")])
        if not path:return
        try:_u149_messagebox.showinfo("CSV","Zapisano:\n"+_u149_export_csv(reports,path),parent=app)
        except Exception as exc:_u149_messagebox.showerror("CSV",f"Nie udało się zapisać: {exc}",parent=app)
    def compare():_u149_show_comparison(app,chosen())
    def refresh(_event=None):
        nonlocal visible
        q=str(query.get() or "").strip().casefold();reports=_u149_read_history()
        reports=[r for r in reports if not q or q in " ".join(str(r.get(k,"")) for k in ("module","test_id","state","computer","summary","created_at")).casefold()]
        for iid in tree.get_children():tree.delete(iid)
        visible={}
        for i,r in enumerate(reports):
            iid=str(i);visible[iid]=r;d=r.get("duration_seconds")
            tree.insert("","end",iid=iid,values=(r["created_at"],r["computer"],r["module"],r["test_id"],r["state"],"N/D" if d is None else f"{float(d):.1f}",r["summary"][:220]))
        if not reports:tree.insert("","end",iid="empty",values=("Brak raportów","—","—","—","N/D","—","Uruchom CPU, RAM lub GPU, aby zapisać pierwszy pomiar."))
    tree.bind("<<TreeviewSelect>>",show_detail);query.trace_add("write",refresh)
    row=_u149_tk.Frame(app.content,bg=t["bg"]);row.pack(fill="x",padx=8,pady=(0,6))
    app.make_button(row,"↻ ODŚWIEŻ",refresh,"card",side="left",ipady=5)
    app.make_button(row,"OTWÓRZ RAPORT HTML",open_html,"card",side="left",ipady=5)
    app.make_button(row,"PORÓWNAJ 2 WYBRANE",compare,"accent",side="left",ipady=5)
    app.make_button(row,"EKSPORT CSV",export,"card",side="left",ipady=5)
    app.make_button(row,"FOLDER RAPORTÓW",lambda:app.open_shell(str(_u149_report_root())),"card",side="left",ipady=5)
    app.make_button(row,"← TESTY",app.show_tests_hub,"card",side="left",ipady=5)
    app.make_button(row,"CPU",lambda:app.show_module("CPU"),"card",side="left",ipady=5)
    app.make_button(row,"RAM",lambda:app.show_module("RAM"),"card",side="left",ipady=5)
    app.make_button(row,"GPU",lambda:app.show_module("GPU"),"card",side="left",ipady=5)
    refresh()

def _u149_execute_catalog_test(app,module,test_id,kind,settings):
    result=_U149_ORIGINAL_EXECUTE_CATALOG(app,module,test_id,kind,settings)
    canonical=_u149_module_key(module)
    if canonical in ("CPU","RAM","GPU") and kind!="sim" and isinstance(result,dict):
        path=result.get("report_path");html_path=result.get("html_report_path")
        if not path or not _u149_Path(str(path)).is_file() or not html_path or not _u149_Path(str(html_path)).is_file():
            _u149_save_report(canonical,test_id,result)
    return result

def _u149_show_test_detail(app,module,test_id):
    result=_U149_ORIGINAL_SHOW_DETAIL(app,module,test_id)
    canonical=_u149_module_key(module)
    if canonical in ("CPU","RAM","GPU"):
        try:
            panels=getattr(app,"_u145_live_panels",{}) or {};panel=panels.get(str(test_id));frame=panel.get("frame") if isinstance(panel,dict) else None
            if frame is not None and frame.winfo_exists() and not panel.get("_u149_history_button_added"):
                actions=_u149_tk.Frame(frame,bg=app.colors()["panel"]);actions.pack(fill="x",padx=7,pady=(0,7))
                app.make_button(actions,"HISTORIA TESTÓW CPU / RAM / GPU",lambda:_u149_show_history(app),"card",side="left",ipady=3)
                panel["_u149_history_button_added"]=True
        except Exception as exc:
            try:app.queue_log("Historia benchmarków: "+repr(exc))
            except Exception:pass
    return result

def _u149_show_module(app,module):
    result=_U149_ORIGINAL_SHOW_MODULE(app,module);canonical=_u149_module_key(module);view=str(getattr(app,"current_view","") or "").upper()
    if canonical in ("CPU","RAM","GPU") and not view.startswith("COMPONENT_TEST_DETAIL"):
        try:
            frame=_u149_tk.Frame(app.content,bg=app.colors()["bg"]);frame.pack(fill="x",padx=7,pady=(1,5))
            app.make_button(frame,"HISTORIA POMIARÓW CPU / RAM / GPU",lambda:_u149_show_history(app),"card",side="left",ipady=4)
        except Exception as exc:
            try:app.queue_log("Przycisk historii: "+repr(exc))
            except Exception:pass
    return result

def _u149_show_tests(app):
    result=_U149_ORIGINAL_SHOW_TESTS_HUB(app)
    try:
        frame=_u149_tk.Frame(app.content,bg=app.colors()["bg"]);frame.pack(fill="x",padx=8,pady=(2,5))
        app.make_button(frame,"HISTORIA POMIARÓW CPU / RAM / GPU",lambda:_u149_show_history(app),"accent",side="left",ipady=5)
    except Exception as exc:
        try:app.queue_log("Historia testów: "+repr(exc))
        except Exception:pass
    return result

def _u149_selftest_benchmark_history():
    assert _U149_BENCHMARK_HISTORY_VERSION=="1.0.0"
    with _u149_tempfile.TemporaryDirectory(prefix="npc-benchmark-history-test-") as tmp:
        cpu={"state":"good","duration_seconds":10.5,"operations_per_second":1250.0,"cpu_load_avg_percent":84.2,"message":"CPU test OK"}
        gpu={"state":"good","duration_seconds":5.0,"average_fps":61.5,"peak_fps_1s":78.2,"renderer":"Test Renderer","message":"<script>not executable</script>"}
        p1=_u149_write_report("CPU","CPU_BENCHMARK",cpu,tmp);p2=_u149_write_report("GPU","3D_SCENE_1",gpu,tmp)
        assert p1 and _u149_Path(p1).is_file() and p2 and _u149_Path(p2).is_file(),"JSON report missing"
        assert _u149_Path(p2).with_suffix(".html").is_file(),"HTML report missing"
        assert "&lt;script&gt;not executable&lt;/script&gt;" in _u149_Path(p2).with_suffix(".html").read_text(encoding="utf-8"),"HTML escaping failed"
        reports=_u149_read_history(tmp)
        assert len(reports)==2 and {r["module"] for r in reports}=={"CPU","GPU"},"history load failed"
        assert _u149_compare(reports[0],reports[1]),"comparison metrics missing"
        csv_path=_u149_export_csv(reports,str(_u149_Path(tmp)/"history.csv"))
        with open(csv_path,"r",encoding="utf-8-sig",newline="") as stream:rows=list(_u149_csv.reader(stream))
        assert len(rows)==3 and rows[0][0]=="Data","CSV export missing rows"
        unsafe={**gpu,"message":'=HYPERLINK("https://bad.example","click")'}
        _u149_write_report("GPU","3D_SCENE_2",unsafe,tmp)
        safe=_u149_export_csv(_u149_read_history(tmp),str(_u149_Path(tmp)/"history-safe.csv"))
        with open(safe,"r",encoding="utf-8-sig",newline="") as stream:safe_rows=list(_u149_csv.reader(stream))
        assert any(row[14].startswith("'=HYPERLINK") for row in safe_rows[1:]),"CSV formula guard failed"
        assert _u149_csv_cell("+SUM(A1:A2)").startswith("'+"),"CSV formula guard failed"
    print("HARDWARE_BENCHMARK_HISTORY_SELFTEST_OK: local JSON/HTML, comparison, CSV formula guard and persistence")

_U149_ORIGINAL_EXECUTE_CATALOG=_u93_execute_catalog_test
_U149_ORIGINAL_SHOW_DETAIL=_u93_show_test_detail
_U149_ORIGINAL_SHOW_MODULE=AppV43.show_module
_U149_ORIGINAL_SHOW_TESTS_HUB=AppV43.show_tests_hub
_u146_save_quality_report=_u149_save_report
_u93_execute_catalog_test=_u149_execute_catalog_test
_u93_show_test_detail=_u149_show_test_detail
AppV43.show_test_detail=_u149_show_test_detail
AppV43.show_module=_u149_show_module
AppV43.show_tests_hub=_u149_show_tests
if __name__=="__main__" and "--selftest-benchmark-history" in _u149_sys.argv:
    try:
        _u149_selftest_benchmark_history()
        raise SystemExit(0)
    except Exception as _u149_exc:
        import traceback as _u149_traceback
        print("HARDWARE_BENCHMARK_HISTORY_SELFTEST_FAILED:",type(_u149_exc).__name__,str(_u149_exc))
        _u149_traceback.print_exc()
        raise SystemExit(1)
