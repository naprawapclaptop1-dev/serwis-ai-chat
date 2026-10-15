# Prepare a new globally distributable build: version bump, 125 themes, icon hover glow.
$ErrorActionPreference = "Stop"
$sourcePath = Join-Path $PSScriptRoot "NaprawaPC_Hardware_Test_PRO.pyw"
$setupPath = Join-Path $PSScriptRoot "SUITE_SETUP.iss"
$manifestPath = Join-Path $PSScriptRoot "..\updates\hardware-test-pro\latest.json"
foreach ($p in @($sourcePath,$setupPath,$manifestPath)) { if (!(Test-Path -LiteralPath $p)) { throw "Missing required file: $p" } }
$manifest = [IO.File]::ReadAllText($manifestPath,[Text.Encoding]::UTF8) | ConvertFrom-Json
if (!$manifest.release_ready -or [string]$manifest.version -notmatch '^\d+\.\d+\.\d+$') { throw "Latest update manifest is not a valid published release." }
$v = [version]$manifest.version
$next = "{0}.{1}.{2}" -f $v.Major,$v.Minor,($v.Build+1)
$setupName = "NAPRAWA-PC-HARDWARE-TEST-PRO-Setup-$next.exe"
$src = [IO.File]::ReadAllText($sourcePath,[Text.Encoding]::UTF8)
$vm = [regex]::Matches($src,'(?m)^VERSION = "(?<v>\d+\.\d+\.\d+) (?<d>[^"]*)"$')
if ($vm.Count -eq 0) { throw "Cannot find application VERSION assignment." }
$last = $vm[$vm.Count-1]
$newLine = 'VERSION = "' + $next + ' ' + $last.Groups["d"].Value + '"'
$src = $src.Substring(0,$last.Index) + $newLine + $src.Substring($last.Index+$last.Length)

if (!$src.Contains("# _U443_THEME_PACK")) {
$theme = @'
# _U443_THEME_PACK — 115 additional selectable palettes
import colorsys as _u443_cs
_U443_PREFIX = ("NEON","DARK","DEEP","ULTRA","FUTURE","CYBER","LASER","ARCTIC","NIGHT","TITAN","QUANTUM","COSMIC","STEALTH","PRO","ELECTRIC","SILK","NOVA","NEXUS","ORBIT","PHOTON","TURBO","HYPER","AURORA")
_U443_SUFFIX = ("OCEAN BLUE","VIOLET","MATRIX GREEN","BLACK GOLD","CRIMSON")
_U443_HUES = (0.56,0.76,0.36,0.12,0.99)
_U443_SKIN_PROFILES = (
    {"name":"NEON GLASS","panel_relief":"flat","panel_bd":0,"panel_highlight":2,"button_relief":"flat","button_overrelief":"ridge","button_bd":0,"font":"Segoe UI","image":"neon","layout":"sidebar","scanlines":False},
    {"name":"CARBON LAYER","panel_relief":"groove","panel_bd":2,"panel_highlight":1,"button_relief":"raised","button_overrelief":"ridge","button_bd":1,"font":"Bahnschrift","image":"carbon","layout":"topbar","scanlines":False},
    {"name":"CYBER ANGULAR","panel_relief":"solid","panel_bd":1,"panel_highlight":2,"button_relief":"flat","button_overrelief":"raised","button_bd":1,"font":"Segoe UI","image":"angular","layout":"grid","scanlines":False},
    {"name":"MATRIX TERMINAL","panel_relief":"ridge","panel_bd":1,"panel_highlight":1,"button_relief":"raised","button_overrelief":"ridge","button_bd":1,"font":"Consolas","image":"matrix","layout":"terminal","scanlines":True},
    {"name":"ICE MINIMAL","panel_relief":"flat","panel_bd":0,"panel_highlight":1,"button_relief":"flat","button_overrelief":"raised","button_bd":0,"font":"Segoe UI","image":"ice","layout":"topbar","scanlines":False},
    {"name":"VIOLET HOLOGRAM","panel_relief":"ridge","panel_bd":2,"panel_highlight":2,"button_relief":"raised","button_overrelief":"ridge","button_bd":1,"font":"Bahnschrift","image":"hologram","layout":"sidebar","scanlines":False},
    {"name":"RED GAMING","panel_relief":"solid","panel_bd":2,"panel_highlight":2,"button_relief":"raised","button_overrelief":"raised","button_bd":2,"font":"Segoe UI","image":"redline","layout":"grid","scanlines":False},
    {"name":"AMBER INDUSTRIAL","panel_relief":"groove","panel_bd":2,"panel_highlight":1,"button_relief":"groove","button_overrelief":"raised","button_bd":1,"font":"Consolas","image":"amber","layout":"terminal","scanlines":True},
    {"name":"STEEL PRO","panel_relief":"ridge","panel_bd":2,"panel_highlight":1,"button_relief":"ridge","button_overrelief":"raised","button_bd":1,"font":"Segoe UI","image":"steel","layout":"topbar","scanlines":False},
    {"name":"CARBON SCANLINE","panel_relief":"sunken","panel_bd":1,"panel_highlight":1,"button_relief":"raised","button_overrelief":"ridge","button_bd":1,"font":"Consolas","image":"carbon","layout":"terminal","scanlines":True},
    {"name":"AURORA LAYER","panel_relief":"flat","panel_bd":0,"panel_highlight":3,"button_relief":"flat","button_overrelief":"ridge","button_bd":0,"font":"Bahnschrift","image":"aurora","layout":"sidebar","scanlines":False},
    {"name":"RETRO HUD","panel_relief":"groove","panel_bd":2,"panel_highlight":1,"button_relief":"raised","button_overrelief":"sunken","button_bd":2,"font":"Consolas","image":"retro","layout":"grid","scanlines":True},
)
def _u443_hex(h,l,s):
    rgb = _u443_cs.hls_to_rgb(h % 1.0,l,s)
    return "#" + "".join(f"{round(x*255):02x}" for x in rgb)
for _u443_tid in range(11,126):
    _u443_i = _u443_tid-11
    _u443_family = _u443_i // 5
    _u443_group = _u443_i % 5
    _u443_hue = (_U443_HUES[_u443_group] + _u443_family*0.0137) % 1.0
    _u443_light = (_u443_i % 17 == 0)
    if _u443_light:
        _u443_bg = _u443_hex(_u443_hue,0.965,0.16)
        _u443_panel = "#ffffff"
        _u443_card = _u443_hex(_u443_hue,0.925,0.22)
        _u443_fg,_u443_muted = "#152033","#5e6d80"
        _u443_accent = _u443_hex(_u443_hue,0.39,0.88)
        _u443_accent2 = _u443_hex(_u443_hue,0.53,0.82)
    else:
        _u443_bg = _u443_hex(_u443_hue,0.055+(_u443_family%3)*0.012,0.48)
        _u443_panel = _u443_hex(_u443_hue,0.085+(_u443_family%3)*0.012,0.50)
        _u443_card = _u443_hex(_u443_hue,0.125+(_u443_family%3)*0.012,0.52)
        _u443_fg,_u443_muted = "#edf7ff","#93a9bd"
        _u443_accent = _u443_hex(_u443_hue,0.60,0.98)
        _u443_accent2 = _u443_hex(_u443_hue,0.77,0.90)
    THEMES[_u443_tid] = {
        "name": f"{_U443_SKIN_PROFILES[_u443_family % len(_U443_SKIN_PROFILES)]['name']} • {_U443_SUFFIX[_u443_group]} • {_u443_tid:03d}",
        "bg": _u443_bg,"panel": _u443_panel,"card": _u443_card,
        "fg": _u443_fg,"muted": _u443_muted,
        "accent": _u443_accent,"accent2": _u443_accent2,
        "good": _u443_hex(0.37,0.55,0.78),
        "warn": _u443_hex(0.12,0.60,0.86),
        "bad": _u443_hex(0.99,0.59,0.88),
    }
for _u443_tid, _u443_theme in THEMES.items():
    _u443_prof = _U443_SKIN_PROFILES[(_u443_tid - 1) % len(_U443_SKIN_PROFILES)]
    _u443_theme["_skin_family"] = _u443_prof["name"]
    _u443_theme["_skin_id"] = (_u443_tid - 1) % len(_U443_SKIN_PROFILES)
    _u443_theme["_panel_relief"] = _u443_prof["panel_relief"]
    _u443_theme["_panel_bd"] = _u443_prof["panel_bd"]
    _u443_theme["_panel_highlight"] = _u443_prof["panel_highlight"]
    _u443_theme["_button_relief"] = _u443_prof["button_relief"]
    _u443_theme["_button_overrelief"] = _u443_prof["button_overrelief"]
    _u443_theme["_button_bd"] = _u443_prof["button_bd"]
    _u443_theme["_font_family"] = _u443_prof["font"]
    _u443_theme["_image_style"] = _u443_prof["image"]
    _u443_theme["_skin_layout"] = _u443_prof["layout"]
    _u443_theme["_scanlines"] = _u443_prof["scanlines"]
'@
    $pattern = '(?m)^\}\r?\n\r?\nMODULES = \['
    if ($src -notmatch $pattern) { throw "Cannot find base theme palette insertion point." }
    $src = [regex]::Replace($src,$pattern,[System.Text.RegularExpressions.MatchEvaluator]{
        param($m)
        return "}" + [Environment]::NewLine + [Environment]::NewLine + $theme + [Environment]::NewLine + "MODULES = ["
    },1)
}
$src = [regex]::Replace($src,'range\(\s*1\s*,\s*11\s*\)','range(1,126)')
$src = $src.Replace("10 STYLOW","125 STYLOW").Replace("10 STYLI","125 STYLI")

