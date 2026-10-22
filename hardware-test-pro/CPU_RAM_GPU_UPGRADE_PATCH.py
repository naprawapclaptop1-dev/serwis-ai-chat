import os as _u145_os
import time as _u145_time
import math as _u145_math
import threading as _u145_threading
import hashlib as _u145_hashlib
import tkinter as _u145_tk
from tkinter import ttk as _u145_ttk

_U145_CPU_RAM_GPU_PATCH_VERSION = "1.0.0"
_U145_ORIGINAL_SHOW_TEST_DETAIL = _u93_show_test_detail
_U145_ORIGINAL_EXECUTE_CATALOG_TEST = _u93_execute_catalog_test
_U145_ORIGINAL_RAM_PROGRESS_UPDATE = globals().get("_u102_ram_progress_update")
_U145_ORIGINAL_GPU_SCENE = _u66_execute_gpu_scene
_U145_ORIGINAL_GPU_SUITE = globals().get("_u88_run_3d_suite")

def _u145_num(value):
    try:
        number=float(value)
        return number if _u145_math.isfinite(number) else None
    except Exception:
        return None

def _u145_snapshot(app=None):
    out={"cpu_percent":None,"process_cpu_percent":None,"per_core_percent":[],"cpu_clock_mhz":None,"cpu_temp_c":None,
         "ram_total_mb":None,"ram_available_mb":None,"ram_used_mb":None,"ram_used_percent":None,
         "gpu_load_percent":None,"gpu_temp_c":None,"gpu_clock_mhz":None}
    p=globals().get("psutil")
    if p is not None:
        try:
            cores=[float(v) for v in (p.cpu_percent(interval=None,percpu=True) or []) if _u145_num(v) is not None]
            if cores:
                out["per_core_percent"]=[round(v,1) for v in cores]
                out["cpu_percent"]=round(sum(cores)/len(cores),1)
        except Exception:pass
        try:out["process_cpu_percent"]=round(float(p.Process(_u145_os.getpid()).cpu_percent(interval=None)),1)
        except Exception:pass
        try:
            f=p.cpu_freq()
            out["cpu_clock_mhz"]=round(float(f.current),1) if f and _u145_num(f.current) is not None else None
        except Exception:pass
        try:
            m=p.virtual_memory()
            out.update({"ram_total_mb":round(m.total/1048576,1),"ram_available_mb":round(m.available/1048576,1),
                        "ram_used_mb":round(m.used/1048576,1),"ram_used_percent":round(float(m.percent),1)})
        except Exception:pass
    cache=getattr(app,"_u66_sensor_cache",{}) or {} if app is not None else {}
    telemetry=getattr(app,"_u84_gpu_last_telemetry",{}) or {} if app is not None else {}
    cache=cache if isinstance(cache,dict) else {}
    telemetry=telemetry if isinstance(telemetry,dict) else {}
    gpu=cache.get("gpu",{}) if isinstance(cache.get("gpu"),dict) else {}
    out["gpu_load_percent"]=_u145_num(telemetry.get("gpu_load_percent",telemetry.get("load_percent",gpu.get("gpu_load_percent",cache.get("gpu_load_percent")))))
    out["gpu_temp_c"]=_u145_num(telemetry.get("temperature_c",telemetry.get("gpu_temp_c",gpu.get("gpu_temp_c",cache.get("gpu_temp_c")))))
    out["gpu_clock_mhz"]=_u145_num(telemetry.get("gpu_clock_mhz",gpu.get("gpu_clock_mhz")))
    out["cpu_temp_c"]=_u145_num(cache.get("cpu_temp_c"))
    sensors=cache.get("sensors")
    if out["cpu_temp_c"] is None and isinstance(sensors,list) and callable(globals().get("_u106_extract_cpu_sensor_values")):
        try:out["cpu_temp_c"]=_u145_num(_u106_extract_cpu_sensor_values({"sensors":sensors}).get("cpu_temp_c"))
        except Exception:pass
    return out

