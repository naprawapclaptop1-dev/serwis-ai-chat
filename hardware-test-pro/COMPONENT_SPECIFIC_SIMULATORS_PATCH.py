# Component-specific simulator rendering. Only CPU/RAM/DYSK/GPU visuals are replaced.
import time as _u150_time
import math as _u150_math
import sys as _u150_sys
import os as _u150_os
import shutil as _u150_shutil
import tkinter as _u150_tk

_U150_COMPONENT_SIMULATORS_VERSION = "1.0.0"
_U150_ORIGINAL_DRAW_COMPONENT_SCENE = _u105_draw_component_scene
_U150_COMPONENT_PROFILES = {
    "CPU": {"title": "PROCESOR / CPU", "subtitle": "PAKIET CPU • RDZENIE • TAKTOWANIE • OBCIĄŻENIE"},
    "RAM": {"title": "PAMIĘĆ RAM", "subtitle": "MODUŁ DIMM • UKŁADY DRAM • ZAJĘTOŚĆ • BUFORY"},
    "DYSK": {"title": "DYSK / SSD / HDD / NVMe", "subtitle": "NOŚNIK • ODCZYT • ZAPIS • WOLNE MIEJSCE"},
    "GPU": {"title": "KARTA GRAFICZNA / GPU", "subtitle": "GPU DIE • VRAM • CHŁODZENIE • CZUJNIKI"},
}


def _u150_number(value):
    if value is None or isinstance(value, bool):
        return None
    try:
        result = float(value)
        return result if _u150_math.isfinite(result) else None
    except Exception:
        return None


def _u150_last_result(app, module):
    results = getattr(app, "results", {}) or {}
    if not isinstance(results, dict):
        return {}
    keys = {
        "CPU": ("CPU_BENCHMARK", "CPU_HASH_BENCHMARK", "CPU_LOAD_BENCHMARK", "CPU"),
        "RAM": ("RAM_BENCHMARK", "RAM"),
        "DYSK": ("DISK_BENCHMARK", "DYSK", "COMPONENT_SCAN_DYSK"),
        "GPU": ("GPU_3D", "3D_SUITE", "GPU", "GPU_WINSAT"),
    }.get(module, ())
    for key in keys:
        item = results.get(key)
        if isinstance(item, dict) and item:
            return item
    return {}


