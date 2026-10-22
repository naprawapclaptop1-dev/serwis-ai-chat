# Quality wiring: measured CPU stages, clear in-app progress, and GPU result/report mapping.
import sys as _u147_sys
import tkinter as _u147_tk
from tkinter import ttk as _u147_ttk, messagebox as _u147_messagebox

_U147_ORIGINAL_MODULE_CPU = AppV43.module_cpu
_U147_ORIGINAL_MODULE_RAM = AppV43.module_ram
_U147_ORIGINAL_GPU_SCENE = _u66_execute_gpu_scene
_U147_ORIGINAL_START_REAL_3D = _u135_start_real_3d
_U147_ORIGINAL_GPU_SUITE = globals().get("_u88_run_3d_suite")

def _u147_safe_stage_update(app, stage_index):
    # draw_stage_progress is the available UI method; _set_stage is not defined by this application.
    try:
        canvas = getattr(app, "progress_canvas", None)
        draw = getattr(app, "draw_stage_progress", None)
        if canvas is None or not canvas.winfo_exists() or not callable(draw):
            return False
        get_index = getattr(app, "stage_index", None)
        current_index = get_index() if callable(get_index) else max(0, int(stage_index))
        draw(current_index)
        return True
    except Exception as exc:
        try:
            app.queue_log("CPU: pominięto niedostępny wskaźnik etapów UI: " + repr(exc))
        except Exception:
            pass
        return False


def _u147_cpu_test(app, seconds):
    requested = max(5, min(900, int(seconds or 5)))
    targets = (10, 25, 50, 75, 100)
    logical = max(1, int(_u147_os.cpu_count() or 1))
    workers = min(32, logical)
    payload = b"NAPRAWA-PC-HARDWARE-TEST-PRO-CPU-SHA256-" * 32768
    samples, stages = [], []
    started = _u147_time.perf_counter()
    stop_check = lambda: bool(getattr(app, "stop_requested", False) or _u147_stopped(getattr(app, "_test_should_stop", None)))
    try:
        if psutil:
            psutil.cpu_percent(interval=None, percpu=True)
            try: psutil.Process(_u147_os.getpid()).cpu_percent(interval=None)
            except Exception: pass
    except Exception: pass
    for stage_index, target in enumerate(targets):
        if stop_check(): break
        stage_seconds = requested / len(targets)
        stage_start = _u147_time.perf_counter()
        stage_deadline = stage_start + stage_seconds
        halt = _u147_threading.Event()
        operations = [0] * workers
        def worker(index):
            quantum = 0.12
            active = quantum * (target / 100.0)
            while not halt.is_set() and _u147_time.perf_counter() < stage_deadline:
                if getattr(app, "stop_requested", False):
                    halt.set()
                    break
                active_start = _u147_time.perf_counter()
                while not halt.is_set() and _u147_time.perf_counter() < active_start + active:
                    _u147_hashlib.sha256(payload).digest()
                    operations[index] += 1
                if target < 100:
                    halt.wait(max(0.0, quantum - active))
        threads = [_u147_threading.Thread(target=worker, args=(index,), daemon=True, name=f"NPC-CPU-{index+1}") for index in range(workers)]
        app.queue_log(f"CPU: etap {target}% — {workers} workerów; obciążenie i taktowanie mierzone w trakcie testu.")
        try: app.queue_action(lambda i=stage_index:_u147_safe_stage_update(app,i))
        except Exception: pass
        for thread in threads: thread.start()
        measured = []
        last_update = 0.0
        while any(thread.is_alive() for thread in threads):
            if stop_check(): halt.set()
            now = _u147_time.perf_counter()
            if now - last_update >= 0.35:
                load = frequency = process_load = per_core = None
                if psutil:
                    try: load = psutil.cpu_percent(interval=0.12)
                    except Exception: load = None
                    try:
                        freq = psutil.cpu_freq()
                        frequency = float(freq.current) if freq and freq.current else None
                    except Exception: pass
                    try: process_load = float(psutil.Process(_u147_os.getpid()).cpu_percent(interval=None))
                    except Exception: pass
                    try: per_core = psutil.cpu_percent(interval=None, percpu=True)
                    except Exception: per_core = None
                sample = {"target":target,"load":load,"freq":frequency,"process_load":process_load,
                          "per_core":per_core,"timestamp":_u147_time.strftime("%H:%M:%S")}
                samples.append(sample); measured.append(sample)
                done = sum(operations)
                percent = int(100 * (stage_index + min(1.0, (now-stage_start)/max(0.001,stage_seconds))) / len(targets))
                _u147_update_view(app,"CPU",percent,
                    f"Etap {target}% • {now-stage_start:.1f}/{stage_seconds:.1f} s • obciążenie systemu {load if load is not None else 'N/D'}%",None)
                try:
                    _u145_queue_panel(app,getattr(app,"_u145_active_test_id",""),percent,
                        f"CPU {target}% • {done:,} operacji SHA-256 • obciążenie {load if load is not None else 'N/D'}%",
                        _u145_metric_values("CPU","cpu_multi",_u145_snapshot(app),{},{}),_u145_snapshot(app))
                except Exception: pass
                last_update = now
            _u147_time.sleep(0.04)
        halt.set()
        for thread in threads: thread.join(timeout=1.0)
        elapsed_stage = max(0.001, _u147_time.perf_counter()-stage_start)
        loads = [float(x["load"]) for x in measured if x.get("load") is not None]
        frequencies = [float(x["freq"]) for x in measured if x.get("freq") is not None]
        stages.append({"target":target,"load":sum(loads)/len(loads) if loads else None,
                       "load_peak":max(loads) if loads else None,"freq":frequencies[-1] if frequencies else None,
                       "seconds":elapsed_stage,"operations":sum(operations),"samples":len(measured)})
        if stop_check(): break
    operations = sum(int(stage.get("operations",0) or 0) for stage in stages)
    elapsed = max(0.001, _u147_time.perf_counter()-started)
    stopped = stop_check()
    all_loads = [x["load"] for x in samples if x.get("load") is not None]
    state = "good" if operations > 0 and not stopped else "warn"
    result = {"state":state,"test":"CPU multi-stage live stress","duration_seconds":round(elapsed,2),
              "requested_seconds":requested,"logical_processors":logical,"workers":workers,"operations":operations,
              "operations_per_second":round(operations/elapsed,2),"stages":stages,
              "cpu_load_avg_percent":round(sum(all_loads)/len(all_loads),1) if all_loads else None,
              "cpu_load_peak_percent":max(all_loads) if all_loads else None,
              "per_core_percent_last":samples[-1].get("per_core") if samples else None,
              "freq_mhz_last":stages[-1].get("freq") if stages else None,"samples":samples[-120:],"stopped":stopped,
              "message":f"CPU {state.upper()}: {operations} operacji SHA-256; średnie obciążenie systemu {round(sum(all_loads)/len(all_loads),1) if all_loads else 'N/D'}%."}
    app.queue_results("CPU",result)
    app.queue_results("CPU_BENCHMARK",result)
    _u146_save_quality_report("CPU","CPU_BENCHMARK",result)
    app.queue_log(result["message"])
    _u146_update_view(app,"CPU",100 if state=="good" else 0,result["message"],result)
    return result