def _u145_metric_values(module,kind,snapshot=None,settings=None,result=None):
    s=snapshot or {};cfg=settings or {};r=result or {}
    if module=="CPU":
        load=_u145_num(r.get("cpu_load_avg_percent",s.get("cpu_percent")))
        process=_u145_num(r.get("process_cpu_avg_percent",s.get("process_cpu_percent")))
        clock=_u145_num(r.get("cpu_clock_mhz_last",s.get("cpu_clock_mhz")))
        temp=_u145_num(r.get("cpu_temp_peak_c",s.get("cpu_temp_c")))
        return {"v1":"N/D" if load is None else f"{load:.1f}% systemu",
                "v2":"N/D" if process is None else f"{process:.1f}% procesu",
                "v3":"N/D" if clock is None else f"{clock:.0f} MHz",
                "v4":"N/D" if temp is None else f"{temp:.1f} °C"}
    if module=="RAM":
        used=_u145_num(s.get("ram_used_percent"));available=_u145_num(s.get("ram_available_mb"))
        tested=_u145_num(r.get("tested_mb",r.get("buffer_mb",cfg.get("memory_mb"))))
        write=_u145_num(r.get("write_mib_s_overall"));verify=_u145_num(r.get("verify_mib_s_overall"))
        speed=f"Zapis {write:.1f} / wer. {verify:.1f} MiB/s" if write is not None and verify is not None else "Wynik po pomiarze"
        return {"v1":"N/D" if used is None else f"{used:.1f}% zajęte",
                "v2":"N/D" if available is None else f"{available:.0f} MB wolne",
                "v3":"N/D" if tested is None else f"{tested:.0f} MB testu","v4":speed}
    load=_u145_num(s.get("gpu_load_percent"));avg=_u145_num(r.get("average_fps",r.get("mean_fps")))
    peak=_u145_num(r.get("peak_fps_1s",r.get("peak_fps")))
    renderer=str(r.get("renderer") or r.get("gpu") or "Wynik renderera po zakończeniu")
    return {"v1":"N/D" if load is None else f"{load:.1f}% z czujnika",
            "v2":"N/D" if avg is None else f"{avg:.2f} FPS",
            "v3":"N/D" if peak is None else f"{peak:.2f} FPS","v4":renderer[:38]}

def _u145_draw_chart(app,panel):
    canvas=panel.get("chart")
    if canvas is None or not canvas.winfo_exists():return
    canvas.delete("all")
    w=max(220,int(canvas.winfo_width() or 540));h=max(56,int(canvas.winfo_height() or 70));t=app.colors()
    module=panel.get("module","CPU")
    field,label={"CPU":("cpu_percent","OBCIĄŻENIE CPU SYSTEMU — RZECZYWISTY ODCZYT (%)"),
                 "RAM":("ram_used_percent","UŻYCIE RAM — RZECZYWISTY ODCZYT (%)"),
                 "GPU":("gpu_load_percent","OBCIĄŻENIE GPU — TYLKO GDY SENSOR JEST DOSTĘPNY (%)")}.get(module,("gpu_load_percent","TELEMETRIA Z DOSTĘPNEGO SENSORA"))
    canvas.configure(bg=t["card"],highlightthickness=0,bd=0)
    canvas.create_text(9,7,anchor="nw",text=label,fill=t["muted"],font=app.fnt(7,"bold"))
    top,bottom,left,right=23,h-8,10,w-10
    for i in range(1,4):
        y=top+(bottom-top)*i/4.0;canvas.create_line(left,y,right,y,fill=t["panel"],width=1)
    vals=[_u145_num(row.get(field)) for row in panel.get("samples",[])]
    vals=[v for v in vals if v is not None]
    if not vals:
        canvas.create_text(w/2,(top+bottom)/2,text="Czekam na rzeczywisty odczyt czujnika…",fill=t["muted"],font=app.fnt(8));return
    points=[]
    for i,value in enumerate(vals[-60:]):
        x=left+(right-left)*i/max(1,min(60,len(vals)-1))
        y=bottom-(bottom-top)*max(0,min(100,value))/100
        points.extend([x,y])
    if len(points)>=4:canvas.create_line(*points,fill=t["accent"],width=2,smooth=True)
    elif len(points)==2:
        x,y=points;canvas.create_oval(x-2,y-2,x+2,y+2,fill=t["accent"],outline=t["accent"])
    canvas.create_text(right,top,anchor="ne",text=f"ostatni: {vals[-1]:.1f}%",fill=t["accent"],font=app.fnt(8,"bold"))

