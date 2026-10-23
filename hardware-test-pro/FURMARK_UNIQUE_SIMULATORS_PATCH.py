# v4.3.151 — dedicated FurMark-style stress page and non-repeating component schematics.
import math as _u152_math
import time as _u152_time
import sys as _u152_sys
import tkinter as _u152_tk
from tkinter import ttk as _u152_ttk, messagebox as _u152_messagebox

_U152_FURMARK_UNIQUE_SIMULATORS_VERSION = "1.0.0"
_U152_ORIGINAL_SHOW_DETAIL = _u93_show_test_detail
_U152_ORIGINAL_SHOW_HUB = AppV43.show_tests_hub
_U152_ORIGINAL_SHOW_MODULE = AppV43.show_module
_U152_COMPONENTS = {
 "CPU":{"title":"PROCESOR / CPU","subtitle":"Pakiet procesora, rdzenie, cache i ścieżki sygnałów","scene_id":8,"test_id":"cpu_sim","kind":"cpu"},
 "RAM":{"title":"PAMIĘĆ RAM","subtitle":"Moduły DIMM, kości DRAM i linie danych","scene_id":17,"test_id":"ram_sim","kind":"ram"},
 "GPU":{"title":"KARTA GRAFICZNA / GPU","subtitle":"Płytka graficzna, wentylatory i pamięć VRAM","scene_id":1,"test_id":"gpu_sim","kind":"gpu"},
 "VRAM":{"title":"PAMIĘĆ GRAFICZNA / VRAM","subtitle":"Osobne układy pamięci karty graficznej","scene_id":26,"test_id":"vram_sim","kind":"vram"},
 "DYSK":{"title":"SSD / HDD / NVMe","subtitle":"Nośnik, kontroler, NAND i część mechaniczna","scene_id":35,"test_id":"disk_sim","kind":"disk"},
 "EKRAN":{"title":"MATRYCA / EKRAN","subtitle":"Panel pikseli, podświetlenie i wzorce kolorów","scene_id":44,"test_id":"screen_sim","kind":"display"},
 "SECURITY":{"title":"BEZPIECZEŃSTWO","subtitle":"Warstwy ochrony, zapora i zdarzenia","scene_id":53,"test_id":"sec_sim","kind":"security"},
 "BATERIA":{"title":"BATERIA / ZASILANIE","subtitle":"Ogniwa, terminale i kontroler ładowania","scene_id":62,"test_id":"bat_sim","kind":"battery"},
 "SIEĆ":{"title":"SIEĆ / INTERNET","subtitle":"Interfejsy, router i połączenia","scene_id":71,"test_id":"net_sim","kind":"network"},
 "USB":{"title":"URZĄDZENIA USB","subtitle":"Porty, kontroler i magistrala urządzeń","scene_id":80,"test_id":"usb_sim","kind":"usb"},
 "AUDIO":{"title":"AUDIO / DŹWIĘK","subtitle":"Przetwornik, kanały i fala sygnału","scene_id":89,"test_id":"audio_sim","kind":"audio"},
 "KLAWIATURA":{"title":"KLAWIATURA","subtitle":"Matryca klawiszy, wiersze i kolumny","scene_id":98,"test_id":"key_sim","kind":"keyboard"},
 "KAMERA":{"title":"KAMERA / MIKROFON","subtitle":"Moduł kamery, obiektyw i optyka","scene_id":107,"test_id":"cam_sim","kind":"camera"},
}
_U152_TEST_MODULE = {value["test_id"]: key for key,value in _U152_COMPONENTS.items()}
_U152_FURMARK_SCENE_ID = 1

def _u152_normalize_module(value):
 text=str(value or "").strip().upper()
 for source,target in (("Ę","E"),("Ć","C"),("Ł","L"),("Ń","N"),("Ó","O"),("Ś","S"),("Ż","Z"),("Ź","Z")):
  text=text.replace(source,target)
 aliases={"PROCESOR":"CPU","PROCESSOR":"CPU","PAMIEC":"RAM","GRAFIKA":"GPU","KARTA GRAFICZNA":"GPU",
  "PAMIEC GRAFICZNA":"VRAM","SSD":"DYSK","HDD":"DYSK","NVME":"DYSK","MATRYCA":"EKRAN","MONITOR":"EKRAN",
  "BEZPIECZENSTWO":"SECURITY","POWER":"BATERIA","BATERIE":"BATERIA","NETWORK":"SIEĆ","SIEC":"SIEĆ",
  "INTERNET":"SIEĆ","SOUND":"AUDIO","DZWIEK":"AUDIO","KEYBOARD":"KLAWIATURA","WEBCAM":"KAMERA","KAMERA / MIKROFON":"KAMERA"}
 text=aliases.get(text,text)
 if text in _U152_COMPONENTS:return text
 for tokens,key in ((("CPU","PROCESOR"),"CPU"),(("RAM","PAMIE"),"RAM"),(("GPU","GRAFICZN"),"GPU"),(("VRAM",),"VRAM"),
  (("DYSK","SSD","HDD","NVME"),"DYSK"),(("EKRAN","MATRYC","MONITOR"),"EKRAN"),(("SECURITY","BEZPIECZ"),"SECURITY"),
  (("BATER","POWER","ZASIL"),"BATERIA"),(("SIEC","SIEĆ","INTERNET"),"SIEĆ"),(("USB",),"USB"),(("AUDIO","DZWIEK"),"AUDIO"),
  (("KLAW","KEYBOARD"),"KLAWIATURA"),(("KAMERA","CAMERA"),"KAMERA")):
  if any(token in text for token in tokens):return key
 return ""