def _u147_ram_test(app, mb):
    started = _u147_time.monotonic()
    requested = max(64,min(2048,int(mb or 512)))
    stats = {}
    duration = 4 if requested <= 512 else 6
    def progress(percent,message):
        _u146_update_view(app,"RAM",percent,message)
        try:
            if getattr(app,"_u145_active_test_id",""):
                _u145_ram_progress_update(app,app._u145_active_test_id,percent,message,1)
        except Exception: pass
    ok,message = ram_pattern_test(requested,duration,progress_callback=progress,
        stop_check=lambda:bool(getattr(app,"stop_requested",False) or _u147_stopped(getattr(app,"_test_should_stop",None))),
        stats_out=stats)
    stopped = bool(stats.get("stopped") or getattr(app,"stop_requested",False))
    actual_mb = int(stats.get("size_mb",0) or 0)
    state = "good" if ok else "warn" if stopped or stats.get("allocation_failed") else "bad"
    elapsed = max(0.001,_u147_time.monotonic()-started)
    result = {"state":state,"size_mb":actual_mb,"requested_mb":requested,"message":message,
        "duration_seconds":round(elapsed,2),"passes":stats.get("passes",0),
        "patterns_completed":stats.get("patterns_completed",0),"patterns_total":stats.get("patterns_total",len(_U146_RAM_PATTERNS)),
        "bytes_written":stats.get("bytes_written",0),"bytes_verified":stats.get("bytes_verified",0),
        "write_MiBps":round(stats.get("bytes_written",0)/1048576/elapsed,2),
        "verify_MiBps":round(stats.get("bytes_verified",0)/1048576/elapsed,2),
        "error_offset":stats.get("error_offset"),"failed_pattern":stats.get("failed_pattern"),"stopped":stopped,
        "note":"Pełny zapis i weryfikacja prywatnego bufora procesu; nie zastępuje testu każdej fizycznej komórki RAM."}
    app.queue_results("RAM_BENCHMARK",result)
    app.queue_results("RAM",{"state":state,"size_mb":actual_mb,"message":message,"benchmark":result})
    _u146_save_quality_report("RAM","RAM_BENCHMARK",result)
    app.queue_log(f"RAM TEST: {state.upper()} • bufor {actual_mb} MB • zapis {result['write_MiBps']} MiB/s • weryfikacja {result['verify_MiBps']} MiB/s • {elapsed:.1f} s")
    _u146_update_view(app,"RAM",100 if state=="good" else 0,message,result)
    return result