def _u150_live_metrics(app, module):
    now = _u150_time.monotonic()
    cached = getattr(app, "_u150_live_metrics_cache", None)
    if isinstance(cached, dict) and cached.get("module") == module and now - cached.get("sampled_at", 0.0) < 0.75:
        return cached
    out = {
        "module": module, "sampled_at": now, "cpu_percent": None, "per_core_percent": [],
        "cpu_clock_mhz": None, "cpu_temp_c": None,
        "ram_percent": None, "ram_used_gb": None, "ram_total_gb": None, "ram_available_gb": None,
        "disk_read_mib_s": None, "disk_write_mib_s": None,
        "volume": "N/D", "volume_free_gb": None, "volume_total_gb": None, "volume_used_percent": None,
        "gpu_load_percent": None, "gpu_temp_c": None, "gpu_clock_mhz": None,
        "vram_used_mb": None, "vram_total_mb": None, "gpu_name": "N/D",
    }
    p = globals().get("psutil")
    if p is not None:
        try:
            cores = p.cpu_percent(interval=None, percpu=True) or []
            cores = [_u150_number(v) for v in cores]
            out["per_core_percent"] = cores
            valid = [v for v in cores if v is not None]
            if valid:
                out["cpu_percent"] = sum(valid) / len(valid)
        except Exception:
            pass
        try:
            frequency = p.cpu_freq()
            out["cpu_clock_mhz"] = _u150_number(frequency.current) if frequency else None
        except Exception:
            pass
        try:
            memory = p.virtual_memory()
            out.update({
                "ram_percent": _u150_number(memory.percent),
                "ram_used_gb": memory.used / (1024 ** 3),
                "ram_total_gb": memory.total / (1024 ** 3),
                "ram_available_gb": memory.available / (1024 ** 3),
            })
        except Exception:
            pass
        try:
            io = p.disk_io_counters()
            if io is not None:
                previous = getattr(app, "_u150_previous_disk_io", None)
                current = {"time": now, "read": int(io.read_bytes), "write": int(io.write_bytes)}
                if isinstance(previous, dict):
                    elapsed = now - float(previous.get("time", now))
                    if 0.08 <= elapsed <= 5.0:
                        out["disk_read_mib_s"] = max(0, current["read"] - int(previous.get("read", current["read"]))) / elapsed / 1048576
                        out["disk_write_mib_s"] = max(0, current["write"] - int(previous.get("write", current["write"]))) / elapsed / 1048576
                app._u150_previous_disk_io = current
        except Exception:
            pass
        if module == "DYSK":
            try:
                variable = getattr(app, "_u69_disk_drive_var", None)
                volume = str(variable.get() if variable else _u150_os.environ.get("SystemDrive", "C:")).strip()
                if volume:
                    if len(volume) == 2 and volume[1] == ":":
                        volume += "\\"
                    usage = _u150_shutil.disk_usage(volume)
                    out.update({
                        "volume": volume,
                        "volume_free_gb": usage.free / (1024 ** 3),
                        "volume_total_gb": usage.total / (1024 ** 3),
                        "volume_used_percent": 100.0 * usage.used / usage.total if usage.total else None,
                    })
            except Exception:
                pass
    try:
        live = getattr(app, "_live_values", {}) or {}
        if out["cpu_percent"] is None:
            out["cpu_percent"] = _u150_number(live.get("cpu"))
        if out["ram_percent"] is None:
            out["ram_percent"] = _u150_number(live.get("ram"))
    except Exception:
        pass
    try:
        sensor_cache = getattr(app, "_u66_sensor_cache", {}) or {}
        gpu_cache = sensor_cache.get("gpu", {}) if isinstance(sensor_cache, dict) else {}
        temp_cache = sensor_cache.get("temps", {}) if isinstance(sensor_cache, dict) else {}
        telemetry = getattr(app, "_u84_gpu_last_telemetry", {}) or {}
        if not isinstance(gpu_cache, dict): gpu_cache = {}
        if not isinstance(temp_cache, dict): temp_cache = {}
        if not isinstance(telemetry, dict): telemetry = {}
        cached_gpus = getattr(app, "gpus", None)
        gpu_info = primary_gpu(cached_gpus) if cached_gpus and callable(globals().get("primary_gpu")) else {}
        if isinstance(gpu_info, dict):
            out["gpu_name"] = str(gpu_info.get("Name") or gpu_info.get("name") or "N/D")
        out["cpu_temp_c"] = _u150_number(temp_cache.get("cpu_temp_c", sensor_cache.get("cpu_temp_c") if isinstance(sensor_cache, dict) else None))
        out["gpu_load_percent"] = _u150_number(telemetry.get("gpu_load_percent") if telemetry.get("gpu_load_percent") is not None else gpu_cache.get("gpu_load_percent", getattr(app, "_gpu_util", None)))
        out["gpu_temp_c"] = _u150_number(telemetry.get("temperature_c") if telemetry.get("temperature_c") is not None else (telemetry.get("gpu_temp_c") if telemetry.get("gpu_temp_c") is not None else gpu_cache.get("temperature_c", temp_cache.get("gpu_temp_c"))))
        out["gpu_clock_mhz"] = _u150_number(telemetry.get("gpu_clock_mhz") if telemetry.get("gpu_clock_mhz") is not None else gpu_cache.get("gpu_clock_mhz"))
        out["vram_used_mb"] = _u150_number(telemetry.get("vram_used_mb") if telemetry.get("vram_used_mb") is not None else gpu_cache.get("vram_used_mb"))
        out["vram_total_mb"] = _u150_number(telemetry.get("vram_total_mb") if telemetry.get("vram_total_mb") is not None else gpu_cache.get("vram_total_mb"))
    except Exception:
        pass
    out["sampled_at"] = now
    app._u150_live_metrics_cache = out
    return out