def _u152_component_summary(app,module):
 module=_u152_normalize_module(module)
 if module in ("CPU","RAM","GPU","DYSK"):
  try: live=_u150_live_metrics(app,module)
  except Exception: live={}
  if module in ("CPU","RAM","GPU"):
   try:
    report,_test_id=_u151_last_result(app,module)
    rows=_u151_metric_rows(module,live,report)
    shown=[f"{label}: {_u151_format_metric(value,unit)}" for label,value,unit in rows[:4]]
    if report:shown.append("Ostatni test: "+str(report.get("state","N/D")).upper())
    return "   •   ".join(shown)
   except Exception:pass
  if module=="DYSK":
   free=live.get("volume_free_gb");total=live.get("volume_total_gb");read=live.get("disk_read_mib_s");write=live.get("disk_write_mib_s")
   return f"Wolumin: {live.get('volume','N/D')} • wolne/łącznie: "+(f"{free:.1f}/{total:.1f} GB" if free is not None and total is not None else "N/D")+" • odczyt/zapis: "+(f"{read:.1f}/{write:.1f} MiB/s" if read is not None and write is not None else "N/D")
 if module=="BATERIA":
  p=globals().get("psutil")
  try:
   battery=p.sensors_battery() if p is not None else None
   if battery is not None:return f"Bateria: {battery.percent:.0f}% • zasilacz: {'podłączony' if battery.power_plugged else 'odłączony'}"
  except Exception:pass
 return "Odczyt czujnika: N/D • schemat edukacyjny; brak danych nie oznacza wyniku pozytywnego."