def _u145_queue_panel(app,test_id,progress=None,headline=None,metrics=None,sample=None):
    def apply():
        panel=(getattr(app,"_u145_live_panels",{}) or {}).get(str(test_id))
        if not panel:return
        frame=panel.get("frame")
        try:
            if frame is None or not frame.winfo_exists():return
            if headline is not None and panel["headline"].winfo_exists():panel["headline"].configure(text=str(headline))
            if progress is not None and panel["progress"].winfo_exists():panel["progress"].configure(value=max(0,min(100,float(progress))))
            for key,value in (metrics or {}).items():
                widget=panel.get("values",{}).get(key)
                if widget is not None and widget.winfo_exists():widget.configure(text=str(value))
            if isinstance(sample,dict):
                panel.setdefault("samples",[]).append(sample);panel["samples"]=panel["samples"][-60:]
                _u145_draw_chart(app,panel)
        except Exception:pass
    try:
        queue=getattr(app,"queue_action",None)
        if callable(queue):queue(apply)
    except Exception:pass

def _u145_add_test_panel(app,module,test_id,kind):
    report=getattr(app,"_u93_detail_report",None)
    if report is None or not report.winfo_exists():return
    t=app.colors();parent=report.master
    frame=_u145_tk.Frame(parent,bg=t["panel"],highlightbackground=t["accent"],highlightthickness=1)
    frame.pack(fill="x",padx=8,pady=(0,7),before=report)
    _u145_tk.Label(frame,text=f"DIAGNOSTYKA NA ŻYWO — {module} • {test_id}",bg=t["panel"],fg=t["accent"],font=app.fnt(10,"bold"),anchor="w").pack(fill="x",padx=10,pady=(7,2))
    headline=_u145_tk.Label(frame,text="GOTOWY — uruchom test, aby zobaczyć rzeczywiste pomiary.",bg=t["panel"],fg=t["muted"],font=app.fnt(8,"bold"),anchor="w",justify="left")
    headline.pack(fill="x",padx=10,pady=(0,3))
    progress=_u145_ttk.Progressbar(frame,mode="determinate",maximum=100,value=0);progress.pack(fill="x",padx=10,pady=(0,5))
    cards=_u145_tk.Frame(frame,bg=t["panel"]);cards.pack(fill="x",padx=5,pady=(0,4))
    specs={"CPU":(("CPU SYSTEM","v1"),("PROCES TESTU","v2"),("TAKTOWANIE","v3"),("TEMP. CPU","v4")),
           "RAM":(("UŻYCIE RAM","v1"),("DOSTĘPNA PAMIĘĆ","v2"),("BUF. TESTU","v3"),("ZAPIS / WERYF.","v4")),
           "GPU":(("OBCIĄŻENIE GPU","v1"),("FPS ŚREDNI","v2"),("FPS PEAK","v3"),("RENDERER","v4"))}[module]
    values={}
    for i,(caption,key) in enumerate(specs):
        card=_u145_tk.Frame(cards,bg=t["card"],highlightbackground=t["panel"],highlightthickness=1);card.grid(row=0,column=i,sticky="nsew",padx=2,pady=2)
        _u145_tk.Label(card,text=caption,bg=t["card"],fg=t["muted"],font=app.fnt(7,"bold")).pack(anchor="w",padx=5,pady=(4,1))
        val=_u145_tk.Label(card,text="N/D",bg=t["card"],fg=t["accent2"],font=app.fnt(9,"bold"),anchor="w",justify="left")
        val.pack(fill="x",padx=5,pady=(0,4));values[key]=val;cards.grid_columnconfigure(i,weight=1,uniform="test-metrics")
    chart=_u145_tk.Canvas(frame,height=70,bg=t["card"],highlightthickness=0,bd=0);chart.pack(fill="x",padx=7,pady=(0,7))
    panels=getattr(app,"_u145_live_panels",None)
    if not isinstance(panels,dict):panels={};app._u145_live_panels=panels
    panel={"frame":frame,"module":module,"test_id":str(test_id),"kind":kind,"headline":headline,"progress":progress,"values":values,"chart":chart,"samples":[]}
    panels[str(test_id)]=panel
    app._u145_active_test_id=str(test_id)
    settings=(getattr(app,"_u145_settings_by_test",{}) or {}).get(str(test_id),{})
    snapshot=_u145_snapshot(app);metrics=_u145_metric_values(module,kind,snapshot,settings,{})
    for key,value in metrics.items():values[key].configure(text=value)
    _u145_draw_chart(app,panel)