def _u150_metric_rows(module, live, result):
    nested = result.get("benchmark") if isinstance(result.get("benchmark"), dict) else {}
    if module == "CPU":
        return [
            ("OBciążenie CPU", live.get("cpu_percent"), "%" ),
            ("Taktowanie CPU", live.get("cpu_clock_mhz"), "MHz"),
            ("Rdzenie / wątki", (len(live.get("per_core_percent") or []) or _u150_os.cpu_count()), "logic."),
            ("Temperatura CPU", live.get("cpu_temp_c"), "°C"),
        ]
    if module == "RAM":
        size = result.get("tested_mb", result.get("size_mb", result.get("buffer_mb", nested.get("size_mb"))))
        write = result.get("write_MiBps", result.get("write_mib_s_overall", nested.get("write_MBps")))
        read = result.get("verify_MiBps", result.get("verify_mib_s_overall", nested.get("read_MBps", nested.get("read_MiBps"))))
        return [
            ("Zajętość RAM", live.get("ram_percent"), "%"),
            ("Dostępne / łącznie", (f"{live['ram_available_gb']:.1f} / {live['ram_total_gb']:.1f} GB" if live.get("ram_available_gb") is not None and live.get("ram_total_gb") is not None else None), ""),
            ("Bufor ostatniego testu", size, "MB"),
            ("Zapis / weryfikacja", (f"{float(write):.1f} / {float(read):.1f}" if _u150_number(write) is not None and _u150_number(read) is not None else None), "MiB/s"),
        ]
    if module == "DYSK":
        bench_read = nested.get("read_bps", nested.get("read_bytes_per_second"))
        bench_write = nested.get("write_bps", nested.get("write_bytes_per_second"))
        read = _u150_number(bench_read) / 1048576 if _u150_number(bench_read) is not None else live.get("disk_read_mib_s")
        write = _u150_number(bench_write) / 1048576 if _u150_number(bench_write) is not None else live.get("disk_write_mib_s")
        return [
            ("Wybrany wolumin", live.get("volume"), ""),
            ("Wolne miejsce", (f"{live['volume_free_gb']:.1f} / {live['volume_total_gb']:.1f} GB" if live.get("volume_free_gb") is not None and live.get("volume_total_gb") is not None else None), ""),
            ("Odczyt", read, "MiB/s"),
            ("Zapis", write, "MiB/s"),
        ]
    return [
        ("Obciążenie GPU", live.get("gpu_load_percent"), "%"),
        ("Temperatura GPU", live.get("gpu_temp_c"), "°C"),
        ("Pamięć VRAM", (f"{live['vram_used_mb']:.0f} / {live['vram_total_mb']:.0f} MB" if live.get("vram_used_mb") is not None and live.get("vram_total_mb") is not None else live.get("vram_used_mb")), "VRAM"),
        ("Średni FPS z renderera", result.get("average_fps", result.get("mean_fps")), "FPS"),
    ]


def _u150_display(value, unit=""):
    if value is None:
        return "N/D"
    if isinstance(value, str):
        return value if value else "N/D"
    try:
        return f"{float(value):,.1f} {unit}".strip()
    except Exception:
        return str(value)