def _u152_draw_component(canvas,module,phase=0.0):
 module=_u152_normalize_module(module);profile=_U152_COMPONENTS[module]
 width=max(640,int(canvas.winfo_width() or 1100));height=max(270,int(canvas.winfo_height() or 350))
 canvas.delete("all");canvas.configure(bg="#06101d",highlightthickness=0,bd=0)
 C={"grid":"#10283c","edge":"#25506c","cyan":"#23d8f0","blue":"#2788ff","purple":"#c16dff","green":"#29e69a","amber":"#ffbf50","white":"#e8f5ff","muted":"#91adc4","chip":"#10243a"}
 for x in range(0,width,38):canvas.create_line(x,0,x,height,fill=C["grid"])
 for y in range(0,height,32):canvas.create_line(0,y,width,y,fill=C["grid"])
 cx,cy=width*.40,height*.53;s=min(height/420.0,width/1120.0)
 def rect(x1,y1,x2,y2,fill,edge=None,w=1):canvas.create_rectangle(x1,y1,x2,y2,fill=fill,outline=edge or fill,width=w)
 def oval(x1,y1,x2,y2,fill,edge=None,w=1):canvas.create_oval(x1,y1,x2,y2,fill=fill,outline=edge or fill,width=w)
 def line(x1,y1,x2,y2,fill,w=1):canvas.create_line(x1,y1,x2,y2,fill=fill,width=w)
 def txt(x,y,value,fill=None,size=10,anchor="center",bold=False):canvas.create_text(x,y,text=value,fill=fill or C["white"],font=("Segoe UI",size,"bold" if bold else "normal"),anchor=anchor)
 def chip(x,y,w,h,label,edge=None):
  rect(x-w/2,y-h/2,x+w/2,y+h/2,C["chip"],edge or C["cyan"],2);rect(x-w*.28,y-h*.2,x+w*.28,y+h*.2,"#183b56",edge or C["cyan"],1)
  txt(x,y,label,C["white"],max(7,int(8*s)),"center",True)
  for pin in range(4):
   px=x-w*.36+pin*w*.24;line(px,y-h/2-6*s,px,y-h/2,C["amber"],2);line(px,y+h/2,px,y+h/2+6*s,C["amber"],2)
 txt(20,16,profile["title"],C["white"],11,"nw",True);txt(width-20,16,"SCHEMAT SPRZĘTOWY • NIE WYNIK TESTU",C["cyan"],8,"ne",True)
 if module=="CPU":
  rect(cx-142*s,cy-116*s,cx+142*s,cy+116*s,"#263d52",C["edge"],3);rect(cx-124*s,cy-99*s,cx+124*s,cy+99*s,"#12263a",C["cyan"],3);rect(cx-95*s,cy-72*s,cx+95*s,cy+72*s,"#20183d",C["purple"],3)
  for r in range(4):
   for c in range(4):
    x=cx-66*s+c*44*s;y=cy-45*s+r*30*s;rect(x,y,x+32*s,y+19*s,"#137a76" if (r+c+int(phase*10))%3==0 else "#16415a",C["cyan"],1)
  for i in range(18):
   p=cx-114*s+i*13*s;line(p,cy-105*s,p,cy-122*s,C["amber"],2);line(p,cy+105*s,p,cy+122*s,C["amber"],2)
  txt(cx,cy+151*s,"CPU PACKAGE • RDZENIE / CACHE",C["cyan"],9,"center",True)
 elif module=="RAM":
  rect(cx-270*s,cy-65*s,cx+270*s,cy+65*s,"#063d36",C["green"],3);rect(cx-255*s,cy-51*s,cx+255*s,cy+45*s,"#11594f",C["cyan"],2)
  for i in range(8):
   x=cx-220*s+i*62*s;rect(x-21*s,cy-35*s,x+21*s,cy+28*s,"#11283e",C["purple"] if i==int(phase)%8 else C["blue"],2)
   for py in (-18,0,18):oval(x-8*s,cy+py*s-4*s,x+8*s,cy+py*s+4*s,C["cyan"])
   txt(x,cy+4*s,f"D{i+1}",C["white"],7,"center",True)
  for i in range(30):
   x=cx-245*s+i*17*s;line(x,cy+64*s,x,cy+83*s,C["amber"],3)
  txt(cx,cy+119*s,"DIMM • DRAM • MAGISTRALA DANYCH",C["green"],9,"center",True)
 elif module=="GPU":
  rect(cx-310*s,cy-92*s,cx+310*s,cy+92*s,"#123247",C["cyan"],3);rect(cx-280*s,cy-71*s,cx+280*s,cy+71*s,"#0b4b51",C["edge"],2);chip(cx,cy-16*s,100*s,70*s,"GPU",C["purple"])
  for x in (cx-185*s,cx,cx+185*s):
   oval(x-56*s,cy-54*s,x+56*s,cy+58*s,"#081725",C["cyan"],3)
   for blade in range(9):
    a=phase+blade*2*_u152_math.pi/9;x1=x+7*s*_u152_math.cos(a);y1=cy+7*s*_u152_math.sin(a);x2=x+45*s*_u152_math.cos(a+.28);y2=cy+45*s*_u152_math.sin(a+.28);x3=x+30*s*_u152_math.cos(a+.95);y3=cy+30*s*_u152_math.sin(a+.95)
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,fill=C["blue"],outline=C["cyan"])
   oval(x-11*s,cy-11*s,x+11*s,cy+11*s,"#c2d7e8",C["white"],1)
  for x in (cx-218*s,cx-75*s,cx+75*s,cx+218*s):chip(x,cy+114*s,56*s,27*s,"VRAM",C["blue"])
  txt(cx,cy+158*s,"GPU • 3 WENTYLATORY • VRAM",C["cyan"],9,"center",True)
 elif module=="VRAM":
  chip(cx,cy,138*s,86*s,"VRAM",C["purple"])
  for r in range(3):
   for c in range(4):
    x=cx-235*s+c*155*s;y=cy-112*s+r*112*s
    if abs(x-cx)>100*s or abs(y-cy)>60*s:rect(x-42*s,y-28*s,x+42*s,y+28*s,"#13273c",C["blue"],2);txt(x,y,"GDDR",C["white"],7,"center",True);line(min(x,cx),y,cx,cy,C["edge"],1)
  txt(cx,cy+179*s,"KOŚCI PAMIĘCI GRAFICZNEJ • ŚCIEŻKI",C["purple"],9,"center",True)
 elif module=="DYSK":
  rect(cx-285*s,cy-92*s,cx+285*s,cy+92*s,"#13293d",C["cyan"],3);rect(cx-260*s,cy-75*s,cx+260*s,cy+74*s,"#081b2c",C["edge"],2);chip(cx-178*s,cy-13*s,80*s,59*s,"CTRL",C["purple"])
  for i in range(4):chip(cx-54*s+i*75*s,cy-17*s,58*s,48*s,"NAND",C["green"] if i%2 else C["blue"])
  oval(cx+197*s,cy-49*s,cx+270*s,cy+24*s,"#20394e",C["white"],2);oval(cx+210*s,cy-36*s,cx+258*s,cy+12*s,"#07101b",C["cyan"],2);oval(cx+226*s,cy-20*s,cx+242*s,cy-4*s,C["amber"],C["amber"])
  txt(cx,cy+132*s,"SSD / NVMe • KONTROLER + NAND",C["cyan"],8,"center",True)
 elif module=="EKRAN":
  rect(cx-235*s,cy-136*s,cx+235*s,cy+116*s,"#1e3148",C["cyan"],3);rect(cx-217*s,cy-118*s,cx+217*s,cy+99*s,"#050d18",C["edge"],2)
  swatches=("#ff4f60","#ffb342","#ffee5e","#28e49a","#24d9ee","#3287ff","#b16dff","#f04bd4")
  for i,color in enumerate(swatches):
   x1=cx-205*s+i*51*s;rect(x1,cy-105*s,x1+47*s,cy-65*s,color,color,1)
  for r in range(7):
   for c in range(12):
    x=cx-201*s+c*34*s;y=cy-49*s+r*20*s;rect(x,y,x+28*s,y+14*s,"#103753" if (r+c)%2 else "#184f66",C["edge"],1)
  rect(cx-28*s,cy+116*s,cx+28*s,cy+166*s,"#36516b","#9fb7cb",1);rect(cx-100*s,cy+166*s,cx+100*s,cy+179*s,"#243f56","#9fb7cb",2);txt(cx,cy+205*s,"RGB / GRADIENT / SZACHOWNICA",C["cyan"],8,"center",True)
 elif module=="SECURITY":
  points=(cx,cy-145*s,cx+130*s,cy-90*s,cx+106*s,cy+65*s,cx,cy+142*s,cx-106*s,cy+65*s,cx-130*s,cy-90*s)
  canvas.create_polygon(*points,fill="#102f47",outline=C["cyan"],width=4);canvas.create_arc(cx-60*s,cy-54*s,cx+60*s,cy+68*s,start=0,extent=180,style="arc",outline=C["purple"],width=9);rect(cx-67*s,cy+3*s,cx+67*s,cy+85*s,"#14253d",C["purple"],3);oval(cx-9*s,cy+29*s,cx+9*s,cy+47*s,C["amber"]);rect(cx-4*s,cy+43*s,cx+4*s,cy+64*s,C["amber"])
  for i in range(6):
   x=cx-235*s+i*94*s;oval(x-17*s,cy+174*s,x+17*s,cy+208*s,"#113a50",C["green"],2);line(x,cy+174*s,x,cy+136*s,C["edge"],2)
  txt(cx,cy+228*s,"ZAPORA • DEFENDER • ZDARZENIA",C["green"],8,"center",True)
 elif module=="BATERIA":
  rect(cx-253*s,cy-91*s,cx+253*s,cy+91*s,"#163044",C["green"],3);rect(cx+253*s,cy-38*s,cx+279*s,cy+38*s,"#879db0","#c2d7e8",2)
  for i in range(6):
   x=cx-231*s+i*78*s;rect(x,cy-64*s,x+62*s,cy+63*s,"#092b29",C["green"],2);rect(x+8*s,cy-50*s,x+54*s,cy+50*s,"#16564a",C["green"],1)
   for j in range(3):line(x+12*s,cy-35*s+j*31*s,x+50*s,cy-35*s+j*31*s,C["edge"],2)
  canvas.create_polygon(cx-15*s,cy-53*s,cx+18*s,cy-53*s,cx-3*s,cy-1*s,cx+27*s,cy-1*s,cx-23*s,cy+55*s,cx-8*s,cy+13*s,cx-32*s,cy+13*s,fill=C["amber"],outline=C["amber"]);txt(cx,cy+139*s,"OGNIWA • BMS • KONTROLER ŁADOWANIA",C["green"],9,"center",True)
 elif module=="SIEĆ":
  points=[(cx-250*s,cy-55*s),(cx-110*s,cy-137*s),(cx,cy-20*s),(cx+133*s,cy-120*s),(cx+252*s,cy+8*s),(cx+90*s,cy+117*s),(cx-97*s,cy+123*s)]
  for a,b in ((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,0),(0,2),(2,5),(2,4)):line(points[a][0],points[a][1],points[b][0],points[b][1],C["edge"],3)
  for idx,(x,y) in enumerate(points):oval(x-31*s,y-31*s,x+31*s,y+31*s,"#0b3346",C["cyan"] if idx==2 else C["blue"],3);txt(x,y,"GW" if idx==2 else str(idx+1),C["white"],9,"center",True)
  txt(cx,cy+191*s,"KARTA SIECIOWA • ROUTER • POŁĄCZENIA",C["cyan"],8,"center",True)
 elif module=="USB":
  rect(cx-266*s,cy-102*s,cx+266*s,cy+102*s,"#102d43",C["cyan"],3);chip(cx,cy,118*s,62*s,"USB HUB",C["purple"])
  for i in range(4):
   x=cx-210*s+i*140*s;rect(x-48*s,cy-69*s,x+48*s,cy-38*s,"#07101b","#c2d7e8",3);rect(x-35*s,cy-61*s,x-7*s,cy-46*s,C["amber"]);rect(x+7*s,cy-61*s,x+35*s,cy-46*s,C["amber"]);line(x,cy-38*s,x,cy+33*s,C["edge"],2);oval(x-17*s,cy+33*s,x+17*s,cy+67*s,"#0a354a",C["green"],2);txt(x,cy+50*s,str(i+1),C["white"],7,"center",True)
  txt(cx,cy+145*s,"PORTY USB • KONTROLER • URZĄDZENIA",C["cyan"],8,"center",True)
 elif module=="AUDIO":
  rect(cx-267*s,cy-87*s,cx-65*s,cy+88*s,"#142d43",C["cyan"],3);oval(cx-232*s,cy-53*s,cx-100*s,cy+54*s,"#081522",C["purple"],3);oval(cx-209*s,cy-31*s,cx-124*s,cy+32*s,"#145064",C["cyan"],2);oval(cx-188*s,cy-15*s,cx-145*s,cy+16*s,C["amber"],C["amber"])
  for i in range(70):
   x=cx-35*s+i*6*s;amp=(18+40*abs(_u152_math.sin(i*.41+phase)))*s;line(x,cy-amp,x,cy+amp,C["green"] if i%3 else C["purple"],2)
  rect(cx+200*s,cy-87*s,cx+267*s,cy+88*s,"#142d43",C["cyan"],3);oval(cx+207*s,cy-75*s,cx+260*s,cy-19*s,"#0b1c2c",C["purple"],3);oval(cx+207*s,cy+15*s,cx+260*s,cy+71*s,"#0b1c2c",C["purple"],3);txt(cx,cy+132*s,"WEJŚCIE • DSP • WYJŚCIE • FALA",C["green"],8,"center",True)
 elif module=="KLAWIATURA":
  rect(cx-302*s,cy-104*s,cx+302*s,cy+104*s,"#132d41",C["cyan"],3)
  for row in range(5):
   count=15 if row<4 else 7
   for col in range(count):
    if row==4:
     x=cx-(count-1)*36*s/2+col*36*s;w=29*s
     if col==3:w=83*s;x-=27*s
    else:x=cx-(count-1)*36*s/2+col*36*s;w=29*s
    y=cy-73*s+row*37*s;fill=C["purple"] if (row==int(phase*2)%5 and col==int(phase*7)%count) else "#102338";rect(x-w/2,y,x+w/2,y+27*s,fill,C["edge"],1)
  txt(cx,cy+144*s,"MATRYCA WIERSZY / KOLUMN • BEZ ZAPISU TREŚCI",C["cyan"],8,"center",True)
 elif module=="KAMERA":
  rect(cx-276*s,cy-112*s,cx+276*s,cy+112*s,"#132d41",C["cyan"],3);rect(cx-238*s,cy-82*s,cx-148*s,cy+82*s,"#0b1c2c","#c2d7e8",2);oval(cx-224*s,cy-55*s,cx-161*s,cy+8*s,"#13273e",C["purple"],3);lens_x=cx+34*s
  for radius,color,line_width in ((94,C["cyan"],3),(74,C["blue"],3),(53,C["purple"],3),(30,C["amber"],3),(10,C["white"],2)):oval(lens_x-radius*s,cy-radius*s,lens_x+radius*s,cy+radius*s,"#06101d",color,line_width)
  for i in range(9):
   angle=2*_u152_math.pi*i/9+phase*.18;x=lens_x+113*s*_u152_math.cos(angle);y=cy+113*s*_u152_math.sin(angle);oval(x-4*s,y-4*s,x+4*s,y+4*s,C["green"])
  txt(cx,cy+150*s,"OBIEKTYW • MATRYCA • BEZ ZAPISU NAGRAŃ",C["cyan"],8,"center",True)
 txt(width-18,height-16,"SCHEMAT EDUKACYJNY • NIE JEST WYNIKIEM TESTU",C["muted"],8,"se",False)