def _u145_show_test_detail(app,module,test_id):
    _U145_ORIGINAL_SHOW_TEST_DETAIL(app,module,test_id)
    try:
        normalized=_u93_norm(module);item=_u93_find_test(normalized,test_id)
        kind=item[3] if item and len(item)>3 else ""
        panel_module="GPU" if normalized=="VRAM" else normalized
        if panel_module in ("CPU","RAM","GPU") and kind!="sim":
            _u145_add_test_panel(app,panel_module,test_id,kind)
    except Exception as exc:
        try:app.queue_log(f"Panel pomiarowy {test_id}: {type(exc).__name__}: {exc}")
        except Exception:pass

def _u145_stopped(app):
    if bool(getattr(app,"stop_requested",False)):return True
    try:return bool(app._test_should_stop())
    except Exception:return False

def _u145_cpu_benchmark(app,kind,settings):
    requested=int(settings.get("duration",15) or 15)
    if kind=="cpu_load60":requested=60
    elif kind=="cpu_load300":requested=300
    seconds=max(5,min(300,requested))
    logical=max(1,int(_u145_os.cpu_count() or 1))
    workers=1 if kind=="cpu_single" else min(64,logical)
    payload=(b"NAPRAWA-PC-HARDWARE-TEST-PRO-CPU-STRESS-SHA256-"*65536)[:2*1024*1024]
    counts=[0]*workers;byte_counts=[0]*workers;halt=_u145_threading.Event()
    started=_u145_time.perf_counter();deadline=started+seconds;samples=[];last=0.0
    p=globals().get("psutil")
    try:
        if p is not None:
            p.cpu_percent(interval=None,percpu=True);p.Process(_u145_os.getpid()).cpu_percent(interval=None)
    except Exception:pass
    def work(index):
        while not halt.is_set() and _u145_time.perf_counter()<deadline:
            if bool(getattr(app,"stop_requested",False)):halt.set();break
            _u145_hashlib.sha256(payload).digest()
            counts[index]+=1;byte_counts[index]+=len(payload)
    threads=[_u145_threading.Thread(target=work,args=(i,),daemon=True,name=f"NPC-CPU-STRESS-{i+1}") for i in range(workers)]
    for thread in threads:thread.start()
    while any(thread.is_alive() for thread in threads):
        now=_u145_time.perf_counter()
        if _u145_stopped(app):halt.set()
        elapsed=now-started
        if now-last>=0.4:
            snap=_u145_snapshot(app);samples.append(snap)
            done=sum(counts);total_bytes=sum(byte_counts);percent=min(99,int(100*elapsed/max(1,seconds)))
            metrics=_u145_metric_values("CPU",kind,snap,settings,{})
            _u145_queue_panel(app,getattr(app,"_u145_active_test_id",""),percent,
                f"CPU {kind.upper()} • {elapsed:.1f}/{seconds} s • {workers} wątków • {done:,} przebiegów SHA-256",metrics,snap)
            try:_u93_detail_status_only(app,f"CPU {kind}: {percent}% • {done:,} przebiegów • {total_bytes/1048576:.0f} MiB")
            except Exception:pass
            last=now
        _u145_time.sleep(0.12)
    for thread in threads:thread.join()
    elapsed=max(0.001,_u145_time.perf_counter()-started);snap=_u145_snapshot(app);samples.append(snap)
    operations=sum(counts);total_bytes=sum(byte_counts);stopped=bool(getattr(app,"stop_requested",False))
    system=[_u145_num(x.get("cpu_percent")) for x in samples];system=[v for v in system if v is not None]
    process=[_u145_num(x.get("process_cpu_percent")) for x in samples];process=[v for v in process if v is not None]
    core_count=max((len(x.get("per_core_percent") or []) for x in samples),default=0);core_avg=[]
    for index in range(core_count):
        vals=[x["per_core_percent"][index] for x in samples if len(x.get("per_core_percent") or [])>index]
        core_avg.append(round(sum(vals)/len(vals),1) if vals else None)
    result={
        "state":"good" if operations>0 and not stopped else "warn","test_id":str(kind),
        "benchmark":"Rzeczywisty test obciążenia CPU przez SHA-256 na buforze 2 MiB; CPU/rdzenie i RAM odczytywane na żywo. Temperatura tylko z dostępnego sensora.",
        "mode":"single-thread" if workers==1 else ("sustained-all-workers" if kind in ("cpu_load60","cpu_load300") else "multi-thread"),
        "workers":workers,"logical_processors":logical,"duration_seconds":round(elapsed,2),
        "operations":operations,"operations_per_second":round(operations/elapsed,2),
        "processed_mib":round(total_bytes/1048576,2),"throughput_mib_s":round(total_bytes/elapsed/1048576,2),
        "cpu_load_avg_percent":round(sum(system)/len(system),2) if system else None,"cpu_load_peak_percent":max(system) if system else None,
        "process_cpu_avg_percent":round(sum(process)/len(process),2) if process else None,"per_core_avg_percent":core_avg,
        "cpu_clock_mhz_last":snap.get("cpu_clock_mhz"),
        "cpu_temp_peak_c":max([v for v in (_u145_num(x.get("cpu_temp_c")) for x in samples) if v is not None],default=None),
        "ram_used_percent_during_test":max([v for v in (_u145_num(x.get("ram_used_percent")) for x in samples) if v is not None],default=None),
        "sample_count":len(samples),"cancelled":stopped,"samples":samples[-120:],
        "note":"SHA-256 porównuje wydajność tej samej pracy na tym komputerze; nie jest samodzielnym dowodem braku wad fizycznych CPU. Brak sensora to N/D."
    }
    result["message"]=f"CPU {kind.upper()}: {workers} wątków • {result['operations_per_second']:.1f} SHA-256/s • średnie obciążenie systemu {result['cpu_load_avg_percent'] if result['cpu_load_avg_percent'] is not None else 'N/D'}%."
    _u93_put_result(app,"CPU_HASH_BENCHMARK" if kind in ("cpu_single","cpu_multi") else "CPU_LOAD_BENCHMARK",result)
    try:app.queue_log(result["message"])
    except Exception:pass
    metrics=_u145_metric_values("CPU",kind,snap,settings,result)
    _u145_queue_panel(app,getattr(app,"_u145_active_test_id",""),100 if result["state"]=="good" else 0,result["message"],metrics,snap)
    return result