def _u147_wrap_module_cpu(self):
    result = _U147_ORIGINAL_MODULE_CPU(self)
    tree = None
    def walk(parent):
        nonlocal tree
        for child in parent.winfo_children():
            if isinstance(child,_u147_ttk.Treeview):
                try:
                    labels=[str(child.heading(col,"text")) for col in child["columns"]]
                    if labels and labels[0]=="ETAP": tree=child
                except Exception: pass
            walk(child)
    try: walk(self.content)
    except Exception: pass
    self._u146_cpu_tree = tree
    if tree is not None:
        try:
            detail=tree.master.master
            bar=_u147_ttk.Progressbar(detail,mode="determinate",maximum=100,value=0)
            bar.pack(fill="x",padx=10,pady=(0,3),before=tree.master)
            label=_u147_tk.Label(detail,text="Gotowy — uruchom test, aby zmierzyć CPU na żywo.",bg=self.colors()["panel"],fg=self.colors()["muted"],font=self.fnt(8),anchor="w")
            label.pack(fill="x",padx=10,pady=(0,4),before=tree.master)
            self._u146_cpu_progressbar=bar;self._u146_cpu_progress_label=label
        except Exception: pass
    return result

def _u147_wrap_module_ram(self):
    result = _U147_ORIGINAL_MODULE_RAM(self)
    try:
        children=self.content.winfo_children()
        panel=children[-1] if children else None
        canvas=next((child for child in (panel.winfo_children() if panel is not None else []) if isinstance(child,_u147_tk.Canvas)),None)
        if panel is not None and canvas is not None:
            bar=_u147_ttk.Progressbar(panel,mode="determinate",maximum=100,value=0)
            bar.pack(fill="x",padx=10,pady=(2,2),before=canvas)
            label=_u147_tk.Label(panel,text="Gotowy — pełny zapis i weryfikacja wzorców pamięci.",bg=self.colors()["panel"],fg=self.colors()["muted"],font=self.fnt(8),anchor="w")
            label.pack(fill="x",padx=10,pady=(0,4),before=canvas)
            self._u146_ram_progressbar=bar;self._u146_ram_progress_label=label
    except Exception as exc:
        try:self.append_log("Panel postępu RAM: "+repr(exc))
        except Exception:pass
    return result

def _u147_wrap_start_real_3d(app,module):
    key=str(module or "").upper()
    if key=="GPU":return _U147_ORIGINAL_START_REAL_3D(app,key)
    if key=="VRAM":return app._u41_start_vram_test()
    if key in ("CPU","RAM","DYSK","BATERIA","SIEĆ","USB","AUDIO","KLAWIATURA","KAMERA"):
        return _u69_launch_component_test(app,key,"benchmark" if key in ("CPU","RAM","DYSK","BATERIA","SIEĆ") else "scan")
    if key=="EKRAN":return app._monitor_test()
    if key=="SECURITY":return app._security_test()
    _u147_messagebox.showinfo("Test podzespołu","Dla tego modułu nie ma niezależnego testu OpenGL. Uruchom właściwy skan.")
    return None

def _u147_execute_gpu_scene(self,scene_id,seconds=5):
    result=_U147_ORIGINAL_GPU_SCENE(self,scene_id,seconds)
    self.queue_results("GPU_3D",result)
    try:
        if isinstance(getattr(self,"results",None),dict):self.results["GPU_3D"]=result
    except Exception:pass
    _u146_save_quality_report("GPU",f"3D_SCENE_{scene_id}",result)
    def refresh():
        try:
            if getattr(self,"header_status",None) is not None and self.header_status.winfo_exists():
                state=str(result.get("state","warn")).lower()
                colour=self.colors()["good"] if state=="good" else self.colors()["warn"]
                self.header_status.configure(text=f"GPU 3D: scena {scene_id} • {result.get('average_fps','N/D')} FPS • {state.upper()}",fg=colour)
            renderer=globals().get("_u86_render_component_report")
            if callable(renderer):renderer(self,"GPU")
        except Exception as exc:
            try:self.queue_log("GPU report refresh: "+repr(exc))
            except Exception:pass
    self.queue_action(refresh)
    return result