def _u152_simulator_tick(app,token):
 if getattr(app,"_u152_simulator_token",None)!=token or str(getattr(app,"current_view",""))!="COMPONENT_SIMULATOR":return
 panel=getattr(app,"_u152_simulator_panel",None)
 try:
  if not isinstance(panel,dict) or not panel["canvas"].winfo_exists():return
  panel["phase"]+=.13;_u152_draw_component(panel["canvas"],panel["module"],panel["phase"]);panel["metrics"].configure(text=_u152_component_summary(app,panel["module"]));app.after(130,lambda:_u152_simulator_tick(app,token))
 except Exception as exc:
  try:app.queue_log("Symulator komponentu: "+repr(exc))
  except Exception:pass

def _u152_show_component_simulator(app,module,test_id=""):
 key=_u152_normalize_module(module)
 if key not in _U152_COMPONENTS:
  _u152_messagebox.showwarning("Symulator podzespołu","Brak osobnego schematu.",parent=app);return
 profile=_U152_COMPONENTS[key];app.current_view="COMPONENT_SIMULATOR";token=int(getattr(app,"_u152_simulator_token",0) or 0)+1;app._u152_simulator_token=token;app.clear();t=app.colors()
 app.header_title.config(text="SYMULATOR PODZESPOŁU — "+profile["title"])
 head=app.panel(app.content);head.pack(fill="x",padx=4,pady=(4,6))
 _u152_tk.Label(head,text=profile["title"]+" • MODEL NIEPOWTARZALNY",bg=t["panel"],fg=t["accent"],font=app.fnt(12,"bold")).pack(anchor="w",padx=12,pady=(8,2))
 _u152_tk.Label(head,text=profile["subtitle"]+". To schemat edukacyjny; rzeczywiste dane czujników są pokazane tylko wtedy, gdy Windows/sterownik je udostępnia.",bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1400,justify="left").pack(anchor="w",padx=12,pady=(0,7))
 canvas=_u152_tk.Canvas(app.content,height=350,bg="#06101d",highlightthickness=0,bd=0);canvas.pack(fill="both",expand=True,padx=8,pady=(0,5))
 metrics=_u152_tk.Label(app.content,text=_u152_component_summary(app,key),bg=t["panel"],fg=t["cyan"],font=app.fnt(9,"bold"),anchor="w",justify="left",wraplength=1400);metrics.pack(fill="x",padx=8,pady=(0,5))
 row=_u152_tk.Frame(app.content,bg=t["bg"]);row.pack(fill="x",padx=8,pady=(0,8))
 app.make_button(row,"← KATALOG TESTÓW",lambda:app.show_component_lab(),"card",side="left",ipady=5)
 app.make_button(row,"GPU FURMARK-STYLE STRESS",lambda:_u152_show_furmark_stress(app),"accent",side="left",ipady=5)
 app.make_button(row,"3D STUDIO • 110 SCEN",lambda:_u66_show_3d_studio(app),"card",side="left",ipady=5)
 app._u152_simulator_panel={"module":key,"canvas":canvas,"metrics":metrics,"phase":0.0,"token":token};_u152_draw_component(canvas,key,0.0);app.after(160,lambda:_u152_simulator_tick(app,token))

