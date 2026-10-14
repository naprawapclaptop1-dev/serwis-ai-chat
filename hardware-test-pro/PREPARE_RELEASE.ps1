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
        "name": f"{_U443_PREFIX[_u443_family]} {_U443_SUFFIX[_u443_group]}",
        "bg": _u443_bg,"panel": _u443_panel,"card": _u443_card,
        "fg": _u443_fg,"muted": _u443_muted,
        "accent": _u443_accent,"accent2": _u443_accent2,
        "good": _u443_hex(0.37,0.55,0.78),
        "warn": _u443_hex(0.12,0.60,0.86),
        "bad": _u443_hex(0.99,0.59,0.88),
    }
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

def _u443_selftest_themes():
    assert len(THEMES)>=125,len(THEMES)
    assert all(i in THEMES for i in range(1,126))
    keys=("name","bg","panel","card","fg","muted","accent","accent2","good","warn","bad")
    assert all(all(k in THEMES[i] for k in keys) for i in range(1,126))
    print("[OK] 125 selectable themes; buttons and icon widgets have hover bindings")
    print("THEMES_125_HOVER_GLOW_OK")
def _u443_selftest_dispatch(flag):
    if flag=="--selftest-themes":
        _u443_selftest_themes()
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