def _u147_run_gpu_suite(self,seconds=5):
    result=_U147_ORIGINAL_GPU_SUITE(self,seconds)
    suite=result if isinstance(result,dict) else (getattr(self,"results",{}) or {}).get("3D_SUITE")
    if isinstance(suite,dict):
        self.queue_results("GPU_3D",suite)
        try:
            if isinstance(getattr(self,"results",None),dict):self.results["GPU_3D"]=suite
        except Exception:pass
        _u146_save_quality_report("GPU","3D_SUITE",suite)
        self.queue_action(lambda:_u86_render_component_report(self,"GPU") if callable(globals().get("_u86_render_component_report")) else None)
    return result

def _u147_selftest_quality_fixes():
    assert _U146_QUALITY_PATCH_VERSION=="1.0.0"
    assert tuple(_U146_RAM_PATTERNS)==(0x00,0xFF,0xAA,0x55)
    assert len(_U146_RAM_PATTERN_MODES)==26 and len(_U40_RAM_PATTERN_LIST)==26
    progress=[];stats={}
    ok,msg=_u146_verify_ram_buffer(bytearray(1024*1024),0,lambda pct,txt:progress.append((pct,txt)),lambda:False,stats)
    assert ok and stats["patterns_completed"]==26 and stats["bytes_verified"]==26*1024*1024
    assert progress and progress[-1][0]==100
    stopped={}
    ok,msg=_u146_verify_ram_buffer(bytearray(4096),0,None,lambda:True,stopped)
    assert not ok and stopped.get("stopped")
    assert callable(AppV43._cpu_test) and callable(AppV43._ram_test)
    assert "_set_stage" not in _u147_cpu_test.__code__.co_names, "CPU worker must not schedule an undefined UI method"
    assert "_u147_safe_stage_update" in _u147_cpu_test.__code__.co_names and callable(_u147_safe_stage_update)
    assert getattr(AppV43._ram_test,"_u102_ram_guard",False)
    keys=globals().get("_U86_COMPONENT_KEYS",{})
    assert keys.get("GPU",("",))[0]=="GPU_3D"
    assert "_U147_ORIGINAL_GPU_SCENE" in _u147_execute_gpu_scene.__code__.co_names
    print("QUALITY_TESTS_SELFTEST_OK: full-buffer RAM verification, cancellation, live CPU metrics and GPU result routing")

AppV43._cpu_test=_u147_cpu_test
if callable(globals().get("_u80_wrap_app_method")):_u80_wrap_app_method("_cpu_test")
_U147_ORIGINAL_RAM_TEST_CURRENT=AppV43._ram_test
AppV43._ram_test=_u147_ram_test
if callable(globals().get("_u80_wrap_app_method")):_u80_wrap_app_method("_ram_test")
try:AppV43._ram_test._u102_ram_guard=True
except Exception:pass
AppV43.module_cpu=_u147_wrap_module_cpu
AppV43.module_ram=_u147_wrap_module_ram
_u135_start_real_3d=_u147_wrap_start_real_3d
_u66_execute_gpu_scene=_u147_execute_gpu_scene
if callable(_U147_ORIGINAL_GPU_SUITE):_u88_run_3d_suite=_u147_run_gpu_suite
try:
    _u147_keys=dict(globals().get("_U86_COMPONENT_KEYS",{}))
    _u147_keys["GPU"]=("GPU_3D","3D_SUITE","GPU","GPU_WINSAT")
    globals()["_U86_COMPONENT_KEYS"]=_u147_keys
except Exception:pass

if __name__=="__main__" and "--selftest-quality-fixes" in _u147_sys.argv:
    try:
        _u147_selftest_quality_fixes()
        raise SystemExit(0)
    except Exception as _u147_exc:
        import traceback as _u147_traceback
        print("QUALITY_TESTS_SELFTEST_FAILED:",type(_u147_exc).__name__,str(_u147_exc))
        _u147_traceback.print_exc()
        raise SystemExit(1)
