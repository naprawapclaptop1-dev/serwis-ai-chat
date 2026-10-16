# NAPRAWA PC HARDWARE TEST PRO — Advanced Knowledge, Live Metrics, Speed Test, 20-scene 3D Studio and Sequential Test Runner.
# Injected by PREPARE_RELEASE.ps1 before __main__. Real measurements only; unsupported sensors stay N/D.
import json as _u66_json
import re as _u66_re
import os as _u66_os
import math as _u66_math
import time as _u66_time
import uuid as _u66_uuid
import html as _u66_html
import webbrowser as _u66_webbrowser
import urllib.parse as _u66_urlparse
import urllib.request as _u66_request
import urllib.error as _u66_urlerror
import subprocess as _u66_subprocess
import threading as _u66_threading
from html.parser import HTMLParser as _U66_HTMLParser
from datetime import datetime as _U66_datetime
from tkinter import filedialog as _u66_filedialog

_U66_KNOWLEDGE_SEED = [
{"title":"CPU obciążenie, taktowanie i throttling","tags":"cpu procesor temperatura taktowanie MHz obciążenie throttling test stress","text":"Test obciążeniowy powinien mierzyć obciążenie, taktowanie, czas i ewentualne ograniczanie częstotliwości. Wartość maksymalna z jednego krótkiego pomiaru nie jest gwarantowanym zegarem turbo. Podczas długiego testu obserwuj temperaturę, zegary, stabilność i błędy. Jeśli program nie ma dostępu do czujnika temperatury, wynik powinien być N/D, a nie wartością zgadywaną.","source":"https://learn.microsoft.com/en-us/windows/win32/perfctrs/about-performance-counters"},
{"title":"Temperatury CPU, GPU i czujniki sprzętowe","tags":"temperatura cpu gpu sensor czujniki wentylator rpm płyta główna","text":"Temperatury zależą od modelu podzespołu, obciążenia, chłodzenia i czujnika. Windows nie udostępnia uniwersalnego czujnika temperatury rdzeni CPU dla każdego komputera. Odczyty z ACPI mogą oznaczać strefę termiczną, a nie temperaturę rdzenia. W programie pokaż źródło czujnika i czas próbki; gdy sensor nie jest dostępny, pokaż N/D. LibreHardwareMonitor potrafi odczytywać temperatury, obroty, napięcia, obciążenia i zegary na obsługiwanym sprzęcie.","source":"https://github.com/LibreHardwareMonitor/LibreHardwareMonitor"},
{"title":"Test RAM — wzorce i ograniczenia","tags":"ram pamięć błąd test wzorce 00 FF AA 55 memtest","text":"Wzorce 00, FF, AA, 55 i pseudolosowe pomagają wykrywać część błędów zapisu/odczytu w przydzielonym buforze. Test aplikacyjny nie sprawdza całej fizycznej pamięci i nie zastępuje niezależnego testu rozruchowego. Zapisuj ilość rzeczywiście przetestowanej pamięci, liczbę porównań i błędy; nie oznaczaj całego RAM jako sprawnego tylko dlatego, że mały bufor przeszedł.","source":"https://www.memtest.org/"},
{"title":"SSD, HDD i pomiar prędkości dysku","tags":"ssd hdd nvme dysk benchmark odczyt zapis MB/s IOPS","text":"Wynik zależy od rozmiaru pliku, cache, zajętości, temperatury, trybu zasilania i rodzaju operacji. Test pliku tymczasowego mierzy konkretną operację w konkretnym miejscu — nie jest pełnym testem powierzchni ani wszystkich IOPS. Używaj pliku testowego ograniczonego rozmiarem, usuwaj go po zakończeniu i nie wykonuj testów niszczących dane bez wyraźnej zgody.","source":"https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/chkdsk"},
{"title":"SMART i diagnostyka nośników","tags":"SMART NVMe SSD HDD błędy wear health dysk","text":"SMART i telemetria nośnika mogą pokazywać błędy odczytu/zapisu, zużycie, temperaturę lub ostrzeżenia producenta. Zestaw dostępnych atrybutów zależy od urządzenia, sterownika i mostka USB. Brak danych SMART nie oznacza zerowej liczby błędów. Przy podejrzeniu awarii najpierw wykonaj kopię danych, a ciężkie skanowanie powierzchni zostaw na zabezpieczonym obrazie lub po kopii.","source":"https://learn.microsoft.com/en-us/windows-hardware/drivers/storage/"},
{"title":"Odzyskiwanie danych po awarii dysku","tags":"odzyskiwanie dane recovery dysk uszkodzony backup","text":"Przy klikaniu, znikaniu urządzenia, błędach I/O lub ważnych danych ogranicz zapisy na oryginalnym nośniku. Najpierw oceń ryzyko, skopiuj dane lub wykonaj obraz sektorowy na inny dysk. Nie zapisuj odzyskanych plików na tym samym nośniku. Przy fizycznym uszkodzeniu kolejne uruchomienia mogą pogorszyć stan urządzenia.","source":"https://www.cisa.gov/stopransomware"},
{"title":"Windows SFC — kontrola plików systemowych","tags":"windows sfc scannow naprawa pliki systemowe","text":"SFC /scannow sprawdza chronione pliki systemowe i próbuje naprawić uszkodzenia korzystając ze źródeł lokalnych. Zapisuj kod wyjścia i pełny log. Gdy magazyn składników jest uszkodzony, SFC może nie móc naprawić wszystkiego; wtedy użyj zalecanej procedury DISM, a następnie ponownie SFC.","source":"https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sfc"},
{"title":"DISM — magazyn składników Windows","tags":"windows dism restorehealth scanhealth checkhealth naprawa","text":"DISM /Online /Cleanup-Image /CheckHealth wykonuje szybką kontrolę stanu, /ScanHealth skanuje magazyn składników, a /RestoreHealth próbuje naprawy. Naprawa może długo trwać i potrzebować źródeł Windows Update lub wskazanego obrazu. Uruchamiaj polecenia z prawami administratora, zachowuj logi i nie zamykaj procesu tylko dlatego, że procent postępu długo się nie zmienia.","source":"https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/repair-a-windows-image"},
{"title":"CHKDSK — system plików","tags":"chkdsk dysk skanowanie /scan naprawa","text":"CHKDSK sprawdza logiczną spójność systemu plików. Na woluminie NTFS tryb /scan wykonuje skan online; operacje naprawcze mogą wymagać blokady lub restartu. CHKDSK nie zastępuje kopii zapasowej i nie powinien być pierwszym działaniem przy fizycznie umierającym nośniku z jedyną kopią danych.","source":"https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/chkdsk"},
{"title":"GPU — obciążenie, VRAM i temperatura","tags":"gpu karta graficzna vram obciążenie temperatura zegar fps","text":"Rozdziel identyfikację adaptera, stan sterownika, obciążenie silników GPU, użycie VRAM, temperaturę i test renderowania. Liczniki różnią się zależnie od sterownika. NVIDIA nvidia-smi może zwracać temperaturę, zegary i pamięć; Windows GPU Performance Counters mogą udostępniać część wykorzystania/pamięci. N/D oznacza brak dostępnego licznika, nie usterkę i nie wynik 0.","source":"https://developer.nvidia.com/system-management-interface"},
{"title":"Benchmark 3D i interpretacja FPS","tags":"3d benchmark fps OpenGL Direct3D renderowanie GPU wynik","text":"FPS można porównywać tylko dla tej samej sceny, rozdzielczości, ustawień synchronizacji i konfiguracji. Wynik jednej sceny nie przewiduje FPS wszystkich gier. Raportuj renderer, wersję API, rozdzielczość, czas trwania, średni FPS i percentyle, jeśli są mierzone. Test musi faktycznie renderować geometrię przez sterownik — animacja dekoracyjna nie jest benchmarkiem.","source":"https://learn.microsoft.com/en-us/windows/win32/direct3d"},
{"title":"Windows WinSAT i Direct3D","tags":"winsat d3d direct3d benchmark windows grafika","text":"WinSAT może mierzyć niektóre cechy wydajności Windows, ale nie jest bezpośrednim zamiennikiem współczesnego benchmarku gier. Zachowaj jego wyjście, czas i kod zakończenia. Nie opisuj identyfikacji karty jako wyniku testu wydajności.","source":"https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/winsat"},
{"title":"Test sieci — download, upload i opóźnienie","tags":"internet speedtest speed test download upload Mbps ping jitter cloudflare","text":"Przepustowość należy mierzyć rzeczywistymi bajtami przesłanymi w czasie, a nie szacować na podstawie stanu interfejsu. Wynik zależy od serwera, trasy, Wi-Fi, obciążenia sieci i limitów ISP. Zapisuj rozmiar transferu, czas, wynik Mbps i status HTTP. Krótki test zużywa dane; nie uruchamiaj wielogigabajtowego transferu bez zgody. Cloudflare Speed Test udostępnia endpointy __down i __up.","source":"https://github.com/cloudflare/speedtest"},
{"title":"Ping, jitter i utrata pakietów","tags":"ping latency jitter packet loss opóźnienie internet","text":"Ping to czas odpowiedzi, jitter opisuje zmienność opóźnienia, a packet loss odsetek utraconych pakietów. Nie utożsamiaj jednego żądania HTTPS z czystym pingiem ICMP. Do rzetelnej diagnozy zmierz kilka próbek, podaj metodę i liczbę prób, a wyniki porównuj przez Ethernet i Wi-Fi osobno.","source":"https://www.cloudflare.com/learning/performance/glossary/what-is-latency/"},
{"title":"Wi-Fi kontra Ethernet","tags":"wifi ethernet lan sieć prędkość zasięg kanał","text":"Na wynik Wi-Fi wpływa pasmo, szerokość kanału, zakłócenia, dystans, ściany i możliwości klienta/AP. Porównaj test przy routerze i przez Ethernet. Nie diagnozuj winy operatora wyłącznie na podstawie pojedynczego pomiaru w sieci Wi-Fi.","source":"https://support.microsoft.com/windows"},
{"title":"Bateria laptopa i raport powercfg","tags":"bateria laptop powercfg batteryreport health cycle capacity","text":"Raport baterii pokazuje m.in. pojemność projektową, pełnego naładowania i historię użytkowania, jeśli kontroler udostępnia dane. Zdrowie wyliczaj tylko wtedy, gdy obie pojemności są wiarygodne. W PC stacjonarnym brak baterii jest stanem N/D, a nie błędem komputera.","source":"https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/powercfg-command-line-options"},
{"title":"EDID i diagnostyka matrycy","tags":"matryca ekran monitor edid dead pixel piksele","text":"EDID identyfikuje część informacji monitora, ale nie wykrywa samodzielnie wszystkich martwych pikseli, smug ani problemów podświetlenia. Do testu pikseli pokazuj pełnoekranowe kolory, gradienty i wzorce; wynik wad pikseli wymaga wzrokowego potwierdzenia człowieka.","source":"https://learn.microsoft.com/en-us/windows-hardware/drivers/display/"},
{"title":"Menedżer urządzeń i kody błędów","tags":"device manager menedżer urządzeń sterownik code 10 43","text":"Stan PnP i kod błędu urządzenia wskazują problemy z inicjalizacją lub sterownikiem, ale sam kod nie określa zawsze przyczyny. Zapisz nazwę, identyfikator sprzętowy, dostawcę sterownika i kod błędu; zmiany sterowników rób z oficjalnego źródła producenta.","source":"https://learn.microsoft.com/en-us/windows-hardware/drivers/install/device-manager"},
{"title":"Bezpieczna aktualizacja sterowników i BIOS","tags":"sterowniki driver BIOS UEFI firmware aktualizacja","text":"Dobieraj BIOS/UEFI wyłącznie do dokładnego modelu i rewizji urządzenia. Zapewnij stabilne zasilanie, zapisz klucz BitLocker i przeczytaj oficjalne instrukcje producenta. Nie wykonuj flashowania na podstawie niepotwierdzonego modelu lub pliku bez kontroli podpisu/sumy.","source":"https://support.microsoft.com/windows"},
{"title":"Ochrona antywirusowa i podejrzany plik","tags":"antywirus malware virus bitdefender defender quarantine trojan","text":"Jeśli program antywirusowy zgłasza wykrycie, nie wyłączaj ochrony i nie przywracaj pliku z kwarantanny, aby wymusić uruchomienie. Sprawdź źródło, podpis cyfrowy, SHA-256 i ocenę dostawcy. Suma SHA-256 potwierdza zgodność pliku, ale sama nie dowodzi, że plik jest bezpieczny.","source":"https://www.cisa.gov/secure-our-world"},
{"title":"Ransomware i kopie zapasowe","tags":"ransomware backup kopia zapasowa malware","text":"Przy podejrzeniu ransomware odłącz urządzenie od sieci, nie podłączaj kopii zapasowych, które mają być czyste, i nie usuwaj logów. Zabezpiecz dowody oraz zgłoś incydent zgodnie z procedurą. Kopie zapasowe powinny być odseparowane i okresowo testowane przez przywracanie.","source":"https://www.cisa.gov/stopransomware"},
{"title":"Autostart i wydajność Windows","tags":"autostart startup programy wydajność boot","text":"Lista autostartu może pomóc wykryć niepotrzebne aplikacje, ale nazwa pliku sama nie wystarcza do oznaczenia malware. Oceniaj podpis, ścieżkę, wydawcę i reputację. Przed wyłączeniem zapisuj stan i zapewnij możliwość przywrócenia.","source":"https://learn.microsoft.com/en-us/sysinternals/"},
{"title":"Windows Performance Counters","tags":"windows liczniki wydajności CPU pamięć dysk GPU telemetry","text":"Liczniki wydajności Windows udostępniają ustandaryzowane próbki CPU, pamięci, dysku i wybranych silników GPU. Nie każdy zestaw liczników istnieje na każdej edycji/systemie/sterowniku. Gdy licznik jest nieobecny, pokaż niedostępność z nazwą metody — nie podstawiaj wartości losowej ani stałej.","source":"https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-counter"},
{"title":"LibreHardwareMonitor — sensory","tags":"LibreHardwareMonitor czujniki temperatury wentylator napięcie CPU GPU","text":"LibreHardwareMonitor udostępnia bibliotekę i aplikację Windows do monitorowania temperatur, obrotów, napięć, obciążenia i zegarów obsługiwanych urządzeń. Dostępność sensorów zależy od sprzętu i sterowników, a niektóre wymagają uprawnień administratora. Zapoznaj się z licencją MPL-2.0 oraz innymi notami licencyjnymi przed dystrybucją biblioteki razem z programem.","source":"https://github.com/LibreHardwareMonitor/LibreHardwareMonitor"},
{"title":"Diagnostyka wentylatorów i chłodzenia","tags":"wentylator fan rpm cooling chłodzenie termika pasta termiczna","text":"Zmienny hałas, spadek zegarów pod obciążeniem i skoki temperatury mogą wskazywać problem chłodzenia, ale nie są samodzielnym dowodem uszkodzenia. Porównaj odczyty na biegu jałowym i pod kontrolowanym obciążeniem, sprawdź obroty oraz przepływ powietrza. Nie zgaduj obrotów, jeśli płyta ich nie udostępnia.","source":"https://www.intel.com/content/www/us/en/support.html"},
{"title":"Czyszczenie po zalaniu","tags":"zalanie ciecz laptop serwis czyszczenie korozja","text":"Po zalaniu wyłącz urządzenie i odłącz zasilanie, nie próbuj ponownie uruchamiać mokrej płyty. W serwisie dokumentuj zakres uszkodzeń, odłącz baterię według instrukcji modelu i wykonuj czyszczenie zgodnie z procedurą. Uszkodzenia cieczą wymagają oceny fizycznej; test programowy nie może zagwarantować braku korozji.","source":"https://www.cisa.gov/"},
{"title":"Test kamery, mikrofonu i głośników","tags":"kamera webcam mikrofon audio speaker dźwięk test","text":"Test kamery powinien pokazać rzeczywisty podgląd oraz rozdzielczość i liczbę klatek. Mikrofon powinien zmierzyć rzeczywiście odebrane próbki i poziom RMS; głośniki wymagają odtworzenia sygnału i często potwierdzenia słuchowego. Brak dostępu, uprawnienia prywatności lub brak urządzenia powinny być opisane jako blokada/N/D, nie zaliczenie testu.","source":"https://support.microsoft.com/windows"},
{"title":"Test USB i urządzeń Plug and Play","tags":"USB urządzenia PnP test port napięcie","text":"Lista urządzeń PnP potwierdza enumerację urządzenia, ale nie dowodzi poprawności zasilania portu, integralności sygnału ani transferu z pełną szybkością. Do diagnostyki portu użyj znanego sprawnego urządzenia i odpowiedniego miernika; raportuj osobno wykrycie i rzeczywisty transfer.","source":"https://learn.microsoft.com/en-us/windows-hardware/drivers/"},
{"title":"Wiarygodność testów i raportów","tags":"raport test PASS WARN FAIL wiarygodność dowody","text":"Każdy wynik powinien zawierać nazwę testu, metodę, godzinę, faktyczne dane pomiarowe, czas trwania i ograniczenia. Rozróżniaj PASS, FAIL, WARN i N/D. Sam fakt wykrycia urządzenia nie jest dowodem stabilności, a uruchomienie testu nie oznacza jego zaliczenia.","source":"https://learn.microsoft.com/en-us/windows/win32/perfctrs/about-performance-counters"},
{"title":"AI Reader — ocena źródeł internetowych","tags":"AI czytnik internet wiedza źródła cytowanie wiarygodność","text":"Wyniki wyszukiwania są punktami wejścia, nie całą wiedzą Internetu. Preferuj dokumentację producenta, Microsoft Learn, normy i repozytoria źródłowe. W odpowiedzi pokazuj link do źródła, datę pobrania i fragment, a wnioski oddziel od cytowanych faktów. Treści zapisane z Internetu powinny być powiązane z URL i możliwe do usunięcia/odświeżenia.","source":"https://learn.microsoft.com/"},
{"title":"Interpretacja temperatur — bez uniwersalnego limitu","tags":"temperatura limit CPU GPU thermal max temperatura progi","text":"Nie stosuj jednego progu temperatury dla wszystkich procesorów i kart graficznych. Limit zależy od konkretnego modelu i specyfikacji producenta, a czujniki mogą używać różnych nazw (CPU Package, Tctl, GPU Hotspot). Podawaj dokładną nazwę sensora i porównuj z dokumentacją modelu.","source":"https://www.intel.com/content/www/us/en/support.html"},
{"title":"Pomiar sieci przez Cloudflare Speed Test","tags":"Cloudflare speed.cloudflare.com __down __up download upload","text":"Cloudflare Speed Test wykonuje transfery download i upload przez endpointy __down oraz __up. Własny pomiar aplikacji musi uwzględniać rozmiar faktycznie odebranych/wysłanych bajtów oraz czas. Endpoint może odmówić ruchu w pewnych warunkach; wtedy pokaż błąd połączenia zamiast fałszywego wyniku.","source":"https://github.com/cloudflare/speedtest"},
{"title":"Zarządzanie energią i tryb wydajności","tags":"zasilanie power plan laptop bateria throttling Windows","text":"Tryb oszczędzania energii może zmieniać zegary i wydajność. Przed benchmarkiem zapisuj plan zasilania, temperaturę otoczenia, ustawienia grafiki oraz czy laptop jest podłączony do zasilacza. Powtarzalne porównanie wymaga tych samych warunków.","source":"https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/powercfg-command-line-options"},
{"title":"Aktualizacje Windows","tags":"Windows Update aktualizacja poprawki security patch","text":"Aktualizacje Windows mogą wymagać restartu i zmieniać wersję sterowników lub plików systemowych. Przed diagnostyką sprawdź historię aktualizacji, oczekujący restart i kod błędu. Nie usuwaj komponentów systemowych automatycznie bez raportu i możliwości cofnięcia zmiany.","source":"https://support.microsoft.com/windows"},
{"title":"Diagnostyka pamięci GPU — test VRAM","tags":"VRAM texture allocation upload readback GPU memory error","text":"Test alokacji i odczytu zwrotnego tekstur sprawdza tylko przydzielony obszar pamięci i ścieżkę sterownika/API. Nie jest to pełny test wszystkich fizycznych komórek VRAM. Raportuj żądaną i faktycznie zaalokowaną pamięć, wzorce, liczbę bajtów zweryfikowanych i błędy API.","source":"https://developer.nvidia.com/system-management-interface"},
{"title":"Windows Device Health i zdarzenia","tags":"event viewer reliability monitor Windows logs błędy system","text":"Podgląd zdarzeń i Monitor niezawodności pomagają skorelować zawieszenia, restarty, awarie sterownika i błędy dysku z czasem wystąpienia. W raporcie zachowuj źródło zdarzenia, Event ID, czas i treść, a nie tylko liczbę zdarzeń.","source":"https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil"},
{"title":"Naprawa aktualizatora i sprawdzanie plików","tags":"SHA256 update manifest installer signature security download","text":"Bezpieczny aktualizator pobiera przez HTTPS, ogranicza hosty i rozmiar, porównuje SHA-256 i sprawdza format PE przed uruchomieniem. Hash potwierdza zgodność z manifestem, ale nie zastępuje podpisu cyfrowego/reputacji antywirusa. Nie obchodź kwarantanny i nie wyłączaj ochrony, aby wymusić uruchomienie.","source":"https://learn.microsoft.com/en-us/windows/security/"},
{"title":"Narzędzia do diagnozy Windows","tags":"Windows msinfo32 perfmon resmon task manager process performance","text":"MSINFO32 pokazuje sprzęt i konfigurację systemu; PerfMon i Resource Monitor pomagają obserwować wykorzystanie zasobów. Uruchom narzędzie tylko wtedy, gdy użytkownik wybrał tę operację, a raport powinien określać, jakie dane faktycznie odczytano.","source":"https://learn.microsoft.com/en-us/windows/"},
{"title":"Wiedza producentów CPU/GPU","tags":"Intel AMD NVIDIA support official product specifications","text":"Do oceny dokładnego modelu korzystaj z dokumentacji producenta. Limity temperatury, maksymalne zegary, obsługa funkcji i pamięć różnią się między generacjami, SKU i wersjami BIOS. Jeśli model jest niepewny, nie dopasowuj specyfikacji na podstawie podobnej nazwy.","source":"https://www.intel.com/content/www/us/en/support.html"}
]