def _u145_ram_progress_update(app,test_id,percent,message,pass_number=1):
    if callable(_U145_ORIGINAL_RAM_PROGRESS_UPDATE):
        _U145_ORIGINAL_RAM_PROGRESS_UPDATE(app,test_id,percent,message,pass_number)
    snapshot=_u145_snapshot(app)
    settings=(getattr(app,"_u145_settings_by_test",{}) or {}).get(str(test_id),{})
    metrics=_u145_metric_values("RAM","ram_pattern",snapshot,settings,{})
    _u145_queue_panel(app,str(test_id),percent,
        f"RAM • przebieg {pass_number} • {message} • wolna pamięć {snapshot.get('ram_available_mb') if snapshot.get('ram_available_mb') is not None else 'N/D'} MB",
        metrics,snapshot)

def _u145_studio_status(app,text_value):
    def apply():
        for name in ("_u66_3d_status","_u90_3d_status","_u90_gpu_status"):
            widget=getattr(app,name,None)
            try:
                if widget is not None and widget.winfo_exists():widget.configure(text=str(text_value))
            except Exception:pass
    try:
        q=getattr(app,"queue_action",None)
        if callable(q):q(apply)
    except Exception:pass
    try:app.queue_status(str(text_value))
    except Exception:pass

def _u145_execute_gpu_scene(app,scene_id,seconds=5):
    holder={};done=_u145_threading.Event();started=_u145_time.perf_counter()
    suite=bool(getattr(app,"_u145_gpu_suite_mode",False));total=max(1,len(_U66_SCENES));duration=max(1,int(seconds or 5))
    def run():
        try:holder["result"]=_U145_ORIGINAL_GPU_SCENE(app,scene_id,seconds)
        except Exception as exc:holder["result"]={"state":"warn","scene_id":int(scene_id),"error":f"{type(exc).__name__}: {exc}"}
        finally:done.set()
    thread=_u145_threading.Thread(target=run,daemon=True,name=f"NPC-GPU-SCENE-{int(scene_id)}");thread.start()
    while not done.wait(0.3):
        elapsed=_u145_time.perf_counter()-started;fraction=min(0.99,elapsed/duration)
        percent=min(99,int(100*((max(1,int(scene_id))-1+fraction)/total))) if suite else min(99,int(100*fraction))
        snap=_u145_snapshot(app);metrics=_u145_metric_values("GPU","gpu_scene",snap,{}, {})
        headline=f"GPU OpenGL • scena {int(scene_id)}/{total} • {elapsed:.1f}/{duration} s • FPS zostaną odczytane z raportu renderera"
        _u145_queue_panel(app,getattr(app,"_u145_active_test_id",""),percent,headline,metrics,snap)
        if suite or "3D" in str(getattr(app,"current_view","")).upper():_u145_studio_status(app,headline)
    thread.join()
    result=holder.get("result") or {"state":"warn","scene_id":int(scene_id),"error":"Brak raportu renderera."}
    snap=_u145_snapshot(app);metrics=_u145_metric_values("GPU","gpu_scene",snap,{},result)
    state=str(result.get("state","warn")).lower()
    headline=f"GPU scena {scene_id}: {state.upper()} • średnio {metrics['v2']} • peak {metrics['v3']} • {str(result.get('renderer') or result.get('error') or 'N/D')[:90]}"
    _u145_queue_panel(app,getattr(app,"_u145_active_test_id",""),100 if state=="good" else 0,headline,metrics,snap)
    _u145_studio_status(app,headline)
    return result