def _u150_draw_component_scene(app):
    canvas = getattr(app, "_u68_sim_canvas", None)
    if canvas is None or not canvas.winfo_exists() or not str(getattr(app, "current_view", "")).startswith("SIM3D_"):
        return
    module = str(app.current_view).replace("SIM3D_", "").upper()
    if module not in _U150_COMPONENT_PROFILES:
        return _U150_ORIGINAL_DRAW_COMPONENT_SCENE(app)
    try:
        width = max(640, int(canvas.winfo_width() or 1000))
        height = max(260, int(canvas.winfo_height() or 320))
        canvas.delete("all")
        canvas.configure(bg="#06101c", highlightthickness=0, bd=0)
        angle = float(getattr(app, "_u68_sim_angle", 0.0))
        live = _u150_live_metrics(app, module)
        result = _u150_last_result(app, module)
        profile = _U150_COMPONENT_PROFILES[module]
        colors = {
            "bg": "#06101c", "panel": "#0b1a2a", "panel_edge": "#1e3a51",
            "grid": "#102538", "cyan": "#22d3ee", "blue": "#2188ff",
            "purple": "#b36bff", "green": "#27d99b", "amber": "#f3bd55",
            "silver": "#9fb7cb", "white": "#edf7ff", "muted": "#8caac0",
            "board": "#102e40", "dark": "#0c1726",
        }
        for x in range(0, width, 42):
            canvas.create_line(x, 0, x, height, fill=colors["grid"], width=1)
        for y in range(0, height, 32):
            canvas.create_line(0, y, width, y, fill=colors["grid"], width=1)
        canvas.create_text(16, 12, text=profile["title"], anchor="nw", fill=colors["white"], font=("Segoe UI", 10, "bold"))
        canvas.create_text(width - 16, 12, text="WIZUALIZACJA DEDYKOWANA • ODCZYTY LIVE", anchor="ne", fill=colors["cyan"], font=("Segoe UI", 8, "bold"))
        canvas.create_text(16, 31, text=profile["subtitle"], anchor="nw", fill=colors["muted"], font=("Segoe UI", 7, "bold"))
        canvas.create_line(16, 50, width - 16, 50, fill=colors["panel_edge"], width=1)

        # The component silhouette uses a small perspective projection. All model faces
        # are polygons/lines; they are intentionally different for CPU, RAM, disk and GPU.
        model_cx = width * 0.285
        model_cy = height * 0.53
        unit = min(height * 0.16, width * 0.075)
        cosine = _u150_math.cos(angle * 0.55)
        sine = _u150_math.sin(angle * 0.55)

        def project(point):
            x, y, z = point
            rx = x * cosine - z * sine
            rz = x * sine + z * cosine
            perspective = 1.0 / max(0.62, 1.0 + rz * 0.045)
            return (model_cx + rx * unit * perspective, model_cy - y * unit * perspective + rz * unit * 0.16 * perspective)

        def poly(points, fill, outline=None, line_width=1):
            coords = []
            for point in points:
                coords.extend(project(point))
            canvas.create_polygon(*coords, fill=fill, outline=outline or fill, width=line_width, smooth=False)

        def path(points, color, line_width=1, dash=None):
            coords = []
            for point in points:
                coords.extend(project(point))
            options = {"fill": color, "width": line_width, "smooth": True, "splinesteps": 10}
            if dash:
                options["dash"] = dash
            canvas.create_line(*coords, **options)

        def box(cx, cy, cz, sx, sy, sz, fill, edge):
            x1, x2 = cx - sx/2, cx + sx/2
            y1, y2 = cy - sy/2, cy + sy/2
            z1, z2 = cz - sz/2, cz + sz/2
            poly([(x1,y2,z1),(x2,y2,z1),(x2,y2,z2),(x1,y2,z2)], fill, edge, 1)
            poly([(x1,y1,z2),(x2,y1,z2),(x2,y2,z2),(x1,y2,z2)], "#07131f", edge, 1)
            poly([(x2,y1,z1),(x2,y1,z2),(x2,y2,z2),(x2,y2,z1)], "#142237", edge, 1)

        def ring(cx, cy, cz, radius, color, line_width=2, phase=0.0, segments=48):
            pts = []
            for i in range(segments + 1):
                a = 2 * _u150_math.pi * i / segments + phase
                pts.append((cx + radius * _u150_math.cos(a), cy, cz + radius * _u150_math.sin(a)))
            path(pts, color, line_width)

        def chip(cx, cy, cz, sx, sz, text, edge):
            box(cx, cy, cz, sx, 0.12, sz, "#15283e", edge)
            ring(cx, cy + .08, cz, min(sx, sz) * .20, edge, 1, angle, 22)
            for k in range(4):
                x = cx - sx * .32 + k * sx * .21
                path([(x,cy+.07,cz-sz*.60),(x,cy+.07,cz-sz*.48)], colors["amber"], 1)
            # Chip text is drawn outside the projected polygon in the dashboard for legibility.

        def fan(cx, cz, radius, phase):
            ring(cx, .16, cz, radius, colors["cyan"], 2, 0, 52)
            ring(cx, .18, cz, radius * .78, colors["panel_edge"], 1, 0, 48)
            for blade in range(8):
                a = phase + blade * 2 * _u150_math.pi / 8
                p1 = (cx + radius*.16*_u150_math.cos(a), .21, cz + radius*.16*_u150_math.sin(a))
                p2 = (cx + radius*.78*_u150_math.cos(a+.22), .21, cz + radius*.78*_u150_math.sin(a+.22))
                p3 = (cx + radius*.55*_u150_math.cos(a+1.02), .21, cz + radius*.55*_u150_math.sin(a+1.02))
                poly([p1,p2,p3], "#15556b", colors["blue"], 1)
            ring(cx, .23, cz, radius*.13, colors["silver"], 2, phase, 24)

        def screen_box(x1, y1, x2, y2, fill, edge=None):
            canvas.create_polygon(x1,y1,x2,y1,x2,y2,x1,y2,fill=fill,outline=edge or fill,width=1)

        def tint(percent):
            value = _u150_number(percent)
            if value is None:
                return "#20374b"
            if value >= 85:
                return "#a73b55"
            if value >= 60:
                return "#95622b"
            if value >= 30:
                return "#1b8290"
            return "#166b68"

        # Four unique device models: CPU package/core array, DIMM memory stick,
        # storage controller/flash and platter icon, and triple-fan discrete GPU.
        if module == "CPU":
            box(0, -.10, 0, 3.55, .28, 3.0, "#253d53", colors["silver"])
            box(0, .10, 0, 3.10, .22, 2.60, "#12263c", colors["cyan"])
            box(0, .24, 0, 2.30, .10, 2.00, "#493767", colors["purple"])
            box(0, .31, 0, 2.08, .08, 1.78, "#0d1b2e", colors["silver"])
            for i in range(13):
                pos = -1.40 + i * .235
                path([(pos,-.22,-1.62),(pos,-.22,-1.85)], colors["amber"], 2)
                path([(pos,-.22,1.62),(pos,-.22,1.85)], colors["amber"], 2)
                path([(-1.82,-.22,pos),( -1.58,-.22,pos)], colors["amber"], 2)
                path([(1.58,-.22,pos),(1.82,-.22,pos)], colors["amber"], 2)
            cores = live.get("per_core_percent") or []
            core_values = []
            for i in range(16):
                row, col = divmod(i, 4)
                x = model_cx - 47 + col * 31
                y = model_cy - 45 + row * 27
                value = _u150_number(cores[i]) if i < len(cores) else None
                core_values.append(value)
                screen_box(x, y, x+26, y+21, tint(value), colors["cyan"] if (int(angle*10)+i)%4==0 else colors["panel_edge"])
                canvas.create_text(x+13, y+7, text=f"C{i+1:02d}", fill=colors["white"], font=("Segoe UI", 6, "bold"))
                canvas.create_text(x+13, y+16, text=(f"{value:.0f}%" if value is not None else "N/D"), fill=colors["white"], font=("Segoe UI", 6))
            canvas.create_text(model_cx, model_cy + unit*1.25, text=f"CPU • {len(cores) or (_u150_os.cpu_count() or 0)} WĄTKÓW", fill=colors["cyan"], font=("Segoe UI", 8, "bold"))
        elif module == "RAM":
            box(0, -.08, 0, 5.35, .22, 1.18, "#063b37", colors["green"])
            box(0, .06, 0, 5.12, .09, .89, "#0d5a50", colors["cyan"])
            for i in range(8):
                x = -2.12 + i*.605
                edge = colors["purple"] if int(angle*2)%8 == i else colors["blue"]
                chip(x, .18, 0, .42, .62, f"D{i+1}", edge)
                for z in (-.48,.48):
                    path([(x,.01,z),(x,.04,z*.92)], colors["green"], 1)
            for i in range(30):
                x = -2.48 + i*.171
                path([(x,-.20,.62),(x,-.20,.82)], colors["amber"], 2)
            for z in (-.30,-.10,.10,.30):
                path([(-2.43,.01,z),(2.43,.01,z)], "#147b72", 1)
            canvas.create_text(model_cx, model_cy + unit*.88, text="DIMM • 8 UKŁADÓW DRAM", fill=colors["cyan"], font=("Segoe UI", 8, "bold"))
        elif module == "DYSK":
            box(0, -.10, 0, 5.30, .25, 1.70, "#15283d", colors["silver"])
            box(0, .04, 0, 5.03, .10, 1.48, "#0b1a2b", colors["cyan"])
            # Controller plus flash packages on a storage card; the platter inset is illustrative only.
            chip(-1.45, .14, -.04, .56, .62, "CTRL", colors["purple"])
            for i in range(4):
                x = -.52 + i*.67
                chip(x, .14, -.10, .48, .73, f"NAND{i+1}", colors["blue"] if i%2 else colors["green"])
            ring(1.55, .20, -.02, .48, colors["silver"], 2, angle*1.8, 50)
            ring(1.55, .22, -.02, .29, colors["blue"], 2, -angle*2.1, 44)
            ring(1.55, .24, -.02, .11, colors["amber"], 2, angle*2.7, 34)
            path([(1.15,.21,.05),(1.45,.21,.30),(1.77,.21,.34)], colors["amber"], 2)
            node = (1.77,.23,.34)
            canvas.create_oval(model_cx + unit*1.78, model_cy - unit*.25, model_cx + unit*1.78+8, model_cy-unit*.25+8, fill=colors["white"], outline="")
            for i in range(22):
                x = -2.3 + i*.21
                path([(x,-.23,.82),(x,-.23,1.0)], colors["amber"], 2)
            canvas.create_text(model_cx, model_cy + unit*.74, text="NOŚNIK • NAND / KONTROLER / ŚCIEŻKI", fill=colors["cyan"], font=("Segoe UI", 8, "bold"))
        elif module == "GPU":
            box(0, -.10, 0, 5.65, .26, 2.32, "#13283c", colors["cyan"])
            box(0, .05, 0, 5.38, .12, 2.08, "#0a3d48", "#247d8d")
            chip(0, .26, -.06, .98, .83, "GPU", colors["purple"])
            for x in (-1.83,-1.10,1.10,1.83):
                chip(x, .18, -.70, .45, .39, "VRAM", colors["blue"])
                chip(x, .18, .70, .45, .39, "VRAM", colors["blue"])
            for x in (-1.72,0,1.72):
                fan(x, -.02, .58, angle * (1.2 if x else -1.45))
            for i in range(28):
                x = -2.52 + i*.187
                path([(x,-.23,1.14),(x,-.23,1.38)], colors["amber"], 2)
            canvas.create_text(model_cx, model_cy + unit*1.18, text="KARTA GRAFICZNA • GPU + VRAM + 3 WENTYLATORY", fill=colors["cyan"], font=("Segoe UI", 8, "bold"))

        # Right-hand values use Windows/driver readings or a genuine completed test report only.
        panel_x = width * .565
        panel_right = width - 14
        panel_top = 62
        canvas.create_line(panel_x-10, 58, panel_x-10, height-29, fill=colors["panel_edge"], width=1)
        canvas.create_text(panel_x, panel_top, text="RZECZYWISTE DANE • NIE WARTOŚCI DEMO", anchor="nw", fill=colors["white"], font=("Segoe UI", 8, "bold"))
        rows = _u150_metric_rows(module, live, result)
        card_h = max(38, min(47, (height - panel_top - 55) / max(1, len(rows))))
        for index, (caption, value, unit_label) in enumerate(rows):
            top = panel_top + 22 + index * (card_h + 3)
            bottom = min(height - 34, top + card_h)
            screen_box(panel_x, top, panel_right, bottom, colors["panel"], colors["panel_edge"])
            canvas.create_text(panel_x+9, top+5, text=caption.upper(), anchor="nw", fill=colors["muted"], font=("Segoe UI", 7, "bold"))
            shown = _u150_display(value, unit_label)
            canvas.create_text(panel_x+9, top+21, text=shown[:58], anchor="nw", fill=colors["cyan"] if value is not None else colors["amber"], font=("Segoe UI", 9, "bold"))
            val = _u150_number(value)
            if unit_label == "%" and val is not None:
                bar_left = panel_right - 100
                screen_box(bar_left, top+24, panel_right-8, top+31, "#14283b", "#14283b")
                x_end = bar_left + (panel_right-8-bar_left)*max(0,min(100,val))/100
                screen_box(bar_left, top+24, x_end, top+31, tint(val), tint(val))
        test_state = str(result.get("state") or "BRAK POMIARU").upper()
        note = "OSTATNI TEST: " + test_state + (" • WYNIK Z RAPORTU" if result else " • NA RAZIE BRAK WYNIKU")
        canvas.create_line(16, height-28, width-16, height-28, fill=colors["panel_edge"], width=1)
        canvas.create_text(16, height-18, text=note, anchor="w", fill=colors["green"] if test_state in ("GOOD","PASS","OK") else colors["amber"], font=("Segoe UI", 7, "bold"))
        canvas.create_text(width-16, height-18, text="MODEL SCHEMATYCZNY • POMIARY Z CZUJNIKÓW / TESTU", anchor="e", fill=colors["muted"], font=("Segoe UI", 7))

        app._u68_sim_angle = angle + 0.035
        if not getattr(app, "_u150_animation_pending", False):
            app._u150_animation_pending = True
            try:
                app._u150_animation_after_id = app.after(90, lambda: _u150_animation_tick(app))
            except Exception:
                app._u150_animation_pending = False
    except Exception as exc:
        try:
            app.queue_log("Symulator dedykowany " + module + ": " + repr(exc))
        except Exception:
            pass