_U66_SCENES = [
("01 — Geometryczne kostki", "boxes", 12),
("02 — Gęsta siatka obiektów", "grid", 24),
("03 — Wireframe stress", "wire", 20),
("04 — Pole sfer", "spheres", 8),
("05 — Torusy proceduralne", "torus", 8),
("06 — Teren trójkątowy", "terrain", 18),
("07 — Wieżowce / city", "city", 70),
("08 — Płytka GPU i chłodzenie", "gpu", 8),
("09 — Ruchome cząstki", "particles", 220),
("10 — Obracające się pierścienie", "rings", 22),
("11 — Strumień trójkątów", "triangles", 900),
("12 — Gęsty mesh", "mesh", 26),
("13 — Pokój 3D", "room", 28),
("14 — Planety i orbity", "planets", 9),
("15 — Fale terenu", "waves", 28),
("16 — Wiele materiałów / kolorów", "materials", 80),
("17 — Sześciany z głębią", "cubes", 90),
("18 — Podwójna geometria", "mixed", 140),
("19 — Extreme triangle load", "triangles_extreme", 3500),
("20 — Ultimate mixed load", "ultimate", 2400),
("21 — CPU Core Matrix / wielowątkowość", "cpu_core_matrix", 180),
("22 — CPU Thread Swarm / obciążenie geometrii", "particles", 480),
("23 — CPU Pipeline Rings", "rings", 64),
("24 — CPU Vector Throughput", "triangles", 3200),
("25 — RAM Address Matrix", "ram_address_matrix", 240),
("26 — RAM Bitfield / wzorce", "materials", 350),
("27 — RAM Bandwidth Visualizer", "triangles", 5200),
("28 — RAM Burst Stress", "ultimate", 700),
("29 — SSD/NVMe Sequential I/O", "disk_sequential", 3600),
("30 — SSD Random I/O / kolejki", "disk_random", 420),
("31 — NVMe Queue / PCIe lanes", "rings", 96),
("32 — Disk Queue Mesh", "mixed", 550),
("33 — VRAM Texture Tiles", "vram_texture_tiles", 180),
("34 — VRAM Fillrate / render target", "triangles_extreme", 8000),
("35 — GPU Shader Geometry Stress", "triangles_extreme", 12000),
("36 — GPU Tiled Composite", "ultimate", 1400),
("37 — PCIe / interfejsy wejścia-wyjścia", "pcie_bus", 500),
("38 — Matryca / Pixel Grid 3D", "display_pixels", 220),
("39 — Chłodzenie / airflow simulation", "waves", 64),
("40 — ULTRA MAX Composite Scene", "ultimate", 2800)
]

def _u66_store_dir():
    root = _u66_os.environ.get("LOCALAPPDATA") or str(Path.home())
    path = Path(root) / "NaprawaPC" / "AIReader"
    path.mkdir(parents=True, exist_ok=True)
    return path