def _u145_execute_catalog_test(app,module,test_id,kind,settings):
    settings=dict(settings or {})
    by_test=getattr(app,"_u145_settings_by_test",None)
    if not isinstance(by_test,dict):by_test={};app._u145_settings_by_test=by_test
    by_test[str(test_id)]=settings
    if kind in ("cpu_single","cpu_multi","cpu_load60","cpu_load300"):
        return _u145_cpu_benchmark(app,kind,settings)
    if kind in ("gpu_suite10","gpu_suite30","gpu_suite60"):
        previous=bool(getattr(app,"_u145_gpu_suite_mode",False));app._u145_gpu_suite_mode=True
        try:result=_U145_ORIGINAL_EXECUTE_CATALOG_TEST(app,module,test_id,kind,settings)
        finally:app._u145_gpu_suite_mode=previous
    else:result=_U145_ORIGINAL_EXECUTE_CATALOG_TEST(app,module,test_id,kind,settings)
    snap=_u145_snapshot(app)
    if kind in ("ram_pattern","ram_bw","ram_bw_max"):
        values=_u145_metric_values("RAM",kind,snap,settings,result if isinstance(result,dict) else {})
        state=str((result or {}).get("state","warn")).lower() if isinstance(result,dict) else "warn"
        tested=(result or {}).get("tested_mb","N/D") if isinstance(result,dict) else "N/D"
        _u145_queue_panel(app,str(test_id),100 if state=="good" else 0,
            f"RAM {state.upper()} • bufor testowy {tested} MB • wynik z weryfikacji wzorców",values,snap)
    elif kind in ("cpu_scan","cpu_sensor"):
        values=_u145_metric_values("CPU",kind,snap,settings,result if isinstance(result,dict) else {})
        state=str((result or {}).get("state","warn")).lower() if isinstance(result,dict) else "warn"
        _u145_queue_panel(app,str(test_id),100 if state=="good" else 0,f"CPU {state.upper()} • odczyt zakończony",values,snap)
    elif kind=="ram_scan":
        values=_u145_metric_values("RAM",kind,snap,settings,result if isinstance(result,dict) else {})
        state=str((result or {}).get("state","warn")).lower() if isinstance(result,dict) else "warn"
        _u145_queue_panel(app,str(test_id),100 if state=="good" else 0,f"RAM {state.upper()} • skan zakończony",values,snap)
    elif kind in ("gpu_scan","gpu_sensor","gpu_scene","gpu_suite10","gpu_suite30","gpu_suite60"):
        values=_u145_metric_values("GPU",kind,snap,settings,result if isinstance(result,dict) else {})
        state=str((result or {}).get("state","warn")).lower() if isinstance(result,dict) else "warn"
        _u145_queue_panel(app,str(test_id),100 if state=="good" else 0,f"GPU {state.upper()} • kontrola zakończona",values,snap)
    return result