def _u152_draw_furmark_preview(canvas,phase=0.0):
 canvas.delete("all");width=max(640,int(canvas.winfo_width() or 1000));height=max(260,int(canvas.winfo_height() or 360));canvas.configure(bg="#020711",highlightthickness=0,bd=0)
 cx,cy=width*.42,height*.51;radius=min(height*.32,width*.22)
 for i in range(7):
  r=radius*(1.0-i*.075);red=120+min(120,i*18);green=28+min(140,i*16);blue=12+min(36,i*4);canvas.create_oval(cx-r*1.38,cy-r*.92,cx+r*1.38,cy+r*.92,outline=("#%02x%02x%02x"%(red,green,blue)),width=max(2,int(8-i*.65)))
 for i in range(460):
  angle=2*_u152_math.pi*i/460+phase;wobble=.86+.15*_u152_math.sin(i*.19+phase*2.1);inner=radius*wobble;outer=inner+radius*(.10+.18*(.5+.5*_u152_math.sin(i*.37+phase)))
  x1=cx+_u152_math.cos(angle)*inner*1.28;y1=cy+_u152_math.sin(angle)*inner*.86;x2=cx+_u152_math.cos(angle)*outer*1.28;y2=cy+_u152_math.sin(angle)*outer*.86
  color="#ffcf58" if i%11<3 else "#ff7b25" if i%4 else "#ff3d1f";canvas.create_line(x1,y1,x2,y2,fill=color,width=1)
 canvas.create_oval(cx-radius*.76,cy-radius*.50,cx+radius*.76,cy+radius*.50,fill="#020711",outline="#1b2e43",width=2)
 canvas.create_text(16,14,text="FURMARK-STYLE GPU STRESS • PODGLĄD SCHEMATYCZNY",anchor="nw",fill="#ffb343",font=("Segoe UI",10,"bold"))
 canvas.create_text(width-16,14,text="FPS TYLKO Z RENDERERA OPENGL",anchor="ne",fill="#43dcf1",font=("Segoe UI",8,"bold"))
 canvas.create_text(width-22,height-18,text="AUTORSKI RENDERER • NIE OFICJALNY FURMARK 2",anchor="se",fill="#8ba4bf",font=("Segoe UI",8,"bold"))