def _u66_saved_knowledge():
    path = _u66_store_dir() / "knowledge_base.json"
    try:
        obj = _u66_json.loads(path.read_text(encoding="utf-8"))
        return obj if isinstance(obj, list) else []
    except Exception:
        try:
            path.write_text(_u66_json.dumps([], ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception:
            pass
        return []

def _u66_save_knowledge(items):
    path = _u66_store_dir() / "knowledge_base.json"
    current = _u66_saved_knowledge()
    by_key = {}
    for item in current:
        if not isinstance(item, dict):
            continue
        source = str(item.get("source", "")).strip()
        title = str(item.get("title", "Zapisany artykuł")).strip()
        by_key[(source, title)] = item
    changed = 0
    for item in items:
        if not isinstance(item, dict):
            continue
        body = str(item.get("text", "")).strip()[:500000]
        source = str(item.get("source", "")).strip()[:2000]
        title = str(item.get("title", "Zapisany artykuł")).strip()[:500]
        if not body or len(body) < 40:
            continue
        key = (source, title)
        normalized = {
            "title": title,
            "tags": str(item.get("tags", ""))[:1000],
            "text": body,
            "source": source,
            "saved_at": _U66_datetime.now().isoformat(timespec="seconds"),
        }
        previous = by_key.get(key)
        if not previous or any(previous.get(k) != normalized.get(k) for k in ("tags", "text", "source", "title")):
            changed += 1
        by_key[key] = normalized
    values = list(by_key.values())[-500:]
    path.write_text(_u66_json.dumps(values, ensure_ascii=False, indent=2), encoding="utf-8")
    return changed, path

def _u66_all_knowledge():
    return list(_U66_KNOWLEDGE_SEED) + _u66_saved_knowledge()

def _u66_rank_knowledge(query, docs=None, limit=8):
    docs = docs if docs is not None else _u66_all_knowledge()
    words = [x for x in _u66_re.findall(r"[a-z0-9ąćęłńóśżź]{3,}", str(query).lower()) if x not in {"oraz","który","która","jest","czyli","this","with","from","that","when","where","what","how"}]
    ranked = []
    for doc in docs:
        if not isinstance(doc,dict):
            continue
        title = str(doc.get("title",""))
        tags = str(doc.get("tags",""))
        body = str(doc.get("text",""))
        hay = (title + " " + tags + " " + body).lower()
        score = sum(5 for w in words if w in title.lower()) + sum(3 for w in words if w in tags.lower()) + sum(1 for w in words if w in hay)
        if not words:
            score = 1
        if score:
            ranked.append((score,doc))
    ranked.sort(key=lambda x:(x[0],len(str(x[1].get("text","")))),reverse=True)
    return [dict(x[1],_score=x[0]) for x in ranked[:max(1,limit)]]

class _U66_DDGParser(_U66_HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items=[]
        self.mode=None
        self.current=None
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        cls=str(a.get("class","")).split()
        if tag=="a" and "result__a" in cls:
            self.current={"title":"","text":"","source":a.get("href",""),"tags":"internet"}
            self.items.append(self.current)
            self.mode="title"
        elif tag in ("a","div") and "result__snippet" in cls:
            if self.items:
                self.current=self.items[-1]
                self.mode="snippet"
        elif tag=="br" and self.mode=="snippet" and self.current is not None:
            self.current["text"] += " "
    def handle_data(self, data):
        if self.current is not None and self.mode in ("title","snippet"):
            key="title" if self.mode=="title" else "text"
            self.current[key] += data
    def handle_endtag(self, tag):
        if tag=="a" and self.mode=="title":
            self.mode=None
        elif tag=="div" and self.mode=="snippet":
            self.mode=None
    def close(self):
        super().close()
        for item in self.items:
            item["title"]=_u66_re.sub(r"\s+"," ",item.get("title","")).strip()
            item["text"]=_u66_re.sub(r"\s+"," ",item.get("text","")).strip()

def _u66_web_search(query, maximum=8):
    results=[]
    headers={"User-Agent":"NAPRAWA-PC-HARDWARE-TEST-PRO/AIReader (desktop diagnostic app)","Accept":"text/html,application/json"}
    q=_u66_urlparse.quote(str(query)[:240])
    try:
        req=_u66_request.Request("https://html.duckduckgo.com/html/?q="+q,headers=headers)
        with _u66_request.urlopen(req,timeout=12) as response:
            raw=response.read(2*1024*1024).decode("utf-8","replace")
        parser=_U66_DDGParser()
        parser.feed(raw)
        for item in parser.items:
            url=str(item.get("source",""))
            if url.startswith("//"):
                url="https:"+url
            parsed=_u66_urlparse.urlparse(url)
            if parsed.scheme not in ("http","https"):
                continue
            params=_u66_urlparse.parse_qs(parsed.query)
            if "uddg" in params:
                url=params["uddg"][0]
            if item.get("title") and url:
                results.append({"title":item["title"],"text":item.get("text",""),"source":url,"tags":"internet-search"})
            if len(results)>=maximum:
                break
    except Exception as exc:
        web_error=f"Wyszukiwarka DuckDuckGo: {type(exc).__name__}: {exc}"
    else:
        web_error=""
    if len(results)<3:
        try:
            wurl="https://pl.wikipedia.org/w/api.php?action=query&list=search&srsearch="+q+"&format=json&utf8=1&srlimit=5"
            req=_u66_request.Request(wurl,headers={"User-Agent":"NAPRAWA-PC-HARDWARE-TEST-PRO/AIReader"})
            with _u66_request.urlopen(req,timeout=10) as response:
                data=_u66_json.loads(response.read(1024*1024).decode("utf-8","replace"))
            for item in data.get("query",{}).get("search",[]):
                title=str(item.get("title",""))
                page="https://pl.wikipedia.org/wiki/"+_u66_urlparse.quote(title.replace(" ","_"))
                summary=_u66_re.sub(r"<[^>]+>"," ",str(item.get("snippet","")))
                summary=_u66_html.unescape(_u66_re.sub(r"\s+"," ",summary)).strip()
                results.append({"title":title,"text":summary,"source":page,"tags":"Wikipedia"})
        except Exception as exc:
            if not web_error:
                web_error=f"Wikipedia API: {type(exc).__name__}: {exc}"
    unique=[]
    seen=set()
    for result in results:
        url=result.get("source","")
        if url and url not in seen:
            seen.add(url); unique.append(result)
    if not unique and web_error:
        raise RuntimeError(web_error)
    return unique[:maximum]

class _U66_TextParser(_U66_HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts=[]
        self.title_parts=[]
        self._skip=0
        self._in_title=False
    def handle_starttag(self, tag, attrs):
        if tag in ("script","style","noscript","svg"):
            self._skip += 1
        if tag=="title":
            self._in_title=True
        if tag in ("p","br","div","li","h1","h2","h3","tr","article","section"):
            self.parts.append("\n")
    def handle_endtag(self, tag):
        if tag in ("script","style","noscript","svg") and self._skip:
            self._skip -= 1
        if tag=="title":
            self._in_title=False
        if tag in ("p","div","li","h1","h2","h3","tr","article","section"):
            self.parts.append("\n")
    def handle_data(self, data):
        if self._skip:
            return
        value=_u66_re.sub(r"\s+"," ",data).strip()
        if value:
            self.parts.append(value+" ")
            if self._in_title:
                self.title_parts.append(value)
    def result(self):
        text=_u66_re.sub(r"[ \t]+\n","\n","".join(self.parts))
        text=_u66_re.sub(r"\n{3,}","\n\n",text)
        return " ".join(self.title_parts).strip(),text.strip()

def _u66_read_web_page(url):
    parsed=_u66_urlparse.urlparse(str(url).strip())
    if parsed.scheme not in ("http","https") or not parsed.hostname:
        raise ValueError("Adres musi zaczynać się od http:// lub https://.")
    req=_u66_request.Request(str(url).strip(),headers={"User-Agent":"NAPRAWA-PC-HARDWARE-TEST-PRO/AIReader","Accept":"text/html,text/plain,application/pdf"})
    with _u66_request.urlopen(req,timeout=15) as response:
        final=_u66_urlparse.urlparse(response.geturl())
        if final.scheme not in ("http","https"):
            raise ValueError("Przekierowanie do nieobsługiwanego protokołu.")
        data=response.read(2*1024*1024)
        ctype=response.headers.get("Content-Type","").lower()
    if "pdf" in ctype or str(url).lower().endswith(".pdf"):
        try:
            import fitz as _u66_fitz
            doc=_u66_fitz.open(stream=data,filetype="pdf")
            text="\n".join(page.get_text("text") for page in doc[:80])[:500000]
            title=parsed.path.rsplit("/",1)[-1] or "Dokument PDF"
        except Exception:
            raise RuntimeError("To jest PDF. Do odczytu bezpośredniego potrzebny jest obsługiwany parser PDF; użyj importu pliku PDF, jeśli biblioteka jest dostępna.")
    elif "html" in ctype or b"<html" in data[:512].lower():
        parser=_U66_TextParser()
        parser.feed(data.decode("utf-8","replace"))
        title,text=parser.result()
    else:
        title=parsed.path.rsplit("/",1)[-1] or parsed.hostname
        text=data.decode("utf-8","replace")
    if not text.strip():
        raise RuntimeError("Strona nie udostępniła czytelnej treści. Może wymagać JavaScript, logowania lub blokować automatyczny odczyt.")
    return {"title":title or parsed.hostname,"text":text[:500000],"source":str(url),"tags":"wczytana strona internetowa","saved_at":_U66_datetime.now().isoformat(timespec="seconds")}

_U66_KNOWLEDGE_PACK_URL = "https://raw.githubusercontent.com/naprawapclaptop1-dev/serwis-ai-chat/main/hardware-test-pro/AI_READER_KNOWLEDGE_PL.json"
_U66_KNOWLEDGE_PACK_FORMAT = "naprawapc-ai-reader-knowledge"
_U66_KNOWLEDGE_MAX_BYTES = 5 * 1024 * 1024
_U66_KNOWLEDGE_MAX_ARTICLES = 500

def _u66_sync_knowledge_failed(self, detail, automatic=False):
    try:
        self._u66_kb_sync_running = False
    except Exception:
        pass
    message = "Nie udało się pobrać bazy wiedzy online: " + str(detail)[:1200]
    try:
        if hasattr(self, "_u66_reader_status") and self._u66_reader_status.winfo_exists():
            self._u66_reader_status.config(text=message)
    except Exception:
        pass
    try:
        self.append_log("AI Reader: " + message)
    except Exception:
        pass
    if not automatic:
        try:
            messagebox.showerror("Aktualizacja bazy Czytnika AI", message)
        except Exception:
            pass

def _u66_sync_knowledge_from_server(self, automatic=False):
    if getattr(self, "_u66_kb_sync_running", False):
        return
    state_path = _u66_store_dir() / "knowledge_sync.json"
    if automatic:
        try:
            state = _u66_json.loads(state_path.read_text(encoding="utf-8"))
            stamp = _U66_datetime.fromisoformat(str(state.get("last_success", "")))
            age = (_U66_datetime.now() - stamp).total_seconds()
            if 0 <= age < 12 * 60 * 60:
                if hasattr(self, "_u66_reader_status"):
                    self._u66_reader_status.config(
                        text=f"Baza lokalna: {len(_U66_KNOWLEDGE_SEED)} tematów wbudowanych + {len(_u66_saved_knowledge())} zapisanych. Ostatnia synchronizacja: {stamp:%Y-%m-%d %H:%M}."
                    )
                return
        except Exception:
            pass
    self._u66_kb_sync_running = True
    try:
        if hasattr(self, "_u66_reader_status"):
            self._u66_reader_status.config(text="Pobieranie kuratorowanej bazy wiedzy przez HTTPS…")
    except Exception:
        pass

    def job():
        try:
            headers = {
                "User-Agent": "NAPRAWA-PC-HARDWARE-TEST-PRO/AIReader",
                "Accept": "application/json",
                "Cache-Control": "no-cache",
            }
            request = _u66_request.Request(_U66_KNOWLEDGE_PACK_URL, headers=headers)
            with _u66_request.urlopen(request, timeout=25) as response:
                final = _u66_urlparse.urlparse(response.geturl())
                if final.scheme != "https" or (final.hostname or "").lower() != "raw.githubusercontent.com":
                    raise ValueError("Adres paczki przekierował poza dozwolony serwer HTTPS GitHub.")
                raw = response.read(_U66_KNOWLEDGE_MAX_BYTES + 1)
            if len(raw) > _U66_KNOWLEDGE_MAX_BYTES:
                raise ValueError("Paczka wiedzy przekracza limit 5 MB.")
            pack = _u66_json.loads(raw.decode("utf-8"))
            if not isinstance(pack, dict) or pack.get("format") != _U66_KNOWLEDGE_PACK_FORMAT:
                raise ValueError("Nieprawidłowy format bazy wiedzy.")
            version = str(pack.get("version", "")).strip()[:80]
            articles = pack.get("articles")
            if not version or not isinstance(articles, list) or not articles or len(articles) > _U66_KNOWLEDGE_MAX_ARTICLES:
                raise ValueError("Paczka nie zawiera prawidłowej wersji lub listy artykułów.")
            clean = []
            for item in articles:
                if not isinstance(item, dict):
                    continue
                title = str(item.get("title", "")).strip()[:300]
                tags = str(item.get("tags", "")).strip()[:800]
                body = str(item.get("text", "")).strip()[:30000]
                source = str(item.get("source", "")).strip()[:1500]
                parsed = _u66_urlparse.urlparse(source)
                if not title or len(body) < 60:
                    continue
                if parsed.scheme != "https" or not parsed.hostname:
                    continue
                # Only import passive text and links; no page or article content is ever executed.
                clean.append({"title": title, "tags": tags, "text": body, "source": source})
            if not clean:
                raise ValueError("W paczce nie znaleziono artykułów ze źródłami HTTPS.")
            changed, db_path = _u66_save_knowledge(clean)
            state_path.write_text(
                _u66_json.dumps({
                    "version": version,
                    "articles_received": len(clean),
                    "last_success": _U66_datetime.now().isoformat(timespec="seconds"),
                    "database": str(db_path),
                }, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            def finish():
                self._u66_kb_sync_running = False
                saved_count = len(_u66_saved_knowledge())
                message = f"Baza wiedzy {version}: {len(clean)} artykułów pobranych; {changed} dodanych/zaktualizowanych. Łącznie lokalnie zapisano {saved_count}. Ścieżka: {db_path}"
                try:
                    if hasattr(self, "_u66_reader_status") and self._u66_reader_status.winfo_exists():
                        self._u66_reader_status.config(text=message)
                except Exception:
                    pass
                try:
                    self.append_log("AI Reader: " + message)
                except Exception:
                    pass
                try:
                    query = str(getattr(self, "_u66_reader_query", tk.StringVar(value="")).get()).strip()
                    if query and getattr(self, "current_view", "") == "AI_READER":
                        _u66_reader_search(self, False)
                except Exception:
                    pass
            self.queue_action(finish)
        except Exception as exc:
            detail = f"{type(exc).__name__}: {exc}"
            self.queue_action(lambda detail=detail, automatic=automatic: _u66_sync_knowledge_failed(self, detail, automatic))
    _u66_threading.Thread(target=job, name="NaprawaPCAIReaderKnowledgeSync", daemon=True).start()


def _u66_show_ai_reader(self):
    self.current_view="AI_READER"
    self.clear()
    t=self.colors()
    self.header_title.config(text="AI CZYTNIK WIEDZY — INTERNET + BAZA LOKALNA")
    intro=self.panel(self.content); intro.pack(fill="x",pady=(0,8))
    tk.Label(intro,text="AI KNOWLEDGE READER • wyszukiwanie źródeł, czytanie stron i lokalna biblioteka",bg=t["panel"],fg=t["accent"],font=self.fnt(13,"bold")).pack(anchor="w",padx=12,pady=(10,3))
    tk.Label(intro,text="To czytnik oparty na lokalnej bazie wiedzy i wyszukiwaniu internetowym. Nie pobiera „całego Internetu” naraz — znajdź temat, przeczytaj źródło i zapisz wybrane materiały do własnej bazy.",bg=t["panel"],fg=t["muted"],font=self.fnt(9),wraplength=1400,justify="left").pack(anchor="w",padx=12,pady=(0,10))
    row=tk.Frame(self.content,bg=t["bg"]); row.pack(fill="x",pady=3)
    self._u66_reader_query=tk.StringVar(value="")
    entry=ttk.Entry(row,textvariable=self._u66_reader_query,font=self.fnt(11))
    entry.pack(side="left",fill="x",expand=True,padx=3,ipady=5)
    self.make_button(row,"SZUKAJ W BAZIE",lambda:_u66_reader_search(self,False),"card",side="left",ipady=5)
    self.make_button(row,"SZUKAJ W INTERNECIE",lambda:_u66_reader_search(self,True),"accent",side="left",ipady=5)
    row2=tk.Frame(self.content,bg=t["bg"]); row2.pack(fill="x",pady=3)
    self._u66_reader_url=tk.StringVar(value="")
    ttk.Entry(row2,textvariable=self._u66_reader_url,font=self.fnt(9)).pack(side="left",fill="x",expand=True,padx=3,ipady=4)
    self.make_button(row2,"CZYTAJ URL",lambda:_u66_reader_load_url(self),"card",side="left",ipady=5)
    self.make_button(row2,"IMPORTUJ PDF/TXT/HTML",lambda:_u66_reader_import_file(self),"card",side="left",ipady=5)
    self.make_button(row2,"ZAPISZ WYNIKI",lambda:_u66_reader_save_results(self),"good",side="left",ipady=5)
    row3=tk.Frame(self.content,bg=t["bg"]); row3.pack(fill="x",pady=3)
    self.make_button(row3,"ANALIZUJ OSTATNIE TESTY",lambda:_u66_reader_analyze_tests(self),"accent",side="left",ipady=5)
    self.make_button(row3,"OTWÓRZ FOLDER BAZY",lambda:_u66_os.startfile(str(_u66_store_dir())) if _u66_os.name=="nt" else _u66_webbrowser.open("file://"+str(_u66_store_dir())),"card",side="left",ipady=5)
    self.make_button(row3,"AKTUALIZUJ / POBIERZ BAZĘ WIEDZY",lambda:_u66_sync_knowledge_from_server(self,automatic=False),"good",side="left",ipady=5)
    self._u66_reader_status=tk.Label(self.content,text=f"Baza wbudowana: {len(_U66_KNOWLEDGE_SEED)} tematów • Zapisane lokalnie: {len(_u66_saved_knowledge())} • Pakiet online jest aktualizowany osobno.",bg=t["bg"],fg=t["muted"],font=self.fnt(8),anchor="w")
    self._u66_reader_status.pack(fill="x",padx=4,pady=3)
    outer=tk.Frame(self.content,bg=t["panel"]); outer.pack(fill="both",expand=True,pady=(3,6))
    self._u66_reader_text=tk.Text(outer,wrap="word",bg=t["panel"],fg=t["fg"],insertbackground=t["fg"],font=self.fnt(10),relief="flat",padx=12,pady=10)
    scroll=ttk.Scrollbar(outer,orient="vertical",command=self._u66_reader_text.yview)
    self._u66_reader_text.configure(yscrollcommand=scroll.set)
    self._u66_reader_text.pack(side="left",fill="both",expand=True); scroll.pack(side="right",fill="y")
    self._u66_reader_text.tag_configure("title",foreground=t["accent"],font=self.fnt(12,"bold"))
    self._u66_reader_text.tag_configure("source",foreground=t["good"],underline=True)
    self._u66_reader_text.insert("end","Wpisz pytanie, np. „jak diagnozować temperaturę CPU i GPU”, „naprawa SFC/DISM”, „test prędkości Internetu” albo „NVMe SMART”. Wyszukiwanie internetowe pobiera wyniki na żądanie.\n","normal")
    self._u66_reader_results=[]
    entry.bind("<Return>",lambda e:_u66_reader_search(self,True))
    self.make_button(self.content,"← POWRÓT DO TESTÓW",self.show_tests_hub,"card",side="left",ipady=5)
    self.after(120,lambda:_u66_sync_knowledge_from_server(self,automatic=True))

def _u66_reader_render(self,heading,paragraph,items):
    try:
        box=self._u66_reader_text
        box.configure(state="normal"); box.delete("1.0","end")
        box.insert("end",heading+"\n","title")
        box.insert("end",paragraph+"\n\n")
        for idx,item in enumerate(items):
            box.insert("end",str(idx+1)+". "+str(item.get("title","Bez tytułu"))+"\n","title")
            text=str(item.get("text","")).strip()
            box.insert("end",(text[:5000] if text else "Brak krótkiego opisu. Otwórz źródło, aby przeczytać pełną treść.")+"\n")
            url=str(item.get("source",""))
            if url.startswith(("https://","http://","file://")):
                tag="u66source"+str(idx)
                box.insert("end","Źródło: "+url+"\n\n",("source",tag))
                box.tag_bind(tag,"<Button-1>",lambda e,u=url:_u66_webbrowser.open(u))
                box.tag_bind(tag,"<Enter>",lambda e:box.config(cursor="hand2"))
                box.tag_bind(tag,"<Leave>",lambda e:box.config(cursor=""))
            else:
                box.insert("end","Źródło: N/D\n\n")
        box.configure(state="disabled")
        try:
            self._u66_reader_status.config(text=f"Wyniki: {len(items)} • Baza lokalna + źródła internetowe; zapis wymaga kliknięcia „ZAPISZ WYNIKI”.")
        except Exception:
            pass
    except Exception as exc:
        try: self.append_log("AI Reader render: "+repr(exc))
        except Exception: pass

def _u66_reader_search(self, online=False):
    query=str(getattr(self,"_u66_reader_query",tk.StringVar(value="")).get()).strip()
    if not query:
        messagebox.showinfo("AI Czytnik","Wpisz temat lub pytanie.")
        return
    local=_u66_rank_knowledge(query,limit=8)
    self._u66_reader_results=list(local)
    _u66_reader_render(self,"WYNIKI BAZY LOKALNEJ",f"Zapytanie: {query}\nWiedza wbudowana: {len(_U66_KNOWLEDGE_SEED)} artykułów. Dopasowanie to wyszukiwanie treści, nie gwarancja kompletnej odpowiedzi.",local)
    if not online:
        return
    _u66_reader_render(self,"WYSZUKIWANIE INTERNETOWE",f"Zapytanie: {query}\nŁączenie z publicznymi źródłami HTTPS…",local)
    def job():
        try:
            web=_u66_web_search(query,8)
            combined=local+web
            def finish():
                self._u66_reader_results=combined
                _u66_reader_render(self,"LOKALNA BAZA + WYNIKI INTERNETOWE",f"Zapytanie: {query}\nWyniki Internetu są aktualne dla chwili wyszukania; sprawdź treść źródła i datę publikacji. Zapis do biblioteki jest lokalny.",combined)
            self.queue_action(finish)
        except Exception as exc:
            def failure():
                _u66_reader_render(self,"WYSZUKIWANIE NIEUDANE",f"{type(exc).__name__}: {exc}\nMożesz użyć bazy lokalnej lub otworzyć stronę źródłową w przeglądarce.",local)
            self.queue_action(failure)
    _u66_threading.Thread(target=job,name="NaprawaPCAIReaderSearch",daemon=True).start()

def _u66_reader_load_url(self):
    url=str(getattr(self,"_u66_reader_url",tk.StringVar(value="")).get()).strip()
    if not url:
        messagebox.showinfo("AI Czytnik","Wklej adres URL strony do przeczytania.")
        return
    _u66_reader_render(self,"CZYTANIE STRONY WWW","Pobieram tekst publicznej strony przez HTTPS/HTTP, limit 2 MB…",[])
    def job():
        try:
            item=_u66_read_web_page(url)
            def finish():
                self._u66_reader_results=[item]
                _u66_reader_render(self,"CZYTANA STRONA: "+item["title"],"Treść pobrana: "+str(len(item["text"]))+" znaków. Kliknij ZAPISZ WYNIKI, aby przechować ją lokalnie.",[item])
            self.queue_action(finish)
        except Exception as exc:
            self.queue_action(lambda:_u66_reader_render(self,"NIE UDAŁO SIĘ ODCZYTAĆ STRONY",f"{type(exc).__name__}: {exc}\nNiektóre witryny wymagają JavaScript, logowania lub blokują automatyczne pobranie.",[]))
    _u66_threading.Thread(target=job,name="NaprawaPCAIReaderPage",daemon=True).start()

def _u66_reader_import_file(self):
    path=_u66_filedialog.askopenfilename(title="Wybierz materiały do biblioteki AI",filetypes=[("Dokumenty","*.txt *.md *.html *.htm *.json *.pdf"),("Wszystkie pliki","*.*")])
    if not path:
        return
    try:
        p=Path(path)
        if p.stat().st_size>5*1024*1024:
            raise ValueError("Plik przekracza limit 5 MB.")
        if p.suffix.lower()==".pdf":
            text=""
            try:
                import pypdf as _u66_pypdf
                reader=_u66_pypdf.PdfReader(str(p))
                text="\n".join((page.extract_text() or "") for page in reader.pages[:100])
            except Exception:
                try:
                    import fitz as _u66_fitz
                    doc=_u66_fitz.open(str(p))
                    text="\n".join(page.get_text("text") for page in doc[:100])
                except Exception:
                    raise RuntimeError("Nie wykryto czytnika PDF wbudowanego w ten build; wybierz TXT/HTML lub skopiuj tekst z PDF.")
        else:
            raw=p.read_text(encoding="utf-8",errors="replace")
            if p.suffix.lower() in (".html",".htm"):
                parser=_U66_TextParser(); parser.feed(raw); title,text=parser.result()
            else:
                text=raw
        if not str(text).strip():
            raise RuntimeError("Nie znaleziono czytelnego tekstu w tym pliku.")
        item={"title":p.name,"text":str(text)[:500000],"source":p.resolve().as_uri(),"tags":"import lokalny","saved_at":_U66_datetime.now().isoformat(timespec="seconds")}
        added,db=_u66_save_knowledge([item])
        self._u66_reader_results=[item]
        _u66_reader_render(self,"ZAIMPORTOWANO DOKUMENT",f"Zapisano materiał do lokalnej biblioteki. Plik: {p}\nBaza: {db}",[item])
    except Exception as exc:
        messagebox.showerror("AI Czytnik — import",f"{type(exc).__name__}: {exc}")

def _u66_reader_save_results(self):
    items=list(getattr(self,"_u66_reader_results",[]) or [])
    if not items:
        messagebox.showinfo("AI Czytnik","Brak wyników do zapisania. Najpierw wyszukaj temat lub wczytaj dokument.")
        return
    added,path=_u66_save_knowledge(items)
    try:
        self._u66_reader_status.config(text=f"Zapisano {added} materiałów • {path}")
    except Exception: pass
    try: self.append_log(f"AI Reader: zapisano {added} materiałów do lokalnej bazy {path}")
    except Exception: pass
    messagebox.showinfo("AI Czytnik",f"Zapisano materiały do lokalnej biblioteki.\nBaza: {path}\n\nZapis nie oznacza potwierdzenia poprawności treści — sprawdź źródła.")

def _u66_reader_analyze_tests(self):
    try:
        self.worker(lambda:(self._ai_report_worker(),self.queue_action(self.show_report)))
    except Exception as exc:
        messagebox.showerror("AI Czytnik",str(exc))

def _u66_format_rate(bytes_per_second):
    value=max(0.0,float(bytes_per_second or 0))*8/1_000_000
    return f"{value:.2f} Mbps"

def _u66_net_request(url,data=None,timeout=30):
    headers={"User-Agent":"NAPRAWA-PC-HARDWARE-TEST-PRO/SpeedTest","Cache-Control":"no-cache"}
    if data is not None:
        headers["Content-Type"]="application/octet-stream"
    req=_u66_request.Request(url,data=data,headers=headers,method="POST" if data is not None else "GET")
    started=_u66_time.perf_counter()
    total=0
    with _u66_request.urlopen(req,timeout=timeout) as response:
        code=getattr(response,"status",200)
        while True:
            chunk=response.read(256*1024)
            if not chunk:
                break
            total+=len(chunk)
        final=_u66_urlparse.urlparse(response.geturl())
        if final.scheme!="https" or final.hostname not in ("speed.cloudflare.com","www.cloudflare.com","cloudflare.com"):
            raise ValueError("Odpowiedź testu sieci przekierowała poza dozwolony host Cloudflare.")
    elapsed=max(.001,_u66_time.perf_counter()-started)
    return {"bytes":total,"seconds":elapsed,"mbps":total*8/elapsed/1_000_000,"status":code}

def _u66_measure_speed(self):
    samples={"latency_ms":[],"download":[],"upload":[],"started_at":_U66_datetime.now().isoformat(timespec="seconds")}
    total_data=0
    def phase(text):
        self.queue_action(lambda m=text:_u66_set_speed_status(self,m))
        self.queue_status(text)
    for i in range(3):
        phase(f"Speed Test: pomiar opóźnienia {i+1}/3…")
        start=_u66_time.perf_counter()
        _u66_net_request("https://speed.cloudflare.com/__down?bytes=0&r="+str(_u66_uuid.uuid4().hex),None,15)
        samples["latency_ms"].append(round((_u66_time.perf_counter()-start)*1000,2))
    for idx,size in enumerate((1_000_000,5_000_000,10_000_000),1):
        phase(f"Speed Test: pobieranie {idx}/3 ({size//1_000_000} MB)…")
        result=_u66_net_request("https://speed.cloudflare.com/__down?bytes="+str(size)+"&r="+_u66_uuid.uuid4().hex,None,35)
        total_data+=result["bytes"]; samples["download"].append({"requested_bytes":size,**result})
    for idx,size in enumerate((500_000,2_000_000,5_000_000),1):
        phase(f"Speed Test: wysyłanie {idx}/3 ({size//1_000_000} MB)…")
        body=b"\x5a"*size
        result=_u66_net_request("https://speed.cloudflare.com/__up?r="+_u66_uuid.uuid4().hex,body,35)
        total_data+=size; samples["upload"].append({"requested_bytes":size,**result})
    samples["latency_average_ms"]=round(sum(samples["latency_ms"])/max(1,len(samples["latency_ms"])),2)
    samples["download_mbps"]=round(max([x["mbps"] for x in samples["download"]] or [0]),2)
    samples["upload_mbps"]=round(max([x["mbps"] for x in samples["upload"]] or [0]),2)
    samples["data_bytes"]=total_data
    samples["state"]="good"
    try:
        folder=_u66_store_dir()/"speedtest"
        folder.mkdir(parents=True,exist_ok=True)
        history=folder/"history.json"
        try: records=_u66_json.loads(history.read_text(encoding="utf-8"))
        except Exception: records=[]
        records.append(samples); history.write_text(_u66_json.dumps(records[-100:],ensure_ascii=False,indent=2),encoding="utf-8")
        samples["history_path"]=str(history)
    except Exception:
        pass
    return samples

def _u66_set_speed_status(self,text):
    try:
        if hasattr(self,"_u66_speed_status") and self._u66_speed_status.winfo_exists():
            self._u66_speed_status.config(text=str(text))
        self._set_status(str(text))
    except Exception:
        pass

def _u66_show_speed_test(self):
    self.current_view="SPEED_TEST"; self.clear(); t=self.colors()
    self.header_title.config(text="SPEED TEST — POMIAR INTERNETU NA ŻYWO")
    p=self.panel(self.content); p.pack(fill="x",pady=(0,8))
    tk.Label(p,text="DOWNLOAD • UPLOAD • OPÓŹNIENIE",bg=t["panel"],fg=t["accent"],font=self.fnt(14,"bold")).pack(anchor="w",padx=12,pady=(10,3))
    tk.Label(p,text="Rzeczywisty transfer przez endpointy Cloudflare. Test używa około 23,5 MB na jeden pomiar i może nie działać w sieci blokującej endpointy.",bg=t["panel"],fg=t["muted"],font=self.fnt(9),wraplength=1400,justify="left").pack(anchor="w",padx=12,pady=(0,8))
    metrics=tk.Frame(self.content,bg=t["bg"]); metrics.pack(fill="x",pady=3)
    self._u66_speed_values={}
    for name,key in (("PING / HTTP","latency"),("DOWNLOAD","download"),("UPLOAD","upload"),("DANE TRANSFEROWANE","data")):
        card=self.panel(metrics); card.pack(side="left",fill="both",expand=True,padx=4)
        tk.Label(card,text=name,bg=t["panel"],fg=t["muted"],font=self.fnt(9,"bold")).pack(pady=(10,2))
        label=tk.Label(card,text="N/D",bg=t["panel"],fg=t["accent"],font=self.fnt(18,"bold"))
        label.pack(pady=(0,10)); self._u66_speed_values[key]=label
    self._u66_speed_status=tk.Label(self.content,text="Gotowy — uruchom test, aby wykonać rzeczywisty transfer.",bg=t["bg"],fg=t["muted"],font=self.fnt(9,"bold"),anchor="w")
    self._u66_speed_status.pack(fill="x",padx=4,pady=6)
    chart=self.panel(self.content); chart.pack(fill="both",expand=True,pady=6)
    tk.Label(chart,text="PRÓBKI PRZEPUSTOWOŚCI — MBIT/S",bg=t["panel"],fg=t["accent"],font=self.fnt(10,"bold")).pack(anchor="w",padx=10,pady=6)
    self._u66_speed_chart=tk.Canvas(chart,bg=t["panel"],height=230,highlightthickness=0); self._u66_speed_chart.pack(fill="both",expand=True,padx=8,pady=8)
    row=tk.Frame(self.content,bg=t["bg"]); row.pack(fill="x")
    self.make_button(row,"▶ URUCHOM SPEED TEST",lambda:_u66_start_speed_test(self),"accent",side="left",ipady=7)
    self.make_button(row,"OTWÓRZ WYNIKI W FOLDERZE",lambda:_u66_os.startfile(str(_u66_store_dir()/"speedtest")) if _u66_os.name=="nt" else None,"card",side="left",ipady=7)
    self.make_button(row,"← TESTY",self.show_tests_hub,"card",side="left",ipady=7)
    self._u66_speed_running=False

def _u66_draw_speed_chart(self,result):
    c=getattr(self,"_u66_speed_chart",None)
    if c is None:
        return
    try:
        if not c.winfo_exists(): return
        t=self.colors(); c.delete("all"); w=max(500,c.winfo_width()); h=max(150,c.winfo_height())
        values=[]
        for i,x in enumerate(result.get("download",[])):
            values.append((f"DL {i+1}",float(x.get("mbps",0)),"#2dd4bf"))
        for i,x in enumerate(result.get("upload",[])):
            values.append((f"UL {i+1}",float(x.get("mbps",0)),"#60a5fa"))
        maximum=max([v[1] for v in values] or [1])
        c.create_text(12,8,anchor="nw",text=f"Najwyższy zmierzony DL {result.get('download_mbps','N/D')} Mbps • UL {result.get('upload_mbps','N/D')} Mbps",fill=t["fg"],font=self.fnt(10,"bold"))
        left=90; right=w-20; top=38; bottom=h-28
        c.create_line(left,bottom,right,bottom,fill=t["muted"])
        barw=max(12,(right-left)/max(1,len(values))*0.55)
        for i,(name,val,col) in enumerate(values):
            x=left+(i+.5)*(right-left)/max(1,len(values))
            y=bottom-(val/maximum)*(bottom-top)
            c.create_rectangle(x-barw/2,y,x+barw/2,bottom,fill=col,outline="")
            c.create_text(x,bottom+10,text=name,fill=t["muted"],font=self.fnt(8))
            c.create_text(x,max(top,y-10),text=f"{val:.1f}",fill=t["fg"],font=self.fnt(8,"bold"))
    except Exception:
        pass

def _u66_start_speed_test(self):
    if getattr(self,"_u66_speed_running",False):
        return
    self._u66_speed_running=True
    _u66_set_speed_status(self,"Rozpoczynam pomiary. Nie zamykaj okna...")
    def job():
        try:
            result=_u66_measure_speed(self)
            self.results["SPEED_TEST"]=result
            def done():
                self._u66_speed_running=False
                if getattr(self,"current_view","")=="SPEED_TEST":
                    self._u66_speed_values["latency"].config(text=str(result["latency_average_ms"])+" ms")
                    self._u66_speed_values["download"].config(text=str(result["download_mbps"])+" Mbps")
                    self._u66_speed_values["upload"].config(text=str(result["upload_mbps"])+" Mbps")
                    self._u66_speed_values["data"].config(text=f"{result['data_bytes']/1_000_000:.1f} MB")
                    _u66_draw_speed_chart(self,result)
                _u66_set_speed_status(self,f"Zakończono pomiar. Download {result['download_mbps']} Mbps, upload {result['upload_mbps']} Mbps. Dane: {result['data_bytes']/1_000_000:.1f} MB.")
                self.queue_log("SPEED TEST: DL="+str(result["download_mbps"])+" Mbps; UL="+str(result["upload_mbps"])+" Mbps; latency="+str(result["latency_average_ms"])+" ms")
            self.queue_action(done)
        except Exception as exc:
            def fail():
                self._u66_speed_running=False
                msg=f"Speed Test nie ukończył pomiaru: {type(exc).__name__}: {exc}"
                _u66_set_speed_status(self,msg)
                try: messagebox.showerror("Speed Test",msg)
                except Exception: pass
                self.queue_log(msg)
            self.queue_action(fail)
    _u66_threading.Thread(target=job,name="NaprawaPCSpeedTest",daemon=True).start()

def _u66_sensor_probe():
    result={"cpu_temp_c":None,"gpu_temp_c":None,"acpi_zones":[],"sensors":[],"method":"Windows WMI (best effort)"}
    if _u66_os.name!="nt":
        return result
    script = r"""
$ErrorActionPreference='SilentlyContinue'
$sensors=@()
foreach($ns in @('root/LibreHardwareMonitor','root/OpenHardwareMonitor')){
  try{
    $xs=@(Get-CimInstance -Namespace $ns -ClassName Sensor -ErrorAction Stop | Where-Object { $_.SensorType -eq 'Temperature' -and $null -ne $_.Value } | Select-Object Name,Parent,Value,SensorType)
    foreach($x in $xs){$sensors += [pscustomobject]@{name=[string]$x.Name; parent=[string]$x.Parent; value=[double]$x.Value; source=$ns}}
  }catch{}
}
$zones=@()
try{
  foreach($x in @(Get-CimInstance -Namespace root/wmi -ClassName MSAcpi_ThermalZoneTemperature -ErrorAction Stop)){
    $c=([double]$x.CurrentTemperature/10.0)-273.15
    if($c -gt -20 -and $c -lt 150){$zones += [pscustomobject]@{name=[string]$x.InstanceName; value=[math]::Round($c,1)}}
  }
}catch{}
[pscustomobject]@{sensors=$sensors;zones=$zones} | ConvertTo-Json -Depth 5 -Compress
"""
    try:
        exe=_u66_os.path.join(_u66_os.environ.get("WINDIR",r"C:\Windows"),"System32","WindowsPowerShell","v1.0","powershell.exe")
        proc=_u66_subprocess.run([exe,"-NoProfile","-NonInteractive","-Command",script],capture_output=True,text=True,timeout=8,creationflags=getattr(_u66_subprocess,"CREATE_NO_WINDOW",0))
        if proc.returncode==0 and proc.stdout.strip():
            payload=_u66_json.loads(proc.stdout.strip().splitlines()[-1])
            result["sensors"]=payload.get("sensors") or []
            result["acpi_zones"]=payload.get("zones") or []
            for sensor in result["sensors"]:
                label=(str(sensor.get("name",""))+" "+str(sensor.get("parent",""))).lower()
                try: value=float(sensor.get("value"))
                except Exception: continue
                if any(x in label for x in ("cpu package","cpu tctl","cpu die","cpu core","cpu ccd","cpu (tctl","processor package")):
                    result["cpu_temp_c"]=value
                    break
                if result["gpu_temp_c"] is None and any(x in label for x in ("gpu core","gpu temperature","gpu hotspot","gpu package")):
                    result["gpu_temp_c"]=value
            if result["cpu_temp_c"] is None and result["acpi_zones"]:
                result["method"]="ACPI zone only — not confirmed CPU die"
    except Exception as exc:
        result["error"]=f"{type(exc).__name__}: {exc}"
    return result

def _u66_sensor_poll(self):
    try:
        if getattr(self,"_u66_sensor_busy",False):
            self.after(4000,lambda:_u66_sensor_poll(self)); return
        if _u66_time.monotonic()-getattr(self,"_u66_sensor_last",0)>8:
            self._u66_sensor_busy=True
            self._u66_sensor_last=_u66_time.monotonic()
            def job():
                try:
                    gpu=_u37_nvidia_telemetry() if "_u37_nvidia_telemetry" in globals() else {"available":False}
                    temps=_u66_sensor_probe()
                    self._u66_sensor_cache={"gpu":gpu,"temps":temps,"time":_u66_time.monotonic()}
                    def update():
                        self._u66_sensor_busy=False
                        if getattr(self,"current_view","")=="LIVE_MONITOR":
                            _u66_live_tick(self)
                    self.queue_action(update)
                except Exception:
                    self._u66_sensor_busy=False
            _u66_threading.Thread(target=job,name="NaprawaPCSensorPoll",daemon=True).start()
    except Exception:
        self._u66_sensor_busy=False
    try: self.after(4000,lambda:_u66_sensor_poll(self))
    except Exception: pass

def _u66_header_live(self):
    try:
        if not hasattr(self,"header_sub") or not self.header_sub.winfo_exists():
            return
        vals=getattr(self,"_live_values",{}) or {}
        cpu=vals.get("cpu"); ram=vals.get("ram")
        cache=getattr(self,"_u66_sensor_cache",{}) or {}
        gpu=cache.get("gpu",{}) or {}; temps=cache.get("temps",{}) or {}
        ctemp=temps.get("cpu_temp_c")
        gtemp=gpu.get("temperature_c")
        fields=[f"CPU {cpu:.0f}%" if isinstance(cpu,(int,float)) else "CPU N/D",
                f"RAM {ram:.0f}%" if isinstance(ram,(int,float)) else "RAM N/D",
                f"TCPU {ctemp:.0f}°C" if isinstance(ctemp,(int,float)) else "TCPU N/D",
                f"GPU {gtemp:.0f}°C" if isinstance(gtemp,(int,float)) else "TGPU N/D"]
        self.header_sub.config(text="v"+str(VERSION).split(" ")[0]+" | "+" | ".join(fields))
    except Exception:
        pass

def _u66_refresh_telemetry(self):
    try:
        _U66_ORIGINAL_REFRESH_TELEMETRY(self)
    except Exception:
        pass
    _u66_header_live(self)
    try:
        if "_u67_refresh_visible_charts" in globals():
            _u67_refresh_visible_charts(self)
    except Exception as exc:
        try: self.append_log("Aktualizacja wykresów live: " + repr(exc))
        except Exception: pass

def _u66_show_live_monitor(self):
    self.current_view="LIVE_MONITOR"; self.clear(); t=self.colors()
    self.header_title.config(text="MONITOR LIVE — TELEMETRIA SPRZĘTU")
    info=self.panel(self.content); info.pack(fill="x",pady=(0,6))
    tk.Label(info,text="ODCZYTY NA ŻYWO • odświeżanie co 1 sekundę, jeśli Windows udostępnia licznik",bg=t["panel"],fg=t["accent"],font=self.fnt(13,"bold")).pack(anchor="w",padx=12,pady=(10,3))
    tk.Label(info,text="Brak czujnika jest pokazywany jako N/D. ACPI thermal zone nie jest automatycznie traktowana jako temperatura rdzenia CPU.",bg=t["panel"],fg=t["muted"],font=self.fnt(9),wraplength=1400,justify="left").pack(anchor="w",padx=12,pady=(0,8))
    grid=tk.Frame(self.content,bg=t["bg"]); grid.pack(fill="x",pady=4)
    self._u66_live_labels={}
    for title,key in [
        ("CPU LOAD","cpu"),("RAM UŻYTA","ram"),("GPU LOAD","gpu"),("TEMP CPU","cpu_temp"),
        ("TEMP GPU","gpu_temp"),("DYSK ODCZYT","disk_read"),("DYSK ZAPIS","disk_write"),
        ("DOWNLOAD LIVE","net_down"),("UPLOAD LIVE","net_up"),("ZEGAR CPU","cpu_freq"),
        ("VRAM UŻYTA","vram"),("CZUJNIK ACPI","acpi")
    ]:
        card=self.panel(grid); card.grid(row=len(self._u66_live_labels)//4,column=len(self._u66_live_labels)%4,sticky="nsew",padx=3,pady=3)
        tk.Label(card,text=title,bg=t["panel"],fg=t["muted"],font=self.fnt(8,"bold")).pack(pady=(8,2))
        val=tk.Label(card,text="N/D",bg=t["panel"],fg=t["accent"],font=self.fnt(14,"bold"))
        val.pack(pady=(0,8)); self._u66_live_labels[key]=val
    for col in range(4): grid.grid_columnconfigure(col,weight=1)
    charts=tk.Frame(self.content,bg=t["bg"]); charts.pack(fill="both",expand=True,pady=6)
    left=self.panel(charts); left.pack(side="left",fill="both",expand=True,padx=(0,4))
    right=self.panel(charts); right.pack(side="left",fill="both",expand=True,padx=(4,0))
    tk.Label(left,text="CPU / RAM / GPU — OSTATNIE 60 PRÓBEK",bg=t["panel"],fg=t["accent"],font=self.fnt(9,"bold")).pack(anchor="w",padx=8,pady=5)
    tk.Label(right,text="SIEĆ — MBIT/S, OSTATNIE 60 PRÓBEK",bg=t["panel"],fg=t["accent"],font=self.fnt(9,"bold")).pack(anchor="w",padx=8,pady=5)
    self._u66_live_chart=tk.Canvas(left,bg=t["panel"],height=200,highlightthickness=0); self._u66_live_chart.pack(fill="both",expand=True,padx=8,pady=8)
    self._u66_net_chart=tk.Canvas(right,bg=t["panel"],height=200,highlightthickness=0); self._u66_net_chart.pack(fill="both",expand=True,padx=8,pady=8)
    row=tk.Frame(self.content,bg=t["bg"]); row.pack(fill="x")
    self.make_button(row,"▶ SPEED TEST",self.show_speed_test,"accent",side="left",ipady=6)
    self.make_button(row,"ODŚWIEŻ SPRZĘT",self.refresh_hardware_async,"card",side="left",ipady=6)
    self.make_button(row,"← TESTY",self.show_tests_hub,"card",side="left",ipady=6)
    if not hasattr(self,"_u66_live_history"):
        self._u66_live_history={"cpu":[],"ram":[],"gpu":[],"down":[],"up":[]}
    _u66_live_tick(self)
    _u66_sensor_poll(self)

def _u66_draw_live_line(self,canvas,series,maximum=100):
    try:
        if not canvas.winfo_exists(): return
        t=self.colors(); canvas.delete("all")
        w=max(250,canvas.winfo_width()); h=max(120,canvas.winfo_height())
        for i in range(1,5):
            y=int(i*h/5); canvas.create_line(0,y,w,y,fill=t["card"],width=1)
        palette={"cpu":t["accent"],"ram":t["warn"],"gpu":"#2dd4bf","down":"#60a5fa","up":"#c084fc"}
        for name,values in series.items():
            if not values: continue
            maxval=max(maximum,max(values) if maximum>0 else 1)
            pts=[]
            for i,v in enumerate(values[-60:]):
                x=8+i*(w-16)/max(1,min(59,len(values)-1))
                y=h-10-(max(0,min(maxval,float(v)))/maxval)*(h-22)
                pts.extend((x,y))
            if len(pts)>=4:
                canvas.create_line(*pts,fill=palette.get(name,t["accent"]),width=2,smooth=False)
        if series:
            labels=[]
            for name,values in series.items():
                if values: labels.append(f"{name.upper()} {values[-1]:.1f}")
            canvas.create_text(8,5,anchor="nw",text="   •   ".join(labels),fill=t["fg"],font=self.fnt(8,"bold"))
    except Exception:
        pass

def _u66_live_tick(self):
    if getattr(self,"current_view","")!="LIVE_MONITOR":
        return
    try:
        vals=getattr(self,"_live_values",{}) or {}
        cache=getattr(self,"_u66_sensor_cache",{}) or {}
        gpu=cache.get("gpu",{}) or {}; temps=cache.get("temps",{}) or {}
        put=lambda key,text: self._u66_live_labels[key].config(text=str(text)) if key in self._u66_live_labels and self._u66_live_labels[key].winfo_exists() else None
        cpu=vals.get("cpu"); ram=vals.get("ram")
        put("cpu",f"{cpu:.1f}%" if isinstance(cpu,(int,float)) else "N/D")
        put("ram",f"{ram:.1f}%" if isinstance(ram,(int,float)) else "N/D")
        gu= gpu.get("gpu_load_percent",getattr(self,"_gpu_util",None))
        put("gpu",f"{float(gu):.1f}%" if isinstance(gu,(int,float)) else "N/D")
        ct=temps.get("cpu_temp_c")
        gt=gpu.get("temperature_c",temps.get("gpu_temp_c"))
        put("cpu_temp",f"{float(ct):.1f} °C" if isinstance(ct,(int,float)) else "N/D")
        put("gpu_temp",f"{float(gt):.1f} °C" if isinstance(gt,(int,float)) else "N/D")
        io=psutil.disk_io_counters() if psutil else None
        now=_u66_time.monotonic()
        prev=getattr(self,"_u66_disk_prev",None)
        dr=dw=0.0
        if io and prev:
            dt=max(.1,now-prev[2]); dr=max(0,(io.read_bytes-prev[0])/dt); dw=max(0,(io.write_bytes-prev[1])/dt)
        if io: self._u66_disk_prev=(io.read_bytes,io.write_bytes,now)
        put("disk_read",f"{dr/1_000_000:.2f} MB/s" if io else "N/D")
        put("disk_write",f"{dw/1_000_000:.2f} MB/s" if io else "N/D")
        put("net_down",_u66_format_rate(vals.get("recv",0)))
        put("net_up",_u66_format_rate(vals.get("sent",0)))
        freq=psutil.cpu_freq() if psutil else None
        put("cpu_freq",f"{freq.current:.0f} MHz" if freq and freq.current else "N/D")
        used=gpu.get("vram_used_mb"); total=gpu.get("vram_total_mb")
        put("vram",f"{used:.0f}/{total:.0f} MB" if isinstance(used,(int,float)) and isinstance(total,(int,float)) else "N/D")
        zones=temps.get("acpi_zones") or []
        put("acpi",f"{zones[0].get('value')} °C (ACPI)" if zones else "N/D")
        hist=getattr(self,"_u66_live_history",{"cpu":[],"ram":[],"gpu":[],"down":[],"up":[]})
        for key,val in (("cpu",cpu),("ram",ram),("gpu",gu),("down",max(0,float(vals.get("recv",0))*8/1_000_000)),("up",max(0,float(vals.get("sent",0))*8/1_000_000))):
            if isinstance(val,(int,float)):
                hist[key].append(float(val)); hist[key]=hist[key][-60:]
        self._u66_live_history=hist
        _u66_draw_live_line(self,self._u66_live_chart,{k:hist[k] for k in ("cpu","ram","gpu")},100)
        _u66_draw_live_line(self,self._u66_net_chart,{k:hist[k] for k in ("down","up")},max(10,max(hist["down"]+hist["up"] or [10])))
        _u66_header_live(self)
    except Exception as exc:
        try: self.append_log("Live telemetry: "+repr(exc))
        except Exception: pass
    try: self.after(1000,lambda:_u66_live_tick(self))
    except Exception: pass

def _u66_open_tests_item(self,key):
    routes={
      "CPU":lambda:(self.show_module("CPU"),self.worker(lambda:self._cpu_test(10))),
      "RAM":lambda:(self.show_module("RAM"),self.worker(lambda:self._ram_test(256))),
      "GPU":lambda:(self.show_module("GPU"),self.worker(self._gpu_test)),
      "DYSK":lambda:(self.show_module("DYSK"),self.worker(lambda:self._disk_test(256))),
      "EKRAN":lambda:(self.show_module("EKRAN"),self.worker(self._monitor_test)),
      "SECURITY":lambda:(self.show_module("SECURITY"),self.worker(self._security_test)),
      "BATERIA":lambda:(self.show_battery_or_power(),self.worker(self._battery_test)),
      "USB":lambda:_u36_start_module_test(self,"USB"),
      "SIEC":lambda:_u36_start_module_test(self,"SIEĆ"),
      "AI":lambda:self.show_ai_reader(),
      "SPEED":lambda:self.show_speed_test(),
      "LIVE":lambda:self.show_live_monitor(),
      "3D":lambda:self.show_3d_studio(),
      "ALL":lambda:_u68_start_all_tests_sequential(self),
      "CENTRUM":lambda:self.show_service_center(),
      "SYSTEM_REPAIR":lambda:_u68_launch_system_repair(self),
      "RAPORT":lambda:self.show_report(),
      "WINSAT":lambda:(self.show_module("GPU"),self.run_winsat_d3d()),
      "PIXEL":lambda:(self.show_module("EKRAN"),self._u37_open_screen_test()),
      "VRAM":lambda:(self.show_module("GPU"),self._u41_start_vram_test()),
      "LAN":lambda:self._start_module_test("SIEĆ"),
      "USB_LIST":lambda:self._start_module_test("USB")
    }
    return routes[key]()

def _u66_show_tests_hub(self):
    self.current_view="TESTY"
    self.clear()
    t=self.colors()
    self.header_title.config(text="CENTRUM TESTÓW — AUTOMATYCZNE, LIVE I SERWIS")
    banner=self.panel(self.content); banner.pack(fill="x",pady=(0,7))
    tk.Label(banner,text="TESTY SPRZĘTOWE • SPEED TEST • 40 SCEN 3D ULTRA/MAX • SYSTEM REPAIR PRO • SERWIS ULTIMATE • AI CZYTNIK",bg=t["panel"],fg=t["accent"],font=self.fnt(12,"bold")).pack(anchor="w",padx=12,pady=(9,3))
    tk.Label(banner,text="„WSZYSTKIE TESTY PO KOLEI” przełącza ekran do aktualnie wykonywanego testu. Wyniki oznaczane są PASS/WARN/FAIL/N/D na podstawie dostępnych pomiarów; brak sensora nie jest zaliczeniem.",bg=t["panel"],fg=t["muted"],font=self.fnt(8),wraplength=1400,justify="left").pack(anchor="w",padx=12,pady=(0,8))
    outer=tk.Frame(self.content,bg=t["bg"]); outer.pack(fill="both",expand=True)
    c=tk.Canvas(outer,bg=t["bg"],highlightthickness=0)
    sb=ttk.Scrollbar(outer,orient="vertical",command=c.yview)
    inner=tk.Frame(c,bg=t["bg"])
    win=c.create_window((0,0),window=inner,anchor="nw")
    inner.bind("<Configure>",lambda e:c.configure(scrollregion=c.bbox("all")))
    c.bind("<Configure>",lambda e:c.itemconfigure(win,width=e.width))
    c.configure(yscrollcommand=sb.set)
    c.pack(side="left",fill="both",expand=True); sb.pack(side="right",fill="y")
    items=[
      ("WSZYSTKIE TESTY PO KOLEI","Przebieg CPU → RAM → GPU/VRAM → 40 scen 3D → SSD/HDD/NVMe → matryca → Speed Test → bezpieczeństwo → bateria/audio/USB. Każdy etap otrzymuje ekran, pomiary i status.","ALL"),
      ("MONITOR LIVE — WSZĘDZIE","CPU/RAM/GPU, zegary, transfer dysku i sieci, temperatury/czujniki z rzeczywistą próbką co sekundę.","LIVE"),
      ("SPEED TEST INTERNETU","Pomiar prawdziwego download/upload w Mbps oraz opóźnienia HTTP; zapis historii lokalnie.","SPEED"),
      ("3D BENCHMARK STUDIO — 40 SCEN • ULTRA / MAX","40 scen OpenGL. Wybierz 5–300 s na scenę; FPS z prawdziwego renderowania trafia do raportu. Dłuższe profile obciążają GPU dłużej.","3D"),
      ("AI CZYTNIK WIEDZY","Baza offline, wyszukiwanie Internetu, czytanie URL, import plików i zapis źródeł do prywatnej biblioteki.","AI"),
      ("CENTRUM SERWISU + SYSTEM REPAIR","SFC, DISM, CHKDSK, narzędzia Windows, prywatne zgłoszenia i naprawy serwisowe.","CENTRUM"),
      ("PEŁNY SYSTEM REPAIR PRO — APLIKACJA WPF","Uruchamia dołączony, samodzielny program .NET System Repair PRO w katalogu instalacji. Brak osobnej ikony na pulpicie.","SYSTEM_REPAIR"),
      ("CPU — obciążenie i zegary","Rzeczywiste obciążenie etapowe, częstotliwość i wykres próbek.","CPU"),
      ("RAM — wzorce zapisu/odczytu","Bufor RAM z weryfikacją wzorców 00/FF/AA/55; wynik opisuje rozmiar rzeczywiście sprawdzony.","RAM"),
      ("GPU — karta i sterownik","Adaptery, status PnP, telemetria dostawcy i dostępne czujniki.","GPU"),
      ("VRAM — tekstury i odczyt zwrotny","Przydział tekstur, zapis/odczyt i porównanie wzorców dla wybranego rozmiaru.","VRAM"),
      ("DYSK — odczyt/zapis","Benchmark pliku tymczasowego, przepływ danych i dostępne dane niezawodności.","DYSK"),
      ("MATRYCA / EDID","Identyfikacja EDID oraz ręczny test wzorców pikseli.","EKRAN"),
      ("ANTYWIRUS / AUTOSTART","Sprawdzenie stanu ochrony i wpisów autostartu; brak danych jest jawnie oznaczony.","SECURITY"),
      ("BATERIA / ZASILANIE","Raport baterii i źródło zasilania; PC stacjonarny nie jest błędnie oceniany jak laptop.","BATERIA"),
      ("SIEĆ / WI-FI / LAN","Interfejsy, ich stan i rzeczywisty transfer w Speed Test.","SIEC"),
      ("USB / URZĄDZENIA","Lista Plug and Play. Sama obecność urządzenia nie jest testem zasilania lub transferu portu.","USB"),
      ("WINSAT / DIRECT3D","Uruchamia natywny test graficzny Windows, gdy jest dostępny.","WINSAT"),
      ("PIKSELE — WZORCE EKRANU","Kolory, gradienty i wzorce; martwe piksele wymagają wzrokowego potwierdzenia.","PIXEL"),
      ("RAPORT I HISTORIA","Wyniki faktycznie zapisanych pomiarów, nie przykładowe wartości.","RAPORT")
    ]
    for i,(title,desc,key) in enumerate(items):
        card=self.panel(inner); card.grid(row=i//3,column=i%3,sticky="nsew",padx=4,pady=4)
        tk.Label(card,text=title,bg=t["panel"],fg=t["accent"],font=self.fnt(9,"bold"),wraplength=400,justify="left").pack(anchor="w",padx=9,pady=(8,4))
        tk.Label(card,text=desc,bg=t["panel"],fg=t["fg"],font=self.fnt(8),wraplength=400,justify="left").pack(fill="x",padx=9,pady=(0,6))
        self.make_button(card,"OTWÓRZ / START",lambda k=key:_u66_open_tests_item(self,k),"accent" if key in ("ALL","SPEED","3D","AI") else "card",fill="x",ipady=5)
    for i in range(3): inner.grid_columnconfigure(i,weight=1)
    row=tk.Frame(self.content,bg=t["bg"]); row.pack(fill="x",pady=(5,0))
    self.make_button(row,"PULPIT",self.show_dashboard,"card",side="left",ipady=5)
    self.make_button(row,"AI CZYTNIK",self.show_ai_reader,"accent",side="left",ipady=5)
    self.make_button(row,"MONITOR LIVE",self.show_live_monitor,"card",side="left",ipady=5)

def _u66_scene_child(output_path, seconds=5, scene_id=1):
    result={"state":"warn","scene_id":int(scene_id),"scene_name":"N/D"}
    pg=None
    try:
        import pygame as pg
        from OpenGL import GL
        from OpenGL.GLU import gluPerspective
        sid=max(1,min(len(_U66_SCENES),int(scene_id)))
        name,kind,complexity=_U66_SCENES[sid-1]
        result.update({"scene_name":name,"test":"OpenGL procedural scene","requested_seconds":seconds,"state":"running"})
        pg.init()
        try:
            pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION,2)
            pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION,1)
        except Exception: pass
        width,height=1280,720
        pg.display.set_mode((width,height),pg.OPENGL|pg.DOUBLEBUF|pg.RESIZABLE,vsync=0)
        renderer=(GL.glGetString(GL.GL_RENDERER) or b"unknown").decode("utf-8","replace")
        version=(GL.glGetString(GL.GL_VERSION) or b"unknown").decode("utf-8","replace")
        GL.glEnable(GL.GL_DEPTH_TEST); GL.glClearColor(.008,.018,.03,1)
        GL.glViewport(0,0,width,height); GL.glMatrixMode(GL.GL_PROJECTION); GL.glLoadIdentity(); gluPerspective(55,width/height,.1,250); GL.glMatrixMode(GL.GL_MODELVIEW)
        start=_u66_time.perf_counter(); frames=0; running=True; samples=[]; win_frames=0; win_start=start; peak=0.0
        requested=max(3,min(300,int(seconds)))
        while running and _u66_time.perf_counter()-start < requested:
            for ev in pg.event.get():
                if ev.type==pg.QUIT or (ev.type==pg.KEYDOWN and ev.key==pg.K_ESCAPE): running=False
                elif ev.type==pg.VIDEORESIZE:
                    width=max(640,ev.w); height=max(480,ev.h); GL.glViewport(0,0,width,height); GL.glMatrixMode(GL.GL_PROJECTION); GL.glLoadIdentity(); gluPerspective(55,width/height,.1,250); GL.glMatrixMode(GL.GL_MODELVIEW)
            elapsed=_u66_time.perf_counter()-start
            GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)
            GL.glPolygonMode(GL.GL_FRONT_AND_BACK,GL.GL_LINE if kind=="wire" else GL.GL_FILL)
            GL.glLoadIdentity(); GL.glTranslatef(0,0,-13); GL.glRotatef(elapsed*18,0,1,0); GL.glRotatef(14+_u66_math.sin(elapsed)*7,1,0,0)
            complexity=max(1,min(12000,int(complexity))); base=min(20,complexity)
            if kind=="cpu_core_matrix":
                _u37_draw_gpu_box(GL,0,0,0,5.4,.22,3.5,(.035,.12,.17))
                _u37_draw_gpu_box(GL,0,.18,0,3.25,.22,2.3,(.32,.37,.42))
                core_count=min(64,max(8,complexity//5))
                for core in range(core_count):
                    x=(core%8-3.5)*.39
                    z=(core//8-3)*.34
                    pulse=.45+.45*(_u66_math.sin(elapsed*2.5+core*.7)+1)/2
                    _u37_draw_gpu_box(GL,x,.38,z,.31,.12,.25,(.05+pulse*.12,.22+pulse*.65,.28+pulse*.58))
                for pin in range(18):
                    _u37_draw_gpu_box(GL,-2.45+pin*.29,-.03,-1.86,.08,.06,.16,(.72,.55,.18))
                    _u37_draw_gpu_box(GL,-2.45+pin*.29,-.03,1.86,.08,.06,.16,(.72,.55,.18))
            elif kind=="ram_address_matrix":
                _u37_draw_gpu_box(GL,0,-.28,0,5.6,.18,3.6,(.025,.22,.13))
                for module_id in range(4):
                    x=(module_id-1.5)*1.28
                    _u37_draw_gpu_box(GL,x,.05,0,.88,.11,3.25,(.035,.14,.1))
                    _u37_draw_gpu_box(GL,x,.13,0,.62,.09,2.85,(.18,.23,.25))
                    for chip in range(8):
                        z=(chip-3.5)*.34
                        pulse=.35+.5*(_u66_math.sin(elapsed*3+module_id+chip*.8)+1)/2
                        _u37_draw_gpu_box(GL,x,.23,z,.43,.1,.23,(.04,.24+pulse*.55,.3+pulse*.45))
                    for pin in range(20):
                        _u37_draw_gpu_box(GL,x-.4+pin*.042,-.01,1.67,.024,.035,.18,(.8,.64,.24))
            elif kind=="disk_sequential":
                GL.glColor3f(.35,.47,.53)
                for radius in (2.1,1.7,1.3,.9,.52):
                    GL.glBegin(GL.GL_LINE_LOOP)
                    for point in range(100):
                        a=2*_U66_math.pi*point/100
                        GL.glVertex3f(radius*_U66_math.cos(a),radius*_U66_math.sin(a),.08)
                    GL.glEnd()
                _u37_draw_gpu_box(GL,0,.1,0,.55,.16,.55,(.55,.61,.66))
                GL.glPushMatrix()
                GL.glRotatef(elapsed*52,0,0,1)
                _u37_draw_gpu_box(GL,1.22,.16,0,1.65,.12,.16,(.04,.8,.56))
                GL.glPopMatrix()
                blocks=min(256,max(48,complexity//10))
                for block in range(blocks):
                    a=(block/blocks)*2*_U66_math.pi+elapsed*.7
                    rad=1.82+(block%3)*.11
                    col=(.05,.35+.55*((block%9)/9),.28)
                    _u37_draw_gpu_box(GL,rad*_U66_math.cos(a),.16,rad*_U66_math.sin(a),.075,.08,.075,col)
            elif kind=="disk_random":
                GL.glColor3f(.35,.47,.53)
                for radius in (2.15,1.65,1.15,.62):
                    GL.glBegin(GL.GL_LINE_LOOP)
                    for point in range(80):
                        a=2*_U66_math.pi*point/80
                        GL.glVertex3f(radius*_U66_math.cos(a),radius*_U66_math.sin(a),.08)
                    GL.glEnd()
                _u37_draw_gpu_box(GL,0,.13,0,.52,.16,.52,(.5,.57,.62))
                points=min(300,max(64,complexity//2))
                for point in range(points):
                    a=point*2.399963+elapsed*(.4+(point%5)*.22)
                    rad=.55+(point%27)/27*1.58
                    pulse=.35+.6*(_U66_math.sin(elapsed*4+point)+1)/2
                    _u37_draw_gpu_box(GL,rad*_U66_math.cos(a),.16,rad*_U66_math.sin(a),.065,.07,.065,(.04,.32+pulse*.55,.75))
            elif kind=="vram_texture_tiles":
                _u37_draw_gpu_box(GL,0,-.35,0,5.7,.18,3.6,(.025,.18,.13))
                _u37_draw_gpu_box(GL,0,-.05,0,1.75,.18,1.45,(.32,.37,.42))
                for mem in range(8):
                    a=2*_U66_math.pi*mem/8
                    _u37_draw_gpu_box(GL,2.0*_U66_math.cos(a),.02,1.23*_U66_math.sin(a),.67,.12,.43,(.03,.34,.19))
                cols=min(12,max(6,complexity//15))
                for tile in range(cols*6):
                    x=(tile%cols-(cols-1)/2)*.38
                    z=(tile//cols-2.5)*.38
                    wave=.5+.5*_U66_math.sin(elapsed*2+tile*.27)
                    GL.glPushMatrix()
                    GL.glTranslatef(x,1.05+wave*.32,z)
                    GL.glRotatef(elapsed*20+tile*11,0,1,0)
                    _u37_draw_gpu_box(GL,0,0,0,.28,.12,.28,(.08+wave*.15,.14+wave*.65,.42+wave*.5))
                    GL.glPopMatrix()
            elif kind=="pcie_bus":
                _u37_draw_gpu_box(GL,0,-.35,0,5.8,.18,3.5,(.025,.2,.12))
                _u37_draw_gpu_box(GL,0,-.12,0,4.4,.12,.32,(.13,.16,.18))
                for lane in range(10):
                    z=(lane-4.5)*.25
                    GL.glColor3f(.05,.43,.74)
                    GL.glBegin(GL.GL_LINE_STRIP)
                    for point in range(30):
                        x=-2.55+point*.175
                        y=.04+.08*_U66_math.sin(elapsed*4-point*.22+lane)
                        GL.glVertex3f(x,y,z)
                    GL.glEnd()
                    pulse=(elapsed*1.5+lane/10)%1
                    _u37_draw_gpu_box(GL,-2.4+pulse*4.8,.12,z,.18,.1,.13,(.08,.8,.95))
                for chip in range(12):
                    x=(chip%6-2.5)*.72
                    z=(chip//6-0.5)*1.65
                    _u37_draw_gpu_box(GL,x,.02,z,.4,.12,.34,(.25,.29,.34))
            elif kind=="display_pixels":
                _u37_draw_gpu_box(GL,0,0,0,5.8,.22,3.7,(.16,.18,.22))
                cols=min(30,max(12,complexity//10)); rows=min(14,max(8,cols*3//5))
                _u37_draw_gpu_box(GL,0,.17,0,5.25,.12,3.12,(.02,.025,.04))
                for pixel in range(cols*rows):
                    x=(pixel%cols-(cols-1)/2)*(.17 if cols>22 else .25)
                    z=(pixel//cols-(rows-1)/2)*.25
                    r=((pixel%3)==0)*.85 + .05
                    g=((pixel%3)==1)*.8 + .04
                    b=((pixel%3)==2)*.9 + .07
                    pulse=.25+.65*(_U66_math.sin(elapsed*2+pixel*.12)+1)/2
                    _u37_draw_gpu_box(GL,x,.29,z,.11,.06,.14,(min(1,r*pulse),min(1,g*pulse),min(1,b*pulse)))
            elif kind in ("boxes","cubes","grid","materials","room","city","gpu","particles","mixed","ultimate"):
                n=min(1200,complexity)
                if kind=="ultimate": n=min(3000,complexity)
                for i in range(n):
                    if kind=="city":
                        x=(i%14-7)*.62; z=(i//14-2)*.7; y=.45+(i*7%13)*.22
                        _u37_draw_gpu_box(GL,x,y,z,.38,y*2,.38,(.06+(i%4)*.09,.22+(i%5)*.07,.44+(i%3)*.12))
                    elif kind=="gpu":
                        GL.glPushMatrix(); GL.glTranslatef((i%4-1.5)*1.2,(i//4%3-1)*.8,(i//12)*-.9)
                        _u37_draw_gpu_box(GL,0,0,0,2.2,.18,1.2,(.03,.3,.19))
                        _u37_draw_gpu_box(GL,0,.18,0,1.4,.12,.9,(.35,.39,.43))
                        for fin in range(7): _u37_draw_gpu_box(GL,-.55+fin*.18,.27,0,.035,.1,.75,(.52,.57,.6))
                        GL.glPopMatrix()
                    else:
                        x=(i%11-5)*.72; y=((i//11)%7-3)*.6; z=-(i//77)*.7
                        if kind=="room": z=-abs(z)*.5
                        if kind=="particles":
                            x=_u66_math.sin(i*13.31+elapsed)*4.5; y=_u66_math.cos(i*6.27+elapsed*1.3)*3.0; z=_u66_math.sin(i*2.7)*3.5
                        col=((i%7)/7.0,.22+(i%4)*.13,.32+(i%5)*.12)
                        _u37_draw_gpu_box(GL,x+_u66_math.sin(elapsed+i)*.12,y,z,.18+(i%3)*.06,.18+(i%2)*.08,.18+(i%4)*.035,col)
            elif kind in ("triangles","triangles_extreme","mesh"):
                tri=min(12000,max(500,complexity)) if kind!="triangles_extreme" else min(48000,max(500,int(complexity)*4))
                GL.glBegin(GL.GL_TRIANGLES)
                for i in range(tri):
                    a=i*.6180339887+elapsed*.1
                    rad=1.4+(i%19)*.19
                    GL.glColor3f((i%7)/7.0,.25+(i%4)*.16,.35+(i%3)*.2)
                    GL.glVertex3f(_u66_math.sin(a)*rad,_u66_math.cos(a*1.13)*rad,_u66_math.sin(a*.71)*2)
                    GL.glVertex3f(_u66_math.sin(a+1.9)*rad,_u66_math.cos(a*1.13+1.4)*rad,_u66_math.sin(a*.71+1)*2)
                    GL.glVertex3f(_u66_math.sin(a+3.4)*rad,_u66_math.cos(a*1.13+3.2)*rad,_u66_math.sin(a*.71+2)*2)
                GL.glEnd()
            elif kind in ("terrain","waves"):
                grid=max(8,min(48,base))
                GL.glBegin(GL.GL_TRIANGLES)
                for x in range(grid):
                    for z in range(grid):
                        for ox,oz in ((0,0),(1,0),(0,1),(1,0),(1,1),(0,1)):
                            xx=(x+ox-grid/2)*.28; zz=(z+oz-grid/2)*.28
                            yy=_u66_math.sin((x+ox)*.55+elapsed)*.35+_u66_math.cos((z+oz)*.45+elapsed*.7)*.35
                            GL.glColor3f(.04+(x%8)*.04,.18+(z%6)*.07,.22+(x%5)*.1)
                            GL.glVertex3f(xx,yy,zz)
                GL.glEnd()
            elif kind=="spheres":
                for i in range(base):
                    cx=(i%4-1.5)*2.1; cy=(i//4%3-1)*1.7; cz=-(i//12)*1.3
                    radius=.38+(i%3)*.07
                    lat=12; lon=16
                    for la in range(lat):
                        t1=_u66_math.pi*la/lat; t2=_u66_math.pi*(la+1)/lat
                        GL.glBegin(GL.GL_TRIANGLES)
                        for lo in range(lon):
                            p1=2*_u66_math.pi*lo/lon; p2=2*_u66_math.pi*(lo+1)/lon
                            def vertex(th,ph):
                                return (cx+radius*_u66_math.sin(th)*_u66_math.cos(ph),cy+radius*_u66_math.cos(th),cz+radius*_u66_math.sin(th)*_u66_math.sin(ph))
                            verts=[vertex(t1,p1),vertex(t2,p1),vertex(t2,p2),vertex(t1,p1),vertex(t2,p2),vertex(t1,p2)]
                            GL.glColor3f(.1+(i%4)*.15,.38+(la%4)*.13,.6)
                            for v in verts: GL.glVertex3f(*v)
                        GL.glEnd()
            elif kind=="torus":
                for i in range(base):
                    GL.glPushMatrix(); GL.glTranslatef((i%4-1.5)*1.8,(i//4%3-1)*1.6,-(i//12)*1.2); GL.glRotatef(elapsed*35+i*23,1,1,.3)
                    for j in range(18):
                        a1=2*_u66_math.pi*j/18; a2=2*_u66_math.pi*(j+1)/18; GL.glBegin(GL.GL_QUAD_STRIP)
                        for k in range(13):
                            b=2*_u66_math.pi*k/12
                            for a in (a1,a2):
                                rad=.55+.17*_u66_math.cos(b); GL.glColor3f(.14+.15*_u66_math.sin(a),.45,.55+.2*_u66_math.cos(b))
                                GL.glVertex3f(rad*_u66_math.cos(a),.17*_u66_math.sin(b),rad*_u66_math.sin(a))
                        GL.glEnd()
                    GL.glPopMatrix()
            elif kind in ("rings","planets"):
                for i in range(base):
                    GL.glPushMatrix(); GL.glTranslatef((i%5-2)*1.2,(i//5%4-1.5)*1.05,-(i//20)*.8); GL.glRotatef(elapsed*38+i*22,1,.4,1)
                    GL.glColor3f(.12+(i%4)*.17,.34+(i%3)*.18,.72)
                    GL.glBegin(GL.GL_LINE_LOOP)
                    for j in range(48):
                        a=2*_u66_math.pi*j/48; GL.glVertex3f(_u66_math.cos(a)*(.4+(i%3)*.08),_u66_math.sin(a)*(.4+(i%3)*.08),_u66_math.sin(a*3)*.06)
                    GL.glEnd()
                    for j in range(8):
                        a=2*_u66_math.pi*j/8; _u37_draw_gpu_box(GL,_u66_math.cos(a)*.48,_u66_math.sin(a)*.48,0,.11,.11,.11,(.7,.26+(i%3)*.15,.12))
                    GL.glPopMatrix()
            else:
                # Fallback workload is real triangle rendering, never a scripted/pass result.
                GL.glBegin(GL.GL_TRIANGLES)
                for i in range(base*base*8):
                    x=_u66_math.sin(i*.17+elapsed)*4; y=_u66_math.cos(i*.21)*3
                    GL.glColor3f((i%7)/7,.4,.7); GL.glVertex3f(x,y,0); GL.glVertex3f(x+.1,y+.2,.2); GL.glVertex3f(x+.2,y-.1,-.2)
                GL.glEnd()
            GL.glPolygonMode(GL.GL_FRONT_AND_BACK,GL.GL_FILL)
            GL.glFlush(); pg.display.flip(); frames+=1; win_frames+=1; now=_u66_time.perf_counter()
            if now-win_start>=1:
                fps=win_frames/(now-win_start); samples.append(round(fps,2)); peak=max(peak,fps); win_frames=0; win_start=now
                pg.display.set_caption(f"NAPRAWA PC 3D {sid}/{len(_U66_SCENES)} • {name} • FPS {fps:.1f} • ESC = stop • {renderer[:80]}")
        elapsed=max(.001,_u66_time.perf_counter()-start)
        result.update({"state":"good" if frames else "warn","renderer":renderer,"opengl_version":version,"frames":frames,"duration_seconds":round(elapsed,2),"average_fps":round(frames/elapsed,2),"peak_fps_1s":round(peak,2),"fps_samples":samples,"workload":kind,"complexity":complexity,"scene_id":sid,"scene_name":name,"stopped_by_user":elapsed<requested-.5})
        pg.display.quit(); pg.quit()
    except Exception as exc:
        result.update({"state":"warn","error":f"{type(exc).__name__}: {exc}","note":"Render 3D nie wystartował lub sterownik nie udostępnił OpenGL. Nie oznacza to automatycznie awarii GPU."})
        try:
            if pg is not None: pg.display.quit(); pg.quit()
        except Exception: pass
    try:
        Path(output_path).write_text(_u66_json.dumps(result,ensure_ascii=False),encoding="utf-8")
    except Exception: pass

def _u66_set_suite_status(self,text):
    try:
        self.queue_status(text)
        self.queue_action(lambda m=text:_u66_update_suite_label(self,m))
        self.queue_log(text)
    except Exception: pass

def _u66_update_suite_label(self,text):
    try:
        for name in ("_u66_3d_status","_u66_speed_status"):
            lbl=getattr(self,name,None)
            if lbl is not None and lbl.winfo_exists():
                lbl.config(text=str(text))
    except Exception: pass

def _u66_execute_gpu_scene(self,scene_id,seconds=5):
    output=Path(tempfile.gettempdir())/("naprawapc_gpu_scene_"+str(os.getpid())+"_"+str(scene_id)+"_"+_u66_uuid.uuid4().hex[:8]+".json")
    try: output.unlink(missing_ok=True)
    except Exception: pass
    if getattr(sys,"frozen",False):
        cmd=[sys.executable,"--gpu-benchmark",str(output),str(int(scene_id)),str(int(seconds))]
    else:
        cmd=[sys.executable,str(Path(__file__).resolve()),"--gpu-benchmark",str(output),str(int(scene_id)),str(int(seconds))]
    _u66_set_suite_status(self,f"SCENA 3D {scene_id}/{len(_U66_SCENES)} — {_U66_SCENES[scene_id-1][0]} — uruchamianie OpenGL…")
    proc=None
    try:
        proc=_u66_subprocess.Popen(cmd,cwd=tempfile.gettempdir(),creationflags=getattr(_u66_subprocess,"CREATE_NO_WINDOW",0))
        deadline=_u66_time.monotonic()+max(20,int(seconds)+40)
        while proc.poll() is None and _u66_time.monotonic()<deadline:
            if getattr(self,"stop_requested",False):
                proc.terminate()
                try: proc.wait(timeout=3)
                except Exception: proc.kill()
                break
            _u66_time.sleep(.25)
        if proc.poll() is None:
            proc.kill()
        rc=proc.wait(timeout=5)
        if not output.is_file():
            result={"state":"warn","scene_id":scene_id,"scene_name":_U66_SCENES[scene_id-1][0],"error":f"Brak raportu renderera; kod procesu {rc}."}
        else:
            result=_u66_json.loads(output.read_text(encoding="utf-8"))
            result["returncode"]=rc
        try: output.unlink(missing_ok=True)
        except Exception: pass
        self.queue_results("3D_SCENE_"+str(scene_id),result)
        self.queue_log(f"3D SCENA {scene_id}: {result.get('state')} | FPS={result.get('average_fps','N/D')} | {result.get('renderer',result.get('error','N/D'))}")
        return result
    except Exception as exc:
        result={"state":"warn","scene_id":scene_id,"scene_name":_U66_SCENES[scene_id-1][0],"error":f"{type(exc).__name__}: {exc}"}
        self.queue_results("3D_SCENE_"+str(scene_id),result)
        return result

def _u66_show_3d_studio(self):
    self.current_view="3D_STUDIO"; self.clear(); t=self.colors()
    self.header_title.config(text="3D BENCHMARK STUDIO — 40 SCEN • ULTRA / MAX")
    info=self.panel(self.content); info.pack(fill="x",pady=(0,7))
    tk.Label(info,text="RZECZYWISTE RENDEROWANIE OPENGL • ŚREDNI FPS • PEAK 1 s • RENDERER • CZAS",bg=t["panel"],fg=t["accent"],font=self.fnt(12,"bold")).pack(anchor="w",padx=12,pady=(9,3))
    tk.Label(info,text="Sceny proceduralne badają różne obciążenia geometrii. Nie są wynikami gier ani porównaniem sprzętu między różnymi API i rozdzielczościami.",bg=t["panel"],fg=t["muted"],font=self.fnt(8),wraplength=1400,justify="left").pack(anchor="w",padx=12,pady=(0,8))
    options=tk.Frame(self.content,bg=t["bg"]); options.pack(fill="x",pady=4)
    names=[f"{i+1:02d} — {sc[0].split('—',1)[-1].strip()}" for i,sc in enumerate(_U66_SCENES)]
    self._u66_scene_var=tk.StringVar(value=names[0])
    ttk.Combobox(options,textvariable=self._u66_scene_var,values=names,state="readonly",width=42).pack(side="left",padx=3,ipady=4)
    self._u66_scene_seconds=tk.StringVar(value="15 s")
    ttk.Combobox(options,textvariable=self._u66_scene_seconds,values=("5 s","15 s","30 s","60 s","120 s","300 s"),state="readonly",width=10).pack(side="left",padx=3,ipady=4)
    tk.Label(options,text="CZAS / PROFIL",bg=t["bg"],fg=t["muted"],font=self.fnt(8,"bold")).pack(side="left",padx=(6,2))
    self._u66_3d_status=tk.Label(self.content,text="Gotowy — wybierz scenę albo uruchom wszystkie 40. Profil: STANDARD / ULTRA / MAX.",bg=t["bg"],fg=t["muted"],font=self.fnt(9,"bold"),anchor="w")
    self._u66_3d_status.pack(fill="x",padx=4,pady=5)
    table=self.panel(self.content); table.pack(fill="both",expand=True,pady=5)
    cols=("SCENA","STATUS","FPS ŚREDNI","FPS PEAK","KLATKI","RENDERER / UWAGI")
    self._u66_3d_tree=self.make_tree(table,cols)
    for i,sc in enumerate(_U66_SCENES,1):
        res=self.results.get("3D_SCENE_"+str(i),{}) or {}
        self._u66_3d_tree.insert("","end",iid=str(i),values=(sc[0],res.get("state","—"),res.get("average_fps","N/D"),res.get("peak_fps_1s","N/D"),res.get("frames","N/D"),res.get("renderer",res.get("error","—"))))
    row=tk.Frame(self.content,bg=t["bg"]); row.pack(fill="x")
    self.make_button(row,"▶ URUCHOM WYBRANĄ SCENĘ",lambda:_u66_start_3d_one(self),"accent",side="left",ipady=5)
    self.make_button(row,"▶ WSZYSTKIE 40 SCEN",lambda:_u66_start_3d_all(self),"good",side="left",ipady=5)
    self.make_button(row,"OCENA GIER / USTAWIENIA",lambda:_u68_show_game_guide(self),"card",side="left",ipady=5)
    self.make_button(row,"← TESTY",self.show_tests_hub,"card",side="left",ipady=5)

def _u66_start_3d_one(self):
    try:
        name=str(self._u66_scene_var.get()).split("—",1)[0].strip()
        sid=int(name)
        seconds=int(str(self._u66_scene_seconds.get()).split()[0])
    except Exception:
        sid=1; seconds=5
    def job():
        result=_u66_execute_gpu_scene(self,sid,seconds)
        self.queue_action(lambda:_u66_show_3d_studio(self))
        if result.get("state")=="warn":
            self.queue_action(lambda:messagebox.showwarning("3D Benchmark",str(result.get("error") or result.get("note") or "Brak wyniku.")))
    self.worker(job)

def _u66_start_3d_all(self):
    try: seconds=int(str(self._u66_scene_seconds.get()).split()[0])
    except Exception: seconds=5
    if not messagebox.askyesno("40 scen 3D — ULTRA / MAX",f"Uruchomić {len(_U66_SCENES)} scen, każdą przez {seconds} s? Łączny czas renderowania to co najmniej {len(_U66_SCENES)*seconds} sekund. Profile 60/120/300 s są długimi testami obciążeniowymi. ESC zatrzymuje aktywną scenę."):
        return
    self.worker(lambda:_u66_run_3d_suite(self,seconds))

def _u66_run_3d_suite(self,seconds=5):
    def show_suite_view(scene_no=0):
        _u66_show_3d_studio(self)
        if getattr(self,"_u67_sequence_active",False):
            stage_no=getattr(self,"_u67_current_num",1)
            stage_total=getattr(self,"_u67_current_total",1)
            stage_title=getattr(self,"_u67_current_title","3D Benchmark")
            suffix=f" — scena {scene_no}/{len(_U66_SCENES)}" if scene_no else ""
            _u67_stage_live_panel(self,stage_no,stage_total,stage_title+suffix)
    self._u66_ui_wait(self,lambda:show_suite_view(0))
    results=[]
    for i,sc in enumerate(_U66_SCENES,1):
        if self._test_should_stop(): break
        self._u66_set_suite_status(self,f"3D BENCHMARK: scena {i}/{len(_U66_SCENES)} — {sc[0]}")
        r=_u66_execute_gpu_scene(self,i,seconds); results.append(r)
        self._u66_ui_wait(self,lambda i=i:show_suite_view(i))
    good=sum(1 for r in results if r.get("state")=="good")
    report={"state":"good" if good==len(results) and results else "warn","completed":len(results),"good":good,"scenes":results,"time":_U66_datetime.now().isoformat(timespec="seconds")}
    self.results["3D_SUITE"]=report
    try:
        folder=_u66_store_dir()/"benchmarks"; folder.mkdir(parents=True,exist_ok=True)
        (folder/("3d-benchmark-"+_U66_datetime.now().strftime("%Y%m%d-%H%M%S")+".json")).write_text(_u66_json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
    except Exception: pass
    self.queue_log(f"3D STUDIO: ukończono {len(results)}/{len(_U66_SCENES)} scen; wyniki prawidłowe: {good}.")

def _u66_ui_wait(self,callback,timeout=10):
    event=_u66_threading.Event()
    def run():
        try: callback()
        except Exception as exc:
            try: self.append_log("UI stage switch: "+repr(exc))
            except Exception: pass
        finally: event.set()
    self.queue_action(run)
    event.wait(timeout)

def _u66_start_all_tests(self):
    if getattr(self,"running",False):
        messagebox.showinfo("Testy","Inny test już trwa. Poczekaj, aż się zakończy.")
        return
    if not messagebox.askyesno("Wszystkie testy po kolei","Pełna sekwencja LIVE uruchamia CPU, RAM, GPU, 40 scen 3D, dysk, matrycę, Internet Speed Test, bezpieczeństwo, baterię i USB/sieć. Przy profilu 5 s na scenę renderowanie zajmie co najmniej 200 sekund, do tego dochodzą pozostałe testy. Test można zatrzymać przyciskiem STOP TEST."):
        return
    self.worker(self._u66_run_all_tests_worker)

def _u66_run_all_tests_worker(self):
    started=_U66_datetime.now().isoformat(timespec="seconds")
    summary=[]
    def stage(num,total,title,view,fn):
        if self._test_should_stop(): return
        _u66_set_suite_status(self,f"TEST {num}/{total}: {title}")
        _u66_ui_wait(self,lambda:view())
        if self._test_should_stop(): return
        try:
            fn()
            item={"stage":title,"state":"completed","time":_U66_datetime.now().isoformat(timespec="seconds")}
        except Exception as exc:
            item={"stage":title,"state":"error","error":f"{type(exc).__name__}: {exc}","time":_U66_datetime.now().isoformat(timespec="seconds")}
            self.queue_log(f"TEST {title}: błąd {item['error']}")
        summary.append(item)
        _u66_ui_wait(self,lambda:view())
    total=10
    stage(1,total,"CPU — obciążenie i zegary",lambda:self.show_module("CPU"),lambda:self._cpu_test(8))
    stage(2,total,"RAM — wzorce",lambda:self.show_module("RAM"),lambda:self._ram_test(256))
    stage(3,total,"GPU — adapter i sterownik",lambda:self.show_module("GPU"),self._gpu_test)
    stage(4,total,"3D Benchmark — 40 scen po kolei",lambda:_u66_show_3d_studio(self),lambda:_u66_run_3d_suite(self,5))
    stage(5,total,"SSD/HDD — odczyt i zapis",lambda:self.show_module("DYSK"),lambda:self._disk_test(128))
    stage(6,total,"Matryca — EDID",lambda:self.show_module("EKRAN"),self._monitor_test)
    def net_job():
        self._u66_speed_running=True
        try:
            result=_u66_measure_speed(self); self.results["SPEED_TEST"]=result
        finally:
            self._u66_speed_running=False
    stage(7,total,"Internet — Speed Test download/upload",lambda:_u66_show_speed_test(self),net_job)
    stage(8,total,"Bezpieczeństwo — Defender/autostart",lambda:self.show_module("SECURITY"),self._security_test)
    stage(9,total,"Bateria / zasilanie",lambda:self.show_battery_or_power(),self._battery_test)
    def peripherals():
        for key in ("USB","SIEĆ"):
            if self._test_should_stop(): break
            try: self._peripheral_test(key)
            except Exception as exc: self.queue_log(f"{key}: {type(exc).__name__}: {exc}")
    stage(10,total,"USB i sieć — enumeracja",lambda:self.show_simple_module("USB / URZĄDZENIA"),peripherals)
    report={"state":"warn" if self._test_should_stop() or any(x.get("state")=="error" for x in summary) else "completed","started":started,"finished":_U66_datetime.now().isoformat(timespec="seconds"),"stages":summary}
    self.results["ALL_TESTS_SEQUENCE"]=report
    try:
        folder=_u66_store_dir()/"reports"; folder.mkdir(parents=True,exist_ok=True)
        target=folder/("all-tests-"+_U66_datetime.now().strftime("%Y%m%d-%H%M%S")+".json")
        target.write_text(_u66_json.dumps({"suite":report,"results":self.results},ensure_ascii=False,indent=2,default=str),encoding="utf-8")
        report["report_path"]=str(target)
    except Exception: pass
    self.queue_log(f"WSZYSTKIE TESTY: {report['state']} — etapy {len(summary)}/{total}.")
    self.queue_status("Testy zakończone" if not self._test_should_stop() else "Testy zatrzymane.")
    self.queue_action(self.show_report)


# v4.3.71 — route dashboard full diagnostic into per-test live views.
# This explicitly replaces the legacy RUN_MONITOR-only route.
def _u67_stage_live_panel(self, index, total, title):
    try:
        old = getattr(self, "_u67_stage_panel", None)
        if old is not None and old.winfo_exists():
            old.destroy()
    except Exception:
        pass
    t = self.colors()
    panel = tk.Frame(self.content, bg=t["panel"], highlightbackground=t["accent"], highlightthickness=1)
    children = self.content.winfo_children()
    if children:
        panel.pack(fill="x", padx=2, pady=(0, 6), before=children[0])
    else:
        panel.pack(fill="x", padx=2, pady=(0, 6))
    self._u67_stage_panel = panel
    top = tk.Frame(panel, bg=t["panel"])
    top.pack(fill="x", padx=10, pady=(6, 3))
    header_text = f"TEST {index}/{total} — {title}" if total > 0 else title
    self._u67_stage_title = tk.Label(top, text=header_text, bg=t["panel"], fg=t["accent"], font=self.fnt(10, "bold"), anchor="w")
    self._u67_stage_title.pack(side="left", fill="x", expand=True)
    if total > 0:
        self.make_button(top, "STOP TEST", self.stop_current_test, "bad", side="right", ipady=3)
    self._u67_stage_values = {}
    metrics = tk.Frame(panel, bg=t["panel"])
    metrics.pack(fill="x", padx=6, pady=(0, 5))
    metric_specs = [
        ("CPU", "cpu"), ("RAM", "ram"), ("GPU", "gpu"), ("TEMP CPU", "cpu_temp"),
        ("TEMP GPU", "gpu_temp"), ("DYSK ODCZYT", "disk_read"), ("DYSK ZAPIS", "disk_write"),
        ("NET ↓", "net_down"), ("NET ↑", "net_up")
    ]
    for i, (label, key) in enumerate(metric_specs):
        card = tk.Frame(metrics, bg=t["card"], highlightbackground=t["accent2"], highlightthickness=1)
        card.grid(row=i // 5, column=i % 5, sticky="nsew", padx=2, pady=2)
        tk.Label(card, text=label, bg=t["card"], fg=t["muted"], font=self.fnt(7, "bold")).pack(padx=5, pady=(3, 0))
        value = tk.Label(card, text="N/D", bg=t["card"], fg=t["accent"], font=self.fnt(9, "bold"))
        value.pack(padx=5, pady=(0, 3))
        self._u67_stage_values[key] = value
    for col in range(5):
        metrics.grid_columnconfigure(col, weight=1)
    graphs = tk.Frame(panel, bg=t["panel"])
    graphs.pack(fill="x", padx=6, pady=(0, 6))
    self._u67_stage_chart_hw = tk.Canvas(graphs, height=82, bg=t["card"], highlightthickness=0)
    self._u67_stage_chart_hw.pack(side="left", fill="both", expand=True, padx=(0, 3))
    self._u67_stage_chart_io = tk.Canvas(graphs, height=82, bg=t["card"], highlightthickness=0)
    self._u67_stage_chart_io.pack(side="left", fill="both", expand=True, padx=(3, 0))
    if not hasattr(self, "_u67_hist"):
        self._u67_hist = {"cpu": [], "ram": [], "gpu": [], "read": [], "write": [], "down": [], "up": []}
    self._u67_stage_key = title
    _u67_refresh_visible_charts(self)


def _u67_draw_history_chart(canvas, series, maximum, title, app):
    if canvas is None or not canvas.winfo_exists():
        return
    t = app.colors()
    canvas.delete("all")
    w = max(220, canvas.winfo_width() or 500)
    h = max(70, canvas.winfo_height() or 82)
    left, right, top, bottom = 32, w - 8, 15, h - 16
    canvas.create_text(8, 3, text=title, anchor="nw", fill=t["muted"], font=app.fnt(7, "bold"))
    maxval = max(1.0, float(maximum or 1))
    for pct in (0, 50, 100):
        y = bottom - (bottom - top) * pct / 100
        canvas.create_line(left, y, right, y, fill=t["panel"], width=1)
    palette = [
        ("cpu", t["accent"]), ("ram", t["good"]), ("gpu", t["warn"]),
        ("read", t["accent2"]), ("write", t["good"]), ("down", t["warn"]), ("up", t["accent"])
    ]
    for key, color in palette:
        vals = series.get(key, [])
        if len(vals) < 2:
            continue
        points = []
        vals = vals[-60:]
        for i, value in enumerate(vals):
            x = left + (right - left) * i / max(1, len(vals) - 1)
            y = bottom - (bottom - top) * max(0, min(maxval, float(value))) / maxval
            points.extend((x, y))
        if len(points) >= 4:
            try:
                canvas.create_line(*points, fill=color, width=2, smooth=True)
            except Exception:
                pass
    canvas.create_text(left + 4, top + 2, text="ostatnie próbki / 1 s", anchor="nw", fill=t["muted"], font=app.fnt(6))


def _u67_refresh_visible_charts(self):
    vals = getattr(self, "_live_values", {}) or {}
    cache = getattr(self, "_u66_sensor_cache", {}) or {}
    gpu = cache.get("gpu", {}) or {}
    temps = cache.get("temps", {}) or {}
    def numeric(x):
        try:
            v = float(x)
            return v if _u66_math.isfinite(v) else None
        except Exception:
            return None
    cpu = numeric(vals.get("cpu"))
    ram = numeric(vals.get("ram"))
    gpu_load = numeric(gpu.get("gpu_load_percent", getattr(self, "_gpu_util", None)))
    cpu_temp = numeric(temps.get("cpu_temp_c"))
    gpu_temp = numeric(gpu.get("temperature_c", temps.get("gpu_temp_c")))
    acpi_val = None
    if cpu_temp is None:
        acpi = temps.get("acpi_zones") or []
        acpi_val = numeric(acpi[0].get("value")) if acpi else None
    now = _u66_time.monotonic()
    try:
        io = psutil.disk_io_counters() if psutil else None
    except Exception:
        io = None
    read_rate = write_rate = None
    prev = getattr(self, "_u67_disk_prev", None)
    if io:
        if prev:
            dt = max(0.1, now - prev[2])
            read_rate = max(0.0, (io.read_bytes - prev[0]) / dt / 1_000_000)
            write_rate = max(0.0, (io.write_bytes - prev[1]) / dt / 1_000_000)
        self._u67_disk_prev = (io.read_bytes, io.write_bytes, now)
    down = numeric(vals.get("recv"))
    up = numeric(vals.get("sent"))
    shown = {
        "cpu": f"{cpu:.1f}%" if cpu is not None else "N/D",
        "ram": f"{ram:.1f}%" if ram is not None else "N/D",
        "gpu": f"{gpu_load:.1f}%" if gpu_load is not None else "N/D",
        "cpu_temp": f"{cpu_temp:.1f} °C" if cpu_temp is not None else (f"ACPI {acpi_val:.1f} °C" if acpi_val is not None else "N/D"),
        "gpu_temp": f"{gpu_temp:.1f} °C" if gpu_temp is not None else "N/D",
        "disk_read": f"{read_rate:.2f} MB/s" if read_rate is not None else "N/D",
        "disk_write": f"{write_rate:.2f} MB/s" if write_rate is not None else "N/D",
        "net_down": f"{down * 8 / 1_000_000:.2f} Mbps" if down is not None else "N/D",
        "net_up": f"{up * 8 / 1_000_000:.2f} Mbps" if up is not None else "N/D"
    }
    for key, value in shown.items():
        try:
            label = getattr(self, "_u67_stage_values", {}).get(key)
            if label is not None and label.winfo_exists():
                label.config(text=value)
        except Exception:
            pass
    hist = getattr(self, "_u67_hist", None)
    if hist is not None:
        for key, value in (
            ("cpu", cpu), ("ram", ram), ("gpu", gpu_load), ("read", read_rate), ("write", write_rate),
            ("down", down * 8 / 1_000_000 if down is not None else None),
            ("up", up * 8 / 1_000_000 if up is not None else None)
        ):
            if value is not None and _u66_math.isfinite(float(value)):
                hist[key].append(float(value))
                hist[key] = hist[key][-60:]
    try:
        _u67_draw_history_chart(getattr(self, "_u67_stage_chart_hw", None), hist or {}, 100, "CPU / RAM / GPU %", self)
        io_series = {"read": (hist or {}).get("read", []), "write": (hist or {}).get("write", []), "down": (hist or {}).get("down", []), "up": (hist or {}).get("up", [])}
        io_vals = io_series["read"] + io_series["write"] + io_series["down"] + io_series["up"]
        io_max = max([1.0] + io_vals)
        _u67_draw_history_chart(getattr(self, "_u67_stage_chart_io", None), io_series, io_max, "DYSK MB/s • SIEĆ Mbps", self)
    except Exception:
        pass
    try:
        if getattr(self, "current_view", "") == "CPU":
            chart = getattr(self, "cpu_module_chart", None)
            if chart is not None and chart.winfo_exists():
                self.draw_sparkline(chart, getattr(self, "_history", {}).get("cpu", []))
    except Exception:
        pass


def _u67_run_visible_speed_test(self):
    self._u66_speed_running = True
    try:
        result = _u66_measure_speed(self)
        self.results["SPEED_TEST"] = result
        def finish():
            if getattr(self, "current_view", "") == "SPEED_TEST":
                for key, val in (
                    ("latency", str(result.get("latency_average_ms", "N/D")) + " ms"),
                    ("download", str(result.get("download_mbps", "N/D")) + " Mbps"),
                    ("upload", str(result.get("upload_mbps", "N/D")) + " Mbps"),
                    ("data", f"{result.get('data_bytes', 0) / 1_000_000:.1f} MB")
                ):
                    try: self._u66_speed_values[key].config(text=val)
                    except Exception: pass
                _u66_draw_speed_chart(self, result)
            _u66_set_speed_status(self, f"Speed Test zakończony: download {result.get('download_mbps', 'N/D')} Mbps / upload {result.get('upload_mbps', 'N/D')} Mbps.")
        _u66_ui_wait(self, finish)
        return result
    finally:
        self._u66_speed_running = False


def _u67_test_state(self, result_keys):
    for key in result_keys:
        obj = (getattr(self, "results", {}) or {}).get(key)
        if isinstance(obj, dict) and obj.get("state") in ("good", "warn", "bad", "error"):
            return obj.get("state"), key
    return "not_reported", "N/D"


def _u67_run_selected_diagnostic(self, selected):
    order = [
        ("CPU", "CPU — obciążenie i zegary", lambda: self.show_module("CPU"), lambda: self._cpu_test(20), ["CPU"]),
        ("GPU", "GPU — karta i sterownik", lambda: self.show_module("GPU"), self._gpu_test, ["GPU"]),
        ("RAM", "RAM — test wzorców", lambda: self.show_module("RAM"), lambda: self._ram_test(2048), ["RAM"]),
        ("DYSKI", "SSD/HDD/NVMe — odczyt i zapis", lambda: self.show_module("DYSK"), lambda: self._disk_test(768), ["DYSK"]),
        ("MATRYCA", "Matryca — EDID i tryby ekranu", lambda: self.show_module("EKRAN"), self._monitor_test, ["EKRAN"]),
        ("BATERIA", "Bateria / zasilanie", lambda: self.show_battery_or_power(), self._battery_test, ["BATERIA"]),
        ("KLAWIATURA", "Klawiatura / touchpad", lambda: self.show_simple_module("KLAWIATURA / TOUCHPAD"), lambda: self._peripheral_test("KLAWIATURA"), ["KLAWIATURA", "PERIPHERAL_KLAWIATURA"]),
        ("AUDIO", "Audio — urządzenia", lambda: self.show_simple_module("DŹWIĘK / AUDIO"), lambda: self._peripheral_test("AUDIO"), ["AUDIO", "PERIPHERAL_AUDIO"]),
        ("SIEC", "Internet — Speed Test download/upload", lambda: _u66_show_speed_test(self), lambda: _u67_run_visible_speed_test(self), ["SPEED_TEST"]),
        ("SYSTEM_SECURITY", "Windows / bezpieczeństwo", lambda: self.show_module("SECURITY"), self._selected_system_security_test, ["SECURITY", "SYSTEM"])
    ]
    chosen = [entry for entry in order if entry[0] in selected]
    if not chosen:
        self.queue_log("PEŁNA DIAGNOSTYKA: brak wybranych testów.")
        return
    expanded = []
    for entry in chosen:
        expanded.append(entry)
        if entry[0] == "GPU":
            expanded.append(("__3D__", "3D Benchmark Studio — 40 scen OpenGL", lambda: _u66_show_3d_studio(self), lambda: _u66_run_3d_suite(self, 5), ["3D_SUITE"]))
        if entry[0] == "SIEC":
            expanded.append(("__USB__", "USB — enumeracja urządzeń", lambda: self.show_simple_module("USB / URZĄDZENIA"), lambda: self._peripheral_test("USB"), ["USB"]))
    started = _U66_datetime.now().isoformat(timespec="seconds")
    summary = []
    total = len(expanded)
    self.queue_log("=== START PEŁNEJ DIAGNOSTYKI LIVE: " + ", ".join(x[0] for x in chosen) + " ===")
    for num, (key, title, view, fn, result_keys) in enumerate(expanded, 1):
        if self._test_should_stop():
            self.queue_log("Diagnostyka: użytkownik zatrzymał przebieg.")
            break
        def prepare_view(view=view, num=num, title=title):
            self._u67_sequence_active = True
            self._u67_current_num = num
            self._u67_current_total = total
            self._u67_current_title = title
            view()
            _u67_stage_live_panel(self, num, total, title)
            try:
                self.header_status.config(text=f"TEST {num}/{total}", fg=self.colors()["warn"])
            except Exception:
                pass
        _u67_set_suite_status(self, f"TEST {num}/{total}: {title}")
        _u66_ui_wait(self, prepare_view)
        if self._test_should_stop():
            break
        error = None
        try:
            fn()
        except Exception as exc:
            error = f"{type(exc).__name__}: {exc}"
            self.queue_log(f"TEST {title}: BŁĄD: {error}")
        _u66_ui_wait(self, lambda: None)
        if error:
            state = "error"
        else:
            state, result_key = _u67_test_state(self, result_keys)
            if state == "not_reported":
                self.queue_log(f"TEST {title}: brak jednoznacznego wyniku modułu — oznaczono N/D.")
            elif state == "warn":
                self.queue_log(f"TEST {title}: OSTRZEŻENIE (dostępne dane ograniczone).")
            elif state == "bad":
                self.queue_log(f"TEST {title}: WYKRYTO PROBLEM.")
            elif state == "good":
                self.queue_log(f"TEST {title}: PASS dla sprawdzonego zakresu; nie oznacza to pełnego testu całego sprzętu.")
        summary.append({"stage": title, "state": state, "result_key": result_keys, "error": error, "time": _U66_datetime.now().isoformat(timespec="seconds")})
        self.queue_log(f"=== ZAKOŃCZONO ETAP {num}/{total}: {title} — {state} ===")
        _u66_ui_wait(self, lambda: _u67_refresh_visible_charts(self))
        if self._test_should_stop():
            break
        _u66_time.sleep(1.5)
    failed = any(x.get("state") in ("bad", "error", "warn", "not_reported") for x in summary)
    report = {
        "state": "warn" if failed or self._test_should_stop() or len(summary) != total else "completed",
        "started": started, "finished": _U66_datetime.now().isoformat(timespec="seconds"),
        "selected": selected, "stages": summary, "completed_stages": len(summary), "total_stages": total
    }
    self.results["ALL_TESTS_SEQUENCE"] = report
    try:
        folder = _u66_store_dir() / "reports"
        folder.mkdir(parents=True, exist_ok=True)
        target = folder / ("full-diagnostic-" + _U66_datetime.now().strftime("%Y%m%d-%H%M%S") + ".json")
        target.write_text(_u66_json.dumps({"suite": report, "results": self.results}, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        report["report_path"] = str(target)
    except Exception as exc:
        self.queue_log("Nie udało się zapisać raportu pełnej diagnostyki: " + repr(exc))
    self.queue_log(f"=== KONIEC PEŁNEJ DIAGNOSTYKI: {report['state']} — {len(summary)}/{total} etapów ===")
    self._u67_sequence_active = False
    self.queue_action(self.show_report)


def _u67_start_selected_diagnostic(self):
    if getattr(self, "running", False):
        messagebox.showinfo("Pełna diagnostyka", "Test już trwa. Poczekaj albo użyj STOP TEST.")
        return
    opts = getattr(self, "full_test_options", None) or {}
    selected = [k for k, v in opts.items() if v]
    if not selected:
        messagebox.showwarning("Pełna diagnostyka", "Zaznacz przynajmniej jeden moduł.")
        return
    labels = {
        "CPU": "CPU", "GPU": "GPU + 40 scen 3D", "RAM": "RAM", "DYSKI": "Dyski",
        "MATRYCA": "Matryca / EDID", "BATERIA": "Bateria", "KLAWIATURA": "Klawiatura / touchpad",
        "AUDIO": "Audio", "SIEC": "Internet Speed Test + USB", "SYSTEM_SECURITY": "Windows i bezpieczeństwo"
    }
    names = [labels.get(k, k) for k in selected]
    if not messagebox.askyesno(
        "Pełna diagnostyka — sekwencja LIVE",
        "Uruchomić wybrane testy po kolei? Każdy etap otworzy własny ekran z metrykami i wykresami. "
        "Brak czujnika będzie oznaczony N/D, a nie PASS. Test sieci przesyła około 24 MB.\n\n"
        "Kolejność: " + " → ".join(names) + "\n\nESC lub STOP TEST zatrzymuje przebieg."
    ):
        return
    self._refresh_after_worker_view = None
    self.worker(lambda: _u67_run_selected_diagnostic(self, selected))


def _u67_init_with_sensor_poll(self):
    _U66_ORIGINAL_INIT_FOR_SENSOR(self)
    try:
        self.after(1600, lambda: _u66_sensor_poll(self))
    except Exception:
        pass



# v4.3.72 — explicit controls for every module: scan, real benchmark, 3D visualizer.
_U68_PROFILE_SECONDS = {"SZYBKI 5 s":5, "STANDARD 15 s":15, "ULTRA 60 s":60, "MAX 120 s":120, "EXTREME 300 s":300}
_U68_MODULE_SCENES = {
    "CPU":21, "RAM":25, "DYSK":29, "GPU":35, "VRAM":34,
    "EKRAN":38, "BATERIA":39, "SIEC":37, "AUDIO":37,
    "KLAWIATURA":37, "USB":37, "SECURITY":40, "SYSTEM":40
}
_U68_GAME_GUIDE = [
    ("Counter-Strike 2","konkurencyjny: niskie/średnie; wyłącz ciężkie efekty","CPU + GPU"),
    ("Valorant","wysokie/ultra zwykle lekkie; celuj w stabilne FPS","CPU"),
    ("Fortnite","Performance Mode dla FPS; DX12 medium/high po sprawdzeniu VRAM","GPU/VRAM"),
    ("Apex Legends","medium/high; ogranicz cienie i efekty","GPU"),
    ("Call of Duty: Warzone","low/medium, upscaling i tekstury według VRAM","GPU/VRAM"),
    ("Grand Theft Auto V Legacy","high/very high; ogranicz advanced distance scaling","GPU/CPU"),
    ("GTA V Enhanced","medium/high, ray tracing off przy słabszym GPU","GPU/VRAM"),
    ("Forza Horizon 5","high; sprawdź VRAM i stabilność 1% low","GPU"),
    ("Red Dead Redemption 2","balanced/high; jakość tekstur zależna od VRAM","GPU/VRAM"),
    ("Cyberpunk 2077","medium/high bez RT; DLSS/FSR/XeSS zależnie od GPU","GPU/VRAM"),
    ("The Witcher 3 Next-Gen","high bez RT lub medium z RT i upscalingiem","GPU"),
    ("Elden Ring","high; gra ma limit FPS zależny od wersji","GPU"),
    ("Hogwarts Legacy","medium, tekstury dopasuj do VRAM; RT off przy słabszym GPU","VRAM"),
    ("Baldur's Gate 3","high; scena i liczba NPC wpływa na CPU","CPU/GPU"),
    ("Diablo IV","high; sprawdź VRAM i tekstury","GPU/VRAM"),
    ("Overwatch 2","high/ultra; profil FPS z naciskiem na CPU","CPU/GPU"),
    ("Rainbow Six Siege","high; celuj w wysoką płynność","CPU/GPU"),
    ("PUBG","medium/high; ogranicz cienie i efekty","CPU/GPU"),
    ("Minecraft Java","shadery osobno; bez shaderów wymagania są dużo niższe","CPU/GPU"),
    ("Microsoft Flight Simulator","medium, render scale i LOD według CPU/RAM/VRAM","CPU/RAM/GPU"),
    ("Starfield","low/medium, upscaling; obserwuj VRAM","GPU/VRAM"),
    ("Alan Wake 2","low/medium z upscalingiem; RT zwykle bardzo wymagający","GPU/VRAM"),
    ("DOOM Eternal","high/ultra gdy GPU i VRAM pozwalają","GPU/VRAM"),
    ("EA SPORTS F1","high; obniż odbicia i ray tracing przy spadkach","GPU"),
    ("Cities: Skylines II","low/medium; mocno zależy od CPU/RAM i rozmiaru miasta","CPU/RAM"),
    ("Escape from Tarkov","low/medium, obserwuj RAM/VRAM i 1% low","CPU/RAM"),
    ("Helldivers 2","medium, upscaling i skalowanie renderingu","GPU/CPU"),
    ("Monster Hunter Wilds","low/medium z upscalingiem; sprawdź aktualne wymagania gry","GPU/VRAM"),
    ("League of Legends","wysokie zwykle lekkie; monitoruj CPU i stabilność","CPU"),
    ("Dota 2","high; płynność zależy też od sceny i CPU","CPU/GPU"),
    ("Roblox","zależnie od konkretnej gry/świata; brak jednej wspólnej oceny","GPU/CPU")
]

def _u68_get_profile(self):
    raw = str(getattr(self, "_u68_profile_var", tk.StringVar(value="STANDARD 15 s")).get())
    return _U68_PROFILE_SECONDS.get(raw, 15)

def _u68_start_visualizer(self, module, scene_id=None):
    scene_id = int(scene_id or _U68_MODULE_SCENES.get(module, 40))
    seconds = _u68_get_profile(self)
    name = _U66_SCENES[scene_id-1][0]
    self.queue_log(f"WIZUALIZATOR 3D {module}: scena {scene_id}/40 — {name} — {seconds} s; FPS mierzy renderer OpenGL.")
    def job():
        result = _u66_execute_gpu_scene(self, scene_id, seconds)
        self.queue_action(lambda: self.results.__setitem__("MODULE_3D_"+module, result))
        self.queue_log(f"WIZUALIZATOR 3D {module}: {result.get('state','N/D')} | FPS {result.get('average_fps','N/D')} | {result.get('renderer',result.get('error','N/D'))}")
    self.worker(job)

def _u68_run_module_action(self, module, action):
    if getattr(self, "running", False):
        messagebox.showinfo("Test sprzętu", "Inny test już trwa. Poczekaj na zakończenie lub zatrzymaj go przyciskiem STOP.")
        return
    aliases = {"DYSKI":"DYSK","SSD":"DYSK","SSD/HDD/NVME":"DYSK","MATRYCA":"EKRAN","DISPLAY":"EKRAN",
               "SIEĆ":"SIEC","WI-FI / LAN":"SIEC","NETWORK":"SIEC","DŹWIĘK / AUDIO":"AUDIO",
               "KLAWIATURA / TOUCHPAD":"KLAWIATURA","USB / URZĄDZENIA":"USB","SYSTEM SECURITY":"SECURITY"}
    module = aliases.get(str(module).strip().upper(), str(module).strip().upper())
    seconds = _u68_get_profile(self)
    profile = str(getattr(self,"_u68_profile_var",tk.StringVar(value="STANDARD 15 s")).get())
    if action == "3d":
        _u68_start_visualizer(self, module)
        return
    if module == "SIEC" and action in ("scan","bench"):
        self.show_speed_test()
        self.after(100, lambda: _u66_start_speed_test(self))
        return
    if module == "VRAM":
        if callable(getattr(self, "_u41_start_vram_test", None)):
            self._u41_start_vram_test()
        else:
            messagebox.showwarning("Test VRAM", "Moduł testu VRAM nie jest dostępny w tej kompilacji.")
        return
    def work():
        try:
            if module == "CPU":
                self._cpu_test(10 if action=="scan" else seconds)
            elif module == "RAM":
                amount = {"SZYBKI 5 s":256,"STANDARD 15 s":512,"ULTRA 60 s":1024,"MAX 120 s":1536,"EXTREME 300 s":2048}.get(profile,512)
                self._ram_test(256 if action=="scan" else amount)
            elif module == "DYSK":
                amount = {"SZYBKI 5 s":256,"STANDARD 15 s":512,"ULTRA 60 s":1024,"MAX 120 s":2048,"EXTREME 300 s":4096}.get(profile,512)
                self._disk_test(256 if action=="scan" else amount)
            elif module == "GPU":
                self._gpu_test()
                if action == "bench":
                    result = _u66_execute_gpu_scene(self,35,seconds)
                    self.queue_log(f"GPU benchmark: FPS={result.get('average_fps','N/D')} renderer={result.get('renderer',result.get('error','N/D'))}")
            elif module == "EKRAN":
                self._monitor_test()
            elif module == "BATERIA":
                self._battery_test()
            elif module == "SECURITY":
                self._selected_system_security_test() if action=="bench" else self._security_test()
            elif module == "AUDIO":
                self._peripheral_test("AUDIO")
            elif module == "KLAWIATURA":
                self._peripheral_test("KLAWIATURA")
            elif module == "USB":
                self._peripheral_test("USB")
            else:
                self.queue_log(f"Brak niezależnego testu dla modułu {module}.")
                return
            self.queue_log(f"{module}: zakończono {'benchmark' if action=='bench' else 'skan'} — profil {seconds} s. Sprawdź raport.")
        except Exception as exc:
            detail = f"{type(exc).__name__}: {exc}"
            self.queue_log(f"{module}: błąd {detail}")
            self.queue_action(lambda detail=detail,module=module: messagebox.showerror(f"Test {module}", detail))
    self.worker(work)

def _u68_add_module_action_panel(self, key, page_kind="hardware"):
    normalized = str(key).strip().upper()
    aliases = {"DYSKI":"DYSK","SSD":"DYSK","SSD/HDD/NVME":"DYSK","MATRYCA":"EKRAN","DISPLAY":"EKRAN",
               "SIEĆ":"SIEC","WI-FI / LAN":"SIEC","NETWORK":"SIEC","DŹWIĘK / AUDIO":"AUDIO",
               "KLAWIATURA / TOUCHPAD":"KLAWIATURA","USB / URZĄDZENIA":"USB","SYSTEM SECURITY":"SECURITY"}
    module = aliases.get(normalized, normalized)
    if module not in _U68_MODULE_SCENES:
        return
    t = self.colors()
    panel = tk.Frame(self.content, bg=t["panel"], highlightbackground=t["accent"], highlightthickness=1)
    children = self.content.winfo_children()
    if children:
        panel.pack(fill="x", padx=3, pady=(0,5), before=children[0])
    else:
        panel.pack(fill="x", padx=3, pady=(0,5))
    tk.Label(panel, text=f"{module} — SKANUJ • BENCHMARK • WIZUALIZATOR 3D", bg=t["panel"], fg=t["accent"], font=self.fnt(9,"bold")).pack(side="left", padx=8, pady=6)
    self._u68_profile_var = tk.StringVar(value="STANDARD 15 s")
    ttk.Combobox(panel, textvariable=self._u68_profile_var, values=tuple(_U68_PROFILE_SECONDS.keys()), state="readonly", width=17).pack(side="left", padx=3, pady=4)
    self.make_button(panel,"SKANUJ",lambda m=module:_u68_run_module_action(self,m,"scan"),"accent",side="left",ipady=4)
    self.make_button(panel,"BENCHMARK / ULTRA",lambda m=module:_u68_run_module_action(self,m,"bench"),"good",side="left",ipady=4)
    self.make_button(panel,"SYMULATOR 3D",lambda m=module:_u68_run_module_action(self,m,"3d"),"card",side="left",ipady=4)
    if module=="GPU":
        self.make_button(panel,"SKANUJ VRAM",lambda:_u68_run_module_action(self,"VRAM","scan"),"accent",side="left",ipady=4)
        self.make_button(panel,"3D VRAM",lambda:_u68_run_module_action(self,"VRAM","3d"),"card",side="left",ipady=4)
    self.make_button(panel,"STOP TEST",self.stop_current_test,"bad",side="left",ipady=4)
    # Every hardware module receives its own continuously refreshed telemetry graphs.
    _u67_stage_live_panel(self,0,0,f"{module} — MONITOR LIVE")

def _u68_show_module_wrapped(self, key):
    _U68_ORIGINAL_SHOW_MODULE(self, key)
    try: _u68_add_module_action_panel(self, key, "hardware")
    except Exception as exc:
        try: self.queue_log("Panel testów modułu: "+repr(exc))
        except Exception: pass

def _u68_show_simple_module_wrapped(self, key):
    _U68_ORIGINAL_SHOW_SIMPLE_MODULE(self, key)
    try: _u68_add_module_action_panel(self, key, "simple")
    except Exception as exc:
        try: self.queue_log("Panel testów modułu: "+repr(exc))
        except Exception: pass

def _u68_show_service_center_wrapped(self):
    _U68_ORIGINAL_SHOW_SERVICE_CENTER(self)
    try:
        t = self.colors()
        row = tk.Frame(self.content, bg=t["bg"])
        children = self.content.winfo_children()
        if children:
            row.pack(fill="x", padx=4, pady=(0,5), before=children[0])
        else:
            row.pack(fill="x", padx=4, pady=(0,5))
        self.make_button(
            row,
            "URUCHOM PEŁNY SYSTEM REPAIR PRO (WPF)",
            lambda: _u68_launch_system_repair(self),
            "accent",
            side="left",
            ipady=5
        )
    except Exception as exc:
        try: self.queue_log("System Repair PRO action button: " + repr(exc))
        except Exception: pass


def _u68_show_game_guide(self):
    self.current_view="GAME_GUIDE"
    self.clear()
    t=self.colors()
    self.header_title.config(text="OCENA GIER — USTAWIENIA GRAFIKI / FPS")
    intro=self.panel(self.content); intro.pack(fill="x",pady=(0,7))
    tk.Label(intro,text="PROFILE GRAFICZNE — WSKAZÓWKI, NIE ZASTĘPUJĄ BENCHMARKU W SAMEJ GRZE",bg=t["panel"],fg=t["accent"],font=self.fnt(12,"bold")).pack(anchor="w",padx=10,pady=(8,3))
    tk.Label(intro,text="Ten przewodnik nie udaje pomiaru FPS w grach. Rekomendacje są startowym profilem; dokładny dobór wymaga modelu GPU, VRAM, RAM, rozdzielczości i pomiaru konkretnej gry. Zapisz wynik gry/benchmarku i dopiero potem dobieraj ustawienia.",bg=t["panel"],fg=t["muted"],font=self.fnt(8),wraplength=1400,justify="left").pack(anchor="w",padx=10,pady=(0,8))
    outer=self.panel(self.content); outer.pack(fill="both",expand=True,pady=4)
    cols=("GRA","PUNKT STARTOWY USTAWIEŃ","GŁÓWNY OGRANICZNIK")
    tree=self.make_tree(outer,cols)
    for row in _U68_GAME_GUIDE:
        tree.insert("","end",values=row)
    row=tk.Frame(self.content,bg=t["bg"]); row.pack(fill="x",pady=4)
    self.make_button(row,"← WRÓĆ DO 3D BENCHMARK",self.show_3d_studio,"card",side="left",ipady=5)
    self.make_button(row,"RAPORT",self.show_report,"card",side="left",ipady=5)

def _u68_start_all_tests_sequential(self):
    """Use the visible, per-module sequential runner for the main ALL button."""
    if getattr(self, "running", False):
        messagebox.showinfo("Wszystkie testy", "Inny test już trwa. Poczekaj albo użyj STOP TEST.")
        return
    selected = ["CPU","GPU","RAM","DYSKI","MATRYCA","BATERIA","KLAWIATURA","AUDIO","SIEC","SYSTEM_SECURITY"]
    stages = len(selected) + 2  # 40-scene GPU suite and USB enumeration are nested stages.
    estimate = "około 6–12 minut, zależnie od szybkości sprzętu i dysku"
    prompt = (
        "Uruchomić WSZYSTKIE TESTY po kolei?\n\n"
        "Każdy test przełączy ekran na dany moduł i pokaże pomiary/wykresy na żywo. "
        "GPU uruchomi dodatkowo 40 scen 3D; sieć wykona test download/upload (~24 MB).\n\n"
        f"Plan: {stages} etapów głównych i podrzędnych; czas: {estimate}. "
        "Długie profile ULTRA/MAX wybiera się osobno w modułach.\n\n"
        "Brak czujnika będzie N/D, a nie fikcyjnym PASS. STOP TEST przerwie przebieg."
    )
    if not messagebox.askyesno("Wszystkie testy — sekwencja LIVE", prompt):
        return
    self._refresh_after_worker_view = None
    self.worker(lambda: _u67_run_selected_diagnostic(self, selected))


def _u68_launch_system_repair(self):
    """Start the full bundled .NET System Repair PRO companion from the installed product directory."""
    try:
        if getattr(sys, "frozen", False):
            base = Path(sys.executable).resolve().parent
        else:
            base = Path(__file__).resolve().parent
        candidates = [
            base / "SystemRepair" / "NAPRAWA-PC-SYSTEM-REPAIR-PRO.exe",
            base / "dist" / "SystemRepair" / "NAPRAWA-PC-SYSTEM-REPAIR-PRO.exe",
            Path(getattr(sys, "_MEIPASS", base)) / "SystemRepair" / "NAPRAWA-PC-SYSTEM-REPAIR-PRO.exe",
        ]
        exe = next((p for p in candidates if p.is_file()), None)
        if exe is None:
            messagebox.showerror(
                "System Repair PRO",
                "Nie znaleziono dołączonej aplikacji WPF. Sprawdź, czy instalator zawiera katalog SystemRepair."
            )
            self.queue_log("System Repair PRO: brak pełnego pliku SystemRepair/NAPRAWA-PC-SYSTEM-REPAIR-PRO.exe.")
            return
        proc = _u66_subprocess.Popen([str(exe)], cwd=str(exe.parent))
        self.queue_log(f"Uruchomiono pełny System Repair PRO: PID={proc.pid}; plik={exe}")
    except Exception as exc:
        detail = f"{type(exc).__name__}: {exc}"
        try:
            self.queue_log("System Repair PRO: " + detail)
        except Exception:
            pass
        messagebox.showerror("System Repair PRO", detail)


def _u66_selftest_advanced():
    assert len(_U66_SCENES)==40, "Studio must have 40 separately named scenes"
    assert len(_U68_GAME_GUIDE)>=30, "Game guide must include at least 30 games"
    assert callable(AppV43.show_module) and callable(AppV43.show_simple_module) and callable(AppV43.show_game_guide)
    assert all(key in _U68_MODULE_SCENES for key in ("CPU","RAM","DYSK","GPU","VRAM"))
    assert callable(_u68_run_module_action) and callable(_u68_start_visualizer)
    assert callable(_u68_launch_system_repair)
    assert callable(_u68_start_all_tests_sequential)
    assert AppV43.start_all_tests_sequential is _u68_start_all_tests_sequential
    assert AppV43.full_test is _u68_start_all_tests_sequential
    assert callable(AppV43.show_service_center)
    assert callable(_u68_show_service_center_wrapped)
    assert len(_U66_KNOWLEDGE_SEED)>=30, "Knowledge seed should cover at least 30 topics"
    assert all(x.get("source","").startswith("https://") for x in _U66_KNOWLEDGE_SEED)
    assert _U66_KNOWLEDGE_PACK_FORMAT == "naprawapc-ai-reader-knowledge"
    assert _U66_KNOWLEDGE_PACK_URL.startswith("https://raw.githubusercontent.com/")
    assert callable(_u66_sync_knowledge_from_server)
    ranked=_u66_rank_knowledge("temperatura CPU GPU",limit=5)
    assert ranked and any("temperatura" in str(x.get("title","")).lower() for x in ranked)
    assert callable(_u66_web_search) and callable(_u66_read_web_page) and callable(_u66_measure_speed)
    assert callable(_u66_scene_child)
    assert callable(_u66_run_all_tests_worker)
    assert callable(_u67_start_selected_diagnostic) and callable(_u67_run_selected_diagnostic)
    assert callable(_u67_refresh_visible_charts) and callable(_u67_stage_live_panel)
    assert AppV43._start_selected_diagnostic is _u67_start_selected_diagnostic
    assert "N/D" in _u67_refresh_visible_charts.__code__.co_consts
    assert _u66_format_rate(1_000_000)=="8.00 Mbps" and _u66_format_rate(0)=="0.00 Mbps"
    print("ADVANCED_MODULES_SELFTEST_OK: live telemetry, internet speed test, AI reader, 20 OpenGL scenes, sequential test suite")

# Integrate into the existing one-window app. Keep the original report/repairs and device test modules.
_U66_ORIGINAL_REFRESH_TELEMETRY=AppV43.refresh_telemetry
AppV43.show_ai_reader=_u66_show_ai_reader
AppV43.show_speed_test=_u66_show_speed_test
AppV43.show_live_monitor=_u66_show_live_monitor
AppV43.show_3d_studio=_u66_show_3d_studio
AppV43.show_tests_hub=_u66_show_tests_hub
AppV43.start_all_tests_sequential=_u68_start_all_tests_sequential
AppV43.full_test=_u68_start_all_tests_sequential
AppV43._start_selected_diagnostic=_u67_start_selected_diagnostic
AppV43._run_selected_diagnostic=_u67_run_selected_diagnostic
_U68_ORIGINAL_SHOW_MODULE=AppV43.show_module
_U68_ORIGINAL_SHOW_SIMPLE_MODULE=AppV43.show_simple_module
AppV43.show_module=_u68_show_module_wrapped
AppV43.show_simple_module=_u68_show_simple_module_wrapped
AppV43.show_game_guide=_u68_show_game_guide
_U68_ORIGINAL_SHOW_SERVICE_CENTER=AppV43.show_service_center
AppV43.show_service_center=_u68_show_service_center_wrapped
AppV43.run_ai_only=_u66_show_ai_reader
AppV43.refresh_telemetry=_u66_refresh_telemetry
_U66_ORIGINAL_INIT_FOR_SENSOR=AppV43.__init__
AppV43.__init__=_u67_init_with_sensor_poll
_u37_gpu_benchmark_child=_u66_scene_child

if __name__ == "__main__" and "--selftest-advanced-modules" in sys.argv:
    try:
        _u66_selftest_advanced()
        raise SystemExit(0)
    except Exception as _u66_exc:
        print("ADVANCED_MODULES_SELFTEST_FAILED:",type(_u66_exc).__name__,str(_u66_exc))
        raise SystemExit(1)