def _u145_selftest_cpu_ram_gpu():
    assert _U145_CPU_RAM_GPU_PATCH_VERSION=="1.0.0"
    assert callable(_u145_snapshot) and callable(_u145_cpu_benchmark) and callable(_u145_show_test_detail)
    assert callable(_u145_execute_catalog_test) and callable(_u145_execute_gpu_scene) and callable(_u145_ram_progress_update)
    cpu=_u145_metric_values("CPU","cpu_multi",{"cpu_percent":87.5,"process_cpu_percent":155.0,"cpu_clock_mhz":4200,"cpu_temp_c":None},{},{"cpu_load_avg_percent":87.5,"process_cpu_avg_percent":155.0,"cpu_clock_mhz_last":4200})
    assert cpu["v1"]=="87.5% systemu" and cpu["v2"]=="155.0% procesu" and cpu["v4"]=="N/D"
    ram=_u145_metric_values("RAM","ram_pattern",{"ram_used_percent":42.0,"ram_available_mb":8192},{"memory_mb":1024},{"tested_mb":768,"write_mib_s_overall":700.0,"verify_mib_s_overall":650.0})
    assert ram["v1"]=="42.0% zajęte" and ram["v2"]=="8192 MB wolne" and "700.0" in ram["v4"]
    gpu=_u145_metric_values("GPU","gpu_scene",{"gpu_load_percent":None},{},{"average_fps":61.25,"peak_fps_1s":74.0,"renderer":"OpenGL/GPU"})
    assert gpu["v1"]=="N/D" and gpu["v2"]=="61.25 FPS" and gpu["v3"]=="74.00 FPS"
    assert "_U145_ORIGINAL_EXECUTE_CATALOG_TEST" in _u145_execute_catalog_test.__code__.co_names
    assert "_U145_ORIGINAL_SHOW_TEST_DETAIL" in _u145_show_test_detail.__code__.co_names
    assert "SHA-256" in _u145_cpu_benchmark.__code__.co_consts
    print("CPU_RAM_GPU_LIVE_SELFTEST_OK: CPU utilization/throughput, live RAM pattern progress and GPU OpenGL FPS/result mapping")

_u93_show_test_detail=_u145_show_test_detail
_u93_execute_catalog_test=_u145_execute_catalog_test
if callable(_U145_ORIGINAL_RAM_PROGRESS_UPDATE):_u102_ram_progress_update=_u145_ram_progress_update
_u66_execute_gpu_scene=_u145_execute_gpu_scene
if callable(_U145_ORIGINAL_GPU_SUITE):
    def _u145_run_gpu_suite(app,seconds=5):
        previous=bool(getattr(app,"_u145_gpu_suite_mode",False));app._u145_gpu_suite_mode=True
        try:return _U145_ORIGINAL_GPU_SUITE(app,seconds)
        finally:app._u145_gpu_suite_mode=previous
    _u88_run_3d_suite=_u145_run_gpu_suite

if __name__=="__main__" and "--selftest-cpu-ram-gpu" in _u145_sys.argv:
    try:
        _u145_selftest_cpu_ram_gpu()
        raise SystemExit(0)
    except Exception as _u145_exc:
        import traceback as _u145_traceback
        print("CPU_RAM_GPU_LIVE_SELFTEST_FAILED:",type(_u145_exc).__name__,str(_u145_exc))
        _u145_traceback.print_exc()
        raise SystemExit(1)
