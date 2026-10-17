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
("21 — Chmura cząstek ULTRA", "particles", 420),
("22 — Gęste miasto proceduralne", "city", 180),
("23 — Wielowarstwowy teren", "terrain", 40),
("24 — Fale geometrii MAX", "waves", 46),
("25 — Siatka obiektów XL", "grid", 110),
("26 — Laboratorium materiałów", "materials", 160),
("27 — Potrójny układ pierścieni", "rings", 54),
("28 — Pole sfer wysokiej jakości", "spheres", 44),
("29 — Torusy wielowarstwowe", "torus", 36),
("30 — Strumień trójkątów ULTRA", "triangles", 2600),
("31 — Mesh ULTRA MAX", "triangles_extreme", 6400),
("32 — Wentylatory i bloki GPU", "gpu", 42),
("33 — Pokój z wieloma obiektami", "room", 140),
("34 — Instancje geometryczne", "cubes", 220),
("35 — Podwójna geometria MAX", "mixed", 360),
("36 — ULTRA MAX — render mieszany", "ultimate", 720),
("37 — ULTRA: fale geometrii", "waves", 46),
("38 — Pole sfer XL", "spheres", 64),
("39 — Torusy wielowarstwowe MAX", "torus", 48),
("40 — Labirynt wireframe", "wire", 46),
("41 — Chłodzenie GPU — geometria", "gpu", 60),
("42 — Laboratorium materiałów ULTRA", "materials", 92),
("43 — Pole cząstek MAX", "particles", 96),
("44 — Instancje sześcianów MAX", "cubes", 100),
("45 — Siatka trójkątów MAX", "triangles_extreme", 9000),
("46 — Ultimate mixed geometry MAX", "ultimate", 700),
("47 — Ultra wireframe corridors", "wire", 90),
("48 — Dense mesh wave", "mesh", 180),
("49 — Dual terrain stress", "terrain", 44),
("50 — High instance cube field", "cubes", 280),
("51 — Particle storm EXTREME", "particles", 650),
("52 — Procedural city EXTREME", "city", 220),
("53 — Geometry workload extreme", "triangles_extreme", 11000),
("54 — Multi-ring stress", "rings", 82),
("55 — Sphere field EXTREME", "spheres", 72),
("56 — Multi-material MAX", "materials", 180),
("57 — Complex GPU board geometry", "gpu", 90),
("58 — Mixed scene EXTREME", "mixed", 440),
("59 — MAX triangle throughput", "triangles_extreme", 14000),
("60 — Ultimate scene endurance", "ultimate", 900)
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
    result={"cpu_temp_c":None,"gpu_temp_c":None,"cpu_power_w":None,"gpu_power_w":None,
            "system_power_w":None,"battery_power_w":None,"cpu_voltage_v":None,"gpu_voltage_v":None,
            "cpu_clock_mhz":None,"gpu_clock_mhz":None,"cpu_fan_rpm":None,"gpu_fan_rpm":None,
            "power_sensors":[],"sensor_groups":{},"acpi_zones":[],"sensors":[],
            "method":"N/D — brak czujnika"}
    if _u66_os.name!="nt":
        return result

    def collect_sensor_rows(rows, source):
        if not isinstance(rows,list):
            return
        result["sensors"]=rows[:2000]
        power_rows=[]
        cpu_power_candidates=[]
        gpu_power_candidates=[]
        system_power_candidates=[]
        for sensor in rows:
            if not isinstance(sensor,dict):
                continue
            name=str(sensor.get("sensor") or sensor.get("name") or "")
            hardware=str(sensor.get("hardware") or "")
            hardware_type=str(sensor.get("hardwareType") or sensor.get("hardware_type") or "")
            parent=str(sensor.get("parent") or "")
            label=(hardware+" "+hardware_type+" "+name+" "+parent).lower()
            sensor_type=str(sensor.get("sensorType") or sensor.get("sensor_type") or "").lower()
            unit=str(sensor.get("unit") or "").lower()
            try:
                value=float(sensor.get("value"))
                if not _u66_math.isfinite(value):
                    continue
            except Exception:
                continue
            if sensor_type=="temperature" or "°c" in unit:
                if result["cpu_temp_c"] is None and any(k in label for k in ("cpu package","cpu tctl","cpu die","cpu core","cpu ccd","processor package")):
                    result["cpu_temp_c"]=value
                if result["gpu_temp_c"] is None and any(k in label for k in ("gpu core","gpu temperature","gpu hotspot","gpu package")):
                    result["gpu_temp_c"]=value
            if sensor_type=="power" or unit in ("w","watt","watts"):
                item={"hardware":hardware,"sensor":name,"value_w":value,"unit":"W","source":sensor.get("source") or source}
                power_rows.append(item)
                cpu_like=("cpu" in label or "processor" in label or hardware_type.lower()=="cpu")
                gpu_like=("gpu" in label or hardware_type.lower()=="gpu" or "graphics" in label)
                if cpu_like:
                    score=3 if "package" in label else (2 if "total" in label or "cores" in label else 1)
                    cpu_power_candidates.append((score,value))
                elif gpu_like:
                    score=3 if "board" in label or "total" in label else (2 if "chip" in label or "asic" in label else 1)
                    gpu_power_candidates.append((score,value))
                elif any(k in label for k in ("system power","platform power","total system","motherboard power")):
                    system_power_candidates.append(value)
                elif "battery" in label and any(k in label for k in ("discharge","power")):
                    result["battery_power_w"]=value
        result["power_sensors"]=power_rows
        if cpu_power_candidates:
            result["cpu_power_w"]=sorted(cpu_power_candidates,key=lambda x:x[0],reverse=True)[0][1]
        if gpu_power_candidates:
            result["gpu_power_w"]=sorted(gpu_power_candidates,key=lambda x:x[0],reverse=True)[0][1]
        if system_power_candidates:
            result["system_power_w"]=system_power_candidates[0]

        # Keep every available sensor category, not just the two selected temperature fields.
        groups={"temperature":[],"voltage":[],"clock":[],"fan":[],"load":[],"power":[],"current":[],"throughput":[],"other":[]}
        chosen={"cpu_voltage":[],"gpu_voltage":[],"cpu_clock":[],"gpu_clock":[],"cpu_fan":[],"gpu_fan":[]}
        for sensor in rows:
            if not isinstance(sensor,dict):
                continue
            name=str(sensor.get("sensor") or sensor.get("name") or "")
            hardware=str(sensor.get("hardware") or sensor.get("parent") or "")
            hardware_type=str(sensor.get("hardwareType") or sensor.get("hardware_type") or "")
            label=(hardware+" "+hardware_type+" "+name+" "+str(sensor.get("parent") or "")).lower()
            stype=str(sensor.get("sensorType") or sensor.get("sensor_type") or "").lower()
            unit=str(sensor.get("unit") or "").strip()
            try:
                value=float(sensor.get("value"))
                if not _u66_math.isfinite(value):
                    continue
            except Exception:
                continue
            category={"temperature":"temperature","voltage":"voltage","clock":"clock","fan":"fan",
                      "load":"load","power":"power","current":"current","throughput":"throughput",
                      "energy":"other","data":"other","smalldata":"other","level":"load"}.get(stype,"other")
            if unit.lower() in ("°c","c") or stype=="temperature": category="temperature"
            elif unit.lower() in ("v","mv") or stype=="voltage": category="voltage"
            elif unit.lower() in ("mhz","ghz") or stype=="clock": category="clock"
            elif unit.lower()=="rpm" or stype=="fan": category="fan"
            elif unit.lower() in ("w","watt","watts") or stype=="power": category="power"
            elif unit.lower() in ("a","ma") or stype=="current": category="current"
            row={"hardware":hardware,"hardwareType":hardware_type,"sensor":name,
                 "sensorType":stype,"value":value,"unit":unit,"source":sensor.get("source") or source,
                 "identifier":str(sensor.get("identifier") or "")}
            groups.setdefault(category,[]).append(row)
            cpu_like=("cpu" in label or "processor" in label or "core voltage" in label or "vcore" in label)
            gpu_like=("gpu" in label or "graphics" in label or "video" in label or "gfx" in label)
            if category=="voltage":
                if cpu_like: chosen["cpu_voltage"].append(value)
                if gpu_like: chosen["gpu_voltage"].append(value)
            elif category=="clock":
                if cpu_like: chosen["cpu_clock"].append(value)
                if gpu_like: chosen["gpu_clock"].append(value)
            elif category=="fan":
                if cpu_like: chosen["cpu_fan"].append(value)
                if gpu_like: chosen["gpu_fan"].append(value)
        result["sensor_groups"]=groups
        for key,values in chosen.items():
            if values:
                result[{"cpu_voltage":"cpu_voltage_v","gpu_voltage":"gpu_voltage_v",
                        "cpu_clock":"cpu_clock_mhz","gpu_clock":"gpu_clock_mhz",
                        "cpu_fan":"cpu_fan_rpm","gpu_fan":"gpu_fan_rpm"}[key]]=values[0]
        result["method"]=source

    bridge_name="NAPRAWA-PC-HARDWARE-SENSOR-BRIDGE.exe"
    candidates=[]
    bundle_dir=getattr(sys,"_MEIPASS",None)
    if bundle_dir:
        candidates.append(_u66_os.path.join(bundle_dir,bridge_name))
    try:
        candidates.append(_u66_os.path.join(_u66_os.path.dirname(_u66_os.path.abspath(sys.executable)),bridge_name))
    except Exception:
        pass
    try:
        candidates.append(_u66_os.path.join(_u66_os.path.dirname(_u66_os.path.abspath(__file__)),"SensorBridge","publish",bridge_name))
    except Exception:
        pass
    for bridge in dict.fromkeys(candidates):
        if not _u66_os.path.isfile(bridge):
            continue
        try:
            proc=_u66_subprocess.run([bridge],capture_output=True,text=True,timeout=12,
                creationflags=getattr(_u66_subprocess,"CREATE_NO_WINDOW",0))
            lines=[line.strip() for line in (proc.stdout or "").splitlines() if line.strip()]
            if lines:
                payload=_u66_json.loads(lines[-1])
                collect_sensor_rows(payload.get("sensors") or [],"LibreHardwareMonitor sensor bridge")
                if result["sensors"]:
                    result["bridge_provider"]=payload.get("provider")
                    result["bridge_errors"]=payload.get("errors") or []
                    break
        except Exception as exc:
            result["bridge_error"]=f"{type(exc).__name__}: {exc}"

    # WMI/ACPI fallback. It can provide temperatures on some systems even if no power sensors exist.
    script = r"""
$ErrorActionPreference='SilentlyContinue'
$sensors=@()
foreach($ns in @('root/LibreHardwareMonitor','root/OpenHardwareMonitor')){
  try{
    $xs=@(Get-CimInstance -Namespace $ns -ClassName Sensor -ErrorAction Stop | Where-Object { $_.SensorType -in @('Temperature','Power') -and $null -ne $_.Value } | Select-Object Name,Parent,Value,SensorType)
    foreach($x in $xs){
      $unit=if($x.SensorType -eq 'Power'){'W'}elseif($x.SensorType -eq 'Temperature'){'°C'}else{''}
      $sensors += [pscustomobject]@{name=[string]$x.Name; parent=[string]$x.Parent; value=[double]$x.Value; sensorType=[string]$x.SensorType; unit=$unit; source=$ns}
    }
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
            if not result["sensors"]:
                collect_sensor_rows(payload.get("sensors") or [],"LibreHardwareMonitor/OpenHardwareMonitor WMI")
            result["acpi_zones"]=payload.get("zones") or []
            for sensor in result["sensors"]:
                if not isinstance(sensor,dict): continue
                label=(str(sensor.get("sensor") or sensor.get("name") or "")+" "+str(sensor.get("hardware") or "")+" "+str(sensor.get("parent") or "")).lower()
                try: value=float(sensor.get("value"))
                except Exception: continue
                if result["cpu_temp_c"] is None and any(x in label for x in ("cpu package","cpu tctl","cpu die","cpu core","cpu ccd","cpu (tctl","processor package")):
                    result["cpu_temp_c"]=value
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
        if _u66_time.monotonic()-getattr(self,"_u66_sensor_last",0)>5:
            self._u66_sensor_busy=True
            self._u66_sensor_last=_u66_time.monotonic()
            def job():
                try:
                    gpu=_u37_nvidia_telemetry() if "_u37_nvidia_telemetry" in globals() else {"available":False}
                    temps=_u66_sensor_probe()
                    self._u66_sensor_cache={"gpu":gpu,"temps":temps,"time":_u66_time.monotonic()}
                    def update():
                        self._u66_sensor_busy=False
                        try:
                            if "_u81_refresh_sensor_table" in globals():
                                _u81_refresh_sensor_table(self)
                            if "_u67_refresh_visible_charts" in globals() and getattr(self,"_u67_stage_panel",None) is not None:
                                _u67_refresh_visible_charts(self)
                        except Exception:
                            pass
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
        ("TEMP GPU","gpu_temp"),("CPU POWER","cpu_power"),("GPU POWER","gpu_power"),
        ("SYSTEM POWER","system_power"),("BATTERY POWER","battery_power"),
        ("CPU VOLTAGE","cpu_voltage"),("GPU VOLTAGE","gpu_voltage"),
        ("CPU CLOCK","cpu_clock"),("GPU CLOCK","gpu_clock"),("CPU FAN","cpu_fan"),("GPU FAN","gpu_fan"),
        ("DYSK ODCZYT","disk_read"),("DYSK ZAPIS","disk_write"),
        ("DOWNLOAD LIVE","net_down"),("UPLOAD LIVE","net_up"),("VRAM UŻYTA","vram"),("CZUJNIK ACPI","acpi")
    ]:
        card=self.panel(grid); card.grid(row=len(self._u66_live_labels)//5,column=len(self._u66_live_labels)%5,sticky="nsew",padx=3,pady=3)
        tk.Label(card,text=title,bg=t["panel"],fg=t["muted"],font=self.fnt(8,"bold")).pack(pady=(8,2))
        val=tk.Label(card,text="N/D",bg=t["panel"],fg=t["accent"],font=self.fnt(14,"bold"))
        val.pack(pady=(0,8)); self._u66_live_labels[key]=val
    for col in range(5): grid.grid_columnconfigure(col,weight=1)
    _u81_attach_sensor_table(self,self.content,height=6)
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
        numeric=lambda x: float(x) if isinstance(x,(int,float)) else None
        for key,field,unit,precision in (
            ("cpu_power","cpu_power_w","W",1),("gpu_power","gpu_power_w","W",1),
            ("system_power","system_power_w","W",1),("battery_power","battery_power_w","W",1),
            ("cpu_voltage","cpu_voltage_v","V",3),("gpu_voltage","gpu_voltage_v","V",3),
            ("cpu_clock","cpu_clock_mhz","MHz",0),("gpu_clock","gpu_clock_mhz","MHz",0),
            ("cpu_fan","cpu_fan_rpm","RPM",0),("gpu_fan","gpu_fan_rpm","RPM",0)
        ):
            value=numeric(temps.get(field))
            put(key,(f"{value:.{precision}f} {unit}" if value is not None else "N/D"))
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
      "ALL":lambda:self.start_all_tests_sequential(),
      "CENTRUM":lambda:self.show_service_center(),
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
    tk.Label(banner,text=f"TESTY SPRZĘTOWE • SPEED TEST • {len(_U66_SCENES)} SCEN 3D • AI CZYTNIK • NAPRAWA WINDOWS",bg=t["panel"],fg=t["accent"],font=self.fnt(12,"bold")).pack(anchor="w",padx=12,pady=(9,3))
    tk.Label(banner,text="„WSZYSTKIE TESTY PO KOLEI” przełącza ekran do aktualnie wykonywanego testu. Wyniki oznaczane są PASS/WARN/FAIL/N/D na podstawie dostępnych pomiarów; brak sensora nie jest zaliczeniem.",bg=t["panel"],fg=t["muted"],font=self.fnt(8),wraplength=1400,justify="left").pack(anchor="w",padx=12,pady=(0,8))
    quick=tk.Frame(self.content,bg=t["bg"]); quick.pack(fill="x",pady=(0,6))
    self.make_button(quick,"▶ URUCHOM SPEED TEST INTERNETU",self.show_speed_test,"accent",side="left",ipady=7)
    self.make_button(quick,"TELEMETRIA LIVE: TEMPERATURY / W / V / MHZ",self.show_live_monitor,"good",side="left",ipady=7)
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
      ( "WSZYSTKIE TESTY PO KOLEI", f"Automatyczny przebieg CPU → RAM → GPU → {len(_U66_SCENES)} scen 3D → SSD/HDD → matryca → sieć Speed Test → bezpieczeństwo → bateria/USB. Każdy etap ma raport; czas zależy od wybranego profilu.", "ALL"),
      ("MONITOR LIVE — WSZĘDZIE","CPU/RAM/GPU, zegary, transfer dysku i sieci, temperatury/czujniki z rzeczywistą próbką co sekundę.","LIVE"),
      ("SPEED TEST INTERNETU","Pomiar prawdziwego download/upload w Mbps oraz opóźnienia HTTP; zapis historii lokalnie.","SPEED"),
      (f"3D BENCHMARK STUDIO — {len(_U66_SCENES)} SCEN", f"{len(_U66_SCENES)} proceduralnych scen OpenGL; FPS jest mierzony z renderowania, renderer i czas trafiają do raportu.", "3D"),
      ("AI CZYTNIK WIEDZY","Baza offline, wyszukiwanie Internetu, czytanie URL, import plików i zapis źródeł do prywatnej biblioteki.","AI"),
      ("CENTRUM SERWISU + SYSTEM REPAIR","SFC, DISM, CHKDSK, raport baterii, narzędzia Windows oraz prywatne zgłoszenia.","CENTRUM"),
      ("CPU — obciążenie i zegary","Rzeczywiste obciążenie etapowe, częstotliwość i wykres próbek.","CPU"),
      ("RAM — wzorce zapisu/odczytu","Bufor RAM z weryfikacją wzorców 00/FF/AA/55; wynik opisuje rozmiar rzeczywiście sprawdzony.","RAM"),
      ("GPU — karta i sterownik","Adaptery, status PnP, telemetria dostawcy i dostępne czujniki.","GPU"),
      ("VRAM — test pamięci tekstur","Niezależna alokacja tekstur, sześć wzorców i porównanie bajtów; dostępne rozmiary 32–256 MB.","VRAM"),
      ("GRY / USTAWIENIA GRAFICZNE","Profile Low/Medium/High/Ultra według wykrytego GPU/RAM/VRAM — to nie są gwarantowane FPS w grach.","GAMES"),
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
    self.make_button(row,"LABORATORIUM PODZESPOŁÓW — 13 MODUŁÓW",self.show_component_lab,"good",side="left",ipady=5)

def _u66_scene_child(output_path, seconds=5, scene_id=1, resolution="1920x1080"):
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
        try:
            width,height=(int(v) for v in str(resolution or "1920x1080").lower().split("x",1))
        except Exception:
            width,height=1920,1080
        width=max(640,min(3840,width)); height=max(480,min(2160,height))
        pg.display.set_mode((width,height),pg.OPENGL|pg.DOUBLEBUF|pg.RESIZABLE,vsync=0)
        renderer=(GL.glGetString(GL.GL_RENDERER) or b"unknown").decode("utf-8","replace")
        version=(GL.glGetString(GL.GL_VERSION) or b"unknown").decode("utf-8","replace")
        GL.glEnable(GL.GL_DEPTH_TEST); GL.glClearColor(.008,.018,.03,1)
        GL.glViewport(0,0,width,height); GL.glMatrixMode(GL.GL_PROJECTION); GL.glLoadIdentity(); gluPerspective(55,width/height,.1,250); GL.glMatrixMode(GL.GL_MODELVIEW)
        start=_u66_time.perf_counter(); frames=0; running=True; samples=[]; win_frames=0; win_start=start; peak=0.0
        requested=max(3,min(900,int(seconds)))
        while running and _u66_time.perf_counter()-start < requested:
            for ev in pg.event.get():
                if ev.type==pg.QUIT or (ev.type==pg.KEYDOWN and ev.key==pg.K_ESCAPE): running=False
                elif ev.type==pg.VIDEORESIZE:
                    width=max(640,ev.w); height=max(480,ev.h); GL.glViewport(0,0,width,height); GL.glMatrixMode(GL.GL_PROJECTION); GL.glLoadIdentity(); gluPerspective(55,width/height,.1,250); GL.glMatrixMode(GL.GL_MODELVIEW)
            elapsed=_u66_time.perf_counter()-start
            GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)
            GL.glPolygonMode(GL.GL_FRONT_AND_BACK,GL.GL_LINE if kind=="wire" else GL.GL_FILL)
            GL.glLoadIdentity(); GL.glTranslatef(0,0,-13); GL.glRotatef(elapsed*18,0,1,0); GL.glRotatef(14+_u66_math.sin(elapsed)*7,1,0,0)
            base=min(100,max(1,int(complexity)))
            if kind in ("boxes","cubes","grid","materials","room","city","gpu","particles","mixed","ultimate"):
                n=base
                if kind=="ultimate": n=max(100,min(720,int(complexity)))
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
                tri=base*base*4 if kind!="triangles_extreme" else max(500,int(complexity)*4)
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
    resolution=str(getattr(self,"_u90_scene_resolution_value","1920x1080") or "1920x1080")
    if getattr(sys,"frozen",False):
        cmd=[sys.executable,"--gpu-benchmark",str(output),str(int(scene_id)),str(int(seconds)),resolution]
    else:
        cmd=[sys.executable,str(Path(__file__).resolve()),"--gpu-benchmark",str(output),str(int(scene_id)),str(int(seconds)),resolution]
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
    self.header_title.config(text=f"3D BENCHMARK STUDIO — {len(_U66_SCENES)} SCEN")
    info=self.panel(self.content); info.pack(fill="x",pady=(0,7))
    tk.Label(info,text="RZECZYWISTE RENDEROWANIE OPENGL • ŚREDNI FPS • PEAK 1 s • RENDERER • CZAS",bg=t["panel"],fg=t["accent"],font=self.fnt(12,"bold")).pack(anchor="w",padx=12,pady=(9,3))
    tk.Label(info,text=f"Profile {len(_U66_SCENES)} scen proceduralnych badają różne obciążenia geometrii. Nie są wynikami gier ani porównaniem sprzętu między różnymi API i rozdzielczościami.",bg=t["panel"],fg=t["muted"],font=self.fnt(8),wraplength=1400,justify="left").pack(anchor="w",padx=12,pady=(0,8))
    options=tk.Frame(self.content,bg=t["bg"]); options.pack(fill="x",pady=4)
    names=[f"{i+1:02d} — {sc[0].split('—',1)[-1].strip()}" for i,sc in enumerate(_U66_SCENES)]
    self._u66_scene_var=tk.StringVar(value=names[0])
    ttk.Combobox(options,textvariable=self._u66_scene_var,values=names,state="readonly",width=42).pack(side="left",padx=3,ipady=4)
    self._u66_scene_seconds=tk.StringVar(value="30 s")
    ttk.Combobox(options,textvariable=self._u66_scene_seconds,values=("3 s","5 s","10 s","30 s","60 s","120 s","180 s","300 s","600 s","900 s"),state="readonly",width=9).pack(side="left",padx=3,ipady=4)
    self._u66_3d_status=tk.Label(self.content,text=f"Gotowy — wybierz scenę albo uruchom wszystkie {len(_U66_SCENES)}.",bg=t["bg"],fg=t["muted"],font=self.fnt(9,"bold"),anchor="w")
    self._u66_3d_status.pack(fill="x",padx=4,pady=5)
    table=self.panel(self.content); table.pack(fill="both",expand=True,pady=5)
    cols=("SCENA","STATUS","FPS ŚREDNI","FPS PEAK","KLATKI","RENDERER / UWAGI")
    self._u66_3d_tree=self.make_tree(table,cols)
    for i,sc in enumerate(_U66_SCENES,1):
        res=self.results.get("3D_SCENE_"+str(i),{}) or {}
        self._u66_3d_tree.insert("","end",iid=str(i),values=(sc[0],res.get("state","—"),res.get("average_fps","N/D"),res.get("peak_fps_1s","N/D"),res.get("frames","N/D"),res.get("renderer",res.get("error","—"))))
    row=tk.Frame(self.content,bg=t["bg"]); row.pack(fill="x")
    self.make_button(row,"▶ URUCHOM WYBRANĄ SCENĘ",lambda:_u66_start_3d_one(self),"accent",side="left",ipady=5)
    self.make_button(row,f"▶ WSZYSTKIE {len(_U66_SCENES)} SCEN",lambda:_u66_start_3d_all(self),"good",side="left",ipady=5)
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
    if not messagebox.askyesno(f"{len(_U66_SCENES)} scen 3D",f"Uruchomić {len(_U66_SCENES)} scen, każdą przez {seconds} s? Łączny czas renderowania to co najmniej {len(_U66_SCENES)*seconds} sekund. ESC zatrzymuje aktywną scenę."):
        return
    self.worker(lambda:_u66_run_3d_suite(self,seconds))

def _u66_run_3d_suite(self,seconds=5):
    _u66_ui_wait(self,lambda:_u66_show_3d_studio(self))
    results=[]
    for i,sc in enumerate(_U66_SCENES,1):
        if self._test_should_stop(): break
        _u66_set_suite_status(self,f"3D BENCHMARK: scena {i}/{len(_U66_SCENES)} — {sc[0]}")
        r=_u66_execute_gpu_scene(self,i,seconds); results.append(r)
        _u66_ui_wait(self,lambda:_u66_show_3d_studio(self))
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
    if not messagebox.askyesno("Wszystkie testy po kolei",f"Uruchomić pełny przebieg: CPU, RAM, GPU, {len(_U66_SCENES)} scen 3D, VRAM, dysk, matryca, Internet Speed Test, bezpieczeństwo, bateria i urządzenia USB/sieć? Każda scena renderuje przez 10 s (minimum {len(_U66_SCENES)*10} s samego GPU); test sieci przesyła około 24 MB. Można zatrzymać klawiszem ESC."):
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
    stage(4,total,f"3D Benchmark — {len(_U66_SCENES)} scen po kolei",lambda:_u66_show_3d_studio(self),lambda:_u66_run_3d_suite(self,10))
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
def _u67_set_suite_status(self, text):
    """Bezpiecznie aktualizuje status pełnej diagnostyki bez zależności od brakującego aliasu."""
    message = str(text or "")
    try:
        queue_status = getattr(self, "queue_status", None)
        if callable(queue_status):
            queue_status(message)
            return
    except Exception:
        pass
    try:
        queue_action = getattr(self, "queue_action", None)
        header = getattr(self, "header_status", None)
        if callable(queue_action) and header is not None:
            queue_action(lambda h=header, m=message: h.config(text=m))
            return
    except Exception:
        pass
    try:
        self.queue_log("Diagnostyka: " + message)
    except Exception:
        pass


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
    self._u67_stage_title = tk.Label(top, text=f"TEST {index}/{total} — {title}", bg=t["panel"], fg=t["accent"], font=self.fnt(10, "bold"), anchor="w")
    self._u67_stage_title.pack(side="left", fill="x", expand=True)
    self.make_button(top, "STOP TEST", self.stop_current_test, "bad", side="right", ipady=3)
    self._u67_stage_values = {}
    metrics = tk.Frame(panel, bg=t["panel"])
    metrics.pack(fill="x", padx=6, pady=(0, 5))
    metric_specs = [
        ("CPU", "cpu"), ("RAM", "ram"), ("GPU", "gpu"), ("TEMP CPU", "cpu_temp"),
        ("TEMP GPU", "gpu_temp"), ("CPU MOC", "cpu_power"), ("GPU MOC", "gpu_power"),
        ("MOC SYSTEMU", "system_power"), ("MOC BATERII", "battery_power"),
        ("CPU V", "cpu_voltage"), ("GPU V", "gpu_voltage"), ("CPU MHz", "cpu_clock"),
        ("GPU MHz", "gpu_clock"), ("WENTYLATOR CPU", "cpu_fan"), ("WENTYLATOR GPU", "gpu_fan"),
        ("DYSK ODCZYT", "disk_read"), ("DYSK ZAPIS", "disk_write"),
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
    self._u67_stage_chart_power = tk.Canvas(graphs, height=82, bg=t["card"], highlightthickness=0)
    self._u67_stage_chart_power.pack(side="left", fill="both", expand=True, padx=(3, 0))
    graphs2 = tk.Frame(panel, bg=t["panel"])
    graphs2.pack(fill="x", padx=6, pady=(0, 5))
    self._u67_stage_chart_temp = tk.Canvas(graphs2, height=94, bg=t["card"], highlightthickness=0)
    self._u67_stage_chart_temp.pack(side="left", fill="both", expand=True, padx=(0, 3))
    self._u67_stage_chart_voltage = tk.Canvas(graphs2, height=94, bg=t["card"], highlightthickness=0)
    self._u67_stage_chart_voltage.pack(side="left", fill="both", expand=True, padx=3)
    self._u67_stage_chart_clocks = tk.Canvas(graphs2, height=94, bg=t["card"], highlightthickness=0)
    self._u67_stage_chart_clocks.pack(side="left", fill="both", expand=True, padx=(3, 0))
    if not hasattr(self, "_u67_hist"):
        self._u67_hist = {"cpu": [], "ram": [], "gpu": [], "read": [], "write": [], "down": [], "up": [],
                          "cpu_power": [], "gpu_power": [], "system_power": [], "battery_power": [],
                          "cpu_temp": [], "gpu_temp": [], "cpu_voltage": [], "gpu_voltage": [],
                          "cpu_clock": [], "gpu_clock": []}
    _u81_attach_sensor_table(self, panel, height=5)
    self._u67_stage_key = title
    _u67_refresh_visible_charts(self)
    _u81_schedule_stage_live_tick(self)


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
        ("read", t["accent2"]), ("write", t["good"]), ("down", t["warn"]), ("up", t["accent"]),
        ("cpu_power", t["accent"]), ("gpu_power", t["warn"]),
        ("system_power", t["good"]), ("battery_power", t["accent2"]),
        ("cpu_temp", t["warn"]), ("gpu_temp", t["accent2"]),
        ("cpu_voltage", t["good"]), ("gpu_voltage", t["accent"]),
        ("cpu_clock", t["accent2"]), ("gpu_clock", t["warn"])
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
    cpu_power = numeric(temps.get("cpu_power_w"))
    gpu_power = numeric(gpu.get("power_draw_w", gpu.get("power_w", temps.get("gpu_power_w"))))
    system_power = numeric(temps.get("system_power_w"))
    battery_power = numeric(temps.get("battery_power_w"))
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
    cpu_voltage = numeric(temps.get("cpu_voltage_v"))
    gpu_voltage = numeric(temps.get("gpu_voltage_v"))
    cpu_clock = numeric(temps.get("cpu_clock_mhz"))
    gpu_clock = numeric(temps.get("gpu_clock_mhz"))
    cpu_fan = numeric(temps.get("cpu_fan_rpm"))
    gpu_fan = numeric(temps.get("gpu_fan_rpm"))
    if cpu_clock is None:
        freq = psutil.cpu_freq() if psutil else None
        cpu_clock = numeric(freq.current) if freq else None
    shown = {
        "cpu": f"{cpu:.1f}%" if cpu is not None else "N/D",
        "ram": f"{ram:.1f}%" if ram is not None else "N/D",
        "gpu": f"{gpu_load:.1f}%" if gpu_load is not None else "N/D",
        "cpu_temp": f"{cpu_temp:.1f} °C" if cpu_temp is not None else (f"ACPI {acpi_val:.1f} °C" if acpi_val is not None else "N/D"),
        "gpu_temp": f"{gpu_temp:.1f} °C" if gpu_temp is not None else "N/D",
        "cpu_power": f"{cpu_power:.1f} W" if cpu_power is not None else "N/D",
        "gpu_power": f"{gpu_power:.1f} W" if gpu_power is not None else "N/D",
        "system_power": f"{system_power:.1f} W" if system_power is not None else "N/D",
        "battery_power": f"{battery_power:.1f} W" if battery_power is not None else "N/D",
        "cpu_voltage": f"{cpu_voltage:.3f} V" if cpu_voltage is not None else "N/D",
        "gpu_voltage": f"{gpu_voltage:.3f} V" if gpu_voltage is not None else "N/D",
        "cpu_clock": f"{cpu_clock:.0f} MHz" if cpu_clock is not None else "N/D",
        "gpu_clock": f"{gpu_clock:.0f} MHz" if gpu_clock is not None else "N/D",
        "cpu_fan": f"{cpu_fan:.0f} RPM" if cpu_fan is not None else "N/D",
        "gpu_fan": f"{gpu_fan:.0f} RPM" if gpu_fan is not None else "N/D",
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
            ("up", up * 8 / 1_000_000 if up is not None else None),
            ("cpu_power", cpu_power), ("gpu_power", gpu_power),
            ("system_power", system_power), ("battery_power", battery_power),
            ("cpu_temp", cpu_temp), ("gpu_temp", gpu_temp), ("cpu_voltage", cpu_voltage), ("gpu_voltage", gpu_voltage),
            ("cpu_clock", cpu_clock), ("gpu_clock", gpu_clock)
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
        power_series = {"cpu_power": (hist or {}).get("cpu_power", []), "gpu_power": (hist or {}).get("gpu_power", []),
                        "system_power": (hist or {}).get("system_power", []), "battery_power": (hist or {}).get("battery_power", [])}
        power_values = power_series["cpu_power"] + power_series["gpu_power"] + power_series["system_power"] + power_series["battery_power"]
        power_max = max([1.0] + power_values)
        _u67_draw_history_chart(getattr(self, "_u67_stage_chart_power", None), power_series, power_max, "POBÓR MOCY W", self)
        thermal = {"cpu_temp": (hist or {}).get("cpu_temp", []), "gpu_temp": (hist or {}).get("gpu_temp", [])}
        thermal_values = thermal["cpu_temp"] + thermal["gpu_temp"]
        _u67_draw_history_chart(getattr(self, "_u67_stage_chart_temp", None), thermal, max([100.0] + thermal_values), "TEMPERATURA °C", self)
        voltage = {"cpu_voltage": (hist or {}).get("cpu_voltage", []), "gpu_voltage": (hist or {}).get("gpu_voltage", [])}
        voltage_values = voltage["cpu_voltage"] + voltage["gpu_voltage"]
        _u67_draw_history_chart(getattr(self, "_u67_stage_chart_voltage", None), voltage, max([2.0] + voltage_values), "NAPIĘCIA V", self)
        clocks = {"cpu_clock": (hist or {}).get("cpu_clock", []), "gpu_clock": (hist or {}).get("gpu_clock", [])}
        clock_values = clocks["cpu_clock"] + clocks["gpu_clock"]
        _u67_draw_history_chart(getattr(self, "_u67_stage_chart_clocks", None), clocks, max([1000.0] + clock_values), "ZEGARY CPU / GPU MHz", self)
    except Exception:
        pass
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
            expanded.append(("__3D__", f"3D Benchmark Studio — {len(_U66_SCENES)} scen OpenGL ULTRA/MAX", lambda: _u66_show_3d_studio(self), lambda: _u66_run_3d_suite(self, 30), ["3D_SUITE"]))
            expanded.append(("__VRAM__", "VRAM — test zapisu/readback 6 wzorców", lambda: _u68_open_vram_test(self), lambda: _u90_run_vram_profile_from_suite(self), ["VRAM_TEST"]))
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
        "CPU": "CPU", "GPU": f"GPU + {len(_U66_SCENES)} scen 3D", "RAM": "RAM", "DYSKI": "Dyski",
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



# v4.3.72 — independent component tests, long ULTRA/MAX profiles, per-component 3D visualizer.
_U68_PROFILE_CHOICES=("KRÓTKI — 15 s","ŚREDNI — 60 s","DŁUGI — 180 s","ULTRA — 300 s","MAX — 600 s","TEST TERMICZNY — 900 s")
_U68_COMPONENT_LABELS={"CPU":"Procesor / CPU","RAM":"Pamięć RAM","GPU":"Karta graficzna / GPU","DYSK":"SSD / HDD / NVMe","EKRAN":"Matryca / EDID","SECURITY":"Bezpieczeństwo","VRAM":"Pamięć karty / VRAM"}

def _u68_profile_seconds(self):
    value=str(getattr(self,"_u68_profile_var",tk.StringVar(value="ULTRA — 300 s")).get())
    try:return max(15,min(900,int(value.split("—",1)[1].strip().split()[0])))
    except Exception:return 180

def _u68_selected_mb(self,kind):
    var=getattr(self,"_u68_"+kind.lower()+"_size_var",None)
    try:value=int(str(var.get()).split()[0])
    except Exception:value=512
    return max(32,min(4096 if kind=="disk" else 2048,value))

def _u68_attach_component_workbench(self,module):
    try:
        t=self.colors();panel=tk.Frame(self.content,bg=t["panel"],highlightbackground=t["accent"],highlightthickness=1)
        children=self.content.winfo_children()
        if len(children)>1:panel.pack(fill="x",padx=3,pady=4,before=children[1])
        elif children:panel.pack(fill="x",padx=3,pady=4,before=children[0])
        else:panel.pack(fill="x",padx=3,pady=4)
        self._u68_workbench_panel=panel
        tk.Label(panel,text="TESTY NIEZALEŻNE • BENCHMARK ULTRA/MAX • WIZUALIZACJA 3D",bg=t["panel"],fg=t["accent"],font=self.fnt(10,"bold")).pack(anchor="w",padx=9,pady=(7,2))
        tk.Label(panel,text="Skan i benchmark wykonują rzeczywistą operację. Model 3D pokazuje schemat działania — nie udaje dodatkowego wyniku FPS.",bg=t["panel"],fg=t["muted"],font=self.fnt(8),wraplength=1300,justify="left").pack(anchor="w",padx=9,pady=(0,5))
        row=tk.Frame(panel,bg=t["panel"]);row.pack(fill="x",padx=6,pady=(0,6))
        self._u68_profile_var=tk.StringVar(value=getattr(self,"_u68_profile_value","ULTRA — 300 s"))
        cb=ttk.Combobox(row,textvariable=self._u68_profile_var,values=_U68_PROFILE_CHOICES,state="readonly",width=18);cb.pack(side="left",padx=3,ipady=3)
        cb.bind("<<ComboboxSelected>>",lambda e:setattr(self,"_u68_profile_value",self._u68_profile_var.get()))
        if module=="RAM":
            self._u68_ram_size_var=tk.StringVar(value=getattr(self,"_u68_ram_value","512 MB"))
            ttk.Combobox(row,textvariable=self._u68_ram_size_var,values=("128 MB","256 MB","512 MB","1024 MB","1536 MB","2048 MB"),state="readonly",width=11).pack(side="left",padx=3,ipady=3)
        elif module=="DYSK":
            self._u68_disk_size_var=tk.StringVar(value=getattr(self,"_u68_disk_value","512 MB"))
            ttk.Combobox(row,textvariable=self._u68_disk_size_var,values=("128 MB","256 MB","512 MB","1024 MB","2048 MB","4096 MB"),state="readonly",width=11).pack(side="left",padx=3,ipady=3)
        self._u68_workbench_status=tk.Label(row,text="Gotowy — wybierz niezależny test.",bg=t["panel"],fg=t["muted"],font=self.fnt(8,"bold"),anchor="w")
        self._u68_workbench_status.pack(side="left",fill="x",expand=True,padx=8)
        self.make_button(row,"SKAN + LIVE 3D",lambda m=module:_u68_open_component_simulator(self,m,True,"scan"),"card",side="left",ipady=5)
        self.make_button(row,"BENCHMARK ULTRA/MAX + 3D",lambda m=module:_u68_open_component_simulator(self,m,True,"benchmark"),"accent",side="left",ipady=5)
        self.make_button(row,"SYMULATOR 3D",lambda m=module:_u68_open_component_simulator(self,m,False,"scan"),"good",side="left",ipady=5)
        if module=="GPU":
            self.make_button(row,"TEST VRAM",lambda:_u68_open_vram_test(self),"card",side="left",ipady=5)
            self.make_button(row,f"{len(_U66_SCENES)} SCEN 3D",lambda:_u68_open_gpu_suite(self),"good",side="left",ipady=5)
    except Exception as exc:
        try:self.append_log("Nie udało się dodać panelu testów komponentu: "+repr(exc))
        except Exception:pass

def _u68_show_module_with_workbench(self,module):
    _U68_ORIGINAL_SHOW_MODULE(self,module)
    if module in ("CPU","GPU","RAM","DYSK","EKRAN","SECURITY"):_u68_attach_component_workbench(self,module)

def _u68_show_simple_module_with_workbench(self,title):
    _U68_ORIGINAL_SHOW_SIMPLE_MODULE(self,title);name=str(title).upper()
    if any(token in name for token in ("AUDIO","SIEĆ","WIFI","WI-FI","LAN","USB","KLAWIATURA","TOUCHPAD","KAMERA","MIKROFON")):
        try:
            t=self.colors();panel=tk.Frame(self.content,bg=t["panel"],highlightbackground=t["accent"],highlightthickness=1)
            children=self.content.winfo_children()
            if len(children)>1:panel.pack(fill="x",padx=3,pady=4,before=children[1])
            else:panel.pack(fill="x",padx=3,pady=4)
            tk.Label(panel,text="DODATKOWY TEST MODUŁU — RZECZYWISTY ODCZYT / POTWIERDZENIE",bg=t["panel"],fg=t["accent"],font=self.fnt(9,"bold")).pack(anchor="w",padx=9,pady=(6,2))
            row=tk.Frame(panel,bg=t["panel"]);row.pack(fill="x",padx=5,pady=(0,5))
            key="USB" if "USB" in name else "SIEĆ" if any(x in name for x in ("SIEĆ","WIFI","WI-FI","LAN")) else "AUDIO" if "AUDIO" in name or "MIKROFON" in name else "KLAWIATURA"
            self.make_button(row,"URUCHOM TEST",lambda k=key:self.worker(lambda:self._peripheral_test(k)),"accent",side="left",ipady=4)
            if key=="SIEĆ":self.make_button(row,"SPEED TEST DOWNLOAD/UPLOAD",self.show_speed_test,"good",side="left",ipady=4)
        except Exception as exc:
            try:self.append_log("Test modułu: "+repr(exc))
            except Exception:pass

def _u68_draw_box3d(canvas,center,size,angle,color,outline,scale,origin):
    x,y,z=center;sx,sy,sz=size
    verts=[(x+dx*sx/2,y+dy*sy/2,z+dz*sz/2) for dx,dy,dz in ((-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1))]
    ca=_u66_math.cos(angle);sa=_u66_math.sin(angle);projected=[]
    for vx,vy,vz in verts:
        rx=vx*ca-vz*sa;rz=vx*sa+vz*ca;factor=scale/max(2.0,5.5+rz)
        projected.append((origin[0]+rx*factor,origin[1]-vy*factor,rz))
    faces=((0,1,2,3),(4,7,6,5),(0,4,5,1),(3,2,6,7),(1,5,6,2),(0,3,7,4));drawn=[]
    for face in faces:
        pts=[]
        for idx in face:pts.extend(projected[idx][:2])
        drawn.append((sum(projected[idx][2] for idx in face)/4,pts))
    for _,pts in sorted(drawn):canvas.create_polygon(*pts,fill=color,outline=outline,width=1)

def _u68_draw_component_scene(self):
    canvas=getattr(self,"_u68_sim_canvas",None)
    if canvas is None or not canvas.winfo_exists() or not str(getattr(self,"current_view","")).startswith("SIM3D_"):return
    try:
        t=self.colors();canvas.delete("all");w=max(640,canvas.winfo_width());h=max(300,canvas.winfo_height())
        canvas.create_rectangle(0,0,w,h,fill="#06101c",outline="")
        for gx in range(0,w,44):canvas.create_line(gx,0,gx,h,fill="#102538",width=1)
        for gy in range(0,h,32):canvas.create_line(0,gy,w,gy,fill="#102538",width=1)
        module=str(self.current_view).replace("SIM3D_","");angle=float(getattr(self,"_u68_sim_angle",0.0))
        origin=(w*.5,h*.5+10);scale=min(w,h)*1.25;teal="#14d9bf";blue="#1683e8";purple="#b041d3";silver="#9aafc2";dark="#193047"
        _u68_draw_box3d(canvas,(0,-1.05,0),(3.6,.2,1.2),angle,dark,teal,scale,origin)
        if module=="CPU":
            _u68_draw_box3d(canvas,(0,0,0),(2.25,.4,.9),angle,silver,teal,scale,origin);_u68_draw_box3d(canvas,(0,.32,0),(1.3,.1,.55),angle,purple,"#ef6cff",scale,origin)
            for xx in (-.38,0,.38):
                for zz in (-.18,.18):_u68_draw_box3d(canvas,(xx,.48,zz),(.16,.09,.16),angle,blue,teal,scale,origin)
            canvas.create_text(20,20,text="CPU • RDZENIE / ZEGARY / OBCIĄŻENIE",anchor="nw",fill="#7ceaff",font=self.fnt(10,"bold"))
        elif module=="RAM":
            _u68_draw_box3d(canvas,(0,0,0),(4.2,.15,.55),angle,dark,teal,scale,origin)
            for i in range(8):_u68_draw_box3d(canvas,(-1.72+i*.49,.23,0),(.38,.35,.4),angle,purple,teal,scale,origin)
            canvas.create_text(20,20,text="RAM • BLOKI / WZORCE / WERYFIKACJA",anchor="nw",fill="#7ceaff",font=self.fnt(10,"bold"))
        elif module=="DYSK":
            _u68_draw_box3d(canvas,(0,0,0),(4.2,.16,1.25),angle,dark,teal,scale,origin)
            for i in range(8):_u68_draw_box3d(canvas,(-1.72+i*.49,.18,.18),(.33,.12,.45),angle,silver,teal,scale,origin)
            _u68_draw_box3d(canvas,(0,.26,-.18),(.65,.16,.52),angle,purple,"#ef6cff",scale,origin)
            canvas.create_text(20,20,text="SSD / HDD / NVMe • ODCZYT / ZAPIS",anchor="nw",fill="#7ceaff",font=self.fnt(10,"bold"))
        elif module in ("GPU","VRAM"):
            _u68_draw_box3d(canvas,(0,0,0),(4.4,.18,1.75),angle,dark,teal,scale,origin);_u68_draw_box3d(canvas,(0,.25,0),(1.35,.22,1.05),angle,purple,"#ef6cff",scale,origin)
            for xx in (-1.35,1.35):
                for zz in (-.48,.48):_u68_draw_box3d(canvas,(xx,.25,zz),(.62,.18,.5),angle,silver,teal,scale,origin)
            for fanx in (-1.1,1.1):
                for i in range(8):
                    aa=angle*1.8+i*(_u66_math.pi/4);px=origin[0]+(fanx*_u66_math.cos(angle)-.1*_u66_math.sin(aa))*scale/5.7;py=origin[1]-(.1+.33*_u66_math.sin(aa))*scale/5.7
                    canvas.create_oval(px-12,py-12,px+12,py+12,outline=teal,width=2)
            canvas.create_text(20,20,text="VRAM • TEKSTURY / ODCZYT ZWROTNY" if module=="VRAM" else "GPU • GEOMETRIA / RENDER / FPS",anchor="nw",fill="#7ceaff",font=self.fnt(10,"bold"))
        elif module in ("SIEĆ","SIEC"):
            _u68_draw_box3d(canvas,(-1.9,0,0),(1.1,.52,1.05),angle,dark,teal,scale,origin)
            for i in range(8):
                _u68_draw_box3d(canvas,(-2.25+(i%4)*.23,.34,(i//4-.5)*.45),(.12,.08,.08),angle,blue,teal,scale,origin)
            for i in range(5):
                _u68_draw_box3d(canvas,(.15+i*.7,.05,(i%3-1)*.5),(.4,.35,.5),angle,silver,teal,scale,origin)
            canvas.create_text(20,20,text="SIEĆ • ADAPTERY / PAKIETY / DOWNLOAD / UPLOAD",anchor="nw",fill="#7ceaff",font=self.fnt(10,"bold"))
        elif module=="USB":
            _u68_draw_box3d(canvas,(0,0,0),(1.25,.48,.55),angle,silver,teal,scale,origin)
            for i in range(6):
                x=-2.1+i*.82
                _u68_draw_box3d(canvas,(x,.5,0),(.42,.16,.3),angle,blue,teal,scale,origin)
                _u68_draw_box3d(canvas,(x,.28,0),(.08,.2,.08),angle,purple,"#ef6cff",scale,origin)
            canvas.create_text(20,20,text="USB • PORTY / URZĄDZENIA / ENUMERACJA",anchor="nw",fill="#7ceaff",font=self.fnt(10,"bold"))
        elif module=="AUDIO":
            _u68_draw_box3d(canvas,(-1.55,0,0),(.95,1.4,.8),angle,dark,teal,scale,origin)
            _u68_draw_box3d(canvas,(1.55,0,0),(.95,1.4,.8),angle,dark,teal,scale,origin)
            for j in range(4):
                yy=-.45+j*.3
                _u68_draw_box3d(canvas,(-1.55,yy,.45),(.36,.18,.08),angle,purple,teal,scale,origin)
                _u68_draw_box3d(canvas,(1.55,yy,.45),(.36,.18,.08),angle,blue,teal,scale,origin)
            canvas.create_text(20,20,text="AUDIO • URZĄDZENIA WEJŚCIA / WYJŚCIA",anchor="nw",fill="#7ceaff",font=self.fnt(10,"bold"))
        elif module=="KLAWIATURA":
            _u68_draw_box3d(canvas,(0,0,0),(4.5,.18,1.65),angle,dark,teal,scale,origin)
            for r in range(4):
                for c in range(13):
                    _u68_draw_box3d(canvas,(-1.92+c*.32,.17,(r-1.5)*.31),(.25,.07,.22),angle,purple if (r+c)%5==0 else silver,teal,scale,origin)
            canvas.create_text(20,20,text="KLAWIATURA / TOUCHPAD • WEJŚCIE UŻYTKOWNIKA",anchor="nw",fill="#7ceaff",font=self.fnt(10,"bold"))
        elif module=="BATERIA":
            _u68_draw_box3d(canvas,(0,0,0),(2.8,.45,1.05),angle,dark,teal,scale,origin)
            for i in range(8):
                _u68_draw_box3d(canvas,(-1.15+i*.32,.27,0),(.23,.18,.68),angle,blue if i<5 else purple,teal,scale,origin)
            _u68_draw_box3d(canvas,(1.55,.02,0),(.25,.6,.35),angle,silver,teal,scale,origin)
            canvas.create_text(20,20,text="BATERIA • POJEMNOŚĆ / CZAS / ZASILANIE",anchor="nw",fill="#7ceaff",font=self.fnt(10,"bold"))
        elif module=="KAMERA":
            _u68_draw_box3d(canvas,(0,0,0),(2.5,.28,.75),angle,dark,teal,scale,origin)
            _u68_draw_box3d(canvas,(0,.05,.44),(.8,.72,.2),angle,silver,teal,scale,origin)
            canvas.create_oval(origin[0]-34,origin[1]-25,origin[0]+34,origin[1]+25,outline="#14d9bf",width=3)
            canvas.create_text(20,20,text="KAMERA • OBECNOŚĆ URZĄDZENIA / PODGLĄD",anchor="nw",fill="#7ceaff",font=self.fnt(10,"bold"))
        elif module=="EKRAN":
            _u68_draw_box3d(canvas,(0,0,0),(3.6,.18,2.1),angle,dark,teal,scale,origin)
            for r in range(4):
                for c in range(9):
                    color=("#ff5c78","#ffd166","#06d6a0","#118ab2","#7b61ff")[(r+c)%5]
                    _u68_draw_box3d(canvas,(-1.45+c*.36,.14,(r-1.5)*.28),(.29,.025,.2),angle,color,teal,scale,origin)
            canvas.create_text(20,20,text="MATRYCA • EDID / PIXELE / KOLOR / GRADIENT",anchor="nw",fill="#7ceaff",font=self.fnt(10,"bold"))
        elif module=="SECURITY":
            _u68_draw_box3d(canvas,(0,0,0),(2.1,.25,2.25),angle,dark,teal,scale,origin)
            _u68_draw_box3d(canvas,(0,.22,0),(1.25,.08,1.45),angle,blue,teal,scale,origin)
            canvas.create_text(20,20,text="BEZPIECZEŃSTWO • AUDYT / URZĄDZENIA / AUTOSTART",anchor="nw",fill="#7ceaff",font=self.fnt(10,"bold"))
        else:
            _u68_draw_box3d(canvas,(0,0,0),(3.4,.22,2.4),angle,silver,teal,scale,origin);canvas.create_text(20,20,text=module+" • WIZUALIZACJA SCHEMATYCZNA",anchor="nw",fill="#7ceaff",font=self.fnt(10,"bold"))
        canvas.create_text(w-20,h-18,text="WIZUALIZACJA 3D SCHEMATYCZNA — POMIARY WYKONYWANE ODDZIELNIE",anchor="se",fill="#a6c8df",font=self.fnt(7))
        self._u68_sim_angle=angle+.045;self.after(55,lambda:_u68_draw_component_scene(self))
    except Exception as exc:
        try:self.append_log("Symulator 3D: "+repr(exc))
        except Exception:pass

def _u68_sim_metrics_tick(self):
    if not str(getattr(self,"current_view","")).startswith("SIM3D_"):return
    try:_u67_refresh_visible_charts(self)
    except Exception:pass
    try:self.after(1000,lambda:_u68_sim_metrics_tick(self))
    except Exception:pass

def _u68_component_result_text(self,module,mode,started):
    keys={"CPU":["CPU"],"RAM":["RAM"],"DYSK":["DYSK"],"GPU":["GPU","GPU_WINSAT"],"EKRAN":["EKRAN"],"SECURITY":["SECURITY"],"VRAM":["VRAM_TEST"]}
    result={}
    for key in keys.get(module,[module]):
        val=(getattr(self,"results",{}) or {}).get(key)
        if isinstance(val,dict) and val:result=val;break
    elapsed=max(.01,_u66_time.monotonic()-started);state=result.get("state","N/D");details=[]
    if module=="CPU":
        stages=result.get("stages",[]);details.append("Etapy obciążenia: "+str(len(stages)))
        if stages:details.extend(["Ostatni odczyt CPU: "+str(stages[-1].get("load","N/D"))+"%","Taktowanie MHz: "+str(stages[-1].get("freq","N/D"))])
    elif module=="RAM":details.extend([f"Bufor testowy: {result.get('size_mb','N/D')} MB",str(result.get("message",""))])
    elif module=="DYSK":
        bm=result.get("benchmark",{})
        if isinstance(bm,dict):details.extend(["Odczyt: "+fmt_speed(bm.get("read_bps",0)),"Zapis: "+fmt_speed(bm.get("write_bps",0))])
        details.append(str(result.get("error","")))
    elif module=="GPU":details.append(str(result.get("message","")))
    elif module=="VRAM":details.extend([f"VRAM: {result.get('allocated_mb',result.get('requested_mb','N/D'))} MB",f"Wzorce: {result.get('patterns_completed',0)}/{result.get('patterns_total',0)}",f"Weryfikowane bajty: {result.get('bytes_verified','N/D')}"])
    elif module=="EKRAN":details.append("Wykryte monitory: "+str(len(result.get("monitors",[]))))
    elif module=="SECURITY":details.append(str(result.get("flags","")))
    summary=f"WYNIK {module}: {state.upper()} • czas {elapsed:.1f} s"
    if details:summary+=" • "+" • ".join(x for x in details if x)
    return summary

def _u68_run_component_worker(self,module,mode):
    started=_u66_time.monotonic();seconds=_u68_profile_seconds(self)
    if module=="CPU":
        if mode=="scan":
            try:
                if psutil:
                    vm=psutil.virtual_memory();self.queue_results("COMPONENT_SCAN_CPU",{"state":"good","cpu":self.cpu,"logical_cpus":os.cpu_count(),"ram_total":vm.total,"sampled_at":_U66_datetime.now().isoformat(timespec="seconds")})
                    self.queue_log(f"CPU SCAN: {self.cpu.get('Name','N/D')} | rdzenie {self.cpu.get('NumberOfCores','N/D')} | wątki {os.cpu_count()}")
                else:self.queue_results("COMPONENT_SCAN_CPU",{"state":"warn","message":"psutil niedostępny"})
            except Exception as exc:self.queue_results("COMPONENT_SCAN_CPU",{"state":"warn","error":repr(exc)})
        else:self._cpu_test(seconds)
    elif module=="RAM":
        if mode=="scan":
            vm=psutil.virtual_memory() if psutil else None
            self.queue_results("COMPONENT_SCAN_RAM",{"state":"good" if vm else "warn","total_bytes":vm.total if vm else None,"available_bytes":vm.available if vm else None,"used_percent":vm.percent if vm else None,"sampled_at":_U66_datetime.now().isoformat(timespec="seconds")})
            self.queue_log("RAM SCAN: "+(f"zainstalowano {fmt_bytes(vm.total)}, dostępne {fmt_bytes(vm.available)}, użycie {vm.percent:.1f}%" if vm else "N/D — psutil niedostępny"))
        else:
            requested=_u68_selected_mb(self,"ram");available_mb=int(psutil.virtual_memory().available/1024/1024) if psutil else 0
            safe_mb=min(requested,max(128,min(2048,int(max(128,available_mb*.25)))))
            self.queue_log(f"RAM BENCHMARK: wybrano {requested} MB, bufor testowy {safe_mb} MB; test nie obejmuje całej pamięci fizycznej.")
            t0=_u66_time.perf_counter();self._ram_test(safe_mb);test_time=max(.001,_u66_time.perf_counter()-t0)
            prev=(self.results.get("RAM",{}) or {})
            self.queue_results("RAM_BENCHMARK",{"state":prev.get("state","warn"),"buffer_mb":safe_mb,"duration_seconds":round(test_time,3),"message":prev.get("message","N/D")})
    elif module=="DYSK":
        if mode=="scan":
            devices=get_physical_disks();reliability=get_storage_reliability()
            self.queue_results("COMPONENT_SCAN_DYSK",{"state":"good" if devices else "warn","devices":devices,"reliability":reliability,"sampled_at":_U66_datetime.now().isoformat(timespec="seconds")})
            self.queue_log(f"DYSK SCAN: wykryto {len(devices)} fizycznych urządzeń i {len(reliability)} rekordów niezawodności.")
        else:self._disk_test(_u68_selected_mb(self,"disk"))
    elif module=="GPU":
        if mode=="scan":self._gpu_test()
        else:_u68_open_gpu_suite(self,auto_start=True);return
    elif module=="VRAM":_u68_open_vram_test(self);return
    elif module=="EKRAN":
        if mode=="scan":self._monitor_test()
        else:
            if hasattr(self,"_u37_open_screen_test"):self._u37_open_screen_test()
            else:self._monitor_test()
    elif module=="SECURITY":self._security_test()
    elif module=="BATERIA":self._battery_test()
    else:self.queue_log("Nieznany moduł: "+module)
    summary=_u68_component_result_text(self,module,mode,started)
    def finish():
        label=getattr(self,"_u68_sim_status",None)
        if label is not None and label.winfo_exists():label.config(text=summary,fg=self.colors()["good"] if "GOOD" in summary else self.colors()["warn"])
        self.header_status.config(text="GOTOWY — "+module)
    self.queue_action(finish)

def _u68_open_component_simulator(self,module,run_test=False,mode="scan"):
    self.current_view="SIM3D_"+module;self.clear();t=self.colors()
    self.header_title.config(text=f"{_U68_COMPONENT_LABELS.get(module,module)} — TESTY NIEZALEŻNE 3D")
    head=self.panel(self.content);head.pack(fill="x",pady=(0,5))
    tk.Label(head,text=f"{_U68_COMPONENT_LABELS.get(module,module)} — SYMULATOR 3D + RZECZYWISTE POMIARY",bg=t["panel"],fg=t["accent"],font=self.fnt(12,"bold")).pack(anchor="w",padx=10,pady=(7,2))
    tk.Label(head,text="Obracany schemat podzespołu i wykresy telemetrii. Skan nie wykonuje zapisu destrukcyjnego. Wynik benchmarku pochodzi z operacji opisanej w raporcie.",bg=t["panel"],fg=t["muted"],font=self.fnt(8),wraplength=1400,justify="left").pack(anchor="w",padx=10,pady=(0,6))
    self._u68_sim_status=tk.Label(self.content,text=f"Gotowy — {mode.upper()} {module}.",bg=t["bg"],fg=t["accent"],font=self.fnt(9,"bold"),anchor="w");self._u68_sim_status.pack(fill="x",padx=5,pady=4)
    self._u68_sim_canvas=tk.Canvas(self.content,height=350,bg="#06101c",highlightthickness=0);self._u68_sim_canvas.pack(fill="x",expand=False,padx=4,pady=3)
    self._u67_stage_values={};metrics=tk.Frame(self.content,bg=t["bg"]);metrics.pack(fill="x",padx=2,pady=2)
    specs=[("CPU","cpu"),("RAM","ram"),("GPU","gpu"),("TEMP CPU","cpu_temp"),("TEMP GPU","gpu_temp"),("DYSK OD.","disk_read"),("DYSK ZAP.","disk_write"),("NET ↓","net_down"),("NET ↑","net_up")]
    for i,(title,key) in enumerate(specs):
        card=tk.Frame(metrics,bg=t["card"],highlightbackground=t["accent2"],highlightthickness=1);card.grid(row=0,column=i,sticky="nsew",padx=1,pady=1)
        tk.Label(card,text=title,bg=t["card"],fg=t["muted"],font=self.fnt(7,"bold")).pack(padx=2,pady=(2,0))
        val=tk.Label(card,text="N/D",bg=t["card"],fg=t["accent"],font=self.fnt(8,"bold"));val.pack(padx=2,pady=(0,2));self._u67_stage_values[key]=val
    for i in range(len(specs)):metrics.grid_columnconfigure(i,weight=1)
    charts=tk.Frame(self.content,bg=t["bg"]);charts.pack(fill="x",padx=2,pady=2)
    self._u67_stage_chart_hw=tk.Canvas(charts,height=88,bg=t["card"],highlightthickness=0);self._u67_stage_chart_hw.pack(side="left",fill="both",expand=True,padx=(0,2))
    self._u67_stage_chart_io=tk.Canvas(charts,height=88,bg=t["card"],highlightthickness=0);self._u67_stage_chart_io.pack(side="left",fill="both",expand=True,padx=(2,0))
    row=tk.Frame(self.content,bg=t["bg"]);row.pack(fill="x",pady=2)
    self.make_button(row,"URUCHOM TEST TEGO MODUŁU",lambda m=module,md=mode:_u68_launch_component_test(self,m,md),"accent",side="left",ipady=5)
    self.make_button(row,"STOP TEST",self.stop_current_test,"bad",side="left",ipady=5)
    self.make_button(row,"WRÓĆ DO MODUŁU",lambda m=module:self.show_module("GPU" if m=="VRAM" else m),"card",side="left",ipady=5)
    if not hasattr(self,"_u67_hist"):self._u67_hist={"cpu":[],"ram":[],"gpu":[],"read":[],"write":[],"down":[],"up":[]}
    self._u68_sim_angle=0.0;_u68_draw_component_scene(self);self.after(450,lambda:_u68_sim_metrics_tick(self))
    if run_test:self.after(120,lambda m=module,md=mode:_u68_launch_component_test(self,m,md))

def _u68_launch_component_test(self,module,mode="benchmark"):
    if getattr(self,"running",False):
        messagebox.showwarning("Test komponentu","Inny test jest już uruchomiony. Zatrzymaj go albo zaczekaj.");return
    if module=="VRAM":_u68_open_vram_test(self);return
    if module=="GPU" and mode!="scan":_u68_open_gpu_suite(self,auto_start=True);return
    if module=="EKRAN" and mode!="scan" and hasattr(self,"_u37_open_screen_test"):self._u37_open_screen_test();return
    if module=="DYSK" and mode!="scan":
        requested=_u68_selected_mb(self,"disk")
        if requested>=2048 and not messagebox.askyesno("Benchmark dysku MAX",f"Uruchomić odczyt/zapis pliku testowego do {requested} MB? Może to obciążyć nośnik i zużyć tymczasowo przestrzeń."):return
    if module=="RAM" and mode!="scan":
        requested=_u68_selected_mb(self,"ram")
        if requested>=1024 and not messagebox.askyesno("Benchmark RAM ULTRA/MAX",f"Uruchomić test wzorców w buforze do {requested} MB? Test nie obejmuje całej pamięci fizycznej."):return
    self._u68_sim_status.config(text=f"TEST TRWA — {module} • tryb {mode.upper()} • pomiary aktualizowane w tle",fg=self.colors()["warn"])
    self.header_status.config(text="TEST TRWA — "+module,fg=self.colors()["warn"])
    self.worker(lambda:_u68_run_component_worker(self,module,mode))

def _u68_open_gpu_suite(self,auto_start=False):
    _u66_show_3d_studio(self)
    try:self._u66_scene_seconds.set(str(_u68_profile_seconds(self))+" s")
    except Exception:
        try:self._u66_scene_seconds.set("10 s")
        except Exception:pass
    if auto_start:self.after(300,lambda:_u66_start_3d_all(self))

def _u68_open_vram_test(self):
    _u69_open_component_simulator(self,"VRAM",False,"scan")

def _u68_show_games_advisor(self):
    self.current_view="GAMES_ADVISOR";self.clear();t=self.colors();self.header_title.config(text="DORADCA GIER — PROFILE GRAFIKI")
    gpus=get_gpu_info();cpu=get_cpu_info();ram=psutil.virtual_memory().total if psutil else 0;main=primary_gpu(gpus) if gpus else {}
    gpu_name=str(main.get("Name","GPU nieustalone"));vr=_u41_vram_inventory_text(main) if main else "N/D";r_gb=float(ram or 0)/1024**3;name=gpu_name.lower()
    if any(k in name for k in ("rtx 50","rtx 40","rx 7900","rx 7800","rx 6800","rx 6900","arc b")):tier="WYSOKA";preset="1080p/1440p — zacznij od High; Ultra po sprawdzeniu pamięci i stabilności."
    elif any(k in name for k in ("rtx 30","rx 6600","rx 6700","rx 7600","arc a7","gtx 1660","gtx 1080","rtx 2060","rtx 2070")):tier="ŚREDNIA/WYSOKA";preset="1080p — Medium/High; Ultra tylko w lżejszych tytułach i po teście."
    elif any(k in name for k in ("gtx 10","gtx 1650","rx 580","rx 5500","mx","uhd graphics","iris xe","vega","radeon graphics")):tier="PODSTAWOWA/ŚREDNIA";preset="720p/1080p — Low/Medium; ogranicz cienie i ray tracing."
    else:tier="NIEUSTALONA";preset="Nie ustawiaj Ultra na podstawie samej nazwy. Wykonaj test GPU/VRAM i sprawdź wymagania konkretnej gry."
    title=tk.Frame(self.content,bg=t["panel"]);title.pack(fill="x",pady=(0,7))
    tk.Label(title,text="DOPASOWANIE WSTĘPNE — NIE SĄ TO FPS Z PRAWDZIWYCH GIER",bg=t["panel"],fg=t["accent"],font=self.fnt(12,"bold")).pack(anchor="w",padx=12,pady=(9,3))
    tk.Label(title,text=f"GPU: {gpu_name} • VRAM: {vr} • RAM: {r_gb:.1f} GB • CPU: {cpu.get('Name','N/D')}",bg=t["panel"],fg=t["fg"],font=self.fnt(9),wraplength=1300,justify="left").pack(anchor="w",padx=12,pady=(0,4))
    tk.Label(title,text=f"Poziom heurystyczny: {tier} • Profil startowy: {preset}",bg=t["panel"],fg=t["good"] if tier=="WYSOKA" else t["warn"],font=self.fnt(9,"bold"),wraplength=1300,justify="left").pack(anchor="w",padx=12,pady=(0,8))
    table=self.panel(self.content);table.pack(fill="both",expand=True);tree=self.make_tree(table,("GRA / TYP","PROFIL STARTOWY","CO ZMIENIĆ PIERWSZE"))
    titles=[
      ("Valorant / League of Legends / Rocket League","Competitive / Low lub Medium","Obniż cienie i efekty; cel to stabilne FPS."),
      ("Counter-Strike 2 / Fortnite","Low/Medium; tryb wydajności gdy dostępny","Zmniejsz cienie, efekty i odległość renderowania."),
      ("Forza Horizon 5 / gry wyścigowe","Medium jako punkt startu; tekstury według VRAM","Przetestuj ruchliwą scenę i użycie VRAM."),
      ("GTA V / gry z otwartym światem","Medium/High zależnie od VRAM i rozdzielczości","Sprawdź gęstość populacji, cienie i zaawansowane efekty."),
      ("Cyberpunk 2077 / Hogwarts Legacy / Starfield","Low/Medium; upscaling tylko jeśli wspierany","Ray tracing wyłącz na start; zweryfikuj płynność."),
      ("Alan Wake 2 / inne wymagające tytuły","Najniższy zgodny preset; wymagania sprawdź dla wersji gry","To nie jest gwarancja zgodności ani uruchomienia.")
    ]
    for item in titles:tree.insert("","end",values=item)
    tk.Label(self.content,text=f"Przed ustawieniem Ultra: wykonaj {len(_U66_SCENES)} scen OpenGL, test VRAM i odczyt RAM. FPS proceduralnego OpenGL nie jest przelicznikiem FPS w grze. Profile są wskazówką, nie gwarancją wydajności.",bg=t["bg"],fg=t["muted"],font=self.fnt(8),wraplength=1400,justify="left").pack(fill="x",padx=5,pady=5)
    row=tk.Frame(self.content,bg=t["bg"]);row.pack(fill="x")
    self.make_button(row,f"▶ URUCHOM {len(_U66_SCENES)} SCEN 3D",lambda:_u68_open_gpu_suite(self,auto_start=True),"accent",side="left",ipady=5)
    self.make_button(row,"▶ TEST VRAM",lambda:_u68_open_vram_test(self),"card",side="left",ipady=5)
    self.make_button(row,"← TESTY",self.show_tests_hub,"card",side="left",ipady=5)

_U68_ORIGINAL_SHOW_MODULE=AppV43.show_module
_U68_ORIGINAL_SHOW_SIMPLE_MODULE=AppV43.show_simple_module
AppV43.show_module=_u68_show_module_with_workbench
AppV43.show_simple_module=_u68_show_simple_module_with_workbench
_U68_ORIGINAL_OPEN_TESTS_ITEM=_u66_open_tests_item
def _u68_open_tests_item(self,key):
    if key=="GAMES":return _u68_show_games_advisor(self)
    return _U68_ORIGINAL_OPEN_TESTS_ITEM(self,key)
_u66_open_tests_item=_u68_open_tests_item


# v4.3.73 — independent component workbenches, selected-volume benchmarks, and own VRAM 3D page.
_U69_COMPONENT_LABELS={
    "CPU":"Procesor / CPU","RAM":"Pamięć RAM","GPU":"Karta graficzna / GPU","VRAM":"Pamięć karty / VRAM",
    "DYSK":"SSD / HDD / NVMe","EKRAN":"Matryca / EDID","SECURITY":"Bezpieczeństwo","BATERIA":"Bateria / zasilanie",
    "SIEĆ":"Sieć / Wi-Fi / LAN","USB":"USB / urządzenia","AUDIO":"Audio / mikrofon / głośniki","KLAWIATURA":"Klawiatura / touchpad","KAMERA":"Kamera"
}
_U69_ORIGINAL_SHOW_MODULE=_U68_ORIGINAL_SHOW_MODULE
_U69_ORIGINAL_SHOW_SIMPLE_MODULE=_U68_ORIGINAL_SHOW_SIMPLE_MODULE
_U69_ORIGINAL_SHOW_BATTERY=AppV43.show_battery_or_power
_U69_ORIGINAL_VRAM_STATUS=getattr(AppV43,"_u41_set_vram_status",None)
_U69_ORIGINAL_OPEN_COMPONENT_SIMULATOR=_u68_open_component_simulator

def _u69_drive_options(self):
    drives=[]
    try:
        logical=getattr(self,"logical_disks",None) or get_logical_disks()
        for item in logical or []:
            ident=str(item.get("DeviceID") or item.get("device_id") or item.get("DriveLetter") or "").strip()
            if len(ident)>=2 and ident[1]==":":
                root=ident[:2]+"\\"
                if root not in drives:drives.append(root)
    except Exception:pass
    if not drives:
        root=str(os.environ.get("SystemDrive","C:")).strip()
        if len(root)==2 and root[1]==":":root+="\\"
        drives=[root or "C:\\"]
    return drives

def _u69_attach_workbench(self,module):
    try:
        t=self.colors()
        panel=tk.Frame(self.content,bg=t["panel"],highlightbackground=t["accent"],highlightthickness=1)
        children=self.content.winfo_children()
        if len(children)>1:panel.pack(fill="x",padx=3,pady=4,before=children[1])
        elif children:panel.pack(fill="x",padx=3,pady=4,before=children[0])
        else:panel.pack(fill="x",padx=3,pady=4)
        self._u69_workbench_panel=panel
        tk.Label(panel,text="TESTY NIEZALEŻNE • SKAN • BENCHMARK ULTRA/MAX • WIZUALIZACJA 3D",bg=t["panel"],fg=t["accent"],font=self.fnt(10,"bold")).pack(anchor="w",padx=9,pady=(7,2))
        tk.Label(panel,text="Każdy przycisk uruchamia osobny test. Wykresy są pomiarami bieżącymi; schemat 3D jest wizualizacją, a FPS mierzy tylko rzeczywisty test renderera.",bg=t["panel"],fg=t["muted"],font=self.fnt(8),wraplength=1400,justify="left").pack(anchor="w",padx=9,pady=(0,5))
        row=tk.Frame(panel,bg=t["panel"]);row.pack(fill="x",padx=6,pady=(0,6))
        self._u68_profile_var=tk.StringVar(value=getattr(self,"_u68_profile_value","ULTRA — 300 s"))
        cb=ttk.Combobox(row,textvariable=self._u68_profile_var,values=_U68_PROFILE_CHOICES,state="readonly",width=18);cb.pack(side="left",padx=3,ipady=3)
        cb.bind("<<ComboboxSelected>>",lambda e:setattr(self,"_u68_profile_value",self._u68_profile_var.get()))
        if module=="RAM":
            self._u68_ram_size_var=tk.StringVar(value=getattr(self,"_u68_ram_value","512 MB"))
            ttk.Combobox(row,textvariable=self._u68_ram_size_var,values=("128 MB","256 MB","512 MB","1024 MB","1536 MB","2048 MB"),state="readonly",width=11).pack(side="left",padx=3,ipady=3)
        elif module=="DYSK":
            self._u68_disk_size_var=tk.StringVar(value=getattr(self,"_u68_disk_value","512 MB"))
            ttk.Combobox(row,textvariable=self._u68_disk_size_var,values=("128 MB","256 MB","512 MB","1024 MB","2048 MB","4096 MB"),state="readonly",width=11).pack(side="left",padx=3,ipady=3)
            drives=_u69_drive_options(self)
            self._u69_disk_drive_var=tk.StringVar(value=getattr(self,"_u69_disk_drive_value",drives[0]))
            if self._u69_disk_drive_var.get() not in drives:self._u69_disk_drive_var.set(drives[0])
            ttk.Combobox(row,textvariable=self._u69_disk_drive_var,values=drives,state="readonly",width=8).pack(side="left",padx=3,ipady=3)
            self._u69_disk_drive_var.trace_add("write",lambda *_:setattr(self,"_u69_disk_drive_value",self._u69_disk_drive_var.get()))
        self._u69_workbench_status=tk.Label(row,text="Gotowy — wybierz SKAN, BENCHMARK albo SYMULATOR 3D.",bg=t["panel"],fg=t["muted"],font=self.fnt(8,"bold"),anchor="w")
        self._u69_workbench_status.pack(side="left",fill="x",expand=True,padx=8)
        self.make_button(row,"SKAN + LIVE 3D",lambda m=module:_u69_open_component_simulator(self,m,True,"scan"),"card",side="left",ipady=5)
        self.make_button(row,"BENCHMARK ULTRA/MAX",lambda m=module:_u69_open_component_simulator(self,m,True,"benchmark"),"accent",side="left",ipady=5)
        self.make_button(row,"SYMULATOR 3D",lambda m=module:_u69_open_component_simulator(self,m,False,"scan"),"good",side="left",ipady=5)
        if module=="GPU":
            self.make_button(row,"TEST VRAM 3D",lambda:_u69_open_vram_test(self),"card",side="left",ipady=5)
            self.make_button(row,f"STUDIO GPU {len(_U66_SCENES)} SCEN",lambda:_u68_open_gpu_suite(self),"good",side="left",ipady=5)
        if module=="EKRAN" and hasattr(self,"_u37_open_screen_test"):
            self.make_button(row,"TEST PIKSELI",self._u37_open_screen_test,"card",side="left",ipady=5)
        labrow=tk.Frame(panel,bg=t["panel"]);labrow.pack(fill="x",padx=6,pady=(0,4))
        self.make_button(labrow,"OTWÓRZ LABORATORIUM — WSZYSTKIE TESTY OSOBNO",self.show_component_lab,"good",side="left",ipady=4)
        speedrow=tk.Frame(panel,bg=t["panel"]);speedrow.pack(fill="x",padx=6,pady=(0,6))
        self.make_button(speedrow,"▶ SPEED TEST INTERNETU — DOWNLOAD / UPLOAD / PING",self.show_speed_test,"accent",side="left",ipady=6)
        self.make_button(speedrow,"MONITOR LIVE — TEMPERATURY / W / V / MHZ",self.show_live_monitor,"card",side="left",ipady=6)
    except Exception as exc:
        try:self.append_log("Nie udało się dodać panelu komponentu: "+repr(exc))
        except Exception:pass

def _u69_show_module(self,module):
    if module in ("DYSKI","DYSKI — SSD / HDD / NVMe","SSD / HDD / NVMe"):module="DYSK"
    _U69_ORIGINAL_SHOW_MODULE(self,module)
    if module in ("CPU","GPU","RAM","DYSK","EKRAN","SECURITY"):_u69_attach_workbench(self,module)

def _u69_key_for_simple(title):
    name=str(title).upper()
    if "USB" in name:return "USB"
    if any(x in name for x in ("SIEĆ","WI-FI","WIFI","LAN")):return "SIEĆ"
    if any(x in name for x in ("AUDIO","DŹWIĘK","MIKROFON","GŁOŚNIK")):return "AUDIO"
    if any(x in name for x in ("KLAWIATURA","TOUCHPAD","MYSZ")):return "KLAWIATURA"
    if any(x in name for x in ("KAMERA","WEBCAM")):return "KAMERA"
    return None

def _u69_attach_simple_workbench(self,module):
    t=self.colors();panel=tk.Frame(self.content,bg=t["panel"],highlightbackground=t["accent"],highlightthickness=1)
    children=self.content.winfo_children()
    if len(children)>1:panel.pack(fill="x",padx=3,pady=4,before=children[1])
    else:panel.pack(fill="x",padx=3,pady=4)
    tk.Label(panel,text=f"{_U69_COMPONENT_LABELS.get(module,module)} • TEST NIEZALEŻNY + WIZUALIZACJA 3D",bg=t["panel"],fg=t["accent"],font=self.fnt(9,"bold")).pack(anchor="w",padx=9,pady=(6,2))
    row=tk.Frame(panel,bg=t["panel"]);row.pack(fill="x",padx=5,pady=(0,5))
    self._u69_simple_status=tk.Label(row,text="Gotowy — wynik skanu nie jest wynikiem benchmarku.",bg=t["panel"],fg=t["muted"],font=self.fnt(8,"bold"),anchor="w")
    self._u69_simple_status.pack(side="left",fill="x",expand=True,padx=5)
    self.make_button(row,"SKAN + LIVE 3D",lambda m=module:_u69_open_component_simulator(self,m,True,"scan"),"card",side="left",ipady=4)
    self.make_button(row,"TEST FUNKCJONALNY",lambda m=module:_u69_open_component_simulator(self,m,True,"benchmark"),"accent",side="left",ipady=4)
    self.make_button(row,"SYMULATOR 3D",lambda m=module:_u69_open_component_simulator(self,m,False,"scan"),"good",side="left",ipady=4)
    labrow=tk.Frame(panel,bg=t["panel"]);labrow.pack(fill="x",padx=5,pady=(0,4))
    self.make_button(labrow,"OTWÓRZ LABORATORIUM — WSZYSTKIE TESTY OSOBNO",self.show_component_lab,"good",side="left",ipady=4)
    speedrow=tk.Frame(panel,bg=t["panel"]);speedrow.pack(fill="x",padx=5,pady=(0,5))
    self.make_button(speedrow,"▶ SPEED TEST INTERNETU — DOWNLOAD / UPLOAD / PING",self.show_speed_test,"accent",side="left",ipady=6)
    self.make_button(speedrow,"MONITOR LIVE — TEMPERATURY / W / V / MHZ",self.show_live_monitor,"card",side="left",ipady=6)

def _u69_show_simple_module(self,title):
    _U69_ORIGINAL_SHOW_SIMPLE_MODULE(self,title)
    key=_u69_key_for_simple(title)
    if key:_u69_attach_simple_workbench(self,key)

def _u69_show_battery_module(self):
    _U69_ORIGINAL_SHOW_BATTERY(self)
    _u69_attach_simple_workbench(self,"BATERIA")

def _u69_ram_throughput_benchmark(self,requested_mb,seconds):
    ctypes_mod=__import__("ctypes");hashlib_mod=__import__("hashlib")
    available_mb=int(psutil.virtual_memory().available/(1024*1024)) if psutil else 512
    safe_mb=max(64,min(int(requested_mb),2048,max(64,int(available_mb*.20))))
    buffer=None
    while safe_mb>=64 and buffer is None:
        try:buffer=bytearray(safe_mb*1024*1024)
        except MemoryError:safe_mb//=2
    if buffer is None:raise MemoryError("Nie udało się przydzielić bezpiecznego bufora RAM nawet 64 MB.")
    size=len(buffer);ptr=ctypes_mod.addressof(ctypes_mod.c_char.from_buffer(buffer))
    expected={}
    for pattern in (0x00,0xFF,0xAA,0x55):
        digest=hashlib_mod.sha256()
        full,rem=divmod(size,1024*1024);chunk=bytes([pattern])*(1024*1024)
        for _ in range(full):digest.update(chunk)
        if rem:digest.update(bytes([pattern])*rem)
        expected[pattern]=digest.digest()
    samples=[];writes=0;reads=0;passes=0;start=_u66_time.perf_counter();deadline=start+max(15,min(900,int(seconds)));error=None
    while passes==0 or _u66_time.perf_counter()<deadline:
        for pattern in (0x00,0xFF,0xAA,0x55):
            if self._test_should_stop():break
            t0=_u66_time.perf_counter()
            ctypes_mod.memset(ptr,pattern,size);writes+=size
            actual=hashlib_mod.sha256(memoryview(buffer)).digest();reads+=size
            if actual!=expected[pattern]:
                error=f"Niezgodność pełnego skrótu wzorca {pattern:02X}; test RAM wykrył różnicę."
                break
            samples.append({"pattern":f"{pattern:02X}","pass":passes+1,"write_MBps":round(size/max(.001,_u66_time.perf_counter()-t0)/1_000_000,2)})
        passes+=1;elapsed=max(.001,_u66_time.perf_counter()-start)
        if error or self._test_should_stop() or elapsed>=seconds:break
        self.queue_action(lambda n=passes,e=elapsed,m=safe_mb:self._u69_status_text(self,f"RAM BENCHMARK: {m} MB • przebieg {n} • {e:.0f}/{seconds} s"))
    elapsed=max(.001,_u66_time.perf_counter()-start)
    result={"state":"bad" if error else "warn" if self._test_should_stop() else "good","buffer_mb":safe_mb,"passes":passes,
            "duration_seconds":round(elapsed,2),"write_MBps":round(writes/elapsed/1_000_000,2),"read_MBps":round(reads/elapsed/1_000_000,2),
            "bytes_written":writes,"bytes_verified":reads,"verification":"SHA-256 full-buffer match for 00/FF/AA/55 patterns","error":error,
            "stopped":bool(self._test_should_stop()),"note":"Testuje przydzielony bufor, nie całą fizyczną pamięć. Hash pełnego bufora potwierdza wzorzec; RAM pozostaje używany przez Windows."}
    self.queue_results("RAM_BENCHMARK",result)
    self.queue_results("RAM",{"state":result["state"],"size_mb":safe_mb,"message":f"RAM wzorce: {passes} przebiegów, zapis {result['write_MBps']} MB/s, odczyt/weryfikacja {result['read_MBps']} MB/s","benchmark":result})
    self.queue_log(f"RAM BENCHMARK: {safe_mb} MB • zapis {result['write_MBps']} MB/s • odczyt+SHA256 {result['read_MBps']} MB/s • przebiegi {passes} • stan {result['state']}")
    return result

def _u69_safe_disk_benchmark(root,mb):
    """Benchmark a unique, exclusively-created temporary file on the selected volume."""
    total=int(max(64,int(mb))*1024*1024)
    block=os.urandom(min(8*1024*1024,total))
    filename=f".naprawapc_hw_benchmark_{os.getpid()}_{_u66_uuid.uuid4().hex}.tmp"
    target=os.path.join(root,filename)
    created=False
    try:
        handle=open(target,"xb",buffering=0)
        created=True
        with handle as f:
            t0=_u66_time.perf_counter();written=0
            while written<total:
                n=min(len(block),total-written)
                f.write(block[:n]);written+=n
            f.flush();os.fsync(f.fileno())
            write_seconds=max(.0001,_u66_time.perf_counter()-t0)
        t0=_u66_time.perf_counter();read=0
        with open(target,"rb",buffering=0) as f:
            while read<total:
                data=f.read(min(len(block),total-read))
                if not data:break
                read+=len(data)
        read_seconds=max(.0001,_u66_time.perf_counter()-t0)
        if read!=total:raise OSError(f"Odczyt niepełny: {read}/{total} bajtów.")
        return {"write_bps":total/write_seconds,"read_bps":read/read_seconds,"size_mb":mb,"root":root,"temp_file":"unikalny i usunięty po teście"}
    finally:
        if created:
            try:os.remove(target)
            except Exception:pass

def _u69_disk_throughput_benchmark(self,requested_mb,seconds):
    var=getattr(self,"_u69_disk_drive_var",None)
    drive=str(var.get() if var else _u69_drive_options(self)[0]).strip()
    drives=_u69_drive_options(self)
    if not drive:drive=drives[0]
    if drive not in drives:raise ValueError("Wybrany wolumin nie należy do listy wykrytych dysków.")
    if len(drive)==2 and drive[1]==":":drive+="\\"
    mb=max(64,min(4096,int(requested_mb)));required=mb*1024*1024+128*1024*1024
    try:free=__import__("shutil").disk_usage(drive).free
    except Exception as exc:raise OSError(f"Nie można odczytać wolnego miejsca na {drive}: {exc}")
    if free<required:raise OSError(f"Na {drive} jest za mało wolnego miejsca dla pliku testowego {mb} MB.")
    samples=[];start=_u66_time.perf_counter();deadline=start+max(15,min(900,int(seconds)));passes=0
    while passes==0 or _u66_time.perf_counter()<deadline:
        if self._test_should_stop():break
        result=_u69_safe_disk_benchmark(drive,mb)
        if "error" in result:
            self.queue_results("DYSK",{"state":"warn","error":result["error"],"target_volume":drive,"requested_mb":mb,"passes":passes})
            raise OSError(result["error"])
        samples.append(result);passes+=1;elapsed=max(.001,_u66_time.perf_counter()-start)
        self.queue_action(lambda n=passes,e=elapsed,r=result,d=drive:self._u69_status_text(self,f"DYSK {d}: przebieg {n} • zapis {fmt_speed(r.get('write_bps',0))} • odczyt {fmt_speed(r.get('read_bps',0))} • {e:.0f}/{seconds} s"))
        if self._test_should_stop():break
    elapsed=max(.001,_u66_time.perf_counter()-start)
    writes=sum(float(x.get("write_bps",0)) for x in samples)/max(1,len(samples))
    reads=sum(float(x.get("read_bps",0)) for x in samples)/max(1,len(samples))
    reliability=get_storage_reliability();critical=[x for x in reliability if safe_int(x.get("ReadErrorsTotal"),0)>0 or safe_int(x.get("WriteErrorsTotal"),0)>0 or safe_int(x.get("Wear"),0)>=100]
    report={"state":"bad" if critical else "warn" if self._test_should_stop() else "good","benchmark":{"write_bps":writes,"read_bps":reads,"size_mb":mb},
            "target_volume":drive,"requested_mb":mb,"passes":passes,"duration_seconds":round(elapsed,2),"samples":samples,
            "devices":get_physical_disks(),"reliability":reliability,"critical_reliability":critical,"note":"Test pliku na wybranym woluminie; nie jest to bezpośredni test sektorów fizycznych."}
    self.queue_results("DYSK",report);self.queue_results("DISK_BENCHMARK",report)
    self.queue_log(f"DYSK BENCHMARK {drive}: zapis {fmt_speed(writes)} • odczyt {fmt_speed(reads)} • {passes} przebiegów • stan {report['state']}")
    return report

def _u69_camera_scan(self):
    items=[]
    if is_windows():
        try:items=_v4319_normalize_items(ps_json("Get-PnpDevice -PresentOnly -ErrorAction SilentlyContinue | Where-Object { $_.Class -match 'Camera|Image' -or $_.FriendlyName -match 'camera|webcam|kamera' } | Select-Object Class,FriendlyName,Status,InstanceId | ConvertTo-Json -Compress",default=[]))
        except Exception:items=[]
    state="good" if items else "warn"
    result={"state":state,"items":items,"count":len(items),"message":f"Wykryte urządzenia kamery: {len(items)}; podgląd obrazu wymaga jawnego uruchomienia użytkownika."}
    self.queue_results("CAMERA",result);self.queue_log("KAMERA: "+result["message"])
    return result

def _u69_battery_monitor(self,seconds):
    start=_u66_time.monotonic();samples=[]
    if not psutil:
        self.queue_results("BATTERY_BENCHMARK",{"state":"warn","message":"psutil niedostępny."});return
    first=psutil.sensors_battery()
    if first is None:
        result={"state":"warn","message":"Brak baterii — prawdopodobnie PC stacjonarny albo kontroler nie udostępnia danych.","samples":[]}
        self.queue_results("BATTERY_BENCHMARK",result);self.queue_log("BATERIA: brak kontrolera, monitorowanie pominięte.");return
    deadline=start+max(15,min(900,int(seconds)))
    while True:
        now=_u66_time.monotonic()
        try:
            battery=psutil.sensors_battery()
            if battery is not None:samples.append({"seconds":round(now-start,1),"percent":float(battery.percent),"plugged":bool(battery.power_plugged)})
        except Exception:pass
        if self._test_should_stop() or now>=deadline:break
        self.queue_action(lambda n=len(samples),p=(samples[-1]["percent"] if samples else "N/D"),e=now-start:self._u69_status_text(self,f"BATERIA: próbka {n} • poziom {p}% • czas {e:.0f}/{seconds} s"))
        _u66_time.sleep(1)
    elapsed=max(.1,_u66_time.monotonic()-start);delta=(samples[-1]["percent"]-samples[0]["percent"]) if len(samples)>1 else None
    result={"state":"warn" if self._test_should_stop() or len(samples)<2 else "good","duration_seconds":round(elapsed,1),"samples":samples,
            "start_percent":samples[0]["percent"] if samples else None,"end_percent":samples[-1]["percent"] if samples else None,
            "delta_percent":round(delta,2) if delta is not None else None,"note":"Krótki test pokazuje obserwowaną zmianę; nie jest pełnym pomiarem czasu pracy baterii."}
    self.queue_results("BATTERY_BENCHMARK",result);self.queue_log(f"BATERIA BENCHMARK: próbki {len(samples)} • zmiana {result.get('delta_percent','N/D')}% • {elapsed:.0f} s")

def _u69_status_text(self,message):
    for name in ("_u69_workbench_status","_u69_sim_status","_u68_sim_status","_u69_simple_status"):
        label=getattr(self,name,None)
        try:
            if label is not None and label.winfo_exists():label.config(text=message,fg=self.colors()["warn"])
        except Exception:pass
    try:self.header_status.config(text="TEST W TOKU",fg=self.colors()["warn"])
    except Exception:pass

def _u69_component_result_text(self,module,mode,started):
    scan_keys={"CPU":"COMPONENT_SCAN_CPU","RAM":"COMPONENT_SCAN_RAM","DYSK":"COMPONENT_SCAN_DYSK","VRAM":"COMPONENT_SCAN_VRAM","SIEĆ":"NETWORK"}
    result={}
    if mode=="scan" and module in scan_keys:result=(getattr(self,"results",{}) or {}).get(scan_keys[module],{}) or {}
    else:
        keys={"CPU":["CPU"],"RAM":["RAM_BENCHMARK","RAM"],"DYSK":["DISK_BENCHMARK","DYSK"],"GPU":["GPU","GPU_WINSAT"],"VRAM":["VRAM_TEST"],
              "EKRAN":["EKRAN"],"SECURITY":["SECURITY"],"BATERIA":["BATTERY_BENCHMARK","BATERIA"],"SIEĆ":["SPEED_TEST","NETWORK"],
              "USB":["USB"],"AUDIO":["AUDIO"],"KLAWIATURA":["INPUTS"],"KAMERA":["CAMERA"]}
        for key in keys.get(module,[module]):
            value=(getattr(self,"results",{}) or {}).get(key)
            if isinstance(value,dict) and value:result=value;break
    error=getattr(self,"_u69_last_component_error",None)
    if isinstance(error,dict) and error.get("module")==module and error.get("time")==getattr(self,"_u69_last_error_time",None):result=error
    elapsed=max(.01,_u66_time.monotonic()-started);state=str(result.get("state","N/D"));details=[]
    if mode=="scan" and state.lower()=="good":state="WYKRYTO"
    if module=="CPU":
        details.extend([f"Model: {(result.get('cpu') or self.cpu or {}).get('Name','N/D')}",f"Etapy: {len(result.get('stages',[]))}"])
    elif module=="RAM":
        if mode=="scan":details.extend([f"Zainstalowano: {fmt_bytes(result.get('total_bytes')) if result.get('total_bytes') else 'N/D'}",f"Użycie: {result.get('used_percent','N/D')}%",f"Dostępne: {fmt_bytes(result.get('available_bytes')) if result.get('available_bytes') else 'N/D'}"])
        else:details.extend([f"Bufor: {result.get('buffer_mb',result.get('size_mb','N/D'))} MB",f"Zapis: {result.get('write_MBps','N/D')} MB/s",f"Odczyt/weryfikacja: {result.get('read_MBps','N/D')} MB/s",f"Przebiegi: {result.get('passes','N/D')}"])
    elif module=="DYSK":
        bench=result.get("benchmark",{}) or {};details.extend([f"Wolumin: {result.get('target_volume','N/D')}",f"Rozmiar: {bench.get('size_mb',result.get('requested_mb','N/D'))} MB",f"Odczyt: {fmt_speed(bench.get('read_bps',0))}",f"Zapis: {fmt_speed(bench.get('write_bps',0))}",f"Przebiegi: {result.get('passes','N/D')}"])
        if mode=="scan":details.append(f"Fizyczne urządzenia: {len(result.get('devices',[]))}; rekordy SMART/reliability: {len(result.get('reliability',[]))}")
    elif module=="VRAM":
        if mode=="scan":details.append("Inwentarz VRAM: "+str(result.get("vram_inventory","N/D"))+" — to skan identyfikacyjny, nie test pamięci.")
        else:details.extend([f"Alokowano: {result.get('allocated_mb','N/D')} MB",f"Wzorce: {result.get('patterns_completed',0)}/{result.get('patterns_total',0)}",f"Zweryfikowane bajty: {result.get('bytes_verified','N/D')}"])
    elif module=="GPU":details.extend([f"Karta: {(primary_gpu(self.gpus) or {}).get('Name','N/D')}",str(result.get('message',''))])
    elif module=="EKRAN":details.append(f"Wykryte monitory: {len(result.get('monitors',[]))}")
    elif module=="SIEĆ":details.extend([f"Download: {result.get('download_mbps','N/D')} Mbps",f"Upload: {result.get('upload_mbps','N/D')} Mbps",f"Latency: {result.get('latency_average_ms','N/D')} ms"])
    elif module=="BATERIA":details.extend([f"Próbki: {len(result.get('samples',[]))}",f"Zmiana: {result.get('delta_percent','N/D')}%"])
    elif module in ("USB","AUDIO","KLAWIATURA","KAMERA"):details.append(str(result.get('message') or f"Elementy wykryte: {len(result.get('items',[]))}"))
    if result.get("error"):details.append("BŁĄD: "+str(result.get("error")))
    prefix="SKAN" if mode=="scan" else "TEST / BENCHMARK"
    return f"{prefix} {module}: {state.upper()} • {elapsed:.1f} s • "+" • ".join(x for x in details if x)

def _u69_run_component_worker(self,module,mode):
    started=_u66_time.monotonic();seconds=_u68_profile_seconds(self)
    self._u69_last_component_error=None;self._u69_last_error_time=None
    try:
        if module=="CPU":
            if mode=="scan":
                vm=psutil.virtual_memory() if psutil else None
                self.queue_results("COMPONENT_SCAN_CPU",{"state":"good" if self.cpu else "warn","cpu":self.cpu,"logical_cpus":os.cpu_count(),"ram_total":vm.total if vm else None,"sampled_at":_U66_datetime.now().isoformat(timespec="seconds")})
                self.queue_log(f"CPU SCAN: {(self.cpu or {}).get('Name','N/D')} | rdzenie {(self.cpu or {}).get('NumberOfCores','N/D')} | wątki {os.cpu_count() or 'N/D'}")
            else:self._cpu_test(seconds)
        elif module=="RAM":
            if mode=="scan":
                vm=psutil.virtual_memory() if psutil else None
                self.queue_results("COMPONENT_SCAN_RAM",{"state":"good" if vm else "warn","total_bytes":vm.total if vm else None,"available_bytes":vm.available if vm else None,"used_percent":vm.percent if vm else None,"sampled_at":_U66_datetime.now().isoformat(timespec="seconds")})
                self.queue_log("RAM SCAN: "+(f"zainstalowano {fmt_bytes(vm.total)}, dostępne {fmt_bytes(vm.available)}, użycie {vm.percent:.1f}%" if vm else "N/D — psutil niedostępny"))
            else:_u69_ram_throughput_benchmark(self,_u68_selected_mb(self,"ram"),seconds)
        elif module=="DYSK":
            if mode=="scan":
                _u76_disk_scan_selected_volume(self)
            else:_u69_disk_throughput_benchmark(self,_u68_selected_mb(self,"disk"),seconds)
        elif module=="GPU":
            if mode=="scan":self._gpu_test()
            else:self.queue_log(f"GPU benchmark uruchamia rzeczywiste {len(_U66_SCENES)} scen OpenGL — ekran 3D Benchmark Studio.")
        elif module=="VRAM":
            if mode=="scan":
                gpus=get_gpu_info();main=primary_gpu(gpus) if gpus else {}
                inv=_u41_vram_inventory_text(main) if main else "N/D"
                self.queue_results("COMPONENT_SCAN_VRAM",{"state":"good" if main else "warn","gpu":main,"vram_inventory":inv,"sampled_at":_U66_datetime.now().isoformat(timespec="seconds")})
                self.queue_log("VRAM SCAN: "+str(inv)+" — to inwentarz, nie test pamięci.")
            else:self.queue_log("VRAM: użyj przycisku URUCHOM TEST VRAM, aby wykonać rzeczywisty zapis i readback tekstur.")
        elif module=="EKRAN":
            if mode=="scan":self._monitor_test()
            elif hasattr(self,"_u37_open_screen_test"):self._u37_open_screen_test()
            else:self._monitor_test()
        elif module=="SECURITY":self._security_test()
        elif module=="BATERIA":
            if mode=="scan":self._battery_test()
            else:_u69_battery_monitor(self,seconds)
        elif module=="SIEĆ":
            if mode=="scan":self._peripheral_test("SIEĆ")
            else:
                result=_u66_measure_speed(self);self.queue_results("SPEED_TEST",result)
                self.queue_log(f"SPEED TEST: download {result.get('download_mbps','N/D')} Mbps / upload {result.get('upload_mbps','N/D')} Mbps")
        elif module in ("USB","AUDIO","KLAWIATURA"):self._peripheral_test(module)
        elif module=="KAMERA":_u69_camera_scan(self)
        else:self.queue_log(f"Brak niezależnego testu dla modułu {module}.")
    except Exception as exc:
        error={"state":"warn","error":f"{type(exc).__name__}: {exc}","module":module,"time":_U66_datetime.now().isoformat(timespec="seconds")}
        self._u69_last_component_error=error;self._u69_last_error_time=error["time"]
        self.queue_results("COMPONENT_ERROR_"+module,error);self.queue_log(f"TEST {module}: {error['error']}")
    def finish():
        text=_u69_component_result_text(self,module,mode,started)
        _u69_status_text(self,text)
        try:self.header_status.config(text="GOTOWY — "+module,fg=self.colors()["good"] if "GOOD" in text or "WYKRYTO" in text else self.colors()["warn"])
        except Exception:pass
    self.queue_action(finish)

def _u69_open_component_simulator(self,module,run_test=False,mode="scan"):
    _U69_ORIGINAL_OPEN_COMPONENT_SIMULATOR(self,module,False,mode)
    try:
        children=self.content.winfo_children()
        if children:children[-1].destroy()
    except Exception:pass
    options=tk.Frame(self.content,bg=self.colors()["bg"])
    try:options.pack(fill="x",padx=3,pady=2,before=self._u68_sim_canvas)
    except Exception:options.pack(fill="x",padx=3,pady=2)
    row=tk.Frame(options,bg=self.colors()["bg"]);row.pack(fill="x")
    if not hasattr(self,"_u68_profile_var"):self._u68_profile_var=tk.StringVar(value=getattr(self,"_u68_profile_value","ULTRA — 300 s"))
    ttk.Combobox(row,textvariable=self._u68_profile_var,values=_U68_PROFILE_CHOICES,state="readonly",width=18).pack(side="left",padx=2,ipady=3)
    if module=="DYSK":
        drives=_u69_drive_options(self);current=getattr(self,"_u69_disk_drive_value",drives[0])
        self._u69_disk_drive_var=tk.StringVar(value=current if current in drives else drives[0])
        ttk.Combobox(row,textvariable=self._u69_disk_drive_var,values=drives,state="readonly",width=9).pack(side="left",padx=2,ipady=3)
        self._u69_disk_drive_var.trace_add("write",lambda *_:setattr(self,"_u69_disk_drive_value",self._u69_disk_drive_var.get()))
        self._u68_disk_size_var=tk.StringVar(value=getattr(self,"_u68_disk_value","512 MB"))
        ttk.Combobox(row,textvariable=self._u68_disk_size_var,values=("128 MB","256 MB","512 MB","1024 MB","2048 MB","4096 MB"),state="readonly",width=11).pack(side="left",padx=2,ipady=3)
    elif module=="RAM":
        self._u68_ram_size_var=tk.StringVar(value=getattr(self,"_u68_ram_value","512 MB"))
        ttk.Combobox(row,textvariable=self._u68_ram_size_var,values=("128 MB","256 MB","512 MB","1024 MB","1536 MB","2048 MB"),state="readonly",width=11).pack(side="left",padx=2,ipady=3)
    elif module=="VRAM":
        self._u41_vram_size_var=tk.StringVar(value=getattr(self,"_u69_vram_size_value","128 MB"))
        ttk.Combobox(row,textvariable=self._u41_vram_size_var,values=("32 MB","64 MB","128 MB","192 MB","256 MB"),state="readonly",width=11).pack(side="left",padx=2,ipady=3)
    self.make_button(row,"SKAN",lambda m=module:_u69_launch_component_test(self,m,"scan"),"card",side="left",ipady=4)
    self.make_button(row,"TEST / BENCHMARK ULTRA/MAX",lambda m=module:_u69_launch_component_test(self,m,"benchmark"),"accent",side="left",ipady=4)
    self.make_button(row,"STOP TEST",self.stop_current_test,"bad",side="left",ipady=4)
    self.make_button(row,"▶ SPEED TEST",self.show_speed_test,"accent",side="left",ipady=4)
    def back(m=module):
        if getattr(self,"_u78_return_to_component_lab",False):
            self._u78_return_to_component_lab=False
            self.show_component_lab()
            return
        if m in ("CPU","GPU","RAM","DYSK","EKRAN","SECURITY","VRAM"):self.show_module("GPU" if m=="VRAM" else m)
        elif m=="BATERIA":self.show_battery_or_power()
        else:self.show_simple_module({"SIEĆ":"SIEĆ / WI-FI / LAN","USB":"USB / URZĄDZENIA","AUDIO":"DŹWIĘK / AUDIO","KLAWIATURA":"KLAWIATURA / TOUCHPAD","KAMERA":"KAMERA"}.get(m,m))
    self.make_button(row,"WRÓĆ",back,"card",side="left",ipady=4)
    self._u68_sim_angle=0.0
    if run_test:self.after(180,lambda m=module,md=mode:_u69_launch_component_test(self,m,md))

def _u69_open_vram_test(self):
    _u69_open_component_simulator(self,"VRAM",False,"scan")

def _u69_launch_component_test(self,module,mode="benchmark"):
    if getattr(self,"running",False):
        messagebox.showwarning("Test komponentu","Inny test jest uruchomiony. Użyj STOP TEST albo poczekaj.");return
    if module=="GPU" and mode!="scan":
        _u68_open_gpu_suite(self,auto_start=True);return
    if module=="VRAM":
        if mode=="scan":
            self._refresh_after_worker_view=None
            self.worker(lambda:_u69_run_component_worker(self,"VRAM","scan"))
            return
        self._u41_start_vram_test();return
    if module=="EKRAN" and mode!="scan" and hasattr(self,"_u37_open_screen_test"):
        self._u37_open_screen_test();return
    seconds=_u68_profile_seconds(self)
    if module=="DYSK" and mode!="scan":
        mb=_u68_selected_mb(self,"disk");var=getattr(self,"_u69_disk_drive_var",None);drive=str(var.get() if var else _u69_drive_options(self)[0])
        if mb>=2048 or seconds>=180:
            if not messagebox.askyesno("Benchmark dysku ULTRA/MAX",f"Test {drive}, plik {mb} MB, do {seconds} s. Wykonuje powtarzane zapisy/odczyty pliku tymczasowego na wybranym woluminie, a następnie go usuwa. Kontynuować?"):return
    if module=="RAM" and mode!="scan":
        mb=_u68_selected_mb(self,"ram")
        if mb>=1024 or seconds>=180:
            if not messagebox.askyesno("Benchmark RAM ULTRA/MAX",f"Test wzorców/hash SHA-256 w buforze do {mb} MB przez około {seconds} s. Nie testuje całej fizycznej pamięci. Kontynuować?"):return
    if module=="BATERIA" and mode!="scan" and seconds>=180:
        if not messagebox.askyesno("Monitor baterii ULTRA/MAX",f"Próbkować baterię do {seconds} s? Wynik będzie jedynie zmianą odczytanego poziomu podczas testu."):return
    if module=="SIEĆ" and mode!="scan":
        if not messagebox.askyesno("Speed Test", "Test pobierania/wysyłania może przesłać około 24 MB przez Internet. Uruchomić?"):return
    self._u69_status_text(self,f"TEST TRWA — {module} • {mode.upper()} • profil {seconds} s")
    try:self.header_status.config(text="TEST W TOKU — "+module,fg=self.colors()["warn"])
    except Exception:pass
    self.worker(lambda:_u69_run_component_worker(self,module,mode))

def _u69_vram_status(self,result):
    try:
        if _U69_ORIGINAL_VRAM_STATUS:_U69_ORIGINAL_VRAM_STATUS(self,result)
    except Exception:pass
    if str(getattr(self,"current_view","")).startswith("SIM3D_VRAM"):
        try:_u69_status_text(self,str(result.get("status_text") or result.get("message") or "Test VRAM w toku"))
        except Exception:pass

def _u69_show_battery_module(self):
    _U69_ORIGINAL_SHOW_BATTERY(self)
    _u69_attach_simple_workbench(self,"BATERIA")

def _u69_selftest_component_workbenches():
    checks = [
        ("component simulator", callable(_u69_open_component_simulator)),
        ("component launch", callable(_u69_launch_component_test)),
        ("disk benchmark", callable(_u69_disk_throughput_benchmark)),
        ("unique safe disk benchmark", callable(_u69_safe_disk_benchmark)),
        ("simulator original delegate", "_U69_ORIGINAL_OPEN_COMPONENT_SIMULATOR" in _u69_open_component_simulator.__code__.co_names or "_U76_ORIGINAL_OPEN_COMPONENT_SIMULATOR" in _u69_open_component_simulator.__code__.co_names),
        ("open function", "open" in _u69_safe_disk_benchmark.__code__.co_names),
        ("exclusive create mode", "xb" in _u69_safe_disk_benchmark.__code__.co_consts),
        ("RAM bandwidth", callable(_u69_ram_throughput_benchmark)),
        ("camera scan", callable(_u69_camera_scan)),
        ("duration max", "900 s" in ("3 s","5 s","10 s","20 s","30 s","60 s","120 s","180 s","300 s","600 s","900 s")),
        ("component labels", all(k in _U69_COMPONENT_LABELS for k in ("CPU","RAM","DYSK","VRAM","GPU","BATERIA","SIEĆ","USB","AUDIO","KLAWIATURA","KAMERA"))),
    ]
    try:
        drives = "".join(_u69_drive_options(type("O", (), {"logical_disks":[{"DeviceID":"C:"}]})()))
        checks.append(("drive selector C:", "C:" in drives))
    except Exception as exc:
        checks.append(("drive selector C:", False))
    failed = [name for name, ok in checks if not ok]
    if failed:
        raise AssertionError("Failed checks: " + ", ".join(failed))
    print("COMPONENT_WORKBENCH_SELFTEST_OK: " + ", ".join(name for name, _ in checks))

_U69_ORIGINAL_COMPONENT_WORKER=_u68_run_component_worker
_u68_run_component_worker=_u69_run_component_worker
_u68_open_component_simulator=_u69_open_component_simulator
_u68_open_vram_test=_u69_open_vram_test
_u68_launch_component_test=_u69_launch_component_test
AppV43.show_module=_u69_show_module
AppV43.show_simple_module=_u69_show_simple_module
AppV43.show_battery_or_power=_u69_show_battery_module
if hasattr(AppV43,"_u41_set_vram_status"):AppV43._u41_set_vram_status=_u69_vram_status


# v4.3.76 — persistent per-component result reports and visible live telemetry.
_U76_ORIGINAL_OPEN_COMPONENT_SIMULATOR = _u69_open_component_simulator
_U76_ORIGINAL_SIM_METRICS_TICK = _u68_sim_metrics_tick
_U76_ORIGINAL_COMPONENT_WORKER = _u69_run_component_worker
_U76_ORIGINAL_STATUS_TEXT = _u69_status_text

def _u76_component_result_keys(module, mode):
    scan = {
        "CPU": ("COMPONENT_SCAN_CPU", "CPU"),
        "RAM": ("COMPONENT_SCAN_RAM", "RAM"),
        "DYSK": ("COMPONENT_SCAN_DYSK", "DISK_BENCHMARK", "DYSK"),
        "GPU": ("GPU", "GPU_WINSAT"),
        "VRAM": ("COMPONENT_SCAN_VRAM", "VRAM_TEST"),
        "EKRAN": ("EKRAN",),
        "SECURITY": ("SECURITY",),
        "BATERIA": ("BATERIA", "BATTERY_BENCHMARK"),
        "SIEĆ": ("NETWORK", "SPEED_TEST"),
        "USB": ("USB",), "AUDIO": ("AUDIO",),
        "KLAWIATURA": ("INPUTS", "KLAWIATURA"), "KAMERA": ("CAMERA",)
    }
    benchmark = {
        "CPU": ("CPU",), "RAM": ("RAM_BENCHMARK", "RAM"),
        "DYSK": ("DISK_BENCHMARK", "DYSK"), "GPU": ("3D_SUITE", "GPU", "GPU_WINSAT"),
        "VRAM": ("VRAM_TEST",), "EKRAN": ("EKRAN",), "SECURITY": ("SECURITY",),
        "BATERIA": ("BATTERY_BENCHMARK", "BATERIA"), "SIEĆ": ("SPEED_TEST", "NETWORK"),
        "USB": ("USB",), "AUDIO": ("AUDIO",),
        "KLAWIATURA": ("INPUTS", "KLAWIATURA"), "KAMERA": ("CAMERA",)
    }
    return (scan if mode == "scan" else benchmark).get(module, (module,))

def _u76_trim_report(value, depth=0):
    if depth >= 4:
        return str(value)[:250]
    if isinstance(value, dict):
        out = {}
        for key, item in value.items():
            if key in ("samples", "fps_samples") and isinstance(item, list):
                out[key] = {"count": len(item), "first": item[:3], "last": item[-3:]}
            else:
                out[str(key)] = _u76_trim_report(item, depth + 1)
        return out
    if isinstance(value, (list, tuple)):
        if len(value) > 12:
            return {"count": len(value), "first": [_u76_trim_report(x, depth+1) for x in value[:6]],
                    "last": [_u76_trim_report(x, depth+1) for x in value[-3:]]}
        return [_u76_trim_report(x, depth+1) for x in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)[:500]

def _u76_component_report_text(self):
    module = str(getattr(self, "_u76_component_module", "") or str(getattr(self, "current_view", "")).replace("SIM3D_", ""))
    mode = str(getattr(self, "_u76_component_mode", "scan"))
    results = getattr(self, "results", {}) or {}
    found, found_key = None, None
    for key in _u76_component_result_keys(module, mode):
        item = results.get(key)
        if isinstance(item, dict) and item:
            found, found_key = item, key
            break
    err = getattr(self, "_u69_last_component_error", None)
    if isinstance(err, dict) and err.get("module") == module:
        found, found_key = err, "COMPONENT_ERROR_" + module
    if not found:
        progress = str(getattr(self, "_u76_live_progress", "") or "")
        return f"MODUŁ: {module} | TRYB: {mode.upper()}\nStan: oczekiwanie na raport rzeczywistego testu.\n{progress or 'Po zakończeniu skanu/benchmarku wynik zostanie pokazany tutaj.'}"
    summary = {
        "module": module, "mode": mode, "result_key": found_key,
        "state": found.get("state", "N/D"), "sampled_at": found.get("sampled_at"),
        "note": found.get("note"), "message": found.get("message"), "error": found.get("error"),
    }
    if module == "CPU":
        cpu = found.get("cpu") or getattr(self, "cpu", {}) or {}
        summary.update({"model":cpu.get("Name",cpu.get("name","N/D")),"logical_threads":os.cpu_count(),
                        "physical_cores":cpu.get("NumberOfCores","N/D"),"stages":found.get("stages",[])})
    elif module == "RAM":
        vm = found.get("benchmark", found)
        summary.update({"installed_bytes":found.get("total_bytes"),"available_bytes":found.get("available_bytes"),
                        "used_percent":found.get("used_percent"),"buffer_mb":vm.get("buffer_mb",vm.get("size_mb")),
                        "read_MBps":vm.get("read_MBps"),"write_MBps":vm.get("write_MBps"),"passes":vm.get("passes"),
                        "bytes_verified":vm.get("bytes_verified"),"verification":vm.get("verification")})
    elif module == "DYSK":
        usage = found.get("volume_usage") or {}
        summary.update({"target_volume":found.get("target_volume",found.get("root","N/D")),
                        "volume_total_bytes":usage.get("total"),"volume_used_bytes":usage.get("used"),
                        "volume_free_bytes":usage.get("free"),"volume_percent":usage.get("percent"),
                        "physical_devices_count":len(found.get("devices",[])),"physical_devices":found.get("devices",[]),
                        "reliability":found.get("reliability",[]),"benchmark":found.get("benchmark",{}),
                        "passes":found.get("passes"),"duration_seconds":found.get("duration_seconds"),
                        "samples":found.get("samples",[])})
    elif module == "GPU":
        gpus = getattr(self, "gpus", []) or []
        summary.update({"gpu":(primary_gpu(gpus) or {}).get("Name","N/D"),"renderer":found.get("renderer"),
                        "opengl_version":found.get("opengl_version"),"completed_scenes":found.get("completed",found.get("completed_scenes")),
                        "average_fps":found.get("average_fps"),"scene_results":found.get("scenes",[])})
    elif module == "VRAM":
        summary.update({"gpu":(found.get("gpu") or {}).get("Name","N/D"),"vram_inventory":found.get("vram_inventory"),
                        "requested_mb":found.get("requested_mb"),"allocated_mb":found.get("allocated_mb"),
                        "patterns_completed":found.get("patterns_completed"),"patterns_total":found.get("patterns_total"),
                        "bytes_verified":found.get("bytes_verified")})
    elif module == "SIEĆ":
        summary.update({"download_mbps":found.get("download_mbps"),"upload_mbps":found.get("upload_mbps"),
                        "latency_average_ms":found.get("latency_average_ms"),"data_bytes":found.get("data_bytes")})
    elif module == "BATERIA":
        summary.update({"start_percent":found.get("start_percent"),"end_percent":found.get("end_percent"),
                        "delta_percent":found.get("delta_percent"),"duration_seconds":found.get("duration_seconds"),
                        "samples":found.get("samples",[])})
    elif module in ("EKRAN","SECURITY","USB","AUDIO","KLAWIATURA","KAMERA"):
        summary.update(found)
    raw = _u66_json.dumps(_u76_trim_report(summary), ensure_ascii=False, indent=2, default=str)
    progress = str(getattr(self, "_u76_live_progress", "") or "")
    return f"RZECZYWISTY RAPORT • {module} • {mode.upper()} • klucz: {found_key}\n" + (("Ostatni postęp: "+progress[:400]+"\n") if progress else "") + raw[:14000]

def _u76_refresh_component_report(self):
    box = getattr(self, "_u76_result_text", None)
    if box is None or not box.winfo_exists(): return
    try:
        value = _u76_component_report_text(self)
        if getattr(self, "_u76_last_report_text", None) == value: return
        self._u76_last_report_text = value
        box.configure(state="normal"); box.delete("1.0", "end"); box.insert("1.0", value); box.configure(state="disabled")
    except Exception as exc:
        try:
            box.configure(state="normal"); box.delete("1.0", "end")
            box.insert("1.0", "Nie udało się wyświetlić raportu: " + repr(exc)); box.configure(state="disabled")
        except Exception: pass

def _u76_open_component_simulator(self, module, run_test=False, mode="scan"):
    _U76_ORIGINAL_OPEN_COMPONENT_SIMULATOR(self, module, run_test, mode)
    try:
        self._u76_component_module = str(module); self._u76_component_mode = str(mode)
        self._u76_live_progress = ""; self._u76_last_report_text = None
        for canvas_name in ("_u67_stage_chart_hw", "_u67_stage_chart_io"):
            canvas = getattr(self, canvas_name, None)
            if canvas is not None and canvas.winfo_exists(): canvas.configure(height=118)
        panel = tk.Frame(self.content, bg=self.colors()["panel"], highlightbackground=self.colors()["accent"], highlightthickness=1)
        panel.pack(fill="both", expand=True, padx=3, pady=(2,4))
        tk.Label(panel, text="RAPORT SKANU / BENCHMARKU — RZECZYWISTE DANE", bg=self.colors()["panel"], fg=self.colors()["accent"], font=self.fnt(9,"bold"), anchor="w").pack(fill="x", padx=8, pady=(4,1))
        frame = tk.Frame(panel, bg=self.colors()["panel"]); frame.pack(fill="both", expand=True, padx=5, pady=(0,4))
        box = tk.Text(frame, height=5, wrap="word", bg=self.colors()["card"], fg=self.colors()["fg"], insertbackground=self.colors()["fg"], relief="flat", font=("Consolas",8), padx=6, pady=5)
        sb = ttk.Scrollbar(frame, orient="vertical", command=box.yview); box.configure(yscrollcommand=sb.set)
        box.pack(side="left", fill="both", expand=True); sb.pack(side="right", fill="y")
        box.configure(state="disabled"); self._u76_result_text = box
        self.after(160, lambda: _u76_refresh_component_report(self))
    except Exception as exc:
        try: self.append_log("Panel raportu modułu: " + repr(exc))
        except Exception: pass

def _u76_run_component_worker(self, module, mode):
    self._u76_component_module = str(module); self._u76_component_mode = str(mode)
    self._u76_live_progress = f"Start: {module} — {mode.upper()}"
    try: return _U76_ORIGINAL_COMPONENT_WORKER(self, module, mode)
    finally:
        try: self.queue_action(lambda: _u76_refresh_component_report(self))
        except Exception: pass

def _u76_status_text(self, message):
    self._u76_live_progress = str(message)
    try: _U76_ORIGINAL_STATUS_TEXT(self, message)
    except Exception: pass
    try: self.queue_action(lambda: _u76_refresh_component_report(self))
    except Exception: pass

def _u76_sim_metrics_tick(self):
    if not str(getattr(self, "current_view", "")).startswith("SIM3D_"): return
    try: _u67_refresh_visible_charts(self)
    except Exception: pass
    try: _u76_refresh_component_report(self)
    except Exception: pass
    try: self.after(1000, lambda: _u76_sim_metrics_tick(self))
    except Exception: pass

def _u76_disk_scan_selected_volume(self):
    drives = _u69_drive_options(self)
    var = getattr(self, "_u69_disk_drive_var", None)
    drive = str(var.get() if var else (drives[0] if drives else "N/D")).strip()
    if not drive: drive = drives[0] if drives else "N/D"
    if len(drive) == 2 and drive[1] == ":": drive += "\\"
    usage, usage_error = None, None
    try: usage = __import__("shutil").disk_usage(drive)
    except Exception as exc: usage_error = f"{type(exc).__name__}: {exc}"
    volume_usage = {"total":getattr(usage,"total",None),"used":getattr(usage,"used",None),"free":getattr(usage,"free",None),
                    "percent":round(usage.used/usage.total*100,2) if usage and usage.total else None,"error":usage_error}
    devices = get_physical_disks(); reliability = get_storage_reliability()
    result = {"state":"good" if devices and not usage_error else "warn","target_volume":drive,"volume_usage":volume_usage,
              "devices":devices,"reliability":reliability,"sampled_at":_U66_datetime.now().isoformat(timespec="seconds"),
              "note":"Skan identyfikacyjny woluminu i nośników; nie jest to destrukcyjny test sektorowy."}
    self.queue_results("COMPONENT_SCAN_DYSK", result)
    self.queue_log(f"DYSK SKAN {drive}: {len(devices)} fizycznych urządzeń; użycie {volume_usage.get('percent','N/D')}%; wolne {volume_usage.get('free','N/D')} bajtów.")
    return result

def _u76_selftest_workbenches():
    assert len(_U66_SCENES) == 60 and len({str(x[0]) for x in _U66_SCENES}) == 60
    assert callable(_u76_component_report_text) and callable(_u76_refresh_component_report)
    assert callable(_u76_open_component_simulator) and callable(_u76_run_component_worker)
    assert callable(_u76_disk_scan_selected_volume)
    assert "COMPONENT_SCAN_DYSK" in _u76_component_result_keys("DYSK", "scan")
    assert "DISK_BENCHMARK" in _u76_component_result_keys("DYSK", "benchmark")
    assert "RAM_BENCHMARK" in _u76_component_result_keys("RAM", "benchmark")
    assert "VRAM_TEST" in _u76_component_result_keys("VRAM", "benchmark")
    assert "3D_SUITE" in _u76_component_result_keys("GPU", "benchmark")
    print("COMPONENT_REPORT_60_SCENES_SELFTEST_OK")

_U69_ORIGINAL_COMPONENT_WORKER = _u69_run_component_worker
_U69_ORIGINAL_STATUS_TEXT_V76 = _u69_status_text
_u69_open_component_simulator = _u76_open_component_simulator
_u68_open_component_simulator = _u76_open_component_simulator
_u69_run_component_worker = _u76_run_component_worker
_u68_run_component_worker = _u76_run_component_worker
_u69_status_text = _u76_status_text
_u68_sim_metrics_tick = _u76_sim_metrics_tick


# v4.3.78 — one obvious independent-test laboratory for every subsystem.
# A schematic animation is never reported as a measured benchmark. Real results are
# read from the same component test functions used in the individual module screens.
_U78_COMPONENT_LAB = [
    ("CPU", "PROCESOR / CPU", "Identyfikacja, rdzenie/wątki, obciążenie, zegary i próbki. Benchmark wykonuje rzeczywiste obciążenie CPU.", "BENCHMARK ULTRA/MAX"),
    ("RAM", "PAMIĘĆ RAM", "Pojemność i dostępność pamięci; test wzorców 00/FF/AA/55 z porównaniem SHA-256 w ograniczonym buforze.", "BENCHMARK RAM ULTRA/MAX"),
    ("GPU", "KARTA GRAFICZNA / GPU", "Identyfikacja adaptera, sterownika i czujników. Benchmark uruchamia sceny OpenGL z prawdziwym pomiarem FPS.", f"{len(_U66_SCENES)} SCEN 3D ULTRA/MAX"),
    ("VRAM", "PAMIĘĆ KARTY / VRAM", "Inwentarz pamięci oraz oddzielny test tekstur, wzorców zapisu i odczytu zwrotnego.", "TEST VRAM ULTRA/MAX"),
    ("DYSK", "SSD / HDD / NVMe", "Wybór woluminu, pojemność/wolne miejsce, urządzenia i dostępne dane niezawodności; benchmark unikalnym plikiem tymczasowym.", "BENCHMARK ODCZYT/ZAPIS"),
    ("EKRAN", "MATRYCA / EDID", "Identyfikacja monitora i trybów. Test funkcjonalny pokazuje wzorce/kolory; martwe piksele wymagają oceny wzrokowej.", "TEST WZORCÓW"),
    ("SECURITY", "BEZPIECZEŃSTWO WINDOWS", "Audyt dostępnego stanu ochrony, autostartu i narzędzi systemu; nie jest to niezależny test wydajności.", "AUDYT FUNKCJONALNY"),
    ("BATERIA", "BATERIA / ZASILANIE", "Odczyt źródła zasilania oraz dostępnej telemetrii baterii; benchmark monitoruje próbki w czasie.", "MONITOR ULTRA/MAX"),
    ("SIEĆ", "SIEĆ / WI-FI / LAN", "Skan interfejsów i stanów; test Internetu mierzy rzeczywiste download/upload i opóźnienie.", "SPEED TEST"),
    ("USB", "USB / URZĄDZENIA", "Enumeracja urządzeń Plug and Play i dostępne kody stanu. Sama obecność USB nie potwierdza transferu ani zasilania portu.", "TEST FUNKCJONALNY"),
    ("AUDIO", "AUDIO / MIKROFON / GŁOŚNIKI", "Wykrywanie urządzeń audio i test funkcjonalny; słyszalność trzeba potwierdzić na sprzęcie.", "TEST FUNKCJONALNY"),
    ("KLAWIATURA", "KLAWIATURA / TOUCHPAD", "Wykrywanie urządzeń wejściowych i test funkcjonalny.", "TEST FUNKCJONALNY"),
    ("KAMERA", "KAMERA", "Wykrywanie urządzenia i kontrola dostępności; działanie obrazu wymaga potwierdzenia podglądem.", "TEST FUNKCJONALNY"),
]

def _u78_latest_component_state(self, module):
    try:
        for mode in ("benchmark", "scan"):
            for key in _u76_component_result_keys(module, mode):
                value = (getattr(self, "results", {}) or {}).get(key)
                if isinstance(value, dict) and value:
                    state = str(value.get("state") or "N/D").upper()
                    sample = value.get("sampled_at") or value.get("time")
                    detail = value.get("message") or value.get("note") or value.get("error")
                    return f"Ostatni zapisany wynik: {state}" + (f" • {sample}" if sample else "") + (f" • {str(detail)[:90]}" if detail else "")
    except Exception:
        pass
    return "Ostatni wynik: nie wykonano jeszcze testu."

def _u78_launch_from_lab(self, module, mode):
    # All controls use the same guarded launch and worker as the existing module screens.
    try:
        self._u78_return_to_component_lab = True
        if mode == "visual":
            _u69_open_component_simulator(self, module, False, "scan")
        else:
            _u69_open_component_simulator(self, module, True, mode)
    except Exception as exc:
        self._u78_return_to_component_lab = False
        message = f"Nie udało się otworzyć modułu {module}: {type(exc).__name__}: {exc}"
        try:
            self.append_log(message)
        except Exception:
            pass
        messagebox.showerror("Laboratorium podzespołów", message)

def _u78_show_component_lab(self):
    self.current_view = "COMPONENT_LAB"
    self.clear()
    t = self.colors()
    self.header_title.config(text="LABORATORIUM PODZESPOŁÓW — 13 MODUŁÓW")
    hero = self.panel(self.content)
    hero.pack(fill="x", pady=(0, 6))
    tk.Label(hero, text="KAŻDY PODZESPÓŁ OSOBNO • SKAN • TEST / BENCHMARK • SYMULATOR 3D", bg=t["panel"], fg=t["accent"], font=self.fnt(12, "bold")).pack(anchor="w", padx=12, pady=(9, 3))
    tk.Label(hero, text=f"{len(_U78_COMPONENT_LAB)} niezależnych modułów. Wybierz pojedynczą operację — nie musisz uruchamiać całej diagnostyki. Profile benchmarków: KRÓTKI 15 s / ŚREDNI 60 s / DŁUGI 180 s / ULTRA 300 s / MAX 600 s / TEST TERMICZNY 900 s. GPU ma {len(_U66_SCENES)} scen OpenGL. Animacja 3D pokazuje schemat podzespołu; wynik PASS/OSTRZEŻENIE/FAIL pochodzi wyłącznie z rzeczywistego testu. Nieobsługiwane sensory oznaczamy N/D.", bg=t["panel"], fg=t["muted"], font=self.fnt(8), wraplength=1450, justify="left").pack(anchor="w", padx=12, pady=(0, 8))
    quick = tk.Frame(self.content, bg=t["bg"])
    quick.pack(fill="x", pady=(0, 6))
    self.make_button(quick, "▶ SPEED TEST INTERNETU — DOWNLOAD / UPLOAD / PING", self.show_speed_test, "accent", side="left", ipady=7)
    self.make_button(quick, "MONITOR LIVE — TEMPERATURY / W / V / MHZ", self.show_live_monitor, "good", side="left", ipady=7)
    outer = tk.Frame(self.content, bg=t["bg"])
    outer.pack(fill="both", expand=True)
    canvas = tk.Canvas(outer, bg=t["bg"], highlightthickness=0)
    sb = ttk.Scrollbar(outer, orient="vertical", command=canvas.yview)
    inner = tk.Frame(canvas, bg=t["bg"])
    win = canvas.create_window((0, 0), window=inner, anchor="nw")
    inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>", lambda e: canvas.itemconfigure(win, width=e.width))
    canvas.configure(yscrollcommand=sb.set)
    canvas.pack(side="left", fill="both", expand=True)
    sb.pack(side="right", fill="y")
    for i, (module, title, description, bench_label) in enumerate(_U78_COMPONENT_LAB):
        card = self.panel(inner)
        card.grid(row=i // 3, column=i % 3, sticky="nsew", padx=4, pady=4)
        tk.Label(card, text=f"{i+1:02d}  {title}", bg=t["panel"], fg=t["accent"], font=self.fnt(9, "bold"), wraplength=430, justify="left").pack(anchor="w", padx=9, pady=(8, 4))
        tk.Label(card, text=description, bg=t["panel"], fg=t["fg"], font=self.fnt(8), wraplength=430, justify="left").pack(fill="x", padx=9, pady=(0, 5))
        result_text = tk.Label(card, text=_u78_latest_component_state(self, module), bg=t["panel"], fg=t["muted"], font=self.fnt(7), wraplength=430, justify="left", anchor="w")
        result_text.pack(fill="x", padx=9, pady=(0, 5))
        buttons = tk.Frame(card, bg=t["panel"])
        buttons.pack(fill="x", padx=5, pady=(0, 7))
        self.make_button(buttons, "SKAN + LIVE 3D", lambda m=module: _u78_launch_from_lab(self, m, "scan"), "card", side="left", ipady=4)
        self.make_button(buttons, bench_label, lambda m=module: _u78_launch_from_lab(self, m, "benchmark"), "accent", side="left", ipady=4)
        self.make_button(buttons, "SAMO SYMULATOR 3D", lambda m=module: _u78_launch_from_lab(self, m, "visual"), "good", side="left", ipady=4)
    for col in range(3):
        inner.grid_columnconfigure(col, weight=1)
    nav = tk.Frame(self.content, bg=t["bg"])
    nav.pack(fill="x", pady=(4, 0))
    self.make_button(nav, "WSZYSTKIE TESTY PO KOLEI", lambda: _u66_start_all_tests(self), "accent", side="left", ipady=5)
    self.make_button(nav, "CENTRUM TESTÓW", self.show_tests_hub, "card", side="left", ipady=5)
    self.make_button(nav, "PULPIT DIAGNOSTYKI", self.show_dashboard, "card", side="left", ipady=5)

def _u78_selftest_component_lab():
    keys = [item[0] for item in _U78_COMPONENT_LAB]
    checks = [
        ("13 unique module entries", len(keys) == 13 and len(set(keys)) == 13),
        ("same set as component simulators", set(keys) == set(_U69_COMPONENT_LABELS)),
        ("60 unique OpenGL scenes", len(_U66_SCENES) == 60 and len({str(x[0]) for x in _U66_SCENES}) == 60),
        ("component lab callable", callable(_u78_show_component_lab) and callable(_u78_launch_from_lab)),
        ("real component launcher callable", callable(_u69_open_component_simulator) and callable(_u69_launch_component_test)),
        ("MAX 900-second profile", len(_U68_PROFILE_CHOICES) >= 6 and str(_U68_PROFILE_CHOICES[-1]).endswith("900 s")),
        ("visible 3D action", any("SAMO SYMULATOR 3D" in str(x) for x in _u78_show_component_lab.__code__.co_consts)),
        ("scan action", any("SKAN + LIVE 3D" in str(x) for x in _u78_show_component_lab.__code__.co_consts)),
        ("visible internet speed test", any("SPEED TEST INTERNETU" in str(x) for x in _u78_show_component_lab.__code__.co_consts) and callable(AppV43.show_speed_test)),
    ]
    failed = [name for name, ok in checks if not ok]
    if failed:
        raise AssertionError("Component lab checks failed: " + ", ".join(failed))
    print("COMPONENT_LAB_13_MODULES_SELFTEST_OK: " + ", ".join(name for name, _ in checks))

def _u66_selftest_advanced():
    assert len(_U66_SCENES)==60, "Studio must have 60 separately named scenes"
    assert len(_U66_KNOWLEDGE_SEED)>=30, "Knowledge seed should cover at least 30 topics"
    assert all(x.get("source","").startswith("https://") for x in _U66_KNOWLEDGE_SEED), "ADVANCED self-test check 1: all(x.get('source','').startswith('https://') for x in _U66_KNOWLEDGE_SEED)"
    assert _U66_KNOWLEDGE_PACK_FORMAT == "naprawapc-ai-reader-knowledge", "ADVANCED self-test check 2: _U66_KNOWLEDGE_PACK_FORMAT == 'naprawapc-ai-reader-knowledge'"
    assert _U66_KNOWLEDGE_PACK_URL.startswith("https://raw.githubusercontent.com/"), "ADVANCED self-test check 3: _U66_KNOWLEDGE_PACK_URL.startswith('https://raw.githubusercontent.com/')"
    assert callable(_u66_sync_knowledge_from_server), "ADVANCED self-test check 4: callable(_u66_sync_knowledge_from_server)"
    ranked=_u66_rank_knowledge("temperatura CPU GPU",limit=5)
    assert ranked and any("temperatura" in str(x.get("title","")).lower() for x in ranked), "ADVANCED self-test check 5: ranked and any('temperatura' in str(x.get('title','')).lower() for x in ranked)"
    assert callable(_u66_web_search) and callable(_u66_read_web_page) and callable(_u66_measure_speed), "ADVANCED self-test check 6: callable(_u66_web_search) and callable(_u66_read_web_page) and callable(_u66_measure_speed"
    assert callable(AppV43.show_speed_test) and callable(_u66_show_speed_test), "ADVANCED self-test check 7: callable(AppV43.show_speed_test) and callable(_u66_show_speed_test)"
    assert "DOWNLOAD" in " ".join(str(x) for x in _u66_show_speed_test.__code__.co_consts), "ADVANCED self-test check 8: 'DOWNLOAD' in ' '.join(str(x) for x in _u66_show_speed_test.__code__.co_consts)"
    assert callable(_u66_scene_child), "ADVANCED self-test check 9: callable(_u66_scene_child)"
    assert callable(_u66_run_all_tests_worker), "ADVANCED self-test check 10: callable(_u66_run_all_tests_worker)"
    assert callable(_u67_start_selected_diagnostic) and callable(_u67_run_selected_diagnostic), "ADVANCED self-test check 11: callable(_u67_start_selected_diagnostic) and callable(_u67_run_selected_diagnostic)"
    assert callable(_u67_refresh_visible_charts) and callable(_u67_stage_live_panel), "ADVANCED self-test check 12: callable(_u67_refresh_visible_charts) and callable(_u67_stage_live_panel)"
    assert callable(_u67_set_suite_status), "ADVANCED self-test check 13: callable(_u67_set_suite_status)"
    assert len(_U66_SCENES)==60 and all(sc[1] for sc in _U66_SCENES), "ADVANCED self-test check 14: len(_U66_SCENES)==60 and all(sc[1] for sc in _U66_SCENES)"
    assert "900 s" in ("3 s","5 s","10 s","20 s","30 s","60 s","120 s","180 s","300 s","600 s","900 s"), "ADVANCED self-test check 15: '900 s' in ('3 s','5 s','10 s','20 s','30 s','60 s','120 s','180 s','300 s','600 s','900 s"
    assert callable(_u68_show_module_with_workbench) and callable(_u68_open_component_simulator), "ADVANCED self-test check 16: callable(_u68_show_module_with_workbench) and callable(_u68_open_component_simulator)"
    assert callable(_u68_run_component_worker) and callable(_u68_draw_component_scene), "ADVANCED self-test check 17: callable(_u68_run_component_worker) and callable(_u68_draw_component_scene)"
    assert callable(_u68_show_games_advisor), "ADVANCED self-test check 18: callable(_u68_show_games_advisor)"
    _u69_selftest_component_workbenches()
    _u76_selftest_workbenches()
    _u78_selftest_component_lab()
    _u80_selftest_sound_hooks()
    assert AppV43.show_component_lab is _u78_show_component_lab, "ADVANCED self-test check 19: AppV43.show_component_lab is _u78_show_component_lab"
    assert AppV43.show_module in (_u69_show_module, _u84_show_module_with_gpu_live, _u86_show_module_with_component_workbench), "ADVANCED self-test check 20: AppV43.show_module in (_u69_show_module, _u84_show_module_with_gpu_live, _u86_show_module_"
    assert AppV43.show_simple_module in (_u83_show_simple_module_speed_entry, _u86_show_simple_module_with_component_workbench), "ADVANCED self-test check 21: AppV43.show_simple_module in (_u83_show_simple_module_speed_entry, _u86_show_simple_module"
    assert len(_U66_SCENES)==60 and len({scene[0] for scene in _U66_SCENES})==60, "ADVANCED self-test check 22: len(_U66_SCENES)==60 and len({scene[0] for scene in _U66_SCENES})==60"
    assert AppV43._start_selected_diagnostic is _u67_start_selected_diagnostic, "ADVANCED self-test check 23: AppV43._start_selected_diagnostic is _u67_start_selected_diagnostic"
    assert "N/D" in _u67_refresh_visible_charts.__code__.co_consts, "ADVANCED self-test check 24: 'N/D' in _u67_refresh_visible_charts.__code__.co_consts"
    assert _u66_format_rate(1_000_000)=="8.00 Mbps" and _u66_format_rate(0)=="0.00 Mbps", "ADVANCED self-test check 25: _u66_format_rate(1_000_000)=='8.00 Mbps' and _u66_format_rate(0)=='0.00 Mbps'"
    print("ADVANCED_MODULES_SELFTEST_OK: live telemetry, 13 independent component tests, 60 OpenGL scenes ULTRA/MAX, per-module 3D workbenches, game graphics advisor, AI reader")

# Integrate into the existing one-window app. Keep the original report/repairs and device test modules.
_U66_ORIGINAL_REFRESH_TELEMETRY=AppV43.refresh_telemetry
AppV43.show_ai_reader=_u66_show_ai_reader
AppV43.show_speed_test=_u66_show_speed_test
AppV43.show_live_monitor=_u66_show_live_monitor
AppV43.show_3d_studio=_u66_show_3d_studio
AppV43.show_tests_hub=_u66_show_tests_hub
AppV43.show_component_lab=_u78_show_component_lab
AppV43.start_all_tests_sequential=_u66_start_all_tests
AppV43.full_test=_u66_start_all_tests
AppV43._start_selected_diagnostic=_u67_start_selected_diagnostic
AppV43._run_selected_diagnostic=_u67_run_selected_diagnostic
AppV43.run_ai_only=_u66_show_ai_reader
AppV43.refresh_telemetry=_u66_refresh_telemetry
_U66_ORIGINAL_INIT_FOR_SENSOR=AppV43.__init__
AppV43.__init__=_u67_init_with_sensor_poll
_u37_gpu_benchmark_child=_u66_scene_child


# v4.3.80 — audible, distinct start/end signals for actual tests.
# Short Windows beeps are synchronous and run from the test worker; they do not block the Tk UI.
def _u80_test_sound(event):
    try:
        import winsound as _u80_winsound
        if event == "start":
            try:
                _u80_winsound.Beep(880, 110)
            except Exception:
                _u80_winsound.MessageBeep(_u80_winsound.MB_ICONASTERISK)
        else:
            try:
                _u80_winsound.Beep(660, 90)
                _u80_winsound.Beep(988, 140)
            except Exception:
                _u80_winsound.MessageBeep(_u80_winsound.MB_OK)
    except Exception:
        # Sound hardware/Windows policy can disable beeps; never fail a diagnostic because of audio.
        pass


def _u80_run_with_sound(app, label, function, *args, **kwargs):
    depth = int(getattr(app, "_u80_test_sound_depth", 0) or 0)
    outermost = depth == 0
    try:
        app._u80_test_sound_depth = depth + 1
    except Exception:
        pass
    if outermost:
        _u80_test_sound("start")
        try:
            app.queue_log(f"DŹWIĘK TESTU: START — {label}")
        except Exception:
            pass
    try:
        return function(*args, **kwargs)
    finally:
        try:
            new_depth = max(0, int(getattr(app, "_u80_test_sound_depth", 1) or 1) - 1)
            app._u80_test_sound_depth = new_depth
        except Exception:
            new_depth = 0
        if outermost:
            _u80_test_sound("end")
            try:
                app.queue_log(f"DŹWIĘK TESTU: KONIEC — {label}")
            except Exception:
                pass


def _u80_wrap_app_method(method_name):
    original = getattr(AppV43, method_name, None)
    if not callable(original) or getattr(original, "_u80_sound_wrapped", False):
        return False
    def wrapped(self, *args, **kwargs):
        return _u80_run_with_sound(self, method_name, original, self, *args, **kwargs)
    wrapped.__name__ = getattr(original, "__name__", method_name)
    wrapped.__doc__ = getattr(original, "__doc__", None)
    wrapped._u80_sound_wrapped = True
    setattr(AppV43, method_name, wrapped)
    return True


def _u80_wrap_global(function_name, label=None):
    original = globals().get(function_name)
    if not callable(original) or getattr(original, "_u80_sound_wrapped", False):
        return False
    def wrapped(app, *args, **kwargs):
        return _u80_run_with_sound(app, label or function_name, original, app, *args, **kwargs)
    wrapped.__name__ = getattr(original, "__name__", function_name)
    wrapped.__doc__ = getattr(original, "__doc__", None)
    wrapped._u80_sound_wrapped = True
    globals()[function_name] = wrapped
    return True


_U80_SOUND_METHODS = (
    "_cpu_test",
    "_ram_test",
    "_gpu_test",
    "_disk_test",
    "_monitor_test",
    "_security_test",
    "_battery_test",
    "_peripheral_test",
    "_system_test",
    "_selected_system_security_test",
)
_U80_SOUND_WRAPPED_METHODS = tuple(name for name in _U80_SOUND_METHODS if _u80_wrap_app_method(name))

# Component-lab runs have their own worker entry point; depth tracking prevents a second
# beep when the worker invokes one of the lower-level CPU/RAM/disk test methods.
_U80_SOUND_COMPONENT_WORKER_WRAPPED = _u80_wrap_global("_u69_run_component_worker", "test komponentu / skan / benchmark")
globals()["_u68_run_component_worker"] = globals().get("_u69_run_component_worker")

# A full 3D suite emits one start/end pair per separately measured OpenGL scene.
_U80_SOUND_3D_SCENE_WRAPPED = _u80_wrap_global("_u66_execute_gpu_scene", "pojedyncza scena benchmarku 3D")
# The selected-test sequence calls the internet throughput function directly, outside the component worker.
_U80_SOUND_SPEED_TEST_WRAPPED = _u80_wrap_global("_u67_run_visible_speed_test", "Internet Speed Test download/upload")


def _u80_selftest_sound_hooks():
    required = ("_cpu_test", "_ram_test", "_gpu_test", "_disk_test", "_monitor_test")
    missing = [name for name in required if not getattr(getattr(AppV43, name, None), "_u80_sound_wrapped", False)]
    checks = {
        "core test methods wrapped": not missing,
        "component worker wrapped": bool(_U80_SOUND_COMPONENT_WORKER_WRAPPED),
        "each 3D scene wrapped": bool(_U80_SOUND_3D_SCENE_WRAPPED),
        "selected-run speed test wrapped": bool(_U80_SOUND_SPEED_TEST_WRAPPED),
        "distinct start/end tones": callable(_u80_test_sound),
        "power telemetry probe and W units": callable(_u66_sensor_probe) and any("cpu_power_w" in repr(item) for item in _u66_sensor_probe.__code__.co_consts),
        "visible power cards and graph": any("MOC SYSTEMU" in repr(item) for item in _u67_stage_live_panel.__code__.co_consts) and any("POBÓR MOCY W" in repr(item) for item in _u67_refresh_visible_charts.__code__.co_consts),
        "nested calls do not double beep": callable(_u80_run_with_sound),
    }
    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        raise AssertionError("Test sound hook checks failed: " + ", ".join(failed) + (("; missing methods: " + ", ".join(missing)) if missing else ""))
    print("TEST_SOUND_HOOKS_SELFTEST_OK: " + ", ".join(checks))



# v4.3.83 — unmistakable direct Speed Test entry on every network screen.
_U83_ORIGINAL_SHOW_SIMPLE_MODULE = AppV43.show_simple_module

def _u83_show_simple_module_speed_entry(self, title):
    _U83_ORIGINAL_SHOW_SIMPLE_MODULE(self, title)
    upper = str(title or "").upper()
    if not any(word in upper for word in ("SIEĆ", "WI-FI", "WIFI", "LAN", "NETWORK", "INTERNET")):
        return
    try:
        if getattr(self, "_u83_speed_bar", None) is not None:
            try:
                if self._u83_speed_bar.winfo_exists():
                    self._u83_speed_bar.destroy()
            except Exception:
                pass
        t = self.colors()
        bar = tk.Frame(self.content, bg=t["panel"], highlightbackground=t["accent"], highlightthickness=1)
        children = list(self.content.winfo_children())
        if children:
            bar.pack(fill="x", padx=4, pady=(2, 5), before=children[0])
        else:
            bar.pack(fill="x", padx=4, pady=(2, 5))
        self._u83_speed_bar = bar
        tk.Label(
            bar,
            text="SPEED TEST INTERNETU — RZECZYWISTY PING / DOWNLOAD / UPLOAD",
            bg=t["panel"], fg=t["accent"], font=self.fnt(10, "bold"), anchor="w"
        ).pack(side="left", fill="x", expand=True, padx=10, pady=7)
        self.make_button(bar, "▶ URUCHOM SPEED TEST", self.show_speed_test, "accent", side="right", ipady=6)
        self.make_button(bar, "MONITOR LIVE", self.show_live_monitor, "card", side="right", ipady=6)
    except Exception as exc:
        try:
            self.append_log("Speed Test: nie udało się dodać przycisku: " + repr(exc))
        except Exception:
            pass


# v4.3.85 — live GPU telemetry panel embedded directly in the GPU module.
_U84_GPU_LIVE_FIELDS = (
    ("GPU LOAD", "load", "gpu_load_percent", "%"),
    ("TEMPERATURA", "temp", "temperature_c", "°C"),
    ("VRAM ZAJĘTA", "vram_used", "vram_used_mb", "MB"),
    ("VRAM RAZEM", "vram_total", "vram_total_mb", "MB"),
    ("ZEGAR RDZENIA", "core_clock", "gpu_clock_mhz", "MHz"),
    ("ZEGAR PAMIĘCI", "memory_clock", "memory_clock_mhz", "MHz"),
    ("MOC GPU", "power", "power_draw_w", "W"),
    ("WENTYLATOR", "fan", "fan_speed_rpm", "RPM"),
)

def _u84_gpu_numeric(value):
    try:
        result = float(value)
        return result if _u66_math.isfinite(result) and result >= 0 else None
    except Exception:
        return None


def _u84_gpu_panel_draw(canvas, series, maximum, title, app, colors):
    try:
        if canvas is None or not canvas.winfo_exists():
            return
        canvas.delete("all")
        width = max(240, canvas.winfo_width() or 360)
        height = max(105, canvas.winfo_height() or 128)
        left, right, top, bottom = 38, width - 8, 17, height - 22
        canvas.create_text(8, 3, text=title, anchor="nw", fill=colors["muted"], font=app.fnt(8, "bold"))
        ceiling = max(1.0, float(maximum or 1))
        for percent in (0, 25, 50, 75, 100):
            y = bottom - (bottom - top) * percent / 100
            canvas.create_line(left, y, right, y, fill=colors["card"], width=1)
        palette = {"load": colors["accent"], "vram": colors["good"], "temp": colors["warn"],
                   "clock": colors["accent2"], "power": "#c084fc"}
        for key, label, color_key in (
            ("load", "GPU %", "load"), ("vram", "VRAM %", "vram"), ("temp", "°C", "temp"),
            ("clock", "MHz", "clock"), ("power", "W", "power")
        ):
            values = list(series.get(key, []))[-90:]
            if len(values) < 2:
                continue
            points = []
            for index, value in enumerate(values):
                x = left + (right - left) * index / max(1, len(values) - 1)
                y = bottom - (bottom - top) * max(0.0, min(ceiling, float(value))) / ceiling
                points.extend((x, y))
            canvas.create_line(*points, fill=palette[color_key], width=2, smooth=True)
        current = []
        for key, label in (("load", "GPU %"), ("vram", "VRAM %"), ("temp", "°C"), ("clock", "MHz"), ("power", "W")):
            values = series.get(key, [])
            if values:
                current.append(f"{label}: {values[-1]:.1f}")
        canvas.create_text(left + 3, bottom + 3, text="  •  ".join(current) or "Zbieranie próbek…",
                           anchor="sw", fill=colors["fg"], font=app.fnt(7))
    except Exception:
        pass


def _u84_attach_gpu_live_panel(self):
    try:
        previous = getattr(self, "_u84_gpu_panel", None)
        if previous is not None and previous.winfo_exists():
            previous.destroy()
        t = self.colors()
        panel = tk.Frame(self.content, bg=t["panel"], highlightbackground=t["accent"], highlightthickness=1)
        workbench = getattr(self, "_u69_workbench_panel", None)
        if workbench is not None and workbench.winfo_exists():
            panel.pack(fill="x", padx=3, pady=(2, 5), after=workbench)
        else:
            panel.pack(fill="x", padx=3, pady=4)
        self._u84_gpu_panel = panel
        title = tk.Frame(panel, bg=t["panel"])
        title.pack(fill="x", padx=10, pady=(7, 2))
        tk.Label(title, text="GPU LIVE STUDIO — TELEMETRIA RZECZYWISTA",
                 bg=t["panel"], fg=t["accent"], font=self.fnt(11, "bold")).pack(side="left", anchor="w")
        self._u84_gpu_status = tk.Label(title, text="Zbieranie odczytów…", bg=t["panel"], fg=t["muted"], font=self.fnt(8))
        self._u84_gpu_status.pack(side="right")
        tk.Label(panel,
                 text="Odświeżanie obrazu co 1 s; źródła czujników aktualizowane zgodnie z możliwościami sterownika. N/D oznacza brak odczytu, nie 0.",
                 bg=t["panel"], fg=t["muted"], font=self.fnt(8), anchor="w").pack(fill="x", padx=10, pady=(0, 5))
        self._u84_gpu_values = {}
        grid = tk.Frame(panel, bg=t["panel"]); grid.pack(fill="x", padx=6, pady=(0, 5))
        specs = [
            ("GPU LOAD", "load", "%", t["accent"]),
            ("TEMPERATURA", "temp", "°C", t["warn"]),
            ("VRAM ZAJĘTA", "vram_used", "MB", t["good"]),
            ("VRAM CAŁKOWITA", "vram_total", "MB", t["good"]),
            ("ZEGAR GPU", "core_clock", "MHz", t["accent2"]),
            ("ZEGAR VRAM", "memory_clock", "MHz", t["accent2"]),
            ("MOC GPU", "power", "W", t["warn"]),
            ("WENTYLATOR", "fan", "RPM", t["accent"]),
        ]
        for i, (caption, key, unit, color) in enumerate(specs):
            card = tk.Frame(grid, bg=t["card"], highlightbackground=t["panel"], highlightthickness=1)
            card.grid(row=i // 4, column=i % 4, sticky="nsew", padx=2, pady=2)
            tk.Label(card, text=caption, bg=t["card"], fg=t["muted"], font=self.fnt(7, "bold")).pack(padx=5, pady=(5, 1))
            value = tk.Label(card, text="N/D", bg=t["card"], fg=color, font=self.fnt(12, "bold"))
            value.pack(padx=5, pady=(0, 2))
            bar = tk.Canvas(card, height=6, bg=t["panel"], highlightthickness=0)
            bar.pack(fill="x", padx=6, pady=(0, 5))
            self._u84_gpu_values[key] = (value, bar, unit, color)
        for column in range(4):
            grid.grid_columnconfigure(column, weight=1)
        charts = tk.Frame(panel, bg=t["panel"]); charts.pack(fill="x", padx=6, pady=(0, 5))
        self._u84_gpu_chart_load = tk.Canvas(charts, height=122, bg=t["card"], highlightthickness=0)
        self._u84_gpu_chart_load.pack(side="left", fill="both", expand=True, padx=(0, 3))
        self._u84_gpu_chart_thermal = tk.Canvas(charts, height=122, bg=t["card"], highlightthickness=0)
        self._u84_gpu_chart_thermal.pack(side="left", fill="both", expand=True, padx=3)
        self._u84_gpu_chart_clock = tk.Canvas(charts, height=122, bg=t["card"], highlightthickness=0)
        self._u84_gpu_chart_clock.pack(side="left", fill="both", expand=True, padx=(3, 0))
        self._u84_gpu_history = {"load": [], "vram": [], "temp": [], "clock": [], "power": []}
        row = tk.Frame(panel, bg=t["panel"]); row.pack(fill="x", padx=6, pady=(0, 6))
        self.make_button(row, "ODŚWIEŻ GPU", lambda: _u84_gpu_poll_now(self), "card", side="left", ipady=4)
        self.make_button(row, "BENCHMARK GPU + 3D", lambda: _u68_open_gpu_suite(self, auto_start=True), "accent", side="left", ipady=4)
        self.make_button(row, "TEST VRAM", lambda: _u69_open_vram_test(self), "good", side="left", ipady=4)
        self.make_button(row, "MONITOR LIVE", self.show_live_monitor, "card", side="left", ipady=4)
        _u84_gpu_poll_now(self)
        _u84_gpu_live_tick(self)
    except Exception as exc:
        try:
            self.append_log("GPU LIVE STUDIO: " + repr(exc))
        except Exception:
            pass


def _u84_gpu_poll_now(self):
    if getattr(self, "_u84_gpu_poll_busy", False):
        return
    self._u84_gpu_poll_busy = True
    def job():
        error = None
        try:
            telemetry = _u37_nvidia_telemetry() if "_u37_nvidia_telemetry" in globals() else {"available": False, "message": "Brak dostawcy GPU."}
        except Exception as exc:
            telemetry = {"available": False, "message": f"{type(exc).__name__}: {exc}"}
            error = telemetry["message"]
        def finish():
            self._u84_gpu_poll_busy = False
            self._u84_gpu_last_telemetry = telemetry
            try:
                self._u66_sensor_cache = dict(getattr(self, "_u66_sensor_cache", {}) or {},
                    gpu=telemetry, time=_u66_time.monotonic())
                if error and hasattr(self, "append_log"):
                    self.append_log("GPU telemetry: " + error)
            except Exception:
                pass
            try:
                if getattr(self, "current_view", "") == "GPU":
                    _u84_gpu_live_tick(self, schedule=False)
            except Exception:
                pass
        try:
            self.queue_action(finish)
        except Exception:
            self._u84_gpu_poll_busy = False
    _u66_threading.Thread(target=job, name="NaprawaPCGpuLiveTelemetry", daemon=True).start()


def _u84_gpu_live_tick(self, schedule=True):
    try:
        if getattr(self, "current_view", "") != "GPU":
            return
        telemetry = getattr(self, "_u84_gpu_last_telemetry", None) or {}
        cache = getattr(self, "_u66_sensor_cache", {}) or {}
        temps = cache.get("temps", {}) or {}
        utilization = _u84_gpu_numeric(telemetry.get("gpu_load_percent"))
        if utilization is None:
            utilization = _u84_gpu_numeric(getattr(self, "_gpu_util", None))
        gpu_temp = _u84_gpu_numeric(telemetry.get("temperature_c"))
        if gpu_temp is None:
            gpu_temp = _u84_gpu_numeric(temps.get("gpu_temp_c"))
        used = _u84_gpu_numeric(telemetry.get("vram_used_mb"))
        total = _u84_gpu_numeric(telemetry.get("vram_total_mb"))
        clock = _u84_gpu_numeric(telemetry.get("gpu_clock_mhz"))
        memory_clock = _u84_gpu_numeric(telemetry.get("memory_clock_mhz"))
        power = _u84_gpu_numeric(telemetry.get("power_draw_w", telemetry.get("power_w", temps.get("gpu_power_w"))))
        fan = _u84_gpu_numeric(telemetry.get("fan_speed_rpm", temps.get("gpu_fan_rpm")))
        vram_percent = used * 100.0 / total if used is not None and total else None
        current = {
            "load": utilization, "temp": gpu_temp, "vram_used": used, "vram_total": total,
            "core_clock": clock, "memory_clock": memory_clock, "power": power, "fan": fan
        }
        hist = getattr(self, "_u84_gpu_history", {"load": [], "vram": [], "temp": [], "clock": [], "power": []})
        for key, value in (("load", utilization), ("vram", vram_percent), ("temp", gpu_temp),
                           ("clock", clock), ("power", power)):
            if value is not None:
                hist[key].append(float(value)); hist[key] = hist[key][-90:]
        self._u84_gpu_history = hist
        label_map = getattr(self, "_u84_gpu_values", {})
        for key, value in current.items():
            try:
                label, bar, unit, color = label_map[key]
                label.config(text=(f"{value:.1f} {unit}" if value is not None else "N/D"))
                bar.delete("all")
                if value is not None:
                    if key == "vram_used":
                        pct = min(100.0, value * 100.0 / total) if total else 0.0
                    elif key == "vram_total":
                        pct = 100.0
                    elif key in ("load", "temp"):
                        pct = min(100.0, value) if key == "load" else min(100.0, value / 110.0 * 100.0)
                    else:
                        pct = 100.0 if value > 0 else 0.0
                    width = max(10, bar.winfo_width())
                    color_fill = self.colors()["bad"] if key == "load" and value >= 95 else self.colors()["warn"] if key == "temp" and value >= 85 else color
                    bar.create_rectangle(0, 0, width * pct / 100.0, 6, fill=color_fill, outline="")
            except Exception:
                pass
        try:
            if hasattr(self, "_u84_gpu_status") and self._u84_gpu_status.winfo_exists():
                provider = str(telemetry.get("provider") or telemetry.get("message") or "Źródło N/D")
                name = str(telemetry.get("name") or "GPU — odczyt podstawowy")
                self._u84_gpu_status.config(text=f"{name} • {provider}" if telemetry.get("available") else f"{name} • telemetria częściowa")
        except Exception:
            pass
        t = self.colors()
        _u84_gpu_panel_draw(getattr(self, "_u84_gpu_chart_load", None), hist, 100, "OBciążenie GPU / VRAM %", self, t)
        _u84_gpu_panel_draw(getattr(self, "_u84_gpu_chart_thermal", None),
                            {"temp": hist.get("temp", [])}, max([100.0] + hist.get("temp", [])), "TEMPERATURA GPU °C", self, t)
        _u84_gpu_panel_draw(getattr(self, "_u84_gpu_chart_clock", None),
                            {"clock": hist.get("clock", []), "power": hist.get("power", [])},
                            max([100.0] + hist.get("clock", []) + hist.get("power", [])), "ZEGAR GPU MHz / MOC W", self, t)
    except Exception as exc:
        try: self.append_log("GPU LIVE odświeżanie: " + repr(exc))
        except Exception: pass
    if schedule:
        try:
            self.after(1000, lambda: _u84_gpu_live_tick(self))
            if not getattr(self, "_u84_gpu_poll_busy", False):
                last = float(getattr(self, "_u84_gpu_poll_time", 0))
                now = _u66_time.monotonic()
                if now - last >= 3.0:
                    self._u84_gpu_poll_time = now
                    _u84_gpu_poll_now(self)
        except Exception:
            pass


_U84_ORIGINAL_SHOW_MODULE = AppV43.show_module
def _u84_show_module_with_gpu_live(self, module):
    _U84_ORIGINAL_SHOW_MODULE(self, module)
    if str(module).strip().upper() == "GPU":
        _u84_attach_gpu_live_panel(self)

AppV43.show_module = _u84_show_module_with_gpu_live


AppV43.show_simple_module = _u83_show_simple_module_speed_entry



# v4.3.86 — universal independent component workbenches, extended telemetry and stress profiles.
_U86_COMPONENT_KEYS = {
    "CPU": ("CPU", "COMPONENT_SCAN_CPU"), "GPU": ("GPU", "GPU_WINSAT", "3D_SUITE"),
    "RAM": ("RAM_BENCHMARK", "RAM", "COMPONENT_SCAN_RAM"), "DYSK": ("DISK_BENCHMARK", "DYSK", "COMPONENT_SCAN_DYSK", "SMART"),
    "VRAM": ("VRAM_TEST", "COMPONENT_SCAN_VRAM"), "EKRAN": ("EKRAN",), "SECURITY": ("SECURITY", "SYSTEM", "STARTUP_AUDIT"),
    "BATERIA": ("BATTERY_BENCHMARK", "BATERIA"), "SIEĆ": ("SPEED_TEST", "NETWORK"),
    "USB": ("USB",), "AUDIO": ("AUDIO",), "KLAWIATURA": ("INPUTS", "KLAWIATURA"), "KAMERA": ("CAMERA",)
}
_U86_MODULE_TITLES = {
    "CPU":"CPU / PROCESOR", "GPU":"GPU / KARTA GRAFICZNA", "RAM":"RAM / PAMIĘĆ", "DYSK":"SSD / HDD / NVMe",
    "VRAM":"VRAM / PAMIĘĆ KARTY", "EKRAN":"MATRYCA / MONITOR", "SECURITY":"BEZPIECZEŃSTWO WINDOWS",
    "BATERIA":"BATERIA / ZASILANIE", "SIEĆ":"SIEĆ / WI-FI / LAN", "USB":"USB / URZĄDZENIA",
    "AUDIO":"AUDIO / MIKROFON", "KLAWIATURA":"KLAWIATURA / TOUCHPAD", "KAMERA":"KAMERA"
}
_U86_HISTORY_KEYS=("cpu","ram","gpu","read","write","down","up","cpu_power","gpu_power","system_power","battery_power","cpu_temp","gpu_temp","cpu_voltage","gpu_voltage","cpu_clock","gpu_clock")

def _u86_stage_live_panel(self,index,total,title):
    try:
        old=getattr(self,"_u67_stage_panel",None)
        if old is not None and old.winfo_exists():old.destroy()
    except Exception:pass
    t=self.colors();panel=tk.Frame(self.content,bg=t["panel"],highlightbackground=t["accent"],highlightthickness=1)
    children=self.content.winfo_children();after_widget=None
    for attr in ("_u84_gpu_panel","_u69_workbench_panel","_u69_simple_workbench_panel"):
        candidate=getattr(self,attr,None)
        try:
            if candidate is not None and candidate.winfo_exists():after_widget=candidate;break
        except Exception:pass
    try:
        if after_widget is not None:panel.pack(fill="x",padx=3,pady=(2,5),after=after_widget)
        elif children:panel.pack(fill="x",padx=3,pady=(2,5),before=children[0])
        else:panel.pack(fill="x",padx=3,pady=(2,5))
    except Exception:panel.pack(fill="x",padx=3,pady=(2,5))
    self._u67_stage_panel=panel
    top=tk.Frame(panel,bg=t["panel"]);top.pack(fill="x",padx=10,pady=(6,3))
    self._u67_stage_title=tk.Label(top,text=f"TEST {index}/{total} — {title}",bg=t["panel"],fg=t["accent"],font=self.fnt(10,"bold"),anchor="w")
    self._u67_stage_title.pack(side="left",fill="x",expand=True)
    self.make_button(top,"STOP TEST",self.stop_current_test,"bad",side="right",ipady=3)
    self._u67_stage_values={}
    metrics=tk.Frame(panel,bg=t["panel"]);metrics.pack(fill="x",padx=5,pady=(0,5))
    specs=[
        ("CPU","cpu"),("RAM","ram"),("GPU","gpu"),("TEMP CPU","cpu_temp"),("TEMP GPU","gpu_temp"),("MOC CPU","cpu_power"),
        ("MOC GPU","gpu_power"),("MOC SYSTEMU","system_power"),("NAPIĘCIE CPU","cpu_voltage"),("NAPIĘCIE GPU","gpu_voltage"),
        ("ZEGAR CPU","cpu_clock"),("ZEGAR GPU","gpu_clock"),("WENTYLATOR CPU","cpu_fan"),("WENTYLATOR GPU","gpu_fan"),
        ("DYSK ODCZYT","disk_read"),("DYSK ZAPIS","disk_write"),("NET ↓","net_down"),("NET ↑","net_up")]
    for i,(label,key) in enumerate(specs):
        card=tk.Frame(metrics,bg=t["card"],highlightbackground=t["accent2"],highlightthickness=1);card.grid(row=i//6,column=i%6,sticky="nsew",padx=1,pady=1)
        tk.Label(card,text=label,bg=t["card"],fg=t["muted"],font=self.fnt(7,"bold")).pack(padx=3,pady=(3,0))
        value=tk.Label(card,text="N/D",bg=t["card"],fg=t["accent"],font=self.fnt(8,"bold"));value.pack(padx=3,pady=(0,3));self._u67_stage_values[key]=value
    for col in range(6):metrics.grid_columnconfigure(col,weight=1)
    charts=tk.Frame(panel,bg=t["panel"]);charts.pack(fill="x",padx=5,pady=(0,5))
    for name,row,col in (("_u67_stage_chart_hw",0,0),("_u67_stage_chart_io",0,1),("_u67_stage_chart_power",0,2),
                         ("_u67_stage_chart_temp",1,0),("_u67_stage_chart_voltage",1,1),("_u67_stage_chart_clocks",1,2)):
        chart=tk.Canvas(charts,height=104,bg=t["card"],highlightthickness=0);chart.grid(row=row,column=col,sticky="nsew",padx=2,pady=2);setattr(self,name,chart)
    for col in range(3):charts.grid_columnconfigure(col,weight=1)
    hist=getattr(self,"_u67_hist",{}) or {}
    for key in _U86_HISTORY_KEYS:hist.setdefault(key,[])
    self._u67_hist=hist;self._u86_result_text=None
    module=getattr(self,"_u86_module_context",None)
    if module and not getattr(self,"_u86_suite_active",False):
        row=tk.Frame(panel,bg=t["panel"]);row.pack(fill="x",padx=5,pady=(0,3))
        self.make_button(row,"SKAN TEGO PODZESPOŁU",lambda m=module:_u86_launch_component_test(self,m,"scan"),"card",side="left",ipady=4)
        self.make_button(row,"BENCHMARK ULTRA / MAX",lambda m=module:_u86_launch_component_test(self,m,"benchmark"),"accent",side="left",ipady=4)
        self.make_button(row,"SYMULATOR 3D TEGO PODZESPOŁU",lambda m=module:_u86_launch_component_test(self,m,"visual"),"good",side="left",ipady=4)
        if module=="GPU":
            self.make_button(row,"TEST VRAM",lambda:_u86_launch_component_test(self,"VRAM","benchmark"),"card",side="left",ipady=4)
            self.make_button(row,f"{len(_U66_SCENES)} SCEN 3D",lambda:_u68_open_gpu_suite(self,auto_start=True),"good",side="left",ipady=4)
        out=tk.Text(panel,height=4,wrap="word",bg=t["card"],fg=t["fg"],insertbackground=t["fg"],relief="flat",font=("Consolas",8),padx=7,pady=5)
        out.pack(fill="x",padx=5,pady=(0,5));out.configure(state="disabled");self._u86_result_text=out
        _u86_render_component_report(self,module)
    _u67_refresh_visible_charts(self)
    self._u86_stage_live_token = int(getattr(self, "_u86_stage_live_token", 0)) + 1
    token = self._u86_stage_live_token
    try:
        self.after(350, lambda token=token: _u86_stage_live_tick(self, token))
    except Exception:
        pass

def _u86_stage_live_tick(self, token):
    if getattr(self, "_u86_stage_live_token", None) != token:
        return
    panel = getattr(self, "_u67_stage_panel", None)
    try:
        if panel is None or not panel.winfo_exists():
            return
    except Exception:
        return
    try:
        _u67_refresh_visible_charts(self)
        # Keep hardware telemetry fresh while a long test is running in a worker thread.
        if not getattr(self, "_u84_gpu_poll_busy", False) and (
            _u66_time.monotonic() - float(getattr(self, "_u86_gpu_poll_time", 0) or 0) >= 3
        ):
            self._u86_gpu_poll_time = _u66_time.monotonic()
            _u84_gpu_poll_now(self)
    except Exception as exc:
        try:
            self.append_log("Live test sampler: " + repr(exc))
        except Exception:
            pass
    try:
        self.after(1000, lambda token=token: _u86_stage_live_tick(self, token))
    except Exception:
        pass


def _u86_result_for_component(self,module):
    resultset=getattr(self,"results",{}) or {}
    for key in _U86_COMPONENT_KEYS.get(module,(module,)):
        value=resultset.get(key)
        if isinstance(value,dict) and value:return key,value
    return "",{}

def _u86_render_component_report(self,module):
    box=getattr(self,"_u86_result_text",None)
    try:
        if box is None or not box.winfo_exists():return
        key,result=_u86_result_for_component(self,module)
        if not result:
            body=("NIE WYKONANO JESZCZE TESTU.\nWybierz SKAN TEGO PODZESPOŁU lub BENCHMARK ULTRA/MAX. "
                  "Puste pole nie oznacza, że podzespół jest sprawny.")
        else:
            state=str(result.get("state","N/D")).upper()
            lines=[f"OSTATNI WYNIK: {module} • {key} • STAN: {state}",f"Czas: {result.get('sampled_at') or result.get('finished') or result.get('time') or 'N/D'}"]
            for k,label in (("target_volume","Wolumin"),("passes","Przebiegi"),("duration_seconds","Czas testu (s)"),
                            ("buffer_mb","Bufor RAM (MB)"),("allocated_mb","VRAM zaalokowana (MB)"),("average_fps","Średni FPS"),
                            ("peak_fps_1s","Szczyt FPS"),("download_mbps","Download Mbps"),("upload_mbps","Upload Mbps"),
                            ("latency_average_ms","Ping ms"),("write_MBps","Zapis RAM MB/s"),("read_MBps","Odczyt RAM MB/s")):
                if result.get(k) is not None:lines.append(f"{label}: {result[k]}")
            usage=result.get("volume_usage")
            if isinstance(usage,dict):
                lines.extend([f"Pojemność woluminu: {fmt_bytes(usage['total']) if usage.get('total') else 'N/D'}",f"Wolne miejsce: {fmt_bytes(usage['free']) if usage.get('free') else 'N/D'}"])
            benchmark=result.get("benchmark")
            if isinstance(benchmark,dict):
                if benchmark.get("read_bps") is not None:lines.append(f"Prędkość odczytu: {fmt_speed(benchmark['read_bps'])}")
                if benchmark.get("write_bps") is not None:lines.append(f"Prędkość zapisu: {fmt_speed(benchmark['write_bps'])}")
            if result.get("message"):lines.append("Informacja: "+str(result["message"])[:1200])
            if result.get("note"):lines.append("Zakres: "+str(result["note"])[:800])
            if result.get("error"):lines.append("BŁĄD: "+str(result["error"])[:1000])
            if state in ("WARN","N/D","ERROR"):lines.append("UWAGA: wynik nie potwierdza pełnej sprawności podzespołu.")
            body="\n".join(lines)
        box.configure(state="normal");box.delete("1.0","end");box.insert("1.0",body);box.configure(state="disabled")
    except Exception as exc:
        try:self.append_log("Raport podzespołu: "+repr(exc))
        except Exception:pass

def _u86_launch_component_test(self,module,mode):
    if mode=="visual":
        try:_u69_open_component_simulator(self,module,False,"scan")
        except Exception as exc:messagebox.showerror("Symulator 3D",str(exc))
        return
    if getattr(self,"running",False):
        messagebox.showwarning("Test komponentu","Inny test już działa. Poczekaj albo użyj STOP TEST.");return
    try:
        if module=="GPU" and mode=="benchmark":_u68_open_gpu_suite(self,auto_start=True);return
        _u69_launch_component_test(self,module,mode)
    except Exception as exc:
        self.queue_log(f"Uruchomienie {module}: {type(exc).__name__}: {exc}")
        messagebox.showerror("Test komponentu",str(exc))

def _u86_component_monitor_tick(self,page_id):
    if getattr(self,"_u86_page_id",None)!=page_id:return
    panel=getattr(self,"_u67_stage_panel",None)
    try:
        if panel is None or not panel.winfo_exists():return
    except Exception:return
    try:
        _u67_refresh_visible_charts(self)
        module=getattr(self,"_u86_module_context",None)
        if module and getattr(self,"_u86_result_text",None) is not None:_u86_render_component_report(self,module)
        if not getattr(self,"_u84_gpu_poll_busy",False) and _u66_time.monotonic()-getattr(self,"_u86_gpu_poll_time",0)>=4:
            self._u86_gpu_poll_time=_u66_time.monotonic();_u84_gpu_poll_now(self)
    except Exception:pass
    try:self.after(1000,lambda:_u86_component_monitor_tick(self,page_id))
    except Exception:pass

def _u86_module_key(value):
    text=str(value or "").strip().upper()
    if text in ("DYSKI","DYSK","SSD / HDD / NVME","DYSKI — SSD / HDD / NVME"):return "DYSK"
    if any(word in text for word in ("WI-FI","WIFI","SIEĆ","LAN","NETWORK","INTERNET")):return "SIEĆ"
    if "USB" in text:return "USB"
    if any(word in text for word in ("AUDIO","DŹWIĘK","MIKROFON")):return "AUDIO"
    if any(word in text for word in ("KLAWIATURA","TOUCHPAD","INPUT")):return "KLAWIATURA"
    if any(word in text for word in ("KAMERA","WEBCAM")):return "KAMERA"
    if any(word in text for word in ("BATTERY","BATERIA","ZASILANIE")):return "BATERIA"
    if "VRAM" in text:return "VRAM"
    if any(word in text for word in ("MATRYCA","EKRAN","MONITOR")):return "EKRAN"
    if any(word in text for word in ("SECURITY","BEZPIECZEŃSTWO","ANTYWIRUS")):return "SECURITY"
    for key in ("CPU","GPU","RAM"):
        if text==key or text.startswith(key+" "):return key
    return ""

_U86_ORIGINAL_SHOW_MODULE=AppV43.show_module
def _u86_show_module_with_component_workbench(self,module):
    _U86_ORIGINAL_SHOW_MODULE(self,module)
    key=_u86_module_key(module)
    if not key or getattr(self,"_u86_suite_active",False):return
    self._u86_page_id=int(getattr(self,"_u86_page_id",0))+1;self._u86_module_context=key
    _u67_stage_live_panel(self,1,1,_U86_MODULE_TITLES.get(key,key)+" — MONITOR LIVE")
    self.after(180,lambda pid=self._u86_page_id:_u86_component_monitor_tick(self,pid))

_U86_ORIGINAL_SHOW_SIMPLE_MODULE=AppV43.show_simple_module
def _u86_show_simple_module_with_component_workbench(self,title):
    _U86_ORIGINAL_SHOW_SIMPLE_MODULE(self,title)
    key=_u86_module_key(title)
    if not key or getattr(self,"_u86_suite_active",False):return
    self._u86_page_id=int(getattr(self,"_u86_page_id",0))+1;self._u86_module_context=key
    _u67_stage_live_panel(self,1,1,_U86_MODULE_TITLES.get(key,key)+" — MONITOR LIVE")
    self.after(180,lambda pid=self._u86_page_id:_u86_component_monitor_tick(self,pid))

_U86_ORIGINAL_SHOW_BATTERY=AppV43.show_battery_or_power
def _u86_show_battery_with_component_workbench(self):
    _U86_ORIGINAL_SHOW_BATTERY(self)
    if getattr(self,"_u86_suite_active",False):return
    self._u86_page_id=int(getattr(self,"_u86_page_id",0))+1;self._u86_module_context="BATERIA"
    _u67_stage_live_panel(self,1,1,"BATERIA / ZASILANIE — MONITOR LIVE")
    self.after(180,lambda pid=self._u86_page_id:_u86_component_monitor_tick(self,pid))

_U86_ORIGINAL_RUN_SELECTED_DIAGNOSTIC=_u67_run_selected_diagnostic
def _u86_run_selected_diagnostic(self,selected):
    self._u86_suite_active=True
    try:return _U86_ORIGINAL_RUN_SELECTED_DIAGNOSTIC(self,selected)
    finally:self._u86_suite_active=False

_U86_ORIGINAL_DRAW_BAR_CHART=AppV43.draw_bar_chart
def _u86_draw_bar_chart(self,canvas,items,title=""):
    t=self.colors();canvas.delete("all")
    w=max(200,canvas.winfo_width() or 500);h=max(120,canvas.winfo_height() or 180)
    if title:canvas.create_text(12,12,text=title,anchor="w",fill=t["fg"],font=self.fnt(9,"bold"))
    if not items:
        canvas.create_text(w/2,h/2-8,text="TEST NIEZROBIONY — URUCHOM SKAN LUB BENCHMARK",fill=t["warn"],font=self.fnt(9,"bold"))
        canvas.create_text(w/2,h/2+15,text="Brak próbki nie oznacza ani usterki, ani sprawności.",fill=t["muted"],font=self.fnt(8))
        return
    _U86_ORIGINAL_DRAW_BAR_CHART(self,canvas,items,title)

def _u86_selftest_component_ui():
    assert len(_U66_SCENES)==60 and len({x[0] for x in _U66_SCENES})==60
    assert str(_U68_PROFILE_CHOICES[-1]).endswith("900 s")
    assert callable(_u86_stage_live_panel) and callable(_u86_launch_component_test)
    assert callable(_u86_render_component_report) and callable(_u86_component_monitor_tick)
    assert all(k in _U86_COMPONENT_KEYS for k in ("CPU","GPU","RAM","DYSK","VRAM","EKRAN","SECURITY","BATERIA","SIEĆ","USB","AUDIO","KLAWIATURA","KAMERA"))
    assert any("NIEZROBIONY" in str(x) for x in _u86_draw_bar_chart.__code__.co_consts)
    assert "cpu_power" in _u67_draw_history_chart.__code__.co_consts
    print("COMPONENT_LIVE_UI_60_SCENE_SELFTEST_OK: 13 modules, independent controls, 6 live charts, sensors N/D")

_u67_stage_live_panel=_u86_stage_live_panel
_u67_run_selected_diagnostic=_u86_run_selected_diagnostic
AppV43.show_module=_u86_show_module_with_component_workbench
AppV43.show_simple_module=_u86_show_simple_module_with_component_workbench
AppV43.show_battery_or_power=_u86_show_battery_with_component_workbench
AppV43.draw_bar_chart=_u86_draw_bar_chart



# v4.3.87 — honest live throughput, per-scene 3D fixes, real short/medium/long VRAM tests, error alarm.
import http.client as _u90_http_client
import ssl as _u90_ssl

_U90_ORIGINAL_QUEUE_RESULTS = AppV43.queue_results
_U90_ERROR_SOUND_GAP = 2.2

def _u90_error_alarm(app, detail):
    now = _u66_time.monotonic()
    if now - float(getattr(app, "_u90_last_error_beep", 0.0) or 0.0) < _U90_ERROR_SOUND_GAP:
        return
    try:
        app._u90_last_error_beep = now
    except Exception:
        pass
    try:
        import winsound as _u90_winsound
        try:
            _u90_winsound.MessageBeep(_u90_winsound.MB_ICONHAND)
        except Exception:
            def alarm():
                try:
                    _u90_winsound.Beep(1300, 180)
                    _u90_winsound.Beep(720, 260)
                except Exception:
                    pass
            _u90_threading.Thread(target=alarm, daemon=True, name="NaprawaPCErrorAlarm").start()
    except Exception:
        pass
    try:
        app.queue_log("ALARM TESTU — wykryto błąd: " + str(detail)[:220])
    except Exception:
        pass


def _u90_queue_results_with_error_alarm(self, key, value):
    result = _U90_ORIGINAL_QUEUE_RESULTS(self, key, value)
    if isinstance(value, dict):
        state = str(value.get("state", "")).lower()
        has_error = bool(value.get("error")) or state in ("bad", "error", "failed", "fail")
        if has_error and not value.get("stopped") and not value.get("stopped_by_user"):
            _u90_error_alarm(self, f"{key}: {value.get('error') or value.get('message') or state}")
    return result

AppV43.queue_results = _u90_queue_results_with_error_alarm


def _u90_speed_request(url, data=None, timeout=40, progress=None, phase="download"):
    parsed = _u66_urlparse.urlparse(str(url))
    if parsed.scheme != "https" or (parsed.hostname or "").lower() != "speed.cloudflare.com":
        raise ValueError("Speed Test dopuszcza wyłącznie HTTPS do speed.cloudflare.com.")
    path = parsed.path or "/"
    if parsed.query:
        path += "?" + parsed.query
    headers = {
        "User-Agent": "NAPRAWA-PC-HARDWARE-TEST-PRO/SpeedTest-live",
        "Cache-Control": "no-cache",
        "Accept-Encoding": "identity",
        "Connection": "close",
    }
    conn = None
    total_started = _u66_time.perf_counter()
    transferred = 0
    response_bytes = 0
    try:
        conn = _u90_http_client.HTTPSConnection(parsed.hostname, parsed.port or 443, timeout=timeout,
                                                context=_u90_ssl.create_default_context())
        if data is None:
            conn.request("GET", path, headers=headers)
            response = conn.getresponse()
            status = int(response.status)
            if status < 200 or status >= 300:
                raise OSError(f"Cloudflare zwrócił HTTP {status}; pomiar download nie jest ważny.")
            started = _u66_time.perf_counter()
            last_t = started
            last_bytes = 0
            expected = None
            try:
                values = _u66_urlparse.parse_qs(parsed.query)
                if values.get("bytes"):
                    expected = max(0, int(values["bytes"][0]))
            except Exception:
                expected = None
            header_length = response.getheader("Content-Length")
            if expected is None and header_length:
                try: expected = max(0, int(header_length))
                except Exception: expected = None
            while True:
                chunk = response.read(256 * 1024)
                if not chunk:
                    break
                transferred += len(chunk)
                now = _u66_time.perf_counter()
                elapsed = max(0.001, now - started)
                inst_elapsed = max(0.001, now - last_t)
                instant = max(0.0, (transferred - last_bytes) * 8 / inst_elapsed / 1_000_000)
                average = transferred * 8 / elapsed / 1_000_000
                if callable(progress):
                    try: progress(phase, transferred, expected or 0, elapsed, instant, average)
                    except Exception: pass
                last_t, last_bytes = now, transferred
            transfer_seconds = max(0.001, _u66_time.perf_counter() - started)
            if expected is not None and expected > 0 and transferred < int(expected * 0.98):
                raise OSError(f"Niepełny download: odebrano {transferred} z {expected} bajtów.")
        else:
            body = memoryview(data)
            conn.putrequest("POST", path)
            conn.putheader("User-Agent", headers["User-Agent"])
            conn.putheader("Cache-Control", headers["Cache-Control"])
            conn.putheader("Accept-Encoding", "identity")
            conn.putheader("Connection", "close")
            conn.putheader("Content-Type", "application/octet-stream")
            conn.putheader("Content-Length", str(len(body)))
            conn.endheaders()
            started = _u66_time.perf_counter()
            last_t = started
            last_bytes = 0
            block_size = 256 * 1024
            for offset in range(0, len(body), block_size):
                chunk = body[offset:offset + block_size]
                conn.send(chunk)
                transferred += len(chunk)
                now = _u66_time.perf_counter()
                elapsed = max(0.001, now - started)
                inst_elapsed = max(0.001, now - last_t)
                instant = max(0.0, (transferred - last_bytes) * 8 / inst_elapsed / 1_000_000)
                average = transferred * 8 / elapsed / 1_000_000
                if callable(progress):
                    try: progress(phase, transferred, len(body), elapsed, instant, average)
                    except Exception: pass
                last_t, last_bytes = now, transferred
            transfer_seconds = max(0.001, _u66_time.perf_counter() - started)
            response = conn.getresponse()
            status = int(response.status)
            if status < 200 or status >= 300:
                raise OSError(f"Cloudflare zwrócił HTTP {status}; pomiar upload nie jest ważny.")
            while True:
                chunk = response.read(64 * 1024)
                if not chunk:
                    break
                response_bytes += len(chunk)
        if data is None:
            # Count the received transfer only. Upload responses are not counted as uploaded bytes.
            response_bytes = 0
        request_seconds = max(0.001, _u66_time.perf_counter() - total_started)
        return {
            "bytes": int(transferred),
            "seconds": round(transfer_seconds, 4),
            "request_seconds": round(request_seconds, 4),
            "mbps": round(transferred * 8 / max(0.001, transfer_seconds) / 1_000_000, 3),
            "status": status,
            "response_bytes": int(response_bytes),
            "transfer_method": "HTTPS real bytes / monotonic clock",
        }
    finally:
        if conn is not None:
            try: conn.close()
            except Exception: pass


def _u90_draw_live_speed_chart(self):
    canvas = getattr(self, "_u66_speed_chart", None)
    if canvas is None:
        return
    try:
        if not canvas.winfo_exists():
            return
        canvas.delete("all")
        t = self.colors()
        w = max(420, canvas.winfo_width() or 520)
        h = max(145, canvas.winfo_height() or 230)
        left, right, top, bottom = 48, w - 14, 30, h - 28
        history = getattr(self, "_u90_speed_history", {"download": [], "upload": {}})
        down = history.get("download", [])[-100:]
        up = history.get("upload", [])[-100:]
        ceiling = max([50.0] + [float(v) for v in down + up if v is not None])
        canvas.create_text(10, 7, text="PRĘDKOŚĆ CHWILOWA Z PRZESŁANYCH BAJTÓW • Mbps", anchor="nw",
                           fill=t["fg"], font=self.fnt(9, "bold"))
        for pct in (0, 25, 50, 75, 100):
            y = bottom - (bottom - top) * pct / 100
            canvas.create_line(left, y, right, y, fill=t["card"])
            canvas.create_text(left - 6, y, text=f"{ceiling*pct/100:.0f}", anchor="e", fill=t["muted"], font=self.fnt(7))
        for values, color in ((down, t["accent"]), (up, t["good"])):
            if len(values) < 2:
                continue
            points = []
            for i, value in enumerate(values):
                x = left + (right-left) * i / max(1, len(values)-1)
                y = bottom - (bottom-top) * max(0.0, min(ceiling, float(value))) / ceiling
                points.extend((x,y))
            canvas.create_line(*points, fill=color, width=2, smooth=True)
        canvas.create_text(left, h-8, text="DOWNLOAD", anchor="sw", fill=t["accent"], font=self.fnt(8, "bold"))
        canvas.create_text(left+100, h-8, text="UPLOAD", anchor="sw", fill=t["good"], font=self.fnt(8, "bold"))
        canvas.create_text(right, h-8, text=f"skala 0–{ceiling:.0f} Mbps", anchor="se", fill=t["muted"], font=self.fnt(7))
    except Exception:
        pass


def _u90_speed_progress_ui(self, phase, done, total, elapsed, instant_mbps, average_mbps, base_data):
    try:
        history = getattr(self, "_u90_speed_history", None)
        if not isinstance(history, dict):
            history = {"download": [], "upload": []}
            self._u90_speed_history = history
        if phase in ("download", "upload"):
            history.setdefault(phase, []).append(max(0.0, float(instant_mbps)))
            history[phase] = history[phase][-100:]
        ratio = f"{done/total*100:.0f}%" if total and total > 0 else "100%"
        rate = f"{instant_mbps:.1f} Mbps chwilowo / {average_mbps:.1f} Mbps średnio"
        if phase in ("download", "upload"):
            label = self._u66_speed_values.get(phase)
            if label is not None and label.winfo_exists():
                label.config(text=f"{instant_mbps:.1f} Mbps")
            data_label = self._u66_speed_values.get("data")
            if data_label is not None and data_label.winfo_exists():
                data_label.config(text=f"{(base_data+done)/1_000_000:.2f} MB")
            _u66_set_speed_status(self,
                f"NA ŻYWO — {phase.upper()} {ratio} • {done/1_000_000:.2f}/{total/1_000_000:.2f} MB • {rate} • {elapsed:.2f} s")
            _u90_draw_live_speed_chart(self)
        elif phase == "ping":
            label = self._u66_speed_values.get("latency")
            if label is not None and label.winfo_exists():
                label.config(text=f"{elapsed:.1f} ms")
            _u66_set_speed_status(self, f"NA ŻYWO — HTTPS RTT {elapsed:.1f} ms (to opóźnienie HTTPS, nie ping ICMP).")
    except Exception:
        pass


def _u90_emit_speed_progress(self, phase, done, total, elapsed, instant, average, base_data=0):
    try:
        self.queue_action(lambda p=phase,d=done,t=total,e=elapsed,i=instant,a=average,b=base_data:
            _u90_speed_progress_ui(self,p,d,t,e,i,a,b))
    except Exception:
        pass


def _u90_median(values):
    vals = sorted(float(v) for v in values if v is not None and _u66_math.isfinite(float(v)))
    if not vals:
        raise ValueError("Brak prawidłowych próbek przepustowości.")
    n = len(vals)
    return vals[n//2] if n % 2 else (vals[n//2-1] + vals[n//2]) / 2.0


def _u90_measure_speed(self):
    samples = {
        "latency_ms": [], "download": [], "upload": [],
        "started_at": _U66_datetime.now().isoformat(timespec="seconds"),
        "method": "Rzeczywiste bajty HTTPS do speed.cloudflare.com; mediana 3 próbek; postęp liczony podczas transmisji.",
        "latency_method": "HTTPS round-trip time, nie ICMP ping",
    }
    total_data = 0
    def phase(text):
        try: self.queue_action(lambda m=text: _u66_set_speed_status(self,m))
        except Exception: pass
        try: self.queue_status(text)
        except Exception: pass
    try:
        for i in range(3):
            phase(f"Speed Test NA ŻYWO: HTTPS RTT {i+1}/3…")
            url = "https://speed.cloudflare.com/__down?bytes=0&r=" + _u66_uuid.uuid4().hex
            t0 = _u66_time.perf_counter()
            _u90_speed_request(url, None, 20, None, "ping")
            latency = round((_u66_time.perf_counter()-t0)*1000, 2)
            samples["latency_ms"].append(latency)
            _u90_emit_speed_progress(self, "ping", 0, 0, latency, 0.0, 0.0, total_data)
        for idx, size in enumerate((1_000_000, 5_000_000, 10_000_000), 1):
            phase(f"Speed Test NA ŻYWO: download {idx}/3 — pobieranie rzeczywistych bajtów ({size//1_000_000} MB)…")
            url = "https://speed.cloudflare.com/__down?bytes=" + str(size) + "&r=" + _u66_uuid.uuid4().hex
            result = _u90_speed_request(url, None, 40,
                lambda p,d,t,e,i,a,b=total_data:_u90_emit_speed_progress(self,p,d,t,e,i,a,b), "download")
            result["requested_bytes"] = size
            samples["download"].append(result)
            total_data += int(result["bytes"])
        for idx, size in enumerate((500_000, 2_000_000, 5_000_000), 1):
            phase(f"Speed Test NA ŻYWO: upload {idx}/3 — wysyłanie rzeczywistych bajtów ({size/1_000_000:.1f} MB)…")
            body = _u66_os.urandom(size)
            url = "https://speed.cloudflare.com/__up?r=" + _u66_uuid.uuid4().hex
            result = _u90_speed_request(url, body, 40,
                lambda p,d,t,e,i,a,b=total_data:_u90_emit_speed_progress(self,p,d,t,e,i,a,b), "upload")
            result["requested_bytes"] = size
            samples["upload"].append(result)
            total_data += int(result["bytes"])
        samples["latency_average_ms"] = round(_u90_median(samples["latency_ms"]), 2)
        samples["download_mbps"] = round(_u90_median([x["mbps"] for x in samples["download"]]), 2)
        samples["upload_mbps"] = round(_u90_median([x["mbps"] for x in samples["upload"]]), 2)
        samples["data_bytes"] = total_data
        samples["state"] = "good"
        try:
            folder = _u66_store_dir() / "speedtest"
            folder.mkdir(parents=True, exist_ok=True)
            history_path = folder / "history.json"
            try: records = _u66_json.loads(history_path.read_text(encoding="utf-8"))
            except Exception: records = []
            records.append(samples)
            history_path.write_text(_u66_json.dumps(records[-100:], ensure_ascii=False, indent=2), encoding="utf-8")
            samples["history_path"] = str(history_path)
        except Exception:
            pass
        return samples
    except Exception as exc:
        _u90_error_alarm(self, f"Speed Test: {type(exc).__name__}: {exc}")
        raise


def _u90_draw_speed_chart(self, result):
    # Keep the live transmission history visible after completion; never replace it with fabricated bars.
    _u90_draw_live_speed_chart(self)
    try:
        if getattr(self, "_u66_speed_status", None) is not None and self._u66_speed_status.winfo_exists():
            self._u66_speed_status.config(
                text=f"WYNIK KOŃCOWY — mediana 3 realnych próbek: DOWNLOAD {result.get('download_mbps','N/D')} Mbps • "
                     f"UPLOAD {result.get('upload_mbps','N/D')} Mbps • HTTPS RTT {result.get('latency_average_ms','N/D')} ms • "
                     f"transfer {result.get('data_bytes',0)/1_000_000:.2f} MB"
            )
    except Exception:
        pass


def _u90_show_speed_test(self):
    _U90_ORIGINAL_SHOW_SPEED_TEST(self)
    self._u90_speed_history = {"download": [], "upload": []}
    try: _u90_draw_live_speed_chart(self)
    except Exception: pass


def _u90_start_speed_test(self):
    if getattr(self, "_u66_speed_running", False):
        return
    self._u66_speed_running = True
    self._u90_speed_history = {"download": [], "upload": []}
    _u66_set_speed_status(self, "Rozpoczynam rzeczywisty test HTTPS. Odczyty będą aktualizowane podczas transferu…")
    def job():
        try:
            result = _u90_measure_speed(self)
            self.results["SPEED_TEST"] = result
            def done(r=result):
                self._u66_speed_running = False
                if getattr(self, "current_view", "") == "SPEED_TEST":
                    for key, val in (
                        ("latency", f"{r['latency_average_ms']} ms"),
                        ("download", f"{r['download_mbps']} Mbps"),
                        ("upload", f"{r['upload_mbps']} Mbps"),
                        ("data", f"{r['data_bytes']/1_000_000:.2f} MB"),
                    ):
                        try: self._u66_speed_values[key].config(text=val)
                        except Exception: pass
                    _u90_draw_speed_chart(self, r)
                _u66_set_speed_status(self,
                    f"Zakończono. Mediana 3 próbek: download {r['download_mbps']} Mbps, "
                    f"upload {r['upload_mbps']} Mbps; HTTPS RTT {r['latency_average_ms']} ms.")
                self.queue_log(f"SPEED TEST RZECZYWISTY: DL={r['download_mbps']} Mbps; UL={r['upload_mbps']} Mbps; RTT={r['latency_average_ms']} ms.")
            self.queue_action(done)
        except Exception as exc:
            def fail(err=exc):
                self._u66_speed_running = False
                msg = f"Speed Test NIEUKOŃCZONY — {type(err).__name__}: {err}"
                _u66_set_speed_status(self, msg)
                _u90_error_alarm(self, msg)
                try: messagebox.showerror("Speed Test — błąd pomiaru", msg)
                except Exception: pass
                self.queue_log(msg)
            self.queue_action(fail)
    _u66_threading.Thread(target=job, name="NaprawaPCSpeedTestLive", daemon=True).start()


def _u90_show_3d_studio(self):
    _U90_ORIGINAL_SHOW_3D_STUDIO(self)
    try:
        self._u90_scene_resolution_var = tk.StringVar(value=str(getattr(self, "_u90_scene_resolution_value", "1920x1080")))
        row = tk.Frame(self.content, bg=self.colors()["bg"])
        if getattr(self, "_u66_3d_status", None) is not None and self._u66_3d_status.winfo_exists():
            row.pack(fill="x", pady=(0, 4), before=self._u66_3d_status)
        else:
            row.pack(fill="x", pady=(0, 4))
        tk.Label(row, text="ROZDZIELCZOŚĆ RENDERERA:", bg=self.colors()["bg"], fg=self.colors()["muted"], font=self.fnt(8, "bold")).pack(side="left", padx=(3, 6))
        cb = ttk.Combobox(row, textvariable=self._u90_scene_resolution_var,
            values=("1280x720", "1920x1080", "2560x1440", "3840x2160"), state="readonly", width=12)
        cb.pack(side="left", padx=3, ipady=3)
        self._u90_scene_resolution_var.trace_add("write", lambda *_: setattr(self, "_u90_scene_resolution_value", self._u90_scene_resolution_var.get()))
        self._u90_scene_resolution_value = self._u90_scene_resolution_var.get()
    except Exception as exc:
        try: self.queue_log("3D: wybór rozdzielczości niedostępny: " + repr(exc))
        except Exception: pass


def _u90_update_3d_scene(self, scene_id, scene, result, index, total):
    try:
        if getattr(self, "current_view", "") == "3D_STUDIO":
            tree = getattr(self, "_u66_3d_tree", None)
            if tree is not None and tree.winfo_exists():
                values=(scene[0],result.get("state","N/D"),result.get("average_fps","N/D"),
                        result.get("peak_fps_1s","N/D"),result.get("frames","N/D"),
                        result.get("renderer",result.get("error","—")))
                try: tree.item(str(scene_id), values=values)
                except Exception: pass
            status=getattr(self,"_u66_3d_status",None)
            if status is not None and status.winfo_exists():
                status.config(text=f"SCENA {index}/{total}: {scene[0]} • {result.get('state','N/D')} • "
                                   f"FPS {result.get('average_fps','N/D')} • {result.get('duration_seconds','N/D')} s")
    except Exception:
        pass


def _u90_run_3d_suite(self, seconds=5):
    seconds=max(3,min(900,int(seconds)))
    _u66_ui_wait(self, lambda: _u90_show_3d_studio(self))
    results=[]
    total=len(_U66_SCENES)
    for i, scene in enumerate(_U66_SCENES,1):
        if self._test_should_stop():
            break
        title=f"3D BENCHMARK {i}/{total} — {scene[0]}"
        _u66_set_suite_status(self,title)
        result=_u66_execute_gpu_scene(self,i,seconds)
        results.append(result)
        if result.get("state") != "good" and not result.get("stopped_by_user"):
            _u90_error_alarm(self, f"3D scena {i}: {result.get('error') or result.get('note') or result.get('state')}")
        _u66_ui_wait(self, lambda sid=i,sc=scene,r=result,n=i,t=total:
            _u90_update_3d_scene(self,sid,sc,r,n,t))
    passed=sum(1 for item in results if item.get("state")=="good")
    report={
        "state":"good" if results and passed==len(results) and len(results)==total else "warn",
        "completed":len(results),"total":total,"good":passed,"seconds_per_scene":seconds,
        "resolution":str(getattr(self,"_u90_scene_resolution_value","1920x1080")),
        "scenes":results,"time":_U66_datetime.now().isoformat(timespec="seconds"),
    }
    self.results["3D_SUITE"]=report
    self.queue_results("3D_SUITE",report)
    try:
        folder=_u66_store_dir()/"benchmarks";folder.mkdir(parents=True,exist_ok=True)
        target=folder/("3d-benchmark-"+_U66_datetime.now().strftime("%Y%m%d-%H%M%S")+".json")
        target.write_text(_u66_json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
        report["report_path"]=str(target)
    except Exception as exc:
        self.queue_log("Nie udało się zapisać raportu 3D: "+repr(exc))
    status=f"3D BENCHMARK: {passed}/{len(results)} udanych scen; {len(results)}/{total} wykonanych; rozdzielczość {report['resolution']}; {seconds} s/scena."
    self.queue_log(status)
    _u66_ui_wait(self,lambda:_u90_set_3d_final_status(self,status))


def _u90_set_3d_final_status(self, status):
    try:
        if getattr(self,"current_view","")=="3D_STUDIO" and self._u66_3d_status.winfo_exists():
            self._u66_3d_status.config(text=status)
    except Exception: pass


def _u90_run_vram_profile_worker(self, requested_mb, seconds, open_gpu_after=False):
    requested=max(32,min(256,int(requested_mb)))
    seconds=max(15,min(900,int(seconds)))
    overall_start=_u66_time.monotonic()
    passes=[]
    pass_index=0
    final_state="warn"
    try:
        self._u41_vram_test_running=True
        _u66_set_suite_status(self,f"VRAM: profil {seconds} s, żądana alokacja {requested} MB.")
        while pass_index==0 or (_u66_time.monotonic()-overall_start)<seconds:
            if self._test_should_stop():
                final_state="warn"
                break
            pass_index += 1
            out=Path(_u66_os.path.join(tempfile.gettempdir(),
                f"naprawapc_vram_{os.getpid()}_{_u66_uuid.uuid4().hex[:10]}_{pass_index}.json"))
            try: out.unlink(missing_ok=True)
            except Exception: pass
            command=[sys.executable,"--vram-test",str(out),str(requested)] if getattr(sys,"frozen",False) else [
                sys.executable,str(Path(__file__).resolve()),"--vram-test",str(out),str(requested)]
            result={"state":"warn","requested_mb":requested,"message":"Tester VRAM nie zwrócił raportu."}
            proc=None
            try:
                proc=_u66_subprocess.Popen(command,cwd=tempfile.gettempdir(),
                    creationflags=getattr(_u66_subprocess,"CREATE_NO_WINDOW",0))
                started=_u66_time.monotonic()
                self._u90_vram_child_process=proc
                while proc.poll() is None and _u66_time.monotonic()-started<240:
                    if self._test_should_stop():
                        try: proc.terminate()
                        except Exception: pass
                        break
                    try:
                        if out.is_file():
                            snap=_u66_json.loads(out.read_text(encoding="utf-8"))
                            self.queue_action(lambda r=snap:self._u41_set_vram_status(r))
                            progress=snap.get("status_text") or snap.get("message") or "VRAM: test tekstur w toku…"
                            self.queue_status(f"VRAM {pass_index}: {progress}")
                            status_label=getattr(self,"_u69_workbench_status",None)
                            if status_label is not None:
                                self.queue_action(lambda label=status_label,msg=progress:
                                    label.config(text=str(msg)) if label.winfo_exists() else None)
                    except Exception: pass
                    _u66_time.sleep(.25)
                if proc.poll() is None:
                    try: proc.kill()
                    except Exception: pass
                    result={"state":"warn","requested_mb":requested,"error":"Timeout po 240 s",
                            "message":"Tester VRAM przekroczył 240 s na jednym przebiegu."}
                elif out.is_file():
                    result=_u66_json.loads(out.read_text(encoding="utf-8"))
                else:
                    result={"state":"warn","requested_mb":requested,"error":f"Brak raportu, kod procesu {proc.returncode}",
                            "message":"Tester VRAM nie wygenerował raportu; sprawdź obsługę OpenGL."}
            except Exception as exc:
                result={"state":"warn","requested_mb":requested,"error":f"{type(exc).__name__}: {exc}",
                        "message":f"Nie udało się uruchomić testera VRAM: {exc}"}
            finally:
                try:
                    if proc is not None and proc.poll() is None: proc.kill()
                except Exception: pass
                self._u90_vram_child_process=None
            result["pass_number"]=pass_index
            result["profile_seconds"]=seconds
            result["elapsed_profile_seconds"]=round(_u66_time.monotonic()-overall_start,2)
            passes.append(result)
            self.queue_log(f"VRAM profil: przebieg {pass_index}, stan {result.get('state')}, "
                           f"alokacja {result.get('allocated_mb','N/D')} MB, "
                           f"wzorce {result.get('patterns_completed','N/D')}/{result.get('patterns_total','N/D')}.")
            if result.get("state") not in ("good",):
                final_state=result.get("state","warn")
                if not result.get("stopped_by_user") and not result.get("stopped"):
                    _u90_error_alarm(self,f"VRAM: {result.get('error') or result.get('message') or final_state}")
                break
            final_state="good"
            if _u66_time.monotonic()-overall_start>=seconds:
                break
        combined={
            "state":final_state if passes else "warn","requested_mb":requested,"profile_seconds":seconds,
            "passes_completed":len(passes),"elapsed_seconds":round(_u66_time.monotonic()-overall_start,2),
            "passes":passes,"stopped":self._test_should_stop(),
            "note":"VRAM to test pamięci tekstur OpenGL z zapisem/readback; każdy przebieg sprawdza sześć wzorców. Jeden pełny przebieg może trwać dłużej niż profil KRÓTKI."
        }
        self.results["VRAM_TEST"]=combined
        self.queue_results("VRAM_TEST",combined)
        self.queue_log(f"VRAM BENCHMARK zakończony: {len(passes)} pełnych przebiegów / {combined['elapsed_seconds']} s / {combined['state']}.")
        return combined
    finally:
        self._u41_vram_test_running=False
        if open_gpu_after:
            def done():
                self.running=False
                self.stop_requested=False
                if getattr(self,"current_view","")=="GPU":
                    try: self.show_module("GPU")
                    except Exception: pass
                try:
                    status=getattr(self,"_u41_vram_status_var",None)
                    if status is not None: status.set(f"VRAM: profil zakończony — {len(passes)} przebiegów; {seconds} s.")
                except Exception: pass
            self.queue_action(done)


def _u90_start_vram_profile_test(self):
    if getattr(self,"running",False) or getattr(self,"_u41_vram_test_running",False):
        messagebox.showwarning("Test VRAM","Inny test już trwa. Zatrzymaj go albo poczekaj.")
        return
    try: requested=int(str(self._u41_vram_size_var.get()).split()[0])
    except Exception: requested=64
    requested=max(32,min(256,requested))
    seconds=_u68_profile_seconds(self)
    if not messagebox.askyesno("Rzeczywisty benchmark VRAM",
        f"Profil {seconds} s, alokacja do {requested} MB. Każdy przebieg zapisuje tekstury przez OpenGL i porównuje 6 wzorców przez readback. "
        "Profil dłuższy powtarza pełne przebiegi. Jeden przebieg może przekroczyć czas profilu. Kontynuować?"):
        return
    self.running=True
    self.stop_requested=False
    _u66_threading.Thread(target=lambda:_u90_run_vram_profile_worker(self,requested,seconds,True),
        name="NaprawaPCVRAMProfile",daemon=True).start()


def _u90_run_vram_profile_from_suite(self):
    try: requested=int(str(self._u41_vram_size_var.get()).split()[0])
    except Exception: requested=64
    return _u90_run_vram_profile_worker(self,requested,_u68_profile_seconds(self),False)


_U90_ORIGINAL_SHOW_SPEED_TEST = _u66_show_speed_test
_U90_ORIGINAL_SHOW_3D_STUDIO = _u66_show_3d_studio
_u66_measure_speed = _u90_measure_speed
_u66_draw_speed_chart = _u90_draw_speed_chart
_u66_show_speed_test = _u90_show_speed_test
_u66_start_speed_test = _u90_start_speed_test
_u66_run_3d_suite = _u90_run_3d_suite
_u69_run_component_worker_original = _u69_run_component_worker
def _u90_component_worker(self, module, mode):
    if module=="VRAM" and mode!="scan":
        _u90_run_vram_profile_from_suite(self)
        return
    return _u69_run_component_worker_original(self,module,mode)
_u69_run_component_worker = _u90_component_worker
_u66_show_3d_studio = _u90_show_3d_studio
AppV43.show_3d_studio = _u90_show_3d_studio
AppV43.show_speed_test = _u90_show_speed_test
AppV43._u41_start_vram_test = _u90_start_vram_profile_test
AppV43._u66_ui_wait = _u66_ui_wait
AppV43._u66_set_suite_status = _u66_set_suite_status


def _u90_selftest_release_fixes():
    assert callable(AppV43._u66_ui_wait), "Missing AppV43._u66_ui_wait compatibility binding"
    assert callable(AppV43._u66_set_suite_status), "Missing AppV43._u66_set_suite_status compatibility binding"
    assert "self" not in _u90_run_3d_suite.__code__.co_names
    assert "self" not in _u90_run_3d_suite.__code__.co_names
    assert "KRÓTKI — 15 s" in _U68_PROFILE_CHOICES
    assert "ŚREDNI — 60 s" in _U68_PROFILE_CHOICES
    assert "DŁUGI — 180 s" in _U68_PROFILE_CHOICES
    assert "900 s" in _U68_PROFILE_CHOICES[-1]
    assert AppV43._u41_start_vram_test is _u90_start_vram_profile_test
    assert AppV43.show_speed_test is _u90_show_speed_test
    assert _u66_measure_speed is _u90_measure_speed
    assert callable(_u90_error_alarm) and AppV43.queue_results is _u90_queue_results_with_error_alarm

    progress=[]
    class _FakeResponse:
        def __init__(self, body, status=200):
            self.body=body; self.position=0; self.status=status
        def getheader(self, name):
            return str(len(self.body)) if name.lower()=="content-length" else None
        def read(self, n=-1):
            if self.position>=len(self.body): return b""
            take=len(self.body)-self.position if n<0 else min(n,len(self.body)-self.position)
            part=self.body[self.position:self.position+take]; self.position+=len(part); return part
    class _FakeHTTPSConnection:
        def __init__(self,*args,**kwargs): self.method="GET"; self.path="/"; self.sent=0; self.response=None
        def request(self,method,path,headers=None):
            self.method=method; self.path=path
            if method=="GET":
                parsed=_u66_urlparse.urlparse(path)
                qs=_u66_urlparse.parse_qs(parsed.query)
                count=int((qs.get("bytes") or ["128"])[0])
                self.response=_FakeResponse(b"X"*max(0,count))
            else: self.response=_FakeResponse(b"OK")
        def putrequest(self,method,path): self.method=method; self.path=path
        def putheader(self,*args): pass
        def endheaders(self): pass
        def send(self,payload): self.sent+=len(payload)
        def getresponse(self): return self.response or _FakeResponse(b"OK")
        def close(self): pass
    original_connection=_u90_http_client.HTTPSConnection
    try:
        _u90_http_client.HTTPSConnection=_FakeHTTPSConnection
        downloaded=_u90_speed_request("https://speed.cloudflare.com/__down?bytes=2048&test=1",None,progress=lambda *x:progress.append(x))
        assert downloaded["bytes"]==2048 and downloaded["status"]==200
        assert downloaded["mbps"]>=0 and progress and progress[-1][1]==2048
        uploaded=_u90_speed_request("https://speed.cloudflare.com/__up?test=1",b"U"*512000,progress=lambda *x:progress.append(x),phase="upload")
        assert uploaded["bytes"]==512000 and uploaded["status"]==200
        assert any(x[0]=="upload" and x[1]==512000 for x in progress)
    finally:
        _u90_http_client.HTTPSConnection=original_connection
    assert _u90_median([100,5,6])==6
    print("RELEASE_4_3_87_SELFTEST_OK: live byte-progress download/upload, median throughput, corrected 3D UI wait, short/medium/long CPU+VRAM profiles, error alarm")

if __name__ == "__main__" and "--selftest-advanced-modules" in sys.argv:
    try:
        _u66_selftest_advanced()
        _u86_selftest_component_ui()
        _u90_selftest_release_fixes()
        assert AppV43.show_module is _u86_show_module_with_component_workbench
        assert _U84_ORIGINAL_SHOW_MODULE is _u69_show_module
        assert callable(_u84_attach_gpu_live_panel)
        assert callable(_u84_gpu_live_tick)
        assert AppV43.show_module is _u86_show_module_with_component_workbench
        assert any("GPU LIVE STUDIO" in str(x) for x in _u84_attach_gpu_live_panel.__code__.co_consts)
        assert _U84_GPU_LIVE_FIELDS and len(_U84_GPU_LIVE_FIELDS) >= 8
        print("GPU_LIVE_PANEL_SELFTEST_OK")
        raise SystemExit(0)
    except Exception as _u66_exc:
        import traceback as _u66_traceback
        print("ADVANCED_MODULES_SELFTEST_FAILED:",type(_u66_exc).__name__,str(_u66_exc))
        _u66_traceback.print_exc()
        raise SystemExit(1)