def _u152_furmark_tick(app,token):
 if getattr(app,"_u152_furmark_token",None)!=token or str(getattr(app,"current_view",""))!="3D_FURMARK_STRESS":return
 try:
  canvas=getattr(app,"_u152_furmark_canvas",None)
  if canvas is not None and canvas.winfo_exists():
   app._u152_furmark_phase=float(getattr(app,"_u152_furmark_phase",0.0))+.08;_u152_draw_furmark_preview(canvas,app._u152_furmark_phase)
  duration=max(1,int(getattr(app,"_u152_furmark_duration",10)));started=float(getattr(app,"_u152_furmark_started_at",0.0));progress=getattr(app,"_u152_furmark_progress",None)
  if bool(getattr(app,"running",False)) and started and progress is not None and progress.winfo_exists():progress.configure(value=max(0.0,min(99.0,100.0*(_u152_time.monotonic()-started)/duration))
  app.after(120,lambda:_u152_furmark_tick(app,token))
 except Exception:pass

def _u152_finish_furmark(app,result,token):
 if getattr(app,"_u152_furmark_token",None)!=token:return
 app._u152_last_furmark_result=dict(result or {});status=getattr(app,"_u152_furmark_status",None);progress=getattr(app,"_u152_furmark_progress",None)
 if progress is not None:
  try:progress.configure(value=100 if result.get("frames",0) else 0)
  except Exception:pass
 try:live=_u150_live_metrics(app,"GPU")
 except Exception:live={}
 avg=result.get("average_fps");peak=result.get("peak_fps_1s");frames=result.get("frames");state=str(result.get("state") or "N/D").upper()
 message=f"WYNIK {state} • średni FPS: {_u151_format_metric(avg,'FPS')} • peak FPS: {_u151_format_metric(peak,'FPS')} • klatki: {frames if frames is not None else 'N/D'} • renderer: {result.get('renderer') or result.get('error') or 'N/D'}"
 try:
  if status is not None and status.winfo_exists():status.configure(text=message,fg=app.colors()["good"] if state in ("GOOD","PASS","OK") else app.colors()["warn"])
  fields=getattr(app,"_u152_furmark_values",{}) or {};vals={"avg":_u151_format_metric(avg,"FPS"),"peak":_u151_format_metric(peak,"FPS"),"frames":str(frames if frames is not None else "N/D"),"temp":_u151_format_metric(live.get("gpu_temp_c"),"°C"),"load":_u151_format_metric(live.get("gpu_load_percent"),"%")}
  for key,value in vals.items():
   widget=fields.get(key)
   if widget is not None and widget.winfo_exists():widget.configure(text=value)
  app.append_log("FURMARK-STYLE GPU STRESS: "+message)
 except Exception:pass

def _u152_start_furmark_test(app):
 if getattr(app,"running",False):_u152_messagebox.showinfo("GPU stress","Zatrzymaj bieżący test przed uruchomieniem kolejnego.",parent=app);return
 try:seconds=int(str(app._u152_furmark_duration_var.get()).split()[0])
 except Exception:seconds=10
 try:resolution=str(app._u152_furmark_resolution_var.get() or "1920x1080")
 except Exception:resolution="1920x1080"
 if seconds>=60 and not _u152_messagebox.askyesno("FurMark-style GPU stress",f"Renderować scenę OpenGL 01 przez {seconds} s w {resolution}? Test obciąża GPU i może zwiększyć temperaturę.",parent=app):return
 app.stop_requested=False;app._u90_scene_resolution_value=resolution;app._u152_furmark_duration=seconds;app._u152_furmark_started_at=_u152_time.monotonic()
 token=int(getattr(app,"_u152_furmark_token",0) or 0)+1;app._u152_furmark_token=token
 try:app._u152_furmark_status.configure(text=f"RENDERER OPENGL W TOKU • scena 1/110 • {seconds} s • {resolution}",fg=app.colors()["accent"]);app._u152_furmark_progress.configure(value=0)
 except Exception:pass
 def job():
  started=_u152_time.monotonic()
  try:result=_u66_execute_gpu_scene(app,_U152_FURMARK_SCENE_ID,seconds)
  except Exception as exc:result={"state":"warn","error":f"{type(exc).__name__}: {exc}"}
  if not isinstance(result,dict):result={"state":"warn","message":"Renderer nie zwrócił raportu."}
  result.update({"app":"NAPRAWA PC HARDWARE TEST PRO","module":"GPU","test_id":"FURMARK_STYLE_GPU_STRESS","test_name":"Autorski FurMark-style OpenGL GPU stress","official_furmark_engine":False,"scene_id":_U152_FURMARK_SCENE_ID,"scene_name":_U100_SCENE_TITLES[_U152_FURMARK_SCENE_ID-1],"requested_duration_seconds":seconds,"duration_seconds":round(_u152_time.monotonic()-started,2),"resolution_requested":resolution,"note":"FPS pochodzi z faktycznie wyrenderowanych klatek. Nie jest to oficjalny silnik FurMark 2 ani benchmark FPS w grach."})
  try:
   save=globals().get("_u149_save_report")
   if callable(save):
    report_path=save("GPU","FURMARK_STYLE_GPU_STRESS",result)
    if report_path:result["report_path"]=str(report_path)
  except Exception as exc:result["report_save_warning"]=f"{type(exc).__name__}: {exc}"
  try:app.queue_results("FURMARK_GPU_STRESS",result);app.queue_log("FURMARK-STYLE GPU STRESS: "+str(result.get("state"))+" • FPS="+str(result.get("average_fps","N/D")))
  except Exception:pass
  try:app.queue_action(lambda r=dict(result),k=token:_u152_finish_furmark(app,r,k))
  except Exception:_u152_finish_furmark(app,result,token)
 app.worker(job);app.after(180,lambda:_u152_furmark_tick(app,token))

def _u152_stop_furmark_test(app):
 if getattr(app,"running",False):
  app.stop_requested=True
  try:app._u152_furmark_status.configure(text="STOP — zatrzymywanie renderera OpenGL…",fg=app.colors()["warn"])
  except Exception:pass
 else:_u152_messagebox.showinfo("GPU stress","Żaden test nie jest w toku.",parent=app)

def _u152_show_furmark_stress(app):
 app.current_view="3D_FURMARK_STRESS";token=int(getattr(app,"_u152_furmark_token",0) or 0)+1;app._u152_furmark_token=token;app.clear();t=app.colors()
 app.header_title.config(text="GPU FURMARK-STYLE STRESS — RZECZYWISTY OPENGL / FPS")
 hero=app.panel(app.content);hero.pack(fill="x",padx=4,pady=(4,5))
 _u152_tk.Label(hero,text="FURMARK-STYLE GPU STRESS • SCENA 01",bg=t["panel"],fg="#ff9b36",font=app.fnt(12,"bold")).pack(anchor="w",padx=12,pady=(8,3))
 _u152_tk.Label(hero,text="Własny renderer OpenGL, nie oficjalny silnik FurMark 2. FPS mierzy rzeczywiście wyrenderowane klatki; temperatura/obciążenie widoczne tylko gdy sterownik ma te czujniki.",bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1450,justify="left").pack(anchor="w",padx=12,pady=(0,8))
 controls=_u152_tk.Frame(app.content,bg=t["bg"]);controls.pack(fill="x",padx=8,pady=(0,5))
 _u152_tk.Label(controls,text="CZAS",bg=t["bg"],fg=t["accent"],font=app.fnt(8,"bold")).pack(side="left",padx=(0,5))
 app._u152_furmark_duration_var=_u152_tk.StringVar(master=app,value="30 s");_u152_ttk.Combobox(controls,textvariable=app._u152_furmark_duration_var,values=("5 s","10 s","30 s","60 s","120 s"),state="readonly",width=9).pack(side="left",padx=(0,12))
 _u152_tk.Label(controls,text="ROZDZIELCZOŚĆ",bg=t["bg"],fg=t["accent"],font=app.fnt(8,"bold")).pack(side="left",padx=(0,5))
 app._u152_furmark_resolution_var=_u152_tk.StringVar(master=app,value=str(getattr(app,"_u90_scene_resolution_value","1920x1080") or "1920x1080"));_u152_ttk.Combobox(controls,textvariable=app._u152_furmark_resolution_var,values=("800x600","1280x720","1600x900","1920x1080","2560x1440","3840x2160"),state="readonly",width=13).pack(side="left",padx=(0,12))
 app.make_button(controls,"▶ START GPU STRESS",lambda:_u152_start_furmark_test(app),"good",side="left",ipady=5);app.make_button(controls,"STOP TEST",lambda:_u152_stop_furmark_test(app),"bad",side="left",ipady=5);app.make_button(controls,"3D STUDIO • 110 SCEN",lambda:_u66_show_3d_studio(app),"card",side="left",ipady=5)
 canvas=_u152_tk.Canvas(app.content,height=315,bg="#020711",highlightthickness=0,bd=0);canvas.pack(fill="x",expand=False,padx=8,pady=(0,5));app._u152_furmark_canvas=canvas;_u152_draw_furmark_preview(canvas,0.0)
 app._u152_furmark_status=_u152_tk.Label(app.content,text="GOTOWY • brak pomiaru • kliknij START GPU STRESS",bg=t["panel"],fg=t["muted"],font=app.fnt(9,"bold"),anchor="w",justify="left",wraplength=1450);app._u152_furmark_status.pack(fill="x",padx=8,pady=(0,5));app._u66_3d_status=app._u152_furmark_status
 app._u152_furmark_progress=_u152_ttk.Progressbar(app.content,mode="determinate",maximum=100,value=0);app._u152_furmark_progress.pack(fill="x",padx=8,pady=(0,6))
 grid=_u152_tk.Frame(app.content,bg=t["bg"]);grid.pack(fill="x",padx=8,pady=(0,6));app._u152_furmark_values={}
 for key,caption in (("avg","ŚREDNI FPS"),("peak","PEAK FPS 1 s"),("frames","WYR. KLATKI"),("temp","TEMP. GPU"),("load","OBCIĄŻENIE GPU")):
  card=_u152_tk.Frame(grid,bg=t["card"],highlightbackground=t["panel"],highlightthickness=1);card.pack(side="left",fill="both",expand=True,padx=2);_u152_tk.Label(card,text=caption,bg=t["card"],fg=t["muted"],font=app.fnt(8,"bold")).pack(pady=(5,1));value=_u152_tk.Label(card,text="N/D",bg=t["card"],fg=t["accent2"],font=app.fnt(12,"bold"));value.pack(pady=(0,5));app._u152_furmark_values[key]=value
 foot=_u152_tk.Frame(app.content,bg=t["bg"]);foot.pack(fill="x",padx=8,pady=(0,6))
 app.make_button(foot,"HISTORIA TESTÓW / RAPORTY",lambda:_u149_show_history(app),"card",side="left",ipady=4);app.make_button(foot,"13 UNIKALNYCH SYMULATORÓW",lambda:_u152_show_simulator_hub(app),"card",side="left",ipady=4);app.make_button(foot,"← TESTY",app.show_tests_hub,"card",side="left",ipady=4)

def _u152_show_simulator_hub(app):
 app.current_view="COMPONENT_SIMULATOR_HUB";app.clear();t=app.colors();app.header_title.config(text="LABORATORIUM SYMULATORÓW — 13 RÓŻNYCH PODZESPOŁÓW")
 head=app.panel(app.content);head.pack(fill="x",padx=4,pady=(4,6))
 _u152_tk.Label(head,text="13 MODELI • BRAK POWTARZANIA TEJ SAMEJ SCENY W KAŻDYM MODULE",bg=t["panel"],fg=t["accent"],font=app.fnt(12,"bold")).pack(anchor="w",padx=12,pady=(8,3))
 _u152_tk.Label(head,text="Każdy kafel pokazuje inny schemat. Prawdziwe testy i dane czujników są osobno; schemat nie jest wynikiem sprzętowym.",bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1450,justify="left").pack(anchor="w",padx=12,pady=(0,8))
 row=_u152_tk.Frame(app.content,bg=t["bg"]);row.pack(fill="x",padx=8,pady=(0,5));app.make_button(row,"GPU FURMARK-STYLE STRESS",lambda:_u152_show_furmark_stress(app),"accent",side="left",ipady=5);app.make_button(row,"110 SCEN OPENGL",lambda:_u66_show_3d_studio(app),"card",side="left",ipady=5)
 grid=_u152_tk.Frame(app.content,bg=t["bg"]);grid.pack(fill="both",expand=True,padx=8,pady=(0,6))
 for col in range(3):grid.grid_columnconfigure(col,weight=1,uniform="simulators")
 for index,(module,profile) in enumerate(_U152_COMPONENTS.items()):
  r,c=divmod(index,3);card=_u152_tk.Frame(grid,bg=t["card"],highlightbackground=t["panel"],highlightthickness=1);card.grid(row=r,column=c,sticky="nsew",padx=3,pady=3)
  _u152_tk.Label(card,text=profile["title"],bg=t["card"],fg=t["accent2"],font=app.fnt(9,"bold"),anchor="w").pack(fill="x",padx=8,pady=(7,2))
  _u152_tk.Label(card,text=profile["subtitle"],bg=t["card"],fg=t["muted"],font=app.fnt(8),wraplength=380,justify="left",anchor="w").pack(fill="x",padx=8,pady=(0,5))
  app.make_button(card,"OTWÓRZ OSOBNY SYMULATOR",lambda m=module,tid=profile["test_id"]:_u152_show_component_simulator(app,m,tid),"card",fill="x",ipady=3)
 footer=_u152_tk.Frame(app.content,bg=t["bg"]);footer.pack(fill="x",padx=8,pady=(0,8));app.make_button(footer,"← TESTY",app.show_tests_hub,"card",side="left",ipady=4)

def _u152_add_hub_controls(app):
 try:
  t=app.colors();row=_u152_tk.Frame(app.content,bg=t["bg"]);children=app.content.winfo_children()
  if children:row.pack(fill="x",padx=8,pady=(2,5),before=children[0])
  else:row.pack(fill="x",padx=8,pady=(2,5))
  app.make_button(row,"GPU FURMARK-STYLE STRESS",lambda:_u152_show_furmark_stress(app),"accent",side="left",ipady=5);app.make_button(row,"13 UNIKALNYCH SYMULATORÓW",lambda:_u152_show_simulator_hub(app),"card",side="left",ipady=5);return True
 except Exception as exc:
  try:app.queue_log("Nie dodano przycisków GPU stress/symulatorów: "+repr(exc))
  except Exception:pass
  return False

def _u152_show_test_detail(app,module,test_id):
 result=_U152_ORIGINAL_SHOW_DETAIL(app,module,test_id)
 try:
  entry=_u93_find_test(_u93_norm(module),test_id);kind=entry[3];canonical=_U152_TEST_MODULE.get(test_id,_u152_normalize_module(module))
  stack=[getattr(app,"content",None)]
  while stack:
   root=stack.pop()
   if root is None:continue
   try:stack.extend(list(root.winfo_children()))
   except Exception:pass
   try:
    if not root.winfo_exists() or not hasattr(root,"cget"):continue
    label=str(root.cget("text") or "")
    if "UNIKALNA SCENA OPENGL / FPS" not in label:continue
    if kind=="sim":
     root.configure(text="OTWÓRZ OSOBNY SYMULATOR — "+_U152_COMPONENTS[canonical]["title"],command=lambda m=canonical,tid=test_id:_u152_show_component_simulator(app,m,tid))
    else:root.destroy()
   except Exception:pass
  return result
 except Exception as exc:
  try:app.queue_log("Naprawa powtarzających się przycisków symulatora: "+repr(exc))
  except Exception:pass
  return result

def _u152_show_tests_hub(app):
 result=_U152_ORIGINAL_SHOW_HUB(app);_u152_add_hub_controls(app);return result

def _u152_show_module(app,module):
 result=_U152_ORIGINAL_SHOW_MODULE(app,module)
 if _u152_normalize_module(module)=="GPU" and not str(getattr(app,"current_view","")).startswith("COMPONENT_TEST_DETAIL_"):
  try:
   bar=_u152_tk.Frame(app.content,bg=app.colors()["bg"]);children=app.content.winfo_children()
   if children:bar.pack(fill="x",padx=8,pady=(2,5),before=children[0])
   else:bar.pack(fill="x",padx=8,pady=(2,5))
   app.make_button(bar,"▶ GPU FURMARK-STYLE STRESS",lambda:_u152_show_furmark_stress(app),"good",side="left",ipady=5);app.make_button(bar,"13 UNIKALNYCH SYMULATORÓW",lambda:_u152_show_simulator_hub(app),"card",side="left",ipady=5)
  except Exception as exc:
   try:app.queue_log("Nie dodano GPU stress toolbar: "+repr(exc))
   except Exception:pass
 return result

def _u152_deep_names(function):
 import types as _u152_types
 pending=[function.__code__];names=set();literals=set()
 while pending:
  code=pending.pop();names.update(code.co_names);names.update(code.co_varnames)
  for value in code.co_consts:
   if isinstance(value,_u152_types.CodeType):pending.append(value)
   elif isinstance(value,str):literals.add(value)
   elif isinstance(value,tuple):literals.update(item for item in value if isinstance(item,str))
 return names,literals

def _u152_selftest_furmark_and_unique_simulators():
 assert _U152_FURMARK_UNIQUE_SIMULATORS_VERSION=="1.0.0"
 assert len(_U152_COMPONENTS)==13 and len({x["title"] for x in _U152_COMPONENTS.values()})==13
 assert len({x["scene_id"] for x in _U152_COMPONENTS.values()})==13 and len({x["kind"] for x in _U152_COMPONENTS.values()})==13
 assert _u152_normalize_module("PROCESOR / CPU")=="CPU" and _u152_normalize_module("PAMIĘĆ RAM")=="RAM"
 assert _u152_normalize_module("KARTA GRAFICZNA / GPU")=="GPU" and _u152_normalize_module("PAMIĘĆ GRAFICZNA / VRAM")=="VRAM" and _u152_normalize_module("SIEĆ / INTERNET")=="SIEĆ"
 assert all(1<=int(x["scene_id"])<=len(_U66_SCENES) for x in _U152_COMPONENTS.values())
 assert _U152_FURMARK_SCENE_ID==1 and callable(_u152_show_furmark_stress) and callable(_u152_start_furmark_test)
 assert callable(_u152_show_component_simulator) and callable(_u152_show_simulator_hub) and callable(_u152_show_test_detail)
 stress_names,stress_literals=_u152_deep_names(_u152_start_furmark_test)
 assert "_u66_execute_gpu_scene" in stress_names and ("_u149_save_report" in stress_names or "_u149_save_report" in stress_literals) and "FURMARK_STYLE_GPU_STRESS" in stress_literals
 detail_names,detail_literals=_u152_deep_names(_u152_show_test_detail)
 assert "_u152_show_component_simulator" in detail_names and "sim" in detail_literals and "UNIKALNA SCENA OPENGL / FPS" in detail_literals
 scene_names,scene_literals=_u152_deep_names(_u152_draw_component)
 assert all(x in scene_literals for x in ("CPU","RAM","GPU","VRAM","DYSK","EKRAN","SECURITY","BATERIA","SIEĆ","USB","AUDIO","KLAWIATURA","KAMERA"))
 assert all(x in scene_names for x in ("create_polygon","create_oval","create_line","create_rectangle"))
 print("FURMARK_AND_UNIQUE_SIMULATORS_SELFTEST_OK: dedicated GPU stress with FPS report, 13 component schematics, generic duplicate links removed")

_u93_show_test_detail=_u152_show_test_detail
AppV43.show_test_detail=_u152_show_test_detail
AppV43.show_tests_hub=_u152_show_tests_hub
AppV43.show_module=_u152_show_module
AppV43.show_furmark_stress=_u152_show_furmark_stress
AppV43.show_simulator_hub=_u152_show_simulator_hub
if __name__=="__main__" and "--selftest-furmark-unique-simulators" in _u152_sys.argv:
 try:
  _u152_selftest_furmark_and_unique_simulators()
  raise SystemExit(0)
 except Exception as _u152_exc:
  import traceback as _u152_traceback
  print("FURMARK_AND_UNIQUE_SIMULATORS_SELFTEST_FAILED:",type(_u152_exc).__name__,str(_u152_exc))
  _u152_traceback.print_exc()
  raise SystemExit(1)