def _u150_animation_tick(app):
    app._u150_animation_pending = False
    if not str(getattr(app, "current_view", "")).startswith("SIM3D_"):
        return
    _u150_draw_component_scene(app)
def _u150_selftest_component_specific_simulators():
    assert _U150_COMPONENT_SIMULATORS_VERSION == "1.0.0"
    assert set(_U150_COMPONENT_PROFILES) == {"CPU","RAM","DYSK","GPU"}
    titles = [item["title"] for item in _U150_COMPONENT_PROFILES.values()]
    assert len(set(titles)) == 4
    for module in ("CPU","RAM","DYSK","GPU"):
        assert callable(_u150_number) and callable(_u150_metric_rows)
        assert _u150_metric_rows(module, {}, {}) and all(
            isinstance(row, tuple) and len(row) == 3 for row in _u150_metric_rows(module, {}, {})
        )
    empty_cpu = _u150_metric_rows("CPU", {}, {})
    empty_gpu = _u150_metric_rows("GPU", {}, {})
    assert empty_cpu[0][1] is None and empty_cpu[1][1] is None and empty_cpu[3][1] is None
    assert empty_cpu[2][1] is None or isinstance(empty_cpu[2][1], (int, float, str))
    assert all(value is None for _caption,value,_unit in empty_gpu)
    names = _u105_recursive_code_names(_u150_draw_component_scene.__code__)
    assert "create_polygon" in names and "create_oval" in names and "create_line" in names
    assert "create_rectangle" not in names, "Component model must use dedicated polygon/line renderers."
    assert all(name in names for name in ("project","poly","path","ring","fan","chip"))
    assert callable(_u150_animation_tick)
    print("COMPONENT_SPECIFIC_SIMULATORS_SELFTEST_OK: CPU core package, DIMM RAM, disk storage model and triple-fan GPU; no demo measurements")


_u105_draw_component_scene = _u150_draw_component_scene
_u68_draw_component_scene = _u150_draw_component_scene


if __name__ == "__main__" and "--selftest-component-specific-simulators" in _u150_sys.argv:
    try:
        _u150_selftest_component_specific_simulators()
        raise SystemExit(0)
    except Exception as _u150_exc:
        import traceback as _u150_traceback
        print("COMPONENT_SPECIFIC_SIMULATORS_SELFTEST_FAILED:", type(_u150_exc).__name__, str(_u150_exc))
        _u150_traceback.print_exc()
        raise SystemExit(1)