if (!$src.Contains("# _U443_ICON_HOVER_GLOW")) {
$hover = @'
# _U443_ICON_HOVER_GLOW — bind glow to real controls each time a view is rebuilt
def _u443_bind_hover_glow(root, app):
    try:
        t=app.colors(); accent=t.get("accent","#1aa7ff"); accent2=t.get("accent2","#55d8ff")
        widgets=root.winfo_children()
    except Exception:
        return
    for w in widgets:
        try:
            if not getattr(w,"_u443_hover_bound",False):
                if isinstance(w,tk.Button):
                    normal={"bg":w.cget("bg"),"fg":w.cget("fg"),"highlightthickness":w.cget("highlightthickness"),"highlightbackground":w.cget("highlightbackground"),"highlightcolor":w.cget("highlightcolor")}
                    def enter(event,ww=w,aa=accent,aa2=accent2):
                        try:
                            if str(ww.cget("state"))!="disabled": ww.configure(bg=aa,fg="#ffffff",highlightbackground=aa2,highlightcolor=aa2,highlightthickness=2)
                        except Exception: pass
                    def leave(event,ww=w,nn=normal):
                        try: ww.configure(**nn)
                        except Exception: pass
                    w.bind("<Enter>",enter,add="+"); w.bind("<Leave>",leave,add="+"); w._u443_hover_bound=True
                elif isinstance(w,ttk.Button):
                    oldstyle=w.cget("style"); st=ttk.Style(app)
                    st.configure("NaprawaPCHover.TButton",background=accent,foreground="#ffffff")
                    st.map("NaprawaPCHover.TButton",background=[("active",accent2),("pressed",accent)])
                    w.bind("<Enter>",lambda e,ww=w: ww.configure(style="NaprawaPCHover.TButton"),add="+")
                    w.bind("<Leave>",lambda e,ww=w,ss=oldstyle: ww.configure(style=ss),add="+"); w._u443_hover_bound=True
                elif isinstance(w,tk.Label):
                    txt=str(w.cget("text") or "").strip()
                    is_icon=bool(txt) and len(txt)<=4 and any(ord(ch)>=0x2300 for ch in txt)
                    if is_icon or str(w.cget("cursor")) in ("hand","hand2"):
                        fg,bg=w.cget("fg"),w.cget("bg")
                        def enter_label(e,ww=w,aa=accent2,bb=accent):
                            try:
                                ww.configure(fg=aa)
                                if str(ww.cget("cursor")) in ("hand","hand2"): ww.configure(bg=bb)
                            except Exception: pass
                        def leave_label(e,ww=w,ff=fg,bbg=bg):
                            try: ww.configure(fg=ff,bg=bbg)
                            except Exception: pass
                        w.bind("<Enter>",enter_label,add="+"); w.bind("<Leave>",leave_label,add="+"); w._u443_hover_bound=True
                elif isinstance(w,tk.Canvas) and str(w.cget("cursor")) in ("hand","hand2"):
                    thick,bg=w.cget("highlightthickness"),w.cget("highlightbackground")
                    w.bind("<Enter>",lambda e,ww=w,aa=accent2: ww.configure(highlightbackground=aa,highlightcolor=aa,highlightthickness=2),add="+")
                    w.bind("<Leave>",lambda e,ww=w,tt=thick,bb=bg: ww.configure(highlightthickness=tt,highlightbackground=bb,highlightcolor=bb),add="+"); w._u443_hover_bound=True
        except Exception: pass
        try: _u443_bind_hover_glow(w,app)
        except Exception: pass

def _u443_schedule_hover(app):
    try: app.after_idle(lambda: _u443_bind_hover_glow(app,app))
    except Exception: pass
_U443_OLD_CLEAR=getattr(AppV43,"clear",None)
if callable(_U443_OLD_CLEAR):
    def _u443_clear_hook(self,*args,**kwargs):
        result=_U443_OLD_CLEAR(self,*args,**kwargs)
        _u443_schedule_hover(self)
        return result
    AppV43.clear=_u443_clear_hook
_U443_OLD_INIT=AppV43.__init__
def _u443_init_hook(self,*args,**kwargs):
    _U443_OLD_INIT(self,*args,**kwargs)
    try: self.after(350,lambda:_u443_bind_hover_glow(self,self))
    except Exception: pass
AppV43.__init__=_u443_init_hook

# Dashboard controls can be recreated on resize; rebind hover glow on each re-creation.
def _u443_wrap_hover_refresh(original):
    def _wrapped(self,*args,**kwargs):
        result=original(self,*args,**kwargs)
        _u443_schedule_hover(self)
        return result
    _wrapped._u443_hover_wrapper=True
    return _wrapped

for _u443_method_name in ("_install_dashboard_controls","_v4321_bind_canvas_router","_v4323_bind_canvas_router","_v4325_install_dashboard_controls"):
    _u443_method=getattr(AppV43,_u443_method_name,None)
    if callable(_u443_method) and not getattr(_u443_method,"_u443_hover_wrapper",False):
        setattr(AppV43,_u443_method_name,_u443_wrap_hover_refresh(_u443_method))

# _U443_TRUE_SKINS — panel shape/depth, typography, real dashboard filters and hover-image controls.
for _u443_tid, _u443_theme in THEMES.items():
    _u443_theme.setdefault("_skin_family", _U443_SKIN_PROFILES[(_u443_tid-1)%len(_U443_SKIN_PROFILES)]["name"])
    _u443_theme.setdefault("_skin_id", (_u443_tid-1)%len(_U443_SKIN_PROFILES))
    _u443_profile = _U443_SKIN_PROFILES[_u443_theme["_skin_id"]]
    for _u443_key, _u443_profile_key in (("_panel_relief","panel_relief"),("_panel_bd","panel_bd"),("_panel_highlight","panel_highlight"),("_button_relief","button_relief"),("_button_overrelief","button_overrelief"),("_button_bd","button_bd"),("_font_family","font"),("_image_style","image"),("_skin_layout","layout"),("_scanlines","scanlines")):
        _u443_theme.setdefault(_u443_key, _u443_profile[_u443_profile_key])

_U443_ORIG_PANEL = AppV43.panel
def _u443_panel_skin(self, parent, bg=None, accent=True):
    frame = _U443_ORIG_PANEL(self, parent, bg, accent)
    t = self.colors()
    try:
        frame.configure(relief=t.get("_panel_relief","flat"), bd=int(t.get("_panel_bd",0)),
                        highlightthickness=int(t.get("_panel_highlight",1)),
                        highlightbackground=t.get("accent","#1aa7ff") if accent else t.get("panel","#0b1c30"),
                        highlightcolor=t.get("accent2","#55d8ff"))
    except Exception: pass
    return frame
AppV43.panel = _u443_panel_skin

_U443_ORIG_MAKE_BUTTON = AppV43.make_button
def _u443_make_button_skin(self, parent, text, command, kind="card", side=None, fill=None, ipady=8):
    button = _U443_ORIG_MAKE_BUTTON(self, parent, text, command, kind, side, fill, ipady)
    t = self.colors()
    try:
        button.configure(relief=t.get("_button_relief","flat"), overrelief=t.get("_button_overrelief","raised"),
                         bd=int(t.get("_button_bd",0)), highlightthickness=1 if int(t.get("_button_bd",0)) else 0,
                         highlightbackground=t.get("accent","#1aa7ff"), highlightcolor=t.get("accent2","#55d8ff"),
                         activebackground=t.get("accent2","#55d8ff"), activeforeground="#ffffff", cursor="hand2")
    except Exception: pass
    return button
AppV43.make_button = _u443_make_button_skin

_U443_ORIG_FNT = AppV43.fnt
def _u443_skin_font(self, size=10, weight="normal"):
    t = self.colors()
    family = t.get("_font_family","Segoe UI")
    key = ("_u443_skin_font", int(size), str(weight), family)
    try:
        if key not in self.fonts:
            self.fonts[key] = tkfont.Font(family=family, size=int(size), weight=str(weight))
        return self.fonts[key]
    except Exception:
        return _U443_ORIG_FNT(self, size, weight)
AppV43.fnt = _u443_skin_font

def _u443_apply_ttk_skin(self):
    try:
        t=self.colors()
        st=ttk.Style(self)
        try: st.theme_use("clam")
        except Exception: pass
        st.configure("TCombobox",fieldbackground=t["card"],background=t["panel"],foreground=t["fg"],arrowcolor=t["accent"],bordercolor=t["accent"],padding=5)
        st.map("TCombobox",fieldbackground=[("readonly",t["card"]),("focus",t["panel"])],foreground=[("readonly",t["fg"])],background=[("active",t["accent"])])
        st.configure("TNotebook",background=t["bg"],borderwidth=int(t.get("_panel_bd",0)))
        st.configure("TNotebook.Tab",background=t["card"],foreground=t["fg"],padding=(12,7),borderwidth=int(t.get("_button_bd",0)))
        st.map("TNotebook.Tab",background=[("selected",t["accent"]),("active",t["accent2"])],foreground=[("selected","#ffffff"),("active","#ffffff")])
        st.configure("Treeview",background=t["card"],fieldbackground=t["card"],foreground=t["fg"],borderwidth=int(t.get("_panel_bd",0)),rowheight=23 if t.get("_skin_layout")=="terminal" else 28)
        st.map("Treeview",background=[("selected",t["accent"])],foreground=[("selected","#ffffff")])
        st.configure("Treeview.Heading",background=t["panel"],foreground=t["accent"],relief=t.get("_panel_relief","flat"),borderwidth=int(t.get("_panel_bd",0)))
        st.map("Treeview.Heading",background=[("active",t["accent"])],foreground=[("active","#ffffff")])
        st.configure("Horizontal.TProgressbar",background=t["accent"],troughcolor=t["card"],bordercolor=t["accent"],lightcolor=t["accent2"],darkcolor=t["panel"],thickness=12 if t.get("_skin_layout")=="terminal" else 16)
    except Exception: pass

_U443_ORIG_BUILD_SHELL = AppV43._build_shell
def _u443_build_shell_skin(self,*args,**kwargs):
    result=_U443_ORIG_BUILD_SHELL(self,*args,**kwargs)
    _u443_apply_ttk_skin(self)
    try: self.after_idle(lambda:_u443_bind_hover_glow(self,self))
    except Exception: pass
    return result
AppV43._build_shell = _u443_build_shell_skin

# Render different dashboard treatments: duotone, scanlines, contrasting card frames and alternate header treatments.
def _u443_skin_dashboard_image(app):
    try:
        from PIL import Image as _I, ImageOps as _IO, ImageEnhance as _IE, ImageDraw as _ID
        base=app._load_reference_base()
        if base is None: return None
        t=app.colors(); style=t.get("_image_style","neon")
        key=(int(app.theme_id),base.size)
        cache=getattr(app,"_u443_skin_image_cache",{})
        if key in cache: return cache[key]
        im=base.convert("RGB")
        gray=_IO.autocontrast(_IO.grayscale(im))
        if style=="matrix":
            im=_IO.colorize(gray,black="#020b05",mid="#12451c",white="#90ffab")
        elif style=="ice":
            im=_IO.colorize(gray,black="#071b36",mid="#6faddb",white="#f0fbff")
        elif style=="hologram":
            im=_IO.colorize(gray,black="#140626",mid="#542c85",white="#e5d7ff")
        elif style=="redline":
            im=_IO.colorize(gray,black="#16060a",mid="#7b1024",white="#ffb2bd")
        elif style=="amber":
            im=_IO.colorize(gray,black="#1b1104",mid="#845018",white="#ffe5a0")
        elif style=="steel":
            im=_IO.colorize(gray,black="#06121c",mid="#526a7d",white="#edf5fc")
        elif style=="retro":
            im=_IO.colorize(gray,black="#1b0b02",mid="#8a3d08",white="#ffdf9a")
        elif style=="carbon":
            im=_IE.Contrast(_IE.Color(im).enhance(0.22)).enhance(1.28)
            im=_I.blend(im,_I.new("RGB",im.size,"#101720"),0.18)
        elif style=="aurora":
            im=_I.blend(_IE.Color(im).enhance(1.3),_I.new("RGB",im.size,t.get("accent2","#55d8ff")),0.14)
        elif style=="angular":
            im=_I.blend(_IE.Contrast(im).enhance(1.18),_I.new("RGB",im.size,t.get("accent","#1aa7ff")),0.13)
        else:
            im=_I.blend(_IE.Color(im).enhance(1.18),_I.new("RGB",im.size,t.get("accent2","#55d8ff")),0.12)
        rgba=im.convert("RGBA")
        overlay=_I.new("RGBA",rgba.size,(0,0,0,0))
        d=_ID.Draw(overlay,"RGBA")
        accent=tuple(int(t.get("accent","#1aa7ff").lstrip("#")[i:i+2],16) for i in (0,2,4))
        accent2=tuple(int(t.get("accent2","#55d8ff").lstrip("#")[i:i+2],16) for i in (0,2,4))
        boxes=[(263,78,963,219),(972,78,1567,219),(263,221,1567,290),(257,386,831,539),(836,386,1567,539),(255,661,666,911),(671,661,1237,911),(1242,661,1567,911)]
        sid=int(t.get("_skin_id",0))
        for idx,box in enumerate(boxes):
            x0,y0,x1,y1=box
            if style=="angular":
                cut=12
                points=[x0+cut,y0,x1-cut,y0,x1,y0+cut,x1,y1-cut,x1-cut,y1,x0+cut,y1,x0,y1-cut,x0,y0+cut]
                d.line(points+[points[0]],fill=(*accent2,235),width=3 if sid%4==2 else 2,joint="curve")
                for xx,yy in ((x0+5,y0+5),(x1-5,y0+5),(x0+5,y1-5),(x1-5,y1-5)): d.ellipse((xx-2,yy-2,xx+2,yy+2),fill=(*accent,245))
            elif style in ("matrix","retro"):
                d.rectangle(box,outline=(*accent,220),width=2)
                d.line((x0+8,y0+5,x0+min(100,x1-x0-8),y0+5),fill=(*accent2,245),width=2)
            elif style=="carbon":
                d.rectangle(box,outline=(165,185,205,180),width=1)
                d.line((x0+7,y0+7,x1-7,y0+7),fill=(235,245,255,70),width=1)
            else:
                radius=16 if style in ("neon","hologram","aurora") else 3
                d.rounded_rectangle(box,radius=radius,outline=(*accent,190 if style=="neon" else 150),width=3 if sid in (0,5,6,10) else 2)
                if style in ("neon","hologram","aurora"): d.line((x0+radius,y0+2,x1-radius,y0+2),fill=(*accent2,125),width=1)
        if t.get("_scanlines"):
            for yy in range(2,rgba.height,4): d.line((0,yy,rgba.width,yy),fill=(0,0,0,32),width=1)
        if t.get("_skin_layout")=="topbar":
            d.rectangle((255,0,rgba.width-1,71),fill=(*accent,32))
            d.line((255,70,rgba.width-1,70),fill=(*accent2,230),width=3)
        elif t.get("_skin_layout")=="terminal":
            for xx in range(260,rgba.width,34): d.line((xx,75,xx,rgba.height-2),fill=(*accent,22),width=1)
        out=_I.alpha_composite(rgba,overlay).convert("RGB")
        if len(cache)>24: cache={}
        cache[key]=out
        app._u443_skin_image_cache=cache
        return out
    except Exception:
        return None

_U443_ORIG_THEME_REFERENCE = AppV43._theme_reference
def _u443_theme_reference_skin(self):
    im=_u443_skin_dashboard_image(self)
    if im is not None: return im
    return _U443_ORIG_THEME_REFERENCE(self)
AppV43._theme_reference = _u443_theme_reference_skin

# The dashboard uses native Tk buttons containing image crops. The hover overlay is baked into each crop so it remains visible even above the image.
def _u443_bind_dashboard_button_hover(app):
    try:
        from PIL import Image as _I, ImageDraw as _ID, ImageEnhance as _IE
        image=getattr(app,"_dash_img",None)
        controls=getattr(app,"_dash_control_widgets",{}) or {}
        specs=getattr(app,"_dash_control_specs",[]) or []
        if image is None or not controls or not specs: return
        token=(int(app.theme_id),id(image),image.size,tuple(sorted(controls.keys())))
        if getattr(app,"_u443_dashboard_hover_token",None)!=token:
            app._u443_dashboard_hover_photos={}
            app._u443_dashboard_base_photos=dict(getattr(app,"_dash_control_photos",{}) or {})
            t=app.colors(); ac=t.get("accent2","#55d8ff"); ac_rgb=tuple(int(ac.lstrip("#")[i:i+2],16) for i in (0,2,4))
            for key,rect,_action in specs:
                btn=controls.get(key)
                if btn is None: continue
                x0,y0,x1,y1=rect; sx=image.width/1586.0; sy=image.height/960.0
                ix0=max(0,min(image.width-1,round(x0*sx))); iy0=max(0,min(image.height-1,round(y0*sy)))
                ix1=max(ix0+1,min(image.width,round(x1*sx))); iy1=max(iy0+1,min(image.height,round(y1*sy)))
                crop=image.crop((ix0,iy0,ix1,iy1))
                crop=_IE.Brightness(crop).enhance(1.24)
                crop=_IE.Color(crop).enhance(1.30)
                rgba=crop.convert("RGBA")
                halo=_I.new("RGBA",rgba.size,(0,0,0,0)); hd=_ID.Draw(halo)
                w,h=rgba.size; line=max(2,min(5,round(min(w,h)*0.055)))
                hd.rectangle((0,0,w-1,h-1),outline=(*ac_rgb,255),width=line)
                if w>8 and h>8: hd.rectangle((line+1,line+1,w-line-2,h-line-2),outline=(255,255,255,255),width=1)
                for inset,alpha in ((1,35),(2,22)):
                    hd.rectangle((inset,inset,w-1-inset,h-1-inset),outline=(*ac_rgb,alpha),width=1)
                app._u443_dashboard_hover_photos[key]=ImageTk.PhotoImage(_I.alpha_composite(rgba,halo),master=btn)
            app._u443_dashboard_hover_token=token
        for key,_rect,_action in specs:
            btn=controls.get(key)
            if btn is None or getattr(btn,"_u443_dashboard_hover_bound",False): continue
            try:
                def _enter(event,control_key=key,control=btn):
                    photo=(getattr(app,"_u443_dashboard_hover_photos",{}) or {}).get(control_key)
                    if photo is not None:
                        control.configure(image=photo,relief="solid",borderwidth=1,highlightthickness=2,
                                          highlightbackground=app.colors().get("accent2","#55d8ff"),
                                          highlightcolor=app.colors().get("accent2","#55d8ff"))
                    app._u443_hovered_dashboard_control=control_key
                def _leave(event,control_key=key,control=btn):
                    photo=(getattr(app,"_dash_control_photos",{}) or {}).get(control_key) or (getattr(app,"_u443_dashboard_base_photos",{}) or {}).get(control_key)
                    if photo is not None:
                        control.configure(image=photo,relief="flat",borderwidth=0,highlightthickness=0,
                                          highlightbackground=app.colors().get("bg","#07111f"),
                                          highlightcolor=app.colors().get("bg","#07111f"))
                    app._u443_hovered_dashboard_control=None
                btn.bind("<Enter>",_enter,add="+")
                btn.bind("<Leave>",_leave,add="+")
                btn._u443_dashboard_hover_bound=True
            except Exception: pass
    except Exception: pass

_U443_ORIG_INSTALL_DASHBOARD = AppV43._install_dashboard_controls
def _u443_install_dashboard_with_hover(self,*args,**kwargs):
    result=_U443_ORIG_INSTALL_DASHBOARD(self,*args,**kwargs)
    try: self.after_idle(lambda: (_u443_bind_dashboard_button_hover(self),_u443_bind_hover_glow(self,self)))
    except Exception: pass
    return result
AppV43._install_dashboard_controls = _u443_install_dashboard_with_hover

_U443_ORIG_CLEAR_ALL = AppV43.clear
def _u443_clear_all_with_hover(self,*args,**kwargs):
    result=_U443_ORIG_CLEAR_ALL(self,*args,**kwargs)
    try: self.after_idle(lambda:_u443_bind_hover_glow(self,self))
    except Exception: pass
    return result
AppV43.clear = _u443_clear_all_with_hover

# The theme preview changes navigation arrangement, panel silhouettes, density and charting—not only the color.
def _u443_draw_theme_preview(self,canvas):
    t=self.colors()
    try:
        from math import sin
        canvas.delete("all"); canvas.update_idletasks()
        w=max(660,canvas.winfo_width()); h=max(190,canvas.winfo_height())
        family=int(t.get("_skin_id",0)); layout=t.get("_skin_layout","sidebar"); relief=t.get("_panel_relief","flat")
        canvas.configure(bg=t["bg"])
        canvas.create_rectangle(4,4,w-4,h-4,fill=t["bg"],outline=t["accent"],width=max(1,int(t.get("_panel_highlight",1))))
        if t.get("_scanlines"):
            for yy in range(7,h,5): canvas.create_line(6,yy,w-6,yy,fill=t["panel"])
        if layout=="topbar":
            canvas.create_rectangle(16,14,w-16,49,fill=t["panel"],outline=t["accent"],width=max(1,int(t.get("_panel_bd",0))))
            canvas.create_text(28,31,text="NAPRAWA PC / HARDWARE TEST PRO",fill=t["accent"],anchor="w",font=self.fnt(10,"bold"))
            for i,name in enumerate(("PULPIT","TESTY","RAPORTY","USTAWIENIA")):
                canvas.create_text(round(w*.56)+i*75,31,text=name,fill=t["accent2"] if i==0 else t["fg"],font=self.fnt(7,"bold"))
            main_x=16; y_cards=61
        elif layout=="terminal":
            canvas.create_rectangle(16,14,185,h-14,fill=t["panel"],outline=t["accent"],width=2)
            canvas.create_text(28,31,text="> SYSTEM / STATUS",fill=t["accent"],anchor="w",font=self.fnt(9,"bold"))
            for i,name in enumerate(("CPU","GPU","RAM","NVME","SECURITY")):
                canvas.create_text(30,53+i*22,text="[+] "+name,fill=t["accent2"] if i==0 else t["fg"],anchor="w",font=self.fnt(8,"normal"))
            main_x=198; y_cards=71
        else:
            canvas.create_rectangle(16,14,160,h-14,fill=t["panel"],outline=t["accent"],width=max(1,int(t.get("_panel_highlight",1))))
            canvas.create_text(27,32,text="NAPRAWA PC",fill=t["accent"],anchor="w",font=self.fnt(10,"bold"))
            for i,name in enumerate(("PULPIT","CPU","GPU","RAM","DYSK","TESTY","RAPORTY")):
                y=55+i*22
                canvas.create_rectangle(22,y,150,y+17,fill=t["accent"] if i==0 else t["card"],outline=t["accent2"] if i==0 else t["panel"])
                canvas.create_text(30,y+8,text=name,fill="#ffffff" if i==0 else t["fg"],anchor="w",font=self.fnt(7,"bold"))
            main_x=170; y_cards=71
        available=max(430,w-main_x-18); hero_h=max(36,int(h*.19))
        if layout!="topbar":
            canvas.create_rectangle(main_x,15,main_x+available,15+hero_h,fill=t["panel"],outline=t["accent"],width=max(1,int(t.get("_panel_bd",0))+1))
            canvas.create_text(main_x+12,28,text=t.get("_skin_family","DIAGNOSTYKA"),fill=t["accent"],anchor="w",font=self.fnt(11,"bold"))
            canvas.create_text(main_x+12,45,text="MONITORING NA ŻYWO • TESTY • WYNIKI",fill=t["muted"],anchor="w",font=self.fnt(7,"bold"))
        count=4 if family%3==0 else (3 if family%3==1 else 5)
        gap=8; cw=max(62,(available-gap*(count-1))//count)
        for i in range(count):
            x=main_x+i*(cw+gap); x1=min(w-17,x+cw)
            if layout=="grid":
                pts=[x+5,y_cards,x1,y_cards,x1-5,y_cards+58,x,y_cards+58]
                canvas.create_polygon(pts,fill=t["card"],outline=t["accent"],width=2)
            elif relief in ("ridge","raised","groove"):
                canvas.create_rectangle(x,y_cards,x1,y_cards+58,fill=t["panel"],outline=t["accent"],width=max(1,int(t.get("_panel_bd",0))+1))
                canvas.create_line(x+3,y_cards+3,x1-3,y_cards+3,fill=t["accent2"],width=1)
            else:
                canvas.create_rectangle(x,y_cards,x1,y_cards+58,fill=t["panel"],outline=t["accent"],width=1)
            canvas.create_text(x+7,y_cards+13,text=("CPU","GPU","RAM","SSD","VRAM")[i%5],fill=t["accent"],anchor="w",font=self.fnt(7,"bold"))
            canvas.create_text((x+x1)//2,y_cards+36,text=f"{(12+i*13):02d}%",fill=t["good"] if i%2==0 else t["fg"],font=self.fnt(15,"bold"))
        gy=min(h-14,y_cards+73)
        canvas.create_rectangle(main_x,gy,w-18,h-14,fill=t["panel"],outline=t["accent"],width=max(1,int(t.get("_panel_bd",0))+1))
        for n in range(1,4):
            yy=gy+(h-gy-20)*n/4; canvas.create_line(main_x+8,yy,w-25,yy,fill=t["card"],dash=(2,3))
        pts=[]
        for xx in range(main_x+10,w-25,8):
            phase=(xx-main_x)/23+family
            yy=gy+int((h-gy-18)*(0.5+0.20*sin(phase)+0.10*sin(phase*0.43)))
            pts.extend((xx,yy))
        if len(pts)>=4: canvas.create_line(*pts,fill=t["accent2"],width=2,smooth=True)
        canvas.create_text(main_x+10,h-22,text=f"SKÓRKA {self.theme_id}/125 • {t.get('_skin_family','STYL')} • {relief.upper()} / {layout.upper()}",fill=t["fg"],anchor="w",font=self.fnt(8,"bold"))
    except Exception as exc:
        try: canvas.delete("all"); canvas.create_text(12,12,text=f"Błąd podglądu skórki: {exc}",fill=t.get("bad","#ff5063"),anchor="nw")
        except Exception: pass
AppV43.draw_theme_preview = _u443_draw_theme_preview

def _u443_selftest_visual_skins():
    assert len(THEMES)>=125,len(THEMES)
    assert len(set(THEMES[i]["name"] for i in range(1,126)))==125
    required=("name","bg","panel","card","fg","muted","accent","accent2","good","warn","bad","_skin_family","_skin_id","_panel_relief","_button_relief","_font_family","_image_style","_skin_layout")
    assert all(all(k in THEMES[i] for k in required) for i in range(1,126))
    assert len(set(THEMES[i]["_skin_family"] for i in range(1,126)))>=12
    assert callable(_u443_bind_dashboard_button_hover)
    assert AppV43.panel is _u443_panel_skin and AppV43.make_button is _u443_make_button_skin
    assert AppV43._theme_reference is _u443_theme_reference_skin
    assert AppV43.draw_theme_preview is _u443_draw_theme_preview
    print("[OK] 125 distinct skin names")
    print("[OK] 12 structural design systems: panel depth, borders, typography, dashboard style and preview")
    print("[OK] dedicated hover image overlays for image-backed dashboard buttons")
    print("VISUAL_SKINS_AND_HOVER_OK")
def _u443_selftest_themes():
    _u443_selftest_visual_skins()
    assert len(THEMES)>=125,len(THEMES)
    assert all(i in THEMES for i in range(1,126))
    keys=("name","bg","panel","card","fg","muted","accent","accent2","good","warn","bad")
    assert all(all(k in THEMES[i] for k in keys) for i in range(1,126))
    print("[OK] 125 selectable themes; buttons and icon widgets have hover bindings")
    print("THEMES_125_HOVER_GLOW_OK")
def _u443_selftest_dispatch(flag):
    if flag=="--selftest-themes":
        _u443_selftest_themes()
        _u445_selftest_skins()
    elif flag=="--selftest-antivirus":
        result=_u37_get_defender_status() if "_u37_get_defender_status" in globals() else _v4326_get_defender_status()
        assert isinstance(result,dict) and "DetectionAvailable" in result
        print("ANTIVIRUS_SELFTEST_OK")
    elif flag=="--selftest-update-flow":
        _u39_selftest_global()
        assert _u37_version_tuple("4.3.45")>_u37_version_tuple("4.3.44")
        print("UPDATE_FLOW_SELFTEST_OK")
    elif flag=="--selftest-launcher":
        assert "_U39_GLOBAL_MANIFEST_URL" in globals()
        assert callable(globals().get("_u39_confirm_downloaded"))
        print("LAUNCHER_SELFTEST_OK")
if __name__=="__main__" and any(f in sys.argv for f in ("--selftest-themes","--selftest-antivirus","--selftest-update-flow","--selftest-launcher")):
    for _f in ("--selftest-themes","--selftest-antivirus","--selftest-update-flow","--selftest-launcher"):
        if _f in sys.argv: _u443_selftest_dispatch(_f)
    raise SystemExit(0)
'@
    $skin = @'
# _U445_REAL_SKIN_SYSTEM — structural skins + universal hover, not palettes alone
_U445_STYLE_PROFILES = (
    {"name":"NEON HUD", "panel_relief":"flat", "panel_bd":0, "panel_edge":2, "button_relief":"flat", "button_bd":0, "sidebar_width":244, "font":"Segoe UI", "design":"hud"},
    {"name":"GLASS PRO", "panel_relief":"groove", "panel_bd":1, "panel_edge":1, "button_relief":"raised", "button_bd":1, "sidebar_width":230, "font":"Segoe UI", "design":"glass"},
    {"name":"MATRIX TERMINAL", "panel_relief":"ridge", "panel_bd":2, "panel_edge":1, "button_relief":"groove", "button_bd":2, "sidebar_width":252, "font":"Consolas", "design":"matrix"},
    {"name":"ICE STUDIO", "panel_relief":"flat", "panel_bd":0, "panel_edge":1, "button_relief":"flat", "button_bd":0, "sidebar_width":220, "font":"Segoe UI", "design":"ice"},
    {"name":"TITANIUM", "panel_relief":"raised", "panel_bd":2, "panel_edge":1, "button_relief":"raised", "button_bd":2, "sidebar_width":260, "font":"Arial", "design":"titanium"},
    {"name":"RETRO CRT", "panel_relief":"groove", "panel_bd":2, "panel_edge":1, "button_relief":"groove", "button_bd":2, "sidebar_width":248, "font":"Consolas", "design":"crt"},
    {"name":"CARBON FIBER", "panel_relief":"ridge", "panel_bd":1, "panel_edge":2, "button_relief":"raised", "button_bd":1, "sidebar_width":236, "font":"Segoe UI", "design":"carbon"},
    {"name":"SOLAR FLARE", "panel_relief":"flat", "panel_bd":0, "panel_edge":2, "button_relief":"raised", "button_bd":1, "sidebar_width":258, "font":"Arial", "design":"solar"},
    {"name":"ULTRAVIOLET", "panel_relief":"groove", "panel_bd":1, "panel_edge":2, "button_relief":"groove", "button_bd":1, "sidebar_width":242, "font":"Segoe UI", "design":"ultraviolet"},
    {"name":"MINIMAL LIGHT", "panel_relief":"flat", "panel_bd":0, "panel_edge":0, "button_relief":"flat", "button_bd":0, "sidebar_width":218, "font":"Segoe UI", "design":"minimal"},
    {"name":"INDUSTRIAL", "panel_relief":"raised", "panel_bd":3, "panel_edge":1, "button_relief":"raised", "button_bd":3, "sidebar_width":266, "font":"Arial", "design":"industrial"},
    {"name":"BLUEPRINT", "panel_relief":"ridge", "panel_bd":1, "panel_edge":1, "button_relief":"ridge", "button_bd":1, "sidebar_width":238, "font":"Consolas", "design":"blueprint"},
)

for _u445_tid, _u445_theme in THEMES.items():
    _u445_sid = (int(_u445_tid) - 1) % len(_U445_STYLE_PROFILES)
    _u445_profile = _U445_STYLE_PROFILES[_u445_sid]
    _u445_theme["_skin_id"] = _u445_sid
    _u445_theme["_skin_style"] = _u445_profile["name"]
    for _u445_key in ("panel_relief","panel_bd","panel_edge","button_relief","button_bd","sidebar_width","font","design"):
        _u445_theme["_skin_" + _u445_key] = _u445_profile[_u445_key]
    if not str(_u445_theme.get("name","")).endswith(" • " + _u445_profile["name"]):
        _u445_theme["name"] = str(_u445_theme.get("name","SKÓRKA")) + " • " + _u445_profile["name"]

def _u445_panel(self, parent, bg=None, accent=True):
    t = self.colors()
    color = bg or t["panel"]
    edge = t["accent"] if accent else color
    return tk.Frame(parent, bg=color, bd=int(t.get("_skin_panel_bd",1)),
                    relief=t.get("_skin_panel_relief","flat"),
                    highlightbackground=edge, highlightcolor=t.get("accent2",edge),
                    highlightthickness=int(t.get("_skin_panel_edge",1)))

def _u445_make_button(self, parent, text, command, kind="card", side=None, fill=None, ipady=8):
    t = self.colors()
    bg = t["card"] if kind=="card" else t["accent"] if kind=="accent" else t["good"] if kind=="good" else t["bad"] if kind=="bad" else t["panel"]
    fg = "#ffffff" if kind in ("accent","good","bad") else t["fg"]
    sid = int(t.get("_skin_id",0))
    btn = tk.Button(parent, text=text, command=command, relief=t.get("_skin_button_relief","flat"),
                    bd=int(t.get("_skin_button_bd",0)), bg=bg, fg=fg,
                    activebackground=t["accent2"], activeforeground="#ffffff",
                    highlightthickness=int(t.get("_skin_panel_edge",1)),
                    highlightbackground=t["accent"], highlightcolor=t["accent2"],
                    font=self.fnt(9,"bold"), cursor="hand2", padx=(4 + sid%3), pady=1)
    opts={}
    if side: opts["side"]=side
    if fill: opts["fill"]=fill
    btn.pack(ipady=ipady,padx=4,pady=3,**opts)
    return btn

def _u445_fnt(self, size, weight="normal"):
    t=self.colors()
    family=str(t.get("_skin_font","Segoe UI"))
    key=("_U445_FONT",family,int(size),str(weight))
    if not hasattr(self,"fonts"): self.fonts={}
    if key not in self.fonts:
        self.fonts[key]=tkfont.Font(family=family,size=int(size),weight=str(weight))
    return self.fonts[key]

def _u445_button_enter(event):
    w=event.widget
    try:
        top=w.winfo_toplevel()
        t=top.colors() if callable(getattr(top,"colors",None)) else THEMES.get(8,{})
        if str(w.cget("state"))=="disabled": return
        if isinstance(w,ttk.Button):
            if not hasattr(w,"_u445_old_style"): w._u445_old_style=w.cget("style")
            sid=int(t.get("_skin_id",0))
            style_name=f"U445Hover{sid}.TButton"
            style=ttk.Style(top)
            style.configure(style_name,background=t.get("accent2","#55d8ff"),foreground="#ffffff",
                            bordercolor=t.get("accent","#1aa7ff"),relief="raised")
            style.map(style_name,background=[("active",t.get("accent2","#55d8ff")),("pressed",t.get("accent","#1aa7ff"))],
                      foreground=[("active","#ffffff")])
            w.configure(style=style_name)
            return
        if not hasattr(w,"_u445_old_options"):
            saved={}
            for k in ("bg","fg","activebackground","activeforeground","relief","bd","highlightthickness","highlightbackground","highlightcolor"):
                try: saved[k]=w.cget(k)
                except Exception: pass
            w._u445_old_options=saved
        options={"bg":t.get("accent2","#55d8ff"),"fg":"#ffffff",
                 "activebackground":t.get("accent","#1aa7ff"),"activeforeground":"#ffffff",
                 "relief":"raised","bd":max(1,int(t.get("_skin_button_bd",1))),
                 "highlightthickness":2,"highlightbackground":t.get("accent","#1aa7ff"),
                 "highlightcolor":t.get("accent2","#55d8ff")}
        w.configure(**{k:v for k,v in options.items() if k in getattr(w,"keys",lambda:[])()})
    except Exception:
        pass

def _u445_button_leave(event):
    w=event.widget
    try:
        if isinstance(w,ttk.Button):
            if hasattr(w,"_u445_old_style"): w.configure(style=w._u445_old_style)
            return
        for k,v in getattr(w,"_u445_old_options",{}).items():
            try: w.configure(**{k:v})
            except Exception: pass
    except Exception:
        pass

def _u445_icon_enter(event):
    w=event.widget
    try:
        text=str(w.cget("text") or "").strip()
        cursor=str(w.cget("cursor") or "")
        looks_like_icon=(len(text)<=5 and any(ord(ch)>127 for ch in text))
        if not (looks_like_icon or cursor in ("hand","hand2")): return
        if not hasattr(w,"_u445_icon_old"):
            w._u445_icon_old={"fg":w.cget("fg"),"bg":w.cget("bg")}
        top=w.winfo_toplevel()
        t=top.colors() if callable(getattr(top,"colors",None)) else THEMES.get(8,{})
        w.configure(fg=t.get("accent2","#55d8ff"))
        if cursor in ("hand","hand2"): w.configure(bg=t.get("accent","#1aa7ff"))
    except Exception:
        pass

def _u445_icon_leave(event):
    w=event.widget
    try:
        old=getattr(w,"_u445_icon_old",None)
        if old: w.configure(**old)
    except Exception:
        pass

def _u445_bind_widget_tree(root, app):
    try: children=root.winfo_children()
    except Exception: return
    for w in children:
        try:
            if isinstance(w,(tk.Button,ttk.Button)) and not getattr(w,"_u445_direct_hover",False):
                w.bind("<Enter>",_u445_button_enter,add="+")
                w.bind("<Leave>",_u445_button_leave,add="+")
                w._u445_direct_hover=True
            elif isinstance(w,tk.Label) and not getattr(w,"_u445_icon_hover",False):
                w.bind("<Enter>",_u445_icon_enter,add="+")
                w.bind("<Leave>",_u445_icon_leave,add="+")
                w._u445_icon_hover=True
        except Exception: pass
        _u445_bind_widget_tree(w,app)

def _u445_install_hover_classes(self):
    if getattr(self,"_u445_class_bind_installed",False): return
    self._u445_class_bind_installed=True
    try:
        self.bind_class("Button","<Enter>",_u445_button_enter,add="+")
        self.bind_class("Button","<Leave>",_u445_button_leave,add="+")
        self.bind_class("TButton","<Enter>",_u445_button_enter,add="+")
        self.bind_class("TButton","<Leave>",_u445_button_leave,add="+")
        self.bind_class("Label","<Enter>",_u445_icon_enter,add="+")
        self.bind_class("Label","<Leave>",_u445_icon_leave,add="+")
    except Exception: pass
    try: self.after(180,lambda:_u445_bind_widget_tree(self,self))
    except Exception: pass

def _u445_skin_frame(self, *args, **kwargs):
    result=_U445_BASE_BUILD_SHELL(self,*args,**kwargs)
    t=self.colors()
    try:
        if hasattr(self,"sidebar"):
            self.sidebar.configure(bg=t["panel"],width=int(t.get("_skin_sidebar_width",244)))
            self.sidebar.pack_propagate(False)
            self.sidebar.configure(highlightbackground=t.get("accent","#1aa7ff"),
                                   highlightthickness=max(0,int(t.get("_skin_panel_edge",1))))
        if hasattr(self,"main"): self.main.configure(bg=t["bg"])
        if hasattr(self,"header"):
            self.header.configure(bg=t["panel"],relief=t.get("_skin_panel_relief","flat"),
                                  bd=int(t.get("_skin_panel_bd",0)),
                                  highlightbackground=t.get("accent","#1aa7ff"),
                                  highlightthickness=max(0,int(t.get("_skin_panel_edge",1))))
        if hasattr(self,"content"): self.content.configure(bg=t["bg"])
    except Exception: pass
    try: self.after_idle(lambda:_u445_bind_widget_tree(self,self))
    except Exception: pass
    return result

def _u445_dashboard_specs(app):
    try:
        fn=globals().get("_v4319_dashboard_control_specs")
        specs=fn(app) if callable(fn) else []
        return [(str(s[0]),tuple(s[1])) for s in specs if len(s)>=2 and len(s[1])==4]
    except Exception:
        return [
            ("PULPIT",(12,8,258,40)),("CPU",(12,142,242,180)),("GPU",(12,181,242,219)),
            ("RAM",(12,220,242,257)),("DYSK",(12,258,242,294)),("MATRYCA",(12,295,242,332)),
            ("START_TESTU",(875,861,1233,902)),("USTAWIENIA",(760,43,875,73)),
            ("ODSWIEZ",(1442,87,1556,126))
        ]

def _u445_draw_dashboard_skin(app):
    c=getattr(app,"dash_canvas",None)
    try:
        if c is None or not c.winfo_exists(): return
        w=max(1,c.winfo_width()); h=max(1,c.winfo_height())
        t=app.colors(); sid=int(t.get("_skin_id",0)); design=t.get("_skin_design","hud")
        sx=w/1586.0; sy=h/960.0
        c.delete("_u445_skin")
        accent=t.get("accent","#1aa7ff"); accent2=t.get("accent2","#55d8ff")
        muted=t.get("muted","#93a9bd"); panel=t.get("panel","#0b1c30")
        def xy(x,y): return (x*sx,y*sy)
        def line(x1,y1,x2,y2,col=None,width=1,dash=None):
            args=[x1*sx,y1*sy,x2*sx,y2*sy]
            kw={"fill":col or accent,"width":width,"tags":"_u445_skin"}
            if dash: kw["dash"]=dash
            c.create_line(*args,**kw)
        def rect(x0,y0,x1,y1,col=None,width=1,dash=None):
            kw={"outline":col or accent,"width":width,"tags":"_u445_skin"}
            if dash: kw["dash"]=dash
            c.create_rectangle(x0*sx,y0*sy,x1*sx,y1*sy,**kw)
        def oval(x0,y0,x1,y1,col=None,width=1):
            c.create_oval(x0*sx,y0*sy,x1*sx,y1*sy,outline=col or accent,width=width,tags="_u445_skin")
        regions=((265,78,963,218),(973,78,1568,218),(255,220,1568,290),
                 (255,300,1568,515),(255,520,1568,655),(255,660,1568,912))
        # Distinct visual grammar per skin: the same dashboard data gets a different UI shell.
        if design=="hud":
            rect(2,2,1584,958,accent,2)
            for x0,y0,x1,y1 in regions:
                for x,y,dx,dy in ((x0,y0,1,1),(x1,y0,-1,1),(x0,y1,1,-1),(x1,y1,-1,-1)):
                    line(x,y,x+dx*24,y,accent2,2); line(x,y,x,y+dy*17,accent2,2)
            line(0,40,1586,40,accent2,2)
        elif design=="glass":
            rect(2,2,1584,958,accent2,1)
            for x0,y0,x1,y1 in regions:
                rect(x0,y0,x1,y1,accent2,1)
                rect(x0+4,y0+4,x1-4,y1-4,accent,1)
            for x in (18,30,42,54): oval(x,12,x+5,17,accent2,1)
        elif design=="matrix":
            line(2,2,2,958,accent,3); line(10,40,1576,40,accent2,1)
            for y in range(48,960,24): line(2,y,22,y,accent,1)
            for x in range(24,230,18): line(x,78,x,918,panel,1)
            for i in range(12): line(268+i*12,42,272+i*12,42+((i*13)%22),accent,1)
        elif design=="ice":
            rect(3,3,1583,957,accent2,1)
            for x0,y0,x1,y1 in regions:
                c.create_polygon(x0*sx,(y0+7)*sy,(x0+7)*sx,y0*sy,(x1-7)*sx,y0*sy,(x1-1)*sx,(y0+7)*sy,
                                 x1*sx,(y1-7)*sy,(x1-7)*sx,y1*sy,(x0+7)*sx,y1*sy,x0*sx,(y1-7)*sy,
                                 fill="",outline=accent2,width=1,tags="_u445_skin")
            for x,y in ((34,32),(1545,30),(34,936),(1545,936)):
                line(x-8,y,x+8,y,accent2,1); line(x,y-8,x,y+8,accent2,1)
        elif design=="titanium":
            rect(2,2,1584,958,muted,2)
            for x0,y0,x1,y1 in regions:
                line(x0,y0,x0+17,y0,accent2,2); line(x0,y0,x0,y0+17,muted,2)
                line(x1-17,y1,x1,y1,accent2,2); line(x1,y1-17,x1,y1,muted,2)
            line(0,42,1586,42,muted,2); line(0,45,1586,45,accent,1)
        elif design=="crt":
            rect(3,3,1583,957,accent,1)
            for y in range(4,960,8): line(0,y,1586,y,panel,1)
            for x0,y0,x1,y1 in regions: rect(x0,y0,x1,y1,accent,1)
            rect(4,4,1582,37,accent2,1)
        elif design=="carbon":
            rect(2,2,1584,958,accent,2)
            for n in range(20): line(n*12,3,n*12+25,38,panel,2)
            for n in range(20): line(1340+n*12,922,1365+n*12,958,panel,2)
            for x0,y0,x1,y1 in regions: rect(x0,y0,x1,y1,accent,1)
        elif design=="solar":
            rect(2,2,1584,958,accent,2)
            for n in range(1,10):
                line(2,2,2+n*18,2,accent2,1); line(1584,958,1584-n*18,958,accent2,1)
            oval(1400,80,1570,250,accent2,2); oval(1410,90,1560,240,accent,1)
            for x0,y0,x1,y1 in regions: rect(x0,y0,x1,y1,accent,1)
        elif design=="ultraviolet":
            rect(2,2,1584,958,accent2,1)
            for radius in (18,27,36):
                oval(1520-radius,125-radius,1520+radius,125+radius,accent,1)
            for x0,y0,x1,y1 in regions: rect(x0,y0,x1,y1,accent2,1,dash=(4,3))
        elif design=="minimal":
            line(0,40,1586,40,accent,1); line(256,40,256,960,muted,1)
            for y in (218,290,515,655,912): line(255,y,1586,y,accent,1)
            line(4,4,1582,4,muted,1)
        elif design=="industrial":
            rect(3,3,1583,957,muted,2)
            for x0,y0,x1,y1 in regions:
                rect(x0,y0,x1,y1,accent,2)
                for x,y in ((x0+7,y0+7),(x1-7,y0+7),(x0+7,y1-7),(x1-7,y1-7)):
                    oval(x-2,y-2,x+2,y+2,muted,1)
            line(0,40,1586,40,accent,2)
        else: # blueprint
            rect(2,2,1584,958,accent2,1)
            for x in range(8,1586,40): line(x,2,x,38,panel,1)
            for y in range(8,960,40): line(2,y,25,y,accent,1)
            for x0,y0,x1,y1 in regions:
                rect(x0,y0,x1,y1,accent2,1,dash=(2,3))
                for x in range(int(x0+12),int(x1-8),80): line(x,y0,x,y0+5,accent,1)
        # Re-paint active hover last so the highlight survives each dashboard refresh.
        hover=getattr(app,"_u445_hover_rect",None)
        if hover:
            x0,y0,x1,y1=hover
            for pad,col,width in ((4,accent,3),(1,accent2,2)):
                rect(x0-pad,y0-pad,x1+pad,y1+pad,col,width)
            line(x0+5,y0+3,min(x0+34,x1-3),y0+3,accent2,2)
    except Exception as exc:
        try: app.append_log("Skin overlay: "+str(exc))
        except Exception: pass

def _u445_dashboard_motion(app,event):
    c=getattr(app,"dash_canvas",None)
    try:
        if c is None or event.widget is not c: return
        sx=max(1,c.winfo_width())/1586.0; sy=max(1,c.winfo_height())/960.0
        x=float(event.x)/sx; y=float(event.y)/sy
        found=None
        for key,rect in _u445_dashboard_specs(app):
            x0,y0,x1,y1=rect
            if x0<=x<=x1 and y0<=y<=y1:
                found=(key,rect); break
        new_key=found[0] if found else None
        if new_key==getattr(app,"_u445_hover_key",None): return
        app._u445_hover_key=new_key
        app._u445_hover_rect=found[1] if found else None
        _u445_draw_dashboard_skin(app)
    except Exception: pass

def _u445_dashboard_leave(app,event=None):
    try:
        app._u445_hover_key=None; app._u445_hover_rect=None
        _u445_draw_dashboard_skin(app)
    except Exception: pass

def _u445_bind_dashboard_hover(app):
    c=getattr(app,"dash_canvas",None)
    try:
        if c is None or not c.winfo_exists() or getattr(c,"_u445_hover_bound",False): return
        c.bind("<Motion>",lambda e,a=app:_u445_dashboard_motion(a,e),add="+")
        c.bind("<Leave>",lambda e,a=app:_u445_dashboard_leave(a,e),add="+")
        c._u445_hover_bound=True
    except Exception: pass

def _u445_draw_ref(self,*args,**kwargs):
    result=_U445_BASE_DRAW_REF(self,*args,**kwargs)
    _u445_bind_dashboard_hover(self)
    _u445_draw_dashboard_skin(self)
    return result

def _u445_build_theme_preview(self,canvas,theme_id=None):
    idx=int(theme_id or getattr(self,"theme_id",8))
    t=THEMES.get(idx,THEMES[8]); design=t.get("_skin_design","hud"); sid=int(t.get("_skin_id",0))
    canvas.delete("all")
    w=max(620,canvas.winfo_width() or 900); h=max(300,canvas.winfo_height() or 370)
    bg=t["bg"]; panel=t["panel"]; card=t["card"]; edge=t["accent"]; edge2=t["accent2"]; fg=t["fg"]
    def box(x0,y0,x1,y1,fill,outline=edge,width=1,relief="normal"):
        if relief=="cut":
            canvas.create_polygon(x0+7,y0,x1,y0,x1,y1-7,x1-7,y1,x0,y1,x0,y0+7,fill=fill,outline=outline,width=width)
        elif relief=="rounded":
            canvas.create_polygon(x0+8,y0,x1-8,y0,x1,y0+8,x1,y1-8,x1-8,y1,x0+8,y1,x0,y1-8,x0,y0+8,fill=fill,outline=outline,width=width,smooth=True)
        else:
            canvas.create_rectangle(x0,y0,x1,y1,fill=fill,outline=outline,width=width)
    box(5,5,w-5,h-5,bg,edge,2,"cut" if design in ("titanium","blueprint") else "normal")
    box(12,12,w-12,43,panel,edge2,1,"cut" if design in ("titanium","industrial") else "normal")
    titlefont=self.fnt(10,"bold")
    canvas.create_text(24,28,text="NAPRAWA PC  /  HARDWARE TEST PRO",anchor="w",fill=edge2,font=titlefont)
    canvas.create_text(w-20,28,text=f"{idx:03d}/125  •  {t['_skin_style']}",anchor="e",fill=t["good"],font=self.fnt(8,"bold"))
    if design in ("matrix","crt","blueprint"):
        for y in range(48,h-8,9 if design=="crt" else 18):
            canvas.create_line(10,y,w-10,y,fill=card,width=1,dash=(2,3) if design=="blueprint" else ())
    left_w=int(w*(.23 if design in ("glass","ice","minimal") else .20))
    if design in ("glass","blueprint"):
        # Top command rail instead of the standard left rail.
        for i,label in enumerate(("PULPIT","TESTY","RAPORTY","NAPRAWA","USTAWIENIA")):
            x=20+i*min(112,(w-40)/5)
            box(x,53,x+min(102,(w-60)/5),77,card,edge2,1,"rounded")
            canvas.create_text(x+8,65,text=label,anchor="w",fill=fg,font=self.fnt(7,"bold"))
        nav_y=87
    else:
        box(14,53,left_w,h-14,panel,edge,1,"cut" if design in ("titanium","industrial") else "normal")
        canvas.create_text(24,66,text=t["name"][:29],anchor="w",fill=edge2,font=self.fnt(8,"bold"))
        for i,label in enumerate(("⌂ PULPIT","◉ CPU / PROCESOR","◆ GPU / GRAFIKA","▦ RAM / PAMIĘĆ","▤ SSD / HDD","▣ MATRYCA","⬡ BEZPIECZEŃSTWO")):
            y=92+i*28
            if i==0: box(20,y-9,left_w-7,y+10,card,edge2,1,"rounded" if design in ("ice","glass") else "normal")
            canvas.create_text(25,y,text=label,anchor="w",fill=edge2 if i==0 else fg,font=self.fnt(7,"bold" if i==0 else "normal"))
        nav_y=53
    x0=left_w+25 if design not in ("glass","blueprint") else 18
    x1=w-15
    hero_top=nav_y+32; hero_bottom=min(h*.53,nav_y+170)
    box(x0,hero_top,x1,hero_bottom,panel,edge,2,"rounded" if design in ("glass","ice","ultraviolet") else "cut" if design in ("titanium","industrial") else "normal")
    canvas.create_text(x0+12,hero_top+13,text="PULPIT DIAGNOSTYKI",anchor="w",fill=edge2,font=self.fnt(9,"bold"))
    # Different skin families change display layout, not only color.
    if design in ("matrix","crt","blueprint"):
        for i,label in enumerate(("CPU LOAD","GPU ENGINE","RAM MAP","STORAGE I/O")):
            y=hero_top+36+i*20
            canvas.create_text(x0+16,y,text="> "+label,anchor="w",fill=edge2,font=self.fnt(7,"bold"))
            canvas.create_line(x0+140,y,x1-15,y,fill=card,width=1)
            canvas.create_line(x0+142,y+2,x0+142+(x1-x0-170)*(.22+(i%3)*.17),y+2,fill=edge,width=3)
    elif design in ("minimal","ice"):
        for i,label in enumerate(("CPU","GPU","RAM")):
            xx=x0+20+i*(x1-x0-40)/3
            canvas.create_oval(xx,hero_top+38,xx+56,hero_top+94,outline=edge,width=3)
            canvas.create_text(xx+28,hero_top+64,text=f"{42+i*13}%",fill=t["good"],font=self.fnt(8,"bold"))
            canvas.create_text(xx+28,hero_top+104,text=label,fill=fg,font=self.fnt(8,"bold"))
    else:
        cx=x0+int((x1-x0)*.32); cy=hero_top+int((hero_bottom-hero_top)*.59)
        canvas.create_oval(cx-39,cy-39,cx+39,cy+39,outline=card,width=7)
        canvas.create_arc(cx-39,cy-39,cx+39,cy+39,start=80,extent=-290,style="arc",outline=t["good"],width=6)
        canvas.create_text(cx,cy,text="98%",fill=t["good"],font=self.fnt(16,"bold"))
        gx=x0+int((x1-x0)*.49)
        canvas.create_polygon(gx,hero_top+50,gx+95,hero_top+27,gx+160,hero_top+51,gx+82,hero_top+74,fill=card,outline=edge,width=2)
        canvas.create_rectangle(gx+48,hero_top+42,gx+93,hero_top+58,fill=bg,outline=edge2,width=1)
    metric_y=hero_bottom+9
    gap=7; metrics=4
    mw=(x1-x0-gap*(metrics-1))/metrics
    for i,label in enumerate(("CPU","GPU","RAM","SSD / HDD")):
        ax=x0+i*(mw+gap); bx=ax+mw
        shape="rounded" if design in ("glass","ice","ultraviolet") else "cut" if design in ("titanium","industrial","blueprint") else "normal"
        box(ax,metric_y,bx,metric_y+66,card,edge,1,shape)
        canvas.create_text(ax+8,metric_y+12,text=label,anchor="w",fill=edge2,font=self.fnt(7,"bold"))
        value=(42,68,25,12)[i]
        canvas.create_text(bx-8,metric_y+13,text=f"{value}%",anchor="e",fill=t["good"],font=self.fnt(8,"bold"))
        for j in range(8):
            x=ax+8+j*(mw-16)/8
            yy=metric_y+52-(math.sin(j*.8+i)*.22+.4)*(metric_y+52-(metric_y+24))
            canvas.create_line(x,yy,x+max(1,(mw-20)/9),yy-3,fill=edge2,width=2)
    chart_y=metric_y+76
    box(x0,chart_y,x1,h-14,bg,edge,1,"cut" if design in ("titanium","industrial","blueprint") else "normal")
    canvas.create_text(x0+10,chart_y+12,text="WYKRESY • TEMPERATURY • OBCIĄŻENIE • TĘTNO SYSTEMU",anchor="w",fill=edge,font=self.fnt(7,"bold"))
    for k in range(1,4):
        yy=chart_y+18+(h-chart_y-38)*k/4
        canvas.create_line(x0+8,yy,x1-8,yy,fill=card,width=1,dash=(2,3))
    pts=[]
    for k in range(65):
        xx=x0+10+k*(x1-x0-20)/64
        yy=h-27-(math.sin(k*.22)*.16+math.sin(k*.53)*.05+.45)*(h-chart_y-35)
        pts.extend((xx,yy))
    canvas.create_line(*pts,fill=edge2,width=2,smooth=True)
    if design in ("industrial","titanium"):
        for x,y in ((x0+5,hero_top+5),(x1-5,hero_top+5),(x0+5,h-20),(x1-5,h-20)):
            canvas.create_oval(x-2,y-2,x+2,y+2,fill=muted,outline=edge)
    elif design=="solar":
        for i in range(1,7): canvas.create_line(0,0,i*14,0,fill=edge2,width=2)
    elif design=="ultraviolet":
        for r in (12,20,28): canvas.create_oval(x1-r-5,hero_top+18-r,x1-r-5+2*r,hero_top+18+r,outline=edge2,width=1)

# Attach style tokens after the legacy 4.3.44 theme table has finished loading.
for _u445_tid,_u445_theme in THEMES.items():
    _u445_theme.setdefault("_skin_design",_u445_THEME_DESIGN if "_u445_THEME_DESIGN" in globals() else _U445_STYLE_PROFILES[_u445_theme["_skin_id"]]["design"])

AppV43.panel=_u445_panel
AppV43.make_button=_u445_make_button
AppV43.fnt=_u445_fnt
_U445_BASE_BUILD_SHELL=AppV43._build_shell
AppV43._build_shell=_u445_skin_frame
_U445_BASE_CLEAR=AppV43.clear
def _u445_clear(self,*args,**kwargs):
    result=_U445_BASE_CLEAR(self,*args,**kwargs)
    try: self.after_idle(lambda:_u445_bind_widget_tree(self,self))
    except Exception: pass
    return result
AppV43.clear=_u445_clear
_U445_BASE_DRAW_REF=AppV43._draw_ref
AppV43._draw_ref=_u445_draw_ref
_u44_draw_theme_preview=_u445_build_theme_preview
AppV43.draw_theme_preview=lambda self,canvas:_u445_build_theme_preview(self,canvas)
_U445_BASE_INIT=AppV43.__init__
def _u445_init(self,*args,**kwargs):
    _U445_BASE_INIT(self,*args,**kwargs)
    _u445_install_hover_classes(self)
    try: self.after(300,lambda:_u445_bind_dashboard_hover(self))
    except Exception: pass
AppV43.__init__=_u445_init

def _u445_selftest_skins():
    assert len(THEMES)==125, f"Expected 125 themes, got {len(THEMES)}"
    assert len({_u445_theme.get("_skin_design") for _u445_theme in THEMES.values()})>=10
    assert all("_skin_style" in t and "_skin_panel_relief" in t and "_skin_button_relief" in t and "_skin_font" in t for t in THEMES.values())
    assert len({t["name"] for t in THEMES.values()})==125
    assert AppV43.panel is _u445_panel and AppV43.make_button is _u445_make_button
    assert callable(_u445_button_enter) and callable(_u445_button_leave) and callable(_u445_dashboard_motion)
    assert callable(_u445_draw_dashboard_skin) and callable(_u445_build_theme_preview)
    print("REAL_SKIN_SELFTEST_OK: 125 named themes, 12 structural layouts, varied panels/buttons/fonts/sidebars")
    print("HOVER_SELFTEST_OK: Tk buttons, ttk buttons, icon labels and dashboard hit areas")

'@
$dispatchPattern = '(?m)^if __name__=="__main__" and any\(f in sys\.argv for f in \(.*--selftest-themes.*\)\):'
if ($hover -notmatch $dispatchPattern) { throw "Nie znaleziono punktu wejścia testów dla nowej warstwy skórek." }
$hover = [regex]::Replace($hover, $dispatchPattern, [System.Text.RegularExpressions.MatchEvaluator]{
    param($m)
    return $skin + [Environment]::NewLine + $m.Value
}, 1)
$main = '(?m)^if __name__ == "__main__":'
    if ($src -notmatch $main) { throw "Cannot find app entry point to install hover effects." }
    $src = [regex]::Replace($src,$main,[System.Text.RegularExpressions.MatchEvaluator]{
        param($m)
        return $hover + [Environment]::NewLine + $m.Value
    },1)
}
if ($src -notmatch 'range\(1,\s*126\)' -or !$src.Contains("_U443_ICON_HOVER_GLOW")) { throw "Theme/hover patch verification failed." }
[IO.File]::WriteAllText($sourcePath,$src,[Text.UTF8Encoding]::new($false))

$setup=[IO.File]::ReadAllText($setupPath,[Text.Encoding]::UTF8)
$setup=[regex]::Replace($setup,'(?m)^(\s*#define AppVersion\s+")\d+\.\d+\.\d+(".*)$',[System.Text.RegularExpressions.MatchEvaluator]{param($m) $m.Groups[1].Value+$next+$m.Groups[2].Value},1)
$setup=[regex]::Replace($setup,'(?m)^(\s*#define ExeName\s+"NAPRAWA-PC-HARDWARE-TEST-PRO-)\d+\.\d+\.\d+(\.exe".*)$', [System.Text.RegularExpressions.MatchEvaluator]{param($m) $m.Groups[1].Value+$next+$m.Groups[2].Value},1)
[IO.File]::WriteAllText($setupPath,$setup,[Text.UTF8Encoding]::new($false))
$nl=[Environment]::NewLine
[IO.File]::AppendAllText($env:GITHUB_ENV,("APP_VERSION=$next"+$nl+"SETUP_FILENAME=$setupName"+$nl),[Text.UTF8Encoding]::new($false))
[IO.File]::AppendAllText($env:GITHUB_OUTPUT,("app_version=$next"+$nl+"setup_filename=$setupName"+$nl),[Text.UTF8Encoding]::new($false))
Write-Host "AUTO_RELEASE_VERSION=$next"
Write-Host "NEXT_VERSION=$next"
Write-Host "THEMES=125 (115 added)"
Write-Host "HOVER_GLOW=patched"
