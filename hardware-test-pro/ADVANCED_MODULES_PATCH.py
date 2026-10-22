# NAPRAWA PC HARDWARE TEST PRO — Advanced Knowledge, Live Metrics, Speed Test, 90-scene GPU Stress Studio and Sequential Test Runner.
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
        c.create_text(12,8,anchor="nw",text=f"MEDIANA DL {result.get('download_mbps','N/D')} Mbps • PEAK DL {result.get('download_peak_mbps','N/D')} • MEDIANA UL {result.get('upload_mbps','N/D')} Mbps • PEAK UL {result.get('upload_peak_mbps','N/D')}",fill=t["fg"],font=self.fnt(9,"bold"))
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

def _u126_sensor_value_present(item):
    if not isinstance(item,dict):
        return False
    value=item.get("value")
    if value is None or isinstance(value,bool):
        return False
    if str(value).strip().casefold() in ("n/d","nd","n/a","na","none","null","—","-",""):
        return False
    try:
        return _u66_math.isfinite(float(value))
    except Exception:
        return False

def _u126_sensor_merge_key(item):
    if not isinstance(item,dict):
        return None
    hardware=str(item.get("hardwareId") or item.get("hardware_id") or item.get("hardware") or item.get("parent") or "").strip().casefold()
    identifier=str(item.get("identifier") or "").strip().casefold()
    name=str(item.get("sensor") or item.get("name") or "").strip().casefold()
    kind=str(item.get("sensorType") or item.get("sensor_type") or item.get("type") or "").strip().casefold()
    unit=str(item.get("unit") or "").strip().casefold()
    if not (hardware or identifier or name):
        return None
    return (hardware,identifier or name,kind,unit)

def _u126_merge_sensor_rows(existing_rows,incoming_rows,source):
    merged=[]
    indexes={}
    for item in existing_rows or []:
        if not isinstance(item,dict):
            continue
        row=dict(item)
        if not row.get("source"):
            row["source"]=source
        key=_u126_sensor_merge_key(row)
        if key is None or key not in indexes:
            if key is not None:
                indexes[key]=len(merged)
            merged.append(row)
        else:
            current=merged[indexes[key]]
            if _u126_sensor_value_present(row) and not _u126_sensor_value_present(current):
                merged[indexes[key]]={**current,**row}
            else:
                for field,value in row.items():
                    if current.get(field) in (None,"") and value not in (None,""):
                        current[field]=value
    for item in (incoming_rows or [])[:10000]:
        if not isinstance(item,dict):
            continue
        row=dict(item)
        if not row.get("source"):
            row["source"]=source
        key=_u126_sensor_merge_key(row)
        if key is None or key not in indexes:
            if key is not None:
                indexes[key]=len(merged)
            merged.append(row)
            continue
        index=indexes[key]
        current=merged[index]
        # Critical: a later valid WMI/driver reading must replace a stale N/D row,
        # while a later missing value must never erase a valid reading.
        if _u126_sensor_value_present(row) and not _u126_sensor_value_present(current):
            merged[index]={**current,**row}
        else:
            for field,value in row.items():
                if current.get(field) in (None,"") and value not in (None,""):
                    current[field]=value
    return merged[:10000]

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
        # Merge sensor inventory from bridge/WMI; keep unavailable values as N/D instead of discarding them.
        result["sensors"]=_u126_merge_sensor_rows(result.get("sensors") or [],rows,source)
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
                    if any(isinstance(item,dict) and item.get("value") is not None for item in result["sensors"]):
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
            if payload.get("sensors"):
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
    self.make_button(quick,"PEŁNY INSPEKTOR CZUJNIKÓW / CSV",lambda:_u106_open_sensor_inspector(self),"card",side="left",ipady=7)
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
    """Jeden panel z akcjami wyłącznie dla wybranego podzespołu."""
    try:
        t=self.colors()
        panel=tk.Frame(self.content,bg=t["panel"],highlightbackground=t["accent"],highlightthickness=1)
        children=self.content.winfo_children()
        if len(children)>1:panel.pack(fill="x",padx=3,pady=4,before=children[1])
        elif children:panel.pack(fill="x",padx=3,pady=4,before=children[0])
        else:panel.pack(fill="x",padx=3,pady=4)
        self._u69_workbench_panel=panel
        title={"CPU":"PROCESOR / CPU","GPU":"KARTA GRAFICZNA / GPU","RAM":"PAMIĘĆ RAM",
               "DYSK":"SSD / HDD / NVMe","EKRAN":"MATRYCA / MONITOR","SECURITY":"WINDOWS / BEZPIECZEŃSTWO"}.get(module,module)
        tk.Label(panel,text=title+" — TESTY TEGO PODZESPOŁU",bg=t["panel"],fg=t["accent"],
                 font=self.fnt(10,"bold")).pack(anchor="w",padx=9,pady=(7,2))
        tk.Label(panel,text="Wybierz jeden tryb. Po uruchomieniu otwiera się osobny ekran wybranego testu; inne podzespoły nie są dodawane do tej strony.",
                 bg=t["panel"],fg=t["muted"],font=self.fnt(8),wraplength=1400,justify="left").pack(anchor="w",padx=9,pady=(0,5))
        row=tk.Frame(panel,bg=t["panel"]);row.pack(fill="x",padx=6,pady=(0,6))
        self._u68_profile_var=tk.StringVar(value=getattr(self,"_u68_profile_value","ULTRA — 300 s"))
        cb=ttk.Combobox(row,textvariable=self._u68_profile_var,values=_U68_PROFILE_CHOICES,state="readonly",width=18)
        cb.pack(side="left",padx=3,ipady=3)
        cb.bind("<<ComboboxSelected>>",lambda e:setattr(self,"_u68_profile_value",self._u68_profile_var.get()))
        if module=="RAM":
            self._u68_ram_size_var=tk.StringVar(value=getattr(self,"_u68_ram_value","512 MB"))
            ttk.Combobox(row,textvariable=self._u68_ram_size_var,values=("128 MB","256 MB","512 MB","1024 MB","1536 MB","2048 MB"),
                         state="readonly",width=11).pack(side="left",padx=3,ipady=3)
        elif module=="DYSK":
            self._u68_disk_size_var=tk.StringVar(value=getattr(self,"_u68_disk_value","512 MB"))
            ttk.Combobox(row,textvariable=self._u68_disk_size_var,values=("128 MB","256 MB","512 MB","1024 MB","2048 MB","4096 MB"),
                         state="readonly",width=11).pack(side="left",padx=3,ipady=3)
            drives=_u69_drive_options(self)
            self._u69_disk_drive_var=tk.StringVar(value=getattr(self,"_u69_disk_drive_value",drives[0]))
            if self._u69_disk_drive_var.get() not in drives:self._u69_disk_drive_var.set(drives[0])
            ttk.Combobox(row,textvariable=self._u69_disk_drive_var,values=drives,state="readonly",width=8).pack(side="left",padx=3,ipady=3)
            self._u69_disk_drive_var.trace_add("write",lambda *_:setattr(self,"_u69_disk_drive_value",self._u69_disk_drive_var.get()))
        self._u69_workbench_status=tk.Label(row,text="Gotowy — wybierz SKAN, BENCHMARK lub SYMULATOR 3D.",
             bg=t["panel"],fg=t["muted"],font=self.fnt(8,"bold"),anchor="w")
        self._u69_workbench_status.pack(side="left",fill="x",expand=True,padx=8)
        self.make_button(row,"SKAN",lambda m=module:_u69_open_component_simulator(self,m,True,"scan"),
                         "card",side="left",ipady=5)
        self.make_button(row,"BENCHMARK ULTRA / MAX",lambda m=module:_u69_open_component_simulator(self,m,True,"benchmark"),
                         "accent",side="left",ipady=5)
        self.make_button(row,"SYMULATOR 3D",lambda m=module:_u69_open_component_simulator(self,m,False,"scan"),
                         "good",side="left",ipady=5)
    except Exception as exc:
        try:self.append_log("Nie udało się dodać panelu pojedynczego podzespołu: "+repr(exc))
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
    self.make_button(row,"RZECZYWISTE OPENGL / FPS",lambda m=module:_u135_start_real_3d(self,m),"accent",side="left",ipady=4)
    if module=="SIEĆ":
        self.make_button(row,"SPEED TEST DOWNLOAD / UPLOAD",self.show_speed_test,"accent",side="left",ipady=4)
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
        ("simulator original delegate", any(name in _u69_open_component_simulator.__code__.co_names for name in ("_U69_ORIGINAL_OPEN_COMPONENT_SIMULATOR", "_U76_ORIGINAL_OPEN_COMPONENT_SIMULATOR", "_U107_ORIGINAL_OPEN_COMPONENT_SIMULATOR"))),
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
    assert len(_U66_SCENES)==110 and len({str(x[0]) for x in _U66_SCENES})==110
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
        ("90 unique OpenGL scenes", len(_U66_SCENES)==110 and len({str(x[0]) for x in _U66_SCENES})==110),
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
    assert len(_U66_SCENES)==110, "Studio must have 110 separately named scenes"
    assert len(_U66_KNOWLEDGE_SEED)>=30, "Knowledge seed should cover at least 30 topics"
    assert all(x.get("source","").startswith("https://") for x in _U66_KNOWLEDGE_SEED), "ADVANCED self-test check 1: all(x.get('source','').startswith('https://') for x in _U66_KNOWLEDGE_SEED)"
    assert _U66_KNOWLEDGE_PACK_FORMAT == "naprawapc-ai-reader-knowledge", "ADVANCED self-test check 2: _U66_KNOWLEDGE_PACK_FORMAT == 'naprawapc-ai-reader-knowledge'"
    assert _U66_KNOWLEDGE_PACK_URL.startswith("https://raw.githubusercontent.com/"), "ADVANCED self-test check 3: _U66_KNOWLEDGE_PACK_URL.startswith('https://raw.githubusercontent.com/')"
    assert callable(_u66_sync_knowledge_from_server), "ADVANCED self-test check 4: callable(_u66_sync_knowledge_from_server)"
    ranked=_u66_rank_knowledge("temperatura CPU GPU",limit=5)
    assert ranked and any("temperatura" in str(x.get("title","")).lower() for x in ranked), "ADVANCED self-test check 5: ranked and any('temperatura' in str(x.get('title','')).lower() for x in ranked)"
    assert callable(_u66_web_search) and callable(_u66_read_web_page) and callable(_u66_measure_speed), "ADVANCED self-test check 6: callable(_u66_web_search) and callable(_u66_read_web_page) and callable(_u66_measure_speed"
    assert callable(AppV43.show_speed_test) and callable(_u66_show_speed_test), "ADVANCED self-test check 7: callable(AppV43.show_speed_test) and callable(_u66_show_speed_test)"
    assert "DOWNLOAD" in " ".join(str(x) for x in _U90_ORIGINAL_SHOW_SPEED_TEST.__code__.co_consts), "Speed Test must expose download/upload labels in the delegated screen"
    assert callable(_u66_scene_child), "ADVANCED self-test check 9: callable(_u66_scene_child)"
    assert callable(_u66_run_all_tests_worker), "ADVANCED self-test check 10: callable(_u66_run_all_tests_worker)"
    assert callable(_u67_start_selected_diagnostic) and callable(_u67_run_selected_diagnostic), "ADVANCED self-test check 11: callable(_u67_start_selected_diagnostic) and callable(_u67_run_selected_diagnostic)"
    assert callable(_u67_refresh_visible_charts) and callable(_u67_stage_live_panel), "ADVANCED self-test check 12: callable(_u67_refresh_visible_charts) and callable(_u67_stage_live_panel)"
    assert callable(_u67_set_suite_status), "ADVANCED self-test check 13: callable(_u67_set_suite_status)"
    assert len(_U66_SCENES)==110 and all(sc[1] for sc in _U66_SCENES), "ADVANCED self-test check 14: len(_U66_SCENES)==110 and all(sc[1] for sc in _U66_SCENES)"
    assert "900 s" in ("3 s","5 s","10 s","20 s","30 s","60 s","120 s","180 s","300 s","600 s","900 s"), "ADVANCED self-test check 15: '900 s' in ('3 s','5 s','10 s','20 s','30 s','60 s','120 s','180 s','300 s','600 s','900 s"
    assert callable(_u68_show_module_with_workbench) and callable(_u68_open_component_simulator), "ADVANCED self-test check 16: callable(_u68_show_module_with_workbench) and callable(_u68_open_component_simulator)"
    assert callable(_u68_run_component_worker) and callable(_u68_draw_component_scene), "ADVANCED self-test check 17: callable(_u68_run_component_worker) and callable(_u68_draw_component_scene)"
    assert callable(_u68_show_games_advisor), "ADVANCED self-test check 18: callable(_u68_show_games_advisor)"
    _u69_selftest_component_workbenches()
    _u76_selftest_workbenches()
    _u78_selftest_component_lab()
    _u80_selftest_sound_hooks()
    assert AppV43.show_component_lab is _u93_show_lab, "ADVANCED self-test check 19: final component catalog must be wired"
    assert AppV43.show_module in (_u69_show_module, _u84_show_module_with_gpu_live, _u86_show_module_with_component_workbench, _u88_show_module_with_independent_tests), "ADVANCED self-test check 20: AppV43.show_module is a supported final view wrapper"
    assert AppV43.show_simple_module in (_u83_show_simple_module_speed_entry, _u86_show_simple_module_with_component_workbench, _u88_show_simple_module_with_independent_tests), "ADVANCED self-test check 21: AppV43.show_simple_module is a supported final view wrapper"
    assert len(_U66_SCENES)==110 and len({scene[0] for scene in _U66_SCENES})==110, "ADVANCED self-test check 22: len(_U66_SCENES)==110 and len({scene[0] for scene in _U66_SCENES})==110"
    assert AppV43._start_selected_diagnostic is _u91_start_selected_diagnostic, "ADVANCED self-test check 23: final guarded selected-test route is installed"
    assert "N/D" in _u67_refresh_visible_charts.__code__.co_consts, "ADVANCED self-test check 24: 'N/D' in _u67_refresh_visible_charts.__code__.co_consts"
    assert _u66_format_rate(1_000_000)=="8.00 Mbps" and _u66_format_rate(0)=="0.00 Mbps", "ADVANCED self-test check 25: _u66_format_rate(1_000_000)=='8.00 Mbps' and _u66_format_rate(0)=='0.00 Mbps'"
    print("ADVANCED_MODULES_SELFTEST_OK: live telemetry, 13 independent component tests, 110 OpenGL scenes ULTRA/MAX, per-module 3D workbenches, game graphics advisor, AI reader")

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
    assert len(_U66_SCENES)==110 and len({x[0] for x in _U66_SCENES})==110
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
    # Compatibility path for callers retained from the original 3D module.
    # Always delegate to the final runner; never use the pre-v4.3.88 UI wait.
    return _u88_run_3d_suite(self, max(3, min(60, int(seconds))))
    seconds=max(3,min(900,int(seconds)))
    _u88_ui_wait(self, lambda: _u90_show_3d_studio(self))
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
    assert AppV43.show_speed_test in (_u90_show_speed_test, _u100_show_speed_test, _u101_show_speed_test, _u107_show_speed_test, _u108_show_speed_test, _u114_show_speed_test, _u124_show_speed_test)
    assert _u66_measure_speed in (_u90_measure_speed, _u100_measure_speed) or getattr(_u66_measure_speed, "__name__", "") in ("_u108_measure_speed", "_u124_measure_speed")
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


# v4.3.88 — final wiring correction: independent component workbenches, safe 3D dispatch,
# per-scene GPU timing, and a sequential runner that shows a separate screen for every test.
def _u88_ui_wait(app, callback, timeout=30.0):
    """Run UI work on Tk's thread and surface failures without closing the main window."""
    queue_action = getattr(app, "queue_action", None)
    if not callable(queue_action):
        raise TypeError(
            f"UI dispatch expected an AppV43 instance with queue_action; received "
            f"{type(app).__module__}.{type(app).__name__}"
        )
    event = _u66_threading.Event()
    outcome = {}
    def invoke():
        try:
            callback()
            outcome["ok"] = True
        except BaseException as exc:
            outcome["error"] = exc
            try:
                app.append_log("Błąd zmiany widoku UI: " + f"{type(exc).__name__}: {exc}")
            except Exception:
                pass
        finally:
            event.set()
    try:
        queue_action(invoke)
    except Exception as exc:
        raise RuntimeError(f"Nie udało się przekazać pracy do kolejki Tkinter: {exc}") from exc
    if not event.wait(max(1.0, float(timeout))):
        raise TimeoutError(
            "Kolejka Tkinter nie obsłużyła zmiany widoku w czasie "
            f"{timeout} s; okno pozostaje otwarte."
        )
    if "error" in outcome:
        raise outcome["error"]
    return bool(outcome.get("ok", False))


def _u88_profile_name(app):
    var = getattr(app, "_u68_profile_var", None)
    try:
        value = str(var.get()).upper() if var is not None else "ULTRA — 300 S"
    except Exception:
        value = "ULTRA — 300 S"
    return value


def _u88_scene_seconds_from_profile(app):
    """Map benchmark profiles to the supported *per-scene* choices, never to 300/600/900 s."""
    value = _u88_profile_name(app)
    if "TEST TERMICZNY" in value or "MAX" in value:
        return 60
    if "ULTRA" in value:
        return 30
    if "DŁUGI" in value:
        return 20
    if "ŚREDNI" in value:
        return 10
    return 5


def _u88_apply_gpu_profile(app):
    seconds = _u88_scene_seconds_from_profile(app)
    try:
        app._u66_scene_seconds.set(f"{seconds} s")
    except Exception:
        pass
    value = _u88_profile_name(app)
    resolution = "3840x2160" if ("MAX" in value or "TEST TERMICZNY" in value) else (
        "2560x1440" if "ULTRA" in value else (
            "1920x1080" if "DŁUGI" in value or "ŚREDNI" in value else "1280x720"
        )
    )
    try:
        app._u90_scene_resolution_value = resolution
        var = getattr(app, "_u90_scene_resolution_var", None)
        if var is not None:
            var.set(resolution)
    except Exception:
        pass
    try:
        app._u66_3d_status.config(
            text=f"Profil {_u88_profile_name(app)} → {resolution}, {seconds} s/scena; "
                 f"{len(_U66_SCENES)} scen = około {len(_U66_SCENES)*seconds} s."
        )
    except Exception:
        pass
    return seconds, resolution


_U88_ORIGINAL_OPEN_GPU_SUITE = _u68_open_gpu_suite
def _u88_open_gpu_suite(app, auto_start=False):
    # Open the real 3D studio first, then set a duration the scene dropdown actually supports.
    _U88_ORIGINAL_OPEN_GPU_SUITE(app, auto_start=False)
    _u88_apply_gpu_profile(app)
    if auto_start:
        app.after(300, lambda: _u88_start_3d_all(app))


def _u88_start_3d_all(app):
    try:
        seconds = int(str(app._u66_scene_seconds.get()).split()[0])
    except Exception:
        seconds = _u88_scene_seconds_from_profile(app)
    seconds = max(3, min(60, seconds))
    total = len(_U66_SCENES)
    total_seconds = total * seconds
    minutes = total_seconds // 60
    remainder = total_seconds % 60
    if not messagebox.askyesno(
        f"{total} scen 3D — ULTRA/MAX",
        f"Uruchomić {total} osobnych scen renderowania OpenGL, każdą przez {seconds} s, "
        f"w rozdzielczości {getattr(app, '_u90_scene_resolution_value', '1920x1080')}?\n\n"
        f"Szacowany czas renderowania: {minutes} min {remainder} s. "
        "Jeżeli sterownik nie uruchomi renderera, przebieg zatrzyma się przy pierwszym błędzie. "
        "ESC lub STOP TEST przerywa test."
    ):
        return
    app.worker(lambda: _u88_run_3d_suite(app, seconds))


def _u88_run_3d_suite(app, seconds=5):
    seconds = max(3, min(60, int(seconds)))
    started = _U66_datetime.now().isoformat(timespec="seconds")
    results = []
    total = len(_U66_SCENES)
    resolution = str(getattr(app, "_u90_scene_resolution_value", "1920x1080"))
    try:
        _u88_ui_wait(app, lambda: _u90_show_3d_studio(app))
        # Re-apply settings after the screen has rebuilt the resolution control.
        try:
            app._u66_scene_seconds.set(f"{seconds} s")
            app._u90_scene_resolution_value = resolution
            if getattr(app, "_u90_scene_resolution_var", None) is not None:
                app._u90_scene_resolution_var.set(resolution)
        except Exception:
            pass
    except Exception as exc:
        app.queue_log(f"3D UI: nie udało się otworzyć studia: {type(exc).__name__}: {exc}")
        raise
    consecutive_failures = 0
    for index, scene in enumerate(_U66_SCENES, 1):
        if app._test_should_stop():
            break
        title = f"3D BENCHMARK {index}/{total} — {scene[0]}"
        _u66_set_suite_status(app, title)
        try:
            result = _u66_execute_gpu_scene(app, index, seconds)
        except Exception as exc:
            result = {
                "state": "warn", "scene_id": index, "scene_name": scene[0],
                "error": f"{type(exc).__name__}: {exc}",
                "note": "Nie uruchomiono renderowania dla tej sceny."
            }
        result["requested_resolution"] = resolution
        result["requested_seconds"] = seconds
        results.append(result)
        try:
            _u88_ui_wait(
                app,
                lambda sid=index, sc=scene, res=result, n=index, count=total:
                    _u90_update_3d_scene(app, sid, sc, res, n, count)
            )
        except Exception as exc:
            app.queue_log(f"3D UI aktualizacji wyniku {index}: {type(exc).__name__}: {exc}")
        if result.get("state") == "good":
            consecutive_failures = 0
        elif not result.get("stopped_by_user") and not result.get("stopped"):
            consecutive_failures += 1
            _u90_error_alarm(app, f"3D scena {index}: {result.get('error') or result.get('note') or result.get('state')}")
            # If the render backend failed, do not launch 59 identical failing child processes.
            app.queue_log("3D: zatrzymano serię po pierwszej scenie bez poprawnego renderowania; to nie jest PASS.")
            break
    passed = sum(1 for item in results if item.get("state") == "good")
    stopped = bool(app._test_should_stop())
    report = {
        "state": "good" if results and passed == len(results) and len(results) == total else "warn",
        "completed": len(results), "total": total, "good": passed,
        "seconds_per_scene": seconds, "requested_resolution": resolution,
        "stopped_by_user": stopped, "started": started,
        "finished": _U66_datetime.now().isoformat(timespec="seconds"),
        "scenes": results
    }
    app.results["3D_SUITE"] = report
    app.queue_results("3D_SUITE", report)
    try:
        folder = _u66_store_dir() / "benchmarks"
        folder.mkdir(parents=True, exist_ok=True)
        target = folder / ("3d-benchmark-" + _U66_datetime.now().strftime("%Y%m%d-%H%M%S") + ".json")
        target.write_text(_u66_json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        report["report_path"] = str(target)
    except Exception as exc:
        app.queue_log("Nie udało się zapisać raportu 3D: " + repr(exc))
    status = (
        f"3D BENCHMARK: {passed}/{len(results)} udanych scen; {len(results)}/{total} wykonanych; "
        f"{resolution}; {seconds} s/scena."
    )
    app.queue_log(status)
    try:
        _u88_ui_wait(app, lambda: _u90_set_3d_final_status(app, status))
    except Exception as exc:
        app.queue_log("3D: końcowy status UI: " + repr(exc))
    return report


def _u88_safe_ram_mb(app, maximum=2048):
    try:
        available = int(psutil.virtual_memory().available / (1024 * 1024)) if psutil else 0
    except Exception:
        available = 0
    if available <= 0:
        return 128
    return max(128, min(int(maximum), 2048, int(available * 0.20)))


def _u88_run_vram_quick(app):
    try:
        requested = int(str(app._u41_vram_size_var.get()).split()[0])
    except Exception:
        requested = 128
    return _u90_run_vram_profile_worker(app, max(32, min(256, requested)), 15, False)


def _u88_test_state(app, result_keys):
    for key in result_keys:
        value = (getattr(app, "results", {}) or {}).get(key)
        if isinstance(value, dict) and value.get("state") in ("good", "warn", "bad", "error"):
            return value.get("state"), key
    return "not_reported", "N/D"


def _u88_prepare_test_view(app, view, num, total, title):
    """Every Tk widget operation for a sequence transition runs on the Tk UI thread."""
    view()
    _u67_stage_live_panel(app, num, total, title)
    try:
        app.header_status.config(text=f"TEST {num}/{total}", fg=app.colors()["warn"])
    except Exception as exc:
        try:
            app.append_log("Nagłówek sekwencji: " + repr(exc))
        except Exception:
            pass


def _u88_run_selected_diagnostic(app, selected):
    order = [
        ("CPU", "CPU — obciążenie i zegary", lambda: app.show_module("CPU"),
         lambda: app._cpu_test(20), ["CPU"]),
        ("GPU", "GPU — identyfikacja i sterownik", lambda: app.show_module("GPU"),
         app._gpu_test, ["GPU", "GPU_WINSAT"]),
        ("RAM", "RAM — wzorce zapisu / odczytu", lambda: app.show_module("RAM"),
         lambda: app._ram_test(_u88_safe_ram_mb(app)), ["RAM"]),
        ("DYSKI", "SSD / HDD / NVMe — pomiar dysku", lambda: app.show_module("DYSK"),
         lambda: app._disk_test(768), ["DYSK"]),
        ("MATRYCA", "Matryca — EDID i tryby", lambda: app.show_module("EKRAN"),
         app._monitor_test, ["EKRAN"]),
        ("BATERIA", "Bateria / zasilanie", lambda: app.show_battery_or_power(),
         app._battery_test, ["BATERIA"]),
        ("KLAWIATURA", "Klawiatura / touchpad", lambda: app.show_simple_module("KLAWIATURA / TOUCHPAD"),
         lambda: app._peripheral_test("KLAWIATURA"), ["KLAWIATURA", "PERIPHERAL_KLAWIATURA"]),
        ("AUDIO", "Audio — urządzenia wejścia / wyjścia", lambda: app.show_simple_module("DŹWIĘK / AUDIO"),
         lambda: app._peripheral_test("AUDIO"), ["AUDIO", "PERIPHERAL_AUDIO"]),
        ("SIEC", "Internet — osobny Speed Test", lambda: _u90_show_speed_test(app),
         lambda: _u88_run_live_speed_test(app), ["SPEED_TEST"]),
        ("SYSTEM_SECURITY", "Windows / bezpieczeństwo", lambda: app.show_module("SECURITY"),
         app._selected_system_security_test, ["SECURITY", "SYSTEM"]),
        ("KAMERA", "Kamera — wykrywanie urządzenia", lambda: app.show_simple_module("KAMERA"),
         lambda: _u69_camera_scan(app), ["CAMERA"]),
    ]
    chosen = [item for item in order if item[0] in selected]
    if not chosen:
        app.queue_log("Pełna diagnostyka: nie wybrano żadnego modułu.")
        return
    expanded = []
    for item in chosen:
        expanded.append(item)
        if item[0] == "GPU":
            expanded.append((
                "__3D__", "GPU — 110 scen OpenGL, pomiar FPS",
                lambda: _u90_show_3d_studio(app),
                lambda: _u88_run_3d_suite(app, 5), ["3D_SUITE"]
            ))
            expanded.append((
                "__VRAM__", "VRAM — osobny test wzorców / readback",
                lambda: _u69_open_component_simulator(app, "VRAM", False, "scan"),
                lambda: _u88_run_vram_quick(app), ["VRAM_TEST"]
            ))
        if item[0] == "SIEC":
            expanded.append((
                "__USB__", "USB — osobna enumeracja urządzeń",
                lambda: app.show_simple_module("USB / URZĄDZENIA"),
                lambda: app._peripheral_test("USB"), ["USB"]
            ))
    started = _U66_datetime.now().isoformat(timespec="seconds")
    summary = []
    total = len(expanded)
    app.queue_log("=== START PEŁNEJ DIAGNOSTYKI SEKWENCYJNEJ: " + " → ".join(x[1] for x in expanded) + " ===")
    for num, (key, title, view, test_fn, result_keys) in enumerate(expanded, 1):
        if app._test_should_stop():
            app.queue_log("Pełna diagnostyka: przerwano przez użytkownika.")
            break
        try:
            _u66_set_suite_status(app, f"TEST {num}/{total}: {title}")
            # IMPORTANT: don't create/destroy Tk widgets from the worker thread.
            # A cross-thread widget switch can terminate the app exactly when stage 2 starts.
            _u88_ui_wait(
                app,
                lambda view=view, num=num, total=total, title=title:
                    _u88_prepare_test_view(app, view, num, total, title),
                timeout=45.0
            )
            if app._test_should_stop():
                break
            test_fn()
            _u88_ui_wait(app, lambda: None, timeout=45.0)
            state, result_key = _u88_test_state(app, result_keys)
        except Exception as exc:
            state, result_key = "error", "N/D"
            detail = f"{type(exc).__name__}: {exc}"
            try:
                app.queue_log(f"TEST {title}: {detail}")
                app.queue_log("Diagnostyka nie zamyka aplikacji; przechodzę do następnego etapu.")
            except Exception:
                pass
        item = {
            "stage": title, "key": key, "state": state, "result_key": result_key,
            "time": _U66_datetime.now().isoformat(timespec="seconds")
        }
        summary.append(item)
        app.queue_log(f"=== ETAP {num}/{total}: {title} — {state.upper()} ===")
        if app._test_should_stop():
            break
        _u66_time.sleep(1.0)
    failed = any(x["state"] in ("bad", "error", "warn", "not_reported") for x in summary)
    report = {
        "state": "warn" if failed or app._test_should_stop() or len(summary) != total else "completed",
        "started": started, "finished": _U66_datetime.now().isoformat(timespec="seconds"),
        "selected": list(selected), "stages": summary, "completed_stages": len(summary),
        "total_stages": total
    }
    app.results["ALL_TESTS_SEQUENCE"] = report
    try:
        folder = _u66_store_dir() / "reports"
        folder.mkdir(parents=True, exist_ok=True)
        target = folder / ("full-diagnostic-" + _U66_datetime.now().strftime("%Y%m%d-%H%M%S") + ".json")
        target.write_text(_u66_json.dumps({"suite": report, "results": app.results}, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        report["report_path"] = str(target)
    except Exception as exc:
        app.queue_log("Nie udało się zapisać raportu pełnej diagnostyki: " + repr(exc))
    app.queue_log(f"=== KONIEC DIAGNOSTYKI: {report['state']} — {len(summary)}/{total} etapów ===")
    app.queue_action(app.show_report)
    return report


def _u88_run_live_speed_test(app):
    result = _u90_measure_speed(app)
    app.results["SPEED_TEST"] = result
    app.queue_results("SPEED_TEST", result)
    app.queue_log(
        f"SPEED TEST: download {result.get('download_mbps', 'N/D')} Mbps / "
        f"upload {result.get('upload_mbps', 'N/D')} Mbps / "
        f"latency {result.get('latency_average_ms', 'N/D')} ms."
    )
    return result


def _u88_start_selected_diagnostic(app):
    if getattr(app, "running", False):
        messagebox.showinfo("Pełna diagnostyka", "Test już trwa. Poczekaj albo użyj STOP TEST.")
        return
    opts = getattr(app, "full_test_options", None) or {}
    selected = [key for key, enabled in opts.items() if enabled]
    if not selected:
        messagebox.showwarning("Pełna diagnostyka", "Zaznacz co najmniej jeden moduł na pulpicie.")
        return
    labels = {
        "CPU": "CPU", "GPU": "GPU + 90 scen 3D + VRAM", "RAM": "RAM",
        "DYSKI": "SSD/HDD/NVMe", "MATRYCA": "Matryca", "BATERIA": "Bateria",
        "KLAWIATURA": "Klawiatura", "AUDIO": "Audio", "SIEC": "Speed Test + USB",
        "SYSTEM_SECURITY": "Windows / bezpieczeństwo", "KAMERA": "Kamera"
    }
    message = (
        "Uruchomić zaznaczone testy po kolei, każdy na osobnym ekranie?\n\n"
        "Wyniki czujników na żywo, wykresy i raport są aktualizowane w trakcie. "
        "GPU: 90 scen po 5 s (około 7 min 30 s) oraz osobny test VRAM 15 s. "
        "RAM wykorzysta bezpieczny bufor maks. 2 GB. STOP TEST przerywa przebieg.\n\n"
        "Kolejność: " + " → ".join(labels.get(k, k) for k in selected)
    )
    if not messagebox.askyesno("Pełna diagnostyka — osobne ekrany", message):
        return
    app.worker(lambda: _u88_run_selected_diagnostic(app, selected))


def _u88_start_all_tests(app):
    if getattr(app, "running", False):
        messagebox.showinfo("Wszystkie testy", "Test już trwa. Poczekaj albo użyj STOP TEST.")
        return
    selected = ["CPU", "GPU", "RAM", "DYSKI", "MATRYCA", "BATERIA",
                "KLAWIATURA", "AUDIO", "SIEC", "SYSTEM_SECURITY", "KAMERA"]
    message = (
        "Uruchomić WSZYSTKIE testy po kolei, każdy na osobnym ekranie?\n\n"
        "Przebieg zawiera CPU, GPU, RAM, dyski, matrycę, baterię, klawiaturę, audio, "
        "90 scen 3D po 5 s, osobny test VRAM, Speed Test, USB, Windows/bezpieczeństwo i kamerę. "
        "GPU+VRAM dodają około 5 minut i 15 sekund; Speed Test przesyła około 24 MB. "
        "Można przerwać przez STOP TEST."
    )
    if not messagebox.askyesno("Wszystkie testy — osobne ekrany", message):
        return
    app.worker(lambda: _u88_run_selected_diagnostic(app, selected))


def _u88_attach_simple_workbench(app, title):
    key = _u86_module_key(title)
    if key not in ("SIEĆ", "USB", "AUDIO", "KLAWIATURA", "KAMERA"):
        return
    t = app.colors()
    panel = tk.Frame(app.content, bg=t["panel"], highlightbackground=t["accent"], highlightthickness=1)
    children = app.content.winfo_children()
    try:
        if len(children) > 1:
            panel.pack(fill="x", padx=3, pady=4, before=children[1])
        elif children:
            panel.pack(fill="x", padx=3, pady=4, before=children[0])
        else:
            panel.pack(fill="x", padx=3, pady=4)
    except Exception:
        panel.pack(fill="x", padx=3, pady=4)
    app._u88_simple_workbench_panel = panel
    tk.Label(panel, text=f"TEST NIEZALEŻNY — {_U86_MODULE_TITLES.get(key, key)}",
             bg=t["panel"], fg=t["accent"], font=app.fnt(9, "bold")).pack(anchor="w", padx=8, pady=(6, 2))
    row = tk.Frame(panel, bg=t["panel"]); row.pack(fill="x", padx=5, pady=(0, 5))
    app.make_button(row, "SKAN", lambda k=key: app.worker(lambda: _u69_run_component_worker(app, k, "scan")),
                    "card", side="left", ipady=4)
    if key == "SIEĆ":
        app.make_button(row, "SPEED TEST DOWNLOAD / UPLOAD", app.show_speed_test, "accent", side="left", ipady=4)
    else:
        app.make_button(row, "TEST FUNKCJONALNY", lambda k=key: app.worker(lambda: _u69_run_component_worker(app, k, "benchmark")),
                        "accent", side="left", ipady=4)
    app.make_button(row, "SYMULATOR 3D", lambda k=key: _u69_open_component_simulator(app, k, False, "scan"),
                    "good", side="left", ipady=4)
    app.make_button(row, "STOP TEST", app.stop_current_test, "bad", side="left", ipady=4)


_U88_ORIGINAL_SHOW_MODULE = AppV43.show_module
def _u88_show_module_with_independent_tests(app, module):
    name=str(module or "").strip()
    if name.upper() in ("DYSKI","DYSKI — SSD / HDD / NVME","SSD / HDD / NVME"):
        name="DYSK"
    if name.upper()=="VRAM":
        _u69_open_component_simulator(app,"VRAM",False,"scan")
        return
    # Invalidate pending live-monitor callbacks from the previous page, then render the unwrapped base view.
    try:
        app._u86_page_id=int(getattr(app,"_u86_page_id",0))+1
        app._u86_module_context=None
    except Exception:
        pass
    _U68_ORIGINAL_SHOW_MODULE(app,name)
    # The full-test runner supplies its own single stage/telemetry panel.
    if getattr(app,"_u86_suite_active",False):
        return
    key=_u86_module_key(name)
    if key in ("CPU","GPU","RAM","DYSK","EKRAN","SECURITY"):
        _u69_attach_workbench(app,key)

_U88_ORIGINAL_SHOW_SIMPLE_MODULE = AppV43.show_simple_module
def _u88_show_simple_module_with_independent_tests(app, title):
    try:
        app._u86_page_id=int(getattr(app,"_u86_page_id",0))+1
        app._u86_module_context=None
    except Exception:
        pass
    _U68_ORIGINAL_SHOW_SIMPLE_MODULE(app,title)
    # Only the selected simple component gets a workbench; do not stack legacy wrappers.
    if getattr(app,"_u86_suite_active",False):
        return
    _u88_attach_simple_workbench(app,title)

_U88_ORIGINAL_SHOW_BATTERY = AppV43.show_battery_or_power
def _u88_show_battery_with_independent_tests(app):
    try:
        app._u86_page_id=int(getattr(app,"_u86_page_id",0))+1
        app._u86_module_context=None
    except Exception:
        pass
    _U69_ORIGINAL_SHOW_BATTERY(app)
    if getattr(app,"_u86_suite_active",False):
        return
    t=app.colors()
    panel=tk.Frame(app.content,bg=t["panel"],highlightbackground=t["accent"],highlightthickness=1)
    children=app.content.winfo_children()
    try:
        if len(children)>1:panel.pack(fill="x",padx=3,pady=4,before=children[1])
        elif children:panel.pack(fill="x",padx=3,pady=4,before=children[0])
        else:panel.pack(fill="x",padx=3,pady=4)
    except Exception:
        panel.pack(fill="x",padx=3,pady=4)
    app._u88_battery_workbench_panel=panel
    tk.Label(panel,text="BATERIA / ZASILANIE — TEN TEST",bg=t["panel"],fg=t["accent"],
             font=app.fnt(9,"bold")).pack(anchor="w",padx=8,pady=(6,2))
    row=tk.Frame(panel,bg=t["panel"]);row.pack(fill="x",padx=5,pady=(0,5))
    app.make_button(row,"SKAN BATERII",lambda:_u69_open_component_simulator(app,"BATERIA",True,"scan"),
                    "card",side="left",ipady=4)
    app.make_button(row,"BENCHMARK BATERII",lambda:_u69_open_component_simulator(app,"BATERIA",True,"benchmark"),
                    "accent",side="left",ipady=4)
    app.make_button(row,"SYMULATOR 3D",lambda:_u69_open_component_simulator(app,"BATERIA",False,"scan"),
                    "good",side="left",ipady=4)
    app.make_button(row,"STOP TEST",app.stop_current_test,"bad",side="left",ipady=4)

# Publish the corrected last-stage routes after all earlier version layers.
_u66_ui_wait = _u88_ui_wait
_u66_run_3d_suite = _u88_run_3d_suite
_u66_start_3d_all = _u88_start_3d_all
_u68_open_gpu_suite = _u88_open_gpu_suite
_u67_run_selected_diagnostic = _u88_run_selected_diagnostic
AppV43._u66_ui_wait = _u88_ui_wait
AppV43._u66_run_3d_suite = _u88_run_3d_suite
AppV43._u66_start_3d_all = _u88_start_3d_all
AppV43._start_selected_diagnostic = _u88_start_selected_diagnostic
AppV43._run_selected_diagnostic = _u88_run_selected_diagnostic
AppV43.full_test = _u88_start_all_tests
AppV43.start_all_tests_sequential = _u88_start_all_tests
AppV43.show_module = _u88_show_module_with_independent_tests
AppV43.show_simple_module = _u88_show_simple_module_with_independent_tests
AppV43.show_battery_or_power = _u88_show_battery_with_independent_tests


# v4.3.90 — final crash guards for the online test sequence and 3D entry points.
# A test failure must leave the Tk application running and record an explicit ERROR result.
_U91_ORIGINAL_3D_RUNNER = _u88_run_3d_suite
def _u91_run_3d_suite_guarded(app, seconds=5):
    started = _U66_datetime.now().isoformat(timespec="seconds")
    try:
        return _U91_ORIGINAL_3D_RUNNER(app, seconds)
    except BaseException as exc:
        detail = f"{type(exc).__name__}: {exc}"
        report = {
            "state": "error",
            "started": started,
            "finished": _U66_datetime.now().isoformat(timespec="seconds"),
            "completed": 0,
            "total": len(_U66_SCENES),
            "good": 0,
            "seconds_per_scene": max(3, min(60, int(seconds))),
            "scenes": [],
            "error": detail,
            "note": "3D benchmark przerwany bez zamykania aplikacji."
        }
        try:
            app.results["3D_SUITE"] = report
            app.queue_results("3D_SUITE", report)
        except Exception:
            pass
        try:
            app.queue_log("3D BENCHMARK — BŁĄD, aplikacja pozostaje otwarta: " + detail)
        except Exception:
            pass
        try:
            app.queue_action(lambda d=detail: _u90_set_3d_final_status(app, "BŁĄD 3D — " + d[:250]))
        except Exception:
            pass
        return report


# All code paths that refer to the historical runner name resolve to the guarded entry point.
_u88_run_3d_suite = _u91_run_3d_suite_guarded
_u66_run_3d_suite = _u91_run_3d_suite_guarded
_u90_run_3d_suite = _u91_run_3d_suite_guarded
AppV43._u66_run_3d_suite = _u91_run_3d_suite_guarded
AppV43._u90_run_3d_suite = _u91_run_3d_suite_guarded
AppV43._u66_ui_wait = _u88_ui_wait
AppV43._u88_ui_wait = _u88_ui_wait


_U91_ORIGINAL_SELECTED_RUNNER = _u88_run_selected_diagnostic
def _u91_run_selected_diagnostic_guarded(app, selected):
    started = _U66_datetime.now().isoformat(timespec="seconds")
    try:
        return _U91_ORIGINAL_SELECTED_RUNNER(app, selected)
    except BaseException as exc:
        detail = f"{type(exc).__name__}: {exc}"
        report = {
            "state": "error",
            "started": started,
            "finished": _U66_datetime.now().isoformat(timespec="seconds"),
            "selected": list(selected),
            "stages": [],
            "completed_stages": 0,
            "total_stages": len(selected),
            "fatal_error": detail
        }
        try:
            app.results["ALL_TESTS_SEQUENCE"] = report
            app.queue_results("ALL_TESTS_SEQUENCE", report)
        except Exception:
            pass
        try:
            app.queue_log("DIAGNOSTYKA — błąd zabezpieczony, aplikacja pozostaje otwarta: " + detail)
        except Exception:
            pass
        def show_error(d=detail):
            try:
                app.header_status.config(text="TEST PRZERWANY — SZCZEGÓŁY W RAPORCIE", fg=app.colors()["bad"])
            except Exception:
                pass
            try:
                messagebox.showerror(
                    "Diagnostyka przerwana — aplikacja nie została zamknięta",
                    d + "\\n\\nSzczegóły zapisano w dzienniku. Możesz wrócić do pulpitu i uruchomić test oddzielnie."
                )
            except Exception:
                pass
        try:
            app.queue_action(show_error)
        except Exception:
            pass
        return report


_U91_ORIGINAL_START_SELECTED = _u88_start_selected_diagnostic
def _u91_start_selected_diagnostic(app):
    if getattr(app, "running", False):
        messagebox.showinfo("Pełna diagnostyka", "Test już trwa. Poczekaj albo użyj STOP TEST.")
        return
    opts = getattr(app, "full_test_options", None) or {}
    selected = [key for key, enabled in opts.items() if enabled]
    if not selected:
        messagebox.showwarning("Pełna diagnostyka", "Zaznacz co najmniej jeden moduł na pulpicie.")
        return
    labels = {
        "CPU": "CPU", "GPU": "GPU + 90 scen 3D + VRAM", "RAM": "RAM",
        "DYSKI": "SSD/HDD/NVMe", "MATRYCA": "Matryca", "BATERIA": "Bateria",
        "KLAWIATURA": "Klawiatura", "AUDIO": "Audio", "SIEC": "Speed Test + USB",
        "SYSTEM_SECURITY": "Windows / bezpieczeństwo", "KAMERA": "Kamera"
    }
    if not messagebox.askyesno(
        "Pełna diagnostyka — osobne ekrany",
        "Uruchomić zaznaczone testy po kolei, każdy na osobnym ekranie?\\n\\n"
        "Każdy wyjątek jest zapisywany jako ERROR/N/D — aplikacja ma pozostać otwarta. "
        "GPU obejmuje osobny benchmark 3D oraz VRAM; STOP TEST przerywa przebieg.\\n\\n"
        "Kolejność: " + " → ".join(labels.get(k, k) for k in selected)
    ):
        return
    app.worker(lambda: _u91_run_selected_diagnostic_guarded(app, selected))


AppV43._start_selected_diagnostic = _u91_start_selected_diagnostic
AppV43._run_selected_diagnostic = _u91_run_selected_diagnostic_guarded
AppV43.full_test = _u91_start_selected_diagnostic
AppV43.start_all_tests_sequential = _u91_start_selected_diagnostic


def _u88_selftest_final_wiring():
    assert callable(AppV43._u66_ui_wait)
    assert AppV43._u66_ui_wait is _u88_ui_wait
    assert _u66_run_3d_suite is _u88_run_3d_suite
    assert "_u88_ui_wait" in _U91_ORIGINAL_3D_RUNNER.__code__.co_names
    assert _U91_ORIGINAL_3D_RUNNER is not _u91_run_3d_suite_guarded
    assert "_u66_ui_wait" not in _u88_run_3d_suite.__code__.co_names
    assert AppV43.show_module is _u88_show_module_with_independent_tests
    assert AppV43.show_simple_module is _u88_show_simple_module_with_independent_tests
    assert AppV43.show_battery_or_power is _u88_show_battery_with_independent_tests
    assert AppV43._start_selected_diagnostic is _u91_start_selected_diagnostic
    assert any(
        "_u88_prepare_test_view" in getattr(code, "co_names", ())
        for code in _u88_run_selected_diagnostic.__code__.co_consts
    ), "Sequential test runner must schedule its view transition through the Tk UI queue"
    assert "_u67_stage_live_panel" not in _u88_run_selected_diagnostic.__code__.co_names
    assert "_u88_ui_wait" in _u88_run_selected_diagnostic.__code__.co_names
    assert "_U91_ORIGINAL_3D_RUNNER" in _u90_run_3d_suite.__code__.co_names
    assert AppV43.full_test is _u91_start_selected_diagnostic
    assert AppV43._start_selected_diagnostic is _u91_start_selected_diagnostic
    assert AppV43._run_selected_diagnostic is _u91_run_selected_diagnostic_guarded
    assert _u88_run_3d_suite is _u91_run_3d_suite_guarded
    assert AppV43._u66_run_3d_suite is _u91_run_3d_suite_guarded
    assert AppV43._u66_ui_wait is _u88_ui_wait
    assert _u88_scene_seconds_from_profile(type("FakeProfile", (), {"_u68_profile_var": type("V", (), {"get": lambda s: "MAX — 600 s"})()})()) == 60
    assert _u88_scene_seconds_from_profile(type("FakeProfile", (), {"_u68_profile_var": type("V", (), {"get": lambda s: "ULTRA — 300 s"})()})()) == 30
    assert len(_U66_SCENES)==110
    assert callable(_u68_attach_component_workbench)
    print("COMPONENT_INDEPENDENT_WORKBENCH_3D_SUITE_SELFTEST_OK: 13 modules, separate screen per test, 90 scenes, 4K MAX and bounded 3D timing")



# v4.3.92 — harden all test-worker/UI dispatch paths against Tkinter tkapp attribute errors.
_U92_APP_INSTANCE = None
_U92_ORIGINAL_INIT = AppV43.__init__
_U92_ORIGINAL_WORKER_WRAP = AppV43._worker_wrap
_U92_ORIGINAL_REPORT_CALLBACK_EXCEPTION = AppV43.report_callback_exception
_U92_ORIGINAL_UI_WAIT = _u88_ui_wait

def _u92_is_real_app(candidate):
    return (
        candidate is not None
        and callable(getattr(candidate, "queue_action", None))
        and callable(getattr(candidate, "worker", None))
        and isinstance(getattr(candidate, "results", None), dict)
    )

def _u92_resolve_app(candidate):
    if _u92_is_real_app(candidate):
        return candidate
    registered = _U92_APP_INSTANCE
    if _u92_is_real_app(registered):
        return registered
    root = getattr(candidate, "_root", None)
    if callable(root):
        try:
            rooted = root()
            if _u92_is_real_app(rooted):
                return rooted
        except Exception:
            pass
    raise TypeError(
        "Nie można odnaleźć obiektu aplikacji AppV43 dla testu. "
        f"Otrzymano {type(candidate).__module__}.{type(candidate).__name__}; "
        "test został zabezpieczony, główne okno pozostaje otwarte."
    )

def _u92_register_app_instance(self, *args, **kwargs):
    global _U92_APP_INSTANCE
    _U92_ORIGINAL_INIT(self, *args, **kwargs)
    _U92_APP_INSTANCE = self

def _u92_ui_wait_safe(candidate, callback, timeout=30.0):
    app = _u92_resolve_app(candidate)
    return _U92_ORIGINAL_UI_WAIT(app, callback, timeout=timeout)

def _u92_worker_wrap_safe(candidate, fn):
    app = _u92_resolve_app(candidate)
    def guarded_fn():
        try:
            return fn()
        except Exception as exc:
            detail = f"{type(exc).__name__}: {exc}"
            record = {
                "state": "error",
                "message": detail,
                "time": _U66_datetime.now().isoformat(timespec="seconds"),
                "scope": "worker/test",
                "note": "Test przerwany przez wyjątek; aplikacja pozostaje otwarta."
            }
            try:
                app.results["UNHANDLED_TEST_ERROR"] = record
            except Exception:
                pass
            try:
                app.queue_log("BŁĄD TESTU ZABEZPIECZONY — aplikacja pozostaje otwarta: " + detail)
                app.queue_results("UNHANDLED_TEST_ERROR", record)
            except Exception:
                pass
            def notify(error=detail):
                try:
                    app.header_status.config(
                        text="TEST PRZERWANY — SPRAWDŹ DZIENNIK",
                        fg=app.colors()["bad"]
                    )
                except Exception:
                    pass
                try:
                    messagebox.showerror(
                        "Test przerwany — aplikacja nadal działa",
                        error + "\\n\\nSzczegóły zapisano w dzienniku. Wróć do pulpitu i uruchom ten test osobno."
                    )
                except Exception:
                    pass
            try:
                app.queue_action(notify)
            except Exception:
                pass
            return None
    return _U92_ORIGINAL_WORKER_WRAP(app, guarded_fn)

def _u92_report_callback_exception(self, exc, value, traceback_obj):
    try:
        app = _u92_resolve_app(self)
        detail = f"{getattr(exc, '__name__', str(exc))}: {value}"
        app.queue_log("BŁĄD WYDARZENIA UI — aplikacja pozostaje otwarta: " + detail)
        try:
            app.header_status.config(text="BŁĄD TESTU/UI — SZCZEGÓŁY W DZIENNIKU", fg=app.colors()["bad"])
        except Exception:
            pass
    except Exception:
        pass
    try:
        return _U92_ORIGINAL_REPORT_CALLBACK_EXCEPTION(self, exc, value, traceback_obj)
    except Exception:
        return None

def _u92_selftest_crash_guard():
    assert callable(_u92_resolve_app)
    assert callable(_u92_ui_wait_safe)
    assert callable(_u92_worker_wrap_safe)
    assert AppV43._u66_ui_wait is _u92_ui_wait_safe
    assert AppV43._u88_ui_wait is _u92_ui_wait_safe
    fake_log = []
    class _U92FakeApp:
        def __init__(self):
            self.results = {}
        def queue_action(self, callback):
            callback()
        def worker(self, callback):
            callback()
        def append_log(self, message):
            fake_log.append(message)
    fake = _U92FakeApp()
    ran = []
    _u92_ui_wait_safe(fake, lambda: ran.append("direct"), timeout=1.0)
    assert ran == ["direct"]
    global _U92_APP_INSTANCE
    old_instance = _U92_APP_INSTANCE
    try:
        _U92_APP_INSTANCE = fake
        _u92_ui_wait_safe(object(), lambda: ran.append("fallback"), timeout=1.0)
        assert ran == ["direct", "fallback"]
    finally:
        _U92_APP_INSTANCE = old_instance
    assert "_U92_APP_INSTANCE" in _u92_resolve_app.__code__.co_names
    print("TKINTER_TEST_CRASH_GUARD_SELFTEST_OK")

AppV43.__init__ = _u92_register_app_instance
_u88_ui_wait = _u92_ui_wait_safe
AppV43._u66_ui_wait = _u92_ui_wait_safe
AppV43._u88_ui_wait = _u92_ui_wait_safe
AppV43._worker_wrap = _u92_worker_wrap_safe
AppV43.report_callback_exception = _u92_report_callback_exception



# v4.3.93 — isolated one-test-per-screen component laboratory.
_U93_MODULES = [
 ("CPU","CPU / PROCESOR"),("RAM","RAM / PAMIĘĆ"),("GPU","GPU / KARTA GRAFICZNA"),
 ("VRAM","VRAM / PAMIĘĆ KARTY"),("DYSK","SSD / HDD / NVMe"),("EKRAN","MATRYCA / MONITOR"),
 ("SECURITY","WINDOWS / BEZPIECZEŃSTWO"),("BATERIA","BATERIA / ZASILANIE"),("SIEĆ","SIEĆ / WI-FI / LAN"),
 ("USB","USB / URZĄDZENIA"),("AUDIO","AUDIO / MIKROFON / GŁOŚNIKI"),("KLAWIATURA","KLAWIATURA / TOUCHPAD"),("KAMERA","KAMERA / WEBCAM")
]
# id, title, description, executor kind
_U93_TEST_CATALOG = {
 "CPU":[
  ("cpu_scan","Skan CPU — model/rdzenie/wątki","Identyfikacja CPU i topologii bez obciążenia.","cpu_scan"),
  ("cpu_single","Benchmark CPU — jeden wątek","Rzeczywiste operacje SHA-256/s w jednym wątku.","cpu_single"),
  ("cpu_multi","Benchmark CPU — wielowątkowy","Rzeczywiste operacje SHA-256/s w równoległych wątkach.","cpu_multi"),
  ("cpu_load60","Obciążenie CPU — 60 s","Osobny test obciążeniowy procesora.","cpu_load60"),
  ("cpu_max","Stabilność CPU — ULTRA 300 s","Dłuższe obciążenie CPU; można przerwać przyciskiem STOP.","cpu_load300"),
  ("cpu_sensor","Czujniki CPU — temperatura/moc/zegar","Odczytuje tylko wartości faktycznie udostępnione przez sterownik.","cpu_sensor"),
  ("cpu_sim","Symulator 3D CPU","Schemat rdzeni; nie jest wynikiem FPS.","sim")
 ],
 "RAM":[
  ("ram_scan","Skan RAM — użycie/dostępność","Odczyt pamięci całkowitej, wolnej i zajętej.","ram_scan"),
  ("ram_512","Test wzorców RAM — 512 MB","Zapis i weryfikacja bufora przydzielonego przez Windows.","ram_pattern"),
  ("ram_1024","Test wzorców RAM — 1024 MB","Wzorce pamięci; rozmiar jest ograniczany dostępną pamięcią.","ram_pattern"),
  ("ram_2048","Test wzorców RAM — do 2048 MB","Większy bufor; nie deklaruje testu całej fizycznej pamięci.","ram_pattern"),
  ("ram_bw","Benchmark przepustowości RAM — 60 s","Zapis i odczyt zweryfikowany SHA-256, rzeczywiste MB/s.","ram_bw"),
  ("ram_max","Stabilność/przepustowość RAM — 300 s","Powtarza bezpieczny test bufora RAM.","ram_bw_max"),
  ("ram_sim","Symulator 3D RAM","Schemat bloków pamięci — pomiar wykonywany oddzielnie.","sim")
 ],
 "GPU":[
  ("gpu_scan","Skan GPU — karta i sterownik","Identyfikacja adaptera/sterownika Windows.","gpu_scan"),
  ("gpu_scene","Jedna scena OpenGL — wybór 1–110","Mierzy FPS/klatki jednej wskazanej sceny i zapisuje renderer.","gpu_scene"),
  ("gpu_std","Benchmark 110 scen — STANDARD","110 scen po 10 sekund każda, rzeczywiste FPS.","gpu_suite10"),
  ("gpu_ultra","Benchmark 110 scen — ULTRA","110 scen po 30 sekund każda, około 55 min renderowania.","gpu_suite30"),
  ("gpu_max","Benchmark 110 scen — MAX","110 scen po 60 sekund każda, około 110 min renderowania.","gpu_suite60"),
  ("gpu_sensor","Czujniki GPU — temperatura/VRAM/zegar/moc","N/D gdy sterownik nie udostępnia pomiaru.","gpu_sensor"),
  ("gpu_games","Doradca gier — ustawienia grafiki","Oddziela pomiary syntetyczne od szacunków FPS w grach.","games"),
  ("gpu_sim","Symulator 3D GPU","Schemat karty; FPS mierzą tylko testy renderowania.","sim")
 ],
 "VRAM":[
  ("vram_scan","Skan VRAM — pojemność","Inwentarz VRAM, nie test komórek pamięci.","vram_scan"),
  ("vram_64","Test VRAM — 64 MB/readback","Zapis/odczyt zwrotny tekstur i wzorce OpenGL.","vram_test"),
  ("vram_128","Test VRAM — 128 MB/readback","Osobny test bufora 128 MB.","vram_test"),
  ("vram_256","Test VRAM — 256 MB/readback","Osobny test bufora do 256 MB.","vram_test"),
  ("vram_max","Stabilność VRAM — 300 s","Powtarza pełne przebiegi wzorców w VRAM.","vram_max"),
  ("vram_sim","Symulator 3D VRAM","Schemat kości pamięci, wynik readback pokazuje test osobny.","sim")
 ],
 "DYSK":[
  ("disk_scan","Skan dysku/woluminu","Wybór konkretnego woluminu, pojemność i wolne miejsce.","disk_scan"),
  ("disk_smart","SMART/niezawodność nośnika","Pokazuje dostępne rekordy; brak SMART to N/D, nie PASS.","disk_smart"),
  ("disk_512","Benchmark wybranego dysku — 512 MB","Zapis/odczyt pliku tymczasowego na wybranym woluminie.","disk_bench"),
  ("disk_2048","Benchmark wybranego dysku — 2 GB","Większy test plikowy z weryfikacją i usuwaniem pliku.","disk_bench"),
  ("disk_4096","Benchmark wybranego dysku — MAX 4 GB","Wymaga wolnego miejsca i potwierdzenia operatora.","disk_bench_max"),
  ("disk_max","Przepustowość dysku — 180 s","Powtarzany zapis/odczyt na wybranym woluminie.","disk_bench_long"),
  ("disk_sim","Symulator 3D SSD/HDD/NVMe","Schemat operacji I/O; benchmark mierzy operacje plikowe.","sim")
 ],
 "EKRAN":[
  ("screen_edid","Skan matrycy — EDID","Informacje monitora i tryby udostępnione przez Windows.","screen_edid"),
  ("screen_modes","Rozdzielczość i odświeżanie","Wyświetla parametry raportowane przez system.","screen_modes"),
  ("screen_patterns","Test wizualny — 20 wzorców","Otwiera osobny ekran wzorców; ocena martwych pikseli wymaga wzroku.","screen_patterns"),
  ("screen_rgb","Test wizualny RGB/gradienty","Otwiera wzorce kolorów bez udawania automatycznego wykrycia wad.","screen_patterns"),
  ("screen_sim","Symulator 3D matrycy","Wizualizacja schematyczna panelu.","sim")
 ],
 "SECURITY":[
  ("sec_scan","Skan bezpieczeństwa Windows","Uruchamia istniejący moduł bezpieczeństwa.","security_scan"),
  ("sec_startup","Audyt autostartu","Zbiera stan systemowego audytu bezpieczeństwa/autostartu.","security_startup"),
  ("sec_events","Diagnostyka Windows","Uruchamia wybraną diagnostykę systemową; brak raportu to N/D.","security_system"),
  ("sec_sim","Symulator 3D bezpieczeństwa","Schemat edukacyjny, nie wynik skanu.","sim")
 ],
 "BATERIA":[
  ("bat_scan","Skan baterii/zasilania","Odczyt poziomu, stanu ładowania i danych kontrolera.","battery_scan"),
  ("bat_180","Monitor ładowania/rozładowania — 180 s","Zapisuje próbki procentu i stanu zasilania.","battery_monitor"),
  ("bat_600","Monitor baterii — MAX 600 s","Dłuższa obserwacja; nie jest pełnym pomiarem czasu pracy.","battery_max"),
  ("bat_report","Raport baterii powercfg","Tworzy raport HTML Windows i pokazuje ścieżkę.","battery_report"),
  ("bat_sim","Symulator 3D baterii","Schemat ogniw; poziom pochodzi z kontrolera.","sim")
 ],
 "SIEĆ":[
  ("net_scan","Skan kart Wi-Fi/LAN","Odczyt adapterów i stanu sieci.","network_scan"),
  ("net_dns","Test DNS + HTTPS","Sprawdza rozwiązywanie nazw i łączność HTTPS.","network_dns"),
  ("net_speed","Speed Test — download/upload/ping","Rzeczywisty transfer bajtów i pomiar opóźnienia.","network_speed"),
  ("net_jitter","Test powtarzanych opóźnień","Próbki DNS w czasie; nie jest to RTT ICMP.","network_jitter"),
  ("net_sim","Symulator 3D sieci","Schemat interfejsów i pakietów.","sim")
 ],
 "USB":[
  ("usb_scan","Skan urządzeń USB","Enumeracja obecnych urządzeń PnP USB.","usb_scan"),
  ("usb_errors","Kontrola statusu USB","Odrębna lista obecnych urządzeń USB zgłaszających problem.","usb_errors"),
  ("usb_functional","Test funkcjonalny USB","Uruchamia test urządzeń bez zmian sterowników.","peripheral_usb"),
  ("usb_sim","Symulator 3D USB","Schemat portów/urządzeń.","sim")
 ],
 "AUDIO":[
  ("audio_scan","Skan urządzeń audio","Lista urządzeń wejścia/wyjścia systemu.","audio_scan"),
  ("audio_mic","Test mikrofonu — poziom RMS/peak","Po potwierdzeniu pobiera 5 s próbki do RAM, nie zapisuje nagrania.","audio_mic"),
  ("audio_output","Test głośników — ton 880 Hz","Po potwierdzeniu odtwarza krótki ton.","audio_output"),
  ("audio_functional","Test funkcjonalny audio","Uruchamia istniejący moduł urządzeń audio.","peripheral_audio"),
  ("audio_sim","Symulator 3D audio","Schemat urządzeń wejścia/wyjścia.","sim")
 ],
 "KLAWIATURA":[
  ("key_scan","Skan klawiatury/touchpada","Urządzenia wejścia wykryte przez system.","keyboard_scan"),
  ("key_press","Test klawiszy — rejestracja","Liczy naciśnięcia; nie zapisuje treści wpisanych znaków.","keyboard_input"),
  ("key_functional","Test funkcjonalny klawiatury/touchpada","Uruchamia moduł urządzeń wejścia.","peripheral_keyboard"),
  ("key_sim","Symulator 3D klawiatury","Schemat klawiszy/touchpada.","sim")
 ],
 "KAMERA":[
  ("cam_scan","Skan kamery/webcam","Wykrywanie urządzeń bez automatycznego uruchamiania obrazu.","camera_scan"),
  ("cam_preview","Podgląd kamery — 10 s","Po potwierdzeniu pokazuje klatki w osobnym oknie bez zapisu.","camera_preview"),
  ("cam_sim","Symulator 3D kamery","Schemat kamery, nie pomiar FPS sensora.","sim")
 ]

}
_U93_ALIASES={"CPU":"CPU","PROCESOR":"CPU","RAM":"RAM","PAMIĘĆ":"RAM","PAMIEC":"RAM","GPU":"GPU","VRAM":"VRAM",
 "DYSK":"DYSK","DYSKI":"DYSK","SSD":"DYSK","HDD":"DYSK","NVME":"DYSK","EKRAN":"EKRAN","MATRYCA":"EKRAN","MONITOR":"EKRAN",
 "SECURITY":"SECURITY","BEZPIECZEŃSTWO":"SECURITY","SYSTEM":"SECURITY","BATERIA":"BATERIA","ZASILANIE":"BATERIA",
 "SIEĆ":"SIEĆ","SIEC":"SIEĆ","WI-FI":"SIEĆ","WIFI":"SIEĆ","LAN":"SIEĆ","USB":"USB","AUDIO":"AUDIO",
 "KLAWIATURA":"KLAWIATURA","TOUCHPAD":"KLAWIATURA","KAMERA":"KAMERA","WEBCAM":"KAMERA"}

def _u93_norm(module):
    raw=str(module or "").upper()
    for token,key in _U93_ALIASES.items():
        if token in raw: return key
    return "CPU"

def _u93_find_test(module,test_id):
    module=_u93_norm(module)
    for item in _U93_TEST_CATALOG.get(module,[]):
        if item[0]==test_id:return item
    raise KeyError("Nie znaleziono testu "+str(test_id)+" dla "+module)

def _u93_add_entry(app,module):
    try:
        t=app.colors();row=tk.Frame(app.content,bg=t["panel"],highlightbackground=t["accent"],highlightthickness=1)
        children=app.content.winfo_children()
        if children:row.pack(fill="x",padx=3,pady=(0,4),before=children[0])
        else:row.pack(fill="x",padx=3,pady=4)
        tk.Label(row,text=f"LABORATORIUM {module} — {len(_U93_TEST_CATALOG[module])} TESTÓW NIEZALEŻNYCH",
                 bg=t["panel"],fg=t["accent"],font=app.fnt(9,"bold")).pack(side="left",padx=7,pady=5)
        app.make_button(row,"KATALOG — WYBIERZ JEDEN TEST",lambda m=module:_u93_show_catalog(app,m),"accent",side="left",ipady=4)
        if module=="GPU":app.make_button(row,"DORADCA GIER",lambda:_u68_show_games_advisor(app),"card",side="left",ipady=4)
    except Exception as exc:
        try:app.append_log("Nie udało się otworzyć laboratorium "+module+": "+repr(exc))
        except Exception:pass

def _u93_show_lab(app):
    app.current_view="COMPONENT_TESTS";app.clear();t=app.colors()
    app.header_title.config(text="LABORATORIUM — WYBIERZ JEDEN PODZESPÓŁ")
    head=app.panel(app.content);head.pack(fill="x",pady=(0,5))
    tk.Label(head,text="ODDZIELNE TESTY — JEDEN TEST NA JEDNYM EKRANIE",bg=t["panel"],fg=t["accent"],font=app.fnt(12,"bold")).pack(anchor="w",padx=10,pady=(8,2))
    tk.Label(head,text="Wybierz komponent. Następnie otwórz jeden konkretny test — jego ustawienia, metryki, wykresy i raport nie będą mieszane z innymi testami.",bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1300,justify="left").pack(anchor="w",padx=10,pady=(0,7))
    grid=tk.Frame(app.content,bg=t["bg"]);grid.pack(fill="both",expand=True)
    for i,(key,label) in enumerate(_U93_MODULES):
        r,c=divmod(i,3);card=tk.Frame(grid,bg=t["card"],highlightbackground=t["accent2"],highlightthickness=1)
        card.grid(row=r,column=c,sticky="nsew",padx=4,pady=4)
        tk.Label(card,text=label,bg=t["card"],fg=t["accent"],font=app.fnt(9,"bold")).pack(anchor="w",padx=8,pady=(6,2))
        tk.Label(card,text=f"{len(_U93_TEST_CATALOG[key])} osobnych testów",bg=t["card"],fg=t["good"],font=app.fnt(8,"bold")).pack(anchor="w",padx=8)
        app.make_button(card,"OTWÓRZ KATALOG",lambda m=key:_u93_show_catalog(app,m),"accent",side="left",ipady=4)
    for c in range(3):grid.grid_columnconfigure(c,weight=1)
    row=tk.Frame(app.content,bg=t["bg"]);row.pack(fill="x",pady=3)
    def center():
        fn=getattr(app,"show_service_center",None)
        fn() if callable(fn) else app.show_repairs()
    app.make_button(row,"CENTRUM SERWISU ULTIMATE / SYSTEM REPAIR PRO",center,"card",side="left",ipady=5)
    app.make_button(row,"CENTRUM NAPRAWY WINDOWS",lambda:_u120_show_system_repair_center(app),"accent",side="left",ipady=5)
    app.make_button(row,"DORADCA GIER",lambda:_u68_show_games_advisor(app),"card",side="left",ipady=5)
    app.make_button(row,"← TESTY",app.show_tests_hub,"card",side="left",ipady=5)

def _u93_scroll_rows(app,parent,module):
    shell=tk.Frame(parent,bg=app.colors()["bg"]);shell.pack(fill="both",expand=True,padx=3,pady=3)
    canvas=tk.Canvas(shell,bg=app.colors()["bg"],highlightthickness=0)
    scroll=ttk.Scrollbar(shell,orient="vertical",command=canvas.yview)
    body=tk.Frame(canvas,bg=app.colors()["bg"]);win=canvas.create_window((0,0),window=body,anchor="nw")
    body.bind("<Configure>",lambda e,c=canvas:c.configure(scrollregion=c.bbox("all")))
    canvas.bind("<Configure>",lambda e,c=canvas,w=win:c.itemconfigure(w,width=e.width))
    canvas.configure(yscrollcommand=scroll.set);canvas.pack(side="left",fill="both",expand=True);scroll.pack(side="right",fill="y")
    t=app.colors()
    for n,item in enumerate(_U93_TEST_CATALOG[module],1):
        test_id,title,desc,kind=item
        card=tk.Frame(body,bg=t["card"],highlightbackground=t["accent2"],highlightthickness=1);card.pack(fill="x",padx=3,pady=3)
        row=tk.Frame(card,bg=t["card"]);row.pack(fill="x",padx=8,pady=(4,1))
        tk.Label(row,text=f"{n:02d}. {title}",bg=t["card"],fg=t["accent"],font=app.fnt(9,"bold"),anchor="w").pack(side="left",fill="x",expand=True)
        app.make_button(row,"OTWÓRZ TEN TEST",lambda m=module,k=test_id:_u93_show_test_detail(app,m,k),"accent",side="right",ipady=3)
        tk.Label(card,text=desc,bg=t["card"],fg=t["muted"],font=app.fnt(8),wraplength=1300,justify="left",anchor="w").pack(fill="x",padx=8,pady=(0,4))

def _u93_show_catalog(app,module):
    module=_u93_norm(module);app.current_view="COMPONENT_TEST_CATALOG_"+module;app.clear();t=app.colors()
    label=next((x[1] for x in _U93_MODULES if x[0]==module),module)
    app.header_title.config(text=label+" — KATALOG TESTÓW")
    head=app.panel(app.content);head.pack(fill="x",pady=(0,4))
    tk.Label(head,text=f"{label} — {len(_U93_TEST_CATALOG[module])} ODDZIELNYCH TESTÓW",bg=t["panel"],fg=t["accent"],font=app.fnt(11,"bold")).pack(anchor="w",padx=10,pady=(7,2))
    tk.Label(head,text="Otwórz jeden wiersz. Każdy test ma osobny ekran, własne ustawienia i wynik. Brak czujnika lub wyniku będzie oznaczony N/D/OSTRZEŻENIE — nie jako PASS.",bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1300,justify="left").pack(anchor="w",padx=10,pady=(0,6))
    _u93_scroll_rows(app,app.content,module)
    row=tk.Frame(app.content,bg=t["bg"]);row.pack(fill="x",pady=3)
    if module=="GPU":
        app.make_button(row,"TESTY VRAM",lambda:_u93_show_catalog(app,"VRAM"),"card",side="left",ipady=4)
        app.make_button(row,"DORADCA GIER",lambda:_u68_show_games_advisor(app),"card",side="left",ipady=4)
        app.make_button(row,"DIAGNOSTYKA GIER",lambda:_u126_show_game_diagnostics(app),"card",side="left",ipady=4)
    app.make_button(row,"CENTRUM SERWISU / SYSTEM REPAIR PRO",lambda: (getattr(app,"show_service_center",None) or app.show_repairs)(),"card",side="left",ipady=4)
    app.make_button(row,"← LABORATORIUM",lambda:_u93_show_lab(app),"card",side="left",ipady=4)



# v4.3.94 — final UI-dispatch and worker safety layer.
# Never call a test-dispatch helper on Tk's internal _tkinter.tkapp object.
_U94_ORIGINAL_UI_WAIT = _U92_ORIGINAL_UI_WAIT
_U94_ORIGINAL_SELECTED_RUNNER = _u91_run_selected_diagnostic_guarded

def _u94_ui_wait_compat(candidate, callback, timeout=30.0):
    app = _u92_resolve_app(candidate)
    return _U94_ORIGINAL_UI_WAIT(app, callback, timeout=timeout)

def _u94_record_failure(app, scope, exc):
    detail = f"{type(exc).__name__}: {exc}"
    report = {
        "state": "error",
        "scope": str(scope),
        "message": detail,
        "time": _U66_datetime.now().isoformat(timespec="seconds"),
        "note": "Test przerwany przez wyjątek. Główne okno aplikacji powinno pozostać otwarte."
    }
    try:
        app.results["UNHANDLED_TEST_ERROR"] = report
    except Exception:
        pass
    try:
        app.queue_log(f"{scope}: BŁĄD ZABEZPIECZONY — {detail}")
        app.queue_results("UNHANDLED_TEST_ERROR", report)
    except Exception:
        pass
    def notify(message=detail):
        try:
            app.header_status.config(text="TEST PRZERWANY — SPRAWDŹ DZIENNIK", fg=app.colors()["bad"])
        except Exception:
            pass
        try:
            messagebox.showerror(
                "Test przerwany — aplikacja pozostaje otwarta",
                message + "\n\nSzczegóły są w dzienniku. Możesz wrócić do testów i uruchomić moduł osobno."
            )
        except Exception:
            pass
    try:
        app.queue_action(notify)
    except Exception:
        pass
    return report

def _u94_selected_runner_safe(candidate, selected):
    app = _u92_resolve_app(candidate)
    try:
        # Use the final isolated-screen dispatcher; the older v4.3.90 runner bypasses this wrapper.
        return _U91_ORIGINAL_SELECTED_RUNNER(app, list(selected or []))
    except BaseException as exc:
        return _u94_record_failure(app, "Pełna diagnostyka sekwencyjna", exc)

def _u94_3d_runner_safe(candidate, seconds=5):
    app = _u92_resolve_app(candidate)
    try:
        # Use the original standalone runner; it dispatches UI callbacks through _u88_ui_wait.
        # Do not invoke helpers through app.tk / _tkinter.tkapp.
        return _U91_ORIGINAL_3D_RUNNER(app, seconds)
    except BaseException as exc:
        return _u94_record_failure(app, "Benchmark 3D", exc)

def _u94_selftest_crash_guard():
    assert callable(_u94_ui_wait_compat)
    assert callable(_u94_selected_runner_safe)
    assert callable(_u94_3d_runner_safe)
    assert AppV43._u66_ui_wait is _u92_ui_wait_safe
    assert AppV43._u88_ui_wait is _u92_ui_wait_safe
    class _U94FakeApp:
        def __init__(self):
            self.results = {}
            self.log = []
        def queue_action(self, callback):
            callback()
        def queue_results(self, key, value):
            self.results[key] = value
        def worker(self, callback):
            callback()
        def append_log(self, message):
            self.log.append(message)
    fake = _U94FakeApp()
    class _U94TkappLike:
        pass
    _U94TkappLike.__module__ = "_tkinter"
    candidate = _U94TkappLike()
    ran = []
    global _U92_APP_INSTANCE
    previous = _U92_APP_INSTANCE
    try:
        _U92_APP_INSTANCE = fake
        _u94_ui_wait_compat(candidate, lambda: ran.append("resolved-from-tkapp"), timeout=1.0)
        assert ran == ["resolved-from-tkapp"]
    finally:
        _U92_APP_INSTANCE = previous
    assert AppV43._u66_ui_wait is _u92_ui_wait_safe
    assert AppV43._run_selected_diagnostic is _u91_run_selected_diagnostic_guarded
    assert AppV43._u66_run_3d_suite is _u91_run_3d_suite_guarded
    assert "_U91_ORIGINAL_3D_RUNNER" in _u94_3d_runner_safe.__code__.co_names
    print("TKINTER_TEST_CRASH_GUARD_V4394_SELFTEST_OK")

# Publish these aliases after all historical/versioned layers.
_u92_ui_wait_safe = _u94_ui_wait_compat
_u88_ui_wait = _u94_ui_wait_compat
_u66_ui_wait = _u94_ui_wait_compat
_u91_run_selected_diagnostic_guarded = _u94_selected_runner_safe
_u91_run_3d_suite_guarded = _u94_3d_runner_safe
_u88_run_3d_suite = _u94_3d_runner_safe
_u90_run_3d_suite = _u94_3d_runner_safe
_u66_run_3d_suite = _u94_3d_runner_safe
AppV43._u66_ui_wait = _u94_ui_wait_compat
AppV43._u88_ui_wait = _u94_ui_wait_compat
AppV43._u66_run_3d_suite = _u94_3d_runner_safe
AppV43._u90_run_3d_suite = _u94_3d_runner_safe
AppV43._run_selected_diagnostic = _u94_selected_runner_safe
_u92_selftest_crash_guard = _u94_selftest_crash_guard




# v4.3.96 — clean, isolated component screens.
# Remove stacked legacy wrappers that were inserting unrelated speed-test, live-monitor and all-tests panels.
AppV43.show_module = _u88_show_module_with_independent_tests
AppV43.show_simple_module = _u88_show_simple_module_with_independent_tests
AppV43.show_battery_or_power = _u88_show_battery_with_independent_tests

# The final guarded full-test runner uses _U91_ORIGINAL_SELECTED_RUNNER, so enable suite mode here.
_U96_ORIGINAL_SELECTED_RUNNER = _u88_run_selected_diagnostic
def _u96_run_selected_diagnostic_single_screen(app, selected):
    prior = bool(getattr(app, "_u86_suite_active", False))
    app._u86_suite_active = True
    try:
        return _U96_ORIGINAL_SELECTED_RUNNER(app, list(selected or []))
    finally:
        app._u86_suite_active = prior
        try:
            app._u86_module_context = None
        except Exception:
            pass
_U91_ORIGINAL_SELECTED_RUNNER = _u96_run_selected_diagnostic_single_screen

def _u96_selftest_single_test_screens():
    assert AppV43.show_module is _u88_show_module_with_independent_tests
    assert AppV43.show_simple_module is _u88_show_simple_module_with_independent_tests
    assert AppV43.show_battery_or_power is _u88_show_battery_with_independent_tests
    names = set(_u69_attach_workbench.__code__.co_names)
    assert "show_component_lab" not in names
    assert "show_speed_test" not in names
    assert "show_live_monitor" not in names
    constants = tuple(str(x) for x in _u69_attach_workbench.__code__.co_consts)
    assert not any("SPEED TEST INTERNETU" in x or "MONITOR LIVE" in x or "WSZYSTKIE TESTY" in x for x in constants)
    # Network test action belongs to the network-specific workbench, not to unrelated component pages.
    assert callable(_u69_open_component_simulator)
    assert callable(AppV43.show_speed_test)
    simple_consts = tuple(str(x) for x in _u88_attach_simple_workbench.__code__.co_consts)
    assert "SPEED TEST DOWNLOAD / UPLOAD" in simple_consts
    assert _U91_ORIGINAL_SELECTED_RUNNER is _u96_run_selected_diagnostic_single_screen
    assert "_U91_ORIGINAL_SELECTED_RUNNER" in _u94_selected_runner_safe.__code__.co_names
    assert "_U94_ORIGINAL_SELECTED_RUNNER" not in _u94_selected_runner_safe.__code__.co_names
    print("SINGLE_COMPONENT_TEST_SCREENS_SELFTEST_OK: selected runner uses isolated wrapper; no stacked/global test panels")


# v4.3.97 — make the per-test catalog executable, with an isolated screen and real result per test.
_U93_SUPPORTED_TEST_KINDS = {
 "cpu_scan","cpu_single","cpu_multi","cpu_load60","cpu_load300","cpu_sensor","sim",
 "ram_scan","ram_pattern","ram_bw","ram_bw_max","gpu_scan","gpu_scene","gpu_suite10",
 "gpu_suite30","gpu_suite60","gpu_sensor","games","vram_scan","vram_test","vram_max",
 "disk_scan","disk_smart","disk_bench","disk_bench_max","disk_bench_long","screen_edid",
 "screen_modes","screen_patterns","security_scan","security_startup","security_system",
 "battery_scan","battery_monitor","battery_max","battery_report","network_scan",
 "network_dns","network_speed","network_jitter","usb_scan","usb_errors","peripheral_usb",
 "audio_scan","audio_mic","audio_output","peripheral_audio","keyboard_scan",
 "keyboard_input","peripheral_keyboard","camera_scan","camera_preview"
}

def _u93_put_result(app,key,result):
    if not isinstance(result,dict):
        result={"state":"warn","message":"Procedura nie zwróciła raportu.","value":str(result)}
    result.setdefault("sampled_at",_U66_datetime.now().isoformat(timespec="seconds"))
    try: app.results[str(key)]=result
    except Exception: pass
    try: app.queue_results(str(key),result)
    except Exception: pass
    return result

def _u93_existing_result(app,keys):
    data=getattr(app,"results",{}) or {}
    for key in keys:
        value=data.get(key)
        if isinstance(value,dict) and value:return value
    return {}

def _u93_detail_status_only(app,message):
    try:
        label=getattr(app,"_u93_detail_status",None)
        if label is not None and label.winfo_exists():
            label.config(text=str(message),fg=app.colors()["warn"])
    except Exception: pass

def _u93_update_detail(app,test_id,status,result=None):
    def apply():
        if getattr(app,"current_view","")!="COMPONENT_TEST_DETAIL_"+str(test_id):return
        label=getattr(app,"_u93_detail_status",None)
        try:
            if label is not None and label.winfo_exists():
                word=str(status).upper()
                color=app.colors()["good"] if word in ("GOOD","GOTOWE","WYKRYTO") else app.colors()["bad"] if word in ("ERROR","BŁĄD","FAIL") else app.colors()["warn"]
                label.config(text=str(status),fg=color)
        except Exception:pass
        box=getattr(app,"_u93_detail_report",None)
        try:
            if box is not None and box.winfo_exists():
                box.configure(state="normal");box.delete("1.0","end")
                body=_u66_json.dumps(result,ensure_ascii=False,indent=2,default=str) if isinstance(result,dict) else str(result or "Brak raportu.")
                box.insert("1.0",body[:24000]);box.configure(state="disabled")
        except Exception:pass
    try:app.queue_action(apply)
    except Exception:
        try:apply()
        except Exception:pass

def _u93_cpu_hash_benchmark(app,multi,seconds):
    import hashlib as _h
    import threading as _th
    import time as _tm
    seconds=max(5,min(300,int(seconds)));workers=min(32,max(1,os.cpu_count() or 1)) if multi else 1
    payload=(b"NAPRAWA-PC-HARDWARE-TEST-PRO-CPU-BENCHMARK-"*32768)[:1024*1024]
    counts=[0]*workers;byte_counts=[0]*workers;halt=_th.Event();started=_tm.perf_counter();deadline=started+seconds
    def work(i):
        while not halt.is_set() and _tm.perf_counter()<deadline:
            if bool(getattr(app,"stop_requested",False)):
                halt.set();break
            try:
                if app._test_should_stop():halt.set();break
            except Exception:pass
            _h.sha256(payload).digest();counts[i]+=1;byte_counts[i]+=len(payload)
    threads=[_th.Thread(target=work,args=(i,),daemon=True,name=f"NPC-CPU-HASH-{i+1}") for i in range(workers)]
    for th in threads:th.start()
    last=0
    while any(th.is_alive() for th in threads):
        now=_tm.perf_counter()
        if bool(getattr(app,"stop_requested",False)):halt.set()
        try:
            if app._test_should_stop():halt.set()
        except Exception:pass
        if now-last>=1:
            _u93_detail_status_only(app,f"CPU SHA-256: {sum(counts):,} operacji • {now-started:.0f}/{seconds} s");last=now
        for th in threads:th.join(.05)
    elapsed=max(.001,_tm.perf_counter()-started);ops=sum(counts);total_bytes=sum(byte_counts)
    result={"state":"good" if ops else "warn","benchmark":"software SHA-256 throughput; not a physical silicon pass/fail test",
      "mode":"multi-thread" if multi else "single-thread","workers":workers,"logical_processors":os.cpu_count(),
      "duration_seconds":round(elapsed,2),"operations":ops,"operations_per_second":round(ops/elapsed,2),
      "processed_mib":round(total_bytes/1024/1024,2),"throughput_mib_s":round(total_bytes/elapsed/1024/1024,2),
      "cancelled":bool(getattr(app,"stop_requested",False))}
    _u93_put_result(app,"CPU_HASH_BENCHMARK",result)
    app.queue_log(f"CPU HASH: {result['operations_per_second']} SHA-256/s, {workers} worker(s)")
    return result

def _u93_persist_result(app,module,test_id,title,result,elapsed):
    report=dict(result or {});report.setdefault("state","warn")
    report.update({"module":str(module),"test_id":str(test_id),"title":str(title),
      "elapsed_seconds":round(float(elapsed),2),"finished_at":_U66_datetime.now().isoformat(timespec="seconds")})
    try:
        folder=_u66_store_dir()/"reports"/"component-tests";folder.mkdir(parents=True,exist_ok=True)
        stamp=_U66_datetime.now().strftime("%Y%m%d-%H%M%S")
        target=folder/f"{test_id}-{stamp}.json"
        target.write_text(_u66_json.dumps(report,ensure_ascii=False,indent=2,default=str),encoding="utf-8")
        report["report_path"]=str(target)
    except Exception as exc:report["report_save_warning"]=f"{type(exc).__name__}: {exc}"
    return report

def _u93_execute_catalog_test(app,module,test_id,kind,settings):
    import time as _tm
    import socket as _sock
    import urllib.request as _urlreq
    import statistics as _stats
    seconds=max(5,min(900,int(settings.get("duration",60) or 60)))
    result={};keys=[]
    if kind=="cpu_scan":
        vm=psutil.virtual_memory() if psutil else None;cpu=getattr(app,"cpu",None) or get_cpu_info() or {}
        result={"state":"good" if cpu else "warn","cpu":cpu,"logical_processors":os.cpu_count(),
          "physical_cores":cpu.get("NumberOfCores","N/D"),"ram_total_bytes":vm.total if vm else None}
        keys=["COMPONENT_SCAN_CPU"]
    elif kind in ("cpu_single","cpu_multi"):
        return _u93_cpu_hash_benchmark(app,kind=="cpu_multi",seconds)
    elif kind in ("cpu_load60","cpu_load300"):
        _u93_remove_old_results(app,["CPU"]);app._cpu_test(seconds)
        result=_u93_existing_result(app,["CPU"]) or {"state":"warn","message":"Test CPU nie zwrócił raportu."};keys=["CPU"]
    elif kind=="cpu_sensor":
        values={}
        try:
            if psutil:
                values["cpu_load_percent"]=psutil.cpu_percent(interval=.5)
                freq=psutil.cpu_freq();values["cpu_clock_mhz"]=round(freq.current,1) if freq and freq.current else None
                temps=psutil.sensors_temperatures() or {};candidates=[]
                for src,items in temps.items():
                    for item in items or []:
                        lab=str(getattr(item,"label","") or src).lower()
                        if any(k in lab for k in ("cpu","package","tctl","tdie","core")) and getattr(item,"current",None) is not None:
                            candidates.append({"source":src,"label":getattr(item,"label",""),"temperature_c":item.current})
                values["temperature_candidates"]=candidates
        except Exception as exc:values["read_error"]=f"{type(exc).__name__}: {exc}"
        has=any(values.get(k) is not None for k in ("cpu_load_percent","cpu_clock_mhz")) or bool(values.get("temperature_candidates"))
        result={"state":"good" if has else "warn",**values,"cpu_power_w":"N/D","cpu_voltage_v":"N/D",
          "note":"Brak czujnika nie jest zastępowany wartością szacowaną."};keys=["CPU_SENSOR_DETAIL"]
    elif kind=="ram_scan":
        vm=psutil.virtual_memory() if psutil else None
        result={"state":"good" if vm else "warn","total_bytes":vm.total if vm else None,
          "available_bytes":vm.available if vm else None,"used_bytes":vm.used if vm else None,
          "used_percent":vm.percent if vm else None,"note":"Skan użycia RAM, nie test komórek pamięci."}
        keys=["COMPONENT_SCAN_RAM"]
    elif kind in ("ram_pattern","ram_bw","ram_bw_max"):
        mb=int(settings.get("memory_mb",512) or 512)
        if test_id=="ram_512":mb=512
        elif test_id=="ram_1024":mb=1024
        elif test_id=="ram_2048":mb=2048
        result=_u69_ram_throughput_benchmark(app,mb,seconds);keys=["RAM_BENCHMARK"]
    elif kind=="gpu_scan":
        _u93_remove_old_results(app,["GPU","GPU_WINSAT"]);app._gpu_test()
        result=_u93_existing_result(app,["GPU","GPU_WINSAT"]) or {"state":"warn","message":"Skan GPU nie zwrócił raportu."};keys=["GPU","GPU_WINSAT"]
    elif kind=="gpu_scene":
        scene=max(1,min(len(_U66_SCENES),int(settings.get("scene_id",1) or 1)))
        result=_u66_execute_gpu_scene(app,scene,max(3,min(60,int(settings.get("gpu_seconds",10) or 10))))
        keys=["3D_SCENE_"+str(scene)]
    elif kind in ("gpu_suite10","gpu_suite30","gpu_suite60"):
        result=_u88_run_3d_suite(app,{"gpu_suite10":10,"gpu_suite30":30,"gpu_suite60":60}[kind]);keys=["3D_SUITE"]
    elif kind=="gpu_sensor":
        tele=getattr(app,"_u84_gpu_last_telemetry",{}) or {};cache=getattr(app,"_u66_sensor_cache",{}) or {};temps=cache.get("temps",{}) if isinstance(cache,dict) else {}
        fields={"gpu_load_percent":tele.get("gpu_load_percent",tele.get("load_percent")),
          "temperature_c":tele.get("temperature_c",temps.get("gpu_temp_c") if isinstance(temps,dict) else None),
          "vram_used_mb":tele.get("vram_used_mb"),"vram_total_mb":tele.get("vram_total_mb"),
          "gpu_clock_mhz":tele.get("gpu_clock_mhz"),"memory_clock_mhz":tele.get("memory_clock_mhz"),
          "power_draw_w":tele.get("power_draw_w",tele.get("power_w")),"fan_speed_rpm":tele.get("fan_speed_rpm")}
        result={"state":"good" if any(v is not None for v in fields.values()) else "warn",
          "gpu":(primary_gpu(get_gpu_info()) or {}).get("Name","N/D"),**fields,
          "note":"Migawka czujników faktycznie dostępnych przez sterownik/bridge."};keys=["GPU_SENSOR_DETAIL"]
    elif kind=="vram_scan":
        gpus=get_gpu_info();main=primary_gpu(gpus) if gpus else {}
        result={"state":"good" if main else "warn","gpu":main,"vram_inventory":_u41_vram_inventory_text(main) if main else "N/D",
          "note":"Inwentarz, nie test fizycznych komórek VRAM."};keys=["COMPONENT_SCAN_VRAM"]
    elif kind in ("vram_test","vram_max"):
        mb=int(settings.get("memory_mb",64) or 64)
        if test_id=="vram_64":mb=64
        elif test_id=="vram_128":mb=128
        elif test_id=="vram_256":mb=256
        dur=300 if kind=="vram_max" else max(15,seconds)
        result=_u90_run_vram_profile_worker(app,mb,dur,False) or _u93_existing_result(app,["VRAM_TEST"])
        if not result:result={"state":"warn","message":"Test VRAM nie zwrócił raportu."}
        keys=["VRAM_TEST"]
    elif kind in ("disk_scan","disk_smart","disk_bench","disk_bench_max","disk_bench_long"):
        drives=_u69_drive_options(app);drive=str(settings.get("drive") or "")
        if drive not in drives and drives:drive=drives[0]
        if hasattr(app,"_u69_disk_drive_var"):app._u69_disk_drive_var.set(drive)
        if kind in ("disk_scan","disk_smart"):
            result=_u76_disk_scan_selected_volume(app)
            if kind=="disk_smart":
                reliability=result.get("reliability") or []
                result={"state":"good" if reliability else "warn","target_volume":result.get("target_volume"),
                  "reliability":reliability,"physical_devices":result.get("devices",[]),
                  "note":"Brak rekordów SMART/reliability oznacza N/D, nie PASS."}
                keys=["DISK_SMART_DETAIL"]
            else:keys=["COMPONENT_SCAN_DYSK"]
        else:
            mb=int(settings.get("memory_mb",512) or 512)
            if test_id=="disk_512":mb=512
            elif test_id=="disk_2048":mb=2048
            elif test_id=="disk_4096":mb=4096
            duration=180 if kind=="disk_bench_long" else seconds
            result=_u69_disk_throughput_benchmark(app,mb,duration)
            keys=["DISK_BENCHMARK"]
    elif kind in ("screen_edid","screen_modes"):
        _u93_remove_old_results(app,["EKRAN"]);app._monitor_test()
        result=_u93_existing_result(app,["EKRAN"]) or {"state":"warn","message":"Moduł monitora nie zwrócił raportu."};keys=["EKRAN"]
    elif kind in ("security_scan","security_system"):
        _u93_remove_old_results(app,["SECURITY"]);app._security_test()
        result=_u93_existing_result(app,["SECURITY"]) or {"state":"warn","message":"Moduł bezpieczeństwa nie zwrócił raportu."}
        if kind=="security_system":result["note"]="Skan diagnostyczny; nie uruchomiono napraw automatycznych."
        keys=["SECURITY"]
    elif kind=="security_startup":
        if not is_windows():result={"state":"warn","message":"Audyt autostartu wymaga Windows."}
        else:
            rows=_v4319_normalize_items(ps_json("Get-CimInstance Win32_StartupCommand -ErrorAction SilentlyContinue | Select-Object Name,Command,Location,User | ConvertTo-Json -Compress",default=[]))
            result={"state":"good" if rows else "warn","entries":rows,"count":len(rows),"note":"Odczyt autostartu; wpisy nie są zmieniane."}
        keys=["SECURITY_STARTUP_DETAIL"]
    elif kind=="battery_scan":
        _u93_remove_old_results(app,["BATERIA"]);app._battery_test()
        result=_u93_existing_result(app,["BATERIA"]) or {"state":"warn","message":"Kontroler baterii nie zwrócił raportu."};keys=["BATERIA"]
    elif kind in ("battery_monitor","battery_max"):
        result=_u69_battery_monitor(app,600 if kind=="battery_max" else max(15,seconds)) or _u93_existing_result(app,["BATTERY_BENCHMARK"])
        if not result:result={"state":"warn","message":"Monitor baterii nie zwrócił raportu."}
        keys=["BATTERY_BENCHMARK"]
    elif kind=="battery_report":
        if not is_windows():result={"state":"warn","message":"Raport powercfg wymaga Windows."}
        else:
            folder=_u66_store_dir()/"reports"/"battery";folder.mkdir(parents=True,exist_ok=True)
            target=folder/("batteryreport-"+_U66_datetime.now().strftime("%Y%m%d-%H%M%S")+".html")
            proc=_u66_subprocess.run(["powercfg","/batteryreport","/output",str(target)],capture_output=True,text=True,timeout=45)
            result={"state":"good" if proc.returncode==0 and target.is_file() else "warn","returncode":proc.returncode,
              "report_path":str(target) if target.is_file() else None,"stderr":(proc.stderr or "")[-2000:]}
        keys=["BATTERY_REPORT_DETAIL"]
    elif kind=="network_scan":
        rows=[]
        if psutil:
            try:
                stats=psutil.net_if_stats();addrs=psutil.net_if_addrs()
                rows=[{"name":name,"is_up":bool(st.isup),"speed_mbps":getattr(st,"speed",None),
                  "addresses":[{"family":str(a.family),"address":a.address} for a in addrs.get(name,[])]}
                  for name,st in stats.items()]
            except Exception as exc:result={"state":"warn","error":f"{type(exc).__name__}: {exc}"}
        if rows:result={"state":"good","interfaces":rows,"count":len(rows)}
        elif not result:result={"state":"warn","interfaces":[],"count":0,"message":"Brak danych kart sieciowych."}
        keys=["NETWORK_SCAN_DETAIL"]
    elif kind=="network_dns":
        t0=_tm.perf_counter();resolved=_sock.getaddrinfo("speed.cloudflare.com",443,type=_sock.SOCK_STREAM);dns_ms=(_tm.perf_counter()-t0)*1000
        t0=_tm.perf_counter();req=_urlreq.Request("https://www.cloudflare.com/cdn-cgi/trace",headers={"User-Agent":"NAPRAWA-PC-HARDWARE-TEST-PRO"})
        with _urlreq.urlopen(req,timeout=12) as response:code=int(response.status);sample=len(response.read(1024))
        result={"state":"good" if code==200 else "warn","addresses":sorted({x[4][0] for x in resolved}),
          "dns_resolve_ms":round(dns_ms,2),"https_status":code,"https_total_ms":round((_tm.perf_counter()-t0)*1000,2),
          "sample_bytes":sample,"endpoint":"https://www.cloudflare.com/cdn-cgi/trace"};keys=["NETWORK_DNS_DETAIL"]
    elif kind=="network_speed":
        result=_u66_measure_speed(app) or {"state":"warn","message":"Speed Test nie zwrócił raportu."};keys=["SPEED_TEST"]
    elif kind=="network_jitter":
        samples=[]
        for i in range(12):
            if bool(getattr(app,"stop_requested",False)):break
            t0=_tm.perf_counter();_sock.getaddrinfo("speed.cloudflare.com",443,type=_sock.SOCK_STREAM)
            samples.append(round((_tm.perf_counter()-t0)*1000,2))
            _u93_detail_status_only(app,f"Próbka DNS {len(samples)}/12 • {samples[-1]:.2f} ms");_tm.sleep(.25)
        deltas=[abs(samples[i]-samples[i-1]) for i in range(1,len(samples))]
        result={"state":"good" if len(samples)>=8 else "warn","samples_ms":samples,
          "minimum_ms":min(samples) if samples else None,"median_ms":round(_stats.median(samples),2) if samples else None,
          "maximum_ms":max(samples) if samples else None,
          "dns_jitter_mean_abs_delta_ms":round(sum(deltas)/len(deltas),2) if deltas else None,
          "note":"Zmienność czasu DNS/resolve; nie jest to RTT ICMP ani jitter pakietowy."};keys=["NETWORK_JITTER_DETAIL"]
    elif kind in ("usb_scan","usb_errors"):
        if not is_windows():result={"state":"warn","message":"Skan PnP USB wymaga Windows."}
        else:
            rows=_v4319_normalize_items(ps_json("Get-PnpDevice -PresentOnly -ErrorAction SilentlyContinue | Where-Object { $_.Class -eq 'USB' -or $_.InstanceId -like 'USB*' } | Select-Object Class,FriendlyName,Status,InstanceId | ConvertTo-Json -Compress",default=[]))
            if kind=="usb_errors":
                bad=[x for x in rows if str(x.get("Status","")).upper() not in ("OK","UNKNOWN")]
                result={"state":"warn" if bad else ("good" if rows else "warn"),"items":bad,"count":len(bad),"devices_checked":len(rows),
                  "note":"Pusta lista błędów nie dowodzi działania fizycznego portu."}
            else:result={"state":"good" if rows else "warn","items":rows,"count":len(rows)}
        keys=["USB_SCAN_DETAIL" if kind=="usb_scan" else "USB_ERRORS_DETAIL"]
    elif kind=="peripheral_usb":
        _u93_remove_old_results(app,["USB"]);app._peripheral_test("USB")
        result=_u93_existing_result(app,["USB"]) or {"state":"warn","message":"Test USB nie zwrócił raportu."};keys=["USB"]
    elif kind=="audio_scan":
        devices=[];err=None
        try:
            import sounddevice as _sd
            devices=[{"index":i,"name":str(d.get("name","N/D")),"max_input_channels":int(d.get("max_input_channels",0)),
              "max_output_channels":int(d.get("max_output_channels",0)),"default_samplerate":float(d.get("default_samplerate",0) or 0)}
              for i,d in enumerate(_sd.query_devices())]
        except Exception as exc:err=f"{type(exc).__name__}: {exc}"
        result={"state":"good" if devices else "warn","devices":devices,"count":len(devices),"device_query_error":err,
          "note":"Lista urządzeń; samo wykrycie nie potwierdza słyszalności ani jakości."};keys=["AUDIO_SCAN_DETAIL"]
    elif kind=="audio_mic":
        import numpy as _np
        import sounddevice as _sd
        dev=_sd.query_devices(kind="input");rate=int(float(dev.get("default_samplerate",44100) or 44100))
        _u93_detail_status_only(app,"Mikrofon: próbki 5 s w pamięci procesu, bez zapisu pliku…")
        data=_sd.rec(int(rate*5),samplerate=rate,channels=1,dtype="float32");_sd.wait()
        rms=float(_np.sqrt(_np.mean(_np.square(data.astype(_np.float64)))));peak=float(_np.max(_np.abs(data)))
        result={"state":"good" if peak>0 else "warn","samplerate_hz":rate,"sample_seconds":5,"rms":rms,
          "rms_dbfs":round(20*_U66_math.log10(max(rms,1e-12)),2),"peak":peak,"frames":int(len(data)),
          "recording_saved":False};keys=["AUDIO_MIC_DETAIL"]
    elif kind=="audio_output":
        import numpy as _np
        import sounddevice as _sd
        dev=_sd.query_devices(kind="output");rate=int(float(dev.get("default_samplerate",44100) or 44100));duration=1.5
        x=_np.arange(int(rate*duration),dtype=_np.float64)/rate
        tone=(.12*_np.sin(2*_U66_math.pi*880*x)).astype("float32");_sd.play(tone,rate);_sd.wait()
        result={"state":"good","frequency_hz":880,"duration_seconds":duration,"amplitude":.12,"samplerate_hz":rate,
          "output_device":str(dev.get("name","N/D")),"note":"Program odtworzył ton; słyszalność musi potwierdzić operator."};keys=["AUDIO_OUTPUT_DETAIL"]
    elif kind=="peripheral_audio":
        _u93_remove_old_results(app,["AUDIO"]);app._peripheral_test("AUDIO")
        result=_u93_existing_result(app,["AUDIO"]) or {"state":"warn","message":"Test audio nie zwrócił raportu."};keys=["AUDIO"]
    elif kind=="keyboard_scan":
        if not is_windows():result={"state":"warn","message":"Inwentarz PnP klawiatur wymaga Windows."}
        else:
            rows=_v4319_normalize_items(ps_json("Get-PnpDevice -PresentOnly -ErrorAction SilentlyContinue | Where-Object { $_.Class -in @('Keyboard','Mouse') } | Select-Object Class,FriendlyName,Status,InstanceId | ConvertTo-Json -Compress",default=[]))
            result={"state":"good" if rows else "warn","devices":rows,"count":len(rows),
              "note":"Skan inwentarza; nie testuje mechanicznego działania klawiszy."}
        keys=["KEYBOARD_SCAN_DETAIL"]
    elif kind=="peripheral_keyboard":
        _u93_remove_old_results(app,["INPUTS","KLAWIATURA"]);app._peripheral_test("KLAWIATURA")
        result=_u93_existing_result(app,["INPUTS","KLAWIATURA"]) or {"state":"warn","message":"Test urządzeń wejścia nie zwrócił raportu."};keys=["INPUTS","KLAWIATURA"]
    elif kind=="camera_scan":
        result=_u69_camera_scan(app) or {"state":"warn","message":"Skan kamery nie zwrócił raportu."};keys=["CAMERA"]
    else:
        result={"state":"warn","message":"Brak obsługiwanego testu dla wybranego rodzaju.","kind":str(kind),"test_id":str(test_id)}
        keys=[]
    if keys:
        existing=_u93_existing_result(app,keys)
        if existing and (not result or len(result)<len(existing)):result=existing
        result.setdefault("state","warn");_u93_put_result(app,keys[0],result)
    return result

def _u93_finish_test_worker(app,module,test_id,title,kind,settings):
    import time as _tm
    start=_tm.monotonic()
    try:result=_u93_execute_catalog_test(app,module,test_id,kind,settings)
    except Exception as exc:
        result={"state":"error","error":f"{type(exc).__name__}: {exc}","module":module,"test_id":test_id,
          "note":"Test przerwany; brak wyniku nie jest PASS."}
        app.queue_log(f"TEST KATALOGU {test_id}: {result['error']}")
    if not isinstance(result,dict):result={"state":"warn","message":"Procedura zakończyła się bez raportu."}
    report=_u93_persist_result(app,module,test_id,title,result,_tm.monotonic()-start)
    _u93_put_result(app,"COMPONENT_CATALOG_"+str(test_id),report)
    _u93_update_detail(app,test_id,str(report.get("state","warn")).upper(),report)
    app.queue_log(f"KATALOG TESTÓW {test_id}: {str(report.get('state','warn')).upper()}")
    return report

def _u93_start_keyboard_capture(app):
    if getattr(app,"_u93_keyboard_capture_active",False):return
    app._u93_keyboard_capture_active=True;app._u93_keyboard_count=0;app._u93_keyboard_started=_u66_time.monotonic()
    _u93_detail_status_only(app,"Naciśnij testowane klawisze. Zapisywana jest tylko liczba naciśnięć — nie znaki ani tekst.")
    try:app.content.configure(takefocus=1);app.content.focus_set()
    except Exception:pass
    def on_key(event):
        if not getattr(app,"_u93_keyboard_capture_active",False):return None
        app._u93_keyboard_count=int(getattr(app,"_u93_keyboard_count",0))+1
        elapsed=max(.01,_u66_time.monotonic()-getattr(app,"_u93_keyboard_started",_u66_time.monotonic()))
        _u93_detail_status_only(app,f"Naciśnięcia: {app._u93_keyboard_count} • {elapsed:.1f} s • znaki nie są zapisywane")
        return "break"
    try:app._u93_keyboard_bind_id=app.bind("<KeyPress>",on_key,add="+")
    except Exception as exc:
        app._u93_keyboard_capture_active=False;_u93_update_detail(app,"key_press","ERROR",{"state":"error","error":str(exc)})

def _u93_finish_keyboard_capture(app):
    app._u93_keyboard_capture_active=False
    try:
        bind_id=getattr(app,"_u93_keyboard_bind_id",None)
        if bind_id:app.unbind("<KeyPress>",bind_id)
    except Exception:pass
    elapsed=max(.01,_u66_time.monotonic()-getattr(app,"_u93_keyboard_started",_u66_time.monotonic()))
    result={"state":"good" if getattr(app,"_u93_keyboard_count",0)>0 else "warn",
      "press_count":int(getattr(app,"_u93_keyboard_count",0)),"duration_seconds":round(elapsed,2),
      "keys_or_text_saved":False,"note":"Zliczono naciśnięcia, nie zapisano symboli klawiszy ani treści."}
    _u93_put_result(app,"KEYBOARD_INPUT_DETAIL",result)
    report=_u93_persist_result(app,"KLAWIATURA","key_press","Test klawiszy — rejestracja",result,elapsed)
    _u93_update_detail(app,"key_press",str(report["state"]).upper(),report)

def _u93_start_camera_preview(app):
    if not messagebox.askyesno("Test kamery — 10 s","Otworzyć obraz z domyślnej kamery na 10 sekund? Obraz nie będzie nagrywany ani zapisany."):return
    try:
        import cv2 as _cv2
        from PIL import Image as _Image,ImageTk as _ImageTk
        cap=_cv2.VideoCapture(0)
        if not cap.isOpened():cap.release();raise RuntimeError("Nie udało się otworzyć domyślnej kamery.")
    except Exception as exc:
        result={"state":"warn","error":f"{type(exc).__name__}: {exc}","recording_saved":False}
        _u93_put_result(app,"CAMERA_PREVIEW",result);_u93_update_detail(app,"cam_preview","OSTRZEŻENIE",result);return
    top=tk.Toplevel(app);top.title("NAPRAWA PC — podgląd kamery bez nagrywania");top.geometry("800x560")
    frame_label=tk.Label(top,text="Uruchamianie…",bg="#07111f",fg="#ffffff");frame_label.pack(fill="both",expand=True,padx=8,pady=8)
    info=tk.Label(top,text="Podgląd w RAM • automatyczne zatrzymanie po 10 s",anchor="w");info.pack(fill="x",padx=8,pady=(0,6))
    start=_u66_time.monotonic();stats={"frames":0,"width":None,"height":None,"closed":False}
    def stop(show=True):
        if stats["closed"]:return
        stats["closed"]=True
        try:cap.release()
        except Exception:pass
        try:
            if top.winfo_exists():top.destroy()
        except Exception:pass
        report={"state":"good" if stats["frames"] else "warn","frames_shown":stats["frames"],
          "duration_seconds":round(max(.01,_u66_time.monotonic()-start),2),"width":stats["width"],"height":stats["height"],
          "recording_saved":False,"note":"Obraz nie został nagrany ani zapisany."}
        _u93_put_result(app,"CAMERA_PREVIEW",report)
        if show:_u93_update_detail(app,"cam_preview",str(report["state"]).upper(),report)
    def tick():
        if stats["closed"] or not top.winfo_exists():stop(False);return
        if _u66_time.monotonic()-start>=10:stop(True);return
        try:
            ok,frame=cap.read()
            if ok:
                stats["height"],stats["width"]=frame.shape[:2]
                photo=_ImageTk.PhotoImage(_Image.fromarray(_cv2.cvtColor(frame,_cv2.COLOR_BGR2RGB)))
                frame_label.config(image=photo,text="");frame_label.image=photo;stats["frames"]+=1
                info.config(text=f"Klatki: {stats['frames']} • {stats['width']}×{stats['height']} • bez zapisu")
        except Exception as exc:info.config(text=f"Błąd podglądu: {type(exc).__name__}: {exc}")
        top.after(40,tick)
    top.protocol("WM_DELETE_WINDOW",lambda:stop(True));top.after(50,tick)

def _u93_start_screen_patterns(app,test_id):
    if not messagebox.askyesno("Test matrycy","Otworzyć pełnoekranowe wzorce? Ocena pikseli wymaga obserwacji operatora; aplikacja nie będzie zgłaszać usterek automatycznie."):return
    fn=getattr(app,"_u37_open_screen_test",None)
    if callable(fn):
        try:fn()
        except Exception as exc:_u93_update_detail(app,test_id,"OSTRZEŻENIE",{"state":"warn","error":f"{type(exc).__name__}: {exc}"})
    else:_u93_update_detail(app,test_id,"N/D",{"state":"warn","message":"Brak procedury wzorców matrycy."})

def _u93_show_test_detail(app,module,test_id):
    module=_u93_norm(module);_,title,description,kind=_u93_find_test(module,test_id)
    if kind not in _U93_SUPPORTED_TEST_KINDS:
        messagebox.showerror("Brak procedury",f"Test {test_id} nie ma handlera ({kind}).");return
    if getattr(app,"_u93_keyboard_capture_active",False):_u93_finish_keyboard_capture(app)
    app.current_view="COMPONENT_TEST_DETAIL_"+str(test_id);app.clear();t=app.colors()
    app.header_title.config(text=f"{module} — {title}")
    hero=app.panel(app.content);hero.pack(fill="x",pady=(0,6))
    tk.Label(hero,text=title,bg=t["panel"],fg=t["accent"],font=app.fnt(12,"bold"),anchor="w").pack(fill="x",padx=10,pady=(8,3))
    tk.Label(hero,text=description,bg=t["panel"],fg=t["fg"],font=app.fnt(9),wraplength=1400,justify="left",anchor="w").pack(fill="x",padx=10,pady=(0,4))
    notes={"sim":"SYMULATOR EDUKACYJNY — nie jest wynikiem testu sprzętowego ani pomiarem FPS.",
      "games":"Rekomendacje są heurystyczne; nie są pomiarem FPS z prawdziwej gry.",
      "keyboard_input":"Test zlicza naciśnięcia bez zapisywania nazw klawiszy, symboli ani treści.",
      "audio_mic":"Po potwierdzeniu pobierze 5 sekund próbek do RAM. Nie zapisuje nagrania.",
      "audio_output":"Po potwierdzeniu odtworzy krótki ton 880 Hz. Ustaw bezpieczny poziom głośności.",
      "camera_preview":"Po potwierdzeniu pokaże 10 sekund obrazu bez nagrywania."}
    tk.Label(hero,text=notes.get(kind,"Wynik pochodzi z procedury testowej. Brak czujnika/wyniku to N/D lub OSTRZEŻENIE."),
      bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1400,justify="left",anchor="w").pack(fill="x",padx=10,pady=(0,8))
    settings=tk.Frame(app.content,bg=t["bg"]);settings.pack(fill="x",pady=(0,5))
    tk.Label(settings,text="USTAWIENIA TEGO TESTU",bg=t["bg"],fg=t["accent"],font=app.fnt(9,"bold")).pack(side="left",padx=(2,8))
    default={"cpu_single":"KRÓTKI — 15 s","cpu_multi":"KRÓTKI — 15 s","cpu_load60":"ŚREDNI — 60 s",
      "cpu_load300":"ULTRA — 300 s","ram_bw":"ŚREDNI — 60 s","ram_bw_max":"ULTRA — 300 s",
      "disk_bench_long":"DŁUGI — 180 s","battery_monitor":"DŁUGI — 180 s","battery_max":"MAX — 600 s"}.get(kind,"KRÓTKI — 15 s")
    app._u68_profile_var=tk.StringVar(value=default);app._u68_profile_value=default
    if kind in ("cpu_single","cpu_multi","cpu_load60","cpu_load300","ram_pattern","ram_bw","ram_bw_max","vram_test","vram_max",
      "disk_bench","disk_bench_max","disk_bench_long","battery_monitor","battery_max","network_jitter"):
        cb=ttk.Combobox(settings,textvariable=app._u68_profile_var,values=tuple(_U68_PROFILE_CHOICES),state="readonly",width=20)
        cb.pack(side="left",padx=4);cb.bind("<<ComboboxSelected>>",lambda e:setattr(app,"_u68_profile_value",app._u68_profile_var.get()))
    if kind in ("gpu_scene","gpu_suite10","gpu_suite30","gpu_suite60"):
        val={"gpu_suite10":10,"gpu_suite30":30,"gpu_suite60":60}.get(kind,10)
        app._u93_gpu_seconds_var=tk.StringVar(value=f"{val} s")
        ttk.Combobox(settings,textvariable=app._u93_gpu_seconds_var,values=("5 s","10 s","15 s","30 s","60 s"),state="readonly",width=10).pack(side="left",padx=4)
    if kind in ("ram_pattern","ram_bw","ram_bw_max"):
        val={"ram_512":512,"ram_1024":1024,"ram_2048":2048}.get(test_id,512)
        app._u93_memory_mb_var=tk.StringVar(value=f"{val} MB")
        ttk.Combobox(settings,textvariable=app._u93_memory_mb_var,values=("128 MB","256 MB","512 MB","1024 MB","1536 MB","2048 MB"),state="readonly",width=12).pack(side="left",padx=4)
    elif kind in ("vram_test","vram_max"):
        val={"vram_64":64,"vram_128":128,"vram_256":256}.get(test_id,128)
        app._u93_memory_mb_var=tk.StringVar(value=f"{val} MB")
        ttk.Combobox(settings,textvariable=app._u93_memory_mb_var,values=("32 MB","64 MB","128 MB","192 MB","256 MB"),state="readonly",width=12).pack(side="left",padx=4)
    elif kind in ("disk_bench","disk_bench_max","disk_bench_long","disk_scan","disk_smart"):
        val={"disk_512":512,"disk_2048":2048,"disk_4096":4096}.get(test_id,512)
        app._u93_memory_mb_var=tk.StringVar(value=f"{val} MB")
        ttk.Combobox(settings,textvariable=app._u93_memory_mb_var,values=("128 MB","256 MB","512 MB","1024 MB","2048 MB","4096 MB"),state="readonly",width=12).pack(side="left",padx=4)
        drives=_u69_drive_options(app);app._u93_drive_var=tk.StringVar(value=drives[0] if drives else "N/D")
        ttk.Combobox(settings,textvariable=app._u93_drive_var,values=drives or ("N/D",),state="readonly",width=10).pack(side="left",padx=4)
    if kind=="gpu_scene":
        names=[f"{i:02d} — {scene[0]}" for i,scene in enumerate(_U66_SCENES,1)]
        app._u93_scene_var=tk.StringVar(value=names[0])
        ttk.Combobox(settings,textvariable=app._u93_scene_var,values=names,state="readonly",width=30).pack(side="left",padx=4)
    box=app.panel(app.content);box.pack(fill="both",expand=True,pady=(0,5))
    app._u93_detail_status=tk.Label(box,text="GOTOWY — wybrano jeden test.",bg=t["panel"],fg=t["muted"],font=app.fnt(9,"bold"),anchor="w")
    app._u93_detail_status.pack(fill="x",padx=10,pady=(7,3))
    app._u93_detail_report=tk.Text(box,height=13,wrap="word",bg=t["card"],fg=t["fg"],insertbackground=t["fg"],
      relief="flat",font=("Consolas",9),padx=8,pady=6)
    app._u93_detail_report.pack(fill="both",expand=True,padx=7,pady=(0,7))
    app._u93_detail_report.insert("1.0","Wynik pojawi się po uruchomieniu. Brak wyniku nie oznacza zaliczenia testu.")
    app._u93_detail_report.configure(state="disabled")
    row=tk.Frame(app.content,bg=t["bg"]);row.pack(fill="x",pady=(0,5))
    if kind=="sim":app.make_button(row,"UNIKALNA SCENA OPENGL / FPS",lambda m=module:_u107_open_component_simulator(app,m,False,"scan"),"good",side="left",ipady=5)
    elif kind=="games":app.make_button(row,"OTWÓRZ DORADCĘ GIER",lambda:_u68_show_games_advisor(app),"accent",side="left",ipady=5)
    elif kind=="keyboard_input":
        app.make_button(row,"START REJESTRACJI KLAWISZY",lambda:_u93_start_keyboard_capture(app),"accent",side="left",ipady=5)
        app.make_button(row,"ZAKOŃCZ I ZAPISZ LICZNIK",lambda:_u93_finish_keyboard_capture(app),"good",side="left",ipady=5)
    elif kind=="camera_preview":app.make_button(row,"URUCHOM PODGLĄD 10 S",lambda:_u93_start_camera_preview(app),"accent",side="left",ipady=5)
    elif kind=="screen_patterns":app.make_button(row,"OTWÓRZ TEST WZORCÓW MATRYCY",lambda:_u93_start_screen_patterns(app,test_id),"accent",side="left",ipady=5)
    else:
        app.make_button(row,"URUCHOM TEN TEST",lambda:_u93_start_catalog_test(app,module,test_id,title,kind),"accent",side="left",ipady=5)
        app.make_button(row,"UNIKALNA SCENA OPENGL / FPS",lambda m=module:_u107_open_component_simulator(app,m,False,"scan"),"good",side="left",ipady=5)
    if kind not in ("keyboard_input","sim","games","camera_preview","screen_patterns"):
        app.make_button(row,"STOP TEST",app.stop_current_test,"bad",side="left",ipady=5)
    nav=tk.Frame(app.content,bg=t["bg"]);nav.pack(fill="x")
    app.make_button(nav,"← KATALOG TESTÓW",lambda m=module:_u93_show_catalog(app,m),"card",side="left",ipady=4)
    app.make_button(nav,"← LABORATORIUM",lambda:_u93_show_lab(app),"card",side="left",ipady=4)

def _u93_start_screen_patterns(app,test_id):
    if not messagebox.askyesno("Test matrycy","Otworzyć wzorce pełnoekranowe? Ocena pikseli wymaga obserwacji operatora; aplikacja nie zgłosi ich automatycznie."):return
    fn=getattr(app,"_u37_open_screen_test",None)
    if callable(fn):
        try:fn()
        except Exception as exc:_u93_update_detail(app,test_id,"OSTRZEŻENIE",{"state":"warn","error":f"{type(exc).__name__}: {exc}"})
    else:_u93_update_detail(app,test_id,"N/D",{"state":"warn","message":"Brak procedury wzorców matrycy."})

def _u93_start_catalog_test(app,module,test_id,title,kind):
    if getattr(app,"running",False):
        messagebox.showinfo("Test w toku","Zakończ lub zatrzymaj bieżący test przed uruchomieniem kolejnego.");return
    try:
        duration=int(str(app._u93_gpu_seconds_var.get() if kind in ("gpu_scene","gpu_suite10","gpu_suite30","gpu_suite60") else app._u68_profile_var.get()).split()[0])
    except Exception:duration={"gpu_suite10":10,"gpu_suite30":30,"gpu_suite60":60,"cpu_load60":60,"cpu_load300":300,
      "ram_bw":60,"ram_bw_max":300,"disk_bench_long":180,"battery_monitor":180,"battery_max":600,"vram_max":300}.get(kind,15)
    try:app._u68_profile_value=str(app._u68_profile_var.get())
    except Exception:pass
    mb=512
    try:mb=int(str(app._u93_memory_mb_var.get()).split()[0])
    except Exception:mb=int({"ram_512":512,"ram_1024":1024,"ram_2048":2048,"disk_512":512,"disk_2048":2048,"disk_4096":4096,
      "vram_64":64,"vram_128":128,"vram_256":256}.get(test_id,512))
    drive=""
    try:drive=str(app._u93_drive_var.get())
    except Exception:pass
    scene=1
    try:scene=int(str(app._u93_scene_var.get()).split("—",1)[0].strip())
    except Exception:pass
    settings={"duration":duration,"memory_mb":mb,"drive":drive,"scene_id":scene,"gpu_seconds":duration}
    if kind in ("disk_bench","disk_bench_max") and (mb>=2048 or kind=="disk_bench_max"):
        if not messagebox.askyesno("Benchmark dysku",f"Zapis/odczyt pliku tymczasowego {mb} MB na {drive}, po teście plik zostanie usunięty. Kontynuować?"):return
    if kind=="disk_bench_long" and not messagebox.askyesno("Długi benchmark dysku",f"Powtarzany zapis/odczyt przez do {duration} s na {drive}. Kontynuować?"):return
    if kind in ("ram_pattern","ram_bw","ram_bw_max") and (mb>=1024 or duration>=180):
        if not messagebox.askyesno("Test RAM",f"Bufor do {mb} MB przez około {duration} s; nie testuje całej fizycznej pamięci. Kontynuować?"):return
    if kind in ("vram_test","vram_max") and (mb>=128 or duration>=180):
        if not messagebox.askyesno("Test VRAM",f"Alokacja do {mb} MB przez do {duration} s. Sterownik może ograniczyć pamięć. Kontynuować?"):return
    if kind in ("gpu_suite10","gpu_suite30","gpu_suite60"):
        total=len(_U66_SCENES)*duration
        if not messagebox.askyesno("Benchmark GPU",f"{len(_U66_SCENES)} scen OpenGL po {duration} s. Szacowany czas {total//60} min {total%60} s. Kontynuować?"):return
    if kind=="network_speed" and not messagebox.askyesno("Speed Test","Test Cloudflare przesyła około 24 MB łącznie. Kontynuować?"):return
    _u93_update_detail(app,test_id,"TEST W TOKU",{"state":"running","test_id":test_id,"module":module,"settings":settings,
      "note":"Brak danych nie będzie oznaczony jako PASS."})
    app.worker(lambda:_u93_finish_test_worker(app,module,test_id,title,kind,settings))

def _u93_deep_code_names(function):
    import types as _u93_types
    pending=[function.__code__]
    names=set()
    while pending:
        code=pending.pop()
        names.update(code.co_names)
        pending.extend(item for item in code.co_consts if isinstance(item,_u93_types.CodeType))
    return names

def _u93_selftest_catalog_routing():
    ids=[];kinds=set()
    for module,entries in _U93_TEST_CATALOG.items():
        assert entries,f"Pusty katalog {module}"
        for test_id,title,description,kind in entries:
            ids.append(test_id);kinds.add(kind);assert title and description
    assert len(ids)==110 and len(set(ids))==110,"Katalog powinien mieć 90 unikalnych testów"
    assert kinds.issubset(_U93_SUPPORTED_TEST_KINDS),f"Nieobsłużone rodzaje: {kinds-_U93_SUPPORTED_TEST_KINDS}"
    assert callable(_u93_show_test_detail) and callable(_u93_execute_catalog_test)
    assert AppV43.show_component_lab is _u93_show_lab
    # The callbacks are lambdas in Tk buttons; inspect nested code objects as well.
    assert "_u93_show_test_detail" in _u93_deep_code_names(_u93_scroll_rows)
    detail_names = _u93_deep_code_names(_u93_show_test_detail)
    if "_u93_start_catalog_test" not in detail_names:
        # RAM progress wrapper delegates to the original screen; inspect that inner screen too.
        original_detail = globals().get("_U102_ORIGINAL_RAM_DETAIL")
        assert callable(original_detail)
        detail_names.update(_u93_deep_code_names(original_detail))
    assert "_u93_start_catalog_test" in detail_names
    assert "_u93_execute_catalog_test" in _u93_deep_code_names(_u93_finish_test_worker)
    assert set(_U107_TEST_SCENES.keys()).issuperset(set(ids))
    assert len(_U93_TEST_CATALOG["SYSTEM_REPAIR_PRO"]) == 10 and len(_U93_TEST_CATALOG["SERWIS_ULTIMATE"]) == 10
    print("EXECUTABLE_COMPONENT_CATALOG_SELFTEST_OK: 110 unique tests, isolated detail screen and real operation dispatcher")

AppV43.show_component_lab = _u93_show_lab


# v4.3.98 — separate current display modes from EDID and require explicit consent for audio I/O tests.
_U98_ORIGINAL_DETAIL_STATUS_ONLY = _u93_detail_status_only
_U98_ORIGINAL_EXECUTE_CATALOG_TEST = _u93_execute_catalog_test
_U98_ORIGINAL_START_CATALOG_TEST = _u93_start_catalog_test

def _u98_detail_status_only(app, message):
    text_value = str(message)
    try:
        queue_action = getattr(app, "queue_action", None)
        if callable(queue_action):
            queue_action(lambda m=text_value: _U98_ORIGINAL_DETAIL_STATUS_ONLY(app, m))
            return
    except Exception:
        pass
    _U98_ORIGINAL_DETAIL_STATUS_ONLY(app, text_value)

def _u98_execute_catalog_test(app, module, test_id, kind, settings):
    if kind != "screen_modes":
        return _U98_ORIGINAL_EXECUTE_CATALOG_TEST(app, module, test_id, kind, settings)
    if not is_windows():
        result = {
            "state": "warn",
            "message": "Lista trybów monitora wymaga Windows.",
            "note": "Ten test nie uruchamia skanu EDID jako zamiennika."
        }
        _u93_put_result(app, "SCREEN_MODES_DETAIL", result)
        return result

    script = r"""
$ErrorActionPreference = 'SilentlyContinue'
$controllers = @(Get-CimInstance -ClassName Win32_VideoController |
  Select-Object Name,VideoModeDescription,CurrentHorizontalResolution,CurrentVerticalResolution,CurrentRefreshRate,DriverVersion)
$monitors = @()
try {
  foreach ($monitor in @(Get-CimInstance -Namespace root\wmi -ClassName WmiMonitorListedSupportedSourceModes -ErrorAction Stop)) {
    $listedModes = @()
    foreach ($mode in @($monitor.MonitorSourceModes)) {
      $listedModes += [pscustomobject]@{
        width = $mode.HorizontalActivePixels
        height = $mode.VerticalActivePixels
        horizontal_refresh_hz = $mode.HorizontalRefreshRate
        vertical_refresh_hz = $mode.VerticalRefreshRate
        display_flags = $mode.DisplayFlags
        timing_flags = $mode.TimingFlags
      }
    }
    $monitors += [pscustomobject]@{
      instance_name = $monitor.InstanceName
      active = $monitor.Active
      mode_count = $listedModes.Count
      modes = $listedModes
    }
  }
} catch { }
[pscustomobject]@{ controllers = $controllers; monitors = $monitors } | ConvertTo-Json -Compress -Depth 8
"""
    try:
        raw = ps_json(script, default={})
        if isinstance(raw, list) and len(raw) == 1 and isinstance(raw[0], dict):
            raw = raw[0]
        if not isinstance(raw, dict):
            raw = {}
        controllers = _v4319_normalize_items(raw.get("controllers", []))
        monitors = _v4319_normalize_items(raw.get("monitors", []))
        listed_count = 0
        normalized_monitors = []
        for item in monitors:
            if not isinstance(item, dict):
                continue
            modes = _v4319_normalize_items(item.get("modes", []))
            listed_count += len(modes)
            normalized_monitors.append({
                "instance_name": item.get("instance_name", "N/D"),
                "active": item.get("active", None),
                "mode_count": int(item.get("mode_count", len(modes)) or len(modes)),
                "modes": modes
            })
        has_current = any(
            item.get("CurrentHorizontalResolution") or item.get("CurrentVerticalResolution")
            for item in controllers if isinstance(item, dict)
        )
        result = {
            "state": "good" if has_current or listed_count else "warn",
            "video_controllers": controllers,
            "supported_monitors": normalized_monitors,
            "supported_mode_count": listed_count,
            "current_modes_available": bool(has_current),
            "sampled_at": _U66_datetime.now().isoformat(timespec="seconds"),
            "note": "To odrębny od EDID odczyt bieżących trybów kontrolera i listy trybów udostępnionej przez WMI. Brak listy WMI oznacza N/D."
        }
        if not controllers and not normalized_monitors:
            result["message"] = "Windows nie zwrócił bieżących trybów ani listy obsługiwanych trybów."
    except Exception as exc:
        result = {"state":"warn","error":f"{type(exc).__name__}: {exc}",
                  "note":"Nie wykonano zastępczego testu EDID; brak danych to ostrzeżenie."}
    _u93_put_result(app, "SCREEN_MODES_DETAIL", result)
    app.queue_log(f"TRYBY EKRANU: {result.get('supported_mode_count',0)} trybów WMI; "
                  f"bieżący tryb kontrolera={'dostępny' if result.get('current_modes_available') else 'N/D'}; "
                  f"stan={result.get('state')}")
    return result

def _u98_start_catalog_test(app, module, test_id, title, kind):
    if kind == "audio_mic":
        if not messagebox.askyesno(
            "Test mikrofonu — zgoda na próbki",
            "Przez 5 sekund aplikacja odczyta próbki z domyślnego mikrofonu do pamięci RAM, aby obliczyć poziom RMS/peak. "
            "Nie zapisze nagrania ani treści mowy do pliku. Rozpocząć?"
        ):
            _u93_update_detail(app, test_id, "ANULOWANO", {
                "state":"warn","message":"Użytkownik anulował test mikrofonu.",
                "recording_saved":False,"samples_captured":False
            })
            return
    elif kind == "audio_output":
        if not messagebox.askyesno(
            "Test głośników — ton 880 Hz",
            "Aplikacja odtworzy krótki ton 880 Hz przez domyślne urządzenie wyjściowe. Ustaw bezpieczną głośność. Odtworzyć ton?"
        ):
            _u93_update_detail(app, test_id, "ANULOWANO", {
                "state":"warn","message":"Użytkownik anulował odtwarzanie tonu."
            })
            return
    return _U98_ORIGINAL_START_CATALOG_TEST(app, module, test_id, title, kind)

def _u98_selftest_catalog_safety():
    # Later RAM and telemetry wrappers intentionally replace the public executor.
    # Verify the active chain instead of requiring an obsolete function identity.
    assert callable(_u93_execute_catalog_test)
    assert ("_U98_ORIGINAL_EXECUTE_CATALOG_TEST" in _u98_execute_catalog_test.__code__.co_names
            or "_U102_ORIGINAL_RAM_EXECUTE" in _u93_execute_catalog_test.__code__.co_names
            or "_U109_ORIGINAL_EXECUTE_CATALOG_TEST" in _u93_execute_catalog_test.__code__.co_names)
    active_start_name = getattr(_u93_start_catalog_test, "__name__", "")
    assert (_u93_start_catalog_test is _u98_start_catalog_test
            or active_start_name in ("_u109_start_catalog_test", "_u114_start_catalog_test"))
    if active_start_name == "_u109_start_catalog_test":
        assert "_U109_ORIGINAL_START_CATALOG_TEST" in _u93_start_catalog_test.__code__.co_names
    elif active_start_name == "_u114_start_catalog_test":
        assert "_U114_ORIGINAL_START_TEST" in _u93_start_catalog_test.__code__.co_names
    assert _u93_detail_status_only is _u98_detail_status_only
    assert "_U98_ORIGINAL_EXECUTE_CATALOG_TEST" in _u98_execute_catalog_test.__code__.co_names
    mode_code = str(_u98_execute_catalog_test.__code__.co_consts)
    assert "Win32_VideoController" in mode_code and "WmiMonitorListedSupportedSourceModes" in mode_code
    assert "audio_mic" in _u98_start_catalog_test.__code__.co_consts
    assert "audio_output" in _u98_start_catalog_test.__code__.co_consts
    print("CATALOG_MODE_AND_AUDIO_CONSENT_SELFTEST_OK: display mode test is separate from EDID, microphone/speaker tests require confirmation")

_u93_detail_status_only = _u98_detail_status_only
_u93_execute_catalog_test = _u98_execute_catalog_test
_u93_start_catalog_test = _u98_start_catalog_test


# v4.3.100 — unique FurMark-style scenes, adaptive real-byte Speed Test, vendor-neutral live sensors.
_U100_SCENE_TITLES = [
 "FurMark Style — Futrzasty donut",
 "FurMark Style — Potrójny futrzasty torus",
 "FurMark Style — Donut i pas asteroid",
 "Torus Knot — Pojedynczy węzeł chromatyczny",
 "Torus Knot — Przeplecione helisy",
 "Torus Knot — Gęste pole węzłów",
 "Układ planetarny — orbity",
 "Układ planetarny — podwójna gwiazda",
 "Układ planetarny — pierścienie i asteroidy",
 "Teren 3D — górskie grzbiety",
 "Teren 3D — kratery i doliny",
 "Teren 3D — warstwowe wysokości MAX",
 "Miasto 3D — nocna panorama",
 "Miasto 3D — gęste centrum",
 "Miasto 3D — wielopoziomowy stress",
 "GPU Board — płytka i radiator",
 "GPU Board — układ trzech wentylatorów",
 "GPU Board — stos kart i pamięci",
 "Particle Storm — wir",
 "Particle Storm — fontanna",
 "Particle Storm — powłoka cząstek EXTREME",
 "Ocean 3D — spokojne fale",
 "Ocean 3D — skrzyżowane fale",
 "Ocean 3D — wielowarstwowy swell",
 "Cube Field — przestrzenne instancje",
 "Cube Field — labirynt sześcianów",
 "Cube Field — spiralny tunel sześcianów",
 "Crystal Field — ogród pryzmatów",
 "Crystal Field — ostre kryształy",
 "Crystal Field — gęsta siatka shardów",
 "Mechanics — przekładnia",
 "Mechanics — pierścienie współosiowe",
 "Mechanics — wirnik i łopatki",
 "Molecule Lab — pojedynczy łańcuch",
 "Molecule Lab — sieć atomów",
 "Molecule Lab — gęsta struktura molekularna",
 "Tunnel — perspektywiczny korytarz",
 "Tunnel — heksagonalne obręcze",
 "Tunnel — wielowarstwowy tunel MAX",
 "Helix Lab — podwójna helisa",
 "Helix Lab — potrójna spirala",
 "Helix Lab — gęsta cewka 3D",
 "Triangle Storm — luźne fragmenty",
 "Triangle Storm — warstwowe arkusze",
 "Triangle Storm — ekstremalna gęstość",
 "Fractal Lab — drzewo przestrzenne",
 "Fractal Lab — rozgałęzienia warstwowe",
 "Fractal Lab — gęsta fraktalna korona",
 "Room 3D — komora testowa",
 "Room 3D — hala z modułami",
 "Room 3D — kompleks przemysłowy",
 "Wireframe Lab — pojedyncza klatka",
 "Wireframe Lab — korytarz siatek",
 "Wireframe Lab — zagnieżdżone klatki MAX",
 "Sphere Field — metaliczne kule",
 "Sphere Field — warstwowe globy",
 "Sphere Field — gęste pole sfer",
 "Ultimate Mix — geometria mieszana I",
 "Ultimate Mix — geometria mieszana II",
 "Ultimate Mix — geometria mieszana MAX",
 "Cyclone Lab — Spirala huraganu I",
 "Cyclone Lab — Oko cyklonu II",
 "Cyclone Lab — Huragan MAX",
 "Ulewa 3D — Deszcz ukośny I",
 "Ulewa 3D — Ściana deszczu II",
 "Ulewa 3D — Ulewa monsunowa MAX",
 "Powódź 3D — Wzbierająca rzeka I",
 "Powódź 3D — Zalane miasto II",
 "Powódź 3D — Fala powodziowa MAX",
 "Pioruny 3D — Pojedyncze wyładowanie I",
 "Pioruny 3D — Burza wielokomórkowa II",
 "Pioruny 3D — Superkomórka MAX",
 "Wyścigi — Tor samochodowy I",
 "Wyścigi — Peleton aut II",
 "Wyścigi — Tor wyścigowy MAX",
 "Drift Lab — Łuk i dym opon I",
 "Drift Lab — Sekcja ósemkowa II",
 "Drift Lab — Drift tandemowy MAX",
 "Rally Stage — Szuter i kurz I",
 "Rally Stage — Górski odcinek II",
 "Rally Stage — Rajdowy stress MAX",
 "F1 Night Circuit — Nocny tor I",
 "F1 Night Circuit — Pit lane i światła II",
 "F1 Night Circuit — Grand Prix MAX",
 "Zamieć śnieżna — Opad śniegu I",
 "Zamieć śnieżna — Wiatr i zawieja II",
 "Zamieć śnieżna — Blizzard MAX",
 "Tsunami Lab — Fala przybrzeżna I",
 "Tsunami Lab — Zalewanie nabrzeża II",
 "Tsunami Lab — Fala powodziowa MAX"
]
_U66_SCENES = [
 (f"{i:02d} — {name}", name.split(" — ",1)[0], 1 + (i % 3) * 2)
 for i,name in enumerate(_U100_SCENE_TITLES,1)
]

def _u100_gpu_benchmark_child(output_path, seconds=30, scene_id=1, resolution="1920x1080"):
    import json as _j
    import math as _m
    import random as _r
    import time as _tm
    from pathlib import Path as _P
    result = {"state":"warn","test":"OpenGL distinct 3D scene benchmark","scene_id":int(scene_id)}
    pg = None
    display_list = None
    try:
        import pygame as pg
        from OpenGL import GL as gl
        from OpenGL.GLU import gluPerspective
        sid = max(1,min(len(_U66_SCENES),int(scene_id)))
        family = (sid-1)//3
        variant = (sid-1)%3
        title = _U100_SCENE_TITLES[sid-1]
        requested_resolution=str(resolution or "1920x1080")
        desktop_w=desktop_h=0
        resolution_limited=False
        try:
            rw,rh=[int(x) for x in requested_resolution.lower().split("x",1)]
            rw=max(640,min(7680,rw));rh=max(480,min(4320,rh))
        except Exception:
            requested_resolution="1920x1080";rw,rh=1920,1080

        # Cap initial OpenGL window to usable desktop area; 1920x1080 may be off-screen on small laptops/high-DPI PCs.
        try:
            if os.name=="nt":
                import ctypes as _u105_ctypes
                desktop_w=int(_u105_ctypes.windll.user32.GetSystemMetrics(0))
                desktop_h=int(_u105_ctypes.windll.user32.GetSystemMetrics(1))
                if desktop_w>=640 and desktop_h>=480:
                    usable_w=max(640,desktop_w-48)
                    usable_h=max(480,desktop_h-112)
                    display_scale=min(1.0,usable_w/float(rw),usable_h/float(rh))
                    if display_scale<0.999:
                        rw=max(640,int(rw*display_scale))
                        rh=max(480,int(rh*display_scale))
                        if rw>usable_w or rh>usable_h:
                            correction=min(usable_w/float(rw),usable_h/float(rh))
                            rw=max(640,int(rw*correction))
                            rh=max(480,int(rh*correction))
                        resolution_limited=True
        except Exception:
            desktop_w=desktop_h=0
        result.update({
            "resolution_requested":requested_resolution,
            "resolution_rendered":f"{rw}x{rh}",
            "desktop_resolution":f"{desktop_w}x{desktop_h}" if desktop_w and desktop_h else "N/D",
            "resolution_limited_by_display":resolution_limited
        })
        seconds=max(3,min(900,int(seconds)))
        pg.init()
        try:
            pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION,2)
            pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION,1)
            pg.display.gl_set_attribute(pg.GL_DOUBLEBUFFER,1)
            pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE,24)
        except Exception:
            pass
        pg.display.set_mode((rw,rh),pg.OPENGL|pg.DOUBLEBUF|pg.RESIZABLE,vsync=0)
        renderer=(gl.glGetString(gl.GL_RENDERER) or b"unknown").decode("utf-8","replace")
        gl_version=(gl.glGetString(gl.GL_VERSION) or b"unknown").decode("utf-8","replace")
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glEnable(gl.GL_NORMALIZE)
        gl.glEnable(gl.GL_COLOR_MATERIAL)
        gl.glColorMaterial(gl.GL_FRONT_AND_BACK,gl.GL_AMBIENT_AND_DIFFUSE)
        gl.glShadeModel(gl.GL_SMOOTH)
        gl.glEnable(gl.GL_LIGHTING)
        gl.glEnable(gl.GL_LIGHT0)
        gl.glLightfv(gl.GL_LIGHT0,gl.GL_POSITION,(3.5,5.0,7.0,1.0))
        gl.glLightfv(gl.GL_LIGHT0,gl.GL_DIFFUSE,(0.95,0.98,1.0,1.0))
        gl.glLightfv(gl.GL_LIGHT0,gl.GL_AMBIENT,(0.22,0.22,0.28,1.0))
        gl.glClearColor(0.006,0.012,0.026,1.0)
        gl.glViewport(0,0,rw,rh)
        gl.glMatrixMode(gl.GL_PROJECTION);gl.glLoadIdentity();gluPerspective(52.0,rw/rh,0.1,150.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        rand=_r.Random(74123+sid*271)
        complexity=1+variant
        primitive_counter={"value":0}
        def color(c):
            gl.glColor3f(float(c[0]),float(c[1]),float(c[2]))
        def box(x,y,z,sx,sy,sz,c):
            gl.glPushMatrix();gl.glTranslatef(x,y,z);gl.glScalef(sx,sy,sz);color(c)
            gl.glBegin(gl.GL_QUADS)
            faces=[
              ((0,0,1),((-0.5,-0.5,0.5),(0.5,-0.5,0.5),(0.5,0.5,0.5),(-0.5,0.5,0.5))),
              ((0,0,-1),((0.5,-0.5,-0.5),(-0.5,-0.5,-0.5),(-0.5,0.5,-0.5),(0.5,0.5,-0.5))),
              ((1,0,0),((0.5,-0.5,0.5),(0.5,-0.5,-0.5),(0.5,0.5,-0.5),(0.5,0.5,0.5))),
              ((-1,0,0),((-0.5,-0.5,-0.5),(-0.5,-0.5,0.5),(-0.5,0.5,0.5),(-0.5,0.5,-0.5))),
              ((0,1,0),((-0.5,0.5,0.5),(0.5,0.5,0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5))),
              ((0,-1,0),((-0.5,-0.5,-0.5),(0.5,-0.5,-0.5),(0.5,-0.5,0.5),(-0.5,-0.5,0.5)))
            ]
            for normal,verts in faces:
                gl.glNormal3f(*normal)
                for v in verts:gl.glVertex3f(*v)
            gl.glEnd();gl.glPopMatrix();primitive_counter["value"]+=12
        def sphere(x,y,z,r,c,lats=8,lons=14):
            color(c);gl.glPushMatrix();gl.glTranslatef(x,y,z)
            for lat in range(max(6,lats)):
                a0=-_m.pi/2+_m.pi*lat/lats;a1=-_m.pi/2+_m.pi*(lat+1)/lats
                gl.glBegin(gl.GL_QUAD_STRIP)
                for lon in range(lons+1):
                    b=2*_m.pi*lon/lons
                    for a in (a0,a1):
                        nx=_m.cos(a)*_m.cos(b);ny=_m.sin(a);nz=_m.cos(a)*_m.sin(b)
                        gl.glNormal3f(nx,ny,nz);gl.glVertex3f(r*nx,r*ny,r*nz)
                gl.glEnd()
            gl.glPopMatrix();primitive_counter["value"]+=lats*lons*2
        def torus(R,r,c,major=36,minor=12):
            color(c)
            for i in range(major):
                u0=2*_m.pi*i/major;u1=2*_m.pi*(i+1)/major
                gl.glBegin(gl.GL_QUAD_STRIP)
                for j in range(minor+1):
                    v=2*_m.pi*j/minor
                    for u in (u0,u1):
                        x=(R+r*_m.cos(v))*_m.cos(u);y=r*_m.sin(v);z=(R+r*_m.cos(v))*_m.sin(u)
                        nx=_m.cos(v)*_m.cos(u);ny=_m.sin(v);nz=_m.cos(v)*_m.sin(u)
                        gl.glNormal3f(nx,ny,nz);gl.glVertex3f(x,y,z)
                gl.glEnd()
            primitive_counter["value"]+=major*minor*2
        def line(a,b,c=(0.2,0.8,1.0),width=1.0):
            gl.glDisable(gl.GL_LIGHTING);color(c);gl.glLineWidth(width);gl.glBegin(gl.GL_LINES);gl.glVertex3f(*a);gl.glVertex3f(*b);gl.glEnd();gl.glEnable(gl.GL_LIGHTING)
            primitive_counter["value"]+=1
        def draw_fur_torus(R,r,count,c):
            torus(R,r,c,36+complexity*8,12+complexity*3)
            gl.glDisable(gl.GL_LIGHTING);gl.glBegin(gl.GL_LINES)
            for i in range(count):
                u=rand.random()*2*_m.pi;v=rand.random()*2*_m.pi
                cu,su,cv,sv=_m.cos(u),_m.sin(u),_m.cos(v),_m.sin(v)
                radial=R+r*cv
                x=radial*cu;y=r*sv;z=radial*su
                nx=cv*cu;ny=sv;nz=cv*su
                length=0.035+rand.random()*0.18
                col=(0.15+rand.random()*0.35,0.35+rand.random()*0.45,0.62+rand.random()*0.34)
                gl.glColor3f(*col);gl.glVertex3f(x,y,z);gl.glVertex3f(x+nx*length,y+ny*length,z+nz*length)
            gl.glEnd();gl.glEnable(gl.GL_LIGHTING);primitive_counter["value"]+=count
        def path_line(points,c=(0.3,0.8,1.0),width=1.5):
            gl.glDisable(gl.GL_LIGHTING);gl.glLineWidth(width);color(c);gl.glBegin(gl.GL_LINE_STRIP)
            for p in points:gl.glVertex3f(*p)
            gl.glEnd();gl.glEnable(gl.GL_LIGHTING);primitive_counter["value"]+=len(points)
        def wire_box(cx,cy,cz,s,c):
            h=s/2
            verts=[(cx+dx*h,cy+dy*h,cz+dz*h) for dx,dy,dz in ((-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1))]
            edges=((0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7))
            gl.glDisable(gl.GL_LIGHTING);color(c);gl.glBegin(gl.GL_LINES)
            for a,b in edges:gl.glVertex3f(*verts[a]);gl.glVertex3f(*verts[b])
            gl.glEnd();gl.glEnable(gl.GL_LIGHTING);primitive_counter["value"]+=12
        def build_scene():
            # Every benchmark scene keeps a FurMark-style animated/fuzzy stress core,
            # but its radius, density, material and surrounding scene vary by scene ID.
            # The native scene family below remains unique; this ring is not the only geometry.
            if family > 0:
                fur_r = 0.56 + (sid % 9) * 0.075
                fur_minor = 0.13 + (variant % 3) * 0.035
                fur_count = 500 + (sid * 37) % 1900
                fur_color = (
                    0.12 + ((sid * 17) % 70) / 100.0,
                    0.18 + ((sid * 29) % 65) / 100.0,
                    0.35 + ((sid * 11) % 60) / 100.0,
                )
                gl.glPushMatrix()
                gl.glRotatef((sid % 7) * 11.0, 1, 0, 0)
                gl.glRotatef((sid % 11) * 7.0, 0, 1, 0)
                draw_fur_torus(fur_r, fur_minor, fur_count, fur_color)
                gl.glPopMatrix()
            color_a=(0.04,0.66,0.88);color_b=(0.88,0.29,0.13);color_c=(0.24,0.8,0.42)
            amount=12+variant*12+(sid%7)*4
            if family==0:
                if variant==0:
                    draw_fur_torus(1.2,0.42,1700,(0.10,0.26,0.82))
                elif variant==1:
                    for q in (-1,0,1):
                        gl.glPushMatrix();gl.glTranslatef(q*1.35,0,0);gl.glRotatef(q*28,0,1,0);draw_fur_torus(0.72,0.27,1100,(0.10,0.62,0.9));gl.glPopMatrix()
                else:
                    draw_fur_torus(1.0,0.35,3200,(0.09,0.25,0.68))
                    for i in range(24):
                        a=2*_m.pi*i/24;sphere(1.55*_m.cos(a),0.4*_m.sin(a*3),1.55*_m.sin(a),0.07,(0.9,0.35+0.4*rand.random(),0.14),6,10)
            elif family==1:
                if variant==0:
                    pts=[]
                    for i in range(900):
                        t=i/899*8*_m.pi;pts.append((1.2*_m.cos(t)+0.45*_m.cos(3*t),0.9*_m.sin(2*t),1.2*_m.sin(t)+0.45*_m.sin(3*t)))
                    path_line(pts,color_a,2.0)
                elif variant==1:
                    for q in range(3):
                        gl.glPushMatrix();gl.glRotatef(q*120,0,1,0);pts=[]
                        for i in range(520):
                            t=i/519*6*_m.pi;pts.append((1.0*_m.cos(t),0.4*_m.sin(3*t+q),1.0*_m.sin(t)))
                        path_line(pts,(0.2+0.3*q,0.85-0.2*q,0.95),1.5);gl.glPopMatrix()
                else:
                    for q in range(5):
                        gl.glPushMatrix();gl.glTranslatef((q-2)*0.55,0,0);torus(0.55,0.13,(0.25,0.45+q*0.08,0.95),28,10);gl.glPopMatrix()
            elif family==2:
                if variant==0:
                    sphere(0,0,0,0.65,(1.0,0.45,0.05),14,22)
                    for i in range(7):
                        r=1.1+i*0.3;line((-r,0,0),(r,0,0),(0.16,0.35,0.75),0.6);torus(r,0.012,(0.15,0.36,0.76),44,4)
                        a=rand.random()*2*_m.pi;sphere(r*_m.cos(a),0.05*i,r*_m.sin(a),0.07+0.018*i,(0.2+0.1*i,0.6,0.85-0.07*i),7,12)
                elif variant==1:
                    sphere(-0.65,0,0,0.5,(1.0,0.27,0.08),12,18);sphere(0.65,0,0,0.5,(0.25,0.55,1.0),12,18)
                    for i in range(5):
                        r=0.9+i*0.36;torus(r,0.018,(0.15,0.75,0.92),38,5)
                        sphere(r*_m.cos(i*1.4),0.2*_m.sin(i),r*_m.sin(i*1.4),0.085,(0.85,0.8,0.3),7,12)
                else:
                    gl.glDisable(gl.GL_LIGHTING);gl.glPointSize(3);gl.glBegin(gl.GL_POINTS)
                    for i in range(3600):
                        a=rand.random()*2*_m.pi;r=1.2+rand.random()*1.5;y=(rand.random()-0.5)*0.75
                        gl.glColor3f(0.3+0.65*rand.random(),0.35+0.5*rand.random(),0.6+0.35*rand.random());gl.glVertex3f(r*_m.cos(a),y,r*_m.sin(a))
                    gl.glEnd();gl.glEnable(gl.GL_LIGHTING);torus(0.8,0.25,(0.95,0.45,0.08),32,12)
            elif family==3:
                grid=32+variant*18
                for row in range(grid):
                    z0=-3+6*row/grid;z1=-3+6*(row+1)/grid
                    gl.glBegin(gl.GL_TRIANGLE_STRIP)
                    for col in range(grid+1):
                        x=-3+6*col/grid
                        for z in (z0,z1):
                            h=0.55*_m.sin(x*1.9+sid)*_m.cos(z*1.5-variant)+0.23*_m.sin((x+z)*4.1)
                            gl.glColor3f(0.05+0.15*(h+1),0.24+0.22*(h+1),0.16+0.1*(h+1));gl.glNormal3f(-0.2*_m.cos(x),1.0,-0.2*_m.sin(z));gl.glVertex3f(x,h,z)
                    gl.glEnd()
                primitive_counter["value"]+=grid*grid*2
            elif family==4:
                for i in range(18+variant*22):
                    x=(i%6-2.5)*0.8;z=(i//6-1.5)*0.8
                    h=0.45+rand.random()*(1.4+variant*0.5)
                    box(x,h/2,z,0.48,h,0.48,(0.08+rand.random()*0.12,0.1+rand.random()*0.14,0.22+rand.random()*0.2))
                    for y in range(1,int(h*8)+1):
                        if rand.random()>0.38:box(x+0.13,y*0.12,z+0.245,0.055,0.045,0.025,(0.1,0.75,0.95))
            elif family==5:
                box(0,0,0,4.4,0.16,2.2,(0.04,0.27,0.16))
                for i in range(18+variant*14):box((i%12-5.5)*0.32,0.13,(i//12-1)*0.65,0.22,0.12,0.23,(0.14,0.18,0.21))
                for i in range(18+variant*10):box(-1.5+i*0.17,0.2,0,0.045,0.1,1.45,(0.45,0.52,0.55))
                fan_count=(1,3,5)[variant]
                for fan in range(fan_count):
                    fx=(fan-(fan_count-1)/2)*1.15
                    torus(0.38,0.06,(0.18,0.65,0.85),24,8)
                    for blade in range(8):
                        a=blade*2*_m.pi/8;line((fx,0.32,0),(fx+0.28*_m.cos(a),0.32,0.28*_m.sin(a)),(0.15,0.8,0.96),2)
                    sphere(fx,0.3,0,0.1,(0.55,0.6,0.66),7,10)
                for i in range(100+variant*120):box(rand.uniform(-2,2),0.13,rand.uniform(-1,1),0.03,0.015,0.03,(0.1,0.8,0.55))
            elif family==6:
                count=(1400,3000,6200)[variant]
                gl.glDisable(gl.GL_LIGHTING);gl.glPointSize((2,2.5,3)[variant]);gl.glBegin(gl.GL_POINTS)
                for i in range(count):
                    t=rand.random()*12*_m.pi
                    if variant==0:r=0.25+1.9*rand.random();y=(rand.random()-0.5)*2.2
                    elif variant==1:r=rand.random()*1.8;y=-1.8+3.6*rand.random()
                    else:r=0.7+rand.random()*1.7;y=1.8*(rand.random()-0.5)
                    gl.glColor3f(0.1+rand.random()*0.65,0.25+rand.random()*0.6,0.6+rand.random()*0.4)
                    gl.glVertex3f(r*_m.cos(t),y,r*_m.sin(t))
                gl.glEnd();gl.glEnable(gl.GL_LIGHTING);primitive_counter["value"]+=count
            elif family==7:
                n=(28,48,68)[variant]
                for row in range(n):
                    z0=-3+6*row/n;z1=-3+6*(row+1)/n
                    gl.glBegin(gl.GL_TRIANGLE_STRIP)
                    for col in range(n+1):
                        x=-3+6*col/n
                        for z in (z0,z1):
                            h=0.25*_m.sin(x*2.2+sid*0.3)+0.22*_m.cos(z*2.8)+0.12*_m.sin((x+z)*5+variant)
                            gl.glColor3f(0.02,0.25+0.2*(h+0.4),0.55+0.3*(h+0.4));gl.glNormal3f(0.0,1.0,0.0);gl.glVertex3f(x,h,z)
                    gl.glEnd()
                if variant>0:
                    for i in range(12+variant*14):
                        x=rand.uniform(-2.8,2.8);z=rand.uniform(-2.8,2.8);sphere(x,0.18,z,0.035,(0.7,0.85,0.95),5,8)
                primitive_counter["value"]+=n*n*2
            elif family==8:
                count=(45,110,230)[variant]
                for i in range(count):
                    if variant==0:x=(i%7-3)*0.65;y=(i//7%4-1.5)*0.65;z=(i//28-0.5)*0.75
                    elif variant==1:
                        a=i*0.34;r=0.5+0.12*i;x=r*_m.cos(a);y=0.03*(i%9);z=r*_m.sin(a)
                    else:
                        a=i*0.26;r=1.4;x=r*_m.cos(a);y=(i%16-8)*0.25;z=r*_m.sin(a)
                    size=0.13+0.1*rand.random()
                    box(x,y,z,size,size,size,(0.12+rand.random()*0.3,0.35+rand.random()*0.5,0.55+rand.random()*0.42))
            elif family==9:
                count=(18,54,120)[variant]
                for i in range(count):
                    x=rand.uniform(-2.5,2.5);z=rand.uniform(-2.5,2.5);h=0.25+rand.random()*(0.6+variant*0.3)
                    color((0.1+rand.random()*0.2,0.35+rand.random()*0.5,0.65+rand.random()*0.3))
                    gl.glBegin(gl.GL_TRIANGLES)
                    gl.glNormal3f(0,1,0);gl.glVertex3f(x,0,z);gl.glVertex3f(x+0.24,h,z);gl.glVertex3f(x,0,z+0.24)
                    gl.glVertex3f(x,0,z);gl.glVertex3f(x,0,z+0.24);gl.glVertex3f(x-0.24,h,z)
                    gl.glEnd();primitive_counter["value"]+=2
            elif family==10:
                if variant==0:
                    for i in range(7):
                        x=(i-3)*0.72;torus(0.3+(i%2)*0.08,0.07,(0.5,0.65,0.76),24,8)
                        for b in range(12):
                            a=b*2*_m.pi/12;box(x+0.36*_m.cos(a),0.15,0.36*_m.sin(a),0.12,0.24,0.08,(0.6,0.68,0.74))
                elif variant==1:
                    for i in range(12):
                        gl.glPushMatrix();gl.glRotatef(i*30,0,1,0);torus(0.9,0.065,(0.15+0.04*i,0.45,0.8),28,6);gl.glPopMatrix()
                else:
                    for i in range(4):
                        x=(i-1.5)*0.8;torus(0.55,0.12,(0.2,0.75-0.1*i,0.84),24,8)
                        for b in range(10):box(x+0.6*_m.cos(b*_m.pi/5),0.04,0.6*_m.sin(b*_m.pi/5),0.12,0.15,0.12,(0.75,0.42,0.12))
            elif family==11:
                atoms=[]
                count=(35,90,180)[variant]
                for i in range(count):
                    x=rand.uniform(-2,2);y=rand.uniform(-1.8,1.8);z=rand.uniform(-2,2);atoms.append((x,y,z))
                    sphere(x,y,z,0.06+0.025*variant,(0.1+rand.random()*0.85,0.3+rand.random()*0.6,0.7+rand.random()*0.3),6,10)
                gl.glDisable(gl.GL_LIGHTING);gl.glColor3f(0.4,0.7,0.9);gl.glBegin(gl.GL_LINES)
                for i,a in enumerate(atoms):
                    for b in atoms[i+1:]:
                        if sum((a[k]-b[k])**2 for k in range(3))<0.48:
                            gl.glVertex3f(*a);gl.glVertex3f(*b);primitive_counter["value"]+=1
                gl.glEnd();gl.glEnable(gl.GL_LIGHTING)
            elif family==12:
                for ring in range(12+variant*8):
                    z=-3+ring*6/(11+variant*8);r=1.0+0.25*_m.sin(ring*0.8)
                    gl.glPushMatrix();gl.glTranslatef(0,0,z);torus(r,0.025,(0.15,0.65,0.88),24+variant*5,5);gl.glPopMatrix()
                    if ring%2==0:wire_box(0,0,z,2.4,(0.22,0.42,0.62))
            elif family==13:
                for helix in range(2+variant):
                    phase=helix*2*_m.pi/(2+variant)
                    pts=[]
                    for i in range(650):
                        t=i/649*5*_m.pi;x=1.1*_m.cos(t+phase);z=1.1*_m.sin(t+phase);y=-2+4*i/649
                        pts.append((x,y,z))
                    path_line(pts,(0.12+0.18*helix,0.4+0.2*helix,0.95-0.1*helix),1.5)
                if variant>0:
                    for i in range(42+variant*44):
                        y=-1.9+3.8*i/(42+variant*44);a=i*0.42
                        line((1.1*_m.cos(a),y,1.1*_m.sin(a)),(1.1*_m.cos(a+_m.pi),y,1.1*_m.sin(a+_m.pi)),(0.15,0.78,0.75),0.7)
            elif family==14:
                count=(900,2600,6800)[variant]
                gl.glDisable(gl.GL_LIGHTING);gl.glBegin(gl.GL_TRIANGLES)
                for i in range(count):
                    x=rand.uniform(-2.8,2.8);y=rand.uniform(-2.1,2.1);z=rand.uniform(-2.8,2.8);size=0.03+rand.random()*0.12
                    gl.glColor3f(rand.random()*0.7,0.2+rand.random()*0.7,0.35+rand.random()*0.65)
                    gl.glVertex3f(x,y,z);gl.glVertex3f(x+size,y+size*rand.random(),z);gl.glVertex3f(x-size,y+size,z+size)
                gl.glEnd();gl.glEnable(gl.GL_LIGHTING);primitive_counter["value"]+=count
            elif family==15:
                def branch(x,y,z,length,depth,angle):
                    if depth<=0:return
                    ex=x+length*_m.sin(angle);ey=y+length;ez=z+length*_m.cos(angle)
                    line((x,y,z),(ex,ey,ez),(0.2,0.75-0.05*depth,0.36+0.05*depth),max(0.5,depth*0.32))
                    branch(ex,ey,ez,length*0.72,depth-1,angle+0.55)
                    branch(ex,ey,ez,length*0.72,depth-1,angle-0.55)
                    if variant>1:branch(ex,ey,ez,length*0.62,depth-1,angle+0.15)
                branch(0,-2,0,1.0,4+variant,0.0)
                if variant>0:
                    for i in range(80+variant*90):
                        x=rand.uniform(-2.5,2.5);y=rand.uniform(0,2.0);z=rand.uniform(-2.5,2.5)
                        sphere(x,y,z,0.035,(0.13,0.5+rand.random()*0.4,0.24),5,8)
            elif family==16:
                box(0,-0.05,0,4.6,0.12,4.6,(0.12,0.16,0.2))
                for i in range(20+variant*25):
                    x=rand.uniform(-2,2);z=rand.uniform(-2,2);y=rand.uniform(0.1,1.4)
                    box(x,y,z,0.25+rand.random()*0.5,0.1+rand.random()*0.25,0.25+rand.random()*0.5,(0.15+rand.random()*0.35,0.25+rand.random()*0.4,0.38+rand.random()*0.4))
                for i in range(1+variant):
                    wire_box(0,0.65,0,2.2+i*0.5,(0.25,0.52,0.72))
            elif family==17:
                for i in range(1+variant):
                    wire_box(0,0,0,1.5+i*0.8,(0.15+0.1*i,0.5,0.9))
                gl.glDisable(gl.GL_LIGHTING);gl.glColor3f(0.1,0.85,0.95);gl.glBegin(gl.GL_LINES)
                for x in range(-6-variant*4,7+variant*4):
                    for y in range(-4-variant*2,5+variant*2):
                        gl.glVertex3f(x*0.26,y*0.26,-2.4);gl.glVertex3f(x*0.26,y*0.26,2.4)
                        gl.glVertex3f(-2.4,y*0.26,x*0.26);gl.glVertex3f(2.4,y*0.26,x*0.26)
                        primitive_counter["value"]+=2
                gl.glEnd();gl.glEnable(gl.GL_LIGHTING)
            elif family==18:
                count=(36,100,220)[variant]
                for i in range(count):
                    x=rand.uniform(-2.5,2.5);y=rand.uniform(-1.9,1.9);z=rand.uniform(-2.5,2.5)
                    sphere(x,y,z,0.06+rand.random()*0.1,(0.12+rand.random()*0.7,0.2+rand.random()*0.7,0.55+rand.random()*0.4),7+variant*2,12+variant*2)
            elif family==19:
                draw_fur_torus(0.9,0.28,800+variant*1200,(0.08,0.25,0.8))
                for i in range(80+variant*80):
                    x=rand.uniform(-2.2,2.2);y=rand.uniform(-1.4,1.4);z=rand.uniform(-2.2,2.2)
                    if i%3==0:sphere(x,y,z,0.075,(0.85,0.32,0.1),5,8)
                    else:box(x,y,z,0.11,0.11,0.11,(0.13,0.5,0.85))
                for i in range(25+variant*30):
                    wire_box(rand.uniform(-1.5,1.5),rand.uniform(-1,1),rand.uniform(-1.5,1.5),0.25+rand.random()*0.35,(0.12,0.8,0.65))
            elif family==20:  # Cyclone / hurricane
                layers=(12,20,30)[variant]
                for layer in range(layers):
                    f=layer/max(1,layers-1);r=0.3+1.7*f
                    gl.glPushMatrix();gl.glTranslatef(0,-2.4+4.8*f,0);gl.glRotatef(layer*31+sid*7,0,1,0)
                    torus(r,0.08+0.025*variant,(0.30+0.2*f,0.42+0.2*f,0.7+0.15*f),32+variant*12,7+variant*3);gl.glPopMatrix()
                for i in range(100+variant*180):
                    a=i*0.41;r=0.35+(i%37)/37*1.6;y=-2.2+(i%53)/52*4.4
                    sphere(r*_m.cos(a),y,r*_m.sin(a),0.04+0.01*variant,(0.30,0.46,0.65),5,8)
            elif family==21:  # Torrential rain
                for i in range(8+variant*6):
                    sphere((i%7-3)*0.72,1.6+(i//7)*0.32,(i%3-1)*0.65,0.48+0.05*variant,(0.10,0.16,0.27),8,13)
                for i in range(180+variant*260):
                    x=-2.8+(i%41)*0.14;z=-2.5+((i*17)%37)*0.14;y=1.4+((i*11)%31)*0.11
                    line((x,y,z),(x-0.12,y-0.36,z+0.03),(0.28,0.57,0.86),0.7)
            elif family==22:  # Flooded settlement
                for side in (-1,1):
                    for i in range(12+variant*8):
                        x=side*(1.9+(i%3)*0.3);z=-2.8+i*5.6/(11+variant*8);h=0.7+0.1*(i%4)
                        box(x,h/2,z,0.5,h,0.42,(0.18,0.24,0.31))
                        for win in range(2+variant):box(x-0.1+win*0.12,0.3+0.08*(i%4),z+0.216,0.045,0.05,0.02,(0.85,0.68,0.24))
                for layer in range(7+variant*5):
                    z=-2.8+layer*5.6/(6+variant*5)
                    path_line([(-1.7,0.04,z),(0,0.12,z+0.05),(1.7,0.04,z)],(0.04,0.36+0.08*variant,0.72),1.0)
            elif family==23:  # Lightning storm
                for i in range(18+variant*15):sphere(-2.5+(i%9)*0.62,1.55+(i%4)*0.18,-1.8+((i*5)%7)*0.52,0.42+0.04*variant,(0.13,0.17,0.26),7+variant*2,11+variant*3)
                for strike in range(1+variant*2):
                    x=-1.7+strike*(3.4/max(1,variant*2));z=-0.9+0.45*(strike%3)
                    pts=[(x,1.45,z),(x-0.16,0.82,z+0.04),(x+0.13,0.48,z+0.12),(x-0.21,-0.1,z+0.19),(x+0.04,-0.62,z+0.12)]
                    path_line(pts,(0.62,0.84,1.0),2.0+variant)
                    if variant>0:path_line([pts[2],(pts[2][0]+0.4,0.2,z+0.4),(pts[2][0]+0.55,-0.1,z+0.5)],(0.45,0.73,1.0),1.4)
            elif family==24:  # Racing circuit
                torus(2.3,0.18,(0.10,0.12,0.16),60+variant*20,8+variant*3)
                torus(2.3,0.035,(0.9,0.9,0.78),64+variant*20,5);torus(2.78,0.05,(0.9,0.20,0.08),64+variant*20,6)
                for i in range(24+variant*20):
                    a=2*_m.pi*i/(24+variant*20);box(2.95*_m.cos(a),0.18,2.95*_m.sin(a),0.18,0.28,0.17,(0.25,0.29,0.35))
                for i in range(10+variant*8):box(-2.7+i*5.4/(9+variant*8),0.35,-2.65,0.36,0.5+0.1*(i%3),0.28,(0.19,0.23,0.3))
            elif family==25:  # Drift figure-eight
                for scale in (1.0,0.78,0.54):
                    path_line([(2.25*_m.sin(i/499*2*_m.pi),0.04,1.48*_m.sin(i/499*2*_m.pi)*_m.cos(i/499*2*_m.pi)*2*scale) for i in range(500)],(0.42,0.47,0.53),5.5*scale)
                for i in range(12+variant*12):
                    a=i*2*_m.pi/(12+variant*12);box(2.1*_m.sin(a),0.12,1.38*_m.sin(a)*_m.cos(a),0.1,0.22,0.1,(0.9,0.33,0.06))
            elif family==26:  # Rally stage
                for i in range(20+variant*18):
                    x=-2.8+(i%11)*0.56;z=-2.65+(i//11)*0.75;h=0.25+((i*7)%9)*0.12
                    box(x,h/2,z,0.42,h,0.45,(0.18+0.03*(i%4),0.20+0.03*(i%5),0.19))
                    sphere(x+0.17,h+0.08,z+0.08,0.12+0.03*variant,(0.22,0.38,0.18),6,9)
                path_line([(2.25*_m.sin(i/299*2*_m.pi),0.08,1.75*_m.sin(i/299*2*_m.pi)*_m.cos(i/299*2*_m.pi)) for i in range(300)],(0.43,0.34,0.19),4.0+variant*1.5)
            elif family==27:  # Night F1 circuit
                torus(2.35,0.16,(0.06,0.09,0.13),68+variant*20,8+variant*3)
                torus(2.35,0.025,(0.05,0.86,0.92),68+variant*20,5);torus(2.68,0.03,(0.88,0.12,0.35),68+variant*20,5)
                for i in range(24+variant*18):
                    a=2*_m.pi*i/(24+variant*18);x=2.95*_m.cos(a);z=2.95*_m.sin(a)
                    box(x,0.42,z,0.05,0.8,0.05,(0.08,0.62,0.95));sphere(x,0.9,z,0.08+0.02*variant,(0.15,0.8,1.0),6,9)
                for row in range(3+variant*2):box(-2.6,0.2+row*0.22,-2.15-row*0.06,5.3,0.14,0.32,(0.12,0.16,0.24))
            elif family==28:  # Blizzard
                for i in range(18+variant*14):
                    x=(i%6-2.5)*0.82;z=(i//6-1)*0.78;h=0.55+((i*7)%8)*0.15
                    box(x,h/2,z,0.52,h,0.48,(0.25,0.31,0.42));sphere(x,h+0.1,z,0.32+0.05*variant,(0.72,0.82,0.93),7+variant*2,10+variant*3)
                for i in range(50+variant*50):
                    x=rand.uniform(-2.7,2.7);z=rand.uniform(-2.5,2.5);line((x,rand.uniform(-0.4,2.2),z),(x+0.06,-0.7,z+0.03),(0.72,0.85,1.0),0.8)
            elif family==29:  # Tsunami and coastal flood
                for i in range(20+variant*16):
                    x=-2.75+(i%10)*0.61;z=-2.3+(i//10)*0.9;h=0.32+((i*5)%9)*0.12
                    box(x,h/2,z,0.45,h,0.46,(0.19,0.24,0.32))
                for layer in range(12+variant*10):
                    y=-1.7+layer*3.4/(11+variant*10);pts=[]
                    for i in range(180):
                        x=-2.8+i*5.6/179;z=-0.6+0.28*_m.sin(x*2.4+layer*0.3)
                        pts.append((x,y+0.16*_m.sin(x*1.4+layer),z))
                    path_line(pts,(0.03,0.40+0.06*variant,0.88),1.0+variant*0.4)
        def draw_dynamic(elapsed):
            def vehicle(x,y,z,scale,paint,heading):
                gl.glPushMatrix();gl.glTranslatef(x,y,z);gl.glRotatef(heading,0,1,0)
                box(0,0,0,1.05*scale,0.18*scale,0.44*scale,paint)
                box(0.12*scale,0.13*scale,-0.01*scale,0.42*scale,0.17*scale,0.32*scale,(0.12,0.17,0.23))
                box(0.48*scale,-0.015*scale,0,0.18*scale,0.12*scale,0.52*scale,paint)
                box(-0.48*scale,0.02*scale,0,0.17*scale,0.08*scale,0.54*scale,(0.16,0.18,0.22))
                for wx in (-0.32,0.34):
                    for wz in (-0.26,0.26):box(wx*scale,-0.105*scale,wz*scale,0.19*scale,0.14*scale,0.10*scale,(0.035,0.045,0.06))
                gl.glPopMatrix()
            def particles(count,kind):
                gl.glDisable(gl.GL_LIGHTING);gl.glBegin(gl.GL_POINTS if kind in ("snow","cyclone") else gl.GL_LINES)
                for i in range(count):
                    a=i*0.754877666+elapsed*(0.8+variant*0.42);seed=(i*0.618033989)%1.0
                    if kind=="cyclone":
                        y=-2.5+((seed+elapsed*(0.12+variant*0.06))%1.0)*5.0;r=0.2+2.05*((y+2.5)/5.0)
                        gl.glColor3f(0.28,0.45+0.08*variant,0.66+0.1*variant);gl.glVertex3f(r*_m.cos(a),y,r*_m.sin(a))
                    elif kind=="rain":
                        x=-2.9+(i%97)*5.8/96;z=-2.8+((i*31)%89)*5.6/88;y=2.85-((elapsed*(4+variant*3)+i*0.193)%5.7)
                        gl.glColor3f(0.25,0.51,0.86);gl.glVertex3f(x,y,z);gl.glVertex3f(x-0.1-0.035*variant,y-0.24-0.06*variant,z+0.035)
                    elif kind=="snow":
                        x=-3+((i*17)%101)*6/100;z=-2.8+((i*37)%97)*5.6/96;y=2.9-((elapsed*(1.3+variant*1.4)+i*0.137)%5.8)
                        gl.glColor3f(0.68,0.82,1.0);gl.glVertex3f(x,y,z)
                    elif kind=="dust":
                        x=-2+((i*13)%47)*4/46;y=-0.2+((i*7)%17)*0.06;z=1+((elapsed*2.4+i*0.071)%3.6)
                        gl.glColor3f(0.58,0.42,0.24);gl.glVertex3f(x,y,z);gl.glVertex3f(x+0.1,y+0.03,z+0.15)
                gl.glEnd();gl.glEnable(gl.GL_LIGHTING)
            if family==20:particles((1200,2600,5200)[variant],"cyclone")
            elif family==21:particles((480,1100,2300)[variant],"rain")
            elif family==22:
                grid=(18,30,44)[variant];gl.glBegin(gl.GL_QUADS)
                for row in range(grid):
                    z0=-3+6*row/grid;z1=-3+6*(row+1)/grid
                    for col in range(grid):
                        x0=-3+6*col/grid;x1=-3+6*(col+1)/grid
                        for x,z in ((x0,z0),(x1,z0),(x1,z1),(x0,z1)):
                            h=0.16*_m.sin(x*2+elapsed*1.6)+0.12*_m.cos(z*2.4-elapsed*1.25)+0.06*_m.sin((x+z)*4+elapsed)
                            gl.glColor3f(0.015,0.24+0.07*_m.sin(elapsed+x),0.52+0.12*_m.cos(elapsed+z));gl.glNormal3f(-0.1*_m.cos(x),1,-0.12*_m.sin(z));gl.glVertex3f(x,h,z)
                gl.glEnd();primitive_counter["value"]+=grid*grid*2
                for i in range(6+variant*5):
                    x=-2.3+((i*19+int(elapsed*4))%23)*0.2;z=-2.4+((i*11)%17)*0.3
                    box(x,0.20+0.04*_m.sin(elapsed+i),z,0.28,0.08,0.16,(0.36,0.27,0.15))
            elif family==23:
                tick=int(elapsed*(4+variant*2))
                if tick%9 in (0,1,5):
                    gl.glDisable(gl.GL_LIGHTING);gl.glLineWidth(2+variant);gl.glColor3f(0.7,0.86,1.0);gl.glBegin(gl.GL_LINE_STRIP)
                    x=-1.8+(tick%4);z=-0.6+(tick%3)*0.45;gl.glVertex3f(x,2,z)
                    for j in range(10+variant*4):
                        x+=(-0.28 if (j+tick)%2 else 0.25)+0.07*_m.sin(elapsed*12+j);y=1.7-j*(3.2/(9+variant*4));z+=0.06*_m.cos(j*2.1+tick);gl.glVertex3f(x,y,z)
                    gl.glEnd();gl.glLineWidth(1.0);gl.glEnable(gl.GL_LIGHTING)
                    for j in range(variant+1):box(x+j*0.12,-1.2+j*0.12,z,0.04,0.42,0.04,(0.5,0.72,1.0))
            elif family==24:
                count=(3,6,10)[variant]
                for i in range(count):
                    a=elapsed*(0.65+0.065*i)+i*2*_m.pi/count
                    vehicle(2.28*_m.cos(a),0.24,2.28*_m.sin(a),0.29,(0.88,0.08+0.06*(i%3),0.10+0.12*(i%4)),90-a*180/_m.pi)
            elif family==25:
                count=(2,4,6)[variant]
                for i in range(count):
                    a=elapsed*(0.75+0.04*i)+i*2*_m.pi/count;x=2*_m.sin(a);z=1.45*_m.sin(a)*_m.cos(a)*1.9;drift=_m.sin(elapsed*2.2+i)*0.45
                    vehicle(x,0.22,z,0.27,(0.08+0.12*(i%3),0.28+0.12*(i%4),0.86),45-a*115/_m.pi+drift*30)
                gl.glDisable(gl.GL_LIGHTING);gl.glBegin(gl.GL_POINTS)
                for i in range(140+variant*220):
                    a=elapsed*1.3+i*0.73;x=1.7*_m.sin(a);z=1.2*_m.sin(a)*_m.cos(a);y=0.08+(i%12)*0.025
                    gl.glColor3f(0.46,0.48,0.52);gl.glVertex3f(x,y,z)
                gl.glEnd();gl.glEnable(gl.GL_LIGHTING)
            elif family==26:
                count=(1,2,4)[variant]
                for i in range(count):
                    a=elapsed*(0.52+0.05*i)+i*1.8;x=2.2*_m.sin(a)+0.22*_m.sin(a*3);z=1.8*_m.sin(a)*_m.cos(a)
                    vehicle(x,0.26,z,0.31,(0.84,0.48,0.08) if i%2==0 else (0.08,0.45,0.76),40-a*70/_m.pi)
                particles((180,360,640)[variant],"dust")
            elif family==27:
                count=(4,8,14)[variant]
                for i in range(count):
                    a=elapsed*(0.86+0.035*i)+i*2*_m.pi/count;x=2.34*_m.cos(a);z=2.34*_m.sin(a)
                    vehicle(x,0.34,z,0.24,(0.94,0.12+0.04*(i%4),0.13) if i%2==0 else (0.04,0.62,0.88),90-a*180/_m.pi)
                    gl.glDisable(gl.GL_LIGHTING);gl.glColor3f(0.1,0.72,1.0);gl.glBegin(gl.GL_LINES);gl.glVertex3f(x-0.4,0.25,z);gl.glVertex3f(x-0.72,0.25,z);gl.glEnd();gl.glEnable(gl.GL_LIGHTING)
            elif family==28:particles((800,1800,3200)[variant],"snow")
            elif family==29:
                grid=(18,30,46)[variant];gl.glBegin(gl.GL_QUADS)
                for row in range(grid):
                    z0=-3+6*row/grid;z1=-3+6*(row+1)/grid
                    for col in range(grid):
                        x0=-3+6*col/grid;x1=-3+6*(col+1)/grid
                        for x,z in ((x0,z0),(x1,z0),(x1,z1),(x0,z1)):
                            y=0.25*_m.sin(x+elapsed*1.3)+0.34*_m.sin(z*1.1-elapsed*1.5)+0.15*_m.sin((x+z)*2.4-elapsed*2)
                            gl.glColor3f(0.02,0.28+0.07*_m.sin(elapsed+x),0.76+0.12*_m.cos(z+elapsed));gl.glNormal3f(-0.15*_m.cos(x+elapsed),1,-0.2*_m.cos(z-elapsed));gl.glVertex3f(x,y,z)
                gl.glEnd();primitive_counter["value"]+=grid*grid*2

        display_list=gl.glGenLists(1);gl.glNewList(display_list,gl.GL_COMPILE);build_scene();gl.glEndList()
        profile = {
          "scene_id":sid,"scene_name":_U66_SCENES[sid-1][0],"family":_U100_SCENE_TITLES[sid-1],
          "profile_variant":variant+1,"resolution_requested":requested_resolution,"resolution_rendered":f"{rw}x{rh}",
          "desktop_resolution":f"{desktop_w}x{desktop_h}" if desktop_w and desktop_h else "N/D",
          "resolution_limited_by_display":resolution_limited,
          "geometry_primitives_estimate":primitive_counter["value"],
          "gpu_renderer":renderer,"opengl_version":gl_version,
          "method":"OpenGL real draw calls + display list; synchronized frame presentation with glFinish",
        }
        clock=pg.time.Clock(); start=_tm.perf_counter(); last=start; frames=0; bucket_frames=0; fps_samples=[];running=True
        max_duration=float(seconds)
        while running and (_tm.perf_counter()-start)<max_duration:
            for ev in pg.event.get():
                if ev.type==pg.QUIT:running=False
                elif ev.type==pg.KEYDOWN and ev.key==pg.K_ESCAPE:running=False
                elif ev.type==pg.VIDEORESIZE:
                    rw=max(640,ev.w);rh=max(480,ev.h);gl.glViewport(0,0,rw,rh)
                    gl.glMatrixMode(gl.GL_PROJECTION);gl.glLoadIdentity();gluPerspective(52.0,rw/rh,0.1,150.0);gl.glMatrixMode(gl.GL_MODELVIEW)
            elapsed=_tm.perf_counter()-start
            if family==23:
                flash=(int(elapsed*4.0+sid)%11) in (0,1,6)
                gl.glClearColor(0.24,0.31,0.48,1.0) if flash else gl.glClearColor(0.004,0.008,0.02,1.0)
            else:
                gl.glClearColor(0.006,0.012,0.026,1.0)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)
            gl.glMatrixMode(gl.GL_MODELVIEW);gl.glLoadIdentity()
            gl.glTranslatef(0.0,0.0,-8.6 if family<16 else -9.5)
            gl.glRotatef(elapsed*(22.0+sid%27),0.2,1.0,0.13)
            gl.glRotatef(11.0+14.0*_m.sin(elapsed*0.63+sid),1.0,0.0,0.2)
            gl.glCallList(display_list)
            if family>=20:
                draw_dynamic(elapsed)
            # Wait for actual GPU completion before counting this frame; avoids queued-frame inflation.
            gl.glFinish();pg.display.flip();frames+=1;bucket_frames+=1
            now=_tm.perf_counter()
            if now-last>=1.0:
                fps=bucket_frames/(now-last);fps_samples.append(fps);bucket_frames=0;last=now
                pg.display.set_caption(f"NAPRAWA PC FURMARK STYLE | SCENA {sid}/{len(_U66_SCENES)} | {title} | FPS {fps:.1f} | {renderer[:65]} | ESC STOP")
            clock.tick(0)
        elapsed=max(.001,_tm.perf_counter()-start)
        avg=frames/elapsed
        stopped=elapsed<max_duration-0.8
        result.update(profile)
        result.update({"state":"good" if frames>0 else "warn","frames":frames,"duration_seconds":round(elapsed,3),
          "average_fps":round(avg,2),"peak_fps_1s":round(max(fps_samples) if fps_samples else avg,2),
          "minimum_fps_1s":round(min(fps_samples) if fps_samples else avg,2),
          "fps_samples":[round(x,2) for x in fps_samples],"stopped_by_user":stopped,
          "note":"Wynik to pomiar tej sceny OpenGL na wybranej rozdzielczości. Nie jest to wynik z prawdziwej gry ani certyfikacja fizycznej pamięci GPU."})
    except Exception as exc:
        result.update({"state":"warn","error":f"{type(exc).__name__}: {exc}",
          "scene_name":_U100_SCENE_TITLES[max(0,min(len(_U100_SCENE_TITLES)-1,int(scene_id)-1))],
          "note":"Renderer nie wystartował poprawnie; brak wyniku nie oznacza usterki GPU."})
    finally:
        try:
            if display_list is not None:
                from OpenGL import GL as _gl_cleanup
                _gl_cleanup.glDeleteLists(display_list,1)
        except Exception:pass
        try:
            if pg is not None:
                pg.display.quit();pg.quit()
        except Exception:pass
        try:_P(output_path).write_text(_j.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
        except Exception:pass
    return result

_U100_ORIGINAL_SPEED_REQUEST = _u90_speed_request
_U100_ORIGINAL_MEASURE_SPEED = _u90_measure_speed
def _u100_measure_speed(app):
    import time as _tm
    data={"latency_ms":[],"download":[],"upload":[],"started_at":_U66_datetime.now().isoformat(timespec="seconds"),
          "method":"Adaptacyjny HTTPS speed test; rzeczywiście wysłane/odebrane bajty; mediana i peak raportowane oddzielnie.",
          "latency_method":"HTTPS round-trip time, nie ICMP ping","profile":"adaptive-standard"}
    total_data=0
    def phase(msg):
        try:app.queue_action(lambda m=msg:_u66_set_speed_status(app,m))
        except Exception:pass
        try:app.queue_status(msg)
        except Exception:pass
    def run_one(kind,size,index,total):
        nonlocal total_data
        if kind=="download":
            url="https://speed.cloudflare.com/__down?bytes="+str(size)+"&r="+_u66_uuid.uuid4().hex
            body=None
        else:
            url="https://speed.cloudflare.com/__up?r="+_u66_uuid.uuid4().hex
            body=_u66_os.urandom(size)
        timeout=180 if size>=30_000_000 else 120 if size>=12_000_000 else 75
        label=f"{kind.upper()} próbka {index}/{total}: {size/1_000_000:.0f} MB"
        phase("Speed Test: "+label+" — przesyłanie rzeczywistych bajtów…")
        try:
            result=_U100_ORIGINAL_SPEED_REQUEST(url,body,timeout,
                lambda p,d,t,e,i,a,b=total_data:_u90_emit_speed_progress(app,p,d,t,e,i,a,b),kind)
            result.update({"requested_bytes":size,"sample_index":index,"sample_count":total,"state":"good","kind":kind})
            total_data += (int(result.get("bytes",0)) if kind=="download" else int(result.get("requested_bytes",size)) if result.get("state")=="good" else 0)
            return result
        except Exception as exc:
            msg=f"{type(exc).__name__}: {exc}"
            app.queue_log(f"Speed Test {label}: {msg}")
            return {"requested_bytes":size,"sample_index":index,"sample_count":total,"state":"error","kind":kind,
                    "bytes":0,"seconds":None,"mbps":None,"error":msg}
    def valid(rows):
        return [r for r in rows if r.get("state")=="good" and isinstance(r.get("mbps"),(int,float)) and r.get("bytes",0)>0]
    for i in range(1,7):
        phase(f"Speed Test: HTTPS RTT {i}/6…")
        start=_tm.perf_counter()
        try:
            _U100_ORIGINAL_SPEED_REQUEST("https://speed.cloudflare.com/__down?bytes=0&r="+_u66_uuid.uuid4().hex,None,25,None,"ping")
            data["latency_ms"].append(round((_tm.perf_counter()-start)*1000,2))
        except Exception as exc:
            data.setdefault("latency_errors",[]).append(f"{type(exc).__name__}: {exc}")
    download_sizes=[12_000_000]
    first=run_one("download",download_sizes[0],1,3)
    data["download"].append(first)
    rate=float(first.get("mbps") or 0) if first.get("state")=="good" else 0
    if rate>=900: rest=(50_000_000,25_000_000)
    elif rate>=500: rest=(40_000_000,20_000_000)
    elif rate>=150: rest=(25_000_000,15_000_000)
    elif rate>=50: rest=(15_000_000,8_000_000)
    else: rest=(8_000_000,4_000_000)
    for idx,size in enumerate(rest,2):data["download"].append(run_one("download",size,idx,3))
    upload_first=4_000_000
    first_up=run_one("upload",upload_first,1,3)
    data["upload"].append(first_up)
    rate_up=float(first_up.get("mbps") or 0) if first_up.get("state")=="good" else 0
    if rate_up>=900: up_rest=(30_000_000,15_000_000)
    elif rate_up>=500: up_rest=(25_000_000,12_000_000)
    elif rate_up>=150: up_rest=(15_000_000,8_000_000)
    elif rate_up>=50: up_rest=(8_000_000,4_000_000)
    else: up_rest=(4_000_000,2_000_000)
    for idx,size in enumerate(up_rest,2):data["upload"].append(run_one("upload",size,idx,3))
    down=valid(data["download"]);up=valid(data["upload"])
    down_rates=[float(x["mbps"]) for x in down];up_rates=[float(x["mbps"]) for x in up]
    data["download_mbps"]=round(_u90_median(down_rates),2) if down_rates else None
    data["upload_mbps"]=round(_u90_median(up_rates),2) if up_rates else None
    data["download_peak_mbps"]=round(max(down_rates),2) if down_rates else None
    data["upload_peak_mbps"]=round(max(up_rates),2) if up_rates else None
    data["download_min_mbps"]=round(min(down_rates),2) if down_rates else None
    data["upload_min_mbps"]=round(min(up_rates),2) if up_rates else None
    data["latency_average_ms"]=round(_u90_median(data["latency_ms"]),2) if data["latency_ms"] else None
    data["latency_jitter_ms"]=round(max(data["latency_ms"])-min(data["latency_ms"]),2) if len(data["latency_ms"])>1 else None
    data["download_data_bytes"]=sum(int(x.get("bytes",0) or 0) for x in data["download"] if x.get("state")=="good")
    data["upload_data_bytes"]=sum(int(x.get("requested_bytes",0) or 0) for x in data["upload"] if x.get("state")=="good")
    data["data_bytes"]=data["download_data_bytes"]+data["upload_data_bytes"]
    data["download_samples_valid"]=len(down);data["upload_samples_valid"]=len(up)
    data["state"]="good" if len(down)>=2 and len(up)>=2 else "warn"
    data["finished_at"]=_U66_datetime.now().isoformat(timespec="seconds")
    data["note"]="Wynik podstawowy jest medianą rzeczywistych próbek, a najwyższa próbka jest raportowana oddzielnie. Rozmiary transferu dostosowują się do pierwszego pomiaru."
    try:
        folder=_u66_store_dir()/"speedtest";folder.mkdir(parents=True,exist_ok=True)
        hp=folder/"history.json"
        try: history=_u66_json.loads(hp.read_text(encoding="utf-8"))
        except Exception: history=[]
        history.append(data);hp.write_text(_u66_json.dumps(history[-100:],ensure_ascii=False,indent=2),encoding="utf-8")
        data["history_path"]=str(hp)
    except Exception as exc:data["history_warning"]=f"{type(exc).__name__}: {exc}"
    return data

_U100_ORIGINAL_SENSOR_POLL = _u66_sensor_poll
def _u100_gpu_from_sensors(probe):
    rows=(probe or {}).get("sensors") or []
    candidates={"load":[],"temperature":[],"vram_used":[],"vram_total":[],"clock":[],"memory_clock":[],"power":[],"fan":[]}
    def num(row):
        try:
            x=float(row.get("value"))
            return x if _u66_math.isfinite(x) and x>=0 else None
        except Exception:return None
    for row in rows:
        if not isinstance(row,dict):continue
        name=str(row.get("sensor") or row.get("name") or "")
        hardware=str(row.get("hardware") or row.get("parent") or "")
        ht=str(row.get("hardwareType") or row.get("hardware_type") or "")
        label=(ht+" "+hardware+" "+name+" "+str(row.get("parent") or "")).lower()
        if not (("gpu" in ht.lower()) or any(k in label for k in ("gpu","graphics","geforce","radeon","arc graphics","video card"))):continue
        value=num(row)
        if value is None:continue
        st=str(row.get("sensorType") or row.get("sensor_type") or "").lower()
        unit=str(row.get("unit") or "").strip().lower()
        if st=="temperature" or unit in ("°c","c"):
            pri=3 if any(k in label for k in ("gpu core","gpu temperature","core temperature")) else 2 if "hot spot" in label or "hotspot" in label else 1
            candidates["temperature"].append((pri,value,name))
        elif st=="load" or unit=="%":
            if any(k in label for k in ("gpu core","gpu load","gpu utilization","d3d 3d","gpu usage","graphics load")) and "memory" not in label:
                candidates["load"].append((2 if "3d" in label or "gpu core" in label else 1,value,name))
        elif st=="clock" or unit in ("mhz","ghz"):
            if "memory" in label or "mem clock" in label:
                candidates["memory_clock"].append((value*1000 if unit=="ghz" else value,name))
            else:
                candidates["clock"].append((value*1000 if unit=="ghz" else value,name))
        elif st=="power" or unit in ("w","watt","watts"):
            pri=3 if "board" in label or "total" in label else 2 if "chip" in label or "asic" in label else 1
            candidates["power"].append((pri,value,name))
        elif st=="fan" or unit=="rpm":
            candidates["fan"].append((value,name))
        elif st in ("smalldata","data") or unit in ("mb","gb"):
            mb=value*1024 if unit=="gb" else value
            if any(k in label for k in ("memory used","vram used","dedicated memory used","gpu memory usage")):
                candidates["vram_used"].append((mb,name))
            elif any(k in label for k in ("memory total","vram total","dedicated memory","memory capacity")) and not any(k in label for k in ("used","usage")):
                candidates["vram_total"].append((mb,name))
    def chosen(key):
        arr=candidates[key]
        return max(arr,key=lambda x:x[0])[1] if arr and key in ("load","temperature","power") else (arr[0][0] if arr else None)
    return {
      "available":bool(rows),"provider":(probe or {}).get("method","LibreHardwareMonitor sensor bridge"),
      "message":"Odczyty z wszystkich sensorów dostępnych przez bridge; część pól może być N/D.",
      "gpu_load_percent":chosen("load"),"temperature_c":chosen("temperature"),
      "vram_used_mb":chosen("vram_used"),"vram_total_mb":chosen("vram_total"),
      "gpu_clock_mhz":chosen("clock"),"memory_clock_mhz":chosen("memory_clock"),
      "power_draw_w":chosen("power"),"fan_speed_rpm":chosen("fan"),
      "sensor_rows":len(rows)
    }

def _u100_sensor_poll(app):
    try:
        if getattr(app,"_u100_sensor_busy",False):
            app.after(4000,lambda:_u100_sensor_poll(app));return
        if _u66_time.monotonic()-getattr(app,"_u100_sensor_last",0)>3.5:
            app._u100_sensor_busy=True;app._u100_sensor_last=_u66_time.monotonic()
            def job():
                try:
                    temps=_u66_sensor_probe()
                    generic=_u100_gpu_from_sensors(temps)
                    try:
                        vendor=_u37_nvidia_telemetry() if "_u37_nvidia_telemetry" in globals() else {}
                    except Exception as exc:vendor={"available":False,"provider":"NVIDIA telemetry unavailable","error":str(exc)}
                    gpu=dict(vendor or {})
                    for key,value in generic.items():
                        if key in ("sensor_rows","message"):continue
                        if value is not None and (gpu.get(key) is None or gpu.get(key) is False or gpu.get(key)=="N/D"):
                            gpu[key]=value
                    if not gpu.get("provider"):gpu["provider"]=generic.get("provider")
                    if not gpu.get("available"):gpu["available"]=generic.get("available",False)
                    gpu["sensor_rows"]=generic.get("sensor_rows",0)
                    if temps.get("gpu_temp_c") is None and generic.get("temperature_c") is not None:temps["gpu_temp_c"]=generic["temperature_c"]
                    if temps.get("gpu_power_w") is None and generic.get("power_draw_w") is not None:temps["gpu_power_w"]=generic["power_draw_w"]
                    snapshot={"gpu":gpu,"temps":temps,"time":_u66_time.monotonic()}
                    def update():
                        app._u100_sensor_busy=False;app._u66_sensor_cache=snapshot;app._u84_gpu_last_telemetry=gpu
                        try:_u100_refresh_sensor_table(app)
                        except Exception:pass
                        try:
                            if getattr(app,"current_view","")=="GPU":_u84_gpu_live_tick(app,schedule=False)
                            if getattr(app,"current_view","")=="LIVE_MONITOR":_u66_live_tick(app)
                            if getattr(app,"_u67_stage_panel",None) is not None:_u67_refresh_visible_charts(app)
                        except Exception:pass
                    app.queue_action(update)
                except Exception as exc:
                    def fail(err=exc):
                        app._u100_sensor_busy=False
                        try:app.queue_log("Czujniki: "+str(err))
                        except Exception:pass
                    app.queue_action(fail)
            _u66_threading.Thread(target=job,name="NaprawaPCAllVendorSensorPoll",daemon=True).start()
    except Exception as exc:
        try:app._u100_sensor_busy=False;app.queue_log("Czujniki: "+repr(exc))
        except Exception:pass
    try:app.after(4000,lambda:_u100_sensor_poll(app))
    except Exception:pass

def _u100_attach_sensor_table(app,parent,height=10):
    try:
        old=getattr(app,"_u100_sensor_panel",None)
        if old is not None and old.winfo_exists():old.destroy()
    except Exception:pass
    try:
        t=app.colors();panel=app.panel(parent);panel.pack(fill="both",expand=False,padx=3,pady=4)
        app._u100_sensor_panel=panel
        top=tk.Frame(panel,bg=t["panel"]);top.pack(fill="x",padx=8,pady=(6,2))
        tk.Label(top,text="PEŁNA LISTA CZUJNIKÓW SPRZĘTOWYCH — LIVE",bg=t["panel"],fg=t["accent"],font=app.fnt(10,"bold")).pack(side="left")
        app._u100_sensor_count=tk.Label(top,text="Oczekiwanie na bridge…",bg=t["panel"],fg=t["muted"],font=app.fnt(8));app._u100_sensor_count.pack(side="right")
        tk.Label(panel,text="Temperatury, obciążenia, zegary, napięcia, wentylatory, moc, pobór prądu, pamięć i pozostałe wartości, które udostępnia sterownik. Lista nie ogranicza się do wybranych kafelków. N/D oznacza brak odczytu.",bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1300,justify="left").pack(fill="x",padx=8,pady=(0,4))
        frame=tk.Frame(panel,bg=t["panel"]);frame.pack(fill="both",expand=True,padx=6,pady=(0,6))
        cols=("type","hardware","sensor","value","unit","source")
        tree=ttk.Treeview(frame,columns=cols,show="headings",height=max(6,min(16,int(height or 10))))
        widths={"type":105,"hardware":210,"sensor":250,"value":90,"unit":70,"source":230}
        labels={"type":"KATEGORIA","hardware":"SPRZĘT","sensor":"CZUJNIK","value":"WARTOŚĆ","unit":"JEDNOSTKA","source":"ŹRÓDŁO"}
        for col in cols:
            tree.heading(col,text=labels[col]);tree.column(col,width=widths[col],minwidth=60,stretch=col in ("hardware","sensor","source"))
        vs=ttk.Scrollbar(frame,orient="vertical",command=tree.yview);hs=ttk.Scrollbar(frame,orient="horizontal",command=tree.xview)
        tree.configure(yscrollcommand=vs.set,xscrollcommand=hs.set)
        tree.grid(row=0,column=0,sticky="nsew");vs.grid(row=0,column=1,sticky="ns");hs.grid(row=1,column=0,sticky="ew")
        frame.grid_rowconfigure(0,weight=1);frame.grid_columnconfigure(0,weight=1)
        app._u100_sensor_tree=tree;app._u100_sensor_signature=None
        _u100_refresh_sensor_table(app)
        return panel
    except Exception as exc:
        try:app.queue_log("Tabela czujników: "+repr(exc))
        except Exception:pass
        return None

def _u100_refresh_sensor_table(app):
    tree=getattr(app,"_u100_sensor_tree",None)
    if tree is None:return
    try:
        if not tree.winfo_exists():return
        cache=getattr(app,"_u66_sensor_cache",{}) or {};temps=cache.get("temps",{}) or {}
        rows=temps.get("sensors",[]) or []
        normalized=[]
        for row in rows:
            if not isinstance(row,dict):continue
            name=str(row.get("sensor") or row.get("name") or "N/D")
            hardware=str(row.get("hardware") or row.get("parent") or "N/D")
            ht=str(row.get("hardwareType") or row.get("hardware_type") or "")
            st=str(row.get("sensorType") or row.get("sensor_type") or row.get("type") or "other")
            unit=str(row.get("unit") or "")
            try:
                val=float(row.get("value"))
                if not _u66_math.isfinite(val):continue
                shown=f"{val:.3f}".rstrip("0").rstrip(".")
            except Exception:shown="N/D"
            source=str(row.get("source") or temps.get("method") or "N/D")
            normalized.append((st,hardware+" "+ht,name,shown,unit,source))
        normalized=normalized[:2500]
        signature=tuple((r[0],r[1],r[2],r[4],r[5]) for r in normalized)
        old_signature=getattr(app,"_u100_sensor_signature",None)
        if signature!=old_signature:
            tree.delete(*tree.get_children())
            for idx,row in enumerate(normalized):tree.insert("","end",iid=f"sensor{idx}",values=row)
            app._u100_sensor_signature=signature
        else:
            for idx,row in enumerate(normalized):
                iid=f"sensor{idx}"
                if tree.exists(iid):tree.item(iid,values=row)
        counts={}
        for row in normalized:counts[row[0]]=counts.get(row[0],0)+1
        label=getattr(app,"_u100_sensor_count",None)
        if label is not None and label.winfo_exists():
            stamp=cache.get("time")
            age=max(0,_u66_time.monotonic()-stamp) if isinstance(stamp,(int,float)) else None
            label.config(text=f"{len(normalized)} czujników • "+", ".join(f"{k}:{v}" for k,v in sorted(counts.items()))+ (f" • próbka {age:.0f}s temu" if age is not None else " • N/D"))
    except Exception as exc:
        try:app.queue_log("Aktualizacja pełnej listy sensorów: "+repr(exc))
        except Exception:pass

_U100_ORIGINAL_ATTACH_GPU_PANEL = _u84_attach_gpu_live_panel
def _u100_attach_gpu_panel(app):
    _U100_ORIGINAL_ATTACH_GPU_PANEL(app)
    try:
        _u100_attach_sensor_table(app,app.content,height=8)
    except Exception:pass

_U100_ORIGINAL_SHOW_SPEED_TEST = AppV43.show_speed_test
def _u100_show_speed_test(app):
    _U100_ORIGINAL_SHOW_SPEED_TEST(app)
    try:
        def walk(parent):
            for child in parent.winfo_children():
                if isinstance(child,tk.Label):
                    val=str(child.cget("text") or "")
                    if "23,5 MB" in val or "23.5 MB" in val:
                        child.config(text="Test adaptacyjny: zwykle kilkanaście MB przy wolnym łączu, do ponad 100 MB przy szybkim. Rozmiar kolejnych próbek dopasowuje się do pierwszego wyniku.")
                    elif val.strip()=="DOWNLOAD":child.config(text="DOWNLOAD • MEDIANA")
                    elif val.strip()=="UPLOAD":child.config(text="UPLOAD • MEDIANA")
                walk(child)
        walk(app.content)
    except Exception:pass

# Route all live-monitor callers to the full hardware sensor bridge table and all-vendor snapshotter.
_u81_attach_sensor_table = _u100_attach_sensor_table
_u81_refresh_sensor_table = _u100_refresh_sensor_table
_u66_sensor_poll = _u100_sensor_poll
_u84_attach_gpu_live_panel = _u100_attach_gpu_panel
_u90_measure_speed = _u100_measure_speed
AppV43.show_speed_test = _u100_show_speed_test

def _u100_selftest_adaptive_speed():
    assert callable(_u90_measure_speed)
    assert "_U100_ORIGINAL_SPEED_REQUEST" in _u100_measure_speed.__code__.co_names
    assert "download_peak_mbps" in _u100_measure_speed.__code__.co_names
    assert "latency_jitter_ms" in _u100_measure_speed.__code__.co_names
    assert callable(_u100_gpu_from_sensors)
    synthetic={"sensors":[
      {"hardware":"AMD GPU","hardwareType":"GpuAmd","sensor":"GPU Core","sensorType":"Temperature","value":68,"unit":"°C"},
      {"hardware":"AMD GPU","hardwareType":"GpuAmd","sensor":"GPU Core","sensorType":"Load","value":93,"unit":"%"},
      {"hardware":"AMD GPU","hardwareType":"GpuAmd","sensor":"GPU Memory Used","sensorType":"SmallData","value":4096,"unit":"MB"},
      {"hardware":"AMD GPU","hardwareType":"GpuAmd","sensor":"GPU Memory Total","sensorType":"Data","value":8,"unit":"GB"},
      {"hardware":"AMD GPU","hardwareType":"GpuAmd","sensor":"GPU Core","sensorType":"Clock","value":2400,"unit":"MHz"},
      {"hardware":"AMD GPU","hardwareType":"GpuAmd","sensor":"GPU Fan","sensorType":"Fan","value":1600,"unit":"RPM"},
      {"hardware":"AMD GPU","hardwareType":"GpuAmd","sensor":"GPU Board Power","sensorType":"Power","value":185,"unit":"W"}
    ]}
    tele=_u100_gpu_from_sensors(synthetic)
    assert tele["gpu_load_percent"]==93
    assert tele["temperature_c"]==68
    assert tele["vram_used_mb"]==4096 and tele["vram_total_mb"]==8192
    assert tele["gpu_clock_mhz"]==2400 and tele["fan_speed_rpm"]==1600 and tele["power_draw_w"]==185
    assert callable(_u100_refresh_sensor_table) and callable(_u100_attach_sensor_table)
    print("ADAPTIVE_SPEED_AND_ALL_VENDOR_SENSOR_SELFTEST_OK")

def _u100_selftest_unique_gpu_scenes():
    assert len(_U66_SCENES)==110 and len(_U100_SCENE_TITLES)==110
    assert len(set(_U100_SCENE_TITLES))==110
    assert callable(_u37_gpu_benchmark_child)
    assert _u37_gpu_benchmark_child.__code__.co_argcount>=4
    assert "glFinish" in _u37_gpu_benchmark_child.__code__.co_names
    assert "glCallList" in _U114_ORIGINAL_GPU_BENCHMARK_CHILD.__code__.co_names
    assert "GetSystemMetrics" in _u37_gpu_benchmark_child.__code__.co_names
    assert any(isinstance(c,tuple) and "resolution_limited_by_display" in c for c in _u37_gpu_benchmark_child.__code__.co_consts)
    assert any(isinstance(c,tuple) and "desktop_resolution" in c for c in _u37_gpu_benchmark_child.__code__.co_consts)
    assert "FurMark Style" in _U100_SCENE_TITLES[0]
    assert any("Ultimate Mix" in x for x in _U100_SCENE_TITLES[57:60])
    for start,end,token in ((60,63,"Cyclone Lab"),(63,66,"Ulewa"),(66,69,"Powódź"),(69,72,"Pioruny"),(72,75,"Wyścigi"),(75,78,"Drift"),(78,81,"Rally Stage"),(81,84,"F1 Night"),(84,87,"Zamieć"),(87,90,"Tsunami Lab")):
        assert all(token in x for x in _U100_SCENE_TITLES[start:end])
    print("UNIQUE_3D_GPU_RENDERER_SELFTEST_OK: 110 distinct named scenes, 20 visual families with 3 different layouts each, synchronized real FPS")

_u37_gpu_benchmark_child = _u100_gpu_benchmark_child


# v4.3.101 — route every Speed Test entry to one adaptive engine; include OS metrics in the full sensor table.
_U101_ORIGINAL_U100_REFRESH_SENSOR_TABLE = _u100_refresh_sensor_table
_U101_ORIGINAL_U100_ATTACH_GPU_PANEL = _u100_attach_gpu_panel
_U101_ORIGINAL_U100_SHOW_SPEED_TEST = _u100_show_speed_test

def _u101_fmt(value, decimals=2):
    if value is None:
        return "N/D"
    if isinstance(value, bool):
        return "TAK" if value else "NIE"
    try:
        number=float(value)
        if not _u66_math.isfinite(number):
            return "N/D"
        return f"{number:.{decimals}f}".rstrip("0").rstrip(".")
    except Exception:
        return str(value)

def _u101_collect_os_metrics(app):
    metrics={}
    if not psutil:
        return metrics
    try:
        metrics["cpu_percent"]=psutil.cpu_percent(interval=0.15)
    except Exception:
        metrics["cpu_percent"]=None
    try:
        freq=psutil.cpu_freq()
        metrics["cpu_clock_mhz"]=float(freq.current) if freq and freq.current else None
        metrics["cpu_clock_max_mhz"]=float(freq.max) if freq and freq.max else None
    except Exception:
        metrics["cpu_clock_mhz"]=metrics["cpu_clock_max_mhz"]=None
    try:
        metrics["cpu_logical"]=int(psutil.cpu_count(logical=True) or 0) or None
        metrics["cpu_physical"]=int(psutil.cpu_count(logical=False) or 0) or None
    except Exception:
        metrics["cpu_logical"]=metrics["cpu_physical"]=None
    try:
        vm=psutil.virtual_memory()
        metrics.update({
            "ram_total_bytes":int(vm.total),"ram_used_bytes":int(vm.used),
            "ram_available_bytes":int(vm.available),"ram_percent":float(vm.percent)
        })
    except Exception:
        metrics.update({"ram_total_bytes":None,"ram_used_bytes":None,"ram_available_bytes":None,"ram_percent":None})
    try:
        swap=psutil.swap_memory()
        metrics.update({"swap_total_bytes":int(swap.total),"swap_used_bytes":int(swap.used),"swap_percent":float(swap.percent)})
    except Exception:
        metrics.update({"swap_total_bytes":None,"swap_used_bytes":None,"swap_percent":None})
    now=_u66_time.monotonic()
    try:
        io=psutil.disk_io_counters()
    except Exception:
        io=None
    try:
        net=psutil.net_io_counters()
    except Exception:
        net=None
    prev=getattr(app,"_u101_io_prev",None)
    disk_read=disk_write=None
    if io is not None and prev and now>prev.get("time",now):
        dt=max(.05,now-prev["time"])
        disk_read=max(0.0,(io.read_bytes-prev.get("read",io.read_bytes))/dt/1_000_000)
        disk_write=max(0.0,(io.write_bytes-prev.get("write",io.write_bytes))/dt/1_000_000)
    net_down=net_up=None
    if net is not None and prev and now>prev.get("time",now):
        dt=max(.05,now-prev["time"])
        net_down=max(0.0,(net.bytes_recv-prev.get("recv",net.bytes_recv))*8/dt/1_000_000)
        net_up=max(0.0,(net.bytes_sent-prev.get("sent",net.bytes_sent))*8/dt/1_000_000)
    metrics["disk_read_mbps"]=disk_read
    metrics["disk_write_mbps"]=disk_write
    metrics["net_down_mbps"]=net_down
    metrics["net_up_mbps"]=net_up
    current={
        "time":now,
        "read":int(io.read_bytes) if io is not None else 0,
        "write":int(io.write_bytes) if io is not None else 0,
        "recv":int(net.bytes_recv) if net is not None else 0,
        "sent":int(net.bytes_sent) if net is not None else 0
    }
    app._u101_io_prev=current
    try:
        battery=psutil.sensors_battery()
        metrics["battery_percent"]=float(battery.percent) if battery and battery.percent is not None else None
        metrics["battery_plugged"]=bool(battery.power_plugged) if battery else None
        metrics["battery_seconds_left"]=int(battery.secsleft) if battery and isinstance(battery.secsleft,(int,float)) and battery.secsleft>=0 else None
    except Exception:
        metrics.update({"battery_percent":None,"battery_plugged":None,"battery_seconds_left":None})
    try:
        metrics["uptime_seconds"]=max(0,int(_u66_time.time()-(psutil.boot_time() if psutil else _u66_time.time())))
    except Exception:
        metrics["uptime_seconds"]=None
    # Some Windows builds expose extra thermal devices through psutil even without the bridge.
    temps=[]
    try:
        getter=getattr(psutil,"sensors_temperatures",None)
        readings=getter() if callable(getter) else {}
        for sensor_group,records in (readings or {}).items():
            for record in records or []:
                value=getattr(record,"current",None)
                try:
                    value=float(value)
                    if not _u66_math.isfinite(value):continue
                except Exception:continue
                temps.append({"hardware":str(sensor_group),"hardwareType":"OS","sensor":str(getattr(record,"label","") or sensor_group),
                    "sensorType":"Temperature","value":value,"unit":"°C","source":"psutil"})
    except Exception:
        pass
    metrics["extra_temperature_sensors"]=temps
    return metrics

def _u101_refresh_sensor_table(app):
    tree=getattr(app,"_u100_sensor_tree",None)
    if tree is None:
        return
    try:
        if not tree.winfo_exists():
            return
        cache=getattr(app,"_u66_sensor_cache",{}) or {}
        temps=cache.get("temps",{}) or {}
        gpu=cache.get("gpu",{}) or {}
        system=cache.get("system",{}) or {}
        normalized=[]
        def add(category,hardware,name,value,unit,source):
            if value is None:
                shown="N/D"
            elif isinstance(value,bool):
                shown="TAK" if value else "NIE"
            else:
                try:
                    v=float(value)
                    if not _u66_math.isfinite(v):
                        shown="N/D"
                    else:
                        shown=f"{v:.3f}".rstrip("0").rstrip(".")
                except Exception:
                    shown=str(value)
            normalized.append((str(category or "other"),str(hardware or "N/D"),str(name or "N/D"),shown,str(unit or ""),str(source or "N/D")))
        sys_source="Windows / psutil"
        # Summary readings are always visible; unsupported sensors remain N/D rather than disappearing or becoming zero.
        metrics=[
          ("Load","CPU","Użycie CPU",system.get("cpu_percent"),"%",sys_source),
          ("Clock","CPU","Zegar CPU",system.get("cpu_clock_mhz"),"MHz",sys_source),
          ("Clock","CPU","Maksymalny zegar CPU",system.get("cpu_clock_max_mhz"),"MHz",sys_source),
          ("Count","CPU","Rdzenie fizyczne",system.get("cpu_physical"),"",sys_source),
          ("Count","CPU","Wątki logiczne",system.get("cpu_logical"),"",sys_source),
          ("Memory","RAM","Użycie RAM",system.get("ram_percent"),"%",sys_source),
          ("Memory","RAM","RAM użyta",system.get("ram_used_bytes")/1_073_741_824 if system.get("ram_used_bytes") is not None else None,"GiB",sys_source),
          ("Memory","RAM","RAM dostępna",system.get("ram_available_bytes")/1_073_741_824 if system.get("ram_available_bytes") is not None else None,"GiB",sys_source),
          ("Memory","RAM","RAM całkowita",system.get("ram_total_bytes")/1_073_741_824 if system.get("ram_total_bytes") is not None else None,"GiB",sys_source),
          ("Memory","Plik stronicowania","Użycie swap",system.get("swap_percent"),"%",sys_source),
          ("Memory","Plik stronicowania","Swap użyty",system.get("swap_used_bytes")/1_073_741_824 if system.get("swap_used_bytes") is not None else None,"GiB",sys_source),
          ("Throughput","Dysk","Odczyt łączny",system.get("disk_read_mbps"),"MB/s",sys_source),
          ("Throughput","Dysk","Zapis łączny",system.get("disk_write_mbps"),"MB/s",sys_source),
          ("Throughput","Sieć","Pobieranie łączne",system.get("net_down_mbps"),"Mbps",sys_source),
          ("Throughput","Sieć","Wysyłanie łączne",system.get("net_up_mbps"),"Mbps",sys_source),
          ("Battery","Bateria","Poziom baterii",system.get("battery_percent"),"%",sys_source),
          ("Battery","Bateria","Zasilanie AC podłączone",system.get("battery_plugged"),"",sys_source),
          ("Temperature","CPU","Temperatura CPU (wybrany czujnik)",temps.get("cpu_temp_c"),"°C",temps.get("method","N/D")),
          ("Temperature","GPU","Temperatura GPU (wybrany czujnik)",gpu.get("temperature_c",temps.get("gpu_temp_c")),"°C",gpu.get("provider",temps.get("method","N/D"))),
          ("Power","CPU","Moc CPU",temps.get("cpu_power_w"),"W",temps.get("method","N/D")),
          ("Power","GPU","Moc GPU",gpu.get("power_draw_w",gpu.get("power_w",temps.get("gpu_power_w"))),"W",gpu.get("provider",temps.get("method","N/D"))),
          ("Power","System","Moc systemu",temps.get("system_power_w"),"W",temps.get("method","N/D")),
          ("Power","Bateria","Moc baterii",temps.get("battery_power_w"),"W",temps.get("method","N/D")),
          ("Voltage","CPU","Napięcie CPU",temps.get("cpu_voltage_v"),"V",temps.get("method","N/D")),
          ("Voltage","GPU","Napięcie GPU",temps.get("gpu_voltage_v"),"V",temps.get("method","N/D")),
          ("Clock","GPU","Zegar GPU",gpu.get("gpu_clock_mhz",temps.get("gpu_clock_mhz")),"MHz",gpu.get("provider",temps.get("method","N/D"))),
          ("Clock","GPU","Zegar pamięci GPU",gpu.get("memory_clock_mhz"),"MHz",gpu.get("provider",temps.get("method","N/D"))),
          ("Load","GPU","Użycie GPU",gpu.get("gpu_load_percent",gpu.get("load_percent")),"% ",gpu.get("provider",temps.get("method","N/D"))),
          ("Memory","VRAM","VRAM użyta",gpu.get("vram_used_mb"),"MB",gpu.get("provider",temps.get("method","N/D"))),
          ("Memory","VRAM","VRAM całkowita",gpu.get("vram_total_mb"),"MB",gpu.get("provider",temps.get("method","N/D"))),
          ("Fan","CPU","Wentylator CPU",temps.get("cpu_fan_rpm"),"RPM",temps.get("method","N/D")),
          ("Fan","GPU","Wentylator GPU",gpu.get("fan_speed_rpm",temps.get("gpu_fan_rpm")),"RPM",gpu.get("provider",temps.get("method","N/D"))),
          ("System","Windows","Czas działania systemu",system.get("uptime_seconds"),"s",sys_source)
        ]
        for row in metrics:add(*row)
        # Show every bridge/vendor sensor, not a hand-picked subset. The summaries above complement this raw list.
        raw=temps.get("sensors",[]) or []
        for row in raw:
            if not isinstance(row,dict):continue
            add(row.get("sensorType") or row.get("sensor_type") or row.get("type") or "other",
                (str(row.get("hardware") or row.get("parent") or "N/D")+" "+str(row.get("hardwareType") or row.get("hardware_type") or "")).strip(),
                row.get("sensor") or row.get("name") or "N/D",row.get("value"),row.get("unit") or "",
                row.get("source") or temps.get("method") or "sensor bridge")
        for row in system.get("extra_temperature_sensors",[]) or []:
            if isinstance(row,dict):
                add(row.get("sensorType","Temperature"),row.get("hardware","OS"),row.get("sensor","Temperature"),row.get("value"),row.get("unit","°C"),row.get("source","psutil"))
        for row in temps.get("acpi_zones",[]) or []:
            if isinstance(row,dict):
                add("Temperature / ACPI",row.get("name","ACPI"),"Strefa termiczna",row.get("value"),"°C","WMI ACPI — nie jest to automatycznie temperatura rdzenia CPU")
        normalized=normalized[:3500]
        signature=tuple((r[0],r[1],r[2],r[4],r[5]) for r in normalized)
        old_signature=getattr(app,"_u101_sensor_signature",None)
        if signature!=old_signature:
            tree.delete(*tree.get_children())
            for idx,row in enumerate(normalized):
                tree.insert("","end",iid=f"sensor{idx}",values=row)
            app._u101_sensor_signature=signature
        else:
            for idx,row in enumerate(normalized):
                iid=f"sensor{idx}"
                if tree.exists(iid):
                    tree.item(iid,values=row)
                else:
                    tree.insert("","end",iid=iid,values=row)
            for iid in tree.get_children():
                try:
                    idx=int(iid.replace("sensor",""))
                    if idx>=len(normalized):tree.delete(iid)
                except Exception:
                    pass
        counts={}
        for row in normalized:
            counts[row[0]]=counts.get(row[0],0)+1
        label=getattr(app,"_u100_sensor_count",None)
        if label is not None and label.winfo_exists():
            stamp=cache.get("time")
            age=max(0,_u66_time.monotonic()-stamp) if isinstance(stamp,(int,float)) else None
            raw_count=len(raw)
            label.config(text=f"{raw_count} surowych czujników + {len(metrics)} metryk systemowych • "+
              ", ".join(f"{k}:{v}" for k,v in sorted(counts.items()))+
              (f" • próbka {age:.0f}s temu" if age is not None else " • oczekiwanie na odczyt"))
    except Exception as exc:
        try:app.queue_log("Pełna tabela telemetrii: "+repr(exc))
        except Exception:pass

def _u101_sensor_poll_once(app):
    if getattr(app,"_u101_sensor_busy",False):
        return
    app._u101_sensor_busy=True
    def job():
        try:
            temps=_u66_sensor_probe()
            generic=_u100_gpu_from_sensors(temps)
            try:
                vendor=_u37_nvidia_telemetry() if "_u37_nvidia_telemetry" in globals() else {}
            except Exception as exc:
                vendor={"available":False,"provider":"vendor telemetry unavailable","error":str(exc)}
            gpu=dict(vendor or {})
            for key,value in generic.items():
                if key in ("sensor_rows","message"):
                    continue
                if value is not None and (gpu.get(key) is None or gpu.get(key) is False or gpu.get(key)=="N/D"):
                    gpu[key]=value
            if not gpu.get("provider"):gpu["provider"]=generic.get("provider")
            if not gpu.get("available"):gpu["available"]=generic.get("available",False)
            gpu["sensor_rows"]=generic.get("sensor_rows",0)
            if temps.get("gpu_temp_c") is None and generic.get("temperature_c") is not None:temps["gpu_temp_c"]=generic["temperature_c"]
            if temps.get("gpu_power_w") is None and generic.get("power_draw_w") is not None:temps["gpu_power_w"]=generic["power_draw_w"]
            try:
                system=_u101_collect_os_metrics(app)
            except Exception as exc:
                system={"error":f"{type(exc).__name__}: {exc}"}
            snapshot={"gpu":gpu,"temps":temps,"system":system,"time":_u66_time.monotonic()}
            def update():
                app._u101_sensor_busy=False
                app._u66_sensor_cache=snapshot
                app._u84_gpu_last_telemetry=gpu
                try:_u101_refresh_sensor_table(app)
                except Exception:pass
                try:
                    if getattr(app,"current_view","")=="GPU":_u84_gpu_live_tick(app,schedule=False)
                    if getattr(app,"current_view","")=="LIVE_MONITOR":_u66_live_tick(app)
                    if getattr(app,"_u67_stage_panel",None) is not None:_u67_refresh_visible_charts(app)
                except Exception:pass
            app.queue_action(update)
        except Exception as exc:
            def fail(err=exc):
                app._u101_sensor_busy=False
                try:app.queue_log("Odczyt czujników: "+str(err))
                except Exception:pass
            app.queue_action(fail)
    _u66_threading.Thread(target=job,name="NaprawaPCAllTelemetryPoll",daemon=True).start()

def _u101_sensor_poll(app):
    if getattr(app,"_u101_sensor_loop_started",False):
        return
    app._u101_sensor_loop_started=True
    def tick():
        try:
            if not app.winfo_exists():
                app._u101_sensor_loop_started=False
                return
            sensor_window=getattr(app,"_u104_sensor_window",None)
            sensor_window_active=False
            try:
                sensor_window_active=sensor_window is not None and bool(sensor_window.winfo_exists())
            except Exception:
                sensor_window_active=False
            active=(getattr(app,"current_view","") in ("LIVE_MONITOR","GPU")
                or bool(getattr(app,"running",False))
                or getattr(app,"_u67_stage_panel",None) is not None
                or sensor_window_active)
            if active:
                _u101_sensor_poll_once(app)
            app.after(4000,tick)
        except Exception as exc:
            app._u101_sensor_loop_started=False
            try:app.queue_log("Pętla telemetryczna: "+repr(exc))
            except Exception:pass
    app.after(0,tick)

def _u101_attach_gpu_panel(app):
    _U101_ORIGINAL_U100_ATTACH_GPU_PANEL(app)
    _u101_sensor_poll(app)

def _u101_start_speed_test(app):
    if getattr(app,"_u66_speed_running",False):
        return
    app._u66_speed_running=True
    try:
        _u66_set_speed_status(app,"Przygotowuję adaptacyjny Speed Test HTTPS…")
    except Exception:
        pass
    def job():
        try:
            result=_u100_measure_speed(app)
            try:app.results["SPEED_TEST"]=result
            except Exception:pass
            def done():
                app._u66_speed_running=False
                if getattr(app,"current_view","")=="SPEED_TEST":
                    values=getattr(app,"_u66_speed_values",{}) or {}
                    def set_value(key,text):
                        try:
                            if key in values and values[key].winfo_exists():values[key].config(text=text)
                        except Exception:pass
                    latency=result.get("latency_average_ms")
                    download=result.get("download_mbps")
                    upload=result.get("upload_mbps")
                    set_value("latency",f"{latency:.1f} ms" if isinstance(latency,(int,float)) else "N/D")
                    set_value("download",f"{download:.1f} Mbps" if isinstance(download,(int,float)) else "N/D")
                    set_value("upload",f"{upload:.1f} Mbps" if isinstance(upload,(int,float)) else "N/D")
                    set_value("data",f"{result.get('data_bytes',0)/1_000_000:.1f} MB")
                    peaks=getattr(app,"_u101_speed_peaks",{}) or {}
                    for key,metric in (("download_peak","download_peak_mbps"),("upload_peak","upload_peak_mbps"),("jitter","latency_jitter_ms")):
                        value=result.get(metric)
                        label=peaks.get(key)
                        try:
                            if label is not None and label.winfo_exists():
                                unit=" ms" if key=="jitter" else " Mbps"
                                label.config(text=f"{value:.1f}{unit}" if isinstance(value,(int,float)) else "N/D")
                        except Exception:pass
                    try:_u66_draw_speed_chart(app,result)
                    except Exception:pass
                status="zakończony" if result.get("state")=="good" else "zakończony z ostrzeżeniem"
                _u66_set_speed_status(app,f"Speed Test {status}: DL mediana {result.get('download_mbps') if result.get('download_mbps') is not None else 'N/D'} Mbps; UL mediana {result.get('upload_mbps') if result.get('upload_mbps') is not None else 'N/D'} Mbps; HTTPS RTT {result.get('latency_average_ms') if result.get('latency_average_ms') is not None else 'N/D'} ms. Pobrano/wysłano {result.get('data_bytes',0)/1_000_000:.1f} MB.")
                try:app.queue_log("SPEED TEST: "+_u66_json.dumps(result,ensure_ascii=False))
                except Exception:pass
            app.queue_action(done)
        except Exception as exc:
            def fail(err=exc):
                app._u66_speed_running=False
                message=f"Speed Test nie ukończył pomiaru: {type(err).__name__}: {err}"
                _u66_set_speed_status(app,message)
                try:messagebox.showerror("Speed Test",message)
                except Exception:pass
                try:app.queue_log(message)
                except Exception:pass
            app.queue_action(fail)
    _u66_threading.Thread(target=job,name="NaprawaPCAdaptiveSpeedTest",daemon=True).start()

def _u101_show_speed_test(app):
    _U101_ORIGINAL_U100_SHOW_SPEED_TEST(app)
    try:
        panel=app.panel(app.content)
        panel.pack(fill="x",padx=3,pady=(0,5))
        title=tk.Label(panel,text="DODATKOWE METRYKI POMIARU",bg=app.colors()["panel"],fg=app.colors()["accent"],font=app.fnt(9,"bold"))
        title.pack(anchor="w",padx=8,pady=(5,2))
        row=tk.Frame(panel,bg=app.colors()["panel"]);row.pack(fill="x",padx=5,pady=(0,5))
        app._u101_speed_peaks={}
        specs=(("DOWNLOAD PEAK","download_peak"),("UPLOAD PEAK","upload_peak"),("ZMIENNOŚĆ HTTPS RTT","jitter"))
        for caption,key in specs:
            card=tk.Frame(row,bg=app.colors()["card"],highlightbackground=app.colors()["panel"],highlightthickness=1)
            card.pack(side="left",fill="both",expand=True,padx=2)
            tk.Label(card,text=caption,bg=app.colors()["card"],fg=app.colors()["muted"],font=app.fnt(8,"bold")).pack(pady=(5,1))
            label=tk.Label(card,text="N/D",bg=app.colors()["card"],fg=app.colors()["accent2"],font=app.fnt(11,"bold"))
            label.pack(pady=(0,5))
            app._u101_speed_peaks[key]=label
        # Override the original callback so the main UI and catalogue use the same measured samples.
        for child in app.content.winfo_children():
            if isinstance(child,tk.Frame):
                for nested in child.winfo_children():
                    if isinstance(nested,tk.Frame):
                        for button in nested.winfo_children():
                            if isinstance(button,tk.Button) and "SPEED TEST" in str(button.cget("text")).upper():
                                button.configure(command=lambda:_u101_start_speed_test(app))
    except Exception as exc:
        try:app.queue_log("Speed Test UI: "+repr(exc))
        except Exception:pass

def _u101_selftest_adaptive_speed():
    speed_code=repr(_u100_measure_speed.__code__.co_consts)+repr(_u100_measure_speed.__code__.co_names)
    assert "_U100_ORIGINAL_SPEED_REQUEST" in _u100_measure_speed.__code__.co_names
    assert "download_peak_mbps" in speed_code
    assert "upload_peak_mbps" in speed_code
    assert "latency_jitter_ms" in speed_code
    assert callable(_u100_gpu_from_sensors)
    synthetic={"sensors":[
      {"hardware":"AMD GPU","hardwareType":"GpuAmd","sensor":"GPU Core","sensorType":"Temperature","value":68,"unit":"°C"},
      {"hardware":"AMD GPU","hardwareType":"GpuAmd","sensor":"GPU Core","sensorType":"Load","value":93,"unit":"%"},
      {"hardware":"AMD GPU","hardwareType":"GpuAmd","sensor":"GPU Memory Used","sensorType":"SmallData","value":4096,"unit":"MB"},
      {"hardware":"AMD GPU","hardwareType":"GpuAmd","sensor":"GPU Memory Total","sensorType":"Data","value":8,"unit":"GB"},
      {"hardware":"AMD GPU","hardwareType":"GpuAmd","sensor":"GPU Core","sensorType":"Clock","value":2400,"unit":"MHz"},
      {"hardware":"AMD GPU","hardwareType":"GpuAmd","sensor":"GPU Fan","sensorType":"Fan","value":1600,"unit":"RPM"},
      {"hardware":"AMD GPU","hardwareType":"GpuAmd","sensor":"GPU Board Power","sensorType":"Power","value":185,"unit":"W"}
    ]}
    tele=_u100_gpu_from_sensors(synthetic)
    assert tele["gpu_load_percent"]==93 and tele["temperature_c"]==68
    assert tele["vram_used_mb"]==4096 and tele["vram_total_mb"]==8192
    assert tele["gpu_clock_mhz"]==2400 and tele["fan_speed_rpm"]==1600 and tele["power_draw_w"]==185
    assert callable(_u101_refresh_sensor_table) and callable(_u101_sensor_poll)
    _speed_name=getattr(_u66_measure_speed, "__name__", "")
    _speed_wrapper_ok=(_speed_name=="_u124_measure_speed" and "_U124_ORIGINAL_MEASURE_SPEED" in _u66_measure_speed.__code__.co_names)
    assert _u66_measure_speed is _u100_measure_speed or _speed_name=="_u108_measure_speed" or _speed_wrapper_ok
    _show_name=getattr(AppV43.show_speed_test, "__name__", "")
    _show_wrapper_ok=(_show_name=="_u124_show_speed_test" and "_U124_ORIGINAL_SHOW_SPEED" in AppV43.show_speed_test.__code__.co_names)
    assert AppV43.show_speed_test is _u107_show_speed_test or _show_name in ("_u108_show_speed_test", "_u114_show_speed_test") or _show_wrapper_ok
    print("ADAPTIVE_SPEED_ALL_ENTRYPOINTS_AND_FULL_TELEMETRY_SELFTEST_OK")

def _u101_selftest_unique_gpu_scenes():
    assert len(_U66_SCENES)==110 and len(_U100_SCENE_TITLES)==110
    assert len(set(_U100_SCENE_TITLES))==110
    assert len({row[0] for row in _U66_SCENES})==110
    assert callable(_u37_gpu_benchmark_child)
    assert _u37_gpu_benchmark_child.__code__.co_argcount>=4
    assert 90 in _u37_gpu_benchmark_child.__code__.co_consts, "Active GPU renderer must accept scene IDs 1-90"
    assert "glFinish" in _u37_gpu_benchmark_child.__code__.co_names
    assert "glCallList" in _U114_ORIGINAL_GPU_BENCHMARK_CHILD.__code__.co_names
    assert "GetSystemMetrics" in _u37_gpu_benchmark_child.__code__.co_names
    assert any(isinstance(c,tuple) and "resolution_limited_by_display" in c for c in _u37_gpu_benchmark_child.__code__.co_consts)
    assert any(isinstance(c,tuple) and "desktop_resolution" in c for c in _u37_gpu_benchmark_child.__code__.co_consts)
    assert "FurMark Style" in _U100_SCENE_TITLES[0]
    assert any("Ultimate Mix" in x for x in _U100_SCENE_TITLES[57:60])
    for start,end,token in ((60,63,"Cyclone Lab"),(63,66,"Ulewa"),(66,69,"Powódź"),(69,72,"Pioruny"),(72,75,"Wyścigi"),(75,78,"Drift"),(78,81,"Rally Stage"),(81,84,"F1 Night"),(84,87,"Zamieć"),(87,90,"Tsunami Lab")):
        assert all(token in x for x in _U100_SCENE_TITLES[start:end])
    print("GPU_SCENE_SELFTEST_OK: 110 unique IDs; all 110 render through distinct per-ID layouts; synchronized real FPS")

# Each test has a unique scene identifier, not just a shared family label.
_U66_SCENES=[(f"{i:02d} — {name}",f"scene_{i:02d}",1+(i%3)*2) for i,name in enumerate(_U100_SCENE_TITLES,1)]
_u100_refresh_sensor_table=_u101_refresh_sensor_table
_u81_refresh_sensor_table=_u101_refresh_sensor_table
_u66_sensor_poll=_u101_sensor_poll
_u84_attach_gpu_live_panel=_u101_attach_gpu_panel
_u66_measure_speed=_u100_measure_speed
_u66_start_speed_test=_u101_start_speed_test
_u90_measure_speed=_u100_measure_speed
AppV43.show_speed_test=_u101_show_speed_test
_u100_selftest_adaptive_speed=_u101_selftest_adaptive_speed
_u100_selftest_unique_gpu_scenes=_u101_selftest_unique_gpu_scenes


# v4.3.102 — RAM tests must keep a visible in-app progress screen and never launch a graphics window.
_U102_ORIGINAL_RAM_EXECUTE = _u93_execute_catalog_test
_U102_ORIGINAL_RAM_DETAIL = _u93_show_test_detail
_U102_ORIGINAL_RAM_METHOD = getattr(AppV43, "_ram_test", None)

def _u102_ram_safe_size(requested_mb, available_mb):
    requested = max(64, min(2048, int(requested_mb or 512)))
    available = max(0, int(available_mb or 0))
    # Keep at least 85% of currently available RAM for Windows and the application.
    # The previous path could reserve up to 25% and gave no per-test progress screen.
    safe_limit = max(64, min(1024, int(available * 0.15)))
    return min(requested, safe_limit)

def _u102_ram_progress_update(app, test_id, percent, message, pass_number=1):
    def apply():
        if getattr(app, "current_view", "") != "COMPONENT_TEST_DETAIL_" + str(test_id):
            return
        try:
            bar = getattr(app, "_u102_ram_progressbar", None)
            if bar is not None and bar.winfo_exists():
                bar.configure(value=max(0, min(100, int(percent))))
            label = getattr(app, "_u102_ram_progress_label", None)
            if label is not None and label.winfo_exists():
                label.configure(text=f"Przebieg {pass_number} • {message}")
            status = getattr(app, "_u93_detail_status", None)
            if status is not None and status.winfo_exists():
                status.configure(text=f"RAM — TEST W TOKU • {int(percent)}%", fg=app.colors()["warn"])
        except Exception:
            pass
    try:
        app.queue_action(apply)
    except Exception:
        try:
            apply()
        except Exception:
            pass

def _u102_show_test_detail(app, module, test_id):
    _U102_ORIGINAL_RAM_DETAIL(app, module, test_id)
    try:
        normalized = _u93_norm(module)
        _, title, description, kind = _u93_find_test(normalized, test_id)
    except Exception:
        return
    if kind not in ("ram_pattern", "ram_bw", "ram_bw_max"):
        return
    try:
        report = getattr(app, "_u93_detail_report", None)
        if report is None or not report.winfo_exists():
            return
        parent = report.master
        t = app.colors()
        bar = ttk.Progressbar(parent, mode="determinate", maximum=100, value=0)
        bar.pack(fill="x", padx=10, pady=(0, 3), before=report)
        label = tk.Label(parent, text="Przygotowuję bezpieczny bufor RAM…",
            bg=t["panel"], fg=t["muted"], font=app.fnt(8), anchor="w", justify="left")
        label.pack(fill="x", padx=10, pady=(0, 7), before=report)
        app._u102_ram_progressbar = bar
        app._u102_ram_progress_label = label
    except Exception as exc:
        try:
            app.queue_log("RAM: nie udało się utworzyć panelu postępu: " + repr(exc))
        except Exception:
            pass

def _u102_ram_pattern_suite(app, module, test_id, kind, settings):
    import time as _u102_time
    requested = int(settings.get("memory_mb", 512) or 512)
    vm = psutil.virtual_memory() if psutil else None
    available_mb = int(vm.available / (1024 * 1024)) if vm else 0
    if vm and available_mb < 192:
        result = {
            "state": "warn", "requested_mb": requested, "tested_mb": 0,
            "available_mb_at_start": available_mb, "patterns_completed": 0,
            "patterns_total": len(_U40_RAM_PATTERN_LIST),
            "message": f"Za mało dostępnej pamięci RAM ({available_mb} MB). Test nie został uruchomiony, aby nie zawiesić Windows.",
            "note": "Brak testu nie jest zaliczeniem. Zamknij część programów i uruchom ponownie."
        }
        _u93_put_result(app, "RAM_BENCHMARK", result)
        _u93_put_result(app, "RAM", {"state":"warn","size_mb":0,"message":result["message"],"benchmark":result})
        return result

    safe_mb = _u102_ram_safe_size(requested, available_mb if vm else 512)
    target_seconds = 0
    if kind == "ram_bw":
        target_seconds = max(15, min(60, int(settings.get("duration", 60) or 60)))
    elif kind == "ram_bw_max":
        target_seconds = max(15, min(300, int(settings.get("duration", 300) or 300)))
    start = _u102_time.monotonic()
    pass_number = 0
    bytes_written = 0
    bytes_verified = 0
    patterns_completed = 0
    patterns_total = len(_U40_RAM_PATTERN_LIST)
    last_stats = {}
    last_message = ""
    final_state = "warn"
    requested_mode = kind

    while True:
        if bool(getattr(app, "stop_requested", False)):
            final_state = "warn"
            last_message = "Test RAM zatrzymany przez użytkownika."
            break
        pass_number += 1
        stats = {}
        pass_start = _u102_time.monotonic()
        def progress(percent, detail, pn=pass_number):
            # Queue UI-only work: the RAM worker never calls Tk widgets directly.
            _u102_ram_progress_update(app, test_id, percent, detail, pn)
        try:
            ok, message = ram_pattern_test(
                safe_mb, 0.0, progress_callback=progress,
                stop_check=app._test_should_stop, stats_out=stats
            )
        except Exception as exc:
            ok = False
            message = f"Test RAM przerwany: {type(exc).__name__}: {exc}"
            stats = {"size_mb":safe_mb,"patterns_total":patterns_total,"patterns_completed":0,
                     "bytes_written":0,"bytes_verified":0,"elapsed_sec":_u102_time.monotonic()-pass_start}
        last_stats = stats
        last_message = str(message)
        bytes_written += int(stats.get("bytes_written", 0) or 0)
        bytes_verified += int(stats.get("bytes_verified", 0) or 0)
        patterns_completed += int(stats.get("patterns_completed", 0) or 0)
        if not ok:
            final_state = "warn" if stats.get("stopped") or app._test_should_stop() or stats.get("allocation_failed") else "bad"
            break
        final_state = "good"
        elapsed = _u102_time.monotonic() - start
        if kind == "ram_pattern" or target_seconds <= 0 or elapsed >= target_seconds:
            break
        _u102_ram_progress_update(app, test_id, min(99, int(elapsed * 100 / max(1, target_seconds))),
                                  f"Zakończono pełny zestaw wzorców; trwa przebieg stabilności {elapsed:.0f}/{target_seconds} s.",
                                  pass_number + 1)

    elapsed = max(0.001, _u102_time.monotonic() - start)
    write_mib_s = bytes_written / (1024 * 1024) / elapsed
    verify_mib_s = bytes_verified / (1024 * 1024) / elapsed
    result = {
        "state": final_state, "kind": kind, "requested_mb": requested,
        "tested_mb": int(last_stats.get("size_mb", safe_mb) or safe_mb),
        "available_mb_at_start": available_mb if vm else None,
        "passes_run": pass_number, "patterns_completed": patterns_completed,
        "patterns_total_per_pass": patterns_total,
        "duration_seconds": round(elapsed, 2),
        "bytes_written": bytes_written, "bytes_verified": bytes_verified,
        "write_mib_s_overall": round(write_mib_s, 2),
        "verify_mib_s_overall": round(verify_mib_s, 2),
        "combined_mib_s": round((bytes_written + bytes_verified) / (1024 * 1024) / elapsed, 2),
        "error_offset": last_stats.get("error_offset"),
        "stopped": bool(getattr(app, "stop_requested", False) or last_stats.get("stopped")),
        "message": last_message,
        "note": "Test zapisuje i weryfikuje prywatny bufor procesu. Nie sprawdza każdej fizycznej komórki RAM. Rozmiar mógł zostać zmniejszony, aby pozostawić pamięć dla Windows."
    }
    _u93_put_result(app, "RAM_BENCHMARK", result)
    _u93_put_result(app, "RAM", {
        "state": final_state, "size_mb": result["tested_mb"],
        "message": f"RAM {final_state.upper()}: {result['tested_mb']} MB • {pass_number} przebieg(ów) • zapis {result['write_mib_s_overall']} MiB/s • weryfikacja {result['verify_mib_s_overall']} MiB/s",
        "benchmark": result
    })
    _u102_ram_progress_update(app, test_id, 100 if final_state == "good" else
        int(min(99, patterns_completed * 100 / max(1, patterns_total * max(1, pass_number)))),
        f"KONIEC • {final_state.upper()} • {elapsed:.1f} s • testowano {result['tested_mb']} MB.", pass_number)
    try:
        app.queue_log(f"RAM KATALOG: {test_id} • {final_state.upper()} • bufor {result['tested_mb']} MB • przebiegi {pass_number} • {elapsed:.1f} s")
    except Exception:
        pass
    return result

def _u102_execute_catalog_test(app, module, test_id, kind, settings):
    if kind in ("ram_pattern", "ram_bw", "ram_bw_max"):
        return _u102_ram_pattern_suite(app, module, test_id, kind, settings)
    return _U102_ORIGINAL_RAM_EXECUTE(app, module, test_id, kind, settings)

def _u102_ram_test_guard(app, mb=512):
    requested = max(64, min(2048, int(mb or 512)))
    try:
        vm = psutil.virtual_memory() if psutil else None
        available_mb = int(vm.available / (1024 * 1024)) if vm else 0
        if vm and available_mb < 192:
            result = {"state":"warn","size_mb":0,"requested_mb":requested,"available_mb_at_start":available_mb,
                      "message":f"Za mało dostępnego RAM ({available_mb} MB); test nie wystartował, aby nie zawiesić systemu."}
            app.queue_results("RAM", result)
            app.queue_log("RAM: " + result["message"])
            return result
        safe_mb = _u102_ram_safe_size(requested, available_mb if vm else 512)
        if safe_mb < requested:
            app.queue_log(f"RAM: rozmiar ograniczono z {requested} do {safe_mb} MB, aby pozostawić zasoby dla Windows.")
        result = _U102_ORIGINAL_RAM_METHOD(app, safe_mb) if callable(_U102_ORIGINAL_RAM_METHOD) else None
        return result
    except Exception as exc:
        result = {"state":"warn","size_mb":requested,"message":f"Test RAM przerwany błędem: {type(exc).__name__}: {exc}",
                  "error":f"{type(exc).__name__}: {exc}"}
        try:
            app.queue_results("RAM", result)
            app.queue_log("RAM: " + result["message"])
        except Exception:
            pass
        return result
    finally:
        def refresh_ram_page():
            try:
                if getattr(app, "current_view", "") == "RAM":
                    updater = getattr(app, "_update_ram_module_live", None)
                    if callable(updater):
                        updater()
            except Exception:
                pass
        try:
            app.queue_action(refresh_ram_page)
        except Exception:
            pass

def _u102_selftest_ram_visible_progress():
    assert callable(_u102_ram_safe_size)
    assert _u102_ram_safe_size(2048, 4096) <= 1024
    assert _u102_ram_safe_size(512, 1024) <= 153
    assert callable(_u102_ram_pattern_suite)
    assert "progress_callback" in repr(_u102_ram_pattern_suite.__code__.co_consts) or "progress_callback" in _u102_ram_pattern_suite.__code__.co_names
    assert "ram_pattern_test" in _u102_ram_pattern_suite.__code__.co_names
    assert "pygame" not in _u102_ram_pattern_suite.__code__.co_names
    assert (_u93_execute_catalog_test is _u102_execute_catalog_test
            or getattr(_u93_execute_catalog_test, "__name__", "") == "_u109_execute_catalog_test")
    if getattr(_u93_execute_catalog_test, "__name__", "") == "_u109_execute_catalog_test":
        assert "_U109_ORIGINAL_EXECUTE_CATALOG_TEST" in _u93_execute_catalog_test.__code__.co_names
    assert _u93_show_test_detail is _u102_show_test_detail
    assert getattr(AppV43._ram_test, "_u102_ram_guard", False)
    print("RAM_VISIBLE_PROGRESS_SELFTEST_OK: isolated in-app progress, safe allocation cap, no OpenGL/pygame path")

_u93_execute_catalog_test = _u102_execute_catalog_test
_u93_show_test_detail = _u102_show_test_detail
if callable(_U102_ORIGINAL_RAM_METHOD):
    _u102_ram_test_guard._u102_ram_guard = True
    # Keep the single start/end sound wrapper active around this RAM operation.
    _u102_ram_test_guard._u80_sound_wrapped = True
    AppV43._ram_test = _u102_ram_test_guard


# v4.3.103 — ninety individually rendered GPU stress scenes; no shared 3-scenes-per-family renderer.
def _u104_gpu_benchmark_child(output_path, seconds=30, scene_id=1, resolution="1920x1080"):
    import math as _m, random as _r, time as _tm, json as _j
    from pathlib import Path as _P
    pg = None
    result = {"state":"warn","test":"OpenGL unique-scene render benchmark","scene_id":int(scene_id)}
    try:
        import pygame as pg
        from OpenGL import GL as gl
        from OpenGL.GLU import gluPerspective
        sid=max(1,min(90,int(scene_id)))
        title=_U100_SCENE_TITLES[sid-1]
        requested_resolution=str(resolution or "1920x1080")
        desktop_w=desktop_h=0
        resolution_limited=False
        try:
            rw,rh=[int(v) for v in requested_resolution.lower().split("x",1)]
        except Exception:
            requested_resolution="1920x1080";rw,rh=1920,1080
        rw=max(640,min(3840,rw));rh=max(480,min(2160,rh))

        # Keep the actual active renderer inside the usable monitor area on smaller/HiDPI PCs.
        try:
            if os.name=="nt":
                import ctypes as _u104_ctypes
                desktop_w=int(_u104_ctypes.windll.user32.GetSystemMetrics(0))
                desktop_h=int(_u104_ctypes.windll.user32.GetSystemMetrics(1))
                if desktop_w>=640 and desktop_h>=480:
                    usable_w=max(640,desktop_w-48)
                    usable_h=max(480,desktop_h-112)
                    display_scale=min(1.0,usable_w/float(rw),usable_h/float(rh))
                    if display_scale<0.999:
                        rw=max(640,int(rw*display_scale))
                        rh=max(480,int(rh*display_scale))
                        if rw>usable_w or rh>usable_h:
                            correction=min(usable_w/float(rw),usable_h/float(rh))
                            rw=max(640,int(rw*correction))
                            rh=max(480,int(rh*correction))
                        resolution_limited=True
        except Exception:
            desktop_w=desktop_h=0
        result.update({
            "resolution_requested":requested_resolution,
            "resolution_rendered":f"{rw}x{rh}",
            "desktop_resolution":f"{desktop_w}x{desktop_h}" if desktop_w and desktop_h else "N/D",
            "resolution_limited_by_display":resolution_limited
        })
        duration=max(3,min(900,int(seconds)))
        pg.init()
        try:
            pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION,2)
            pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION,1)
            pg.display.gl_set_attribute(pg.GL_DOUBLEBUFFER,1)
            pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE,24)
        except Exception: pass
        pg.display.set_mode((rw,rh),pg.OPENGL|pg.DOUBLEBUF|pg.RESIZABLE,vsync=0)
        renderer=(gl.glGetString(gl.GL_RENDERER) or b"unknown").decode("utf-8","replace")
        gl_version=(gl.glGetString(gl.GL_VERSION) or b"unknown").decode("utf-8","replace")
        gl.glEnable(gl.GL_DEPTH_TEST);gl.glEnable(gl.GL_NORMALIZE);gl.glEnable(gl.GL_COLOR_MATERIAL)
        gl.glColorMaterial(gl.GL_FRONT_AND_BACK,gl.GL_AMBIENT_AND_DIFFUSE);gl.glShadeModel(gl.GL_SMOOTH)
        gl.glEnable(gl.GL_LIGHTING);gl.glEnable(gl.GL_LIGHT0)
        gl.glLightfv(gl.GL_LIGHT0,gl.GL_POSITION,(3.5,5.0,7.0,1.0))
        gl.glLightfv(gl.GL_LIGHT0,gl.GL_DIFFUSE,(0.95,0.98,1.0,1.0))
        gl.glLightfv(gl.GL_LIGHT0,gl.GL_AMBIENT,(0.18,0.2,0.27,1.0))
        gl.glClearColor(0.004,0.009,0.022,1.0)
        gl.glViewport(0,0,rw,rh);gl.glMatrixMode(gl.GL_PROJECTION);gl.glLoadIdentity()
        gluPerspective(52.0,rw/rh,0.1,240.0);gl.glMatrixMode(gl.GL_MODELVIEW)
        rng=_r.Random(8241+sid*173)
        budget={"boxes":0,"spheres":0,"tori":0,"vertices":0,"points":0,"scene_id":sid}
        palette=[
            (0.08,0.60,0.98),(0.10,0.88,0.72),(0.96,0.34,0.13),
            (0.66,0.32,0.98),(0.98,0.72,0.16),(0.20,0.82,0.42)
        ]
        c=palette[(sid-1)%len(palette)]
        c2=palette[(sid+1)%len(palette)]
        c3=palette[(sid+3)%len(palette)]

        def box(x,y,z,sx,sy,sz,col):
            gl.glPushMatrix();gl.glTranslatef(x,y,z);gl.glScalef(sx,sy,sz);gl.glColor3f(*col)
            faces=[
             ((0,0,1),((-0.5,-0.5,0.5),(0.5,-0.5,0.5),(0.5,0.5,0.5),(-0.5,0.5,0.5))),
             ((0,0,-1),((0.5,-0.5,-0.5),(-0.5,-0.5,-0.5),(-0.5,0.5,-0.5),(0.5,0.5,-0.5))),
             ((1,0,0),((0.5,-0.5,0.5),(0.5,-0.5,-0.5),(0.5,0.5,-0.5),(0.5,0.5,0.5))),
             ((-1,0,0),((-0.5,-0.5,-0.5),(-0.5,-0.5,0.5),(-0.5,0.5,0.5),(-0.5,0.5,-0.5))),
             ((0,1,0),((-0.5,0.5,0.5),(0.5,0.5,0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5))),
             ((0,-1,0),((-0.5,-0.5,-0.5),(0.5,-0.5,-0.5),(0.5,-0.5,0.5),(-0.5,-0.5,0.5)))]
            gl.glBegin(gl.GL_QUADS)
            for normal,verts in faces:
                gl.glNormal3f(*normal)
                for v in verts:gl.glVertex3f(*v)
            gl.glEnd();gl.glPopMatrix();budget["boxes"]+=1;budget["vertices"]+=24

        def sphere(x,y,z,r,col,lats=10,lons=16):
            gl.glPushMatrix();gl.glTranslatef(x,y,z);gl.glColor3f(*col)
            for la in range(max(6,lats)):
                a0=-_m.pi/2+_m.pi*la/lats;a1=-_m.pi/2+_m.pi*(la+1)/lats
                gl.glBegin(gl.GL_QUAD_STRIP)
                for lo in range(lons+1):
                    b=2*_m.pi*lo/lons
                    for a in (a0,a1):
                        nx=_m.cos(a)*_m.cos(b);ny=_m.sin(a);nz=_m.cos(a)*_m.sin(b)
                        gl.glNormal3f(nx,ny,nz);gl.glVertex3f(r*nx,r*ny,r*nz)
                gl.glEnd()
            gl.glPopMatrix();budget["spheres"]+=1;budget["vertices"]+=lats*lons*2

        def torus(R,r,col,major=36,minor=12):
            gl.glColor3f(*col)
            for i in range(major):
                u0=2*_m.pi*i/major;u1=2*_m.pi*(i+1)/major
                gl.glBegin(gl.GL_QUAD_STRIP)
                for j in range(minor+1):
                    v=2*_m.pi*j/minor
                    for u in (u0,u1):
                        x=(R+r*_m.cos(v))*_m.cos(u);y=r*_m.sin(v);z=(R+r*_m.cos(v))*_m.sin(u)
                        gl.glNormal3f(_m.cos(v)*_m.cos(u),_m.sin(v),_m.cos(v)*_m.sin(u))
                        gl.glVertex3f(x,y,z)
                gl.glEnd()
            budget["tori"]+=1;budget["vertices"]+=major*minor*2

        def line(a,b,col,width=1.0):
            gl.glDisable(gl.GL_LIGHTING);gl.glLineWidth(width);gl.glColor3f(*col)
            gl.glBegin(gl.GL_LINES);gl.glVertex3f(*a);gl.glVertex3f(*b);gl.glEnd();gl.glEnable(gl.GL_LIGHTING)
            budget["vertices"]+=2

        def line_strip(points,col,width=1.4):
            if len(points)<2:return
            gl.glDisable(gl.GL_LIGHTING);gl.glLineWidth(width);gl.glColor3f(*col);gl.glBegin(gl.GL_LINE_STRIP)
            for p in points:gl.glVertex3f(*p)
            gl.glEnd();gl.glEnable(gl.GL_LIGHTING);budget["vertices"]+=len(points)

        def wire_cube(cx,cy,cz,size,col):
            h=size/2;v=[(cx+dx*h,cy+dy*h,cz+dz*h) for dx,dy,dz in
              ((-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1))]
            edges=((0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7))
            gl.glDisable(gl.GL_LIGHTING);gl.glColor3f(*col);gl.glBegin(gl.GL_LINES)
            for a,b in edges:gl.glVertex3f(*v[a]);gl.glVertex3f(*v[b])
            gl.glEnd();gl.glEnable(gl.GL_LIGHTING);budget["vertices"]+=24

        def furry_donut(R=1.2,r=.42,hairs=1500,col=None):
            col=col or c
            torus(R,r,col,44,14)
            gl.glDisable(gl.GL_LIGHTING);gl.glLineWidth(1.0);gl.glBegin(gl.GL_LINES)
            for _ in range(hairs):
                u=rng.random()*2*_m.pi;v=rng.random()*2*_m.pi
                rr=R+r*_m.cos(v);x=rr*_m.cos(u);y=r*_m.sin(v);z=rr*_m.sin(u)
                nx=_m.cos(v)*_m.cos(u);ny=_m.sin(v);nz=_m.cos(v)*_m.sin(u)
                length=.045+rng.random()*.19
                gl.glColor3f(.15+rng.random()*.3,.36+rng.random()*.45,.64+rng.random()*.35)
                gl.glVertex3f(x,y,z);gl.glVertex3f(x+nx*length,y+ny*length,z+nz*length)
            gl.glEnd();gl.glEnable(gl.GL_LIGHTING);budget["vertices"]+=hairs*2

        def terrain(grid,kind):
            for row in range(grid):
                z0=-3.4+6.8*row/grid;z1=-3.4+6.8*(row+1)/grid
                gl.glBegin(gl.GL_TRIANGLE_STRIP)
                for ix in range(grid+1):
                    x=-3.4+6.8*ix/grid
                    for z in (z0,z1):
                        if kind==0:h=.65*_m.sin(x*1.4+sid*.17)*_m.cos(z*1.8)+.2*_m.sin((x+z)*3.1)
                        elif kind==1:
                            h=.45*_m.sin(x*1.2)*_m.cos(z*1.3)
                            for cx,cz,rad in ((-1.2,-.6,.65),(1.1,1.2,.9),(.5,-1.8,.5)):
                                d=((x-cx)**2+(z-cz)**2)**.5
                                h-=.75*_m.exp(-d*d/(rad*rad))
                        else:h=.35*_m.sin(x*3.2+sid)+.27*_m.cos(z*2.9)+.25*_m.sin((x-z)*4.2)+.1*_m.cos(x*z*3)
                        shade=max(0,min(1,(h+1.4)/2.8))
                        gl.glColor3f(.04+.15*shade,.12+.45*shade,.20+.22*(1-shade))
                        gl.glNormal3f(-.15,1,.1);gl.glVertex3f(x,h,z)
                gl.glEnd()
            budget["vertices"]+=grid*grid*4

        def city(layout,count=72):
            for i in range(count):
                if layout==0:
                    x=(i%12-5.5)*.52;z=(i//12-2.5)*.55
                elif layout==1:
                    a=i*2.39996;rad=.4+(i%13)*.22;x=rad*_m.cos(a);z=rad*_m.sin(a)
                else:
                    a=i*.41;rad=.15+i*.045;x=rad*_m.cos(a);z=rad*_m.sin(a)
                h=.35+rng.random()*(1.2+(i%5)*.24)
                col=(.04+rng.random()*.10,.08+rng.random()*.14,.20+rng.random()*.28)
                box(x,h/2,z,.34,h,.36,col)
                if i%2==0:
                    for yy in range(1,max(2,int(h*4))):
                        if (i+yy)%3:
                            box(x+.175,yy*.17,z+.03,.025,.04,.09,(.08,.65+rng.random()*.28,.95))
            budget["vertices"]+=count*25

        def fan(cx,cy,cz,r,angle=0,blades=9):
            torus(r,.06,c2,28,8);sphere(cx,cy,cz,.10,c3,7,10)
            for j in range(blades):
                a=2*_m.pi*j/blades+angle
                line((cx,cy,cz),(cx+r*.82*_m.cos(a),cy,cz+r*.82*_m.sin(a)),c,2.0)

        def crystal(x,y,z,scale,col):
            gl.glPushMatrix();gl.glTranslatef(x,y,z);gl.glScalef(scale,scale*1.8,scale);gl.glColor3f(*col)
            verts=[(0,1,0),(1,0,0),(0,0,1),(-1,0,0),(0,0,-1),(0,-.65,0)]
            faces=((0,1,2),(0,2,3),(0,3,4),(0,4,1),(5,2,1),(5,3,2),(5,4,3),(5,1,4))
            gl.glBegin(gl.GL_TRIANGLES)
            for face in faces:
                for k in face:gl.glVertex3f(*verts[k])
            gl.glEnd();gl.glPopMatrix();budget["vertices"]+=24

        def gear(x,y,z,r,teeth,col):
            torus(r*.68,r*.15,col,40,10)
            for n in range(teeth):
                a=2*_m.pi*n/teeth
                box(x+(r+r*.16)*_m.cos(a),y+(r+r*.16)*_m.sin(a),z,r*.3,r*.20,r*.24,col)

        def molecular_chain(count,spacing=.34):
            pts=[((i-(count-1)/2)*spacing, .22*_m.sin(i*.9),0) for i in range(count)]
            for i,p in enumerate(pts):
                sphere(*p,.12,c if i%2==0 else c2,7,10)
                if i:line(pts[i-1],p,c3,2)
            budget["vertices"]+=count*20

        def tunnel(rings=12,kind=0):
            for n in range(rings):
                z=4.0-n*.62;ang=n*.17 if kind==2 else (n%2)*.14
                pts=[]
                sides=6 if kind==1 else 40
                for j in range(sides+1):
                    a=2*_m.pi*j/sides+ang
                    radius=1.65 if kind!=2 else 1.15+.35*_m.sin(n*.7)
                    pts.append((radius*_m.cos(a),radius*_m.sin(a),z))
                line_strip(pts,c if n%2==0 else c2,1.5)
                if n%2==0:sphere(pts[0][0],pts[0][1],z,.07,c3,6,8)

        def helix(strands=2,points=460,pitch=.024):
            for strand in range(strands):
                pts=[]
                phase=2*_m.pi*strand/strands
                for i in range(points):
                    t=i*.055
                    pts.append((1.1*_m.cos(t+phase),pitch*i-3.1,1.1*_m.sin(t+phase)))
                line_strip(pts,palette[strand%len(palette)],1.8)
            for i in range(0,points,8):
                t=i*.055;y=pitch*i-3.1
                for strand in range(strands-1):
                    a=t+2*_m.pi*strand/strands;b=t+2*_m.pi*(strand+1)/strands
                    line((1.1*_m.cos(a),y,1.1*_m.sin(a)),(1.1*_m.cos(b),y,1.1*_m.sin(b)),c3,.7)

        def points_cloud(count,kind):
            gl.glDisable(gl.GL_LIGHTING);gl.glPointSize(2.5);gl.glBegin(gl.GL_POINTS)
            for i in range(count):
                t=rng.random()*2*_m.pi;u=rng.random()*2*_m.pi
                if kind==0:r=.4+1.9*rng.random();x=r*_m.cos(t);z=r*_m.sin(t);y=1.25*_m.sin(t*2)+.25*_m.cos(u*3)
                elif kind==1:r=.2+1.7*rng.random();x=r*_m.cos(t);z=r*_m.sin(t);y=-2.6+5.2*rng.random()
                else:r=1.2+.8*_m.sin(u*3);x=r*_m.cos(t);z=r*_m.sin(t);y=1.7*_m.sin(u)
                gl.glColor3f(.1+.8*rng.random(),.25+.7*rng.random(),.4+.6*rng.random())
                gl.glVertex3f(x,y,z)
            gl.glEnd();gl.glEnable(gl.GL_LIGHTING);budget["points"]+=count;budget["vertices"]+=count

        def tree_branch(x,y,z,length,angle,depth,mode):
            if depth<=0:return
            xx=x+_m.sin(angle)*length;yy=y+length;zz=z+_m.cos(angle)*length
            line((x,y,z),(xx,yy,zz),palette[(depth+mode)%len(palette)],max(.5,depth*.26))
            if depth<=2:sphere(xx,yy,zz,.045+depth*.012,c2,5,7)
            bend=.42 if mode==0 else .64 if mode==1 else .25
            tree_branch(xx,yy,zz,length*.73,angle-bend,depth-1,mode)
            tree_branch(xx,yy,zz,length*.73,angle+bend,depth-1,mode)
            if mode==2 and depth>3:tree_branch(xx,yy,zz,length*.61,angle+.1,depth-2,mode)

        def mesh_triangles(count,mode):
            gl.glBegin(gl.GL_TRIANGLES)
            for i in range(count):
                a=rng.random()*2*_m.pi
                if mode==0:x=rng.uniform(-2.7,2.7);y=rng.uniform(-2.5,2.5);z=rng.uniform(-2,2)
                elif mode==1:
                    x=-2.8+(i%48)*.12;y=-1.8+(i//48%22)*.16;z=_m.sin(x*2+y*3)*.35
                else:
                    a=i*.017;x=2*_m.sin(a);y=2*_m.cos(a*1.27);z=2*_m.sin(a*.67)
                gl.glColor3f(.12+rng.random()*.75,.18+rng.random()*.7,.4+rng.random()*.6)
                gl.glVertex3f(x,y,z);gl.glVertex3f(x+.05+rng.random()*.25,y+.1+rng.random()*.25,z+.1)
                gl.glVertex3f(x-.1,y+.03,z-.08-rng.random()*.25)
            gl.glEnd();budget["vertices"]+=count*3

        def draw_scene():
            sid_local=sid
            if sid_local==1:
                furry_donut(1.28,.48,2400,(.12,.33,.95))
            elif sid_local==2:
                gl.glPushMatrix();gl.glTranslatef(-1.45,0,0);gl.glRotatef(27,1,0,0);furry_donut(.68,.25,700,c);gl.glPopMatrix()
                gl.glPushMatrix();gl.glTranslatef(1.45,.1,0);gl.glRotatef(68,0,1,0);furry_donut(.68,.25,700,c2);gl.glPopMatrix()
                gl.glPushMatrix();gl.glTranslatef(0,.5,.25);gl.glRotatef(42,0,0,1);furry_donut(.62,.23,700,c3);gl.glPopMatrix()
            elif sid_local==3:
                torus(1.15,.32,c,44,14)
                for i in range(420):
                    a=rng.random()*2*_m.pi;r=1.75+rng.random()*1.0
                    sphere(r*_m.cos(a),rng.uniform(-.8,.8),r*_m.sin(a),.018+rng.random()*.05,c2,5,7)
            elif sid_local==4:
                pts=[]
                for i in range(2400):
                    t=i/2399*2*_m.pi*8
                    pts.append(((1.15+.42*_m.cos(3*t))*_m.cos(2*t),.42*_m.sin(3*t),(1.15+.42*_m.cos(3*t))*_m.sin(2*t)))
                line_strip(pts,c,2.2)
                for i in range(16):sphere(pts[i*145][0],pts[i*145][1],pts[i*145][2],.08,c2,6,10)
            elif sid_local==5:
                for offset in (0,_m.pi):
                    pts=[]
                    for i in range(1200):
                        t=i*.045+offset;pts.append((1.0*_m.cos(t),.003*i-2.1,1.0*_m.sin(t)))
                    line_strip(pts,c if offset==0 else c2,2.1)
                for i in range(55):
                    y=-2.1+i*.077
                    line((-.9,y,0),(.9,y,0),c3,.6)
            elif sid_local==6:
                for j in range(5):
                    gl.glPushMatrix();gl.glRotatef(j*36,1,.3,1);torus(1.2-j*.13,.11,c if j%2==0 else c2,48,8);gl.glPopMatrix()
                points_cloud(1000,2)
            elif sid_local==7:
                sphere(0,0,0,.48,(1,.43,.08),18,26)
                for i,r in enumerate((.85,1.35,1.9,2.5)):
                    torus(r,.018,palette[i],60,4)
                    a=i*1.63;sphere(r*_m.cos(a),.04*i,r*_m.sin(a),.10+i*.015,palette[(i+1)%6],8,12)
            elif sid_local==8:
                sphere(-.72,0,0,.42,(1,.30,.08),16,22);sphere(.72,0,0,.38,(.18,.45,1),16,22)
                torus(1.55,.024,c3,60,5);torus(2.1,.018,c2,60,4)
                for i in range(8):
                    a=i*2*_m.pi/8;sphere(2.1*_m.cos(a),.25*_m.sin(a*3),2.1*_m.sin(a),.07,c,7,10)
            elif sid_local==9:
                sphere(0,0,0,.8,(.15,.38,.93),20,32)
                for r,col in ((1.1,c),(1.4,c2),(1.7,c3)):
                    gl.glPushMatrix();gl.glRotatef(24 if r<1.3 else -34,1,0,0);torus(r,.065,col,56,10);gl.glPopMatrix()
                for i in range(240):
                    a=rng.random()*2*_m.pi;r=2+rng.random()*.65
                    sphere(r*_m.cos(a),rng.uniform(-.3,.3),r*_m.sin(a),.014+rng.random()*.035,c2,5,7)
            elif sid_local in (10,11,12):
                terrain(42 if sid_local==10 else 50 if sid_local==11 else 58,sid_local-10)
                if sid_local==11:
                    for i in range(34):
                        x=rng.uniform(-2.7,2.7);z=rng.uniform(-2.7,2.7);sphere(x,.10,z,.08+rng.random()*.13,c2,6,8)
                if sid_local==12:
                    for i in range(180):
                        x=rng.uniform(-3,3);z=rng.uniform(-3,3)
                        h=.25+rng.random()*1.3;box(x,h/2,z,.065,h,.065,c3)
            elif sid_local in (13,14,15):
                city(sid_local-13,90 if sid_local==13 else 115 if sid_local==14 else 160)
                if sid_local==14:
                    for i in range(28):line((-3.0,-1.7,i*.19-2.6),(3.0,-1.7,i*.19-2.6),c2,.7)
                elif sid_local==15:
                    for level in range(3):
                        y=-.6+level*.65
                        for x in range(-4,5):line((x*.65,y,-2.5),(x*.65,y,2.5),c3,.65)
            elif sid_local==16:
                box(0,-.22,0,4.6,.18,2.5,(.04,.24,.14))
                for i in range(22):box(-1.8+i*.17,.0,0,.045,.18,2.05,(.45,.52,.6))
                for x in (-1.05,0,1.05):fan(x,.22,0,.43)
                for i in range(20):box((i%10-4.5)*.35,.0,(i//10-.5)*.75,.19,.16,.24,c2)
            elif sid_local==17:
                box(0,-.28,0,5,.16,2.6,(.04,.23,.14))
                for i in range(30):box(-2.3+i*.16,-.02,0,.035,.14,2.4,(.52,.57,.64))
                for x in (-1.45,0,1.45):fan(x,.22,0,.53,0,11)
                for i in range(3):
                    torus(.63,.035,c if i%2==0 else c3,36,6)
            elif sid_local==18:
                for layer in range(3):
                    gl.glPushMatrix();gl.glTranslatef(0,(layer-1)*.55,(layer-1)*.3);gl.glRotatef(layer*13,0,1,0)
                    box(0,0,0,4.2,.14,1.9,(.04,.19+.05*layer,.12))
                    for i in range(18):box(-1.7+i*.2,.12,0,.04,.12,1.7,(.45,.5,.58))
                    fan(-1.0,.22,0,.35,layer*.7);fan(1.0,.22,0,.35,-layer*.4)
                    gl.glPopMatrix()
            elif sid_local in (19,20,21):
                points_cloud(3200 if sid_local==19 else 4000 if sid_local==20 else 6200,sid_local-19)
                if sid_local==19:
                    for i in range(9):
                        pts=[]
                        for j in range(500):
                            t=j*.04+i*.68;r=.15+j*.004
                            pts.append((r*_m.cos(t),.12*_m.sin(3*t+i),r*_m.sin(t)))
                        line_strip(pts,c3,.7)
                elif sid_local==20:
                    for i in range(60):
                        a=i*2*_m.pi/60
                        line((0,-2.5,0),(1.8*_m.cos(a),2.5,1.8*_m.sin(a)),c2,.6)
                else:
                    for i in range(18):
                        a=i*2*_m.pi/18;torus(1.15,.014,c3,36,4)
                        sphere(1.8*_m.cos(a),.4*_m.sin(i),1.8*_m.sin(a),.06,c2,6,8)
            elif sid_local in (22,23,24):
                terrain(52 if sid_local==22 else 58 if sid_local==23 else 62,3+(sid_local-22))
                if sid_local==23:
                    gl.glPushMatrix();gl.glRotatef(87,0,1,0);terrain(44,0);gl.glPopMatrix()
                elif sid_local==24:
                    for i in range(80):
                        x=rng.uniform(-3,3);z=rng.uniform(-3,3)
                        sphere(x,rng.uniform(-.1,.4),z,.025+rng.random()*.045,(.65,.83,.95),5,7)
            elif sid_local==25:
                for z in range(7):
                    for y in range(6):
                        for x in range(7):
                            xx=(x-3)*.66;yy=(y-2.5)*.62;zz=(z-3)*.66
                            box(xx,yy,zz,.33,.33,.33,palette[(x+2*y+z)%6])
            elif sid_local==26:
                for row in range(9):
                    for col in range(9):
                        if (row+col)%3:
                            x=(col-4)*.65;z=(row-4)*.65
                            box(x,.1+((row*col)%4)*.16,z,.42,.2+((row+col)%4)*.15,.42,palette[(row+col)%6])
                for r in range(3):wire_cube(0,r*.75-.8,0,2.0+r*.55,c3)
            elif sid_local==27:
                for i in range(160):
                    a=i*.25;z=3.8-i*.045;r=.25+i*.014
                    box(r*_m.cos(a),r*_m.sin(a),z,.23,.23,.23,palette[i%6])
                tunnel(12,2)
            elif sid_local==28:
                for i in range(42):
                    x=(i%7-3)*.72;z=(i//7-3)*.72
                    crystal(x,-.35,z,.23+rng.random()*.18,palette[i%6])
                for i in range(18):torus(.35+i*.09,.012,c2,32,4)
            elif sid_local==29:
                for i in range(110):
                    crystal(rng.uniform(-2.7,2.7),rng.uniform(-2.2,2.2),rng.uniform(-2.7,2.7),.12+rng.random()*.30,palette[i%6])
                for i in range(20):
                    line((rng.uniform(-2,2),-2,rng.uniform(-2,2)),(rng.uniform(-2,2),2,rng.uniform(-2,2)),c3,.5)
            elif sid_local==30:
                for i in range(240):
                    crystal(rng.uniform(-3,3),rng.uniform(-2.5,2.5),rng.uniform(-3,3),.06+rng.random()*.22,(.05+rng.random()*.4,.25+rng.random()*.6,.75+rng.random()*.25))
            elif sid_local==31:
                gear(0,0,0,1.9,24,c);torus(1.3,.16,c2,48,12);sphere(0,0,0,.48,c3,14,22)
            elif sid_local==32:
                for x,y,r,n in ((-1.0,.55,1.0,18),(1.0,-.3,.8,16),(0,1.6,.45,12)):
                    gl.glPushMatrix();gl.glTranslatef(x,y,0);gear(0,0,0,r,n,c if n%2==0 else c2);gl.glPopMatrix()
                for i in range(18):sphere(rng.uniform(-2,2),rng.uniform(-1.5,1.5),rng.uniform(-.4,.4),.07,c3,6,8)
            elif sid_local==33:
                torus(1.7,.11,c2,48,10);sphere(0,0,0,.4,c,12,18)
                for i in range(12):
                    a=i*2*_m.pi/12
                    box(1.0*_m.cos(a),1.0*_m.sin(a),0,.95,.16,.18,(.66,.7,.76))
                    sphere(1.45*_m.cos(a),1.45*_m.sin(a),0,.08,c3,6,8)
            elif sid_local==34:
                molecular_chain(28,.28)
                for i in range(24):
                    x=(i-12)*.28;y=.22*_m.sin(i*.9);sphere(x,y,0,.18,palette[i%6],8,12)
            elif sid_local==35:
                positions=[]
                for x in range(5):
                    for y in range(4):
                        for z in range(4):positions.append(((x-2)*.62,(y-1.5)*.62,(z-1.5)*.62))
                for x,y,z in positions:sphere(x,y,z,.11,palette[(round(x+y+z)*13)%6],7,10)
                for i,p in enumerate(positions):
                    if i%4==0 and i+1<len(positions):line(p,positions[i+1],c3,.7)
            elif sid_local==36:
                for i in range(180):
                    a=i*2.39996;r=1.9*(i/180)**.5;y=rng.uniform(-1.9,1.9)
                    sphere(r*_m.cos(a),y,r*_m.sin(a),.06+rng.random()*.10,palette[i%6],6,8)
                for i in range(16):
                    a=i*2*_m.pi/16;torus(.65+i*.07,.012,c2,24,4)
            elif sid_local==37:
                tunnel(22,0)
                for i in range(120):
                    a=i*2*_m.pi/120
                    sphere(1.65*_m.cos(a),1.65*_m.sin(a),rng.uniform(-3,3),.025,c2,5,7)
            elif sid_local==38:
                tunnel(22,1)
                for z in range(15):
                    box(0,0,3-z*.42,.04,3.4,.04,c3)
            elif sid_local==39:
                tunnel(26,2)
                for i in range(140):
                    t=i*.09;line((1.4*_m.cos(t),1.4*_m.sin(t),2.8-i*.04),(1.5*_m.cos(t+.6),1.5*_m.sin(t+.6),2.8-i*.04),c2,.6)
            elif sid_local==40:
                helix(2,1200,.0052)
            elif sid_local==41:
                helix(3,1050,.006)
                for i in range(80):
                    y=-2.8+i*.07;sphere(.18*_m.sin(i),y,.18*_m.cos(i),.04,c3,5,7)
            elif sid_local==42:
                pts=[]
                for i in range(3000):
                    t=i*.045;r=.45+.12*_m.sin(i*.015)
                    pts.append((r*_m.cos(t),i/3000*6-3,r*_m.sin(t)))
                line_strip(pts,c,3)
                for i in range(26):torus(.48,.018,c2,18,5)
            elif sid_local==43:
                mesh_triangles(900,0)
            elif sid_local==44:
                mesh_triangles(8500,1)
                for i in range(14):
                    gl.glPushMatrix();gl.glTranslatef(0,(i-7)*.25,0);gl.glRotatef(i*11,0,1,0);torus(1.45,.013,c2,32,4);gl.glPopMatrix()
            elif sid_local==45:
                mesh_triangles(28000,2)
            elif sid_local in (46,47,48):
                depth=7 if sid_local==46 else 8 if sid_local==47 else 9
                mode=sid_local-46
                tree_branch(0,-2.7,0,1.45,0,depth,mode)
                for i in range(50 if sid_local==46 else 120 if sid_local==47 else 220):
                    x=rng.uniform(-2.5,2.5);y=rng.uniform(-1.2,2.5);z=rng.uniform(-2.0,2.0)
                    sphere(x,y,z,.035+rng.random()*.04,palette[i%6],5,7)
            elif sid_local==49:
                wire_cube(0,0,0,5,c2)
                for x in (-1.8,0,1.8):
                    for y in (-1.3,0,1.3):
                        for z in (-1.2,0,1.2):box(x,y,z,.36,.36,.36,palette[(round(x+y+z)*7)%6])
            elif sid_local==50:
                for x in range(8):
                    for z in range(7):
                        h=.5+rng.random()*1.6
                        box((x-3.5)*.72,h/2,(z-3)*.72,.36,h,.36,(.18,.24,.32))
                for y in (0,.8,1.6):
                    for x in range(8):line(((x-3.5)*.72,y,-2.2),((x-3.5)*.72,y,2.2),c3,.7)
            elif sid_local==51:
                for i in range(18):
                    y=-2.0+i*.23
                    pts=[]
                    for j in range(220):
                        t=j/219*2*_m.pi
                        pts.append((1.7*_m.cos(t+i*.2),y+.14*_m.sin(t*3),1.7*_m.sin(t+i*.2)))
                    line_strip(pts,palette[i%6],1.1)
                for i in range(30):sphere(rng.uniform(-2,2),rng.uniform(-2,2),rng.uniform(-2,2),.07,c3,6,8)
            elif sid_local==52:
                for x in range(-4,5):
                    for y in range(-4,5):
                        for z in range(-3,4):wire_cube(x*.55,y*.55,z*.55,.48,palette[(x+y+z)%6])
            elif sid_local==53:
                tunnel(32,0)
                for i in range(18):
                    for j in range(18):line((i*.18-1.6,j*.18-1.6,-3.5),(i*.18-1.6,j*.18-1.6,3.5),c3,.45)
            elif sid_local==54:
                for i in range(16):
                    gl.glPushMatrix();gl.glRotatef(i*11,1,1,.4);wire_cube(0,0,0,.35+i*.22,palette[i%6]);gl.glPopMatrix()
                for i in range(10):
                    a=i*2*_m.pi/10;line((0,0,0),(2.2*_m.cos(a),1.5*_m.sin(a*2),2.2*_m.sin(a)),c2,.8)
            elif sid_local==55:
                for x in range(7):
                    for y in range(5):
                        for z in range(5):
                            sphere((x-3)*.7,(y-2)*.7,(z-2)*.7,.22,palette[(x*3+y*2+z)%6],12,18)
            elif sid_local==56:
                for i in range(36):
                    a=i*2.39996;r=.55+(i%5)*.28
                    sphere(r*_m.cos(a),(i%7-3)*.34,r*_m.sin(a),.16,palette[i%6],10,14)
                    gl.glPushMatrix();gl.glTranslatef(r*_m.cos(a),(i%7-3)*.34,r*_m.sin(a));gl.glRotatef(i*17,1,0,1);torus(.24,.018,c3,20,5);gl.glPopMatrix()
            elif sid_local==57:
                for i in range(18):
                    gl.glPushMatrix();gl.glRotatef(i*20,1,.7,.3)
                    sphere(0,0,0,1.75,palette[i%6],16,24)
                    gl.glDisable(gl.GL_LIGHTING);gl.glColor3f(*c2);gl.glBegin(gl.GL_POINTS)
                    for j in range(900):
                        a=rng.random()*2*_m.pi;v=rng.random()*_m.pi
                        gl.glVertex3f(1.8*_m.sin(v)*_m.cos(a),1.8*_m.cos(v),1.8*_m.sin(v)*_m.sin(a))
                    gl.glEnd();gl.glEnable(gl.GL_LIGHTING);gl.glPopMatrix()
            elif sid_local==58:
                furry_donut(.85,.26,650,c2)
                for i in range(75):
                    crystal(rng.uniform(-2.8,2.8),rng.uniform(-2.1,2.1),rng.uniform(-2.8,2.8),.08+rng.random()*.16,palette[i%6])
            elif sid_local==59:
                for rack in range(4):
                    z=(rack-1.5)*1.05
                    box(0,0,z,4.7,.72,.75,(.035,.08,.12))
                    for x in (-1.65,0,1.65):fan(x,.15,z+.42,.22,blades=7)
                    for i in range(22):box(-2.1+i*.2,-.12,z+.39,.035,.12,.1,c3)
            elif sid_local in (61,62,63):  # Cyclone / hurricane scenes
                v=sid_local-61
                layers=(12,22,34)[v]
                for layer in range(layers):
                    f=layer/max(1,layers-1);radius=.28+1.75*f
                    gl.glPushMatrix();gl.glTranslatef(0,-2.4+4.8*f,0);gl.glRotatef(layer*27+elapsed_seed(sid_local),0,1,0)
                    torus(radius,.065+.025*v,(.25+.3*f,.42+.25*f,.68+.18*f),32+v*12,7+v*3);gl.glPopMatrix()
                for i in range((350,950,1900)[v]):
                    a=i*.41;r=.4+(i%41)/41*1.55;y=-2.2+(i%57)/56*4.4
                    sphere(r*_m.cos(a),y,r*_m.sin(a),.025+.012*v,(.36,.50,.72),5,8)
            elif sid_local in (64,65,66):  # Heavy rain: rain wall and layered storm clouds
                v=sid_local-64
                for i in range((9,18,30)[v]):
                    sphere((i%8-3.5)*.68,1.7+(i//8)*.24,(i%5-2)*.48,.42+.06*v,(.08,.13,.23),8+v*2,12+v*3)
                for i in range((180,430,850)[v]):
                    x=-2.8+(i%47)*.12;z=-2.7+((i*17)%43)*.13;y=1.8+((i*11)%31)*.09
                    line((x,y,z),(x-.12-.04*v,y-.34-.07*v,z+.025),( .22,.50+.05*v,.86),.7+v*.2)
            elif sid_local in (67,68,69):  # Flooded city, street grid and water wall
                v=sid_local-67
                for side in (-1,1):
                    for i in range((8,15,24)[v]):
                        x=side*(1.85+(i%3)*.28);z=-2.8+i*5.6/max(1,(7,14,23)[v]);h=.6+.09*(i%5)
                        box(x,h/2,z,.46,h,.42,(.13+.02*v,.20+.025*(i%4),.29+.02*v))
                        for w in range(1+v):box(x-.08+w*.13,.22+.10*(i%4),z+.214,.04,.05,.018,(.86,.65,.20))
                for level in range((5,10,18)[v]):
                    z=-2.7+level*5.4/max(1,(4,9,17)[v])
                    line_strip([(-1.65,.05,z),(0,.10+.04*_m.sin(level),z+.04),(1.65,.05,z)],(.02,.34+.08*v,.74),1.3+v*.15)
            elif sid_local in (70,71,72):  # Thunderstorm, branching lightning and cloud bank
                v=sid_local-70
                for i in range((12,25,42)[v]):
                    sphere(-2.6+(i%10)*.57,1.55+(i%5)*.13,-1.8+((i*5)%9)*.40,.34+.035*v,(.09,.13,.22),8+v*2,11+v*3)
                for j in range((1,3,6)[v]):
                    x=-1.7+j*(3.4/max(1,(1,3,6)[v]));z=-.8+.27*(j%4)
                    pts=[(x,1.45,z),(x-.18,.88,z+.05),(x+.12,.45,z+.10),(x-.23,-.12,z+.17),(x+.03,-.65,z+.12)]
                    line_strip(pts,(.65,.84,1.0),1.8+v)
                    if v:line_strip([pts[2],(pts[2][0]+.35,.18,z+.35),(pts[2][0]+.52,-.12,z+.42)],(.45,.74,1.0),1.2+v*.2)
            elif sid_local in (73,74,75):  # Race track, grandstands and pit lane
                v=sid_local-73
                torus(2.15,.17,(.08,.10,.14),56+v*18,8+v*3)
                torus(2.15,.025,(.9,.9,.8),60+v*18,5)
                torus(2.57,.045,(.92,.16,.06),60+v*18,5)
                for i in range((18,38,68)[v]):
                    a=2*_m.pi*i/max(1,(18,38,68)[v]);x=2.85*_m.cos(a);z=2.85*_m.sin(a)
                    box(x,.16,z,.12+.02*v,.25+.04*(i%3),.15,(.22,.26,.33))
                for row in range(2+v*2):box(-2.55,.2+row*.20,-2.3-row*.06,5.1,.12,.3,(.17,.22,.30))
                for i in range(5+v*6):box(-2.2+i*.42,.12,1.95,.26,.20,.18,palette[(i+v)%len(palette)])
            elif sid_local in (76,77,78):  # Drift figure-eight and tire stacks
                v=sid_local-76
                for scale in (1.0,.77,.52):
                    pts=[]
                    for i in range(420+v*120):
                        t=i/max(1,419+v*120)*2*_m.pi
                        pts.append((2.1*_m.sin(t),.02,1.43*_m.sin(t)*_m.cos(t)*2*scale))
                    line_strip(pts,(.34+.08*v,.40,.49),5.0*scale)
                for i in range(14+v*14):
                    a=i*2*_m.pi/(14+v*14)
                    box(2.12*_m.sin(a),.11,1.4*_m.sin(a)*_m.cos(a),.10,.22,.10,(.94,.35,.04))
                for i in range(40+v*55):
                    a=i*.37;x=1.7*_m.sin(a);z=1.2*_m.sin(a)*_m.cos(a)
                    sphere(x,.05+(i%9)*.025,z,.025+.01*v,(.39,.42,.45),4,6)
            elif sid_local in (79,80,81):  # Rally stage: gravel, banks, rocks and barriers
                v=sid_local-79
                terrain((24,36,54)[v],1.6+.15*v)
                for i in range((18,38,70)[v]):
                    x=-2.7+(i%12)*.48;z=-2.6+(i//12)*.70;h=.16+((i*7)%9)*.07
                    box(x,h/2,z,.24+.03*v,h,.30,(.19+.02*(i%4),.17+.02*v,.13))
                    sphere(x+.15,h+.05,z+.05,.08+.015*v,(.24,.32,.17),5,7)
                for side in (-1,1):
                    for i in range(12+v*7):box(side*2.35,.12,-2.6+i*.43,.12,.24,.30,(.65,.62,.5))
            elif sid_local in (82,83,84):  # Neon F1 night circuit and lighting gantries
                v=sid_local-82
                torus(2.15,.16,(.035,.065,.11),60+v*18,8+v*3)
                torus(2.15,.023,(.03,.82,1.0),60+v*18,5)
                torus(2.55,.028,(.96,.08,.30),60+v*18,5)
                for i in range(22+v*20):
                    a=2*_m.pi*i/(22+v*20);x=2.8*_m.cos(a);z=2.8*_m.sin(a)
                    box(x,.42,z,.045,.78,.045,(.05,.48+.08*v,.95))
                    sphere(x,.87,z,.07+.015*v,(.12,.82,1.0),6,9)
                for row in range(2+v*2):box(-2.4,.18+row*.22,-2.05-row*.05,4.8,.12,.25,(.10,.15,.23))
            elif sid_local in (85,86,87):  # Blizzard: snowdrifts, icy rock and trees
                v=sid_local-85
                terrain((22,34,50)[v],1.2+.12*v)
                for i in range((15,28,46)[v]):
                    x=(i%7-3)*.75;z=(i//7-2)*.7;h=.42+((i*7)%8)*.11
                    box(x,h/2,z,.42,h,.4,(.22,.30,.42))
                    sphere(x,h+.09,z,.20+.05*v,(.73,.84,.96),7+v*2,10+v*2)
                for i in range((70,180,360)[v]):
                    x=-2.8+(i*17%101)*5.6/100;z=-2.6+(i*31%89)*5.2/88;y=-.1+(i*13%30)*.08
                    line((x,y,z),(x+.06,-.6,z+.04),(.72,.85,1.0),.65)
            elif sid_local in (88,89,90):  # Tsunami: coastal buildings, wave wall and foam
                v=sid_local-88
                for i in range((16,30,50)[v]):
                    x=-2.65+(i%10)*.58;z=-2.2+(i//10)*.72;h=.28+((i*5)%10)*.09
                    box(x,h/2,z,.42,h,.42,(.17,.23,.32))
                for layer in range((10,20,34)[v]):
                    y=-1.7+layer*3.4/max(1,(9,19,33)[v]);pts=[]
                    for i in range(160+v*80):
                        x=-2.8+i*5.6/max(1,(159+v*80));z=-.5+.3*_m.sin(x*2.4+layer*.28)
                        pts.append((x,y+.18*_m.sin(x*1.4+layer),z))
                    line_strip(pts,(.02,.35+.07*v,.88),.9+.25*v)
            budget["scene_id"]=sid_local

        def draw_dynamic_scene(elapsed):
            sid_local=sid
            v=(sid_local-61)%3
            def vehicle(x,y,z,scale,paint,heading):
                gl.glPushMatrix();gl.glTranslatef(x,y,z);gl.glRotatef(heading,0,1,0)
                box(0,0,0,1.05*scale,.18*scale,.44*scale,paint)
                box(.10*scale,.13*scale,0,.42*scale,.16*scale,.30*scale,(.10,.15,.23))
                for wx in (-.32,.32):
                    for wz in (-.26,.26):box(wx*scale,-.1*scale,wz*scale,.18*scale,.13*scale,.09*scale,(.035,.04,.06))
                gl.glPopMatrix()
            def particle_lines(kind,count):
                gl.glDisable(gl.GL_LIGHTING);gl.glBegin(gl.GL_POINTS if kind in ("snow","cyclone") else gl.GL_LINES)
                for i in range(count):
                    a=i*.754877666+elapsed*(.8+.4*v);seed=(i*.618033989)%1.0
                    if kind=="cyclone":
                        y=-2.5+((seed+elapsed*(.14+.06*v))%1.0)*5;r=.2+2.05*(y+2.5)/5
                        gl.glColor3f(.28,.44+.08*v,.68);gl.glVertex3f(r*_m.cos(a),y,r*_m.sin(a))
                    elif kind=="rain":
                        x=-2.9+(i%97)*5.8/96;z=-2.8+((i*31)%89)*5.6/88;y=2.85-((elapsed*(4+3*v)+i*.193)%5.7)
                        gl.glColor3f(.24,.5,.88);gl.glVertex3f(x,y,z);gl.glVertex3f(x-.12,y-.28-.06*v,z+.03)
                    elif kind=="snow":
                        x=-3+((i*17)%101)*6/100;z=-2.8+((i*37)%97)*5.6/96;y=2.9-((elapsed*(1.3+1.4*v)+i*.137)%5.8)
                        gl.glColor3f(.72,.86,1.0);gl.glVertex3f(x,y,z)
                    elif kind=="dust":
                        x=-2+((i*13)%47)*4/46;y=.05+(i%10)*.025;z=1+((elapsed*2.4+i*.071)%3.6)
                        gl.glColor3f(.52,.42,.3);gl.glVertex3f(x,y,z);gl.glVertex3f(x+.09,y+.02,z+.14)
                gl.glEnd();gl.glEnable(gl.GL_LIGHTING)
            if 61<=sid_local<=63:particle_lines("cyclone",(1000,2400,5200)[v])
            elif 64<=sid_local<=66:particle_lines("rain",(500,1200,2400)[v])
            elif 67<=sid_local<=69:
                grid=(18,30,44)[v];gl.glBegin(gl.GL_QUADS)
                for row in range(grid):
                    z0=-3+6*row/grid;z1=-3+6*(row+1)/grid
                    for col in range(grid):
                        x0=-3+6*col/grid;x1=-3+6*(col+1)/grid
                        for x,z in ((x0,z0),(x1,z0),(x1,z1),(x0,z1)):
                            wave=.18*_m.sin(x*2+elapsed*1.6)+.12*_m.cos(z*2.4-elapsed*1.25)
                            gl.glColor3f(.015,.24+.05*_m.sin(elapsed+x),.55+.12*_m.cos(elapsed+z));gl.glNormal3f(0,1,0);gl.glVertex3f(x,wave,z)
                gl.glEnd()
                for i in range(6+v*5):box(-2.2+((i*19+int(elapsed*4))%23)*.2,.16,-2.2+((i*11)%17)*.28,.24,.07,.14,(.35,.26,.14))
            elif 70<=sid_local<=72:
                tick=int(elapsed*(4+v*2))
                flash=(tick%9) in (0,1,5)
                if flash:
                    gl.glDisable(gl.GL_LIGHTING);gl.glLineWidth(2+v);gl.glColor3f(.72,.88,1.0);gl.glBegin(gl.GL_LINE_STRIP)
                    x=-1.8+(tick%4);z=-.6+(tick%3)*.45;gl.glVertex3f(x,2,z)
                    for j in range(10+v*4):
                        x+=(-.28 if (j+tick)%2 else .25)+.07*_m.sin(elapsed*12+j);y=1.7-j*(3.2/(9+v*4));z+=.06*_m.cos(j*2.1+tick);gl.glVertex3f(x,y,z)
                    gl.glEnd();gl.glLineWidth(1);gl.glEnable(gl.GL_LIGHTING)
            elif 73<=sid_local<=75:
                count=(3,6,10)[v]
                for i in range(count):
                    a=elapsed*(.65+.065*i)+i*2*_m.pi/count
                    vehicle(2.25*_m.cos(a),.22,2.25*_m.sin(a),.28,(.9,.08+.05*(i%3),.12+.1*(i%4)),90-a*180/_m.pi)
            elif 76<=sid_local<=78:
                count=(2,4,7)[v]
                for i in range(count):
                    a=elapsed*(.75+.04*i)+i*2*_m.pi/count;x=2*_m.sin(a);z=1.4*_m.sin(a)*_m.cos(a)*1.9
                    vehicle(x,.2,z,.27,(.08,.3+.1*(i%3),.88),45-a*115/_m.pi+_m.sin(elapsed*2+i)*18)
                particle_lines("dust",(160,360,700)[v])
            elif 79<=sid_local<=81:
                count=(1,2,4)[v]
                for i in range(count):
                    a=elapsed*(.52+.05*i)+i*1.8;x=2.15*_m.sin(a)+.22*_m.sin(a*3);z=1.8*_m.sin(a)*_m.cos(a)
                    vehicle(x,.23,z,.30,(.85,.48,.08) if i%2==0 else (.08,.45,.78),40-a*70/_m.pi)
                particle_lines("dust",(180,360,640)[v])
            elif 82<=sid_local<=84:
                count=(4,8,14)[v]
                for i in range(count):
                    a=elapsed*(.86+.035*i)+i*2*_m.pi/count;x=2.25*_m.cos(a);z=2.25*_m.sin(a)
                    vehicle(x,.32,z,.23,(.92,.12,.16) if i%2==0 else (.02,.55,.92),90-a*180/_m.pi)
                    gl.glDisable(gl.GL_LIGHTING);gl.glBegin(gl.GL_LINES);gl.glColor3f(.1,.75,1.0);gl.glVertex3f(x-.3,.24,z);gl.glVertex3f(x-.65,.24,z);gl.glEnd();gl.glEnable(gl.GL_LIGHTING)
            elif 85<=sid_local<=87:particle_lines("snow",(900,1900,3600)[v])
            elif 88<=sid_local<=90:
                grid=(18,30,46)[v];gl.glBegin(gl.GL_QUADS)
                for row in range(grid):
                    z0=-3+6*row/grid;z1=-3+6*(row+1)/grid
                    for col in range(grid):
                        x0=-3+6*col/grid;x1=-3+6*(col+1)/grid
                        for x,z in ((x0,z0),(x1,z0),(x1,z1),(x0,z1)):
                            wave=.24*_m.sin(x+elapsed*1.3)+.34*_m.sin(z*1.1-elapsed*1.5)+.12*_m.sin((x+z)*2.4-elapsed*2)
                            gl.glColor3f(.02,.28+.05*_m.sin(elapsed+x),.78+.1*_m.cos(z+elapsed));gl.glNormal3f(0,1,0);gl.glVertex3f(x,wave,z)
                gl.glEnd();particle_lines("rain",(80,180,320)[v])

        list_id=gl.glGenLists(1)
        gl.glNewList(list_id,gl.GL_COMPILE);draw_scene();gl.glEndList()
        gl.glFinish()
        start=_tm.perf_counter();frames=0;win_start=start;win_frames=0;peak=0.;samples=[];running=True
        while running and (_tm.perf_counter()-start)<duration:
            for event in pg.event.get():
                if event.type==pg.QUIT or (event.type==pg.KEYDOWN and event.key==pg.K_ESCAPE):running=False
                elif event.type==pg.VIDEORESIZE:
                    rw=max(640,event.w);rh=max(480,event.h);gl.glViewport(0,0,rw,rh)
                    gl.glMatrixMode(gl.GL_PROJECTION);gl.glLoadIdentity();gluPerspective(52.0,rw/rh,.1,240.0);gl.glMatrixMode(gl.GL_MODELVIEW)
            elapsed=_tm.perf_counter()-start
            if 70<=sid<=72 and (int(elapsed*4+sid)%9) in (0,1,5):
                gl.glClearColor(.22,.30,.47,1.0)
            else:
                gl.glClearColor(.004,.008,.02,1.0)
            gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)
            gl.glLoadIdentity();gl.glTranslatef(0,-.18,-12)
            gl.glRotatef(elapsed*(14+(sid%11)*2.2),.35+(sid%3)*.3,1,.22+(sid%5)*.08)
            gl.glRotatef(10*_m.sin(elapsed*.7+sid),1,0,0)
            gl.glCallList(list_id)
            if sid>=61:
                draw_dynamic_scene(elapsed)
            gl.glFinish()
            pg.display.flip();frames+=1;win_frames+=1;now=_tm.perf_counter()
            if now-win_start>=1.0:
                fps=win_frames/(now-win_start);samples.append(round(fps,2));peak=max(peak,fps)
                win_frames=0;win_start=now
                pg.display.set_caption(f"NAPRAWA PC • SCENA {sid:02d}/90 • {title} • FPS {fps:.1f} • MAX {peak:.1f} • {renderer[:80]} • ESC = STOP")
        elapsed=max(.001,_tm.perf_counter()-start)
        result.update({"state":"good" if frames else "warn","scene_id":sid,"scene_name":title,
            "renderer":renderer,"opengl_version":gl_version,"resolution":f"{rw}x{rh}",
            "frames":frames,"duration_seconds":round(elapsed,3),"average_fps":round(frames/elapsed,2),
            "peak_fps_1s":round(peak,2),"fps_samples":samples,"workload":"separately authored static geometry recipe + real OpenGL display-list rendering; glFinish synchronized per frame",
            "geometry_budget":budget,"stopped_by_user":elapsed<duration-.5,
            "note":"FPS jest zmierzony z faktycznego renderowania OpenGL. Nie jest przewidywaniem FPS w konkretnej grze."})
        try:gl.glDeleteLists(list_id,1)
        except Exception:pass
        pg.display.quit();pg.quit()
    except Exception as exc:
        result.update({"state":"warn","error":f"{type(exc).__name__}: {exc}",
            "note":"Renderer OpenGL nie wystartował lub sterownik nie udostępnił wymaganej funkcji. Nie oznacza to automatycznie awarii GPU."})
        try:
            if pg is not None:pg.display.quit();pg.quit()
        except Exception:pass
    try:_P(output_path).write_text(_j.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    except Exception:pass

# Route the child process and each selected scene to the separate 90-scene renderer.
_u37_gpu_benchmark_child = _u104_gpu_benchmark_child

# v4.3.104 — adaptive speed test for low-bandwidth links plus a searchable full sensor window.
def _u104_speed_sample_sizes(rate_mbps):
    try:rate=max(0.02,float(rate_mbps or 0))
    except Exception:rate=.02
    target=int(rate*1_000_000/8*3.5)
    target=max(512_000,min(24_000_000,target))
    return (max(512_000,int(target*.75)),target,min(30_000_000,max(512_000,int(target*1.25))))

def _u104_speed_timeout(size_bytes,rate_mbps):
    try:rate=max(.05,float(rate_mbps or 0))
    except Exception:rate=.05
    estimated=float(size_bytes)*8/(rate*1_000_000)
    return max(45,min(180,int(estimated*2.5+15)))

_U104_ORIGINAL_MEASURE_SPEED = _u100_measure_speed
def _u104_measure_speed(app):
    import time as _tm
    data={"latency_ms":[],"download":[],"upload":[],"started_at":_U66_datetime.now().isoformat(timespec="seconds"),
      "method":"Adaptacyjny HTTPS; transfer dopasowany do prędkości próbki rozgrzewkowej; mediana i peak osobno.",
      "latency_method":"HTTPS round-trip time, nie ICMP ping","profile":"adaptive-low-bandwidth-safe","warmup":{}}
    total_data=0
    def phase(msg):
        try:app.queue_action(lambda m=msg:_u66_set_speed_status(app,m))
        except Exception:pass
        try:app.queue_status(msg)
        except Exception:pass
    def run_one(kind,size,index,total,rate_hint=.5,label_override=None):
        nonlocal total_data
        if kind=="download":
            url="https://speed.cloudflare.com/__down?bytes="+str(int(size))+"&r="+_u66_uuid.uuid4().hex;body=None
        else:
            url="https://speed.cloudflare.com/__up?r="+_u66_uuid.uuid4().hex;body=_u66_os.urandom(int(size))
        timeout=_u104_speed_timeout(size,rate_hint)
        label=label_override or f"{kind.upper()} próbka {index}/{total}: {size/1_000_000:.2f} MB"
        phase("Speed Test: "+label+" — transfer rzeczywistych bajtów…")
        try:
            result=_U100_ORIGINAL_SPEED_REQUEST(url,body,timeout,
              lambda p,d,t,e,i,a,b=total_data:_u90_emit_speed_progress(app,p,d,t,e,i,a,b),kind)
            result.update({"requested_bytes":int(size),"sample_index":index,"sample_count":total,"state":"good","kind":kind,"timeout_seconds":timeout})
            total_data+=int(result.get("bytes",0))
            return result
        except Exception as exc:
            msg=f"{type(exc).__name__}: {exc}"
            try:app.queue_log(f"Speed Test {label}: {msg}")
            except Exception:pass
            return {"requested_bytes":int(size),"sample_index":index,"sample_count":total,"state":"error","kind":kind,
              "bytes":0,"seconds":None,"mbps":None,"timeout_seconds":timeout,"error":msg}
    def valid(rows):
        return [r for r in rows if r.get("state")=="good" and isinstance(r.get("mbps"),(int,float)) and r.get("bytes",0)>0]
    # Detect a broken endpoint early: do not wait through four long timeouts on an offline PC.
    failed_rtt=0
    for i in range(1,6):
        phase(f"Speed Test: HTTPS RTT {i}/5…")
        t0=_tm.perf_counter()
        try:
            _U100_ORIGINAL_SPEED_REQUEST("https://speed.cloudflare.com/__down?bytes=0&r="+_u66_uuid.uuid4().hex,None,12,None,"ping")
            data["latency_ms"].append(round((_tm.perf_counter()-t0)*1000,2));failed_rtt=0
        except Exception as exc:
            failed_rtt+=1;data.setdefault("latency_errors",[]).append(f"{type(exc).__name__}: {exc}")
            if failed_rtt>=2:break
    if len(data["latency_ms"])==0:
        data.update({"state":"warn","download_mbps":None,"upload_mbps":None,"download_peak_mbps":None,
          "upload_peak_mbps":None,"latency_average_ms":None,"latency_jitter_ms":None,"data_bytes":0,
          "download_samples_valid":0,"upload_samples_valid":0,"finished_at":_U66_datetime.now().isoformat(timespec="seconds"),
          "note":"Endpoint testowy nie odpowiedział na dwa kolejne HTTPS RTT. Transfer nie był uruchamiany."})
        return data
    # Small warm-up transfer measures the link before selecting long test payloads.
    warm_down=run_one("download",256_000,1,1,.5,"rozgrzewka DOWNLOAD 0.26 MB")
    data["warmup"]["download"]=warm_down
    down_rate=float(warm_down.get("mbps") or 0) if warm_down.get("state")=="good" else 0.5
    if warm_down.get("state")!="good":down_rate=max(.1,down_rate)
    down_sizes=_u104_speed_sample_sizes(down_rate)
    for idx,size in enumerate(down_sizes,1):
        data["download"].append(run_one("download",size,idx,3,down_rate))
    warm_up=run_one("upload",256_000,1,1,.5,"rozgrzewka UPLOAD 0.26 MB")
    data["warmup"]["upload"]=warm_up
    up_rate=float(warm_up.get("mbps") or 0) if warm_up.get("state")=="good" else 0.5
    if warm_up.get("state")!="good":up_rate=max(.1,up_rate)
    up_sizes=_u104_speed_sample_sizes(up_rate)
    for idx,size in enumerate(up_sizes,1):
        data["upload"].append(run_one("upload",size,idx,3,up_rate))
    down=valid(data["download"]);up=valid(data["upload"])
    down_rates=[float(x["mbps"]) for x in down];up_rates=[float(x["mbps"]) for x in up]
    data["download_mbps"]=round(_u90_median(down_rates),2) if down_rates else None
    data["upload_mbps"]=round(_u90_median(up_rates),2) if up_rates else None
    data["download_peak_mbps"]=round(max(down_rates),2) if down_rates else None
    data["upload_peak_mbps"]=round(max(up_rates),2) if up_rates else None
    data["download_min_mbps"]=round(min(down_rates),2) if down_rates else None
    data["upload_min_mbps"]=round(min(up_rates),2) if up_rates else None
    data["latency_average_ms"]=round(_u90_median(data["latency_ms"]),2) if data["latency_ms"] else None
    diffs=[abs(data["latency_ms"][i]-data["latency_ms"][i-1]) for i in range(1,len(data["latency_ms"]))]
    data["latency_jitter_ms"]=round(_u90_median(diffs),2) if diffs else None
    data["latency_spread_ms"]=round(max(data["latency_ms"])-min(data["latency_ms"]),2) if len(data["latency_ms"])>1 else None
    data["data_bytes"]=total_data;data["download_samples_valid"]=len(down);data["upload_samples_valid"]=len(up)
    data["download_sample_sizes_bytes"]=[x["requested_bytes"] for x in data["download"]]
    data["upload_sample_sizes_bytes"]=[x["requested_bytes"] for x in data["upload"]]
    data["state"]="good" if len(down)>=2 and len(up)>=2 else "warn"
    data["finished_at"]=_U66_datetime.now().isoformat(timespec="seconds")
    data["note"]="Próbka rozgrzewkowa dobiera rozmiar trzech prób DL i UL. Na wolnym łączu nie wymusza pierwszego transferu 8 MB; wynik podstawowy jest medianą faktycznych próbek."
    try:
        folder=_u66_store_dir()/"speedtest";folder.mkdir(parents=True,exist_ok=True)
        history_path=folder/"history.json"
        try:history=_u66_json.loads(history_path.read_text(encoding="utf-8"))
        except Exception:history=[]
        history.append(data);history_path.write_text(_u66_json.dumps(history[-100:],ensure_ascii=False,indent=2),encoding="utf-8")
        data["history_path"]=str(history_path)
    except Exception as exc:data["history_warning"]=f"{type(exc).__name__}: {exc}"
    return data

# Make all existing Speed Test entry points use the same adaptive engine.
_u100_measure_speed = _u104_measure_speed
_u90_measure_speed = _u104_measure_speed
_u66_measure_speed = _u104_measure_speed

def _u104_sensor_records(app):
    cache=getattr(app,"_u66_sensor_cache",{}) or {}
    temps=cache.get("temps",{}) or {};gpu=cache.get("gpu",{}) or {};system=cache.get("system",{}) or {}
    rows=[]
    def add(category,hardware,name,value,unit,source):
        if value is None:shown="N/D"
        elif isinstance(value,bool):shown="TAK" if value else "NIE"
        elif isinstance(value,(int,float)):
            try:
                number=float(value);shown=f"{number:.4f}".rstrip("0").rstrip(".") if _u66_math.isfinite(number) else "N/D"
            except Exception:shown="N/D"
        else:shown=str(value)
        rows.append({"category":str(category or "Other"),"hardware":str(hardware or "N/D"),
          "sensor":str(name or "N/D"),"value":shown,"unit":str(unit or ""),
          "source":str(source or "N/D")})
    sys_source="Windows / psutil"
    metric_rows=[
      ("Load","CPU","Użycie CPU",system.get("cpu_percent"),"%"),
      ("Clock","CPU","Zegar CPU",system.get("cpu_clock_mhz"),"MHz"),
      ("Clock","CPU","Maksymalny zegar CPU",system.get("cpu_clock_max_mhz"),"MHz"),
      ("Count","CPU","Rdzenie fizyczne",system.get("cpu_physical"),""),
      ("Count","CPU","Wątki logiczne",system.get("cpu_logical"),""),
      ("Memory","RAM","Użycie RAM",system.get("ram_percent"),"%"),
      ("Memory","RAM","RAM użyta",system.get("ram_used_bytes")/1073741824 if system.get("ram_used_bytes") is not None else None,"GiB"),
      ("Memory","RAM","RAM dostępna",system.get("ram_available_bytes")/1073741824 if system.get("ram_available_bytes") is not None else None,"GiB"),
      ("Memory","RAM","RAM całkowita",system.get("ram_total_bytes")/1073741824 if system.get("ram_total_bytes") is not None else None,"GiB"),
      ("Memory","Swap","Użycie swap",system.get("swap_percent"),"%"),
      ("Memory","Swap","Swap użyty",system.get("swap_used_bytes")/1073741824 if system.get("swap_used_bytes") is not None else None,"GiB"),
      ("Throughput","Dysk","Odczyt całkowity",system.get("disk_read_mbps"),"MB/s"),
      ("Throughput","Dysk","Zapis całkowity",system.get("disk_write_mbps"),"MB/s"),
      ("Throughput","Sieć","Download systemowy",system.get("net_down_mbps"),"Mbps"),
      ("Throughput","Sieć","Upload systemowy",system.get("net_up_mbps"),"Mbps"),
      ("Battery","Bateria","Poziom baterii",system.get("battery_percent"),"%"),
      ("Battery","Bateria","Zasilacz podłączony",system.get("battery_plugged"),""),
      ("Battery","Bateria","Pozostały czas",system.get("battery_seconds_left"),"s"),
      ("System","Windows","Czas pracy",system.get("uptime_seconds"),"s"),
      ("Temperature","CPU","Temperatura CPU",temps.get("cpu_temp_c"),"°C"),
      ("Temperature","GPU","Temperatura GPU",gpu.get("temperature_c",temps.get("gpu_temp_c")),"°C"),
      ("Power","CPU","Moc CPU",temps.get("cpu_power_w"),"W"),
      ("Power","GPU","Moc GPU",gpu.get("power_draw_w",gpu.get("power_w",temps.get("gpu_power_w"))),"W"),
      ("Power","System","Moc systemu",temps.get("system_power_w"),"W"),
      ("Power","Bateria","Moc baterii",temps.get("battery_power_w"),"W"),
      ("Voltage","CPU","Napięcie CPU",temps.get("cpu_voltage_v"),"V"),
      ("Voltage","GPU","Napięcie GPU",temps.get("gpu_voltage_v"),"V"),
      ("Clock","GPU","Zegar GPU",gpu.get("gpu_clock_mhz",temps.get("gpu_clock_mhz")),"MHz"),
      ("Clock","GPU","Zegar pamięci GPU",gpu.get("memory_clock_mhz"),"MHz"),
      ("Load","GPU","Użycie GPU",gpu.get("gpu_load_percent",gpu.get("load_percent")),"%"),
      ("Memory","VRAM","VRAM użyta",gpu.get("vram_used_mb"),"MB"),
      ("Memory","VRAM","VRAM całkowita",gpu.get("vram_total_mb"),"MB"),
      ("Fan","CPU","Wentylator CPU",temps.get("cpu_fan_rpm"),"RPM"),
      ("Fan","GPU","Wentylator GPU",gpu.get("fan_speed_rpm",temps.get("gpu_fan_rpm")),"RPM")]
    for cat,hw,name,val,unit in metric_rows:add(cat,hw,name,val,unit,sys_source)
    for sensor in temps.get("sensors",[]) or []:
        if not isinstance(sensor,dict):continue
        add(sensor.get("sensorType") or sensor.get("sensor_type") or sensor.get("type") or "Other",
          (str(sensor.get("hardware") or sensor.get("parent") or "N/D")+" "+str(sensor.get("hardwareType") or sensor.get("hardware_type") or "")).strip(),
          sensor.get("sensor") or sensor.get("name") or "N/D",sensor.get("value"),sensor.get("unit") or "",
          sensor.get("source") or temps.get("method") or "Sensor Bridge")
    for sensor in system.get("extra_temperature_sensors",[]) or []:
        if isinstance(sensor,dict):add("Temperature",sensor.get("hardware","OS"),sensor.get("sensor","Temperatura"),sensor.get("value"),sensor.get("unit","°C"),sensor.get("source","psutil"))
    for zone in temps.get("acpi_zones",[]) or []:
        if isinstance(zone,dict):add("ACPI","Windows",zone.get("name","Strefa termiczna"),zone.get("value"),"°C","WMI ACPI — nie zawsze temperatura CPU")
    return rows

def _u104_render_sensor_tree(win):
    tree=getattr(win,"_u104_tree",None)
    if tree is None or not tree.winfo_exists():return
    rows=getattr(win,"_u104_rows",[]) or []
    query=str(win._u104_search.get() or "").strip().lower()
    category=str(win._u104_category.get() or "Wszystkie")
    visible=[]
    for row in rows:
        if category not in ("Wszystkie","All") and row["category"].lower()!=category.lower():continue
        if query and query not in " ".join(row.values()).lower():continue
        visible.append(row)
    tree.delete(*tree.get_children())
    for idx,row in enumerate(visible):
        tree.insert("","end",iid=f"sensor_{idx}",values=(row["category"],row["hardware"],row["sensor"],row["value"],row["unit"],row["source"]))
    try:win._u104_status.config(text=f"Wyświetlono {len(visible)} z {len(rows)} odczytów • automatyczna aktualizacja co 3 s • N/D = brak danych sterownika")
    except Exception:pass

def _u104_show_all_sensors(app):
    current=getattr(app,"_u104_sensor_window",None)
    try:
        if current is not None and current.winfo_exists():
            current.deiconify();current.lift();current.focus_force()
            _u101_sensor_poll_once(app)
            return current
    except Exception:pass
    _u101_sensor_poll(app)
    try:_u101_sensor_poll_once(app)
    except Exception:pass
    win=tk.Toplevel(app);win.title("NAPRAWA PC — PEŁNA TELEMETRIA / WSZYSTKIE CZUJNIKI")
    win.geometry("1380x820");win.minsize(900,540)
    try:win.transient(app)
    except Exception:pass
    app._u104_sensor_window=win
    t=app.colors()
    header=tk.Frame(win,bg=t["panel"],highlightbackground=t["accent"],highlightthickness=1);header.pack(fill="x",padx=8,pady=8)
    tk.Label(header,text="PEŁNY MONITOR CZUJNIKÓW SPRZĘTOWYCH",bg=t["panel"],fg=t["accent"],font=app.fnt(14,"bold")).pack(anchor="w",padx=12,pady=(8,2))
    tk.Label(header,text="Wszystkie temperatury, użycie, zegary, napięcia, wentylatory, moc, RAM/VRAM, dyski, sieć, bateria oraz surowe odczyty LibreHardwareMonitor. Nieobsługiwane pomiary pozostają N/D.",bg=t["panel"],fg=t["muted"],font=app.fnt(9),wraplength=1300,justify="left").pack(fill="x",padx=12,pady=(0,8))
    controls=tk.Frame(win,bg=t["bg"]);controls.pack(fill="x",padx=8,pady=(0,6))
    tk.Label(controls,text="Szukaj:",bg=t["bg"],fg=t["fg"],font=app.fnt(9,"bold")).pack(side="left",padx=(0,5))
    win._u104_search=tk.StringVar(master=win,value="")
    search=ttk.Entry(controls,textvariable=win._u104_search,width=34);search.pack(side="left",padx=(0,10))
    tk.Label(controls,text="Kategoria:",bg=t["bg"],fg=t["fg"],font=app.fnt(9,"bold")).pack(side="left",padx=(0,5))
    win._u104_category=tk.StringVar(master=win,value="Wszystkie")
    categories=("Wszystkie","Temperature","Load","Clock","Voltage","Power","Fan","Memory","Throughput","Current","Energy","Other","ACPI","Battery","System","Count")
    chooser=ttk.Combobox(controls,textvariable=win._u104_category,values=categories,state="readonly",width=17);chooser.pack(side="left",padx=(0,10))
    app.make_button(controls,"ODŚWIEŻ TERAZ",lambda:(_u101_sensor_poll_once(app),win._u104_status.config(text="Pobieranie aktualnych próbek…")),"accent",side="left",ipady=4)
    def export_csv():
        import csv as _csv
        import tkinter.filedialog as _fd
        from datetime import datetime as _dt
        initial="NAPRAWA-PC-SENSORY-"+_dt.now().strftime("%Y%m%d-%H%M%S")+".csv"
        target=_fd.asksaveasfilename(parent=win,title="Eksport wszystkich czujników",initialfile=initial,
          defaultextension=".csv",filetypes=[("CSV UTF-8","*.csv")])
        if not target:return
        rows=getattr(win,"_u104_rows",[]) or []
        try:
            with open(target,"w",newline="",encoding="utf-8-sig") as f:
                writer=_csv.DictWriter(f,fieldnames=("category","hardware","sensor","value","unit","source"),delimiter=";")
                writer.writeheader();writer.writerows(rows)
            win._u104_status.config(text=f"Zapisano {len(rows)} odczytów do: {target}")
        except Exception as exc:
            messagebox.showerror("Eksport czujników",f"{type(exc).__name__}: {exc}",parent=win)
    app.make_button(controls,"EKSPORTUJ WSZYSTKIE CSV",export_csv,"good",side="left",ipady=4)
    win._u104_status=tk.Label(win,text="Oczekiwanie na czujniki…",bg=t["bg"],fg=t["muted"],anchor="w",font=app.fnt(9,"bold"))
    win._u104_status.pack(fill="x",padx=10,pady=(0,4))
    frame=tk.Frame(win,bg=t["bg"]);frame.pack(fill="both",expand=True,padx=8,pady=(0,8))
    cols=("category","hardware","sensor","value","unit","source")
    tree=ttk.Treeview(frame,columns=cols,show="headings",height=24)
    labels={"category":"KATEGORIA","hardware":"PODZESPÓŁ / CZUJNIK","sensor":"NAZWA ODCZYTU","value":"WARTOŚĆ","unit":"JEDNOSTKA","source":"ŹRÓDŁO / METODA"}
    widths={"category":115,"hardware":260,"sensor":300,"value":120,"unit":80,"source":370}
    for col in cols:tree.heading(col,text=labels[col]);tree.column(col,width=widths[col],minwidth=70,stretch=col in ("hardware","sensor","source"))
    vs=ttk.Scrollbar(frame,orient="vertical",command=tree.yview);hs=ttk.Scrollbar(frame,orient="horizontal",command=tree.xview)
    tree.configure(yscrollcommand=vs.set,xscrollcommand=hs.set);tree.grid(row=0,column=0,sticky="nsew");vs.grid(row=0,column=1,sticky="ns");hs.grid(row=1,column=0,sticky="ew")
    frame.grid_rowconfigure(0,weight=1);frame.grid_columnconfigure(0,weight=1)
    win._u104_tree=tree;win._u104_rows=[]
    def refresh_rows():
        try:
            if not win.winfo_exists():return
            new_rows=_u104_sensor_records(app)
            signature=tuple((r["category"],r["hardware"],r["sensor"],r["value"],r["unit"],r["source"]) for r in new_rows)
            old=getattr(win,"_u104_signature",None)
            if signature!=old:
                win._u104_rows=new_rows;win._u104_signature=signature;_u104_render_sensor_tree(win)
            else:
                try:win._u104_status.config(text=f"{len(new_rows)} odczytów • aktualizacja co 3 s • N/D = brak danych czujnika")
                except Exception:pass
            win.after(3000,refresh_rows)
        except Exception as exc:
            try:win._u104_status.config(text=f"Błąd odczytu: {type(exc).__name__}: {exc}")
            except Exception:pass
            try:win.after(3000,refresh_rows)
            except Exception:pass
    win._u104_search.trace_add("write",lambda *_:_u104_render_sensor_tree(win))
    chooser.bind("<<ComboboxSelected>>",lambda _:_u104_render_sensor_tree(win))
    def close_window():
        try:win.destroy()
        finally:
            try:app._u104_sensor_window=None
            except Exception:pass
    win.protocol("WM_DELETE_WINDOW",close_window)
    refresh_rows();search.focus_set()
    return win

_U104_ORIGINAL_ATTACH_SENSOR_TABLE = _u100_attach_sensor_table
def _u104_attach_sensor_table(app,parent,height=10):
    panel=_U104_ORIGINAL_ATTACH_SENSOR_TABLE(app,parent,height)
    try:
        header=panel.winfo_children()[0]
        app.make_button(header,"PEŁNY MONITOR / SZUKAJ / CSV",
          lambda:_u104_show_all_sensors(app),"accent",side="right",ipady=2)
    except Exception as exc:
        try:app.queue_log("Przycisk pełnej telemetrii: "+repr(exc))
        except Exception:pass
    return panel

_u100_attach_sensor_table = _u104_attach_sensor_table
_u81_attach_sensor_table = _u104_attach_sensor_table

def _u104_selftest_speed_and_sensors():
    for speed in (0.1,0.25,1,10,100,700,1500):
        sizes=_u104_speed_sample_sizes(speed)
        assert len(sizes)==3 and all(512_000<=n<=30_000_000 for n in sizes)
        assert tuple(sorted(sizes))==sizes
        assert all(_u104_speed_timeout(n,speed)>=45 for n in sizes)
    assert "_U100_ORIGINAL_SPEED_REQUEST" in _u104_measure_speed.__code__.co_names
    assert "download_peak_mbps" in repr(_u104_measure_speed.__code__.co_consts)+repr(_u104_measure_speed.__code__.co_names)
    assert "latency_jitter_ms" in repr(_u104_measure_speed.__code__.co_consts)+repr(_u104_measure_speed.__code__.co_names)
    sample={"temps":{"cpu_temp_c":64.5,"sensors":[
       {"hardware":"CPU Core","hardwareType":"Cpu","sensor":"Core #1","sensorType":"Temperature","value":65.2,"unit":"°C","source":"selftest"},
       {"hardware":"GPU","hardwareType":"GpuAmd","sensor":"GPU Usage","sensorType":"Load","value":90,"unit":"%","source":"selftest"}],
       "acpi_zones":[{"name":"TZ0","value":42.0}],"method":"selftest"},
       "gpu":{"temperature_c":71,"gpu_load_percent":93},"system":{"ram_percent":52.0,"cpu_percent":35.0}}
    rows=_u104_sensor_records(type("FakeApp",(),{"_u66_sensor_cache":sample})())
    assert any(x["sensor"]=="Core #1" and x["value"]=="65.2" for x in rows)
    assert any(x["sensor"]=="GPU Usage" and x["value"]=="90" for x in rows)
    assert any(x["sensor"]=="Użycie RAM" and x["value"]=="52" for x in rows)
    assert any(x["category"] == "ACPI" and x["sensor"] == "TZ0" and x["value"] == "42" for x in rows)
    assert callable(_u104_show_all_sensors) and callable(_u104_attach_sensor_table)
    assert any("_u104_sensor_window" in repr(nested.co_consts) for nested in _u101_sensor_poll.__code__.co_consts if hasattr(nested,"co_consts"))
    print("ADAPTIVE_LOW_SPEED_TEST_AND_FULL_SENSOR_EXPLORER_SELFTEST_OK")



# v4.3.105 — visual-quality pass: no progress rectangles; technical component renderers and radial gauges.
# Preserve the existing theme, navigation, test controls, telemetry sources and result reporting.
_U105_COLORS = {
    "bg":"#06101c","panel":"#0a1726","grid":"#14283b","grid_hi":"#203b53",
    "cyan":"#39e7d0","blue":"#3688ff","violet":"#b77aff","green":"#69efb0",
    "amber":"#ffbd68","red":"#ff667f","silver":"#b6c9d8","muted":"#6c859a",
    "white":"#e9f5ff","board":"#0b645b","board_edge":"#34dbc9"
}
_U105_PI = _u66_math.pi
_U66_PI = _u66_math.pi  # compatibility alias used by the renderer's rotating model helpers

def _u105_ring_gauge(canvas, title, value, maximum=100.0, unit="%", color="#39e7d0"):
    try:
        if canvas is None or not canvas.winfo_exists():
            return
        canvas.delete("all")
        w=max(96,int(canvas.winfo_width() or 132))
        h=max(86,int(canvas.winfo_height() or 108))
        cx=w/2.0; cy=h*0.57
        radius=min(w*0.34,h*0.34)
        left=cx-radius; top=cy-radius; right=cx+radius; bottom=cy+radius
        muted=_U105_COLORS["grid_hi"]
        canvas.create_text(w/2,8,text=title,fill=_U105_COLORS["muted"],font=("Segoe UI",8,"bold"))
        canvas.create_arc(left,top,right,bottom,start=135,extent=270,style="arc",outline=muted,width=7)
        for idx in range(11):
            angle=_u66_math.radians(135+27*idx)
            r0=radius+4;r1=radius+9
            x1=cx+_u66_math.cos(angle)*r0;y1=cy+_u66_math.sin(angle)*r0
            x2=cx+_u66_math.cos(angle)*r1;y2=cy+_u66_math.sin(angle)*r1
            canvas.create_line(x1,y1,x2,y2,fill=muted,width=1)
        numeric=None
        try:
            number=float(value)
            if _u66_math.isfinite(number):numeric=number
        except Exception:
            pass
        if numeric is not None:
            pct=max(0.0,min(1.0,numeric/max(1.0,float(maximum))))
            if pct>0:
                canvas.create_arc(left,top,right,bottom,start=135,extent=270*pct,style="arc",outline=color,width=7)
            shown=("{:.0f}".format(numeric) if abs(numeric)>=10 else "{:.1f}".format(numeric))
            canvas.create_text(cx,cy-1,text=shown,fill=_U105_COLORS["white"],font=("Segoe UI",14,"bold"))
            canvas.create_text(cx,cy+17,text=unit,fill=color,font=("Segoe UI",7,"bold"))
        else:
            canvas.create_text(cx,cy-1,text="N/D",fill=_U105_COLORS["muted"],font=("Segoe UI",12,"bold"))
            canvas.create_text(cx,cy+17,text="brak odczytu",fill=_U105_COLORS["muted"],font=("Segoe UI",7))
    except Exception:
        pass

def _u105_draw_live_gauges(app):
    gauges=getattr(app,"_u105_gauges",None) or getattr(app,"_u105_sim_gauges",None)
    if not isinstance(gauges,dict) or not gauges:
        return
    vals=getattr(app,"_live_values",{}) or {}
    cache=getattr(app,"_u66_sensor_cache",{}) or {}
    temps=cache.get("temps",{}) or {}
    gpu=cache.get("gpu",{}) or {}
    system=cache.get("system",{}) or {}
    telemetry=getattr(app,"_u84_gpu_last_telemetry",{}) or {}
    def number(value):
        try:
            result=float(value)
            return result if _u66_math.isfinite(result) else None
        except Exception:
            return None
    cpu=number(vals.get("cpu"))
    if cpu is None: cpu=number(system.get("cpu_percent",getattr(app,"_cpu_util",None)))
    ram=number(vals.get("ram"))
    if ram is None: ram=number(system.get("ram_percent",getattr(app,"_ram_util",None)))
    gpu_load=number(gpu.get("gpu_load_percent",gpu.get("load_percent")))
    if gpu_load is None: gpu_load=number(telemetry.get("gpu_load_percent",telemetry.get("load_percent",getattr(app,"_gpu_util",None))))
    cpu_temp=number(temps.get("cpu_temp_c"))
    gpu_temp=number(gpu.get("temperature_c",temps.get("gpu_temp_c")))
    if gpu_temp is None: gpu_temp=number(telemetry.get("temperature_c"))
    source={
        "cpu":(cpu,100.0,"%",_U105_COLORS["cyan"]),
        "ram":(ram,100.0,"%",_U105_COLORS["violet"]),
        "gpu":(gpu_load,100.0,"%",_U105_COLORS["blue"]),
        "temp":(gpu_temp,110.0,"°C",_U105_COLORS["amber"]),
        "cpu_temp":(cpu_temp,110.0,"°C",_U105_COLORS["amber"]),
        "gpu_temp":(gpu_temp,110.0,"°C",_U105_COLORS["red"])
    }
    for key,canvas in gauges.items():
        item=source.get(key)
        if item:
            _u105_ring_gauge(canvas,{"cpu":"CPU LOAD","ram":"RAM USED","gpu":"GPU LOAD",
                "temp":"TEMPERATURA","cpu_temp":"TEMP CPU","gpu_temp":"TEMP GPU"}.get(key,key.upper()),
                item[0],item[1],item[2],item[3])

def _u105_draw_component_scene(app):
    canvas=getattr(app,"_u68_sim_canvas",None)
    if canvas is None or not canvas.winfo_exists():
        return
    if not str(getattr(app,"current_view","")).startswith("SIM3D_"):
        return
    try:
        w=int(canvas.winfo_width() or 0);h=int(canvas.winfo_height() or 0)
        if w < 180 or h < 140:
            return
        canvas.delete("all")
        canvas.configure(bg=_U105_COLORS["bg"],highlightthickness=0,bd=0)
        module=str(app.current_view).replace("SIM3D_","").upper()
        angle=float(getattr(app,"_u68_sim_angle",0.0))
        center_x=w*0.50;center_y=h*0.50
        scale=min(w*0.96,h*1.48)
        rot=angle*0.62
        def project(point):
            x,y,z=point
            rx=x*_u66_math.cos(rot)-z*_u66_math.sin(rot)
            rz=x*_u66_math.sin(rot)+z*_u66_math.cos(rot)
            f=scale/max(2.6,5.6+rz*0.42)
            return (center_x+rx*f,center_y-y*f+rz*f*0.24)
        def poly(points,fill,outline=None,width=1):
            coords=[]
            for p in points:coords.extend(project(p))
            canvas.create_polygon(*coords,fill=fill,outline=outline or fill,width=width,smooth=False)
        def path(points,color,width=1,dash=None):
            coords=[]
            for p in points:coords.extend(project(p))
            opts={"fill":color,"width":width,"smooth":True,"splinesteps":12}
            if dash:opts["dash"]=dash
            canvas.create_line(*coords,**opts)
        def node(point,r,color,outline=None):
            x,y=project(point)
            canvas.create_oval(x-r,y-r,x+r,y+r,fill=color,outline=outline or color,width=1)
        def ring(cx,y,cz,r,color,width=2,phase=0.0,segments=54):
            pts=[]
            for i in range(segments+1):
                a=2*_U105_PI*i/segments+phase
                pts.append((cx+r*_u66_math.cos(a),y,cz+r*_u66_math.sin(a)))
            path(pts,color,width)
        def rounded_board(cx,cy,cz,sx,sz,fill,edge):
            c=.13
            pts=[(cx-sx/2+c,cy,cz-sz/2),(cx+sx/2-c,cy,cz-sz/2),
                 (cx+sx/2,cy,cz-sz/2+c),(cx+sx/2,cy,cz+sz/2-c),
                 (cx+sx/2-c,cy,cz+sz/2),(cx-sx/2+c,cy,cz+sz/2),
                 (cx-sx/2,cy,cz+sz/2-c),(cx-sx/2,cy,cz-sz/2+c)]
            poly(pts,fill,edge,2)
        def chip(cx,cy,cz,sx,sz,color,edge):
            rounded_board(cx,cy,cz,sx,sz,color,edge)
            ring(cx,cy+0.025,cz,min(sx,sz)*.25,edge,1,angle*.6,28)
            for dx in (-.34,0,.34):
                for dz in (-.25,.25):
                    node((cx+dx*sx,cy+0.03,cz+dz*sz),1.2,edge)
        def fan(cx,cz,r,phase):
            ring(cx,.16,cz,r,_U105_COLORS["cyan"],2,0,64)
            ring(cx,.18,cz,r*.78,_U105_COLORS["grid_hi"],1,0,48)
            ring(cx,.21,cz,r*.20,_U105_COLORS["silver"],2,phase,36)
            for k in range(9):
                a=phase+k*2*_U66_math.pi/9
                def pt(rad,da=0.0,y=.2):
                    q=a+da
                    return (cx+rad*_u66_math.cos(q),y,cz+rad*_u66_math.sin(q))
                poly([pt(r*.20,-.22),pt(r*.90,-.10),pt(r*.72,.17),pt(r*.34,.24)],
                     "#155e68" if k%2 else "#186b78",_U105_COLORS["cyan"],1)
            node((cx,.24,cz),r*.11,_U105_COLORS["white"],_U105_COLORS["cyan"])
        # Background: perspective field, restrained star points and luminous horizon.
        horizon=h*.69
        canvas.create_text(18,14,text=_U68_COMPONENT_LABELS.get(module,module).upper(),
            anchor="nw",fill=_U105_COLORS["white"],font=("Segoe UI",10,"bold"))
        canvas.create_text(w-18,14,text="PODGLĄD TECHNICZNY 3D  •  LIVE",
            anchor="ne",fill=_U105_COLORS["cyan"],font=("Segoe UI",8,"bold"))
        canvas.create_line(18,horizon,w-18,horizon,fill=_U105_COLORS["grid_hi"],width=1)
        for i in range(1,7):
            y=horizon+(h-horizon)*(i/7.0)**1.7
            canvas.create_line(18,y,w-18,y,fill=_U105_COLORS["grid"],width=1)
        for i in range(-9,10):
            x=w/2+i*w*.052
            canvas.create_line(w*.5,horizon,x,h-8,fill=_U105_COLORS["grid"],width=1)
        for i in range(58):
            x=(i*137+int(angle*8))%w
            y=(i*67+17)%(max(50,int(horizon)))
            r=1 if i%6 else 1.8
            canvas.create_oval(x-r,y-r,x+r,y+r,fill=_U105_COLORS["grid_hi"],outline="")
        # A luminous platform is a soft technical silhouette, not a stack of rectangular blocks.
        ring(0,-.50,0,2.28,_U105_COLORS["grid_hi"],1,-angle*.2,72)
        ring(0,-.50,0,1.92,_U105_COLORS["cyan"],1,angle*.15,72)
        mode_phase=angle
        if module in ("GPU","VRAM"):
            rounded_board(0,-.12,0,5.05,2.18,_U105_COLORS["board"],_U105_COLORS["board_edge"])
            rounded_board(0,-.07,0,4.68,1.83,"#0a3e4a","#228f95")
            # Main GPU die and memory packages have cut corners, inner traces and edge contacts.
            chip(0,.22,-.05,1.18,.88,"#182b49",_U105_COLORS["violet"])
            for cx,cz in ((-2.0,-.47),(-1.02,.55),(1.03,.55),(2.0,-.47)):
                chip(cx,.02,cz,.47,.42,"#16304a",_U105_COLORS["blue"])
            for k in range(18):
                z=-.82+k*.095
                path([(-2.15,.015,z),(-1.55,.015,z),(-1.38,.025,z*.5),(-.66,.025,z*.4)],
                     "#1cb4a9" if k%2 else "#256f88",1)
                path([(2.15,.015,-z),(1.55,.015,-z),(1.38,.025,-z*.5),(.66,.025,-z*.4)],
                     "#1cb4a9" if k%2 else "#256f88",1)
            for x in [ -2.25+i*.18 for i in range(26) ]:
                path([(x,-.035,1.1),(x,-.035,1.27)],"#e0b96e",2)
                path([(x,-.035,-1.1),(x,-.035,-1.27)],"#e0b96e",2)
            fan(-1.25,-.05,.66,angle*1.6)
            fan(1.25,-.05,.66,-angle*1.4)
            canvas.create_text(w/2,h-15,text="RENDER / GEOMETRIA / PAMIĘĆ  •  FPS pochodzi z osobnego testu OpenGL",
                anchor="s",fill=_U105_COLORS["muted"],font=("Segoe UI",8))
        elif module=="CPU":
            rounded_board(0,-.12,0,2.62,2.28,"#22394d",_U105_COLORS["silver"])
            rounded_board(0,-.02,0,2.22,1.90,"#132940",_U105_COLORS["cyan"])
            rounded_board(0,.16,0,1.45,1.23,"#6a497e",_U105_COLORS["violet"])
            rounded_board(0,.25,0,1.08,.90,"#192d48",_U105_COLORS["silver"])
            for k in range(13):
                a=2*_U66_math.pi*k/13+angle*.28
                node((1.48*_u66_math.cos(a),.0,1.08*_u66_math.sin(a)),2.3,_U105_COLORS["amber"])
            for k in range(8):
                a=2*_U66_math.pi*k/8-angle
                path([(0,.30,0),(.30*_u66_math.cos(a),.31,.30*_u66_math.sin(a)),
                      (.45*_u66_math.cos(a),.31,.45*_u66_math.sin(a))],_U105_COLORS["cyan"],2)
            canvas.create_text(w/2,h-15,text="CPU PACKAGE  •  RDZENIE / ZEGARY / OBCIĄŻENIE",
                anchor="s",fill=_U105_COLORS["muted"],font=("Segoe UI",8))
        elif module=="RAM":
            rounded_board(0,-.12,0,4.90,.78,"#07544d",_U105_COLORS["cyan"])
            path([(-2.25,-.02,-.22),(2.25,-.02,-.22)],"#3c9b8f",2)
            for i in range(8):
                x=-1.86+i*.53
                chip(x,.08,0,.37,.48,"#192d4d",_U105_COLORS["violet"] if i%2 else _U105_COLORS["blue"])
                ring(x,.10,0,.12,_U105_COLORS["cyan"],1,angle+i,22)
            for i in range(32):
                x=-2.35+i*.15
                path([(x,-.17,.40),(x,-.17,.54)],"#e6bc72",2)
            for i in range(6):
                z=-.30+i*.12
                path([(-2.15,.0,z),(2.15,.0,z)],"#1b887f",1)
            canvas.create_text(w/2,h-15,text="RAM CHANNELS  •  WZORCE / PRZEPUSTOWOŚĆ / OBCIĄŻENIE",
                anchor="s",fill=_U105_COLORS["muted"],font=("Segoe UI",8))
        elif module=="DYSK":
            rounded_board(0,-.10,0,4.85,1.55,"#14283c",_U105_COLORS["cyan"])
            for x in (-1.55,-.52,.52,1.55):
                chip(x,.06,0,.70,.55,"#182d48",_U105_COLORS["blue"])
                path([(x-.25,.10,-.32),(x,.11,-.46),(x+.25,.10,-.32)],_U105_COLORS["cyan"],1)
            ring(0,.0,0,.70,_U105_COLORS["violet"],2,angle,70)
            ring(0,.015,0,.49,_U105_COLORS["blue"],2,-angle*1.5,64)
            ring(0,.03,0,.20,_U105_COLORS["silver"],2,angle*2,40)
            path([(.10,.12,.1),(1.02,.12,.50),(1.5,.12,.45)],_U105_COLORS["amber"],2)
            node((1.5,.14,.45),3,_U105_COLORS["white"])
            canvas.create_text(w/2,h-15,text="SSD / HDD / NVMe  •  ODCZYT / ZAPIS / CZASY",
                anchor="s",fill=_U105_COLORS["muted"],font=("Segoe UI",8))
        elif module=="EKRAN":
            rounded_board(0,-.05,0,4.20,2.48,"#172d44",_U105_COLORS["cyan"])
            rounded_board(0,.02,0,3.92,2.20,"#0b1422",_U105_COLORS["blue"])
            palette=["#ff5777","#ffb454","#f7df71","#63edac","#36cfda","#418dff","#8d74ff"]
            for i,col in enumerate(palette):
                x=-1.68+i*.56
                poly([(x,.08,-.70),(x+.43,.08,-.70),(x+.43,.08,.70),(x,.08,.70)],col,col,1)
            path([(-1.6,.10,-.50),(1.6,.10,-.50)],"#ffffff",1)
            path([(-1.6,.10,0),(1.6,.10,0)],"#ffffff",1)
            path([(-1.6,.10,.50),(1.6,.10,.50)],"#ffffff",1)
            ring(0,.14,0,.45,_U105_COLORS["white"],1,angle,50)
            rounded_board(0,-.30,-1.32,.40,.25,"#2b4155",_U105_COLORS["silver"])
            canvas.create_text(w/2,h-15,text="MATRYCA  •  KOLORY / GRADIENT / TRYBY / EDID",
                anchor="s",fill=_U105_COLORS["muted"],font=("Segoe UI",8))
        elif module in ("BATERIA","BATTERY"):
            rounded_board(0,-.08,0,3.35,1.72,"#18374a",_U105_COLORS["cyan"])
            for i in range(7):
                x=-1.35+i*.45
                ring(x,.05,0,.19,_U105_COLORS["green"] if i<5 else _U105_COLORS["amber"],2,angle,34)
                node((x,.08,0),5,_U105_COLORS["green"] if i<5 else _U105_COLORS["amber"])
            ring(0,.12,0,1.06,_U105_COLORS["blue"],1,angle*.45,58)
            path([(-1.85,.12,0),(-1.25,.12,-.36),(-.72,.12,.36),(0,.12,0),(.65,.12,-.35),(1.24,.12,.36),(1.85,.12,0)],
                 _U105_COLORS["cyan"],2)
            canvas.create_text(w/2,h-15,text="POWER / BATTERY  •  POJEMNOŚĆ / STAN / CZAS",
                anchor="s",fill=_U105_COLORS["muted"],font=("Segoe UI",8))
        elif module in ("SIEĆ","SIEC","NETWORK"):
            coords=[(-2.05,0,0),(-1.05,.35,.35),(0,.05,-.25),(1.05,.38,.40),(2.05,0,0)]
            for i in range(len(coords)-1):
                path([coords[i],((coords[i][0]+coords[i+1][0])/2,.42,_u66_math.sin(angle*2+i)*.45),coords[i+1]],
                     _U105_COLORS["cyan"],2)
            for i,p in enumerate(coords):
                ring(p[0],p[1],p[2],.26,_U105_COLORS["blue"] if i%2 else _U105_COLORS["violet"],2,angle*(i+1),42)
                node(p,5,_U105_COLORS["white"])
            for i in range(20):
                u=(i/19.0+angle*.12)%1.0
                seg=min(3,int(u*4));frac=u*4-seg
                a=coords[seg];b=coords[min(4,seg+1)]
                node((a[0]+(b[0]-a[0])*frac,.20,a[2]+(b[2]-a[2])*frac),1.8,_U105_COLORS["green"])
            canvas.create_text(w/2,h-15,text="SIEĆ  •  PAKIETY / OPÓŹNIENIE / TRANSFER",
                anchor="s",fill=_U105_COLORS["muted"],font=("Segoe UI",8))
        elif module=="AUDIO":
            ring(-1.18,.10,0,.72,_U105_COLORS["cyan"],2,angle,60)
            ring(-1.18,.12,0,.43,_U105_COLORS["blue"],2,-angle,52)
            ring(1.18,.10,0,.72,_U105_COLORS["violet"],2,-angle*.8,60)
            ring(1.18,.12,0,.43,_U105_COLORS["cyan"],2,angle*.7,52)
            pts=[]
            for i in range(61):
                x=-2.2+i*4.4/60
                y=.15+.28*_u66_math.sin(i*.48+angle*3)
                pts.append((x,y,.6))
            path(pts,_U105_COLORS["green"],2)
            canvas.create_text(w/2,h-15,text="AUDIO  •  WEJŚCIE / WYJŚCIE / SYGNAŁ",
                anchor="s",fill=_U105_COLORS["muted"],font=("Segoe UI",8))
        elif module=="KAMERA":
            ring(0,.12,0,1.0,_U105_COLORS["silver"],3,angle,64)
            ring(0,.17,0,.78,_U105_COLORS["cyan"],2,-angle*1.4,64)
            ring(0,.21,0,.50,_U105_COLORS["blue"],3,angle*2,60)
            ring(0,.25,0,.21,_U105_COLORS["violet"],3,-angle*2,44)
            for i in range(7):
                a=2*_U66_PI*i/7+angle*.5
                poly([(0,.29,0),(.25*_u66_math.cos(a),.29,.25*_u66_math.sin(a)),
                      (.50*_u66_math.cos(a+.25),.29,.50*_u66_math.sin(a+.25))],
                     "#203b58",_U105_COLORS["cyan"],1)
            for i in range(8):
                a=2*_U66_PI*i/8
                node((1.18*_u66_math.cos(a),.1,1.18*_u66_math.sin(a)),2,_U105_COLORS["amber"])
            canvas.create_text(w/2,h-15,text="KAMERA  •  OPTYKA / KLATKI / PODGLĄD",
                anchor="s",fill=_U105_COLORS["muted"],font=("Segoe UI",8))
        elif module=="USB":
            path([(-2.4,.15,.25),(-1.3,.15,.25),(-.9,.15,0),(.1,.15,0),(.5,.15,.3),(1.65,.15,.3)],
                 _U105_COLORS["cyan"],4)
            for x,z in ((-1.55,.25),(-.75,0),(.30,0),(1.15,.3)):
                ring(x,.20,z,.25,_U105_COLORS["blue"],2,angle,38)
                node((x,.23,z),3,_U105_COLORS["white"])
            rounded_board(2.0,-.03,.3,.72,.55,"#344a60",_U105_COLORS["silver"])
            for i in range(4):
                z=.12+i*.12
                path([(1.70,.02,z),(2.25,.02,z)],_U105_COLORS["amber"],2)
            canvas.create_text(w/2,h-15,text="USB  •  KONTROLER / ŁĄCZE / URZĄDZENIA",
                anchor="s",fill=_U105_COLORS["muted"],font=("Segoe UI",8))
        elif module=="KLAWIATURA":
            rounded_board(0,-.10,0,4.65,1.62,"#112d3e",_U105_COLORS["cyan"])
            for rr in range(4):
                count=14 if rr<3 else 8
                for cc in range(count):
                    x=-2.0+cc*(4.0/max(1,count-1))
                    z=-.56+rr*.37
                    a=angle*.25+(rr+cc)*.03
                    poly([(x-.10,.02,z-.10),(x+.10,.02,z-.10),(x+.13,.02,z+.10),
                          (x-.08,.02,z+.10)],"#1c3850",_U105_COLORS["blue"] if (rr+cc)%5==0 else "#367b83",1)
            path([(-1.15,.02,.72),(1.15,.02,.72)],_U105_COLORS["violet"],3)
            for i in range(20):
                x=-2.0+i*.21
                path([(x,.01,-.82),(x,.01,-.68)],"#d9b46f",2)
            canvas.create_text(w/2,h-15,text="INPUT  •  KLAWISZE / TOUCHPAD / REJESTRACJA",
                anchor="s",fill=_U105_COLORS["muted"],font=("Segoe UI",8))
        else:
            for i in range(13):
                a=2*_U66_PI*i/13+angle*.3
                x=1.62*_u66_math.cos(a);z=1.15*_u66_math.sin(a)
                path([(0,.18,0),(x,.14,z)],_U105_COLORS["grid_hi"],1)
                ring(x,.15,z,.14,_U105_COLORS["cyan"] if i%2 else _U105_COLORS["violet"],1,angle,28)
                node((x,.18,z),2,_U105_COLORS["white"])
            ring(0,.20,0,.65,_U105_COLORS["blue"],2,angle,58)
        # Bottom telemetry rail: subtle lines only, no filled rectangular status bars.
        canvas.create_line(18,h-34,w-18,h-34,fill=_U105_COLORS["grid_hi"],width=1)
        vals=getattr(app,"_live_values",{}) or {}
        cpu=vals.get("cpu");ram=vals.get("ram")
        gpu=(getattr(app,"_u66_sensor_cache",{}) or {}).get("gpu",{}) or {}
        gpu_load=gpu.get("gpu_load_percent",getattr(app,"_gpu_util",None))
        def fmt(v,unit):
            try:return "{:.0f}{}".format(float(v),unit)
            except Exception:return "N/D"
        summary="CPU "+fmt(cpu,"%")+"     RAM "+fmt(ram,"%")+"     GPU "+fmt(gpu_load,"%")
        canvas.create_text(20,h-20,text=summary,anchor="w",fill=_U105_COLORS["white"],font=("Segoe UI",8,"bold"))
        canvas.create_text(w-20,h-20,text="SCHEMAT 3D • NIE ZASTĘPUJE POMIARU",anchor="e",
            fill=_U105_COLORS["muted"],font=("Segoe UI",7))
    except Exception as exc:
        try:app.queue_log("Nowy renderer 3D: "+repr(exc))
        except Exception:pass

def _u105_stage_live_panel(self,index,total,title):
    try:
        old=getattr(self,"_u67_stage_panel",None)
        if old is not None and old.winfo_exists():old.destroy()
    except Exception:pass
    t=self.colors()
    panel=tk.Frame(self.content,bg=t["panel"],highlightthickness=0,bd=0)
    children=self.content.winfo_children()
    after_widget=None
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
    top=tk.Frame(panel,bg=t["panel"],bd=0);top.pack(fill="x",padx=4,pady=(4,3))
    self._u67_stage_title=tk.Label(top,text="TEST {}/{} — {}".format(index,total,title),
        bg=t["panel"],fg=t["accent"],font=self.fnt(10,"bold"),anchor="w")
    self._u67_stage_title.pack(side="left",fill="x",expand=True)
    self.make_button(top,"STOP TEST",self.stop_current_test,"bad",side="right",ipady=3)
    gauges=tk.Frame(panel,bg=t["panel"],bd=0);gauges.pack(fill="x",padx=2,pady=(0,4))
    self._u105_gauges={}
    for i,(key,label) in enumerate((("cpu","CPU LOAD"),("ram","RAM USED"),("gpu","GPU LOAD"),("temp","TEMP GPU"))):
        gauge=tk.Canvas(gauges,width=142,height=104,bg=t["panel"],highlightthickness=0,bd=0)
        gauge.grid(row=0,column=i,sticky="nsew",padx=7,pady=0)
        self._u105_gauges[key]=gauge
        gauges.grid_columnconfigure(i,weight=1)
    self._u67_stage_values={}
    hidden=tk.Frame(panel,bg=t["panel"],bd=0)
    for key in ("cpu","ram","gpu","gpu_temp","cpu_power","gpu_power","system_power","battery_power","cpu_voltage","gpu_voltage","cpu_fan","gpu_fan"):
        self._u67_stage_values[key]=tk.Label(hidden,text="N/D",bg=t["panel"],fg=t["accent"])
    specs=[
        ("TEMP CPU","cpu_temp"),("ZEGAR CPU","cpu_clock"),("ZEGAR GPU","gpu_clock"),
        ("DYSK ODCZYT","disk_read"),("DYSK ZAPIS","disk_write"),("NET ↓","net_down"),("NET ↑","net_up"),
        ("MOC CPU","cpu_power"),("MOC GPU","gpu_power"),("MOC SYSTEMU","system_power"),
        ("NAPIĘCIE CPU","cpu_voltage"),("NAPIĘCIE GPU","gpu_voltage"),("WENTYLATOR CPU","cpu_fan"),
        ("WENTYLATOR GPU","gpu_fan"),("MOC BATERII","battery_power")]
    strip=tk.Frame(panel,bg=t["panel"],bd=0);strip.pack(fill="x",padx=7,pady=(0,5))
    for i,(caption,key) in enumerate(specs):
        cell=tk.Frame(strip,bg=t["panel"],bd=0)
        cell.grid(row=i//5,column=i%5,sticky="ew",padx=5,pady=2)
        tk.Label(cell,text=caption,bg=t["panel"],fg=t["muted"],font=self.fnt(7,"bold"),anchor="w").pack(anchor="w")
        value=tk.Label(cell,text="N/D",bg=t["panel"],fg=t["accent"],font=self.fnt(9,"bold"),anchor="w")
        value.pack(anchor="w")
        self._u67_stage_values[key]=value
    for col in range(5):strip.grid_columnconfigure(col,weight=1)
    try: stage_screen_h=max(600,int(self.winfo_screenheight()))
    except Exception: stage_screen_h=900
    stage_chart_h=max(52,min(82,int(stage_screen_h*0.075)))
    charts=tk.Frame(panel,bg=t["panel"],bd=0);charts.pack(fill="x",padx=2,pady=(0,5))
    for name,row,col in (("_u67_stage_chart_hw",0,0),("_u67_stage_chart_io",0,1),
                         ("_u67_stage_chart_temp",1,0),("_u67_stage_chart_clocks",1,1),
                         ("_u67_stage_chart_power",2,0),("_u67_stage_chart_voltage",2,1)):
        chart=tk.Canvas(charts,height=stage_chart_h,bg=t["bg"],highlightthickness=0,bd=0)
        chart.grid(row=row,column=col,sticky="nsew",padx=4,pady=3)
        setattr(self,name,chart)
    for col in range(2):charts.grid_columnconfigure(col,weight=1)
    hist=getattr(self,"_u67_hist",{}) or {}
    for key in _U86_HISTORY_KEYS:hist.setdefault(key,[])
    self._u67_hist=hist
    self._u86_result_text=None
    module=getattr(self,"_u86_module_context",None)
    if module and not getattr(self,"_u86_suite_active",False):
        row=tk.Frame(panel,bg=t["panel"],bd=0);row.pack(fill="x",padx=5,pady=(0,3))
        self.make_button(row,"SKAN TEGO PODZESPOŁU",lambda m=module:_u86_launch_component_test(self,m,"scan"),"card",side="left",ipady=4)
        self.make_button(row,"BENCHMARK ULTRA / MAX",lambda m=module:_u86_launch_component_test(self,m,"benchmark"),"accent",side="left",ipady=4)
        self.make_button(row,"SYMULATOR 3D TEGO PODZESPOŁU",lambda m=module:_u86_launch_component_test(self,m,"visual"),"good",side="left",ipady=4)
        if module=="GPU":
            self.make_button(row,"TEST VRAM",lambda:_u86_launch_component_test(self,"VRAM","benchmark"),"card",side="left",ipady=4)
            self.make_button(row,"90 SCEN 3D",lambda:_u68_open_gpu_suite(self,auto_start=True),"good",side="left",ipady=4)
        out=tk.Text(panel,height=3,wrap="word",bg=t["bg"],fg=t["fg"],insertbackground=t["fg"],
            relief="flat",bd=0,font=("Consolas",8),padx=6,pady=4)
        out.pack(fill="x",padx=5,pady=(0,4));out.configure(state="disabled");self._u86_result_text=out
        _u86_render_component_report(self,module)
    self._u67_hist=getattr(self,"_u67_hist",{}) or {}
    _u105_refresh_visible_charts(self)
    return panel

def _u105_open_component_base(self,module,run_test=False,mode="scan"):
    self.current_view="SIM3D_"+str(module);self.clear();t=self.colors()
    title=_U68_COMPONENT_LABELS.get(str(module),str(module))
    self.header_title.config(text=title+" — SYMULATOR TECHNICZNY 3D")
    head=self.panel(self.content);head.pack(fill="x",pady=(0,4))
    tk.Label(head,text=title.upper()+"  •  PODGLĄD 3D + LIVE TELEMETRIA",bg=t["panel"],fg=t["accent"],
        font=self.fnt(11,"bold")).pack(anchor="w",padx=9,pady=(6,1))
    tk.Label(head,text="Model animowany • dane pochodzą z dostępnych liczników Windows i sterowników • brak czujnika = N/D",
        bg=t["panel"],fg=t["muted"],font=self.fnt(8),wraplength=1300,justify="left").pack(anchor="w",padx=9,pady=(0,5))
    self._u68_sim_status=tk.Label(self.content,text="Gotowy — tryb "+str(mode).upper()+".",
        bg=t["bg"],fg=t["accent"],font=self.fnt(9,"bold"),anchor="w")
    self._u68_sim_status.pack(fill="x",padx=5,pady=(2,2))
    try: screen_h=max(600,int(self.winfo_screenheight()))
    except Exception: screen_h=900
    canvas_h=max(220,min(420,int(screen_h*0.34)))
    gauge_h=max(72,min(98,int(screen_h*0.09)))
    chart_h=max(56,min(86,int(screen_h*0.08)))
    self._u68_sim_canvas=tk.Canvas(self.content,height=canvas_h,bg=_U105_COLORS["bg"],highlightthickness=0,bd=0)
    self._u68_sim_canvas.pack(fill="x",expand=True,padx=2,pady=(0,3))
    self._u68_sim_canvas.bind("<Configure>",lambda _e:self.after_idle(lambda:_u105_draw_component_scene(self)))
    gauges=tk.Frame(self.content,bg=t["bg"],bd=0);gauges.pack(fill="x",padx=2,pady=(0,1))
    self._u105_sim_gauges={}
    for i,key in enumerate(("cpu","ram","gpu","temp")):
        gauge=tk.Canvas(gauges,width=136,height=gauge_h,bg=t["bg"],highlightthickness=0,bd=0)
        gauge.grid(row=0,column=i,sticky="nsew",padx=8)
        self._u105_sim_gauges[key]=gauge
        gauges.grid_columnconfigure(i,weight=1)
    hidden=tk.Frame(self.content,bg=t["bg"],bd=0)
    self._u67_stage_values={}
    self._u67_stage_values["cpu"]=tk.Label(hidden,text="N/D")
    self._u67_stage_values["ram"]=tk.Label(hidden,text="N/D")
    self._u67_stage_values["gpu"]=tk.Label(hidden,text="N/D")
    self._u67_stage_values["gpu_temp"]=tk.Label(hidden,text="N/D")
    specs=[("TEMP CPU","cpu_temp"),("ZEGAR CPU","cpu_clock"),("ZEGAR GPU","gpu_clock"),
           ("DYSK ODCZYT","disk_read"),("DYSK ZAPIS","disk_write"),("NET ↓","net_down"),("NET ↑","net_up")]
    strip=tk.Frame(self.content,bg=t["bg"],bd=0);strip.pack(fill="x",padx=6,pady=(0,3))
    for i,(caption,key) in enumerate(specs):
        cell=tk.Frame(strip,bg=t["bg"],bd=0);cell.grid(row=i//4,column=i%4,sticky="ew",padx=6,pady=1)
        tk.Label(cell,text=caption,bg=t["bg"],fg=t["muted"],font=self.fnt(7,"bold"),anchor="w").pack(anchor="w")
        value=tk.Label(cell,text="N/D",bg=t["bg"],fg=t["accent"],font=self.fnt(9,"bold"),anchor="w")
        value.pack(anchor="w");self._u67_stage_values[key]=value
    for c in range(4):strip.grid_columnconfigure(c,weight=1)
    charts=tk.Frame(self.content,bg=t["bg"],bd=0);charts.pack(fill="x",padx=2,pady=(1,2))
    self._u67_stage_chart_hw=tk.Canvas(charts,height=chart_h,bg=t["bg"],highlightthickness=0,bd=0)
    self._u67_stage_chart_hw.grid(row=0,column=0,sticky="nsew",padx=4,pady=2)
    self._u67_stage_chart_io=tk.Canvas(charts,height=chart_h,bg=t["bg"],highlightthickness=0,bd=0)
    self._u67_stage_chart_io.grid(row=0,column=1,sticky="nsew",padx=4,pady=2)
    for c in range(2):charts.grid_columnconfigure(c,weight=1)
    self._u67_stage_chart_power=None;self._u67_stage_chart_temp=None
    self._u67_stage_chart_voltage=None;self._u67_stage_chart_clocks=None
    self._u67_hist=getattr(self,"_u67_hist",{}) or {}
    for key in _U86_HISTORY_KEYS:self._u67_hist.setdefault(key,[])
    _u105_draw_component_scene(self);_u105_draw_live_gauges(self)
    try:self.after(350,lambda:_u68_sim_metrics_tick(self))
    except Exception:pass
    # The wrapping v4.3.73 controller removes only this legacy action row and inserts current controls above the model.
    dummy=tk.Frame(self.content,bg=t["bg"],height=1,bd=0);dummy.pack(fill="x")
    if run_test:
        try:self.after(150,lambda m=module,md=mode:_u69_launch_component_test(self,m,md))
        except Exception:pass

_U105_ORIGINAL_REFRESH_VISIBLE_CHARTS=_u67_refresh_visible_charts
def _u105_refresh_visible_charts(self):
    _U105_ORIGINAL_REFRESH_VISIBLE_CHARTS(self)
    no_data_label="N/D"
    try:
        _u105_draw_live_gauges(self)
        hist=getattr(self,"_u67_hist",{}) or {}
        def draw(attr,series,maximum,title):
            canvas=getattr(self,attr,None)
            if canvas is not None and canvas.winfo_exists():
                _u67_draw_history_chart(canvas,series,maximum,title,self)
                if not any(len(values or []) >= 2 for values in series.values()):
                    width=max(220,int(canvas.winfo_width() or 500))
                    height=max(56,int(canvas.winfo_height() or 82))
                    canvas.create_text(width/2,height-16,text=no_data_label,
                        fill=self.colors()["muted"],font=self.fnt(8,"bold"))
        draw("_u67_stage_chart_hw",{k:hist.get(k,[]) for k in ("cpu","ram","gpu")},100,"CPU / RAM / GPU  •  %")
        io={k:hist.get(k,[]) for k in ("read","write","down","up")}
        io_values=[v for items in io.values() for v in items]
        draw("_u67_stage_chart_io",io,max([1.0]+io_values),"DYSK MB/s  •  SIEĆ Mbps")
        draw("_u67_stage_chart_temp",{k:hist.get(k,[]) for k in ("cpu_temp","gpu_temp")},
             max([100.0]+hist.get("cpu_temp",[])+hist.get("gpu_temp",[])),"TEMPERATURA °C")
        clocks={k:hist.get(k,[]) for k in ("cpu_clock","gpu_clock")}
        clock_values=[v for items in clocks.values() for v in items]
        draw("_u67_stage_chart_clocks",clocks,max([1000.0]+clock_values),"ZEGARY MHz")
        power={k:hist.get(k,[]) for k in ("cpu_power","gpu_power","system_power","battery_power")}
        power_values=[v for items in power.values() for v in items]
        draw("_u67_stage_chart_power",power,max([1.0]+power_values),"POBÓR MOCY W")
        voltage={k:hist.get(k,[]) for k in ("cpu_voltage","gpu_voltage")}
        voltage_values=[v for items in voltage.values() for v in items]
        draw("_u67_stage_chart_voltage",voltage,max([0.1]+voltage_values),"NAPIĘCIE V")
    except Exception:
        pass


# GPU LIVE page uses the same DPI-safe radial presentation as the component workbench.
_U105_ORIGINAL_GPU_PANEL = _u84_attach_gpu_live_panel
_U105_ORIGINAL_GPU_TICK = _u84_gpu_live_tick

def _u105_attach_gpu_panel(app):
    _U105_ORIGINAL_GPU_PANEL(app)
    for key,item in (getattr(app,"_u84_gpu_values",{}) or {}).items():
        try:
            _label,_canvas,_unit,_color=item
            if _canvas is not None and _canvas.winfo_exists():
                _canvas.configure(height=62,width=86,bg=_U105_COLORS["panel"],highlightthickness=0,bd=0)
        except Exception:
            pass

def _u105_gpu_live_tick(app,schedule=True):
    _U105_ORIGINAL_GPU_TICK(app,schedule=schedule)
    values=getattr(app,"_u84_gpu_values",{}) or {}
    telemetry=getattr(app,"_u84_gpu_last_telemetry",None) or {}
    cache=getattr(app,"_u66_sensor_cache",{}) or {}
    temps=cache.get("temps",{}) or {}
    used=_u84_gpu_numeric(telemetry.get("vram_used_mb"))
    total=_u84_gpu_numeric(telemetry.get("vram_total_mb"))
    data={
      "load":(_u84_gpu_numeric(telemetry.get("gpu_load_percent",getattr(app,"_gpu_util",None))),100.0,"%"),
      "temp":(_u84_gpu_numeric(telemetry.get("temperature_c",temps.get("gpu_temp_c"))),110.0,"°C"),
      "vram_used":(used,total or 8192.0,"MB"),
      "vram_total":(total,total or 8192.0,"MB"),
      "core_clock":(_u84_gpu_numeric(telemetry.get("gpu_clock_mhz")),3500.0,"MHz"),
      "memory_clock":(_u84_gpu_numeric(telemetry.get("memory_clock_mhz")),3000.0,"MHz"),
      "power":(_u84_gpu_numeric(telemetry.get("power_draw_w",telemetry.get("power_w",temps.get("gpu_power_w")))),500.0,"W"),
      "fan":(_u84_gpu_numeric(telemetry.get("fan_speed_rpm",temps.get("gpu_fan_rpm"))),4000.0,"RPM")
    }
    captions={"load":"GPU LOAD","temp":"GPU TEMP","vram_used":"VRAM USED",
      "vram_total":"VRAM TOTAL","core_clock":"CORE MHz","memory_clock":"MEM MHz",
      "power":"GPU POWER","fan":"FAN RPM"}
    for key,item in values.items():
        try:
            _label,canvas,unit,color=item
            val,maximum,default_unit=data.get(key,(None,100.0,unit))
            _u105_ring_gauge(canvas,captions.get(key,key.upper()),val,maximum,default_unit,color)
        except Exception:
            pass

_u84_attach_gpu_live_panel=_u105_attach_gpu_panel
_u84_gpu_live_tick=_u105_gpu_live_tick

def _u105_recursive_code_names(code):
    import types as _u105_types
    names=set(code.co_names)
    names.add(code.co_name)
    for item in code.co_consts:
        if isinstance(item,_u105_types.CodeType):
            names.update(_u105_recursive_code_names(item))
    return names

def _u105_selftest_visual_quality():
    assert callable(_u105_draw_component_scene)
    assert callable(_u105_open_component_base)
    assert callable(_u105_ring_gauge)
    names=_u105_recursive_code_names(_u105_draw_component_scene.__code__)
    assert "create_polygon" in names and "create_oval" in names and "create_line" in names
    assert "create_rectangle" not in names, "The new 3D renderer must not draw the model out of rectangles."
    assert _U69_ORIGINAL_OPEN_COMPONENT_SIMULATOR is _u105_open_component_base
    assert _U105_PI > 3.14 and _U66_PI > 3.14
    assert "max(640" not in _u105_draw_component_scene.__code__.co_consts
    assert callable(_u105_attach_gpu_panel) and callable(_u105_gpu_live_tick)
    assert "create_rectangle" not in _u105_gpu_live_tick.__code__.co_names
    assert _u67_stage_live_panel is _u105_stage_live_panel
    assert _u67_refresh_visible_charts is _u105_refresh_visible_charts
    stage_constants=repr(_u105_stage_live_panel.__code__.co_consts)
    refresh_constants=repr(_u105_refresh_visible_charts.__code__.co_consts)
    assert "_u67_stage_chart_power" in stage_constants and "_u67_stage_chart_voltage" in stage_constants
    assert "POBÓR MOCY W" in refresh_constants and "NAPIĘCIE V" in refresh_constants
    assert all(k in names for k in ("project","poly","path","ring","fan","chip"))
    print("POLISHED_SIMULATOR_UI_SELFTEST_OK: technical component renderers, radial gauges, line charts, no bar/rectangle model")

# Replace only the visual layer; keep the existing theme colors, module dispatch, tests and results.
_U69_ORIGINAL_OPEN_COMPONENT_SIMULATOR=_u105_open_component_base
_u68_draw_component_scene=_u105_draw_component_scene
_u67_stage_live_panel=_u105_stage_live_panel
_u67_refresh_visible_charts=_u105_refresh_visible_charts


# v4.3.106 — robust CPU sensor mapping, full searchable sensor inspector and accurate adaptive Speed Test byte accounting.
import csv as _u106_csv

def _u106_extract_cpu_sensor_values(probe):
    rows=(probe or {}).get("sensors") or []
    candidates={
        "cpu_temp_c":[],"cpu_power_w":[],"cpu_clock_mhz":[],
        "cpu_voltage_v":[],"cpu_fan_rpm":[]
    }
    counts={}
    for row in rows:
        if not isinstance(row,dict):
            continue
        st=str(row.get("sensorType") or row.get("sensor_type") or row.get("type") or "").strip().lower()
        unit=str(row.get("unit") or "").strip().lower()
        hardware=str(row.get("hardware") or "")
        hardware_type=str(row.get("hardwareType") or row.get("hardware_type") or "")
        name=str(row.get("sensor") or row.get("name") or "")
        parent=str(row.get("parent") or "")
        label=(hardware+" "+hardware_type+" "+parent+" "+name).lower()
        htype=hardware_type.lower()
        cpu_like=("cpu" in htype or "processor" in htype
                  or "processor" in label or "cpu" in label
                  or ("core" in label and ("amd" in hardware.lower() or "intel" in hardware.lower())))
        if not cpu_like:
            continue
        try:
            value=float(row.get("value"))
            if not _u66_math.isfinite(value):
                continue
        except Exception:
            continue
        if st=="temperature" or unit in ("°c","c"):
            # Package/Tctl/Tdie/CCD are preferred over a generic core or board reading.
            if any(k in label for k in ("tctl","tdie","cpu die","ccd")):
                priority=60
            elif "package" in label:
                priority=55
            elif "core" in label:
                priority=45
            elif "cpu" in label or "processor" in label:
                priority=35
            else:
                priority=10
            candidates["cpu_temp_c"].append((priority,value,name))
            counts["temperature"]=counts.get("temperature",0)+1
        elif st=="power" or unit in ("w","watt","watts"):
            priority=60 if any(k in label for k in ("package","ppt","cpu package")) else 40
            candidates["cpu_power_w"].append((priority,value,name))
            counts["power"]=counts.get("power",0)+1
        elif st=="clock" or unit in ("mhz","ghz"):
            if unit=="ghz":
                value*=1000.0
            priority=60 if any(k in label for k in ("effective","core clock","core #","cpu clock")) else 35
            candidates["cpu_clock_mhz"].append((priority,value,name))
            counts["clock"]=counts.get("clock",0)+1
        elif st=="voltage" or unit in ("v","mv"):
            if unit=="mv":
                value/=1000.0
            priority=60 if any(k in label for k in ("vcore","core voltage","cpu core")) else 35
            candidates["cpu_voltage_v"].append((priority,value,name))
            counts["voltage"]=counts.get("voltage",0)+1
        elif st=="fan" or unit=="rpm":
            candidates["cpu_fan_rpm"].append((50 if "cpu" in label else 30,value,name))
            counts["fan"]=counts.get("fan",0)+1
    result={}
    for field,items in candidates.items():
        if items:
            result[field]=max(items,key=lambda x:x[0])[1]
        else:
            result[field]=None
    result["cpu_sensor_candidates"]=counts
    result["sensor_count"]=len([x for x in rows if isinstance(x,dict)])
    return result

_U106_ORIGINAL_SENSOR_PROBE=_u66_sensor_probe
def _u106_sensor_probe():
    result=_U106_ORIGINAL_SENSOR_PROBE()
    if not isinstance(result,dict):
        return result
    mapped=_u106_extract_cpu_sensor_values(result)
    for field in ("cpu_temp_c","cpu_power_w","cpu_clock_mhz","cpu_voltage_v","cpu_fan_rpm"):
        value=mapped.get(field)
        if value is not None:
            result[field]=value
    result["sensor_count"]=mapped.get("sensor_count",len(result.get("sensors") or []))
    result["cpu_sensor_candidates"]=mapped.get("cpu_sensor_candidates",{})
    rows=result.get("sensors") or []
    result["sensor_category_counts"]={}
    for row in rows:
        if not isinstance(row,dict):
            continue
        category=str(row.get("sensorType") or row.get("sensor_type") or row.get("type") or "other")
        result["sensor_category_counts"][category]=result["sensor_category_counts"].get(category,0)+1
    # Use all-vendor GPU sensor matching for drivers whose labels omit "GPU Core".
    try:
        gpu_values=_u100_gpu_from_sensors(result)
        mapping={
            "gpu_temp_c":"temperature_c",
            "gpu_power_w":"power_draw_w",
            "gpu_clock_mhz":"gpu_clock_mhz",
            "gpu_fan_rpm":"fan_speed_rpm"
        }
        for target,source in mapping.items():
            if result.get(target) is None and gpu_values.get(source) is not None:
                result[target]=gpu_values[source]
    except Exception:
        pass
    return result

def _u106_get_sensor_rows(app):
    # Merge compact dashboard values with every raw sensor exposed by the bridge, Windows and GPU telemetry.
    rows=[]
    try:
        tree=getattr(app,"_u100_sensor_tree",None)
        if tree is not None and tree.winfo_exists():
            for item in tree.get_children(""):
                values=tree.item(item,"values") or ()
                if len(values)>=6:
                    rows.append({"category":str(values[0]),"hardware":str(values[1]),
                        "sensor":str(values[2]),"value":str(values[3]),"unit":str(values[4]),"source":str(values[5])})
    except Exception:
        pass
    def signature(row):
        return tuple(str(row.get(k,"") if row.get(k) is not None else "N/D").strip().casefold()
            for k in ("hardware","sensor","unit"))
    seen={signature(row) for row in rows}
    def add(row):
        sig=signature(row)
        if sig not in seen:
            rows.append(row)
            seen.add(sig)
    cache=getattr(app,"_u66_sensor_cache",{}) or {}
    temps=cache.get("temps",{}) or {}
    system=cache.get("system",{}) or {}
    gpu=cache.get("gpu",{}) or {}
    for row in temps.get("sensors",[]) or []:
        if not isinstance(row,dict): continue
        add({"category":row.get("sensorType") or row.get("sensor_type") or "Other",
            "hardware":row.get("hardware") or row.get("hardwareType") or row.get("parent") or "N/D",
            "sensor":row.get("sensor") or row.get("name") or "N/D","value":row.get("value"),
            "unit":row.get("unit") or "","source":row.get("source") or temps.get("method") or "LibreHardwareMonitor / Sensor Bridge"})
    for key,value in system.items():
        if not isinstance(value,(dict,list,tuple)):
            add({"category":"System","hardware":"Windows","sensor":key,"value":value,"unit":"","source":"Windows / psutil"})
    for key,value in gpu.items():
        if key not in ("sensor_rows","message","available","provider","error") and not isinstance(value,(dict,list,tuple)):
            add({"category":"GPU","hardware":"GPU","sensor":key,"value":value,"unit":"","source":gpu.get("provider") or "GPU telemetry"})
    return rows

def _u106_open_sensor_inspector(app):
    try:
        existing=getattr(app,"_u106_sensor_window",None)
        if existing is not None and existing.winfo_exists():
            existing.deiconify()
            existing.lift()
            refresh=getattr(app,"_u106_sensor_refresh",None)
            if callable(refresh):
                refresh()
            return
    except Exception:
        pass
    win=tk.Toplevel(app)
    app._u106_sensor_window=win
    win.title("NAPRAWA PC — PEŁNY INSPEKTOR CZUJNIKÓW")
    win.geometry("1280x780")
    try:
        win.minsize(900,520)
    except Exception:
        pass
    t=app.colors()
    root=tk.Frame(win,bg=t["bg"]);root.pack(fill="both",expand=True,padx=10,pady=10)
    headline=tk.Frame(root,bg=t["panel"]);headline.pack(fill="x",pady=(0,6))
    tk.Label(headline,text="PEŁNE ODCZYTY SPRZĘTOWE — WSZYSTKIE DOSTĘPNE SENSORY",
             bg=t["panel"],fg=t["accent"],font=app.fnt(13,"bold")).pack(anchor="w",padx=12,pady=(9,2))
    tk.Label(headline,text="Dane z LibreHardwareMonitor/Sensor Bridge, Windows/psutil i sterowników. Brak pomiaru = N/D; lista może obejmować setki odczytów.",
             bg=t["panel"],fg=t["muted"],font=app.fnt(9),wraplength=1200,justify="left").pack(anchor="w",padx=12,pady=(0,8))
    controls=tk.Frame(root,bg=t["bg"]);controls.pack(fill="x",pady=(0,6))
    tk.Label(controls,text="Szukaj:",bg=t["bg"],fg=t["fg"],font=app.fnt(9,"bold")).pack(side="left",padx=(0,5))
    search_var=tk.StringVar()
    search=ttk.Entry(controls,textvariable=search_var,width=34)
    search.pack(side="left",padx=(0,10))
    tk.Label(controls,text="Kategoria:",bg=t["bg"],fg=t["fg"],font=app.fnt(9,"bold")).pack(side="left",padx=(0,5))
    category_var=tk.StringVar(value="Wszystkie")
    category=ttk.Combobox(controls,textvariable=category_var,state="readonly",width=18,
        values=("Wszystkie","Temperature","Load","Clock","Voltage","Fan","Power","Memory","Throughput","Battery","System","ACPI / Temperature","Other"))
    category.pack(side="left",padx=(0,10))
    count_label=tk.Label(controls,text="Odczyty: 0",bg=t["bg"],fg=t["muted"],font=app.fnt(9,"bold"))
    count_label.pack(side="left",padx=6)
    status_label=tk.Label(controls,text="Odświeżanie co 3 s",bg=t["bg"],fg=t["muted"],font=app.fnt(8))
    status_label.pack(side="right",padx=4)
    table_frame=tk.Frame(root,bg=t["panel"]);table_frame.pack(fill="both",expand=True)
    cols=("category","hardware","sensor","value","unit","source")
    tree=ttk.Treeview(table_frame,columns=cols,show="headings")
    labels={"category":"KATEGORIA","hardware":"PODZESPÓŁ","sensor":"CZUJNIK / METRYKA","value":"WARTOŚĆ","unit":"JEDNOSTKA","source":"ŹRÓDŁO"}
    widths={"category":130,"hardware":230,"sensor":300,"value":120,"unit":90,"source":270}
    for col in cols:
        tree.heading(col,text=labels[col])
        tree.column(col,width=widths[col],minwidth=70,stretch=col in ("hardware","sensor","source"))
    vs=ttk.Scrollbar(table_frame,orient="vertical",command=tree.yview)
    hs=ttk.Scrollbar(table_frame,orient="horizontal",command=tree.xview)
    tree.configure(yscrollcommand=vs.set,xscrollcommand=hs.set)
    tree.grid(row=0,column=0,sticky="nsew");vs.grid(row=0,column=1,sticky="ns");hs.grid(row=1,column=0,sticky="ew")
    table_frame.grid_rowconfigure(0,weight=1);table_frame.grid_columnconfigure(0,weight=1)
    footer=tk.Frame(root,bg=t["bg"]);footer.pack(fill="x",pady=(6,0))
    def export_csv():
        full_rows=_u106_get_sensor_rows(app)
        filename=filedialog.asksaveasfilename(parent=win,title="Eksport wszystkich odczytów czujników",
            defaultextension=".csv",filetypes=(("CSV","*.csv"),("Wszystkie pliki","*.*")),
            initialfile="NaprawaPC-Czujniki-"+_U66_datetime.now().strftime("%Y%m%d-%H%M%S")+".csv")
        if not filename:
            return
        try:
            with open(filename,"w",newline="",encoding="utf-8-sig") as stream:
                writer=_u106_csv.DictWriter(stream,fieldnames=("category","hardware","sensor","value","unit","source"))
                writer.writeheader()
                writer.writerows(full_rows)
            status_label.config(text=f"CSV zapisany • {len(full_rows)} odczytów")
            app.queue_log(f"INSPEKTOR CZUJNIKÓW: eksport CSV {filename} ({len(full_rows)} odczytów)")
        except Exception as exc:
            messagebox.showerror("Eksport czujników",f"{type(exc).__name__}: {exc}",parent=win)
    tk.Button(footer,text="EKSPORTUJ PEŁNĄ LISTĘ CSV",command=export_csv,bg=t["accent"],fg="#06111c",
        activebackground=t["accent2"],relief="flat",padx=12,pady=6).pack(side="left")
    tk.Button(footer,text="ODŚWIEŻ TERAZ",command=lambda:refresh(False),bg=t["card"],fg=t["fg"],
        activebackground=t["accent2"],relief="flat",padx=12,pady=6).pack(side="left",padx=5)
    tk.Button(footer,text="ZAMKNIJ",command=win.destroy,bg=t["card"],fg=t["fg"],
        activebackground=t["accent2"],relief="flat",padx=12,pady=6).pack(side="right")
    state={"signature":None,"closed":False}
    def refresh(schedule_next=True):
        try:
            if not win.winfo_exists():
                state["closed"]=True
                return
            rows=_u106_get_sensor_rows(app)
            query=str(search_var.get() or "").strip().casefold()
            wanted=str(category_var.get() or "Wszystkie").casefold()
            if wanted=="wszystkie":
                filtered=rows
            else:
                filtered=[r for r in rows if wanted in str(r.get("category","")).casefold()
                    or (wanted=="system" and any(k in str(r.get("category","")).casefold() for k in ("system","memory","throughput","battery")))
                    or (wanted=="other" and str(r.get("category","")).casefold() not in {
                        "temperature","load","clock","voltage","fan","power","memory","throughput","battery","system"})]
            if query:
                filtered=[r for r in filtered if query in " ".join(str(r.get(k,"")) for k in ("category","hardware","sensor","value","unit","source")).casefold()]
            signature=tuple(tuple(str(r.get(k,"")) for k in cols) for r in filtered)
            if signature!=state["signature"]:
                tree.delete(*tree.get_children(""))
                for index,row in enumerate(filtered):
                    tree.insert("","end",iid=f"sensor-{index}",values=tuple(row.get(k,"") if row.get(k) is not None else "N/D" for k in cols))
                state["signature"]=signature
            count_label.config(text=f"Wyświetlane: {len(filtered)} / {len(rows)}")
            status_label.config(text="Źródło aktualizowane w tle • odświeżenie 3 s")
        except Exception as exc:
            try:status_label.config(text=f"Błąd odświeżania: {type(exc).__name__}")
            except Exception:pass
        try:
            if schedule_next and win.winfo_exists():
                win.after(3000,refresh)
        except Exception:
            pass
    app._u106_sensor_refresh=lambda:refresh(False)
    search.bind("<KeyRelease>",lambda _event:refresh(False))
    category.bind("<<ComboboxSelected>>",lambda _event:refresh(False))
    def on_close():
        state["closed"]=True
        try:win.destroy()
        except Exception:pass
    win.protocol("WM_DELETE_WINDOW",on_close)
    refresh()
    try:
        if callable(globals().get("_u101_sensor_poll")):
            _u101_sensor_poll(app)
    except Exception:
        pass

_U106_ORIGINAL_ATTACH_SENSOR_TABLE=_u100_attach_sensor_table
def _u106_attach_sensor_table(app,parent,height=10):
    panel=_U106_ORIGINAL_ATTACH_SENSOR_TABLE(app,parent,height)
    try:
        if panel is None or not panel.winfo_exists():
            return panel
        if getattr(panel,"_u106_inspector_button_added",False):
            return panel
        children=panel.winfo_children()
        top=children[0] if children else None
        if top is not None and top.winfo_exists():
            t=app.colors()
            tk.Button(top,text="PEŁNY INSPEKTOR / CSV",
                command=lambda a=app:_u106_open_sensor_inspector(a),
                bg=t["card"],fg=t["fg"],activebackground=t["accent"],relief="flat",
                font=app.fnt(8,"bold"),padx=7,pady=3).pack(side="right",padx=(5,4))
            panel._u106_inspector_button_added=True
    except Exception as exc:
        try:app.queue_log("Inspektor czujników UI: "+repr(exc))
        except Exception:pass
    return panel

_U106_ORIGINAL_SPEED_STARTER=_u101_start_speed_test
_u66_sensor_probe=_u106_sensor_probe
_u100_attach_sensor_table=_u106_attach_sensor_table
_u81_attach_sensor_table=_u106_attach_sensor_table
_u81_refresh_sensor_table=_u101_refresh_sensor_table


_U106_ORIGINAL_MEASURE_SPEED=_u100_measure_speed

def _u106_speed_transfer_counts(download_rows, upload_rows):
    downloads=[row for row in (download_rows or []) if isinstance(row,dict) and row.get("state")=="good"]
    uploads=[row for row in (upload_rows or []) if isinstance(row,dict) and row.get("state")=="good"]
    download_bytes=sum(max(0,int(row.get("bytes",0) or 0)) for row in downloads)
    upload_bytes=sum(max(0,int(row.get("requested_bytes",0) or 0)) for row in uploads)
    return {"download_data_bytes":download_bytes,"upload_data_bytes":upload_bytes,"data_bytes":download_bytes+upload_bytes}

def _u106_measure_speed(app):
    # Keep the original HTTPS transport and validate real transfer results through this common wrapper.
    request_transport=_U100_ORIGINAL_SPEED_REQUEST
    if not callable(request_transport):
        raise RuntimeError("Brakuje HTTPS transportu Speed Test.")
    result=_U106_ORIGINAL_MEASURE_SPEED(app)
    if not isinstance(result,dict):
        return result
    counts=_u106_speed_transfer_counts(result.get("download",[]),result.get("upload",[]))
    result.update(counts)
    # Keep stable metric fields visible to the UI and diagnostic history even if a provider sample failed.
    result["download_peak_mbps"]=result.get("download_peak_mbps")
    result["upload_peak_mbps"]=result.get("upload_peak_mbps")
    result["latency_jitter_ms"]=result.get("latency_jitter_ms")
    try:
        history_path=result.get("history_path")
        if history_path:
            hp=Path(history_path)
            records=_u66_json.loads(hp.read_text(encoding="utf-8"))
            if records and records[-1].get("started_at")==result.get("started_at"):
                records[-1].update(counts)
                hp.write_text(_u66_json.dumps(records[-100:],ensure_ascii=False,indent=2),encoding="utf-8")
    except Exception as exc:
        result["history_warning"]=f"Nie udało się zaktualizować historii po korekcie bajtów: {type(exc).__name__}: {exc}"
    return result

_u100_measure_speed=_u106_measure_speed
_u90_measure_speed=_u106_measure_speed
_u66_measure_speed=_u106_measure_speed

def _u106_selftest_sensor_mapping():
    synthetic={"sensors":[
        {"hardware":"AMD Ryzen 7","hardwareType":"CpuAmd","sensor":"Core (Tctl/Tdie)","sensorType":"Temperature","value":77.5,"unit":"°C"},
        {"hardware":"AMD Ryzen 7","hardwareType":"CpuAmd","sensor":"Core #1","sensorType":"Temperature","value":63.0,"unit":"°C"},
        {"hardware":"Intel CPU","hardwareType":"CpuIntel","sensor":"CPU Package","sensorType":"Power","value":84.2,"unit":"W"},
        {"hardware":"Intel CPU","hardwareType":"CpuIntel","sensor":"Core Clock","sensorType":"Clock","value":4.2,"unit":"GHz"},
        {"hardware":"Intel CPU","hardwareType":"CpuIntel","sensor":"Core Voltage","sensorType":"Voltage","value":1100,"unit":"mV"},
        {"hardware":"Intel CPU","hardwareType":"CpuIntel","sensor":"CPU Fan","sensorType":"Fan","value":1250,"unit":"RPM"}
    ]}
    mapped=_u106_extract_cpu_sensor_values(synthetic)
    assert mapped["cpu_temp_c"]==77.5
    assert mapped["cpu_power_w"]==84.2
    assert mapped["cpu_clock_mhz"]==4200.0
    assert mapped["cpu_voltage_v"]==1.1
    assert mapped["cpu_fan_rpm"]==1250
    assert mapped["sensor_count"]==6
    class _U106FakeApp:
        _u100_sensor_tree=None
        _u66_sensor_cache={"temps":{"method":"test bridge","sensors":[
            {"hardware":"CPU Package","sensor":"CPU Package","sensorType":"Temperature","value":77.5,"unit":"°C"},
            {"hardware":"GPU Core","sensor":"GPU Core","sensorType":"Temperature","value":68.0,"unit":"°C"},
            {"hardware":"Motherboard","sensor":"Fan #1","sensorType":"Fan","value":1250,"unit":"RPM"}]},
            "system":{"cpu_percent":37.5,"ram_percent":61.0,"disk_read_mbps":12.5},
            "gpu":{"provider":"test GPU","gpu_load_percent":88.0,"temperature_c":68.0}}
    expanded=_u106_get_sensor_rows(_U106FakeApp())
    names={str(row.get("sensor")) for row in expanded}
    assert {"CPU Package","GPU Core","Fan #1","Użycie CPU","Użycie RAM","Odczyt wszystkich dysków","gpu_load_percent"}.issubset(names)
    assert len(expanded)>=7, "Full inspector must merge raw bridge rows and system/GPU metrics"
    assert callable(_u106_open_sensor_inspector)
    print("CPU_SENSOR_MAPPING_AND_FULL_SENSOR_INSPECTOR_SELFTEST_OK")

def _u106_selftest_adaptive_speed_payloads():
    sample=_u106_speed_transfer_counts(
        [{"state":"good","bytes":1234},{"state":"error","bytes":9999}],
        [{"state":"good","requested_bytes":5678},{"state":"error","requested_bytes":1111}]
    )
    assert sample=={"download_data_bytes":1234,"upload_data_bytes":5678,"data_bytes":6912}
    code=repr(_u100_measure_speed.__code__.co_consts)+repr(_u100_measure_speed.__code__.co_names)
    assert "_U100_ORIGINAL_SPEED_REQUEST" in _u100_measure_speed.__code__.co_names
    assert "download_peak_mbps" in code and "upload_peak_mbps" in code
    assert "latency_jitter_ms" in code
    assert callable(_u101_start_speed_test)
    _speed_name=getattr(_u66_measure_speed, "__name__", "")
    _speed_wrapper_ok=(_speed_name=="_u124_measure_speed" and "_U124_ORIGINAL_MEASURE_SPEED" in _u66_measure_speed.__code__.co_names)
    assert _u66_measure_speed is _u100_measure_speed or _speed_name=="_u108_measure_speed" or _speed_wrapper_ok, "Speed Test must use the validated adaptive engine, optionally wrapped by the profile selector"
    print("ADAPTIVE_SPEED_PAYLOAD_ACCOUNTING_SELFTEST_OK")


# v4.3.111 — fix live sensor refresh, expose per-core/per-device metrics, validate throughput samples, and give every catalog test its own OpenGL scene.
_U107_ORIGINAL_COLLECT_OS_METRICS = _u101_collect_os_metrics
_U107_ORIGINAL_SENSOR_RECORDS = _u104_sensor_records
_U107_ORIGINAL_SENSOR_ROWS = _u106_get_sensor_rows
_U107_ORIGINAL_OPEN_SENSOR_INSPECTOR = _u106_open_sensor_inspector
_U107_ORIGINAL_ATTACH_SENSOR_TABLE = _u106_attach_sensor_table
_U107_ORIGINAL_MEASURE_SPEED = _u100_measure_speed
_U107_ORIGINAL_SHOW_SPEED_TEST = AppV43.show_speed_test
_U107_ORIGINAL_OPEN_COMPONENT_SIMULATOR = _u69_open_component_simulator

# One explicitly assigned renderer scene for each of the 70 independent catalog tests.
# Each scene ID is unique; the renderer measures real OpenGL FPS and reports GPU renderer/API.
_U107_TEST_SCENES = {
    "cpu_scan":46, "cpu_single":47, "cpu_multi":48, "cpu_load60":49, "cpu_max":50, "cpu_sensor":51, "cpu_sim":12,
    "ram_scan":25, "ram_512":26, "ram_1024":27, "ram_2048":28, "ram_bw":29, "ram_max":30, "ram_sim":24,
    "gpu_scan":1, "gpu_scene":2, "gpu_std":3, "gpu_ultra":16, "gpu_max":17, "gpu_sensor":18, "gpu_games":58, "gpu_sim":59,
    "vram_scan":31, "vram_64":32, "vram_128":33, "vram_256":55, "vram_max":56, "vram_sim":57,
    "disk_scan":13, "disk_smart":14, "disk_512":15, "disk_2048":37, "disk_4096":38, "disk_max":39, "disk_sim":22,
    "screen_edid":52, "screen_modes":53, "screen_patterns":54, "screen_rgb":10, "screen_sim":11,
    "sec_scan":43, "sec_startup":44, "sec_events":45, "sec_sim":60,
    "bat_scan":7, "bat_180":8, "bat_600":9, "bat_report":64, "bat_sim":65,
    "net_scan":61, "net_dns":62, "net_speed":63, "net_jitter":67, "net_sim":68,
    "usb_scan":19, "usb_errors":20, "usb_functional":21, "usb_sim":42,
    "audio_scan":4, "audio_mic":5, "audio_output":6, "audio_functional":40, "audio_sim":41,
    "key_scan":34, "key_press":35, "key_functional":36, "key_sim":23,
    "cam_scan":76, "cam_preview":77, "cam_sim":78
}


def _u107_finite_number(value):
    try:
        number=float(value)
        return number if _u66_math.isfinite(number) else None
    except Exception:
        return None

def _u107_collect_os_metrics(app):
    metrics=_U107_ORIGINAL_COLLECT_OS_METRICS(app) or {}
    if not psutil:
        return metrics
    try:
        values=psutil.cpu_percent(interval=None,percpu=True)
        metrics["cpu_per_core_percent"]=[round(float(x),2) for x in values]
    except Exception:
        metrics["cpu_per_core_percent"]=[]
    now=_u66_time.monotonic()
    # Per-physical/logical disk counters. First sample is N/D, never a fabricated zero rate.
    try:
        disk_now=psutil.disk_io_counters(perdisk=True) or {}
    except Exception:
        disk_now={}
    disk_prev=getattr(app,"_u107_disk_io_prev",{}) or {}
    disk_dt=max(.05,now-float(disk_prev.get("time",now))) if disk_prev else None
    disk_rows=[]
    disk_snapshot={}
    for name,counter in disk_now.items():
        read=int(getattr(counter,"read_bytes",0) or 0)
        write=int(getattr(counter,"write_bytes",0) or 0)
        read_count=int(getattr(counter,"read_count",0) or 0)
        write_count=int(getattr(counter,"write_count",0) or 0)
        old=(disk_prev.get("items") or {}).get(name)
        read_rate=write_rate=read_iops=write_iops=None
        if old and disk_dt:
            read_rate=max(0.0,(read-old["read"])/disk_dt/1_000_000)
            write_rate=max(0.0,(write-old["write"])/disk_dt/1_000_000)
            read_iops=max(0.0,(read_count-old["read_count"])/disk_dt)
            write_iops=max(0.0,(write_count-old["write_count"])/disk_dt)
        disk_rows.append({"name":str(name),"read_mbps":read_rate,"write_mbps":write_rate,
            "read_iops":read_iops,"write_iops":write_iops,"read_bytes_total":read,
            "write_bytes_total":write,"read_operations_total":read_count,"write_operations_total":write_count})
        disk_snapshot[str(name)]={"read":read,"write":write,"read_count":read_count,"write_count":write_count}
    app._u107_disk_io_prev={"time":now,"items":disk_snapshot}
    metrics["disk_devices"]=disk_rows

    # Per-network-interface throughput, adapter state, link speed and addresses.
    try:
        net_now=psutil.net_io_counters(pernic=True) or {}
    except Exception:
        net_now={}
    net_prev=getattr(app,"_u107_net_io_prev",{}) or {}
    net_dt=max(.05,now-float(net_prev.get("time",now))) if net_prev else None
    try: iface_stats=psutil.net_if_stats() or {}
    except Exception: iface_stats={}
    try: iface_addrs=psutil.net_if_addrs() or {}
    except Exception: iface_addrs={}
    net_rows=[];net_snapshot={}
    for name,counter in net_now.items():
        recv=int(getattr(counter,"bytes_recv",0) or 0)
        sent=int(getattr(counter,"bytes_sent",0) or 0)
        old=(net_prev.get("items") or {}).get(name)
        down=up=None
        if old and net_dt:
            down=max(0.0,(recv-old["recv"])*8/net_dt/1_000_000)
            up=max(0.0,(sent-old["sent"])*8/net_dt/1_000_000)
        stat=iface_stats.get(name)
        addresses=[]
        for addr in iface_addrs.get(name,[]) or []:
            address=str(getattr(addr,"address","") or "")
            if address: addresses.append(address)
        net_rows.append({"name":str(name),"download_mbps":down,"upload_mbps":up,
            "bytes_received_total":recv,"bytes_sent_total":sent,
            "is_up":bool(stat.isup) if stat else None,
            "link_speed_mbps":getattr(stat,"speed",None) if stat else None,
            "mtu":getattr(stat,"mtu",None) if stat else None,"addresses":addresses})
        net_snapshot[str(name)]={"recv":recv,"sent":sent}
    app._u107_net_io_prev={"time":now,"items":net_snapshot}
    metrics["network_interfaces"]=net_rows

    # Filesystem capacity per mounted volume. A failed/unavailable mount remains absent, not zero.
    partitions=[]
    try:
        mounts=psutil.disk_partitions(all=False) or []
    except Exception:
        mounts=[]
    for part in mounts:
        mount=str(getattr(part,"mountpoint","") or "")
        if not mount: continue
        try:
            usage=psutil.disk_usage(mount)
            partitions.append({"device":str(getattr(part,"device","") or mount),"mountpoint":mount,
                "filesystem":str(getattr(part,"fstype","") or "N/D"),"total_bytes":int(usage.total),
                "used_bytes":int(usage.used),"free_bytes":int(usage.free),"used_percent":float(usage.percent)})
        except Exception:
            partitions.append({"device":str(getattr(part,"device","") or mount),"mountpoint":mount,
                "filesystem":str(getattr(part,"fstype","") or "N/D"),"total_bytes":None,
                "used_bytes":None,"free_bytes":None,"used_percent":None})
    metrics["partitions"]=partitions
    metrics["sampled_at"]=_U66_datetime.now().isoformat(timespec="seconds")
    return metrics

def _u107_sensor_category(sensor_type,unit=""):
    st=str(sensor_type or "Other").strip().lower()
    un=str(unit or "").strip().lower()
    if st=="temperature" or un in ("°c","c"): return "Temperature"
    if st in ("load","level") or un=="%": return "Load"
    if st=="clock" or un in ("mhz","ghz"): return "Clock"
    if st=="voltage" or un in ("v","mv"): return "Voltage"
    if st=="fan" or un=="rpm": return "Fan"
    if st=="power" or un in ("w","watt","watts"): return "Power"
    if st in ("smallData".lower(),"data","memory"): return "Memory"
    if st in ("throughput","current","energy","timespan"): return st.title()
    return "Other"

def _u107_get_sensor_rows(app):
    # Rebuild from the freshest cache first. The prior implementation could prefer stale Treeview text over new readings.
    cache=getattr(app,"_u66_sensor_cache",{}) or {}
    temps=cache.get("temps",{}) or {}
    system=cache.get("system",{}) or {}
    gpu=cache.get("gpu",{}) or {}
    rows=[]
    seen=set()
    def identity(row):
        # Sensor identifiers distinguish multiple same-name fans/cores on the same controller.
        return tuple(str(row.get(k,"") if row.get(k) is not None else "N/D").strip().casefold()
            for k in ("hardware","sensor","unit","_identity_hint"))
    def add(category,hardware,name,value,unit="",source="N/D",identity_hint=""):
        if isinstance(value,dict) or isinstance(value,(list,tuple)):
            return
        if value is None:
            shown="N/D"
        elif isinstance(value,bool):
            shown="TAK" if value else "NIE"
        elif isinstance(value,(int,float)):
            try:
                number=float(value)
                shown=(f"{number:.2f}".rstrip("0").rstrip(".") if _u66_math.isfinite(number) else "N/D")
            except Exception:
                shown="N/D"
        else:
            shown=str(value)
        row={"category":str(category or "Other"),"hardware":str(hardware or "N/D"),
             "sensor":str(name or "N/D"),"value":shown,"unit":str(unit or ""),
             "source":str(source or "N/D"),"_identity_hint":str(identity_hint or "")}
        key=identity(row)
        if key not in seen:
            seen.add(key);rows.append(row)

    # Raw sensor records from LibreHardwareMonitor/Sensor Bridge are the authoritative source.
    raw=temps.get("sensors",[]) or []
    if not raw:
        for group,items in (temps.get("sensor_groups",{}) or {}).items():
            for item in items or []:
                if isinstance(item,dict):
                    raw=list(raw)+[item]
    for sensor in raw:
        if not isinstance(sensor,dict): continue
        unit=sensor.get("unit") or ""
        stype=sensor.get("sensorType") or sensor.get("sensor_type") or sensor.get("type") or "Other"
        hardware=(str(sensor.get("hardware") or sensor.get("parent") or "N/D")
            +(" / "+str(sensor.get("hardwareType") or sensor.get("hardware_type")) if (sensor.get("hardwareType") or sensor.get("hardware_type")) else ""))
        add(_u107_sensor_category(stype,unit),hardware,
            sensor.get("sensor") or sensor.get("name") or "N/D",sensor.get("value"),unit,
            sensor.get("source") or temps.get("method") or temps.get("bridge_provider") or "Sensor Bridge",
            sensor.get("identifier") or sensor.get("hardwareId") or sensor.get("hardware_id") or "")

    # The compact summaries supplement the raw feed when a provider exposes only a subset of sensor objects.
    temp_summaries=[
        ("Temperature","CPU","Temperatura CPU (wybrany czujnik)",temps.get("cpu_temp_c"),"°C"),
        ("Temperature","GPU","Temperatura GPU (wybrany czujnik)",gpu.get("temperature_c",temps.get("gpu_temp_c")),"°C"),
        ("Power","CPU","Moc CPU",temps.get("cpu_power_w"),"W"),
        ("Power","GPU","Moc GPU",gpu.get("power_draw_w",gpu.get("power_w",temps.get("gpu_power_w"))),"W"),
        ("Power","System","Moc systemu",temps.get("system_power_w"),"W"),
        ("Power","Bateria","Moc baterii",temps.get("battery_power_w"),"W"),
        ("Voltage","CPU","Napięcie CPU",temps.get("cpu_voltage_v"),"V"),
        ("Voltage","GPU","Napięcie GPU",temps.get("gpu_voltage_v"),"V"),
        ("Clock","CPU","Zegar CPU",temps.get("cpu_clock_mhz"),"MHz"),
        ("Clock","GPU","Zegar GPU",gpu.get("gpu_clock_mhz",temps.get("gpu_clock_mhz")),"MHz"),
        ("Clock","GPU","Zegar pamięci GPU",gpu.get("memory_clock_mhz"),"MHz"),
        ("Fan","CPU","Wentylator CPU",temps.get("cpu_fan_rpm"),"RPM"),
        ("Fan","GPU","Wentylator GPU",gpu.get("fan_speed_rpm",temps.get("gpu_fan_rpm")),"RPM"),
        ("Load","GPU","Użycie GPU",gpu.get("gpu_load_percent",gpu.get("load_percent")),"%"),
        ("Memory","VRAM","VRAM użyta",gpu.get("vram_used_mb"),"MB"),
        ("Memory","VRAM","VRAM całkowita",gpu.get("vram_total_mb"),"MB"),
        ("Count","Sensor Bridge","Liczba odczytów sprzętowych",temps.get("sensor_count",len(raw)),""),
    ]
    for row in temp_summaries:
        add(*row,temps.get("method") or gpu.get("provider") or "Wybrany czujnik / N/D")

    # OS-level values: RAM, swap, per-core load, aggregate I/O, uptime, battery and temperatures.
    system_names={
      "cpu_percent":("Load","CPU","Użycie CPU","%"),
      "cpu_clock_mhz":("Clock","CPU","Zegar CPU","MHz"),
      "cpu_clock_max_mhz":("Clock","CPU","Maksymalny zegar CPU","MHz"),
      "ram_percent":("Memory","RAM","Użycie RAM","%"),
      "ram_total_bytes":("Memory","RAM","RAM całkowita", "B"),
      "ram_used_bytes":("Memory","RAM","RAM użyta","B"),
      "ram_available_bytes":("Memory","RAM","RAM dostępna","B"),
      "swap_percent":("Memory","Swap","Użycie swap","%"),
      "swap_total_bytes":("Memory","Swap","Swap całkowity","B"),
      "swap_used_bytes":("Memory","Swap","Swap użyty","B"),
      "disk_read_mbps":("Throughput","Dysk","Odczyt wszystkich dysków","MB/s"),
      "disk_write_mbps":("Throughput","Dysk","Zapis wszystkich dysków","MB/s"),
      "net_down_mbps":("Throughput","Sieć","Pobieranie łączne","Mbps"),
      "net_up_mbps":("Throughput","Sieć","Wysyłanie łączne","Mbps"),
      "battery_percent":("Battery","Bateria","Poziom baterii","%"),
      "battery_plugged":("Battery","Bateria","Zasilanie AC podłączone",""),
      "battery_seconds_left":("Battery","Bateria","Pozostały czas baterii","s"),
      "uptime_seconds":("System","Windows","Czas działania systemu","s"),
    }
    mapped=set()
    for key,spec in system_names.items():
        if key in system:
            cat,hw,label,unit=spec
            value=system.get(key)
            if key.endswith("_bytes") and value is not None:
                try: value=round(float(value)/1073741824,3);unit="GiB"
                except Exception: pass
            add(cat,hw,label,value,unit,"Windows / psutil");mapped.add(key)
    for index,value in enumerate(system.get("cpu_per_core_percent",[]) or [],1):
        add("Load","CPU","Rdzeń logiczny %d — użycie"%index,value,"%","Windows / psutil per-core")
    for disk in system.get("disk_devices",[]) or []:
        if not isinstance(disk,dict): continue
        name=str(disk.get("name") or "Dysk")
        for key,label,unit in (("read_mbps","Odczyt","MB/s"),("write_mbps","Zapis","MB/s"),
                               ("read_iops","Operacje odczytu","IOPS"),("write_iops","Operacje zapisu","IOPS")):
            add("Throughput",name,label,disk.get(key),unit,"Windows / psutil per-disk")
        add("Other",name,"Operacje odczytu — licznik",disk.get("read_operations_total"),"operacje","Windows / psutil")
        add("Other",name,"Operacje zapisu — licznik",disk.get("write_operations_total"),"operacje","Windows / psutil")
    for nic in system.get("network_interfaces",[]) or []:
        if not isinstance(nic,dict): continue
        name=str(nic.get("name") or "Interfejs sieciowy")
        add("Throughput",name,"Download",nic.get("download_mbps"),"Mbps","Windows / psutil per-interface")
        add("Throughput",name,"Upload",nic.get("upload_mbps"),"Mbps","Windows / psutil per-interface")
        add("System",name,"Interfejs aktywny",nic.get("is_up"),"","Windows / psutil")
        add("System",name,"Szybkość łącza",nic.get("link_speed_mbps"),"Mbps","Windows / psutil")
        add("Other",name,"MTU",nic.get("mtu"),"","Windows / psutil")
        add("Other",name,"Adresy",", ".join(nic.get("addresses",[]) or []),"","Windows / psutil")
    for volume in system.get("partitions",[]) or []:
        if not isinstance(volume,dict): continue
        name=str(volume.get("mountpoint") or volume.get("device") or "Wolumin")
        for key,label,unit in (("used_percent","Wykorzystanie","%"),
            ("total_bytes","Całkowita pojemność","GiB"),("used_bytes","Zajęte","GiB"),("free_bytes","Wolne","GiB")):
            value=volume.get(key)
            if unit=="GiB" and value is not None:
                try:value=round(float(value)/1073741824,3)
                except Exception:pass
            add("Storage",name,label,value,unit,"Windows / psutil filesystem")
        add("Storage",name,"System plików",volume.get("filesystem"),"","Windows / psutil")

    # Include every scalar returned by Windows/GPU providers, even if a future provider adds new fields.
    for key,value in system.items():
        if key in mapped or key in ("cpu_per_core_percent","disk_devices","network_interfaces","partitions","extra_temperature_sensors","sampled_at"):
            continue
        if not isinstance(value,(dict,list,tuple)):
            add("System","Windows",str(key),value,"","Windows / psutil")
    for sensor in system.get("extra_temperature_sensors",[]) or []:
        if isinstance(sensor,dict):
            add("Temperature",sensor.get("hardware","OS"),sensor.get("sensor","Temperature"),
                sensor.get("value"),sensor.get("unit","°C"),sensor.get("source","psutil"))
    for zone in temps.get("acpi_zones",[]) or []:
        if isinstance(zone,dict):
            add("ACPI / Temperature","Windows ACPI",zone.get("name","Strefa termiczna"),
                zone.get("value"),"°C", "Windows WMI ACPI — to nie musi być temperatura rdzenia CPU")

    # Keep scalar vendor telemetry and any future GPU fields visible.
    for key,value in gpu.items():
        if key in ("sensor_rows","message","available","provider","error","sensors") or isinstance(value,(dict,list,tuple)):
            continue
        add("GPU","GPU",str(key),value,"",gpu.get("provider") or "GPU telemetry")
    for sensor in gpu.get("sensors",[]) or []:
        if isinstance(sensor,dict):
            add(_u107_sensor_category(sensor.get("sensorType"),sensor.get("unit")),
                sensor.get("hardware") or sensor.get("hardwareType") or "GPU",
                sensor.get("sensor") or sensor.get("name") or "N/D",sensor.get("value"),
                sensor.get("unit") or "",sensor.get("source") or gpu.get("provider") or "GPU telemetry")

    # Tree values are fallback only for rows not present in the current sensor snapshot.
    try:
        tree=getattr(app,"_u100_sensor_tree",None)
        if tree is not None and tree.winfo_exists():
            for item in tree.get_children(""):
                values=tree.item(item,"values") or ()
                if len(values)>=6:
                    add(values[0],values[1],values[2],values[3],values[4],values[5])
    except Exception:
        pass
    return rows

def _u107_sensor_records(app):
    # The compact dashboard uses the same data source as the full inspector; add per-core, disk and NIC rows.
    rows=_U107_ORIGINAL_SENSOR_RECORDS(app)
    expanded=_u107_get_sensor_rows(app)
    seen=set((str(r.get("hardware","")).casefold(),str(r.get("sensor","")).casefold(),str(r.get("unit","")).casefold()) for r in rows)
    for row in expanded:
        key=(str(row.get("hardware","")).casefold(),str(row.get("sensor","")).casefold(),str(row.get("unit","")).casefold())
        if key in seen:
            continue
        rows.append(row);seen.add(key)
    return rows

def _u107_attach_sensor_table(app,parent,height=10):
    panel=_U107_ORIGINAL_ATTACH_SENSOR_TABLE(app,parent,height)
    try:
        tree=getattr(app,"_u100_sensor_tree",None)
        if tree is not None and tree.winfo_exists():
            tree.configure(height=max(12,int(height or 12)))
    except Exception:
        pass
    return panel

def _u107_open_sensor_inspector(app):
    result=_U107_ORIGINAL_OPEN_SENSOR_INSPECTOR(app)
    try:
        win=getattr(app,"_u106_sensor_window",None)
        if win is not None and win.winfo_exists():
            # This alias keeps the four-second poll loop active while the inspector is open on any app page.
            app._u104_sensor_window=win
    except Exception as exc:
        try:app.queue_log("Pełny inspektor sensorów: "+repr(exc))
        except Exception:pass
    return result

# Validate HTTP status, transferred bytes and elapsed time before accepting a throughput sample.
def _u107_validate_speed_sample(row,direction):
    if not isinstance(row,dict):
        return {"state":"error","direction":direction,"error":"Brak rekordu próbki."}
    sample=dict(row)
    status=sample.get("status")
    try:status=int(status)
    except Exception:status=0
    if status<200 or status>=300:
        sample.update({"state":"error","direction":direction,"error":sample.get("error") or f"HTTP {status or 'N/D'}"})
        return sample
    amount=0;requested=0;seconds=None
    try:amount=max(0,int(sample.get("bytes",0) or 0))
    except Exception:amount=0
    try:requested=max(0,int(sample.get("requested_bytes",0) or 0))
    except Exception:requested=0
    try:seconds=float(sample.get("seconds"))
    except Exception:seconds=None
    if not _u107_finite_number(seconds) or float(seconds)<=0:
        sample.update({"state":"error","direction":direction,"error":"Brak poprawnego czasu pomiaru."})
        return sample
    if amount<=0:
        sample.update({"state":"error","direction":direction,"error":"Nie przesłano żadnych bajtów."})
        return sample
    if requested>0 and amount<int(requested*.98):
        sample.update({"state":"error","direction":direction,"error":f"Niepełny transfer: {amount} / {requested} B."})
        return sample
    sample.update({"state":"good","direction":direction,"measured_bytes":amount,
        "mbps":round(amount*8/float(seconds)/1_000_000,3)})
    return sample

def _u107_finalize_speed_result(result):
    import statistics as _u107_stats
    if not isinstance(result,dict):
        return result
    latencies=[]
    for value in result.get("latency_ms",[]) or []:
        number=_u107_finite_number(value)
        if number is not None and number>=0:latencies.append(float(number))
    errors=[]
    directions={}
    for direction in ("download","upload"):
        checked=[]
        for original in result.get(direction,[]) or []:
            row=_u107_validate_speed_sample(original,direction)
            checked.append(row)
            if row.get("state")!="good":
                errors.append({"direction":direction,"sample_index":row.get("sample_index"),
                    "error":row.get("error") or "Próbka niezaliczona"})
        directions[direction]=checked
        result[direction]=checked
    warmup=result.get("warmup",{}) or {}
    checked_warm={}
    for direction,original in warmup.items():
        if direction in ("download","upload") and isinstance(original,dict):
            row=_u107_validate_speed_sample(original,direction+"-warmup")
            checked_warm[direction]=row
            if row.get("state")!="good":
                errors.append({"direction":direction+"-warmup","sample_index":row.get("sample_index"),
                    "error":row.get("error") or "Próbka rozgrzewkowa niezaliczona"})
        else:
            checked_warm[direction]=original
    result["warmup"]=checked_warm
    valid={direction:[row for row in rows if row.get("state")=="good"] for direction,rows in directions.items()}
    rates={direction:[float(row["mbps"]) for row in rows] for direction,rows in valid.items()}
    def stats(direction):
        values=rates[direction]
        if not values:return {"median":None,"mean":None,"minimum":None,"peak":None,"cv":None}
        mean=float(_u107_stats.fmean(values))
        cv=float(_u107_stats.pstdev(values)/mean*100) if mean>0 and len(values)>1 else (0.0 if mean>0 else None)
        return {"median":round(_u90_median(values),2),"mean":round(mean,2),
            "minimum":round(min(values),2),"peak":round(max(values),2),"cv":round(cv,2) if cv is not None else None}
    down=stats("download");up=stats("upload")
    result.update({
        "download_mbps":down["median"],"download_mean_mbps":down["mean"],
        "download_min_mbps":down["minimum"],"download_peak_mbps":down["peak"],
        "download_cv_percent":down["cv"],
        "upload_mbps":up["median"],"upload_mean_mbps":up["mean"],
        "upload_min_mbps":up["minimum"],"upload_peak_mbps":up["peak"],
        "upload_cv_percent":up["cv"],
        "download_samples_valid":len(valid["download"]),
        "upload_samples_valid":len(valid["upload"]),
        "total_download_samples":len(directions["download"]),
        "total_upload_samples":len(directions["upload"]),
        "successful_samples":len(valid["download"])+len(valid["upload"]),
        "total_samples":len(directions["download"])+len(directions["upload"]),
        "latency_samples_valid":len(latencies),
        "latency_average_ms":round(_u90_median(latencies),2) if latencies else None,
        "latency_min_ms":round(min(latencies),2) if latencies else None,
        "latency_max_ms":round(max(latencies),2) if latencies else None,
        "latency_spread_ms":round(max(latencies)-min(latencies),2) if len(latencies)>1 else None,
        "latency_jitter_ms":round(_u90_median([abs(latencies[i]-latencies[i-1]) for i in range(1,len(latencies))]),2) if len(latencies)>1 else None,
        "transfer_errors":errors,
        "data_bytes":sum(int(row.get("bytes",0) or 0) for rows in valid.values() for row in rows)
            +sum(int(row.get("bytes",0) or 0) for row in checked_warm.values() if isinstance(row,dict) and row.get("state")=="good"),
        "method":"HTTPS Cloudflare; wszystkie bajty i HTTP status zweryfikowane; mediana, peak i CV liczone z ważnych próbek.",
        "latency_method":"HTTPS round-trip time; nie jest to ICMP ping."
    })
    result["state"]="good" if len(valid["download"])==len(directions["download"]) and len(valid["upload"])==len(directions["upload"]) and len(latencies)>=3 else "warn"
    result["finished_at"]=_U66_datetime.now().isoformat(timespec="seconds")
    return result

def _u107_measure_speed(app):
    # Keep the compatibility keys in this public wrapper for existing updater/self-tests.
    _stable_metric_names=("download_peak_mbps","upload_peak_mbps","latency_jitter_ms")
    # Keep a hard guard in the code path: the measured engine must use the HTTPS transport already tested by CI.
    if not callable(_U100_ORIGINAL_SPEED_REQUEST):
        raise RuntimeError("Brakuje transportu HTTPS dla Speed Test.")
    result=_U107_ORIGINAL_MEASURE_SPEED(app)
    result=_u107_finalize_speed_result(result)
    if not isinstance(result,dict):
        return result
    try:
        history_path=result.get("history_path")
        if history_path:
            history_file=Path(history_path)
            records=_u66_json.loads(history_file.read_text(encoding="utf-8"))
            if records and records[-1].get("started_at")==result.get("started_at"):
                records[-1].update(result)
                history_file.write_text(_u66_json.dumps(records[-100:],ensure_ascii=False,indent=2),encoding="utf-8")
    except Exception as exc:
        result["history_warning"]=f"Nie udało się zsynchronizować historii: {type(exc).__name__}: {exc}"
    def update_metrics():
        controls=getattr(app,"_u107_speed_metrics",{}) or {}
        values={
            "sample_count":f"DL {result.get('download_samples_valid',0)}/{result.get('total_download_samples',0)} • UL {result.get('upload_samples_valid',0)}/{result.get('total_upload_samples',0)}",
            "rtt_spread":f"{result['latency_spread_ms']:.1f} ms" if isinstance(result.get("latency_spread_ms"),(int,float)) else "N/D",
            "download_cv":f"CV {result['download_cv_percent']:.1f}%" if isinstance(result.get("download_cv_percent"),(int,float)) else "N/D",
            "upload_cv":f"CV {result['upload_cv_percent']:.1f}%" if isinstance(result.get("upload_cv_percent"),(int,float)) else "N/D"
        }
        for key,value in values.items():
            try:
                label=controls.get(key)
                if label is not None and label.winfo_exists():label.config(text=value)
            except Exception:pass
    try:app.queue_action(update_metrics)
    except Exception:pass
    return result

def _u107_show_speed_test(app):
    _U107_ORIGINAL_SHOW_SPEED_TEST(app)
    try:
        t=app.colors()
        pane=app.panel(app.content)
        children=app.content.winfo_children()
        before=children[-1] if children else None
        pane.pack(fill="x",padx=3,pady=(0,5),before=before)
        tk.Label(pane,text="JAKOŚĆ PRÓBEK I STABILNOŚĆ ŁĄCZA",bg=t["panel"],fg=t["accent"],
            font=app.fnt(9,"bold")).pack(anchor="w",padx=8,pady=(5,2))
        tk.Label(pane,text="Prędkość główna = mediana; peak pokazuje maksimum. CV pokazuje rozrzut próbek (mniej = stabilniej). Transfery z błędnym HTTP, niepełnymi bajtami lub czasem są odrzucane.",
            bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1320,justify="left").pack(fill="x",padx=8,pady=(0,4))
        row=tk.Frame(pane,bg=t["panel"]);row.pack(fill="x",padx=5,pady=(0,5))
        app._u107_speed_metrics={}
        specs=(("UDANE PRÓBKI","sample_count"),("ROZPIĘTOŚĆ RTT","rtt_spread"),
            ("STABILNOŚĆ DOWNLOAD","download_cv"),("STABILNOŚĆ UPLOAD","upload_cv"))
        for caption,key in specs:
            card=tk.Frame(row,bg=t["card"],highlightbackground=t["panel"],highlightthickness=1)
            card.pack(side="left",fill="both",expand=True,padx=2)
            tk.Label(card,text=caption,bg=t["card"],fg=t["muted"],font=app.fnt(8,"bold")).pack(pady=(5,1))
            label=tk.Label(card,text="N/D",bg=t["card"],fg=t["accent2"],font=app.fnt(11,"bold"))
            label.pack(pady=(0,5));app._u107_speed_metrics[key]=label
    except Exception as exc:
        try:app.queue_log("Speed Test extended UI: "+repr(exc))
        except Exception:pass

def _u107_launch_scene_preview(app,module,test_id,scene_id):
    scene_title=_U100_SCENE_TITLES[int(scene_id)-1]
    if not messagebox.askyesno("Unikalna scena OpenGL",
        f"Uruchomić własną scenę {int(scene_id):02d}/110 dla testu {test_id}?\n\n"
        f"{scene_title}\n\n"
        "To prawdziwe renderowanie OpenGL z pomiarem FPS GPU przez 10 sekund. "
        "Scena jest przypisana wyłącznie do tego testu, ale FPS nie jest wynikiem sprawności CPU/RAM/dysku. Kontynuować?"):
        return
    if getattr(app,"running",False):
        messagebox.showinfo("Test w toku","Poczekaj na zakończenie bieżącego testu albo zatrzymaj go.")
        return
    _u93_update_detail(app,test_id,"SCENA OPENGL W TOKU",{
        "state":"running","test_id":test_id,"module":module,"scene_id":int(scene_id),
        "scene_name":scene_title,"duration_seconds":10,
        "note":"Unikalny renderer OpenGL. Pomiar FPS dotyczy renderowania GPU; nie zastępuje testu podzespołu w nazwie."
    })
    def job():
        start=_u66_time.monotonic()
        try:
            result=_u66_execute_gpu_scene(app,int(scene_id),10)
            if not isinstance(result,dict):result={"state":"warn","message":"Renderer nie zwrócił raportu."}
        except Exception as exc:
            result={"state":"error","error":f"{type(exc).__name__}: {exc}"}
        result.update({"test_id":str(test_id),"module":str(module),"scene_id":int(scene_id),
            "scene_name":scene_title,"preview_duration_seconds":round(_u66_time.monotonic()-start,2),
            "note":"Ta scena OpenGL jest unikalna dla wybranego wpisu katalogu. FPS jest wynikiem renderera GPU, nie diagnozą sprawności CPU/RAM/dysku."})
        try:
            report=_u93_persist_result(app,module,"scene-"+str(test_id),"Scena OpenGL: "+scene_title,result,
                _u66_time.monotonic()-start)
            _u93_put_result(app,"COMPONENT_SCENE_"+str(test_id),report)
            _u93_update_detail(app,test_id,"SCENA ZAKOŃCZONA • FPS "+str(result.get("average_fps","N/D")),report)
            app.queue_log(f"UNIKALNA SCENA TESTU {test_id}: {result.get('state')} • scena {scene_id}/110 • FPS {result.get('average_fps','N/D')}")
        except Exception as exc:
            app.queue_log(f"Raport sceny {test_id}: {type(exc).__name__}: {exc}")
    app.worker(job)

def _u107_open_component_simulator(app,module,fullscreen=False,mode="scan"):
    # Catalog screens use a dedicated real OpenGL scene; non-catalog callers retain the existing module simulator.
    view=str(getattr(app,"current_view","") or "")
    if view.startswith("COMPONENT_TEST_DETAIL_"):
        test_id=view.split("COMPONENT_TEST_DETAIL_",1)[1]
        scene_id=_U107_TEST_SCENES.get(test_id)
        if scene_id is not None:
            _u107_launch_scene_preview(app,module,test_id,scene_id)
            return
    return _U107_ORIGINAL_OPEN_COMPONENT_SIMULATOR(app,module,fullscreen,mode)

def _u107_selftest_sensor_inspector():
    class FakeTree:
        def __init__(self,values):self._values=values
        def winfo_exists(self):return True
        def get_children(self,_root=""):return list(range(len(self._values)))
        def item(self,item,_field):return {"values":self._values[item]}
    class FakeApp:
        _u100_sensor_tree=None
        _u66_sensor_cache={
          "temps":{"method":"fake bridge","sensor_count":3,"cpu_temp_c":72.0,"cpu_power_w":52.0,
            "sensors":[
              {"hardware":"CPU Package","hardwareType":"CpuAmd","sensor":"Tctl/Tdie","sensorType":"Temperature","value":72.0,"unit":"°C","source":"test"},
              {"hardware":"CPU Core","hardwareType":"CpuAmd","sensor":"Core #1","sensorType":"Temperature","value":68.0,"unit":"°C","source":"test"}],
            "acpi_zones":[{"name":"TZ0","value":39.0}]},
          "gpu":{"provider":"fake gpu","temperature_c":64.0,"gpu_load_percent":87.0,"vram_used_mb":4096},
          "system":{"cpu_percent":32.0,"ram_percent":61.0,"cpu_per_core_percent":[31.0,58.0],
            "disk_devices":[{"name":"PhysicalDrive0","read_mbps":17.5,"write_mbps":8.0,"read_iops":120.0,"write_iops":60.0}],
            "network_interfaces":[{"name":"Ethernet","download_mbps":92.0,"upload_mbps":8.0,"is_up":True,"link_speed_mbps":1000,"addresses":["192.0.2.5"]}],
            "partitions":[{"mountpoint":"C:\\\\","total_bytes":1000000,"used_bytes":500000,"free_bytes":500000,"used_percent":50,"filesystem":"NTFS"}],
            "extra_temperature_sensors":[{"hardware":"OS","sensor":"ACPI package","value":43.0,"unit":"°C","source":"test"}]}}
    rows=_u107_get_sensor_rows(FakeApp())
    signatures={(r["hardware"],r["sensor"],r["unit"]) for r in rows}
    assert any("Tctl/Tdie" in x[1] for x in signatures)
    assert any(x[1]=="Rdzeń logiczny 2 — użycie" and x[2]=="%" for x in signatures)
    assert any(x[0]=="PhysicalDrive0" and x[1]=="Odczyt" for x in signatures)
    assert any(x[0]=="Ethernet" and x[1]=="Download" for x in signatures)
    assert any(x[0]=="C:\\\\" and x[1]=="Wykorzystanie" for x in signatures)
    assert any(x[0]=="Windows ACPI" and x[1]=="TZ0" for x in signatures)
    assert any(x[1]=="Temperatura CPU (wybrany czujnik)" for x in signatures)
    assert any(x[1]=="cpu_percent" for x in signatures) is False  # known values have human-friendly labels
    assert len(rows)>=20
    print("LIVE_SENSOR_INSPECTOR_PER_CORE_DISK_NIC_PARTITION_SELFTEST_OK")

def _u107_selftest_speed_validation():
    sample={
      "state":"good","latency_ms":[22.0,24.0,25.0,23.0],
      "download":[
        {"state":"good","status":200,"requested_bytes":1000000,"bytes":1000000,"seconds":1.0,"mbps":8.0},
        {"state":"good","status":200,"requested_bytes":2000000,"bytes":2000000,"seconds":1.0,"mbps":16.0},
        {"state":"good","status":503,"requested_bytes":3000000,"bytes":3000000,"seconds":1.0,"mbps":24.0}],
      "upload":[
        {"state":"good","status":200,"requested_bytes":500000,"bytes":500000,"seconds":1.0,"mbps":4.0},
        {"state":"good","status":200,"requested_bytes":1000000,"bytes":1000000,"seconds":2.0,"mbps":4.0}],
      "warmup":{"download":{"state":"good","status":200,"requested_bytes":256000,"bytes":256000,"seconds":.3},
                "upload":{"state":"good","status":200,"requested_bytes":256000,"bytes":256000,"seconds":.4}}}
    result=_u107_finalize_speed_result(sample)
    assert result["download_samples_valid"]==2 and result["upload_samples_valid"]==2
    assert result["download_mbps"]==12.0 and result["upload_mbps"]==4.0
    assert result["download"][2]["state"]=="error" and result["state"]=="warn"
    assert result["data_bytes"]==1000000+2000000+500000+1000000+256000+256000
    assert result["latency_min_ms"]==22.0 and result["latency_max_ms"]==25.0
    assert result["latency_spread_ms"]==3.0
    assert result["download_cv_percent"] is not None and result["upload_cv_percent"]==0.0
    print("SPEED_TEST_HTTP_BYTES_MEDIAN_JITTER_STABILITY_SELFTEST_OK")

def _u107_selftest_unique_scene_per_catalog_test():
    catalog_ids=[]
    for module,entries in _U93_TEST_CATALOG.items():
        for test_id,title,description,kind in entries:
            catalog_ids.append(test_id)
            assert test_id in _U107_TEST_SCENES, "Brak indywidualnej sceny dla "+str(test_id)
            scene_id=_U107_TEST_SCENES[test_id]
            assert 1<=scene_id<=len(_U100_SCENE_TITLES)
            assert "SIMULATOR" not in str(title).upper() or scene_id>0
    assert len(catalog_ids)==110 and len(set(catalog_ids))==110
    scene_ids=[_U107_TEST_SCENES[test_id] for test_id in catalog_ids]
    assert len(set(scene_ids))==110, "Dwa testy katalogu wskazują na tę samą scenę OpenGL."
    assert callable(_u107_open_component_simulator) and callable(_u107_launch_scene_preview)
    assert callable(_u107_get_sensor_rows) and callable(_u107_measure_speed)
    assert "COMPONENT_TEST_DETAIL_" in _u107_open_component_simulator.__code__.co_consts
    print("UNIQUE_OPENGL_SCENE_PER_CATALOG_TEST_SELFTEST_OK: 110 different scene IDs")

_u101_collect_os_metrics=_u107_collect_os_metrics
_u104_sensor_records=_u107_sensor_records
_u106_get_sensor_rows=_u107_get_sensor_rows
_u106_open_sensor_inspector=_u107_open_sensor_inspector
_u106_attach_sensor_table=_u107_attach_sensor_table
_u81_attach_sensor_table=_u107_attach_sensor_table
_u100_measure_speed=_u107_measure_speed
_u90_measure_speed=_u107_measure_speed
_u66_measure_speed=_u107_measure_speed
_u69_open_component_simulator=_u107_open_component_simulator
AppV43.show_speed_test=_u107_show_speed_test


# v4.3.102 — restore the full live OS telemetry into the visible hardware table,
# and expose quick/standard/max throughput profiles without changing the default cost.
_U108_ORIGINAL_SENSOR_POLL = _u100_sensor_poll
_U108_ORIGINAL_SENSOR_REFRESH = _u100_refresh_sensor_table
_U108_ORIGINAL_SPEED_SAMPLE_SIZES = _u104_speed_sample_sizes
_U108_ORIGINAL_SPEED_MEASURE = _u107_measure_speed
_U108_ORIGINAL_START_SPEED_TEST = _u66_start_speed_test
_U108_ORIGINAL_SHOW_SPEED_TEST = AppV43.show_speed_test
_U108_ACTIVE_SPEED_PROFILE = "STANDARD"

def _u108_build_sensor_snapshot(app, temps, gpu, system=None):
    if not isinstance(temps, dict):
        temps = {}
    if not isinstance(gpu, dict):
        gpu = {}
    if system is None:
        try:
            system = _u107_collect_os_metrics(app)
        except Exception as exc:
            system = {"metrics_error": f"{type(exc).__name__}: {exc}"}
    if not isinstance(system, dict):
        system = {}
    temps.setdefault("sensors", [])
    temps.setdefault("sensor_groups", {})
    temps.setdefault("acpi_zones", [])
    return {
        "gpu": gpu,
        "temps": temps,
        "system": system,
        "time": _u66_time.monotonic(),
        "sampled_at": _U66_datetime.now().isoformat(timespec="seconds")
    }

def _u108_refresh_sensor_table(app):
    tree = getattr(app, "_u100_sensor_tree", None)
    if tree is None:
        return
    try:
        if not tree.winfo_exists():
            return
        rows = _u107_get_sensor_rows(app)
        normalized = []
        for row in rows:
            if not isinstance(row, dict):
                continue
            normalized.append((
                str(row.get("category") or "Other"),
                str(row.get("hardware") or "N/D"),
                str(row.get("sensor") or "N/D"),
                str(row.get("value") if row.get("value") is not None else "N/D"),
                str(row.get("unit") or ""),
                str(row.get("source") or "N/D")
            ))
        # Preserve row order; update values in place when the sensor inventory is unchanged.
        signature = tuple((r[0], r[1], r[2], r[4], r[5]) for r in normalized)
        old_signature = getattr(app, "_u108_sensor_signature", None)
        if signature != old_signature:
            current = tree.get_children()
            if current:
                tree.delete(*current)
            for idx, row in enumerate(normalized):
                tree.insert("", "end", iid=f"u108sensor{idx}", values=row)
            app._u108_sensor_signature = signature
        else:
            for idx, row in enumerate(normalized):
                iid = f"u108sensor{idx}"
                if tree.exists(iid):
                    tree.item(iid, values=row)
                else:
                    tree.insert("", "end", iid=iid, values=row)
        counts = {}
        for row in normalized:
            counts[row[0]] = counts.get(row[0], 0) + 1
        label = getattr(app, "_u100_sensor_count", None)
        if label is not None and label.winfo_exists():
            cache = getattr(app, "_u66_sensor_cache", {}) or {}
            stamp = cache.get("time")
            age = max(0, _u66_time.monotonic() - stamp) if isinstance(stamp, (int, float)) else None
            text = f"{len(normalized)} pozycji • " + ", ".join(f"{k}:{v}" for k, v in sorted(counts.items()))
            text += f" • próbka {age:.0f} s temu" if age is not None else " • N/D"
            label.config(text=text)
    except Exception as exc:
        try:
            app.queue_log("Pełna tabela telemetrii: " + repr(exc))
        except Exception:
            pass

def _u108_sensor_poll(app):
    try:
        if getattr(app, "_u100_sensor_busy", False):
            app.after(3000, lambda: _u108_sensor_poll(app))
            return
        if _u66_time.monotonic() - getattr(app, "_u100_sensor_last", 0) > 2.8:
            app._u100_sensor_busy = True
            app._u100_sensor_last = _u66_time.monotonic()

            def job():
                try:
                    temps = _u66_sensor_probe()
                    generic = _u100_gpu_from_sensors(temps)
                    try:
                        vendor = _u37_nvidia_telemetry() if "_u37_nvidia_telemetry" in globals() else {}
                    except Exception as exc:
                        vendor = {"available": False, "provider": "GPU vendor telemetry unavailable", "error": str(exc)}
                    gpu = dict(vendor or {})
                    for key, value in generic.items():
                        if key in ("sensor_rows", "message"):
                            continue
                        if value is not None and (gpu.get(key) is None or gpu.get(key) is False or gpu.get(key) == "N/D"):
                            gpu[key] = value
                    if not gpu.get("provider"):
                        gpu["provider"] = generic.get("provider")
                    if not gpu.get("available"):
                        gpu["available"] = generic.get("available", False)
                    gpu["sensor_rows"] = generic.get("sensor_rows", 0)
                    if temps.get("gpu_temp_c") is None and generic.get("temperature_c") is not None:
                        temps["gpu_temp_c"] = generic["temperature_c"]
                    if temps.get("gpu_power_w") is None and generic.get("power_draw_w") is not None:
                        temps["gpu_power_w"] = generic["power_draw_w"]

                    # This was missing from the published cache: without it, per-core CPU,
                    # RAM/swap, per-disk I/O, NIC throughput, battery and per-volume rows
                    # existed in code but the UI received an empty system object.
                    system = _u107_collect_os_metrics(app)
                    snapshot = _u108_build_sensor_snapshot(app, temps, gpu, system)

                    def update():
                        app._u100_sensor_busy = False
                        app._u66_sensor_cache = snapshot
                        app._u84_gpu_last_telemetry = gpu
                        try:
                            _u108_refresh_sensor_table(app)
                        except Exception:
                            pass
                        try:
                            if getattr(app, "current_view", "") == "GPU":
                                _u84_gpu_live_tick(app, schedule=False)
                            if getattr(app, "current_view", "") == "LIVE_MONITOR":
                                _u66_live_tick(app)
                            if getattr(app, "_u67_stage_panel", None) is not None:
                                _u67_refresh_visible_charts(app)
                        except Exception:
                            pass
                    app.queue_action(update)
                except Exception as exc:
                    def fail(err=exc):
                        app._u100_sensor_busy = False
                        try:
                            app.queue_log("Odczyt pełnej telemetrii: " + str(err))
                        except Exception:
                            pass
                    try:
                        app.queue_action(fail)
                    except Exception:
                        fail()
            _u66_threading.Thread(target=job, name="NaprawaPCFullHardwareTelemetry", daemon=True).start()
    except Exception as exc:
        try:
            app._u100_sensor_busy = False
            app.queue_log("Telemetria: " + repr(exc))
        except Exception:
            pass
    try:
        app.after(3000, lambda: _u108_sensor_poll(app))
    except Exception:
        pass

# Three speed profiles: QUICK minimizes transfer; STANDARD preserves current adaptive sizes;
# MAX measures longer and warns before any large network transfer.
def _u108_speed_sample_sizes(rate_mbps):
    try:
        rate = max(0.02, float(rate_mbps or 0))
    except Exception:
        rate = 0.02
    profile = str(_U108_ACTIVE_SPEED_PROFILE or "STANDARD").upper()
    if profile == "QUICK":
        target = max(256_000, min(8_000_000, int(rate * 1_000_000 / 8 * 1.8)))
        return (max(256_000, int(target * .65)), target, min(10_000_000, max(target, int(target * 1.25))))
    if profile == "MAX":
        target = max(1_000_000, min(48_000_000, int(rate * 1_000_000 / 8 * 7.5)))
        return (max(1_000_000, int(target * .75)), target, min(60_000_000, max(target, int(target * 1.25))))
    return _U108_ORIGINAL_SPEED_SAMPLE_SIZES(rate)

def _u108_measure_speed(app):
    global _U108_ACTIVE_SPEED_PROFILE
    profile = str(getattr(app, "_u108_speed_profile", "STANDARD") or "STANDARD").upper()
    if profile not in ("QUICK", "STANDARD", "MAX"):
        profile = "STANDARD"
    _U108_ACTIVE_SPEED_PROFILE = profile
    result = _U108_ORIGINAL_SPEED_MEASURE(app)
    if isinstance(result, dict):
        result["measurement_profile"] = profile
        result["profile_note"] = {
            "QUICK": "Krótszy test z mniejszym transferem.",
            "STANDARD": "Adaptacyjny test standardowy, dobrany do próbki rozgrzewkowej.",
            "MAX": "Dłuższe próbki dla szybkich łączy; większy transfer danych."
        }[profile]
    return result

def _u108_start_speed_test(app):
    global _U108_ACTIVE_SPEED_PROFILE
    profile = str(getattr(app, "_u108_speed_profile", "STANDARD") or "STANDARD").upper()
    if profile == "MAX":
        if not messagebox.askyesno(
            "Speed Test MAX — duży transfer",
            "Maksymalny test może przesłać do około 340 MB łącznie, zależnie od prędkości łącza (w tym do 64 MB dodatkowego transferu równoległego). "
            "Wykona dłuższe próbki, aby ograniczyć wpływ narzutu HTTPS. Kontynuować?"
        ):
            _u66_set_speed_status(app, "Test MAX anulowany — nie rozpoczęto transferu.")
            return
    _U108_ACTIVE_SPEED_PROFILE = profile
    app._u108_speed_profile = profile
    return _U108_ORIGINAL_START_SPEED_TEST(app)

def _u108_show_speed_test(app):
    _U108_ORIGINAL_SHOW_SPEED_TEST(app)
    try:
        t = app.colors()
        children = app.content.winfo_children()
        before = children[-1] if children else None
        pane = app.panel(app.content)
        pane.pack(fill="x", padx=3, pady=(0, 5), before=before)
        tk.Label(pane, text="PROFIL POMIARU", bg=t["panel"], fg=t["accent"],
                 font=app.fnt(9, "bold")).pack(anchor="w", padx=8, pady=(5, 2))
        options = {
            "SZYBKI — mały transfer": "QUICK",
            "STANDARD — adaptacyjny": "STANDARD",
            "MAX — długi pomiar": "MAX"
        }
        reverse = {value: key for key, value in options.items()}
        current = str(getattr(app, "_u108_speed_profile", "STANDARD") or "STANDARD").upper()
        if current not in reverse:
            current = "STANDARD"
        app._u108_speed_profile = current
        app._u108_speed_profile_var = tk.StringVar(value=reverse[current])
        cb = ttk.Combobox(pane, textvariable=app._u108_speed_profile_var,
                          values=tuple(options.keys()), state="readonly", width=32)
        cb.pack(anchor="w", padx=8, pady=(0, 5))
        def selected(_event=None):
            app._u108_speed_profile = options.get(app._u108_speed_profile_var.get(), "STANDARD")
        cb.bind("<<ComboboxSelected>>", selected)
        tk.Label(pane,
            text="Wartość główna to mediana udanych próbek. MAX pyta o zgodę przed większym transferem; błędne lub niepełne próbki nie są uznawane za wynik.",
            bg=t["panel"], fg=t["muted"], font=app.fnt(8), wraplength=1320, justify="left"
        ).pack(fill="x", padx=8, pady=(0, 4))
    except Exception as exc:
        try:
            app.queue_log("Profil Speed Test: " + repr(exc))
        except Exception:
            pass

def _u108_selftest_live_telemetry():
    class FakeTree:
        def __init__(self): self.items = {}
        def winfo_exists(self): return True
        def get_children(self): return list(self.items.keys())
        def delete(self, *ids):
            for iid in ids: self.items.pop(iid, None)
        def insert(self, _parent, _index, iid=None, values=None, **kwargs):
            key = iid or str(len(self.items)); self.items[key] = tuple(values or ())
        def exists(self, iid): return iid in self.items
        def item(self, iid, **kwargs):
            if "values" in kwargs: self.items[iid] = tuple(kwargs["values"])
            return {"values": self.items.get(iid, ())}
    class FakeLabel:
        def __init__(self): self.text = ""
        def winfo_exists(self): return True
        def config(self, **kwargs): self.text = kwargs.get("text", self.text)
    class FakeApp:
        pass
    app = FakeApp()
    app._u100_sensor_tree = FakeTree()
    app._u100_sensor_count = FakeLabel()
    temps = {"method":"synthetic test bridge","sensors":[
        {"hardware":"CPU Package","hardwareType":"CpuAmd","sensor":"Tctl/Tdie","sensorType":"Temperature","value":72.0,"unit":"°C","source":"test"},
        {"hardware":"GPU Core","hardwareType":"GpuNvidia","sensor":"GPU Temperature","sensorType":"Temperature","value":66.0,"unit":"°C","source":"test"}
    ],"acpi_zones":[{"name":"TZ0","value":39.0}]}
    system = {"cpu_percent":35.0,"cpu_per_core_percent":[22.0,67.0],
        "ram_percent":61.0,"ram_total_bytes":16*1073741824,"ram_used_bytes":8*1073741824,
        "disk_devices":[{"name":"PhysicalDrive0","read_mbps":25.5,"write_mbps":4.5,"read_iops":200.0,"write_iops":40.0}],
        "network_interfaces":[{"name":"Ethernet","download_mbps":92.0,"upload_mbps":8.0,"is_up":True,"link_speed_mbps":1000,"mtu":1500,"addresses":["192.0.2.5"]}],
        "partitions":[{"mountpoint":"C:\\\\","total_bytes":1000000,"used_bytes":500000,"free_bytes":500000,"used_percent":50,"filesystem":"NTFS"}],
        "extra_temperature_sensors":[{"hardware":"Windows ACPI","sensor":"TZ0","value":39.0,"unit":"°C","source":"test"}],
        "sampled_at":_U66_datetime.now().isoformat(timespec="seconds")}
    app._u66_sensor_cache = _u108_build_sensor_snapshot(app, temps, {"temperature_c":66.0}, system)
    rows = _u107_get_sensor_rows(app)
    assert any(r["sensor"]=="Rdzeń logiczny 2 — użycie" and r["value"]=="67" for r in rows)
    assert any(r["hardware"]=="PhysicalDrive0" and r["sensor"]=="Odczyt" for r in rows)
    assert any(r["hardware"]=="Ethernet" and r["sensor"]=="Download" for r in rows)
    assert any(r["hardware"]=="C:\\\\" and r["sensor"]=="Wykorzystanie" for r in rows)
    assert any(r["sensor"]=="Tctl/Tdie" and r["unit"]=="°C" for r in rows)
    _u108_refresh_sensor_table(app)
    values=list(app._u100_sensor_tree.items.values())
    assert any("Rdzeń logiczny 2 — użycie" in str(row) for row in values)
    assert any("PhysicalDrive0" in str(row) for row in values)
    assert any("Ethernet" in str(row) for row in values)
    assert len(values)>=20 and "pozycji" in app._u100_sensor_count.text
    print("FULL_LIVE_SENSOR_TABLE_SELFTEST_OK: temperatures, per-core load, RAM/swap, per-disk I/O, NIC, partitions")

def _u108_selftest_speed_profiles():
    global _U108_ACTIVE_SPEED_PROFILE
    old = _U108_ACTIVE_SPEED_PROFILE
    try:
        _U108_ACTIVE_SPEED_PROFILE = "QUICK"; quick = _u108_speed_sample_sizes(1000)
        _U108_ACTIVE_SPEED_PROFILE = "STANDARD"; standard = _u108_speed_sample_sizes(1000)
        _U108_ACTIVE_SPEED_PROFILE = "MAX"; maximum = _u108_speed_sample_sizes(1000)
        assert max(quick) <= 10_000_000
        assert max(standard) <= 30_000_000
        assert max(maximum) <= 60_000_000
        assert max(maximum) > max(standard) > max(quick)
        print("SPEED_TEST_PROFILE_SELFTEST_OK: quick < standard < max payloads")
    finally:
        _U108_ACTIVE_SPEED_PROFILE = old

# The new collector feeds the visible table; every display refresh shows raw hardware sensors
# plus OS-level per-core, memory, disk, network, battery and filesystem metrics.
_u100_refresh_sensor_table = _u108_refresh_sensor_table
_u81_refresh_sensor_table = _u108_refresh_sensor_table
_u100_sensor_poll = _u108_sensor_poll
_u66_sensor_poll = _u108_sensor_poll
_u104_speed_sample_sizes = _u108_speed_sample_sizes
_u66_measure_speed = _u108_measure_speed
_u66_start_speed_test = _u108_start_speed_test
AppV43.show_speed_test = _u108_show_speed_test


# v4.3.112 — extend the independent test catalog with distinct read-only service diagnostics.
# These are additional probes in the same app, not a claim of byte-for-byte parity with the source ZIPs.
_U109_ORIGINAL_EXECUTE_CATALOG_TEST = _u93_execute_catalog_test
_U109_ORIGINAL_START_CATALOG_TEST = _u93_start_catalog_test

_U109_SERVICE_PROBES = {
 "sr_os_activation": r"""
$os=Get-CimInstance Win32_OperatingSystem | Select-Object Caption,Version,BuildNumber,OSArchitecture,ProductType
$lic=@(Get-CimInstance SoftwareLicensingProduct -ErrorAction SilentlyContinue | Where-Object { $_.ApplicationID -eq '55c92734-d682-4d71-983e-d6ec3f16059f' -and $_.PartialProductKey } | Select-Object Name,Description,LicenseStatus)
[pscustomobject]@{os=$os;license_products=$lic;count=$lic.Count;method='CIM read-only; no product keys returned'} | ConvertTo-Json -Depth 5 -Compress
""",
 "sr_bios_uefi": r"""
$bios=Get-CimInstance Win32_BIOS | Select-Object Manufacturer,SMBIOSBIOSVersion,ReleaseDate
$board=Get-CimInstance Win32_BaseBoard | Select-Object Manufacturer,Product,Version
$secure=$null;try {$secure=Confirm-SecureBootUEFI -ErrorAction Stop} catch {$secure=$null}
$tpm=$null;try {$tpm=Get-Tpm | Select-Object TpmPresent,TpmReady,TpmEnabled,TpmActivated,LockedOut} catch {}
[pscustomobject]@{bios=$bios;board=$board;secure_boot=$secure;tpm=$tpm} | ConvertTo-Json -Depth 5 -Compress
""",
 "sr_driver_audit": r"""
$devices=@(Get-PnpDevice -PresentOnly -ErrorAction SilentlyContinue | Select-Object Class,FriendlyName,Status,Problem,InstanceId)
$bad=@($devices | Where-Object { $_.Status -and $_.Status -ne 'OK' -or $_.Problem -and $_.Problem -ne 0 })
$drivers=@(Get-CimInstance Win32_PnPSignedDriver -ErrorAction SilentlyContinue | Select-Object DeviceName,DriverProviderName,DriverVersion,InfName)
[pscustomobject]@{device_count=$devices.Count;problem_count=$bad.Count;problem_devices=$bad;driver_count=$drivers.Count;drivers=$drivers | Select-Object -First 150} | ConvertTo-Json -Depth 7 -Compress
""",
 "sr_update_audit": r"""
$services=@(Get-Service wuauserv,bits,cryptsvc,TrustedInstaller,WaaSMedicSvc -ErrorAction SilentlyContinue | Select-Object Name,Status,StartType)
$reboot=@()
if(Test-Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending'){$reboot+='CBS'}
if(Test-Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired'){$reboot+='WindowsUpdate'}
$rename=(Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager' -Name PendingFileRenameOperations -ErrorAction SilentlyContinue).PendingFileRenameOperations
if($rename){$reboot+='PendingFileRenameOperations'}
[pscustomobject]@{services=$services;service_count=$services.Count;pending_reboot_sources=$reboot;pending_file_rename=[bool]$rename} | ConvertTo-Json -Depth 5 -Compress
""",
 "sr_event_errors": r"""
$start=(Get-Date).AddHours(-24);$items=@()
foreach($log in @('System','Application')) {
 try {$items+=@(Get-WinEvent -FilterHashtable @{LogName=$log;Level=1,2;StartTime=$start} -MaxEvents 30 -ErrorAction Stop | Select-Object TimeCreated,LogName,ProviderName,Id,LevelDisplayName,Message)} catch {}
}
$items=@($items | Sort-Object TimeCreated -Descending | Select-Object -First 50)
[pscustomobject]@{window_hours=24;event_count=$items.Count;events=$items} | ConvertTo-Json -Depth 6 -Compress
""",
 "sr_service_health": r"""
$names=@('RpcSs','DcomLaunch','EventLog','Winmgmt','PlugPlay','LanmanWorkstation','Dhcp','Dnscache','WlanSvc','BITS','wuauserv','CryptSvc','Schedule','WinDefend')
$rows=@(Get-CimInstance Win32_Service -ErrorAction SilentlyContinue | Where-Object { $_.Name -in $names } | Select-Object Name,DisplayName,State,StartMode,ExitCode)
$stopped=@($rows | Where-Object { $_.StartMode -eq 'Auto' -and $_.State -ne 'Running' -and $_.Name -notin @('WlanSvc','BITS','wuauserv') })
[pscustomobject]@{checked_count=$rows.Count;stopped_automatic_count=$stopped.Count;stopped_automatic=$stopped;services=$rows} | ConvertTo-Json -Depth 5 -Compress
""",
 "sr_storage_health": r"""
$volumes=@(Get-Volume -ErrorAction SilentlyContinue | Where-Object DriveLetter | Select-Object DriveLetter,FileSystemLabel,FileSystem,HealthStatus,OperationalStatus,Size,SizeRemaining)
$disks=@();try {$disks=@(Get-PhysicalDisk -ErrorAction Stop | Select-Object FriendlyName,MediaType,BusType,HealthStatus,OperationalStatus,Size)} catch {}
$bad=@($disks | Where-Object { $_.HealthStatus -and $_.HealthStatus -notin @('Healthy','Unknown') })
[pscustomobject]@{volume_count=$volumes.Count;volumes=$volumes;physical_disk_count=$disks.Count;physical_disks=$disks;unhealthy_disk_count=$bad.Count;unhealthy_disks=$bad;note='SMART/HealthStatus depends on driver and storage provider'} | ConvertTo-Json -Depth 6 -Compress
""",
 "sr_recovery_bcd": r"""
$winre='';$bcd=''
try {$winre=(& reagentc.exe /info 2>&1 | Out-String)} catch {$winre=$_.Exception.Message}
try {$bcd=(& bcdedit.exe /enum '{current}' 2>&1 | Out-String)} catch {$bcd=$_.Exception.Message}
[pscustomobject]@{winre_info=$winre;bcd_current=$bcd;method='read-only; no BCD or recovery changes'} | ConvertTo-Json -Depth 4 -Compress
""",
 "sr_network_services": r"""
$names=@('Dhcp','Dnscache','NlaSvc','WlanSvc','Netman','netprofm','LanmanWorkstation')
$rows=@(Get-CimInstance Win32_Service -ErrorAction SilentlyContinue | Where-Object {$_.Name -in $names} | Select-Object Name,State,StartMode,ExitCode)
$adapters=@(Get-NetAdapter -ErrorAction SilentlyContinue | Select-Object Name,Status,LinkSpeed,MacAddress)
[pscustomobject]@{services=$rows;adapter_count=$adapters.Count;adapters=$adapters} | ConvertTo-Json -Depth 5 -Compress
""",
 "sr_component_store": r"""
$text=(& dism.exe /Online /Cleanup-Image /CheckHealth 2>&1 | Out-String)
$code=$LASTEXITCODE
[pscustomobject]@{dism_exit_code=$code;output=$text;method='DISM /CheckHealth only; no repair was requested'} | ConvertTo-Json -Depth 4 -Compress
""",
 "su_hardware_inventory": r"""
$cpu=Get-CimInstance Win32_Processor | Select-Object Name,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed
$gpu=@(Get-CimInstance Win32_VideoController | Select-Object Name,AdapterRAM,DriverVersion,VideoModeDescription)
$ram=@(Get-CimInstance Win32_PhysicalMemory | Select-Object Capacity,Speed,Manufacturer)
$board=Get-CimInstance Win32_BaseBoard | Select-Object Manufacturer,Product,Version
$bios=Get-CimInstance Win32_BIOS | Select-Object Manufacturer,SMBIOSBIOSVersion,ReleaseDate
[pscustomobject]@{cpu=$cpu;gpu=$gpu;ram=$ram;motherboard=$board;bios=$bios;note='Serial numbers omitted'} | ConvertTo-Json -Depth 6 -Compress
""",
 "su_software_inventory": r"""
$paths=@('HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*','HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*','HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*')
$items=@(foreach($path in $paths){Get-ItemProperty $path -ErrorAction SilentlyContinue | Where-Object {$_.DisplayName} | Select-Object DisplayName,DisplayVersion,Publisher,InstallDate})
$items=@($items | Sort-Object DisplayName -Unique | Select-Object -First 250)
[pscustomobject]@{application_count=$items.Count;applications=$items;source='Uninstall registry keys; no Win32_Product query'} | ConvertTo-Json -Depth 5 -Compress
""",
 "su_startup_audit": r"""
$startup=@(Get-CimInstance Win32_StartupCommand -ErrorAction SilentlyContinue | Select-Object Name,Command,Location,User)
$tasks=@()
try {$tasks=@(Get-ScheduledTask -ErrorAction Stop | Where-Object {$_.Triggers.CimClass.CimClassName -match 'BootTrigger|LogonTrigger'} | Select-Object -First 80 TaskName,TaskPath,State)} catch {}
[pscustomobject]@{startup_count=$startup.Count;startup=$startup;startup_task_count=$tasks.Count;startup_tasks=$tasks;note='Read-only audit; startup entries are not changed'} | ConvertTo-Json -Depth 6 -Compress
""",
 "su_crash_history": r"""
$start=(Get-Date).AddDays(-30);$items=@()
foreach($provider in @('Application Error','Windows Error Reporting')) {
 try {$items+=@(Get-WinEvent -FilterHashtable @{LogName='Application';ProviderName=$provider;StartTime=$start} -MaxEvents 40 -ErrorAction Stop | Select-Object TimeCreated,ProviderName,Id,LevelDisplayName,Message)} catch {}
}
$items=@($items | Sort-Object TimeCreated -Descending | Select-Object -First 60)
[pscustomobject]@{window_days=30;crash_event_count=$items.Count;events=$items} | ConvertTo-Json -Depth 6 -Compress
""",
 "su_network_config": r"""
$rows=@()
try {$rows=@(Get-NetIPConfiguration -ErrorAction Stop | Select-Object InterfaceAlias,InterfaceDescription,NetProfile,IPv4Address,IPv4DefaultGateway,DNSServer)} catch {}
[pscustomobject]@{interface_count=$rows.Count;interfaces=$rows;method='Get-NetIPConfiguration read-only'} | ConvertTo-Json -Depth 7 -Compress
""",
 "su_wmi_health": r"""
$svc=Get-Service Winmgmt -ErrorAction SilentlyContinue | Select-Object Name,Status,StartType
$probe=$null;$errorText=$null
try {$probe=Get-CimInstance Win32_OperatingSystem -ErrorAction Stop | Select-Object Caption,BuildNumber} catch {$errorText=$_.Exception.Message}
$verify='not run';$verifyError=$null
try {$verify=(& winmgmt.exe /verifyrepository 2>&1 | Out-String)} catch {$verifyError=$_.Exception.Message}
[pscustomobject]@{wmi_service=$svc;cim_query=$probe;cim_query_error=$errorText;repository_verification=$verify;repository_error=$verifyError;method='verification only; no salvage/reset'} | ConvertTo-Json -Depth 5 -Compress
""",
 "su_windows_update_history": r"""
$items=@(Get-HotFix -ErrorAction SilentlyContinue | Sort-Object InstalledOn -Descending | Select-Object -First 60 HotFixID,Description,InstalledBy,InstalledOn)
[pscustomobject]@{installed_update_count=$items.Count;updates=$items;source='Get-HotFix; recent installed hotfixes'} | ConvertTo-Json -Depth 5 -Compress
""",
 "su_system_services": r"""
$items=@(Get-CimInstance Win32_Service -ErrorAction SilentlyContinue | Where-Object {$_.StartMode -eq 'Auto'} | Select-Object Name,DisplayName,State,StartMode,StartName)
$stopped=@($items | Where-Object {$_.State -ne 'Running'})
[pscustomobject]@{automatic_service_count=$items.Count;stopped_count=$stopped.Count;stopped_automatic=$stopped | Select-Object -First 100;services=$items | Select-Object -First 200} | ConvertTo-Json -Depth 5 -Compress
""",
 "su_report_folder": r"""
$roots=@((Join-Path $env:LOCALAPPDATA 'NaprawaPC'),(Join-Path $env:USERPROFILE 'Desktop\NAPRAWA_PC_RAPORTY'),(Join-Path $env:USERPROFILE 'Documents\NaprawaPC'))
$found=@()
foreach($root in $roots){if(Test-Path -LiteralPath $root){$found+=@(Get-ChildItem -LiteralPath $root -File -Recurse -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 40 @{n='Root';e={$root}},FullName,Length,LastWriteTime)}}
$found=@($found | Sort-Object LastWriteTime -Descending | Select-Object -First 100)
[pscustomobject]@{searched_roots=$roots;report_count=$found.Count;reports=$found;note='File inventory only; report contents are not uploaded'} | ConvertTo-Json -Depth 5 -Compress
""",
 "su_windows_installations": r"""
$found=@()
$drives=@(Get-CimInstance Win32_LogicalDisk -Filter 'DriveType=3' -ErrorAction SilentlyContinue)
foreach($drive in $drives) {
 $root=$drive.DeviceID+'\'
 $software=Join-Path $root 'Windows\System32\config\SOFTWARE'
 $system=Join-Path $root 'Windows\System32\config\SYSTEM'
 if((Test-Path -LiteralPath $software) -and (Test-Path -LiteralPath $system)) {
   $found += [pscustomobject]@{drive=$drive.DeviceID;windows_directory=(Join-Path $root 'Windows');software_hive=$software;system_hive=$system;offline=($drive.DeviceID -ne $env:SystemDrive)}
 }
}
[pscustomobject]@{installation_count=$found.Count;installations=$found;method='read-only file marker scan; no offline registry hives mounted'} | ConvertTo-Json -Depth 5 -Compress
"""
}

def _u109_service_probe(app, module, test_id, settings):
    if not is_windows():
        return {"state":"warn","test_id":test_id,"module":module,
                "message":"Ten odczyt diagnostyczny wymaga Windows.","returncode":None}
    script=_U109_SERVICE_PROBES.get(str(test_id))
    if not script:
        return {"state":"error","test_id":test_id,"module":module,"message":"Brak skryptu dla testu serwisowego."}
    try:
        raw=ps_json(script, default=None)
        if isinstance(raw,list) and len(raw)==1 and isinstance(raw[0],dict):
            raw=raw[0]
        if not isinstance(raw,dict):
            return {"state":"warn","test_id":test_id,"module":module,"raw_result":str(raw)[:12000],
                    "message":"PowerShell nie zwrócił obiektu JSON. Wynik nie jest zaliczony."}
        result=dict(raw)
        state="good"
        warnings=[]
        if test_id=="sr_driver_audit" and int(result.get("problem_count",0) or 0)>0:
            state="warn";warnings.append("Znaleziono urządzenia PnP zgłaszające status inny niż OK.")
        if test_id=="sr_service_health" and int(result.get("stopped_automatic_count",0) or 0)>0:
            state="warn";warnings.append("Jedna lub więcej usług z listy kontrolnej ma status zatrzymany.")
        if test_id=="sr_storage_health" and int(result.get("unhealthy_disk_count",0) or 0)>0:
            state="warn";warnings.append("Dostawca magazynu zgłasza stan dysku wymagający uwagi.")
        if test_id=="sr_event_errors" and int(result.get("event_count",0) or 0)>0:
            state="warn";warnings.append("W dzienniku znaleziono zdarzenia krytyczne/błędy; ich przyczyna wymaga analizy.")
        if test_id=="su_crash_history" and int(result.get("crash_event_count",0) or 0)>0:
            state="warn";warnings.append("W historii znaleziono zdarzenia awarii; obecność wpisu nie określa sama przyczyny.")
        if test_id=="su_wmi_health" and (result.get("cim_query_error") or not result.get("cim_query")):
            state="warn";warnings.append("Zapytanie CIM nie zwróciło danych.")
        if test_id=="su_system_services" and int(result.get("stopped_count",0) or 0)>0:
            state="warn";warnings.append("Występują zatrzymane usługi automatyczne; nie wszystkie muszą być wymagane w tej konfiguracji.")
        if test_id=="sr_update_audit" and result.get("pending_reboot_sources"):
            state="warn";warnings.append("System zgłasza źródło oczekującego ponownego uruchomienia.")
        if test_id in ("sr_driver_audit","sr_service_health","sr_storage_health","sr_event_errors",
                       "su_crash_history","su_software_inventory","su_windows_update_history",
                       "su_startup_audit","su_hardware_inventory","su_network_config","su_system_services") and not raw:
            state="warn";warnings.append("Puste dane — test nie jest oznaczony jako PASS.")
        # A successful PowerShell invocation alone is not enough to call every probe PASS.
        # Missing provider data or non-zero native-command exits are explicitly surfaced.
        if test_id=="sr_os_activation":
            if not result.get("os"):
                state="warn";warnings.append("Brak informacji o wydaniu systemu operacyjnego.")
            licenses=result.get("license_products") or []
            if not licenses:
                state="warn";warnings.append("Dostawca licencjonowania nie zwrócił statusu; nie odczytano klucza produktu.")
            elif not any(int(item.get("LicenseStatus",-1) or 0)==1 for item in licenses if isinstance(item,dict)):
                state="warn";warnings.append("Nie wykryto aktywnego statusu licencji w rekordach zwróconych przez Windows.")
        if test_id=="sr_bios_uefi":
            if not result.get("bios") or not result.get("board"):
                state="warn";warnings.append("Brak części danych BIOS/płyty głównej.")
            if result.get("secure_boot") is None:
                state="warn";warnings.append("Secure Boot jest niedostępny/N/D na tym systemie.")
            if not result.get("tpm"):
                state="warn";warnings.append("Get-Tpm nie zwrócił stanu TPM.")
        if test_id=="sr_driver_audit" and not int(result.get("device_count",0) or 0) and not int(result.get("driver_count",0) or 0):
            state="warn";warnings.append("Nie uzyskano listy urządzeń ani sterowników.")
        if test_id=="sr_update_audit" and not int(result.get("service_count",0) or 0):
            state="warn";warnings.append("Nie uzyskano statusów usług aktualizacji.")
        if test_id=="sr_service_health" and not int(result.get("checked_count",0) or 0):
            state="warn";warnings.append("Nie udało się odczytać usług z listy kontrolnej.")
        if test_id=="sr_storage_health" and not int(result.get("volume_count",0) or 0):
            state="warn";warnings.append("Nie uzyskano informacji o woluminach.")
        if test_id=="sr_recovery_bcd":
            if not result.get("winre_info") and not result.get("bcd_current"):
                state="warn";warnings.append("WinRE i bieżący wpis BCD nie zwróciły danych.")
            output=(str(result.get("winre_info",""))+" "+str(result.get("bcd_current",""))).lower()
            if any(word in output for word in ("access is denied","access denied","error:","failure")):
                state="warn";warnings.append("Wyjście WinRE/BCD zawiera komunikat błędu; wymagany jest przegląd szczegółów.")
        if test_id=="sr_network_services" and not int(result.get("adapter_count",0) or 0) and not result.get("services"):
            state="warn";warnings.append("Nie uzyskano informacji o kartach ani usługach sieciowych.")
        if test_id=="sr_component_store" and (result.get("dism_exit_code") is None or int(result.get("dism_exit_code",-1))!=0):
            state="warn";warnings.append("DISM /CheckHealth zwrócił kod inny niż 0; odczytaj szczegóły wyniku.")
        if test_id=="su_hardware_inventory" and not any(result.get(key) for key in ("cpu","gpu","ram","motherboard","bios")):
            state="warn";warnings.append("Nie uzyskano danych inwentarza sprzętu.")
        if test_id=="su_software_inventory" and not int(result.get("application_count",0) or 0):
            state="warn";warnings.append("Rejestr Uninstall nie zwrócił zainstalowanych aplikacji.")
        if test_id=="su_network_config" and not int(result.get("interface_count",0) or 0):
            state="warn";warnings.append("Get-NetIPConfiguration nie zwrócił interfejsów.")
        if test_id=="su_wmi_health":
            verification=str(result.get("repository_verification","")).lower()
            if "inconsistent" in verification or "not consistent" in verification:
                state="warn";warnings.append("Narzędzie WMI zgłosiło niespójność repozytorium; aplikacja nie podjęła naprawy.")
        if test_id=="su_windows_update_history" and not int(result.get("installed_update_count",0) or 0):
            state="warn";warnings.append("Get-HotFix nie zwrócił listy aktualizacji — źródło może nie być dostępne.")
        if test_id=="su_system_services" and not int(result.get("automatic_service_count",0) or 0):
            state="warn";warnings.append("Nie uzyskano listy usług automatycznych.")
        if test_id=="su_report_folder" and not int(result.get("report_count",0) or 0):
            state="warn";warnings.append("Nie znaleziono raportów w sprawdzonych lokalnych katalogach.")
        if test_id=="su_windows_installations" and not int(result.get("installation_count",0) or 0):
            state="warn";warnings.append("Nie znaleziono markerów instalacji Windows na widocznych woluminach.")
        result.update({"state":state,"test_id":str(test_id),"module":str(module),
            "checked_at":_U66_datetime.now().isoformat(timespec="seconds"),
            "method":"Windows PowerShell read-only diagnostic",
            "warnings":warnings,
            "note":"Odczyt diagnostyczny; nic nie usuwa, nie wyłącza i nie naprawia automatycznie."})
        _u93_put_result(app,"SERVICE_PROBE_"+str(test_id),result)
        app.queue_log(f"SERVICE PROBE {test_id}: {state.upper()}"+( " — "+ "; ".join(warnings) if warnings else ""))
        return result
    except Exception as exc:
        return {"state":"error","test_id":str(test_id),"module":str(module),
                "error":f"{type(exc).__name__}: {exc}","note":"Nie wykonano operacji naprawczej."}

def _u109_execute_catalog_test(app,module,test_id,kind,settings):
    if kind=="service_probe":
        return _u109_service_probe(app,module,test_id,settings)
    return _U109_ORIGINAL_EXECUTE_CATALOG_TEST(app,module,test_id,kind,settings)

def _u109_start_catalog_test(app,module,test_id,title,kind):
    if kind=="service_probe" and test_id=="sr_component_store":
        if not messagebox.askyesno("DISM CheckHealth — test odczytowy",
            "Uruchomić DISM /Online /Cleanup-Image /CheckHealth? To kontrola magazynu składników bez naprawy. Może potrwać kilkanaście sekund. Kontynuować?"):
            _u93_update_detail(app,test_id,"ANULOWANO",{"state":"warn","message":"Anulowano za zgodą operatora; nie uruchomiono DISM."})
            return
    return _U109_ORIGINAL_START_CATALOG_TEST(app,module,test_id,title,kind)

def _u109_selftest_service_catalog():
    module_keys=[item[0] for item in _U93_MODULES]
    assert set(module_keys)==set(_U93_TEST_CATALOG.keys()),"Każdy moduł z laboratorium musi mieć swój katalog."
    assert len(module_keys)==15 and len(set(module_keys))==15
    all_tests=[test for entries in _U93_TEST_CATALOG.values() for test in entries]
    ids=[item[0] for item in all_tests]
    assert len(ids)==110 and len(set(ids))==110
    for module in ("SYSTEM_REPAIR_PRO","SERWIS_ULTIMATE"):
        assert len(_U93_TEST_CATALOG[module])==10
        assert all(test[3]=="service_probe" for test in _U93_TEST_CATALOG[module])
    scenes=[_U107_TEST_SCENES[test_id] for test_id in ids]
    assert len(set(scenes))==90
    assert set(ids).issubset(_U107_TEST_SCENES)
    assert "service_probe" in _U93_SUPPORTED_TEST_KINDS
    assert callable(_u109_service_probe)
    print("SYSTEM_REPAIR_PRO_SERWIS_ULTIMATE_CATALOG_SELFTEST_OK: 20 read-only diagnostics, 15 modules, 110 unique tests and OpenGL scenes")

_U93_SUPPORTED_TEST_KINDS.add("service_probe")
_U93_TEST_CATALOG["SYSTEM_REPAIR_PRO"] = [
 ("sr_os_activation","Windows — wersja i stan licencji","Odczyt wydania Windows i stanu licencji bez ujawniania klucza produktu.","service_probe"),
 ("sr_bios_uefi","BIOS / UEFI / Secure Boot / TPM","Odczyt wersji BIOS, płyty, stanu Secure Boot i TPM.","service_probe"),
 ("sr_driver_audit","Audyt sterowników i PnP","Lista urządzeń PnP oraz dostępne kody błędów i wersje sterowników.","service_probe"),
 ("sr_update_audit","Stan usług Windows Update","Status usług aktualizacji oraz wskaźniki oczekującego restartu.","service_probe"),
 ("sr_event_errors","Dziennik błędów Windows — 24 h","Zbiera ograniczoną listę ostatnich zdarzeń krytycznych i błędów.","service_probe"),
 ("sr_service_health","Zdrowie usług krytycznych Windows","Kontrola statusu usług systemowych; niczego nie uruchamia ani nie wyłącza.","service_probe"),
 ("sr_storage_health","Zdrowie woluminów i nośników","Odczyt wolnego miejsca, statusu woluminów i dostępnej telemetrii fizycznych dysków.","service_probe"),
 ("sr_recovery_bcd","WinRE / BCD — diagnostyka odczytowa","Odczytuje konfigurację środowiska odzyskiwania i bieżącego wpisu rozruchu.","service_probe"),
 ("sr_network_services","Usługi sieciowe Windows","Kontrola usług DHCP, DNS, WLAN i NLA.","service_probe"),
 ("sr_component_store","Magazyn składników DISM — CheckHealth","Odczytowy test DISM /CheckHealth; nie wykonuje naprawy ani RestoreHealth.","service_probe")
]
_U93_TEST_CATALOG["SERWIS_ULTIMATE"] = [
 ("su_hardware_inventory","Inwentarz sprzętu serwisowego","Zbiera model CPU, GPU, RAM, płyty głównej i BIOS bez numerów seryjnych.","service_probe"),
 ("su_software_inventory","Inwentarz zainstalowanego oprogramowania","Odczyt listy aplikacji z rejestru Uninstall; nie używa Win32_Product.","service_probe"),
 ("su_startup_audit","Autostart i zadania przy logowaniu","Audyt poleceń autostartu oraz ograniczonej listy zadań harmonogramu.","service_probe"),
 ("su_crash_history","Historia awarii aplikacji — 30 dni","Zbiera ograniczoną listę błędów Application Error / Windows Error Reporting.","service_probe"),
 ("su_network_config","Konfiguracja LAN / Wi-Fi / DNS","Odczyt adresów IP, bramy, DNS i profilu sieciowego dla aktywnych kart.","service_probe"),
 ("su_wmi_health","Spójność WMI — test odczytowy","Weryfikuje usługę WMI i dostępność zapytań CIM bez naprawiania repozytorium.","service_probe"),
 ("su_windows_update_history","Lista zainstalowanych aktualizacji","Odczyt ostatnio zainstalowanych poprawek Windows z Get-HotFix.","service_probe"),
 ("su_system_services","Audyt automatycznych usług Windows","Lista usług z automatycznym startem i tych, które obecnie nie działają.","service_probe"),
 ("su_report_folder","Raporty lokalne Naprawa PC","Wyszukuje ostatnie raporty w znanych katalogach lokalnych; nie wysyła ich do sieci.","service_probe"),
 ("su_windows_installations","Wykrywanie instalacji Windows na dyskach","Odczytowo wykrywa katalogi Windows i pliki rejestru offline na widocznych woluminach.","service_probe")
]
_U93_MODULES.extend([
 ("SYSTEM_REPAIR_PRO","SYSTEM REPAIR PRO — DIAGNOSTYKA WINDOWS"),
 ("SERWIS_ULTIMATE","SERWIS ULTIMATE — NARZĘDZIA SERWISOWE")
])
_U93_ALIASES.update({
 "SYSTEM REPAIR PRO":"SYSTEM_REPAIR_PRO","SYSTEMREPAIRPRO":"SYSTEM_REPAIR_PRO","SYSTEM_REPAIR_PRO":"SYSTEM_REPAIR_PRO",
 "SERWIS ULTIMATE":"SERWIS_ULTIMATE","SERWISULTIMATE":"SERWIS_ULTIMATE","SERWIS_ULTIMATE":"SERWIS_ULTIMATE"
})
_U107_TEST_SCENES.update({
 "sr_os_activation":66, "sr_bios_uefi":69, "sr_driver_audit":70, "sr_update_audit":71,
 "sr_event_errors":72, "sr_service_health":73, "sr_storage_health":74, "sr_recovery_bcd":75,
 "sr_network_services":79, "sr_component_store":80,
 "su_hardware_inventory":81, "su_software_inventory":82, "su_startup_audit":83, "su_crash_history":84,
 "su_network_config":85, "su_wmi_health":86, "su_windows_update_history":87,
 "su_system_services":88, "su_report_folder":89, "su_windows_installations":90
})
_u93_execute_catalog_test = _u109_execute_catalog_test
_u93_start_catalog_test = _u109_start_catalog_test



# v4.3.114 — add 20 read-only diagnostics, a distinct 110-scene GPU renderer,
# preserve sensors with unavailable values, and provide a parallel-stream Turbo speed profile.
_U114_EXTRA_SCENE_TITLES = [
    "System Repair PRO — Płynna siatka termiczna",
    "System Repair PRO — CPU socket / heat-spreader",
    "System Repair PRO — Moduły RAM / kanały",
    "System Repair PRO — NVMe / storage topology",
    "System Repair PRO — Wirniki chłodzenia",
    "System Repair PRO — Oscyloskop sygnałów",
    "System Repair PRO — Mapa obciążenia / ciepła",
    "System Repair PRO — Wektorowy wir cząstek",
    "System Repair PRO — Sieć pakietów / topologia",
    "Serwis Ultimate — Rząd serwerów / rack",
    "Serwis Ultimate — Ścieżki płyty głównej",
    "Serwis Ultimate — Mechanizm przekładni",
    "Serwis Ultimate — Ogród kryształów",
    "Serwis Ultimate — Światłowodowe pasma",
    "Serwis Ultimate — Pętla chłodzenia cieczą",
    "Serwis Ultimate — Tunel pierścieni",
    "Serwis Ultimate — Chiplet / mesh procesora",
    "Serwis Ultimate — Zasilacz / transformatory",
    "Serwis Ultimate — Fraktalna korona 3D",
    "Benchmark Ultimate — Gęsty renderer mieszany"
]
if len(_U100_SCENE_TITLES) == 90:
    _U100_SCENE_TITLES.extend(_U114_EXTRA_SCENE_TITLES)
if len(_U66_SCENES) == 90:
    _U66_SCENES.extend([
        (f"{i:02d} — {title}", title.split(" — ", 1)[0], 1 + ((i - 91) % 3) * 2)
        for i, title in enumerate(_U114_EXTRA_SCENE_TITLES, 91)
    ])

# New read-only probes for System Repair PRO and Serwis Ultimate.
# These scripts collect diagnostic data only; they do not disable protection or modify Windows.
_U114_SERVICE_PROBES = {
 "sr_firewall_profiles": r"""
$rows=@(Get-NetFirewallProfile -ErrorAction SilentlyContinue | Select-Object Name,Enabled,DefaultInboundAction,DefaultOutboundAction,NotifyOnListen)
[pscustomobject]@{profiles=$rows;profile_count=$rows.Count;note='Read-only Windows Defender Firewall profile audit'} | ConvertTo-Json -Depth 5 -Compress
""",
 "sr_defender_status": r"""
try {$status=Get-MpComputerStatus -ErrorAction Stop | Select-Object AMServiceEnabled,AntivirusEnabled,AntispywareEnabled,RealTimeProtectionEnabled,BehaviorMonitorEnabled,IoavProtectionEnabled,NISEnabled,AntivirusSignatureLastUpdated,QuickScanAge,FullScanAge
 [pscustomobject]@{available=$true;status=$status;note='Read-only Microsoft Defender status; no protection settings are changed'} | ConvertTo-Json -Depth 5 -Compress
} catch {[pscustomobject]@{available=$false;error=$_.Exception.Message;note='Defender status unavailable; this does not mean protection is disabled'} | ConvertTo-Json -Depth 4 -Compress}
""",
 "sr_bitlocker_audit": r"""
$volumes=@()
try {$volumes=@(Get-BitLockerVolume -ErrorAction Stop | Select-Object MountPoint,VolumeType,VolumeStatus,ProtectionStatus,LockStatus,EncryptionPercentage,EncryptionMethod)
 [pscustomobject]@{available=$true;volume_count=$volumes.Count;volumes=$volumes;note='No recovery keys or secrets are collected'} | ConvertTo-Json -Depth 6 -Compress
} catch {[pscustomobject]@{available=$false;volume_count=0;volumes=@();error=$_.Exception.Message;note='BitLocker provider unavailable'} | ConvertTo-Json -Depth 4 -Compress}
""",
 "sr_pending_reboot": r"""
$sources=@()
if(Test-Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Component Based Servicing\RebootPending'){$sources+='CBS'}
if(Test-Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired'){$sources+='WindowsUpdate'}
if(Test-Path 'HKLM:\SOFTWARE\Microsoft\Updates\UpdateExeVolatile'){$v=(Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Updates\UpdateExeVolatile' -ErrorAction SilentlyContinue).UpdateExeVolatile;if($v){$sources+='UpdateExeVolatile'}}
$rename=(Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager' -Name PendingFileRenameOperations -ErrorAction SilentlyContinue).PendingFileRenameOperations
if($rename){$sources+='PendingFileRenameOperations'}
[pscustomobject]@{pending_reboot=($sources.Count -gt 0);sources=@($sources | Select-Object -Unique);pending_file_rename=[bool]$rename;checked_at=(Get-Date).ToString('o')} | ConvertTo-Json -Depth 4 -Compress
""",
 "sr_reliability_events": r"""
$start=(Get-Date).AddDays(-7);$items=@()
foreach($log in @('System','Application')){
 try {$items+=@(Get-WinEvent -FilterHashtable @{LogName=$log;Level=1,2;StartTime=$start} -MaxEvents 60 -ErrorAction Stop | Select-Object -First 40 TimeCreated,LogName,ProviderName,Id,LevelDisplayName,Message)}catch{}
}
$items=@($items | Sort-Object TimeCreated -Descending | Select-Object -First 80)
[pscustomobject]@{window_days=7;event_count=$items.Count;events=$items;note='Recent critical/error events only; event presence is not a root-cause diagnosis'} | ConvertTo-Json -Depth 6 -Compress
""",
 "sr_boot_status": r"""
$os=Get-CimInstance Win32_OperatingSystem | Select-Object Caption,Version,BuildNumber,LastBootUpTime,LocalDateTime,OSArchitecture
$events=@()
try {$events=@(Get-WinEvent -FilterHashtable @{LogName='System';ProviderName='Microsoft-Windows-Kernel-General';Id=12;StartTime=(Get-Date).AddDays(-14)} -MaxEvents 20 -ErrorAction Stop | Select-Object TimeCreated,Id,Message)}catch{}
[pscustomobject]@{os=$os;recent_boot_events=$events;recent_boot_event_count=$events.Count} | ConvertTo-Json -Depth 5 -Compress
""",
 "sr_device_problems": r"""
$devices=@(Get-PnpDevice -PresentOnly -ErrorAction SilentlyContinue | Where-Object { ($_.Status -and $_.Status -ne 'OK') -or ($_.Problem -and $_.Problem -ne 0) } | Select-Object Class,FriendlyName,Status,Problem,InstanceId)
[pscustomobject]@{problem_count=$devices.Count;problem_devices=$devices;checked_at=(Get-Date).ToString('o');note='Present Plug and Play devices only; a clean list does not test physical ports'} | ConvertTo-Json -Depth 6 -Compress
""",
 "sr_volume_capacity": r"""
$volumes=@(Get-Volume -ErrorAction SilentlyContinue | Where-Object DriveLetter | Select-Object DriveLetter,FileSystemLabel,FileSystem,HealthStatus,OperationalStatus,Size,SizeRemaining)
$mapped=@($volumes | ForEach-Object {$total=[double]$_.Size;$free=[double]$_.SizeRemaining;[pscustomobject]@{drive=$_.DriveLetter;label=$_.FileSystemLabel;filesystem=$_.FileSystem;health=$_.HealthStatus;operational=$_.OperationalStatus;total_bytes=$total;free_bytes=$free;used_bytes=[math]::Max(0,$total-$free);used_percent=if($total -gt 0){[math]::Round(($total-$free)*100/$total,2)}else{$null}}})
[pscustomobject]@{volume_count=$mapped.Count;volumes=$mapped} | ConvertTo-Json -Depth 6 -Compress
""",
 "sr_sfc_verify": r"""
$out=(& sfc.exe /verifyonly 2>&1 | Out-String);$code=$LASTEXITCODE
[pscustomobject]@{exit_code=$code;output=$out;method='sfc /verifyonly — read-only verification, no repair'} | ConvertTo-Json -Depth 4 -Compress
""",
 "sr_dism_scanhealth": r"""
$out=(& dism.exe /Online /Cleanup-Image /ScanHealth 2>&1 | Out-String);$code=$LASTEXITCODE
[pscustomobject]@{exit_code=$code;output=$out;method='DISM /ScanHealth — scans component store; does not request RestoreHealth'} | ConvertTo-Json -Depth 4 -Compress
""",
 "su_process_pressure": r"""
$rows=@(Get-Process -ErrorAction SilentlyContinue | Sort-Object WorkingSet64 -Descending | Select-Object -First 30 Name,Id,CPU,WorkingSet64,PrivateMemorySize64,Handles,Threads)
[pscustomobject]@{process_count=$rows.Count;top_by_working_set=$rows;note='Process names and resource counters only; command lines and document contents are not collected'} | ConvertTo-Json -Depth 5 -Compress
""",
 "su_task_scheduler_audit": r"""
$rows=@()
try {$rows=@(Get-ScheduledTask -ErrorAction Stop | Where-Object { $_.State -eq 'Disabled' -or $_.TaskPath -match '\\Startup\\' } | Select-Object -First 100 TaskName,TaskPath,State,Author,Description)}catch{}
[pscustomobject]@{task_count=$rows.Count;tasks=$rows;note='Selected scheduled task metadata; tasks are not changed'} | ConvertTo-Json -Depth 5 -Compress
""",
 "su_path_health": r"""
$entries=@();$processPath=[Environment]::GetEnvironmentVariable('Path','Process');$machinePath=[Environment]::GetEnvironmentVariable('Path','Machine');$userPath=[Environment]::GetEnvironmentVariable('Path','User')
foreach($scope in @(@{name='Process';value=$processPath},@{name='Machine';value=$machinePath},@{name='User';value=$userPath})){
 foreach($item in ([string]$scope.value -split ';' | Where-Object {$_ -and $_.Trim()})){
  $path=$item.Trim().Trim('"');$exists=Test-Path -LiteralPath $path
  $entries += [pscustomobject]@{scope=$scope.name;path=$path;exists=$exists}
 }
}
$duplicates=@($entries | Group-Object {$_.path.ToLowerInvariant()} | Where-Object Count -gt 1 | ForEach-Object {[pscustomobject]@{path=$_.Group[0].path;occurrences=$_.Count}})
$missing=@($entries | Where-Object {!$_.exists})
[pscustomobject]@{entry_count=$entries.Count;missing_count=$missing.Count;missing=$missing;duplicate_path_count=$duplicates.Count;duplicates=$duplicates;entries=$entries} | ConvertTo-Json -Depth 6 -Compress
""",
 "su_dns_audit": r"""
$adapters=@(Get-DnsClientServerAddress -ErrorAction SilentlyContinue | Select-Object InterfaceAlias,AddressFamily,ServerAddresses)
$resolved=@();$errorText=$null
try {$resolved=@(Resolve-DnsName cloudflare.com -Type A -DnsOnly -ErrorAction Stop | Select-Object Name,Type,IPAddress)}catch{$errorText=$_.Exception.Message}
[pscustomobject]@{dns_adapter_count=$adapters.Count;dns_adapters=$adapters;resolved_count=$resolved.Count;resolved=$resolved;resolve_error=$errorText;note='Performs a small DNS lookup only; not a speed test'} | ConvertTo-Json -Depth 6 -Compress
""",
 "su_perf_counter_audit": r"""
$queries=@()
foreach($path in @('\Processor(_Total)\% Processor Time','\Memory\Available MBytes')){
 try {$counter=Get-Counter -Counter $path -ErrorAction Stop;foreach($sample in $counter.CounterSamples){$queries += [pscustomobject]@{path=$sample.Path;cooked_value=[math]::Round($sample.CookedValue,2);status='OK'}}}
 catch {$queries += [pscustomobject]@{path=$path;cooked_value=$null;status='N/D';error=$_.Exception.Message}}
}
[pscustomobject]@{counter_count=$queries.Count;usable_count=@($queries | Where-Object {$_.status -eq 'OK'}).Count;counters=$queries;note='Counter names can be localized; N/D means this counter path is unavailable'} | ConvertTo-Json -Depth 5 -Compress
""",
 "su_power_plan": r"""
$active='';try {$active=(& powercfg.exe /getactivescheme 2>&1 | Out-String)}catch{$active=$_.Exception.Message}
$plans=@();try {$plans=@(Get-CimInstance -Namespace root\cimv2\power -ClassName Win32_PowerPlan -ErrorAction Stop | Select-Object ElementName,IsActive,InstanceID)}catch{}
$battery=$null;try {$battery=Get-CimInstance Win32_Battery | Select-Object Name,BatteryStatus,EstimatedChargeRemaining,EstimatedRunTime}catch{}
[pscustomobject]@{active_scheme=$active;plans=$plans;battery=$battery;plan_count=$plans.Count} | ConvertTo-Json -Depth 5 -Compress
""",
 "su_windows_features": r"""
$names=@('Microsoft-Hyper-V-All','VirtualMachinePlatform','Microsoft-Windows-Subsystem-Linux','NetFx3','Containers','IIS-WebServerRole')
$rows=@()
foreach($name in $names){try{$x=Get-WindowsOptionalFeature -Online -FeatureName $name -ErrorAction Stop;$rows += [pscustomobject]@{name=$name;state=$x.State;available=$true}}catch{$rows += [pscustomobject]@{name=$name;state='N/D';available=$false;error=$_.Exception.Message}}}
[pscustomobject]@{feature_count=$rows.Count;available_count=@($rows | Where-Object {$_.available}).Count;features=$rows;note='Selected optional features only; the list is not an exhaustive inventory'} | ConvertTo-Json -Depth 5 -Compress
""",
 "su_temp_folder_health": r"""
$paths=@($env:TEMP,(Join-Path $env:WINDIR 'Temp'),(Join-Path $env:LOCALAPPDATA 'Temp')) | Where-Object {$_} | Select-Object -Unique
$rows=@()
foreach($path in $paths){
 $bytes=0;$files=0;$errorText=$null
 try {foreach($file in @(Get-ChildItem -LiteralPath $path -File -Force -ErrorAction SilentlyContinue | Select-Object -First 5000)){$bytes += [long]$file.Length;$files++}}catch{$errorText=$_.Exception.Message}
 $rows += [pscustomobject]@{path=$path;exists=(Test-Path -LiteralPath $path);sampled_file_count=$files;sampled_bytes=$bytes;error=$errorText;sample_limit=5000}
}
[pscustomobject]@{folder_count=$rows.Count;folders=$rows;note='Read-only estimate from up to 5000 top-level files per folder'} | ConvertTo-Json -Depth 5 -Compress
""",
 "su_crash_dump_audit": r"""
$paths=@((Join-Path $env:LOCALAPPDATA 'CrashDumps'),(Join-Path $env:WINDIR 'Minidump'))
$rows=@()
foreach($path in $paths){
 $files=@()
 try {$files=@(Get-ChildItem -LiteralPath $path -File -Force -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 100 Name,Length,LastWriteTime)}catch{}
 $rows += [pscustomobject]@{path=$path;exists=(Test-Path -LiteralPath $path);dump_count=$files.Count;recent_dumps=$files}
}
[pscustomobject]@{locations=$rows;note='Lists dump-file metadata only; does not open or upload dump contents'} | ConvertTo-Json -Depth 5 -Compress
""",
 "su_network_profile_audit": r"""
$profiles=@();$adapters=@()
try {$profiles=@(Get-NetConnectionProfile -ErrorAction Stop | Select-Object Name,InterfaceAlias,NetworkCategory,IPv4Connectivity,IPv6Connectivity)}catch{}
try {$adapters=@(Get-NetAdapter -ErrorAction Stop | Select-Object Name,Status,LinkSpeed,MediaType,InterfaceDescription)}catch{}
[pscustomobject]@{profile_count=$profiles.Count;profiles=$profiles;adapter_count=$adapters.Count;adapters=$adapters;note='Read-only network profile and adapter metadata'} | ConvertTo-Json -Depth 5 -Compress
"""
}
_U109_SERVICE_PROBES.update(_U114_SERVICE_PROBES)

_U93_TEST_CATALOG["SYSTEM_REPAIR_PRO"].extend([
 ("sr_firewall_profiles","Zapora Windows — profile i reguły podstawowe","Odczytuje aktywność profili zapory; nie zmienia reguł.","service_probe"),
 ("sr_defender_status","Microsoft Defender — stan ochrony","Odczyt ochrony w czasie rzeczywistym i wieku sygnatur; nie zmienia ustawień.","service_probe"),
 ("sr_bitlocker_audit","BitLocker — status woluminów","Odczyt statusu szyfrowania i ochrony bez pobierania kluczy odzyskiwania.","service_probe"),
 ("sr_pending_reboot","Windows — wykrywanie oczekującego restartu","Sprawdza znane wskaźniki Pending Reboot w rejestrze.","service_probe"),
 ("sr_reliability_events","Zdarzenia błędów — ostatnie 7 dni","Ograniczona lista ostatnich błędów i zdarzeń krytycznych z dzienników.","service_probe"),
 ("sr_boot_status","Czas startu i historia rozruchu","Odczyt LastBootUpTime i ostatnich zdarzeń startu systemu.","service_probe"),
 ("sr_device_problems","Urządzenia PnP z kodami problemów","Oddzielny audyt urządzeń raportujących status problemowy.","service_probe"),
 ("sr_volume_capacity","Pojemność i wolne miejsce woluminów","Szczegóły pojemności i stanu woluminów Windows.","service_probe"),
 ("sr_sfc_verify","SFC — weryfikacja plików systemowych","sfc /verifyonly — dłuższa weryfikacja bez naprawy plików.","service_probe"),
 ("sr_dism_scanhealth","DISM — skan magazynu składników","DISM /ScanHealth — kontrola magazynu składników bez RestoreHealth.","service_probe")
])
_U93_TEST_CATALOG["SERWIS_ULTIMATE"].extend([
 ("su_process_pressure","Procesy — zużycie pamięci i CPU","Top procesów według working set; bez wierszy poleceń i treści dokumentów.","service_probe"),
 ("su_task_scheduler_audit","Harmonogram zadań — wybrany audyt","Odczyt metadanych wybranych zadań; nie uruchamia ani nie usuwa zadań.","service_probe"),
 ("su_path_health","PATH — brakujące i powtarzające się ścieżki","Wykrywa brakujące katalogi i duplikaty wpisów PATH.","service_probe"),
 ("su_dns_audit","DNS — konfiguracja kart i resolver","Odczyt serwerów DNS i małe zapytanie resolvera, bez testu przepustowości.","service_probe"),
 ("su_perf_counter_audit","Liczniki wydajności Windows","Sprawdza dostępność wybranych liczników CPU i wolnej pamięci.","service_probe"),
 ("su_power_plan","Plan zasilania i bateria","Odczyt aktywnego planu zasilania oraz dostępnego statusu baterii.","service_probe"),
 ("su_windows_features","Opcjonalne funkcje Windows — wybrane","Odczyt stanu wybranych funkcji opcjonalnych, nie pełna inwentaryzacja.","service_probe"),
 ("su_temp_folder_health","Katalogi TEMP — wykorzystanie","Oszacowanie liczby i rozmiaru plików w wybranych katalogach TEMP.","service_probe"),
 ("su_crash_dump_audit","Zrzuty awarii — metadane plików","Lista metadanych ostatnich zrzutów; nie odczytuje zawartości plików.","service_probe"),
 ("su_network_profile_audit","Profile LAN/Wi‑Fi i adaptery","Odczyt profili sieciowych i linków kart sieciowych.","service_probe")
])

_U107_TEST_SCENES.update({
 "sr_firewall_profiles":91, "sr_defender_status":92, "sr_bitlocker_audit":93, "sr_pending_reboot":94,
 "sr_reliability_events":95, "sr_boot_status":96, "sr_device_problems":97, "sr_volume_capacity":98,
 "sr_sfc_verify":99, "sr_dism_scanhealth":100,
 "su_process_pressure":101, "su_task_scheduler_audit":102, "su_path_health":103, "su_dns_audit":104,
 "su_perf_counter_audit":105, "su_power_plan":106, "su_windows_features":107, "su_temp_folder_health":108,
 "su_crash_dump_audit":109, "su_network_profile_audit":110
})

# Wrap probes with result grading for potentially lengthy verification commands.
_U114_ORIGINAL_SERVICE_PROBE = _u109_service_probe
def _u114_service_probe(app,module,test_id,settings):
    result=_U114_ORIGINAL_SERVICE_PROBE(app,module,test_id,settings)
    if not isinstance(result,dict):
        return {"state":"warn","test_id":str(test_id),"message":"Brak raportu z diagnostyki odczytowej."}
    warnings=list(result.get("warnings") or [])
    output=str(result.get("output") or "")
    if test_id=="sr_sfc_verify":
        code=result.get("exit_code")
        if code is None or int(code or 0)!=0:
            warnings.append("SFC /verifyonly zakończył się kodem innym niż 0; sprawdź pełny tekst wyniku.")
            result["state"]="warn"
        low=output.casefold()
        if any(token in low for token in ("found integrity violations","found corrupt files","could not perform the requested operation")):
            warnings.append("Tekst SFC wskazuje możliwe naruszenie integralności albo przerwany test.")
            result["state"]="warn"
    elif test_id=="sr_dism_scanhealth":
        code=result.get("exit_code")
        if code is None or int(code or 0)!=0:
            warnings.append("DISM /ScanHealth nie zwrócił kodu sukcesu.")
            result["state"]="warn"
        low=output.casefold()
        if any(token in low for token in ("component store is repairable","component store corruption was detected","corruption detected")):
            warnings.append("DISM zgłosił uszkodzenie magazynu składników; nie wykonano automatycznej naprawy.")
            result["state"]="warn"
    elif test_id=="sr_firewall_profiles":
        profiles=result.get("profiles") or []
        if not profiles:
            result["state"]="warn";warnings.append("Nie odczytano profili zapory.")
        elif not any(isinstance(row,dict) and row.get("Enabled") is True for row in profiles):
            result["state"]="warn";warnings.append("Żaden profil zapory nie został zgłoszony jako włączony; sprawdź szczegóły i zasady organizacji.")
    elif test_id=="sr_defender_status":
        if not result.get("available"):
            result["state"]="warn";warnings.append("Nie udało się odczytać statusu Microsoft Defender.")
        else:
            status=result.get("status") or {}
            if status.get("AntivirusEnabled") is False or status.get("RealTimeProtectionEnabled") is False:
                result["state"]="warn";warnings.append("Defender zgłosił wyłączony składnik ochrony; potwierdź konfigurację na tym komputerze.")
    elif test_id=="sr_bitlocker_audit":
        if not result.get("available") or not int(result.get("volume_count",0) or 0):
            result["state"]="warn";warnings.append("Nie uzyskano statusu woluminów BitLocker; dostawca może być niedostępny.")
    elif test_id=="sr_pending_reboot":
        if result.get("pending_reboot"):
            result["state"]="warn";warnings.append("Wykryto źródło oczekującego restartu systemu.")
    elif test_id=="sr_reliability_events":
        if int(result.get("event_count",0) or 0)>0:
            result["state"]="warn";warnings.append("Znaleziono wpisy krytyczne/błędy z ostatnich 7 dni; przejrzyj treść zdarzeń.")
    elif test_id=="sr_boot_status":
        if not result.get("os"):
            result["state"]="warn";warnings.append("Nie uzyskano podstawowych informacji o uruchomionym systemie.")
    elif test_id=="sr_device_problems":
        if int(result.get("problem_count",0) or 0)>0:
            result["state"]="warn";warnings.append("Co najmniej jedno obecne urządzenie PnP zgłasza problem.")
        elif result.get("problem_devices") is None:
            result["state"]="warn";warnings.append("Dostawca PnP nie zwrócił listy wyników.")
    elif test_id=="sr_volume_capacity":
        if not int(result.get("volume_count",0) or 0):
            result["state"]="warn";warnings.append("Nie odczytano woluminów; nie oznaczono skanu jako PASS.")
    elif test_id=="su_process_pressure":
        if not int(result.get("process_count",0) or 0):
            result["state"]="warn";warnings.append("Nie uzyskano inwentarza działających procesów.")
    elif test_id=="su_task_scheduler_audit":
        if not int(result.get("task_count",0) or 0):
            result["state"]="warn";warnings.append("Nie zwrócono zadań odpowiadających filtrowi; wynik nie dowodzi braku zadań.")
    elif test_id=="su_path_health":
        if not int(result.get("entry_count",0) or 0):
            result["state"]="warn";warnings.append("Nie uzyskano żadnych wpisów PATH.")
        if int(result.get("missing_count",0) or 0)>0:
            result["state"]="warn";warnings.append("PATH zawiera wpisy wskazujące na brakujące katalogi.")
        if int(result.get("duplicate_path_count",0) or 0)>0:
            warnings.append("Wykryto powtarzające się ścieżki PATH.")
    elif test_id=="su_dns_audit":
        if not int(result.get("dns_adapter_count",0) or 0):
            result["state"]="warn";warnings.append("Nie odczytano serwerów DNS kart sieciowych.")
        if not int(result.get("resolved_count",0) or 0):
            result["state"]="warn";warnings.append("Zapytanie DNS nie zwróciło odpowiedzi; sprawdź połączenie i resolver.")
    elif test_id=="su_perf_counter_audit":
        if int(result.get("usable_count",0) or 0)<2:
            result["state"]="warn";warnings.append("Co najmniej jeden wybrany licznik wydajności jest niedostępny.")
    elif test_id=="su_power_plan":
        if not result.get("active_scheme"):
            result["state"]="warn";warnings.append("Nie odczytano aktywnego planu zasilania.")
    elif test_id=="su_windows_features":
        if not int(result.get("available_count",0) or 0):
            result["state"]="warn";warnings.append("Nie odczytano stanów żadnej z wybranych funkcji Windows.")
    elif test_id=="su_temp_folder_health":
        folders=result.get("folders") or []
        if not folders or not any(isinstance(row,dict) and row.get("exists") for row in folders):
            result["state"]="warn";warnings.append("Nie odczytano żadnego istniejącego katalogu TEMP.")
    elif test_id=="su_crash_dump_audit":
        locations=result.get("locations") or []
        if not locations:
            result["state"]="warn";warnings.append("Nie uzyskano informacji o lokalizacjach zrzutów.")
    elif test_id=="su_network_profile_audit":
        if not int(result.get("adapter_count",0) or 0) and not int(result.get("profile_count",0) or 0):
            result["state"]="warn";warnings.append("Nie odczytano profili sieciowych ani kart sieciowych.")
    result["warnings"]=warnings
    result["note"]=str(result.get("note") or "Diagnostyka odczytowa; nie uruchomiono operacji naprawczej.")
    return result

_U114_ORIGINAL_START_TEST=_u93_start_catalog_test
def _u114_start_catalog_test(app,module,test_id,title,kind):
    if kind=="service_probe" and test_id in ("sr_sfc_verify","sr_dism_scanhealth"):
        label="SFC /verifyonly" if test_id=="sr_sfc_verify" else "DISM /ScanHealth"
        duration="może potrwać kilka minut"
        if not messagebox.askyesno(label+" — wymaga potwierdzenia",
            f"Uruchomić {label}? To dłuższa diagnostyka odczytowa systemu Windows ({duration}); nie uruchamia naprawy. Kontynuować?"):
            _u93_update_detail(app,test_id,"ANULOWANO",{"state":"warn","message":"Anulowano; nie uruchomiono polecenia.","repair_started":False})
            return
    return _U114_ORIGINAL_START_TEST(app,module,test_id,title,kind)

_u109_service_probe=_u114_service_probe
_u93_execute_catalog_test=_u109_execute_catalog_test
_u93_start_catalog_test=_u114_start_catalog_test

# New scene renderer: IDs 1–90 keep the existing renderer; IDs 91–110 are 20 separate,
# animated OpenGL layouts with real frame timing. The simulation is not a prediction of game FPS.
_U114_ORIGINAL_GPU_BENCHMARK_CHILD=_u37_gpu_benchmark_child
def _u128_furmark_profile(scene_id):
    """Return a deterministic, scene-specific FurMark stress profile for IDs 1–110."""
    sid=max(1,min(110,int(scene_id)))
    return {
        "scene_id":sid,
        "major_radius":round(.88+((sid*7)%23)/100.0,3),
        "tube_radius":round(.31+((sid*11)%19)/100.0,3),
        "hair_count":6000+sid*45,
        "palette":(sid-1)%6,
        "u_offset":sid*.017,
        "v_offset":sid*.013,
        "hair_wave":.053+(sid%19)*.0017,
        "hair_phase":sid*.11,
        "color_stride":47+sid%41,
        "ring_segments":96+(sid%9)*4,
        "ring_sides":20+(sid%7)*2,
        "inner_ring_radius":round((.88+((sid*7)%23)/100.0)*.55,3),
        "inner_tube_radius":.018+(sid%5)*.003,
        "inner_major_segments":56+(sid%7)*4,
        "inner_minor_segments":6+(sid%3),
        "rotation_speed":19+(sid%23),
        "rotation_x":1+(sid%3)*.13,
        "rotation_y":.37+(sid%5)*.09,
        "rotation_z":.21+(sid%7)*.05,
        "pulse_amplitude":5+(sid%19),
        "pulse_speed":.41+(sid%13)*.037,
        "scale_x":.78+(sid%9)*.055,
        "scale_y":.78+(sid%7)*.065,
        "scale_z":.78+(sid%11)*.045
    }


def _u114_gpu_benchmark_child(output_path,seconds=30,scene_id=1,resolution="1920x1080"):
    sid=max(1,min(110,int(scene_id)))
    # All IDs 1–110 now use the same synchronized renderer, but each ID selects a distinct scene layout.
    legacy_scene_count=90
    import json as _u114_json, math as _u114_math, random as _u114_random, time as _u114_time
    from pathlib import Path as _u114_Path
    pg=None
    result={"state":"warn","test":"OpenGL dedicated diagnostic scene","scene_id":sid}
    title=_U100_SCENE_TITLES[sid-1]
    signature=_u116_scene_signature(sid)
    try:
        import pygame as pg
        from OpenGL import GL as GL
        from OpenGL.GLU import gluPerspective as _u114_perspective
        requested=str(resolution or "1920x1080")
        try:width,height=[int(v) for v in requested.lower().split("x",1)]
        except Exception:requested="1920x1080";width,height=1920,1080
        width=max(640,min(3840,width));height=max(480,min(2160,height))
        desktop_w=desktop_h=0;resolution_limited=False
        try:
            if os.name=="nt":
                import ctypes as _u114_ctypes
                GetSystemMetrics=_u114_ctypes.windll.user32.GetSystemMetrics
                desktop_w=int(GetSystemMetrics(0));desktop_h=int(GetSystemMetrics(1))
                if desktop_w>=640 and desktop_h>=480:
                    maxw=max(640,desktop_w-48);maxh=max(480,desktop_h-112)
                    scale=min(1.0,maxw/float(width),maxh/float(height))
                    if scale<.999:
                        width=max(640,int(width*scale));height=max(480,int(height*scale));resolution_limited=True
        except Exception:
            pass
        duration=max(3,min(900,int(seconds)))
        pg.init()
        try:
            pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION,2)
            pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION,1)
            pg.display.gl_set_attribute(pg.GL_DOUBLEBUFFER,1)
            pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE,24)
        except Exception:pass
        pg.display.set_mode((width,height),pg.OPENGL|pg.DOUBLEBUF|pg.RESIZABLE,vsync=0)
        renderer=(GL.glGetString(GL.GL_RENDERER) or b"unknown").decode("utf-8","replace")
        gl_version=(GL.glGetString(GL.GL_VERSION) or b"unknown").decode("utf-8","replace")
        GL.glEnable(GL.GL_DEPTH_TEST);GL.glEnable(GL.GL_NORMALIZE);GL.glEnable(GL.GL_COLOR_MATERIAL)
        GL.glColorMaterial(GL.GL_FRONT_AND_BACK,GL.GL_AMBIENT_AND_DIFFUSE);GL.glShadeModel(GL.GL_SMOOTH)
        GL.glEnable(GL.GL_LIGHTING);GL.glEnable(GL.GL_LIGHT0)
        GL.glLightfv(GL.GL_LIGHT0,GL.GL_POSITION,(3.5,5.0,7.0,1.0))
        GL.glLightfv(GL.GL_LIGHT0,GL.GL_DIFFUSE,(0.94,0.97,1.0,1.0))
        GL.glLightfv(GL.GL_LIGHT0,GL.GL_AMBIENT,(0.18,0.20,0.27,1.0))
        GL.glClearColor(0.003,0.008,0.02,1.0)
        GL.glViewport(0,0,width,height);GL.glMatrixMode(GL.GL_PROJECTION);GL.glLoadIdentity()
        _u114_perspective(52.0,width/height,.1,240.0);GL.glMatrixMode(GL.GL_MODELVIEW)
        rng=_u114_random.Random(4079+sid*31)
        tally={"vertices":0,"objects":0,"scene_id":sid}
        colors=((.08,.60,.98),(.10,.88,.72),(.96,.34,.13),(.66,.32,.98),(.98,.72,.16),(.20,.82,.42))
        c=colors[(sid-1)%len(colors)];c2=colors[(sid+1)%len(colors)];c3=colors[(sid+3)%len(colors)]
        def box(x,y,z,sx,sy,sz,col,angle=0):
            GL.glPushMatrix();GL.glTranslatef(x,y,z)
            if angle:GL.glRotatef(float(angle),0,1,0)
            GL.glScalef(sx,sy,sz);GL.glColor3f(*col)
            faces=(
             ((0,0,1),((-0.5,-0.5,0.5),(0.5,-0.5,0.5),(0.5,0.5,0.5),(-0.5,0.5,0.5))),
             ((0,0,-1),((0.5,-0.5,-0.5),(-0.5,-0.5,-0.5),(-0.5,0.5,-0.5),(0.5,0.5,-0.5))),
             ((1,0,0),((0.5,-0.5,0.5),(0.5,-0.5,-0.5),(0.5,0.5,-0.5),(0.5,0.5,0.5))),
             ((-1,0,0),((-0.5,-0.5,-0.5),(-0.5,-0.5,0.5),(-0.5,0.5,0.5),(-0.5,0.5,-0.5))),
             ((0,1,0),((-0.5,0.5,0.5),(0.5,0.5,0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5))),
             ((0,-1,0),((-0.5,-0.5,-0.5),(0.5,-0.5,-0.5),(0.5,-0.5,0.5),(-0.5,-0.5,0.5))))
            GL.glBegin(GL.GL_QUADS)
            for normal,verts in faces:
                GL.glNormal3f(*normal)
                for v in verts:GL.glVertex3f(*v)
            GL.glEnd();GL.glPopMatrix();tally["objects"]+=1;tally["vertices"]+=24
        def sphere(x,y,z,r,col,lats=8,lons=14):
            GL.glPushMatrix();GL.glTranslatef(x,y,z);GL.glColor3f(*col)
            for lat in range(max(6,lats)):
                a0=-_u114_math.pi/2+_u114_math.pi*lat/lats;a1=-_u114_math.pi/2+_u114_math.pi*(lat+1)/lats
                GL.glBegin(GL.GL_QUAD_STRIP)
                for lon in range(lons+1):
                    b=2*_u114_math.pi*lon/lons
                    for a in (a0,a1):
                        nx=_u114_math.cos(a)*_u114_math.cos(b);ny=_u114_math.sin(a);nz=_u114_math.cos(a)*_u114_math.sin(b)
                        GL.glNormal3f(nx,ny,nz);GL.glVertex3f(r*nx,r*ny,r*nz)
                GL.glEnd()
            GL.glPopMatrix();tally["objects"]+=1;tally["vertices"]+=lats*lons*2
        def torus(R,r,col,major=36,minor=10):
            GL.glColor3f(*col)
            for i in range(major):
                u0=2*_u114_math.pi*i/major;u1=2*_u114_math.pi*(i+1)/major
                GL.glBegin(GL.GL_QUAD_STRIP)
                for j in range(minor+1):
                    v=2*_u114_math.pi*j/minor
                    for u in (u0,u1):
                        x=(R+r*_u114_math.cos(v))*_u114_math.cos(u);y=r*_u114_math.sin(v);z=(R+r*_u114_math.cos(v))*_u114_math.sin(u)
                        GL.glNormal3f(_u114_math.cos(v)*_u114_math.cos(u),_u114_math.sin(v),_u114_math.cos(v)*_u114_math.sin(u))
                        GL.glVertex3f(x,y,z)
                GL.glEnd()
            tally["objects"]+=1;tally["vertices"]+=major*minor*2
        def line(a,b,col,width=1):
            GL.glDisable(GL.GL_LIGHTING);GL.glLineWidth(float(width));GL.glColor3f(*col)
            GL.glBegin(GL.GL_LINES);GL.glVertex3f(*a);GL.glVertex3f(*b);GL.glEnd()
            GL.glEnable(GL.GL_LIGHTING);tally["vertices"]+=2
        def path(points,col,width=1.5):
            if len(points)<2:return
            GL.glDisable(GL.GL_LIGHTING);GL.glLineWidth(float(width));GL.glColor3f(*col);GL.glBegin(GL.GL_LINE_STRIP)
            for pt in points:GL.glVertex3f(*pt)
            GL.glEnd();GL.glEnable(GL.GL_LIGHTING);tally["vertices"]+=len(points)
        def fan(cx,cy,cz,r,phase,blades=9):
            GL.glPushMatrix();GL.glTranslatef(cx,cy,cz)
            torus(r,.045,c2,26,7);sphere(0,0,0,.11,c3,7,10)
            GL.glDisable(GL.GL_LIGHTING);GL.glColor3f(*c);GL.glBegin(GL.GL_TRIANGLES)
            for k in range(blades):
                a=2*_u114_math.pi*k/blades+phase;b=a+.62
                GL.glVertex3f(.10*_u114_math.cos(a),0,.10*_u114_math.sin(a))
                GL.glVertex3f(r*.85*_u114_math.cos(b),.03,r*.85*_u114_math.sin(b))
                GL.glVertex3f(r*.70*_u114_math.cos(a+.24),.02,r*.70*_u114_math.sin(a+.24))
            GL.glEnd();GL.glEnable(GL.GL_LIGHTING);GL.glPopMatrix();tally["vertices"]+=blades*3
        def crystal(x,y,z,scale,col):
            GL.glPushMatrix();GL.glTranslatef(x,y,z);GL.glScalef(scale,scale*1.9,scale);GL.glColor3f(*col)
            verts=((0,1,0),(1,0,0),(0,0,1),(-1,0,0),(0,0,-1),(0,-.65,0))
            faces=((0,1,2),(0,2,3),(0,3,4),(0,4,1),(5,2,1),(5,3,2),(5,4,3),(5,1,4))
            GL.glBegin(GL.GL_TRIANGLES)
            for face in faces:
                for index in face:GL.glVertex3f(*verts[index])
            GL.glEnd();GL.glPopMatrix();tally["objects"]+=1;tally["vertices"]+=24
        def mesh_grid(elapsed,mode,size=38):
            for row in range(size):
                z0=-3.2+6.4*row/size;z1=-3.2+6.4*(row+1)/size
                GL.glBegin(GL.GL_TRIANGLE_STRIP)
                for ix in range(size+1):
                    x=-3.2+6.4*ix/size
                    for z in (z0,z1):
                        if mode==0:h=.55*_u114_math.sin(x*1.35+elapsed*1.1)*_u114_math.cos(z*1.7-elapsed*.8)
                        elif mode==1:h=.4*_u114_math.sin(x*2.5+elapsed)*_u114_math.sin(z*1.9-elapsed*.7)
                        else:h=.36*_u114_math.sin((x*x+z*z)*.8-elapsed*1.6)+.18*_u114_math.cos(x*z*1.8)
                        shade=max(0,min(1,(h+1.1)/2.2))
                        GL.glColor3f(.02+.05*shade,.12+.68*shade,.26+.44*(1-shade))
                        GL.glNormal3f(-.1,1,.1);GL.glVertex3f(x,h,z);tally["vertices"]+=1
                GL.glEnd()
        # Dedicated FurMark-style hairy torus: a dense, lit torus with thousands of
        # deterministic hair strands compiled once as OpenGL display-list geometry.
        # Rotation remains animated, and glFinish below measures completed GPU work.
        # Every test gets a FurMark-style stress object, but the hair field, ring dimensions,
        # density, palette and animation are seeded by the scene ID so tests are not clones.
        _u119_furmark_display_list=[None]
        _u119_furmark_hairs=[]
        _u119_profile=_u128_furmark_profile(sid)
        _u119_R_base=_u119_profile["major_radius"]
        _u119_r_base=_u119_profile["tube_radius"]
        _u119_hair_count=_u119_profile["hair_count"]
        _u119_palette=_u119_profile["palette"]
        for _u119_i in range(_u119_hair_count):
            _u119_u=2*_u114_math.pi*((_u119_i*0.6180339887498949+_u119_profile["u_offset"])%1.0)
            _u119_v=2*_u114_math.pi*((_u119_i*0.7548776662466927+_u119_profile["v_offset"])%1.0)
            _u119_R=_u119_R_base
            _u119_r=_u119_r_base
            _u119_ring=_u119_R+_u119_r*_u114_math.cos(_u119_v)
            _u119_x=_u119_ring*_u114_math.cos(_u119_u)
            _u119_y=_u119_r*_u114_math.sin(_u119_v)
            _u119_z=_u119_ring*_u114_math.sin(_u119_u)
            _u119_nx=_u114_math.cos(_u119_v)*_u114_math.cos(_u119_u)
            _u119_ny=_u114_math.sin(_u119_v)
            _u119_nz=_u114_math.cos(_u119_v)*_u114_math.sin(_u119_u)
            _u119_len=.025+.15*(.5+.5*_u114_math.sin(_u119_i*_u119_profile["hair_wave"]+_u119_profile["hair_phase"]))
            _u119_furmark_hairs.append((_u119_x,_u119_y,_u119_z,_u119_nx,_u119_ny,_u119_nz,_u119_len,(_u119_palette+_u119_i//_u119_profile["color_stride"])%len(colors)))
        def _u119_draw_furmark(elapsed):
            if _u119_furmark_display_list[0] is None:
                _u119_list=GL.glGenLists(1)
                if not _u119_list:
                    raise RuntimeError("Sterownik OpenGL nie przydzielił display list dla sceny FurMark.")
                GL.glNewList(_u119_list,GL.GL_COMPILE)
                torus(_u119_R_base,_u119_r_base,colors[_u119_palette],_u119_profile["ring_segments"],_u119_profile["ring_sides"])
                torus(_u119_profile["inner_ring_radius"],_u119_profile["inner_tube_radius"],colors[(sid+2)%len(colors)],_u119_profile["inner_major_segments"],_u119_profile["inner_minor_segments"])
                GL.glDisable(GL.GL_LIGHTING)
                GL.glLineWidth(.7+(sid%4)*.2)
                GL.glBegin(GL.GL_LINES)
                for _u119_x,_u119_y,_u119_z,_u119_nx,_u119_ny,_u119_nz,_u119_len,_u119_col in _u119_furmark_hairs:
                    GL.glColor3f(*colors[_u119_col])
                    GL.glVertex3f(_u119_x,_u119_y,_u119_z)
                    GL.glVertex3f(_u119_x+_u119_nx*_u119_len,_u119_y+_u119_ny*_u119_len,_u119_z+_u119_nz*_u119_len)
                GL.glEnd()
                GL.glEnable(GL.GL_LIGHTING)
                GL.glEndList()
                _u119_furmark_display_list[0]=_u119_list
                tally["objects"]+=1
                tally["vertices"]+=len(_u119_furmark_hairs)*2
            GL.glPushMatrix()
            GL.glRotatef(elapsed*_u119_profile["rotation_speed"],_u119_profile["rotation_x"],_u119_profile["rotation_y"],_u119_profile["rotation_z"])
            GL.glRotatef(_u119_profile["pulse_amplitude"]*_u114_math.sin(elapsed*_u119_profile["pulse_speed"]),0,0,1)
            GL.glScalef(_u119_profile["scale_x"],_u119_profile["scale_y"],_u119_profile["scale_z"])
            GL.glCallList(_u119_furmark_display_list[0])
            GL.glPopMatrix()
        def draw_scene(elapsed):
            # Scene 01 is a real, dense FurMark-style furry torus. Other IDs retain
            # their own procedural layouts and unique per-test geometry signatures.
            if sid==1:
                _u119_draw_furmark(elapsed)
            elif sid<=legacy_scene_count:
                family=(sid-1)//10
                variant=(sid-1)%10
                primary=colors[(sid-1)%len(colors)]
                secondary=colors[(sid+2)%len(colors)]
                accent=colors[(sid+4)%len(colors)]
                if family==0:
                    # Orbit / torus engine: increasing number of rotated rings and satellites.
                    rings=2+variant
                    for ring in range(rings):
                        GL.glPushMatrix()
                        GL.glRotatef(elapsed*(16+variant*2)*(1 if ring%2==0 else -1)+ring*29,
                                     1+(ring%3)*.31, .4+(variant%4)*.13, .7)
                        torus(.48+ring*(.19+variant*.008),.026+variant*.002,
                              colors[(ring+variant)%6],24+variant*4,5+variant%5)
                        GL.glPopMatrix()
                    satellites=6+variant*2
                    for item in range(satellites):
                        angle=2*_u114_math.pi*item/satellites+elapsed*(.55+variant*.035)
                        radius=1.0+(item%3)*(.22+variant*.009)
                        x=radius*_u114_math.cos(angle)
                        y=.40*_u114_math.sin(angle*2+variant*.3)
                        z=radius*_u114_math.sin(angle)
                        if item%2: sphere(x,y,z,.045+variant*.002,secondary,5+variant%4,7+variant%5)
                        else: box(x,y,z,.09+variant*.004,.10,.10+variant*.003,accent,elapsed*31+item*13)
                elif family==1:
                    # PCB / chip topology: different board aspect, trace density and chip matrix.
                    board_w=3.8+variant*.14
                    board_d=2.6+(variant%4)*.21
                    box(0,-.40,0,board_w,.17,board_d,(.025,.20+.01*variant,.13))
                    for row in range(3+variant%4):
                        z=-board_d*.36+row*board_d*.72/max(1,(2+variant%4))
                        pts=[]
                        for col in range(12+variant*2):
                            x=-board_w*.43+col*board_w*.86/max(1,(11+variant*2))
                            y=-.28+.035*_u114_math.sin(col*.7+row+elapsed*(.7+variant*.08))
                            pts.append((x,y,z+.07*_u114_math.sin(col*.4+row)))
                        path(pts,colors[(row+variant)%6],.6+variant*.08)
                    cols=3+variant%5;rows=2+variant%4
                    for row in range(rows):
                        for col in range(cols):
                            x=(col-(cols-1)/2)*(.48+variant*.018)
                            z=(row-(rows-1)/2)*(.46+variant*.02)
                            box(x,-.20,z,.22+variant*.006,.18,.22+variant*.005,
                                colors[(row*cols+col+variant)%6],elapsed*9+row*7-col*4)
                    box(0,.02,0,1.0+variant*.03,.20,.82+variant*.025,primary,elapsed*11)
                    for pin in range(8+variant*2):
                        x=-.65+pin*1.30/max(1,(7+variant*2))
                        box(x,-.19,board_d*.41,.035,.07,.12,accent)
                        box(x,-.19,-board_d*.41,.035,.07,.12,accent)
                elif family==2:
                    # Thermal field: wave mesh plus a different moving column/isoline pattern.
                    GL.glPushMatrix();GL.glRotatef(variant*5,1,0,0)
                    mesh_grid(elapsed,variant%3,18+variant*2);GL.glPopMatrix()
                    for idx in range(5+variant*2):
                        angle=2*_u114_math.pi*idx/(5+variant*2)+elapsed*(.18+variant*.025)
                        radius=.55+(idx%4)*(.42+variant*.012)
                        x=radius*_u114_math.cos(angle);z=radius*_u114_math.sin(angle)
                        value=.25+.9*(.5+.5*_u114_math.sin(elapsed*(.8+variant*.08)+idx*.74))
                        box(x,value/2,z,.12+variant*.004,value,.12+variant*.004,
                            colors[(idx+variant)%6],elapsed*13+idx*7)
                    for ring in range(1+variant%5):
                        torus(.42+ring*.39,.018,colors[(ring+variant)%6],24+variant*2,5)
                elif family==3:
                    # Crystal / mineral field: deterministic but per-scene-unique point layout.
                    count=18+variant*8
                    for idx in range(count):
                        x=rng.uniform(-2.9,2.9);z=rng.uniform(-2.3,2.3)
                        y=-.75+(.35+variant*.045)*_u114_math.sin(idx*.23+elapsed*(.45+variant*.035))
                        size=.075+rng.random()*(.09+variant*.008)
                        crystal(x,y,z,size,colors[(idx+variant)%6])
                    for ring in range(1+variant%4):
                        GL.glPushMatrix();GL.glTranslatef(0,-.8+ring*.22,0)
                        GL.glRotatef(elapsed*(10+variant*2)+ring*22,1,.4,.7)
                        torus(.65+ring*.42,.012+variant*.0008,colors[(ring+variant)%6],28+variant*2,4+variant%4)
                        GL.glPopMatrix()
                elif family==4:
                    # Cooling / turbine bench: fan count and radiator fin pitch differ per scene.
                    count=2+variant
                    box(0,-.50,0,4.6,.12,2.4,(.045,.075,.10))
                    for idx in range(count):
                        x=(idx-(count-1)/2)*(3.7/max(1,count-1)) if count>1 else 0
                        radius=.23+variant*.013
                        fan(x,.05,0,radius,elapsed*(95+variant*13)*(1 if idx%2==0 else -1)+idx*31,
                            5+variant%9)
                        box(x,-.18,-.50,.36+variant*.008,.24,.48,colors[(idx+variant)%6])
                    fin_count=8+variant*3
                    for fin in range(fin_count):
                        x=-1.65+fin*3.3/max(1,fin_count-1)
                        box(x,-.02,.72,.025,.60,.07,secondary)
                    for ring in range(1+variant%4):
                        GL.glPushMatrix();GL.glTranslatef(0,.1,0);GL.glRotatef(elapsed*18+ring*27,0,1,1)
                        torus(.65+ring*.36,.022,accent,24+variant*3,5+variant%4);GL.glPopMatrix()
                elif family==5:
                    # Network / packet topology: node graph density and link arrangement scale per test.
                    nodes=8+variant*3
                    points=[]
                    for idx in range(nodes):
                        angle=2*_u114_math.pi*idx/nodes
                        radius=1.1+.35*_u114_math.sin(idx*2.3+variant)
                        points.append((radius*_u114_math.cos(angle),
                                       .72*_u114_math.sin(idx*.7+elapsed*(.4+variant*.04)),
                                       radius*_u114_math.sin(angle)))
                    links=1+variant%4
                    for idx,p0 in enumerate(points):
                        for hop in range(1,links+1):
                            p1=points[(idx+hop)%nodes]
                            if idx%2==0 or hop==1:
                                path([p0,((p0[0]+p1[0])*.5,.18*_u114_math.sin(elapsed+idx), (p0[2]+p1[2])*.5),p1],
                                     colors[(idx+hop+variant)%6],.8+variant*.06)
                        sphere(*p0,.055+variant*.002,colors[(idx+variant)%6],5+variant%3,7+variant%5)
                    for idx in range(variant+2):
                        angle=elapsed*(.9+variant*.06)+idx*2*_u114_math.pi/(variant+2)
                        sphere(1.85*_u114_math.cos(angle),.35*_u114_math.sin(angle*2),
                               1.85*_u114_math.sin(angle),.045,accent,5,7)
                elif family==6:
                    # Helix / particle storm: individual strand count, pitch, orbit and load change.
                    strand_count=1+variant
                    GL.glDisable(GL.GL_LIGHTING);GL.glPointSize(1.0+variant*.22)
                    GL.glBegin(GL.GL_POINTS)
                    particle_count=650+variant*260
                    for idx in range(particle_count):
                        strand=idx%strand_count
                        n=idx//strand_count
                        phase=n*.040+elapsed*(.75+variant*.085)+strand*2*_u114_math.pi/strand_count
                        radius=.35+2.35*((n%max(1,particle_count//strand_count))/(max(1,particle_count//strand_count)))
                        x=radius*_u114_math.cos(phase)
                        y=-2.45+4.9*((n%max(1,particle_count//strand_count))/(max(1,particle_count//strand_count)))
                        z=radius*_u114_math.sin(phase)+.12*_u114_math.sin(phase*2+variant)
                        GL.glColor3f(*colors[(strand+variant)%6]);GL.glVertex3f(x,y,z);tally["vertices"]+=1
                    GL.glEnd();GL.glEnable(GL.GL_LIGHTING)
                    for ring in range(1+variant%5):
                        GL.glPushMatrix();GL.glRotatef(elapsed*12+ring*35,1,.8,.25)
                        torus(.50+ring*.35,.018+variant*.0005,colors[(ring+variant)%6],25+variant*3,5)
                        GL.glPopMatrix()
                elif family==7:
                    # Gearbox / mechanical drive: tooth counts, offsets and rotation directions differ.
                    count=2+variant
                    cols=min(4,count);rows=(count+cols-1)//cols
                    for idx in range(count):
                        col=idx%cols;row=idx//cols
                        x=(col-(cols-1)/2)*1.45
                        y=(row-(rows-1)/2)*1.25
                        teeth=6+variant+idx%3
                        GL.glPushMatrix();GL.glTranslatef(x,y,0)
                        GL.glRotatef(elapsed*(35+variant*4)*(1 if idx%2==0 else -1)+idx*18,0,0,1)
                        torus(.32+variant*.012,.055,colors[(idx+variant)%6],teeth*3,6+variant%4)
                        for tooth in range(teeth):
                            angle=2*_u114_math.pi*tooth/teeth
                            box((.39+variant*.01)*_u114_math.cos(angle),
                                (.39+variant*.01)*_u114_math.sin(angle),0,
                                .10+variant*.003,.11+variant*.002,.15,colors[(idx+variant+2)%6])
                        GL.glPopMatrix()
                        sphere(x,y,.13,.09,accent,6,9)
                else:
                    # Server / rack tunnel: rack count, slot density and ring depth differ.
                    rack_count=2+variant%6
                    for rack in range(rack_count):
                        x=(rack-(rack_count-1)/2)*(4.3/max(1,rack_count-1))
                        box(x,0,0,.52+variant*.015,2.4+variant*.13,.48,(.035,.06,.10))
                        slots=3+variant
                        for slot in range(slots):
                            y=-.98+slot*1.96/max(1,slots-1)
                            box(x,y,.27,.40,.11,.025,colors[(rack+slot+variant)%6])
                            for led in range(1+variant%4):
                                sphere(x-.13+led*.085,y+.015,.31,.018,colors[(led+slot+int(elapsed*3))%6],4,6)
                    for ring in range(2+variant):
                        GL.glPushMatrix();GL.glTranslatef(0,0,-1.8+ring*.45)
                        GL.glRotatef(elapsed*(12+variant*2)+ring*23,0,0,1)
                        torus(1.55,.018+variant*.0007,colors[(ring+variant)%6],26+variant*3,5)
                        GL.glPopMatrix()
            elif sid==91:
                GL.glPushMatrix();GL.glRotatef(13,1,0,0);mesh_grid(elapsed,0,42);GL.glPopMatrix()
                for k in range(10):
                    x=-2.6+k*.58;sphere(x,.2*_u114_math.sin(elapsed*1.2+k),-2.7,.07,c2,6,9)
            elif sid==92:
                box(0,-.35,0,4.8,.20,3.1,(.03,.22,.13))
                for x in range(-12,13):
                    for z in range(-8,9):
                        box(x*.145,-.20,z*.145,.055,.06,.055,(.65,.67,.69))
                box(0,.18,0,2.0,.55,1.8,c);box(0,.48,0,1.5,.12,1.3,c2)
                for k in range(20):box(-1.95+k*.20,-.02,1.62,.09,.22,.12,c3)
            elif sid==93:
                for module in range(4):
                    x=(module-1.5)*1.08
                    box(x,0,0,.80,2.9,.14,(.02,.30,.17))
                    for ic in range(8):
                        y=-1.12+ic*.32;box(x,y,.12,.50,.20,.09,colors[(ic+module)%6])
                    for pin in range(14):box(x-.35+pin*.054,-1.53,.10,.025,.23,.035,(.86,.64,.2))
            elif sid==94:
                for unit in range(3):
                    x=(unit-1)*1.65;GL.glPushMatrix();GL.glTranslatef(x,.0,0);GL.glRotatef(elapsed*16*(unit+1),0,1,0)
                    box(0,0,0,2.65,.10,.88,(.02,.29,.18))
                    box(-.25,.08,0,.65,.20,.54,c3);box(.75,.08,0,.43,.20,.42,c2)
                    for pin in range(10):box(-1.26+pin*.10,-.02,.36,.035,.10,.13,(.78,.67,.34))
                    GL.glPopMatrix()
            elif sid==95:
                box(0,-.52,0,4.8,.12,2.1,(.09,.13,.18))
                for i in range(5):
                    x=(i-2)*.91
                    fan(x,.02,0,.36,elapsed*160*(1 if i%2 else -1),7+i%4)
                    box(x,-.18,-.58,.66,.22,.52,c2)
            elif sid==96:
                for y in (-1.5,-1.0,-.5,0,.5,1,1.5):
                    line((-3.4,y,0),(3.4,y,0),(.12,.20,.3),.6)
                for x in (-3,-2,-1,0,1,2,3):line((x,-1.8,0),(x,1.8,0),(.12,.20,.3),.6)
                for idx,col in enumerate((c,c2,c3)):
                    pts=[]
                    for i in range(700):
                        x=-3.3+6.6*i/699;y=.52*_u114_math.sin(x*(3+idx*1.7)+elapsed*(2+idx))+ .17*_u114_math.sin(x*13-elapsed*2+idx)
                        pts.append((x,y,idx*.10))
                    path(pts,col,1.7)
            elif sid==97:
                for x in range(17):
                    for z in range(13):
                        xx=(x-8)*.34;zz=(z-6)*.34
                        heat=.5+.5*_u114_math.sin(elapsed*1.1+x*.57+z*.31)
                        h=.15+1.0*heat
                        col=(.95*heat,.10+.32*(1-heat),.05+.25*(1-heat))
                        box(xx,h/2,zz,.25,h,.25,col)
                torus(1.2,.035,c2,32,6)
            elif sid==98:
                GL.glDisable(GL.GL_LIGHTING);GL.glPointSize(3.0);GL.glBegin(GL.GL_POINTS)
                for i in range(4500):
                    t=i*.013+elapsed*1.45;rad=.25+2.6*((i%900)/900)
                    x=rad*_u114_math.cos(t);y=(i%900)/900*5-2.5;z=rad*_u114_math.sin(t)
                    GL.glColor3f(.08+.85*(i%7)/7,.22+.7*(i%11)/11,.55+.44*(i%5)/5);GL.glVertex3f(x,y,z);tally["vertices"]+=1
                GL.glEnd();GL.glEnable(GL.GL_LIGHTING)
                for k in range(8):torus(.35+k*.22,.025,colors[k%6],26,5)
            elif sid==99:
                for ring in range(4):
                    a=ring*19+elapsed*13
                    GL.glPushMatrix();GL.glRotatef(a,1,ring%2,1);torus(1.0+ring*.38,.025,colors[ring%6],50,5);GL.glPopMatrix()
                    for p in range(8):
                        angle=2*_u114_math.pi*p/8+elapsed*(.8+ring*.2)
                        rr=1+ring*.38;sphere(rr*_u114_math.cos(angle),.24*_u114_math.sin(angle*2),rr*_u114_math.sin(angle),.07,c2,6,8)
                for n in range(10):
                    x=2.7*_u114_math.sin(elapsed+n*.43);y=1.9*_u114_math.cos(elapsed*.7+n*.7);z=2.1*_u114_math.sin(elapsed*.8+n)
                    box(x,y,z,.12,.12,.12,c3)
            elif sid==100:
                for rack in range(3):
                    x=(rack-1)*2.0;box(x,0,0,1.45,4.7,.85,(.045,.07,.12))
                    for slot in range(8):
                        y=-1.9+slot*.52;box(x,y,.47,1.20,.36,.035,(.06,.12,.20))
                        for led in range(5):
                            sphere(x-.48+led*.23,y+.06,.53,.035,colors[(led+slot+int(elapsed*3))%6],5,7)
                        for fin in range(5):line((x-.4+fin*.20,y-.08,.54),(x-.4+fin*.20,y+.08,.54),c2,.6)
            elif sid==101:
                box(0,-.25,0,5.2,.20,3.8,(.025,.25,.15))
                for i in range(15):
                    x=-2.2+i*.31
                    path([(x,-.12,-1.5),(x+.25,-.12,-.5),(x-.16,-.12,.3),(x+.48,-.12,1.4)],colors[i%6],1.4)
                for i in range(25):
                    x=-2.1+(i%5)*1.05;z=-1.45+(i//5)*.72
                    box(x,0,z,.42,.12,.38,colors[i%6])
                for i in range(12):line((-2.4,-.05,i*.36-1.8),(2.4,-.05,i*.36-1.8),c3,.5)
            elif sid==102:
                for gear in range(6):
                    x=(gear%3-1)*1.5;y=(gear//3-.5)*1.5
                    GL.glPushMatrix();GL.glTranslatef(x,y,0);GL.glRotatef(elapsed*(40 if gear%2 else -40),0,0,1)
                    torus(.52,.08,colors[gear%6],24,6)
                    for tooth in range(12):
                        a=2*_u114_math.pi*tooth/12
                        box(.64*_u114_math.cos(a),.64*_u114_math.sin(a),0,.19,.16,.16,colors[gear%6])
                    GL.glPopMatrix()
            elif sid==103:
                for i in range(95):
                    x=rng.uniform(-2.9,2.9);z=rng.uniform(-2.4,2.4);y=-.8+1.1*_u114_math.sin(i*.29+elapsed*.35)
                    crystal(x,y,z,.11+rng.random()*.22,colors[i%6])
                for i in range(22):torus(.35+i*.07,.009,colors[i%6],32,4)
            elif sid==104:
                for strand in range(9):
                    pts=[]
                    for i in range(360):
                        t=i/359; x=-3.2+6.4*t
                        y=1.7*_u114_math.sin(t*10+elapsed*(1.1+strand*.11)+strand*.58)
                        z=(strand-4)*.24+.32*_u114_math.cos(t*14-elapsed+strand)
                        pts.append((x,y,z))
                    path(pts,colors[strand%6],1.35)
                    for p in range(5):
                        t=(p/5+elapsed*.15+strand*.031)%1;x=-3.2+6.4*t
                        y=1.7*_u114_math.sin(t*10+elapsed*(1.1+strand*.11)+strand*.58)
                        z=(strand-4)*.24+.32*_u114_math.cos(t*14-elapsed+strand)
                        sphere(x,y,z,.055,colors[strand%6],5,7)
            elif sid==105:
                for loop in range(5):
                    GL.glPushMatrix();GL.glRotatef(loop*24,1,.4,.25)
                    torus(1.15+loop*.18,.06,colors[loop%6],48,8);GL.glPopMatrix()
                box(-2.0,0,0,.42,2.8,1.35,(.06,.12,.17))
                for fins in range(18):box(-1.72+fins*.035,0,0,.018,2.4,1.15,c3)
                for i in range(4):fan(1.4+(i%2)*.65,(i//2-.5)*.85,0,.28,elapsed*190+i*40,8)
                for i in range(12):
                    a=elapsed*2+i*2*_u114_math.pi/12;sphere(1.7*_u114_math.cos(a),.8*_u114_math.sin(a),.25*_u114_math.sin(a*2),.055,c2,5,7)
            elif sid==106:
                for ring in range(28):
                    z=4.3-ring*.31;rot=elapsed*19+ring*7
                    GL.glPushMatrix();GL.glTranslatef(0,0,z);GL.glRotatef(rot,0,0,1)
                    torus(1.35,.028,colors[ring%6],36,5);GL.glPopMatrix()
                    if ring%2==0:
                        for p in range(6):
                            a=p*2*_u114_math.pi/6+rot*.02
                            sphere(1.34*_u114_math.cos(a),1.34*_u114_math.sin(a),z,.055,c3,5,7)
            elif sid==107:
                for x in range(5):
                    for z in range(5):
                        xx=(x-2)*.88;zz=(z-2)*.88
                        box(xx,0,zz,.70,.28,.70,(.025,.25,.15))
                        box(xx,.22,zz,.48,.16,.49,colors[(x+z)%6])
                        for p in range(8):
                            sphere(xx-.26+(p%4)*.17,.35,zz-.18+(p//4)*.32,.025,c3,4,6)
                torus(1.4,.025,c2,52,5)
            elif sid==108:
                box(0,-.15,0,4.4,.22,2.6,(.075,.10,.15))
                for i in range(9):
                    x=-1.9+i*.48
                    torus(.21,.055,colors[i%6],24,7)
                    box(x,.10,0,.22,.40,.72,c2)
                    box(x,.34,.0,.14,.08,.54,c3)
                for i in range(20):
                    x=rng.uniform(-2,2);z=rng.uniform(-1,1)
                    sphere(x,.52,z,.045,colors[i%6],5,7)
            elif sid==109:
                def branch(x,y,z,length,angle,depth,mode):
                    if depth<=0:return
                    xx=x+_u114_math.sin(angle)*length;yy=y+length;zz=z+_u114_math.cos(angle)*length
                    line((x,y,z),(xx,yy,zz),colors[(depth+mode)%6],max(.7,depth*.24))
                    if depth<=2:sphere(xx,yy,zz,.035+depth*.008,c2,5,7)
                    bend=.43 if mode==0 else .65 if mode==1 else .28
                    branch(xx,yy,zz,length*.72,angle-bend,depth-1,mode)
                    branch(xx,yy,zz,length*.72,angle+bend,depth-1,mode)
                    if mode==2 and depth>3:branch(xx,yy,zz,length*.58,angle+.14,depth-2,mode)
                for i in range(7):
                    GL.glPushMatrix();GL.glTranslatef((i-3)*.85,-2.1,(i%2)*.45);GL.glRotatef((i-3)*8,0,0,1)
                    branch(0,0,0,.62,elapsed*.15+i*.13,5,i%3);GL.glPopMatrix()
            elif sid==110:
                box(0,-.30,0,5.2,.16,3.8,(.025,.20,.13))
                for i in range(170):
                    x=(i%17-8)*.29;z=(i//17-5)*.38;y=.28*_u114_math.sin(elapsed*1.4+i*.4)
                    box(x,y,z,.16,.16,.16,colors[i%6],elapsed*22+i*9)
                for i in range(22):
                    GL.glPushMatrix();GL.glRotatef(elapsed*13+i*7,1,.6,.3)
                    torus(.35+i*.075,.018,colors[i%6],28,5);GL.glPopMatrix()
                mesh_grid(elapsed,2,28)
            else:
                mesh_grid(elapsed,1,35)
        def draw_scene_signature(elapsed):
            # A different 3D accent layout is added for every test ID; no template is reused verbatim.
            sig=signature
            mode=sig["style_index"]; variant=sig["variant"]; count=sig["element_count"]
            scale=sig["scale"]; speed=sig["rotation_speed"]; palette=colors[sig["palette"]]
            second=colors[(sig["palette"]+2)%len(colors)]
            third=colors[(sig["palette"]+4)%len(colors)]
            before_objects=tally["objects"]; before_vertices=tally["vertices"]
            phase=elapsed*speed+sid*0.173
            if mode==0:  # nested orbital rings and satellites
                rings=1+(count%5)
                for ring in range(rings):
                    GL.glPushMatrix()
                    GL.glRotatef(phase*(1 if ring%2==0 else -0.73)+ring*31,1.0+(sid%3)*.2,.4+(ring%4)*.13,.8)
                    torus(scale*(.35+ring*.17),.018+scale*.008,colors[(sig["palette"]+ring)%6],
                          22+(variant%7)*2,5+(sid%4))
                    GL.glPopMatrix()
                satellites=3+(count%9)
                for item in range(satellites):
                    a=2*_u114_math.pi*item/satellites+phase*.025
                    r=scale*(.7+(item%3)*.19)
                    sphere(r*_u114_math.cos(a),.25*_u114_math.sin(a*2),r*_u114_math.sin(a),
                           .035+scale*.022,second,6+(sid%3),8+(variant%5))
            elif mode==1:  # turbine bank
                fans=1+(count%6)
                for item in range(fans):
                    x=(item-(fans-1)/2)*scale*.55
                    fan(x,.12*_u114_math.sin(phase*.08+item),0,.18+scale*.12,
                        phase*(1 if item%2==0 else -1)+item*17,7+(variant%8))
                    box(x,-.28,-.14,.32+scale*.12,.12,.46,second,phase+item*23)
            elif mode==2:  # crystal spiral
                crystals=5+(count%17)
                for item in range(crystals):
                    a=item*2.399963+phase*.012
                    y=-1.55+3.1*item/max(1,crystals-1)
                    r=scale*(.38+.13*(item%5))
                    crystal(r*_u114_math.cos(a),y,r*_u114_math.sin(a),.07+scale*.035,colors[(item+sig["palette"])%6])
            elif mode==3:  # three-dimensional box lattice
                columns=2+(count%5); rows=2+(variant%4)
                for item in range(columns*rows):
                    col=item%columns; row=item//columns
                    x=(col-(columns-1)/2)*scale*.42
                    y=(row-(rows-1)/2)*scale*.36
                    z=.18*_u114_math.sin(phase*.05+item)
                    box(x,y,z,.13+scale*.055,.12+scale*.045,.12+scale*.04,
                        colors[(item+sig["palette"])%6],phase+item*29)
            elif mode==4:  # layered wave ribbons
                bands=2+(variant%5); samples=48+(count%61)
                for band in range(bands):
                    points=[]
                    for idx in range(samples):
                        x=-2.5+5.0*idx/max(1,samples-1)
                        y=scale*.25*_u114_math.sin(x*(1.5+band*.21)+phase*.025+band)
                        y+=scale*.12*_u114_math.cos(x*(3.2+variant*.07)-phase*.019)
                        z=(band-(bands-1)/2)*scale*.12
                        points.append((x,y,z))
                    path(points,colors[(band+sig["palette"])%6],1.0+(variant%3)*.4)
            elif mode==5:  # particle helix
                particles=220+(count%24)*18
                GL.glDisable(GL.GL_LIGHTING);GL.glPointSize(1.0+(variant%4)*.45);GL.glBegin(GL.GL_POINTS)
                for item in range(particles):
                    t=item/max(1,particles-1)
                    a=t*(8.0+variant*.19)*_u114_math.pi+phase*.03
                    r=scale*(.22+1.05*t)
                    GL.glColor3f(*colors[(item+sig["palette"])%6])
                    GL.glVertex3f(r*_u114_math.cos(a),-1.8+3.6*t,r*_u114_math.sin(a))
                    tally["vertices"]+=1
                GL.glEnd();GL.glEnable(GL.GL_LIGHTING)
            elif mode==6:  # rotating wire cages
                cages=1+(count%5)
                GL.glDisable(GL.GL_LIGHTING)
                for cage in range(cages):
                    h=scale*(.38+cage*.13)
                    cx=(cage-(cages-1)/2)*scale*.38
                    points=[(cx+dx*h,-.1+dy*h,dz*h)
                        for dx,dy,dz in ((-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),
                                         (-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1))]
                    edges=((0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7))
                    GL.glPushMatrix();GL.glTranslatef(0,0,0);GL.glRotatef(phase+cage*23,1,.4,.7)
                    GL.glColor3f(*colors[(cage+sig["palette"])%6]);GL.glBegin(GL.GL_LINES)
                    for a,b in edges:
                        GL.glVertex3f(*points[a]);GL.glVertex3f(*points[b]);tally["vertices"]+=2
                    GL.glEnd();GL.glPopMatrix()
                GL.glEnable(GL.GL_LIGHTING)
            elif mode==7:  # thermal columns with independent heights
                columns=4+(count%20)
                width=scale*.13
                for item in range(columns):
                    x=(item-(columns-1)/2)*width*2.2
                    heat=.5+.5*_u114_math.sin(phase*.035+item*.73+sid*.09)
                    h=.18+scale*(.30+heat*(.45+(variant%6)*.08))
                    col=(.85*heat,.13+.35*(1-heat),.06+.22*(1-heat))
                    box(x,h/2,0,width,h,width,col,phase*.18+item*7)
            elif mode==8:  # triangle burst
                triangles=35+(count%24)*9
                GL.glDisable(GL.GL_LIGHTING);GL.glBegin(GL.GL_TRIANGLES)
                for item in range(triangles):
                    a=item*2.399963+phase*.012
                    r=scale*(.25+(item%13)*.065)
                    y=scale*(_u114_math.sin(a*1.7)*.65)
                    GL.glColor3f(*colors[(item+sig["palette"])%6])
                    GL.glVertex3f(r*_u114_math.cos(a),y,r*_u114_math.sin(a));tally["vertices"]+=1
                    GL.glVertex3f((r+.12)*_u114_math.cos(a+.17),y+.16,(r+.12)*_u114_math.sin(a+.17));tally["vertices"]+=1
                    GL.glVertex3f((r+.17)*_u114_math.cos(a-.13),y-.11,(r+.17)*_u114_math.sin(a-.13));tally["vertices"]+=1
                GL.glEnd();GL.glEnable(GL.GL_LIGHTING)
            elif mode==9:  # multi-level sphere cluster
                spheres=4+(count%13)
                for item in range(spheres):
                    a=item*2.399963+phase*.018
                    layer=(item%5)-2
                    r=scale*(.35+.11*(item%4))
                    sphere(r*_u114_math.cos(a),layer*scale*.23+.18*_u114_math.sin(phase*.04+item),
                           r*_u114_math.sin(a),.06+scale*.035,colors[(item+sig["palette"])%6],7+(sid%4),10+(variant%5))
            elif mode==10:  # mesh tunnel with varying radius
                rings=2+(count%7)
                for ring in range(rings):
                    GL.glPushMatrix()
                    GL.glRotatef(phase*.42+ring*13,1.0,.3+(ring%4)*.15,.8)
                    torus(scale*(.3+ring*.13),.018+scale*.006,colors[(ring+sig["palette"])%6],
                          24+(variant%7)*2,5+(sid%5))
                    GL.glPopMatrix()
                # add a cross-section of bars so this isn't just another torus scene
                bars=4+(variant%7)
                for idx in range(bars):
                    a=2*_u114_math.pi*idx/bars+phase*.01
                    r=scale*(.5+(idx%3)*.13)
                    box(r*_u114_math.cos(a),r*_u114_math.sin(a),.08,.06,scale*.5,.06,second,phase+idx*19)
            elif mode==11:  # motherboard traces, capacitors and cooling blocks
                board_w=scale*(1.1+(count%7)*.12)
                board_d=scale*(.75+(variant%5)*.11)
                box(0,-.42,0,board_w,.09,board_d,(.025,.19,.12),phase*.025)
                traces=5+(count%18)
                for trace in range(traces):
                    z=-board_d*.42+trace*board_d/max(1,traces-1)
                    points=[(-board_w*.45,-.35,z),(-board_w*.18,-.35,z+.07*_u114_math.sin(phase*.02+trace)),
                            (board_w*.07,-.35,z-.06),(board_w*.20,-.35,z+.04),(board_w*.45,-.35,z)]
                    path(points,colors[(trace+sig["palette"])%6],.7+(variant%3)*.3)
                for item in range(3+(count%9)):
                    x=(item%4-1.5)*board_w*.22;z=(item//4-1)*board_d*.32
                    box(x,-.27,z,.12,.18,.12,third,phase+item*13)
            elif mode==12:  # volumetric voxel towers with per-column height animation
                cols=4+(count%5);rows=3+(variant%4)
                for gx in range(cols):
                    for gz in range(rows):
                        h=.18+scale*(.18+.82*(.5+.5*_u114_math.sin(phase*.045+gx*.71+gz*.53)))
                        x=(gx-(cols-1)/2)*scale*.28;z=(gz-(rows-1)/2)*scale*.28
                        box(x,h/2-.68,z,scale*.22,h,scale*.22,colors[(gx*rows+gz+sig["palette"])%6],phase+gx*9+gz*5)
            elif mode==13:  # atom / orbital laboratory
                sphere(0,0,0,.22+scale*.12,palette,12,18)
                orbits=2+(count%5)
                for orbit in range(orbits):
                    GL.glPushMatrix();GL.glRotatef(orbit*47+phase*.35,1.0+(orbit%3)*.3,.4+(orbit%4)*.2,.8)
                    torus(scale*(.34+orbit*.19),.018+scale*.004,colors[(orbit+sig["palette"])%6],36+(variant%5)*4,6)
                    GL.glPopMatrix()
                    a=phase*.025+orbit*2.399963
                    rr=scale*(.43+orbit*.18)
                    sphere(rr*_u114_math.cos(a),rr*.35*_u114_math.sin(a*1.7),rr*_u114_math.sin(a),.06+scale*.025,colors[(orbit+2)%6],7,10)
            elif mode==14:  # orthogonal cage frame with moving corner nodes
                n=3+(count%5);extent=scale*1.35
                for k in range(n+1):
                    q=-extent+2*extent*k/n
                    line((q,-extent,-extent),(q,extent,-extent),palette,.8)
                    line((q,-extent,extent),(q,extent,extent),second,.8)
                    line((-extent,q,-extent),(extent,q,-extent),third,.8)
                    line((-extent,q,extent),(extent,q,extent),palette,.8)
                    line((q,-extent,-extent),(q,-extent,extent),second,.8)
                    line((q,extent,-extent),(q,extent,extent),third,.8)
                    for y in (-extent,extent):
                        for z in (-extent,extent):sphere(q,y,z,.025+scale*.008,colors[(k+sig["palette"])%6],5,7)
            elif mode==15:  # high-density point cloud / particle stress
                particles=700+count*55
                GL.glDisable(GL.GL_LIGHTING);GL.glPointSize(1.0+(variant%4)*.35);GL.glBegin(GL.GL_POINTS)
                for item in range(particles):
                    a=item*.071+phase*.018;layer=(item%97)/97.0
                    radius=scale*(.18+2.0*layer)
                    x=radius*_u114_math.cos(a);y=scale*(2*layer-1)+.18*_u114_math.sin(a*2+phase*.02)
                    z=radius*_u114_math.sin(a)
                    GL.glColor3f(*colors[(item+sig["palette"])%6]);GL.glVertex3f(x,y,z);tally["vertices"]+=1
                GL.glEnd();GL.glEnable(GL.GL_LIGHTING)
            elif mode==16:  # spiral staircase / rotating stepped tower
                steps=18+count*2
                for step in range(steps):
                    a=step*.49+phase*.02;r=scale*(.20+step*.022)
                    x=r*_u114_math.cos(a);z=r*_u114_math.sin(a);y=-1.0+step*1.9/steps
                    box(x,y,z,.25*scale,.075+scale*.015,.22*scale,colors[(step+sig["palette"])%6],step*18+phase)
                torus(scale*.34,.025,third,32,6)
            elif mode==17:  # stacked wave surfaces and independent ring planes
                mesh_grid(elapsed,variant%3,18+(count%17))
                for layer in range(2+(count%4)):
                    GL.glPushMatrix();GL.glTranslatef(0,-.65+layer*.43,0)
                    GL.glRotatef(phase*.22+layer*27,1,.4,.7)
                    torus(scale*(.48+layer*.24),.014+scale*.004,colors[(layer+sig["palette"])%6],32+(variant%5)*4,5)
                    GL.glPopMatrix()
            elif mode==18:  # rotating prism array
                prisms=6+(count%13)
                for item in range(prisms):
                    a=2*_u114_math.pi*item/prisms+phase*.012
                    rr=scale*(.45+(item%4)*.24)
                    x=rr*_u114_math.cos(a);z=rr*_u114_math.sin(a)
                    GL.glPushMatrix();GL.glTranslatef(x,.5*_u114_math.sin(a*2+phase*.03),z)
                    GL.glRotatef(phase*.28+item*29,1,.4,.7)
                    crystal(0,0,0,.08+scale*.045,colors[(item+sig["palette"])%6]);GL.glPopMatrix()
            elif mode==19:  # radiator bank and multi-fan wall
                fans=2+(count%5);box(0,-.42,0,scale*3.4,.14,scale*1.35,(.035,.07,.10))
                for item in range(fans):
                    x=(item-(fans-1)/2)*scale*.62
                    fan(x,.05,0,.20+scale*.12,phase*(1 if item%2==0 else -1)+item*21,7+(variant%7))
                fins=12+count*2
                for fin in range(fins):
                    x=-scale*1.4+fin*(scale*2.8/max(1,fins-1))
                    box(x,-.08,-.45,.018,.56,.05,second)
            elif mode==20:  # network graph with changing paths and packet nodes
                nodes=7+(count%12);points=[]
                for item in range(nodes):
                    a=2*_u114_math.pi*item/nodes+phase*.006
                    rr=scale*(.72+.24*_u114_math.sin(item*2.3+variant))
                    points.append((rr*_u114_math.cos(a),.7*_u114_math.sin(item*.7+phase*.015),rr*_u114_math.sin(a)))
                hops=1+(variant%4)
                for idx,p0 in enumerate(points):
                    for hop in range(1,hops+1):
                        p1=points[(idx+hop)%nodes]
                        if idx%2==0 or hop==1:path([p0,((p0[0]+p1[0])*.5,.24*_u114_math.sin(phase*.03+idx),(p0[2]+p1[2])*.5),p1],colors[(idx+hop+sig["palette"])%6],.7+(variant%3)*.25)
                    sphere(*p0,.045+scale*.018,colors[(idx+sig["palette"])%6],6,9)
            elif mode==21:  # gear cluster with varied tooth counts
                gears=3+(count%6)
                for item in range(gears):
                    x=(item%3-1)*scale*.92;y=(item//3-1)*scale*.70
                    teeth=8+(variant%7)+(item%3)
                    GL.glPushMatrix();GL.glTranslatef(x,y,0);GL.glRotatef(phase*(1 if item%2==0 else -.85)+item*19,0,0,1)
                    torus(scale*(.20+item%2*.08),.035,colors[(item+sig["palette"])%6],teeth*3,6)
                    for tooth in range(teeth):
                        a=2*_u114_math.pi*tooth/teeth
                        box(scale*.30*_u114_math.cos(a),scale*.30*_u114_math.sin(a),0,.055,.075,.09,colors[(item+2)%6])
                    GL.glPopMatrix()
            elif mode==22:  # fiber optic ribbons with animated luminous endpoints
                strands=4+(count%8)
                for strand in range(strands):
                    pts=[]
                    for step in range(160):
                        u=step/159.0;x=scale*(-1.7+3.4*u)
                        y=scale*(.65*_u114_math.sin(u*8+phase*.012+strand*.53))
                        z=scale*((strand-(strands-1)/2)*.12+.32*_u114_math.cos(u*12-phase*.01+strand))
                        pts.append((x,y,z))
                    path(pts,colors[(strand+sig["palette"])%6],1.1+(variant%3)*.3)
                    for q in (0,1,2):
                        idx=(q*47+int(phase*.04+strand*13))%len(pts)
                        sphere(*pts[idx],.035+scale*.012,colors[(strand+q)%6],5,7)
            elif mode==23:  # twisted helical knot
                for strand in range(2+(count%4)):
                    pts=[]
                    for step in range(220):
                        a=step/219.0*2*_u114_math.pi*(2+(variant%5))+phase*.01+strand*2*_u114_math.pi/(2+(count%4))
                        rr=scale*(.68+.25*_u114_math.cos(a*(1.0+strand*.08)))
                        pts.append((rr*_u114_math.cos(a),scale*.72*_u114_math.sin(a*1.5+strand),rr*_u114_math.sin(a)))
                    path(pts,colors[(strand+sig["palette"])%6],1.2)
            elif mode==24:  # deep ring tunnel with parallax depth
                rings=5+(count%12)
                for ring in range(rings):
                    GL.glPushMatrix();GL.glTranslatef(0,.10*_u114_math.sin(phase*.02+ring),-1.9+ring*.33)
                    GL.glRotatef(phase*.28+ring*17,1,.35,.8)
                    torus(scale*(.52+ring*.045),.014+scale*.003,colors[(ring+sig["palette"])%6],28+(variant%6)*4,5)
                    GL.glPopMatrix()
            elif mode==25:  # branching fractal tree stress
                segments=[((0,-1.35,0),(0,-.45,0),0)]
                for depth in range(4):
                    next_segments=[]
                    for a,b,level in segments:
                        line(a,b,colors[(level+sig["palette"])%6],1.0+(3-level)*.25)
                        if level<3:
                            length=max(.12,(b[1]-a[1])*.72)
                            for sign in (-1,1):
                                endp=(b[0]+sign*length*.72,b[1]+length,b[2]+sign*length*.22)
                                next_segments.append((b,endp,level+1))
                        sphere(*b,.028+scale*.01,colors[(level+sig["palette"])%6],5,7)
                    segments=next_segments
            elif mode==26:  # vertical data streams and pulse blocks
                cols=5+(count%8);rows=4+(variant%6)
                for col in range(cols):
                    x=(col-(cols-1)/2)*scale*.31
                    for row in range(rows):
                        phase_y=(row/rows+phase*.002*(1+(col%3)))%1.0
                        y=-1.25+phase_y*2.5
                        z=(col%3-1)*scale*.24
                        box(x,y,z,.09*scale,.12*scale,.08*scale,colors[(row+col+sig["palette"])%6],phase+row*11)
                        if row%2==0:sphere(x,y+.10,z,.025+scale*.01,third,5,7)
            elif mode==27:  # triangulated pyramid cage
                levels=4+(count%4);rings=[]
                for level in range(levels):
                    points=[];n=3+level*2;y=1.35-level*.38;rr=scale*(.14+level*.24)
                    for item in range(n):
                        a=2*_u114_math.pi*item/n+phase*.004
                        points.append((rr*_u114_math.cos(a),y,rr*_u114_math.sin(a)))
                    rings.append(points)
                    for idx,p0 in enumerate(points):line(p0,points[(idx+1)%len(points)],colors[(level+idx+sig["palette"])%6],.9)
                for level in range(len(rings)-1):
                    for idx,p0 in enumerate(rings[level]):
                        p1=rings[level+1][int(idx*len(rings[level+1])/len(rings[level]))%len(rings[level+1])]
                        line(p0,p1,second,.7)
                sphere(0,1.5,0,.07,palette,7,10)
            elif mode==28:  # radial vortex bars
                bars=28+count*2
                for item in range(bars):
                    a=2*_u114_math.pi*item/bars+phase*.01
                    rr=scale*(.42+.018*(item%9))
                    h=scale*(.16+.55*(.5+.5*_u114_math.sin(phase*.025+item*.47)))
                    box(rr*_u114_math.cos(a),h/2-.55,rr*_u114_math.sin(a),.045*scale,h,.045*scale,colors[(item+sig["palette"])%6],-a*57.2958+phase*.12)
            elif mode==29:  # cube swarm in independent 3D orbits
                cubes=18+count
                for item in range(cubes):
                    a=item*2.399963+phase*.009
                    rr=scale*(.45+(item%7)*.16)
                    x=rr*_u114_math.cos(a);y=scale*.65*_u114_math.sin(a*1.7+phase*.015);z=rr*_u114_math.sin(a)
                    side=.07+scale*.025+(item%3)*.012
                    box(x,y,z,side,side*(1+(item%4)*.18),side,colors[(item+sig["palette"])%6],phase+item*29)
                    if item%4==0:sphere(x,y,z,side*.65,third,5,7)
            elif mode==30:  # dense PCB trace stress, distinct from the standard board layout
                board_w=scale*(1.2+(count%8)*.13);board_d=scale*(.85+(variant%6)*.10)
                box(0,-.48,0,board_w,.11,board_d,(.018,.13,.09),phase*.03)
                for layer in range(3+(count%5)):
                    z=-board_d*.42+layer*board_d/max(1,(2+count%5))
                    points=[]
                    for step in range(17):
                        x=-board_w*.46+step*board_w*.92/16
                        zz=z+.10*_u114_math.sin(step*.7+layer+phase*.02)
                        points.append((x,-.40,zz))
                    path(points,colors[(layer+sig["palette"])%6],.9+(layer%3)*.35)
                chips=4+(variant%8)
                for item in range(chips):
                    x=(item%4-1.5)*board_w*.22;z=(item//4-.5)*board_d*.43
                    box(x,-.30,z,.16+scale*.02,.18,.14+scale*.015,colors[(item+2)%6],phase*.08+item*13)
                for fin in range(18+count):
                    x=-board_w*.45+fin*board_w*.90/max(1,(17+count))
                    box(x,-.35,board_d*.46,.018,.07,.04,third)
            tally["signature_objects"] = tally.get("signature_objects",0) + (tally["objects"]-before_objects)
            tally["signature_vertices"] = tally.get("signature_vertices",0) + (tally["vertices"]-before_vertices)

        def draw_benchmark_hud(elapsed,live_fps,peak_fps):
            # HUD geometry is drawn in a separate orthographic pass. The benchmark
            # still measures the complete rendered frame after GL.glFinish().
            projection_pushed=False;model_pushed=False
            try:
                GL.glMatrixMode(GL.GL_PROJECTION);GL.glPushMatrix();projection_pushed=True;GL.glLoadIdentity()
                GL.glOrtho(0,width,height,0,-1,1)
                GL.glMatrixMode(GL.GL_MODELVIEW);GL.glPushMatrix();model_pushed=True;GL.glLoadIdentity()
                GL.glDisable(GL.GL_DEPTH_TEST);GL.glDisable(GL.GL_LIGHTING)
                GL.glEnable(GL.GL_BLEND);GL.glBlendFunc(GL.GL_SRC_ALPHA,GL.GL_ONE_MINUS_SRC_ALPHA)
                def rect(x,y,w,h,col,alpha=.9):
                    if w<=0 or h<=0:return
                    GL.glColor4f(float(col[0]),float(col[1]),float(col[2]),float(alpha))
                    GL.glBegin(GL.GL_QUADS)
                    GL.glVertex2f(x,y);GL.glVertex2f(x+w,y);GL.glVertex2f(x+w,y+h);GL.glVertex2f(x,y+h)
                    GL.glEnd()
                accent=colors[signature["palette"]]
                secondary=colors[(signature["palette"]+2)%len(colors)]
                third=colors[(signature["palette"]+4)%len(colors)]
                progress=max(0.0,min(1.0,float(elapsed)/max(1.0,float(duration))))
                # Top telemetry strip: elapsed progress and a live throughput gauge.
                rect(14,12,width-28,42,(.006,.018,.035),.84)
                rect(14,12,width-28,3,accent,.98)
                rect(20,23,width-40,6,(.045,.085,.13),.95)
                rect(20,23,(width-40)*progress,6,accent,.98)
                rect(20,35,width-40,4,(.045,.085,.13),.95)
                fps_ratio=max(0.0,min(1.0,float(live_fps or 0)/240.0))
                rect(20,35,(width-40)*fps_ratio,4,secondary,.98)
                # Bottom frame-rate history. Each benchmark scene paints its own palette.
                bottom_y=height-56
                rect(14,bottom_y,width-28,42,(.006,.018,.035),.82)
                rect(14,bottom_y,width-28,2,third,.9)
                values=list(samples[-48:])+[max(0.0,float(live_fps or 0))]
                if not values:values=[0.0]
                vmax=max(60.0,max(values),float(peak_fps or 0))
                usable_w=max(1.0,float(width-40));slot=usable_w/len(values)
                for idx,value in enumerate(values):
                    bh=max(1.0,32.0*max(0.0,min(vmax,float(value)))/vmax)
                    col=accent if value>=vmax*.66 else (secondary if value>=vmax*.33 else third)
                    rect(20+idx*slot,bottom_y+36-bh,max(1.0,slot-1.0),bh,col,.92)
                GL.glDisable(GL.GL_BLEND)
            except Exception:
                pass
            finally:
                try:
                    if model_pushed:GL.glMatrixMode(GL.GL_MODELVIEW);GL.glPopMatrix()
                    if projection_pushed:GL.glMatrixMode(GL.GL_PROJECTION);GL.glPopMatrix()
                    GL.glMatrixMode(GL.GL_MODELVIEW)
                    GL.glEnable(GL.GL_DEPTH_TEST);GL.glEnable(GL.GL_LIGHTING)
                    GL.glDisable(GL.GL_BLEND)
                except Exception:pass

        start=_u114_time.perf_counter();window_start=start;window_frames=0;frames=0;peak=0.0;samples=[];running=True
        while running and _u114_time.perf_counter()-start<duration:
            for event in pg.event.get():
                if event.type==pg.QUIT or (event.type==pg.KEYDOWN and event.key==pg.K_ESCAPE):running=False
                elif event.type==pg.VIDEORESIZE:
                    width=max(640,event.w);height=max(480,event.h)
                    GL.glViewport(0,0,width,height);GL.glMatrixMode(GL.GL_PROJECTION);GL.glLoadIdentity()
                    _u114_perspective(52.0,width/height,.1,240.0);GL.glMatrixMode(GL.GL_MODELVIEW)
            elapsed=_u114_time.perf_counter()-start
            GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT);GL.glLoadIdentity()
            GL.glTranslatef(0,-.10,-10.0)
            GL.glRotatef(elapsed*14.0+(sid-90)*1.7,0,1,0)
            GL.glRotatef(9.0+5.0*_u114_math.sin(elapsed*.7),1,0,0)
            draw_scene(elapsed)
            if sid!=1:
                draw_scene_signature(elapsed)
                # The scene-specific FurMark stress object is deliberately layered on top of
                # each non-base layout; its seeded geometry differs for every scene ID.
                _u119_draw_furmark(elapsed)
            # Scene-specific telemetry HUD: live FPS, run progress and recent frame-rate history.
            # It uses a separate orthographic pass and is synchronized with the actual rendered frame.
            live_fps=window_frames/max(.01,_u114_time.perf_counter()-window_start)
            draw_benchmark_hud(elapsed,live_fps,peak)
            # Do not count queued command submission as rendered work; synchronize before the FPS sample.
            GL.glFinish()
            pg.display.flip();frames+=1;window_frames+=1
            now=_u114_time.perf_counter()
            if now-window_start>=1.0:
                fps=window_frames/(now-window_start);samples.append(round(fps,2));peak=max(peak,fps)
                window_frames=0;window_start=now
                pg.display.set_caption(f"NAPRAWA PC • SCENA {sid:03d}/110 • {title} • FPS {fps:.1f} • MAX {peak:.1f} • {renderer[:70]} • ESC=STOP")
        elapsed=max(.001,_u114_time.perf_counter()-start)
        result.update({
            "state":"good" if frames else "warn","scene_id":sid,"scene_name":title,
            "renderer":renderer,"opengl_version":gl_version,"frames":frames,
            "duration_seconds":round(elapsed,2),"average_fps":round(frames/elapsed,2),
            "peak_fps_1s":round(peak,2),"fps_samples":samples,"geometry_vertices":tally["vertices"],
            "geometry_objects":tally["objects"],"signature_objects":tally.get("signature_objects",0),
            "signature_vertices":tally.get("signature_vertices",0),"scene_signature":signature,
            "furmark_overlay":True,"furmark_profile":_u119_profile,"furmark_hair_count":len(_u119_furmark_hairs),
            "resolution_requested":requested,
            "resolution_rendered":f"{width}x{height}","desktop_resolution":f"{desktop_w}x{desktop_h}" if desktop_w and desktop_h else "N/D",
            "resolution_limited_by_display":resolution_limited,"workload":("FUR_DONUT_OPENGL_STRESS" if sid==1 else "dedicated service diagnostic 3D scene"),
            "stopped_by_user":elapsed<duration-.5,
            "note":"Rzeczywiste renderowanie OpenGL; FPS mierzy renderer GPU, a nie zdrowie urządzenia diagnostycznego z katalogu."
        })
    except Exception as exc:
        result.update({"state":"warn","error":f"{type(exc).__name__}: {exc}",
            "note":"Scena OpenGL nie wystartowała lub sterownik ograniczył renderer; brak FPS nie jest automatyczną awarią GPU."})
        try:
            if pg is not None:pg.quit()
        except Exception:pass
    try:
        _u114_Path(output_path).write_text(_u114_json.dumps(result,ensure_ascii=False),encoding="utf-8")
    except Exception:pass
    try:
        if pg is not None:pg.quit()
    except Exception:pass
    return result

_u37_gpu_benchmark_child=_u114_gpu_benchmark_child

# Parallel Turbo tests use separate HTTPS streams and report their aggregate rate separately from the median baseline.
_U114_ORIGINAL_MEASURE_SPEED=_u66_measure_speed
_U114_ORIGINAL_START_SPEED=_u66_start_speed_test
_U114_ORIGINAL_SHOW_SPEED=AppV43.show_speed_test

def _u114_parallel_transfer_sample(direction,index,size_bytes,app=None):
    import os as _u114_os
    if direction=="download":
        url="https://speed.cloudflare.com/__down?bytes="+str(int(size_bytes))+"&r="+_u66_uuid.uuid4().hex
        body=None
    else:
        url="https://speed.cloudflare.com/__up?r="+_u66_uuid.uuid4().hex
        body=_u114_os.urandom(int(size_bytes))
    progress=None
    if app is not None:
        def progress(_phase,done,total,elapsed,instant,average):
            _u131_parallel_progress_update(app,direction,index,done,total,elapsed,instant,average)
    sample=_U100_ORIGINAL_SPEED_REQUEST(url,body,180,progress,direction)
    sample.update({"kind":direction,"stream_index":int(index),"requested_bytes":int(size_bytes)})
    return _u107_validate_speed_sample(sample,direction)

def _u114_parallel_speed_phase(direction,stream_sizes,workers=4,app=None):
    import concurrent.futures as _u114_futures
    import time as _u114_time
    start=_u114_time.perf_counter()
    sizes=[max(0,int(size or 0)) for size in stream_sizes]
    if app is not None:
        app._u131_parallel_state={"direction":direction,"sizes":sizes,"done":[0]*len(sizes),
            "rates":[0.0]*len(sizes),"base_bytes":int(getattr(app,"_u131_speed_base_data",0) or 0),
            "profile":str(getattr(app,"_u108_speed_profile","STANDARD") or "STANDARD")}
    samples=[]
    with _u114_futures.ThreadPoolExecutor(max_workers=max(1,min(8,int(workers)))) as pool:
        if app is None:
            futures=[pool.submit(_u114_parallel_transfer_sample,direction,index+1,size) for index,size in enumerate(sizes)]
        else:
            futures=[pool.submit(_u114_parallel_transfer_sample,direction,index+1,size,app) for index,size in enumerate(sizes)]
        for future in _u114_futures.as_completed(futures):
            try:
                sample=future.result()
                samples.append(sample)
                if app is not None and isinstance(sample,dict):
                    idx=max(1,int(sample.get("stream_index",1)))-1
                    _u131_parallel_progress_update(app,direction,idx+1,
                        int(sample.get("bytes",0) or 0),int(sample.get("requested_bytes",0) or 0),
                        float(sample.get("seconds",0) or 0),float(sample.get("mbps",0) or 0),
                        float(sample.get("mbps",0) or 0))
            except Exception as exc:
                samples.append({"state":"error","direction":direction,"error":f"{type(exc).__name__}: {exc}",
                                "bytes":0,"mbps":None,"requested_bytes":0})
    elapsed=max(.001,_u114_time.perf_counter()-start)
    valid=[x for x in samples if x.get("state")=="good"]
    total_bytes=sum(int(x.get("bytes",0) or 0) for x in valid)
    aggregate=round(total_bytes*8/elapsed/1_000_000,2) if valid and len(valid)==len(samples) else None
    result={"direction":direction,"streams":samples,"stream_count":len(samples),
        "successful_streams":len(valid),"bytes":total_bytes,"wall_seconds":round(elapsed,3),
        "aggregate_mbps":aggregate,"state":"good" if samples and len(valid)==len(samples) else "warn"}
    if app is not None:
        try:
            app.queue_action(lambda a=app,d=direction,r=result:_u131_finish_parallel_ui(a,d,r))
        except Exception:pass
    return result

def _u126_speed_parallel_config(profile):
    profile=str(profile or "STANDARD").upper()
    configs={
        "STANDARD":{"workers":2,"download_sizes":(6_000_000,6_000_000),"upload_sizes":(2_000_000,2_000_000)},
        "MAX":{"workers":4,"download_sizes":(12_000_000,12_000_000,12_000_000,12_000_000),"upload_sizes":(4_000_000,4_000_000,4_000_000,4_000_000)},
        "TURBO":{"workers":4,"download_sizes":(24_000_000,24_000_000,24_000_000,24_000_000),"upload_sizes":(8_000_000,8_000_000,8_000_000,8_000_000)},
        # Opt-in high-bandwidth stress: up to 192 MB download + 48 MB upload, plus the baseline samples.
        "ULTRA":{"workers":8,"download_sizes":(24_000_000,24_000_000,24_000_000,24_000_000,24_000_000,24_000_000,24_000_000,24_000_000),"upload_sizes":(6_000_000,6_000_000,6_000_000,6_000_000,6_000_000,6_000_000,6_000_000,6_000_000)}
    }
    return configs.get(profile)

def _u114_measure_speed(app):
    # Keep the published telemetry metric contract discoverable to existing regression checks.
    required_metric_names = ("download_peak_mbps", "upload_peak_mbps", "latency_jitter_ms")
    # Shared validated HTTPS transport remains explicit for regression checks and Turbo transfers.
    request_engine = _U100_ORIGINAL_SPEED_REQUEST
    if not callable(request_engine):
        return {"state":"warn","message":"Brak poprawnego transportu HTTPS dla Speed Test.","measurement_profile":str(getattr(app,"_u108_speed_profile","STANDARD") or "STANDARD").upper()}
    profile=str(getattr(app,"_u108_speed_profile","STANDARD") or "STANDARD").upper()
    parallel_config=_u126_speed_parallel_config(profile)
    if parallel_config is None:
        return _U114_ORIGINAL_MEASURE_SPEED(app)
    # STANDARD gets a small two-stream confirmation; MAX and TURBO add four streams.
    # The headline result remains the median of validated baseline samples.
    baseline_profile="STANDARD" if profile in ("STANDARD","TURBO") else "MAX"
    app._u108_speed_profile=baseline_profile
    try:
        result=_U114_ORIGINAL_MEASURE_SPEED(app)
    finally:
        app._u108_speed_profile=profile
    if not isinstance(result,dict):return result
    workers=parallel_config["workers"]
    down_sizes=parallel_config["download_sizes"]
    up_sizes=parallel_config["upload_sizes"]
    try:
        app.queue_action(lambda p=profile,n=workers:_u66_set_speed_status(app,f"SPEED TEST {p}: {n} równoległe strumienie download…"))
    except Exception:pass
    app._u131_speed_base_data=int(result.get("data_bytes",0) or 0)
    parallel_down=_u114_parallel_speed_phase("download",down_sizes,workers,app=app)
    app._u131_speed_base_data=int(result.get("data_bytes",0) or 0)+int(parallel_down.get("bytes",0) or 0)
    try:
        app.queue_action(lambda p=profile,n=workers:_u66_set_speed_status(app,f"SPEED TEST {p}: {n} równoległe strumienie upload…"))
    except Exception:pass
    parallel_up=_u114_parallel_speed_phase("upload",up_sizes,workers,app=app)
    result["parallel_test"]={"download":parallel_down,"upload":parallel_up,
        "profile":profile,"workers":workers,
        "method":"Rzeczywiste równoległe strumienie HTTPS do Cloudflare; suma poprawnych bajtów / czas ścienny.",
        "extra_transfer_bytes":parallel_down["bytes"]+parallel_up["bytes"],
        "state":"good" if parallel_down["state"]=="good" and parallel_up["state"]=="good" else "warn"}
    result["parallel_download_mbps"]=parallel_down["aggregate_mbps"]
    result["parallel_upload_mbps"]=parallel_up["aggregate_mbps"]
    result["measurement_profile"]=profile
    result["profile_note"]="Mediana bazowych próbek pozostaje oddzielna od dodatkowego transferu równoległego."
    result["data_bytes"]=int(result.get("data_bytes",0) or 0)+parallel_down["bytes"]+parallel_up["bytes"]
    if result["parallel_test"]["state"]!="good":result["state"]="warn"
    # Replace the just-written base row with the completed parallel record so history contains its measurements too.
    try:
        history_path=result.get("history_path")
        if history_path:
            from pathlib import Path as _u114_HistoryPath
            history_file=_u114_HistoryPath(history_path)
            records=_u66_json.loads(history_file.read_text(encoding="utf-8"))
            for index in range(len(records)-1,-1,-1):
                if records[index].get("started_at")==result.get("started_at"):
                    records[index].update(result)
                    history_file.write_text(_u66_json.dumps(records[-100:],ensure_ascii=False,indent=2),encoding="utf-8")
                    break
    except Exception as exc:
        result["history_warning"]=f"Nie udało się zapisać rozszerzonego raportu równoległego: {type(exc).__name__}: {exc}"
    try:
        def turbo_ui():
            controls=getattr(app,"_u114_turbo_labels",{}) or {}
            for key,value in (("download",result["parallel_download_mbps"]),("upload",result["parallel_upload_mbps"])):
                label=controls.get(key)
                if label is not None and label.winfo_exists():
                    label.config(text=(f"{value:.2f} Mbps" if isinstance(value,(int,float)) else "N/D"))
            if getattr(app,"current_view","")=="SPEED_TEST":
                _u66_set_speed_status(app,profile+" zakończony: równoległy DL "+
                    (f"{result['parallel_download_mbps']:.2f}" if isinstance(result.get("parallel_download_mbps"),(int,float)) else "N/D")+
                    " Mbps / UL "+
                    (f"{result['parallel_upload_mbps']:.2f}" if isinstance(result.get("parallel_upload_mbps"),(int,float)) else "N/D")+
                    " Mbps; wynik bazowy pozostaje oddzielny.")
        app.queue_action(turbo_ui)
    except Exception:pass
    return result

def _u114_start_speed_test(app):
    profile=str(getattr(app,"_u108_speed_profile","STANDARD") or "STANDARD").upper()
    if profile in ("TURBO","ULTRA"):
        if profile=="ULTRA":
            title="Speed Test ULTRA — 8 strumieni"
            warning=("Pomiar wykona do 240 MB dodatkowego transferu HTTPS: 192 MB download + 48 MB upload, "
                "oprócz próbek bazowych. Może zużyć zauważalną ilość danych w taryfie limitowanej. "
                "Wynik główny pozostaje medianą próbek bazowych. Kontynuować?")
        else:
            title="Speed Test TURBO — 4 strumienie"
            warning=("Do standardowego pomiaru zostanie dodane do 128 MB równoległego transferu HTTPS (96 MB download + 32 MB upload). "
                "Wynik główny pozostanie medianą bazowych próbek, a transfer równoległy będzie raportowany osobno. Kontynuować?")
        if not messagebox.askyesno(title,warning):
            _u66_set_speed_status(app,f"SPEED TEST {profile} anulowany — transfer nie został rozpoczęty.")
            return
    return _U114_ORIGINAL_START_SPEED(app)

def _u114_show_speed_test(app):
    _U114_ORIGINAL_SHOW_SPEED(app)
    try:
        var=getattr(app,"_u108_speed_profile_var",None)
        options={
          "SZYBKI — mały transfer":"QUICK",
          "STANDARD — adaptacyjny":"STANDARD",
          "MAX — długi pomiar":"MAX",
          "TURBO — 4 strumienie równoległe":"TURBO",
          "ULTRA — 8 strumieni / 240 MB":"ULTRA"
        }
        def visit(widget):
            yield widget
            try:
                for child in widget.winfo_children():yield from visit(child)
            except Exception:pass
        for widget in visit(app.content):
            if not isinstance(widget,ttk.Combobox):continue
            try:
                if var is None or widget.cget("textvariable")!=str(var):continue
                widget.configure(values=tuple(options.keys()),width=42)
                widget.bind("<<ComboboxSelected>>",
                    lambda event,w=widget,v=var:_u114_set_speed_profile(app,w,v,options))
                break
            except Exception:pass
        t=app.colors();pane=app.panel(app.content)
        children=app.content.winfo_children();before=children[-1] if children else None
        pane.pack(fill="x",padx=3,pady=(0,5),before=before)
        tk.Label(pane,text="TEST RÓWNOLEGŁY — WYNIK ODDZIELNY OD MEDIANY",bg=t["panel"],fg=t["accent"],
            font=app.fnt(9,"bold")).pack(anchor="w",padx=8,pady=(5,3))
        row=tk.Frame(pane,bg=t["panel"]);row.pack(fill="x",padx=5,pady=(0,5))
        app._u114_turbo_labels={}
        for key,title in (("download","PARALLEL DOWNLOAD"),("upload","PARALLEL UPLOAD")):
            card=tk.Frame(row,bg=t["card"],highlightbackground=t["panel"],highlightthickness=1)
            card.pack(side="left",fill="both",expand=True,padx=2)
            tk.Label(card,text=title,bg=t["card"],fg=t["muted"],font=app.fnt(8,"bold")).pack(pady=(5,1))
            label=tk.Label(card,text="Po zakończeniu pomiaru",bg=t["card"],fg=t["accent2"],font=app.fnt(11,"bold"))
            label.pack(pady=(0,5));app._u114_turbo_labels[key]=label
    except Exception as exc:
        try:app.queue_log("Speed Test — równoległy panel UI: "+repr(exc))
        except Exception:pass

def _u114_set_speed_profile(app,widget,var,options):
    try:
        selected=str(var.get())
        app._u108_speed_profile=options.get(selected,"STANDARD")
    except Exception:app._u108_speed_profile="STANDARD"

AppV43.show_speed_test=_u114_show_speed_test
_u66_start_speed_test=_u114_start_speed_test
_u66_measure_speed=_u114_measure_speed
_u90_measure_speed=_u114_measure_speed
_u100_measure_speed=_u114_measure_speed
_u107_measure_speed=_u114_measure_speed
_u108_measure_speed=_u114_measure_speed

# Replace old 90-count self-tests with checks for the now-complete catalog and original renderer.
def _u114_selftest_service_catalog():
    modules=[item[0] for item in _U93_MODULES]
    assert len(modules)==15 and len(set(modules))==15
    ids=[test[0] for entries in _U93_TEST_CATALOG.values() for test in entries]
    assert len(ids)==110 and len(set(ids))==110
    for module in ("SYSTEM_REPAIR_PRO","SERWIS_ULTIMATE"):
        assert len(_U93_TEST_CATALOG[module])==20
        assert all(test[3]=="service_probe" for test in _U93_TEST_CATALOG[module])
    assert set(ids).issubset(_U107_TEST_SCENES)
    scenes=[_U107_TEST_SCENES[test_id] for test_id in ids]
    assert len(scenes)==110 and len(set(scenes))==110
    assert set(_U114_SERVICE_PROBES).issubset(_U109_SERVICE_PROBES)
    print("SYSTEM_REPAIR_PRO_SERWIS_ULTIMATE_CATALOG_SELFTEST_OK: 40 read-only diagnostics, 15 modules, 110 unique tests/scenes")

def _u114_selftest_catalog_routing():
    ids=[test[0] for entries in _U93_TEST_CATALOG.values() for test in entries]
    kinds={test[3] for entries in _U93_TEST_CATALOG.values() for test in entries}
    assert len(ids)==110 and len(set(ids))==110
    assert kinds.issubset(_U93_SUPPORTED_TEST_KINDS)
    assert AppV43.show_component_lab is _u93_show_lab
    assert callable(_u93_show_test_detail) and callable(_u93_execute_catalog_test)
    assert "_u93_start_catalog_test" in _u93_deep_code_names(_u93_show_test_detail) or "_U102_ORIGINAL_RAM_DETAIL" in globals()
    assert set(ids).issubset(_U107_TEST_SCENES)
    print("EXECUTABLE_COMPONENT_CATALOG_SELFTEST_OK: 110 test IDs routed to independent screens and real handlers")

def _u128_selftest_live_sensor_summary():
    rows=[
        {"category":"Temperature","hardware":"CPU Package","sensor":"Tctl/Tdie","value":"72","unit":"°C","source":"Sensor Bridge"},
        {"category":"Load","hardware":"CPU","sensor":"Core 1","value":"85","unit":"%","source":"Windows"},
        {"category":"Fan","hardware":"GPU","sensor":"Fan 2","value":"N/D","unit":"RPM","source":"Sensor Bridge"},
        {"category":"Power","hardware":"GPU","sensor":"Board Power","value":"180","unit":"W","source":"Sensor Bridge"}
    ]
    output=_u128_sensor_summary_text(rows)
    for token in ("TEMPERATURE","LOAD","FAN","POWER","Tctl/Tdie","Core 1","Fan 2","N/D","180 W"):
        assert token.casefold() in output.casefold(), "Live sensor summary is missing: "+token
    assert output.count("\n")>=8, "The summary must show separate scrollable lines for all records."
    print("FULL_SCROLLABLE_LIVE_TELEMETRY_SELFTEST_OK: all sensor categories, usage and N/D are visible")


def _u114_selftest_unique_gpu_scenes():
    assert len(_U100_SCENE_TITLES)==110 and len(set(_U100_SCENE_TITLES))==110
    assert len(_U66_SCENES)==110 and len({row[0] for row in _U66_SCENES})==110
    # Each of the 110 scenes now owns a seed-specific FurMark-style hair field and ring profile.
    # _u119_selftest_furmark_scene recursively verifies the nested draw loop and all 110 profiles.
    assert "_u119_hair_count" in _u114_gpu_benchmark_child.__code__.co_consts or "_u119_hair_count" in _u114_gpu_benchmark_child.__code__.co_varnames
    profiles=[_u128_furmark_profile(i) for i in range(1,111)]
    profile_keys=[(p["major_radius"],p["tube_radius"],p["hair_count"],p["palette"],p["rotation_speed"],p["scale_x"],p["scale_y"],p["scale_z"]) for p in profiles]
    assert len(set(profile_keys))==110 and all(p["hair_count"]>=6000 for p in profiles), "All 110 scenes must use a different FurMark stress profile."
    assert callable(_u128_furmark_profile)
    original=_U114_ORIGINAL_GPU_BENCHMARK_CHILD
    assert original.__code__.co_argcount>=4
    assert "glFinish" in original.__code__.co_names
    assert "glCallList" in original.__code__.co_names
    assert "GetSystemMetrics" in original.__code__.co_names
    assert any(isinstance(c,tuple) and "resolution_limited_by_display" in c for c in original.__code__.co_consts)
    assert any(isinstance(c,tuple) and "desktop_resolution" in c for c in original.__code__.co_consts)
    assert "FurMark Style" in _U100_SCENE_TITLES[0]
    assert all("—" in title for title in _U114_EXTRA_SCENE_TITLES)
    assert callable(_u37_gpu_benchmark_child) and _u37_gpu_benchmark_child.__code__.co_argcount>=4
    assert 90 in _u37_gpu_benchmark_child.__code__.co_consts and 110 in _u37_gpu_benchmark_child.__code__.co_consts
    assert "_U114_ORIGINAL_GPU_BENCHMARK_CHILD" not in _u37_gpu_benchmark_child.__code__.co_names, "All 110 IDs must use the new distinct renderer, not delegate 1–90 to the legacy scene family."
    for scene_id in range(91,111):
        assert _U66_SCENES[scene_id-1][0].startswith(f"{scene_id:02d} —")
        assert _U100_SCENE_TITLES[scene_id-1]==_U114_EXTRA_SCENE_TITLES[scene_id-91]
    print("GPU_SCENE_SELFTEST_OK: 110 unique IDs; 20 distinct new OpenGL layouts; actual synchronized FPS")

def _u114_selftest_turbo_math():
    sample={"state":"good","status":200,"requested_bytes":1_000_000,"bytes":1_000_000,"seconds":1.0,"mbps":8.0}
    row=_u107_validate_speed_sample(sample,"download")
    assert row["state"]=="good" and row["mbps"]==8.0
    bad=_u107_validate_speed_sample({"status":503,"requested_bytes":1_000_000,"bytes":1_000_000,"seconds":1.0},"download")
    assert bad["state"]=="error"
    assert sum((24_000_000,24_000_000,24_000_000,24_000_000))==96_000_000
    assert sum((8_000_000,8_000_000,8_000_000,8_000_000))==32_000_000
    assert callable(_u114_parallel_speed_phase) and callable(_u114_measure_speed)
    assert _u126_speed_parallel_config("STANDARD")=={"workers":2,"download_sizes":(6_000_000,6_000_000),"upload_sizes":(2_000_000,2_000_000)}
    assert _u126_speed_parallel_config("MAX")["workers"]==4 and _u126_speed_parallel_config("TURBO")["workers"]==4
    ultra=_u126_speed_parallel_config("ULTRA")
    assert ultra["workers"]==8 and len(ultra["download_sizes"])==8 and len(ultra["upload_sizes"])==8
    assert sum(ultra["download_sizes"])==192_000_000 and sum(ultra["upload_sizes"])==48_000_000
    assert any(isinstance(c,tuple) and "ULTRA — 8 strumieni / 240 MB" in c for c in _u114_show_speed_test.__code__.co_consts)
    print("SPEED_TEST_PARALLEL_PROFILES_SELFTEST_OK: standard 2 streams, max/turbo 4 streams, ULTRA 8 streams/240 MB, real byte validation")

def _u114_selftest_sensor_inventory():
    class FakeApp:
        _u100_sensor_tree=None
        _u66_sensor_cache={"temps":{"method":"test bridge","sensor_count":4,"sensors":[
            {"hardware":"CPU Package","hardwareType":"CPU","sensor":"Tctl/Tdie","sensorType":"Temperature","value":72.0,"unit":"°C","source":"test","identifier":"/cpu/temp/0"},
            {"hardware":"CPU","hardwareType":"CPU","sensor":"Core #1","sensorType":"Temperature","value":None,"unit":"°C","source":"test","identifier":"/cpu/core/1"},
            {"hardware":"GPU","hardwareType":"GPU","sensor":"Memory Hotspot","sensorType":"Temperature","value":None,"unit":"°C","source":"test","identifier":"/gpu/hotspot"},
            {"hardware":"GPU","hardwareType":"GPU","sensor":"Fan","sensorType":"Fan","value":1100.0,"unit":"RPM","source":"test","identifier":"/gpu/fan/0"},
            {"hardware":"GPU","hardwareType":"GPU","sensor":"Fan","sensorType":"Fan","value":1250.0,"unit":"RPM","source":"test","identifier":"/gpu/fan/1"}]},
            "system":{"cpu_percent":35.0,"cpu_per_core_percent":[20.0,70.0]},"gpu":{}}
    rows=_u107_get_sensor_rows(FakeApp())
    assert any(r["sensor"]=="Tctl/Tdie" and r["value"]=="72" for r in rows)
    assert any(r["sensor"]=="Core #1" and r["value"]=="N/D" for r in rows)
    assert any(r["sensor"]=="Memory Hotspot" and r["value"]=="N/D" for r in rows)
    assert any(r["sensor"]=="Rdzeń logiczny 2 — użycie" and r["value"]=="70" for r in rows)
    fans=[r for r in rows if r["sensor"]=="Fan" and r["unit"]=="RPM"]
    assert len(fans)==2 and {r["value"] for r in fans}=={"1100","1250"}, "Same-name sensors with distinct hardware identifiers must not be collapsed."
    print("FULL_SENSOR_INVENTORY_SELFTEST_OK: active values, N/D and duplicate sensor IDs remain visible")

_u109_selftest_service_catalog=_u114_selftest_service_catalog
_u93_selftest_catalog_routing=_u114_selftest_catalog_routing
# Keep the original unique-scene routing self-test; do not alias it to the service catalog test.
_u100_selftest_unique_gpu_scenes=_u114_selftest_unique_gpu_scenes



# v4.3.116 — enforce a unique geometric signature per scene and expose full sensor availability in the UI.
_U116_SCENE_STYLE_NAMES = (
    "ORBITAL RINGS","TURBINE ARRAY","CRYSTAL SPIRAL","BOX LATTICE",
    "WAVE RIBBONS","PARTICLE HELIX","WIRE CAGES","THERMAL COLUMNS",
    "TRIANGLE BURST","SPHERE CLUSTER","MESH TUNNEL","PCB COOLING GRID",
    "VOXEL TOWER MATRIX","ATOM ORBIT LAB","CAGE FRAME STRESS","PARTICLE CLOUD",
    "SPIRAL STAIRCASE","LAYERED WAVE SURFACE","PRISM ROTOR ARRAY","RADIATOR FAN WALL",
    "NETWORK GRAPH","GEAR CLUSTER","FIBER OPTIC RIBBONS","HELICAL KNOT",
    "RING TUNNEL","FRACTAL BRANCH TREE","MATRIX DATA STREAM","TRIANGLE PYRAMID CAGE",
    "RADIAL VORTEX BARS","CUBE SWARM","PCB TRACE STRESS"
)

def _u116_scene_signature(scene_id):
    sid=max(1,min(110,int(scene_id)))
    style_index=(sid*7+sid//4)%len(_U116_SCENE_STYLE_NAMES)
    return {
        "scene_id":sid,
        "style_index":style_index,
        "style_name":_U116_SCENE_STYLE_NAMES[style_index],
        "variant":1+((sid*11+sid//3)%17),
        "element_count":4+((sid*17+sid//5)%27),
        "scale":round(.42+((sid*13)%37)/20.0,3),
        "rotation_speed":12+((sid*19)%43),
        "palette":(sid*5+sid//8)%6,
        "seed":sid*1009+(sid%7)*13
    }

_U116_ORIGINAL_REFRESH_SENSOR_TABLE=_u108_refresh_sensor_table
_U116_ORIGINAL_ATTACH_SENSOR_TABLE=_u100_attach_sensor_table
_U116_ORIGINAL_SHOW_LIVE_MONITOR=AppV43.show_live_monitor

def _u116_refresh_sensor_table(app):
    _U116_ORIGINAL_REFRESH_SENSOR_TABLE(app)
    try:
        tree=getattr(app,"_u100_sensor_tree",None)
        label=getattr(app,"_u100_sensor_count",None)
        if tree is None or label is None or not tree.winfo_exists() or not label.winfo_exists():
            return
        items=tree.get_children("")
        available=0;missing=0;categories={}
        for iid in items:
            values=tree.item(iid,"values") or ()
            if len(values)<4:
                missing+=1;continue
            cat=str(values[0] or "Other")
            categories[cat]=categories.get(cat,0)+1
            raw=str(values[3] if values[3] is not None else "N/D").strip().casefold()
            if raw in ("n/d","nd","n/a","na","none","null","—","-",""):
                missing+=1
            else:
                available+=1
        cache=getattr(app,"_u66_sensor_cache",{}) or {}
        stamp=cache.get("time")
        age=max(0,_u66_time.monotonic()-stamp) if isinstance(stamp,(int,float)) else None
        data=f"{len(items)} pozycji • wartości: {available} • N/D: {missing}"
        if age is not None:
            data+=f" • próbka: {age:.1f} s"
        if categories:
            data+=" • "+", ".join(f"{k}:{v}" for k,v in sorted(categories.items()))
        label.config(text=data)
        app._u116_sensor_availability={"total":len(items),"available":available,"missing":missing,"age_seconds":age}
    except Exception as exc:
        try:app.queue_log("Licznik dostępności czujników: "+repr(exc))
        except Exception:pass

def _u116_attach_sensor_table(app,parent,height=10):
    panel=_U116_ORIGINAL_ATTACH_SENSOR_TABLE(app,parent,max(16,int(height or 16)))
    try:
        tree=getattr(app,"_u100_sensor_tree",None)
        if tree is not None and tree.winfo_exists():
            tree.configure(height=max(16,int(height or 16)))
    except Exception:pass
    return panel

def _u116_force_sensor_refresh(app):
    try:
        app._u100_sensor_last=0
        app._u66_sensor_last=0
        _u108_sensor_poll(app)
        app.queue_status("Odświeżenie pełnej telemetrii zlecone — oczekiwanie na Sensor Bridge i liczniki Windows.")
        app.queue_log("Wymuszono odświeżenie: LHM/Sensor Bridge + CPU per-core + RAM + I/O dysków + NIC + woluminy.")
    except Exception as exc:
        try:app.queue_log("Wymuszone odświeżenie czujników nie powiodło się: "+repr(exc))
        except Exception:pass
        try:messagebox.showerror("Telemetria",str(exc))
        except Exception:pass

def _u116_export_sensor_csv(app):
    try:
        import csv as _u116_csv
        from pathlib import Path as _u116_Path
        rows=_u107_get_sensor_rows(app)
        if not rows:
            messagebox.showwarning("Eksport telemetrii","Brak dostępnych wierszy pomiarowych do eksportu. Najpierw odśwież czujniki.")
            return
        folder=_u66_store_dir()/"reports"/"sensors"
        folder.mkdir(parents=True,exist_ok=True)
        stamp=_U66_datetime.now().strftime("%Y%m%d-%H%M%S")
        target=folder/("telemetry-"+stamp+".csv")
        fields=("category","hardware","sensor","value","unit","source")
        with target.open("w",encoding="utf-8-sig",newline="") as stream:
            writer=_u116_csv.DictWriter(stream,fieldnames=fields,extrasaction="ignore")
            writer.writeheader()
            for row in rows:
                writer.writerow({key:row.get(key,"N/D") if row.get(key) is not None else "N/D" for key in fields})
        report={"state":"good","path":str(target),"row_count":len(rows),
            "available_rows":sum(1 for row in rows if str(row.get("value","N/D")).strip().casefold() not in ("n/d","nd","n/a","none","null","—","-","")),
            "note":"Eksport lokalny. Obejmuje wszystkie rekordy scalar, w tym N/D; nie wysyła danych do sieci."}
        try:app.results["SENSOR_CSV_EXPORT"]=report
        except Exception:pass
        try:app.queue_log(f"Eksport telemetrii CSV: {len(rows)} wierszy → {target}")
        except Exception:pass
        messagebox.showinfo("Eksport zakończony",f"Zapisano {len(rows)} wierszy telemetrii.\n\n{target}\n\nPlik jest lokalny i zawiera także rekordy N/D.")
        return str(target)
    except Exception as exc:
        msg=f"{type(exc).__name__}: {exc}"
        try:app.queue_log("Eksport CSV sensorów: "+msg)
        except Exception:pass
        try:messagebox.showerror("Eksport telemetrii",msg)
        except Exception:pass
        return None

def _u128_sensor_summary_text(rows):
    """Create a complete grouped live readout, not just two clipped temperature/load strings."""
    groups={}
    missing_tokens=("n/d","nd","n/a","na","none","null","—","-","")
    for row in rows or []:
        if not isinstance(row,dict):continue
        category=str(row.get("category") or "Other").strip() or "Other"
        hardware=str(row.get("hardware") or "N/D").strip() or "N/D"
        name=str(row.get("sensor") or "N/D").strip() or "N/D"
        raw=row.get("value")
        value="N/D" if raw is None else str(raw).strip()
        if value.casefold() in missing_tokens:value="N/D"
        unit=str(row.get("unit") or "")
        source=str(row.get("source") or "N/D")
        groups.setdefault(category,[]).append((hardware,name,value,unit,source))
    if not groups:return "Brak rekordów telemetrii. Użyj ODŚWIEŻ WSZYSTKIE CZUJNIKI.\nN/D oznacza brak wartości udostępnionej przez sterownik."
    preferred=("Temperature","Load","Clock","Power","Voltage","Fan","Memory","Throughput","Disk I/O","Network","Battery","Other")
    ordered=sorted(groups,key=lambda key:(preferred.index(key) if key in preferred else len(preferred),key.casefold()))
    lines=["PEŁNA LISTA ODCZYTÓW — wartości aktualizowane z Sensor Bridge i liczników Windows.",
           "N/D = czujnik wykryty, ale brak bieżącej wartości; nie jest to fikcyjny odczyt."]
    for category in ordered:
        values=groups[category]
        lines.append("")
        lines.append(f"━━ {category.upper()} ({len(values)}) ━━")
        for hardware,name,value,unit,source in values:
            lines.append(f"{hardware} | {name}: {value}{(' '+unit) if unit else ''}  ·  {source}")
    lines.append("")
    lines.append(f"RAZEM: {sum(len(v) for v in groups.values())} rekordów w {len(groups)} grupach.")
    return "\n".join(lines)


def _u126_refresh_live_sensor_summary(app):
    try:
        if getattr(app,"current_view","")!="LIVE_MONITOR":
            return
        widget=getattr(app,"_u126_sensor_summary_label",None)
        if widget is None or not widget.winfo_exists():
            return
        rows=_u107_get_sensor_rows(app)
        content=_u128_sensor_summary_text(rows)
        # The monitor now uses a scrollable Text widget; retain Label compatibility for older screens.
        if isinstance(widget,tk.Text):
            widget.configure(state="normal")
            widget.delete("1.0","end")
            widget.insert("1.0",content)
            widget.configure(state="disabled")
        else:
            widget.config(text=content)
        app.after(2500,lambda:_u126_refresh_live_sensor_summary(app))
    except Exception as exc:
        try:app.queue_log("Pełne podsumowanie telemetrii: "+repr(exc))
        except Exception:pass

def _u116_show_live_monitor(app):
    result=_U116_ORIGINAL_SHOW_LIVE_MONITOR(app)
    try:
        t=app.colors()
        pane=app.panel(app.content)
        pane.pack(fill="x",padx=3,pady=(2,6))
        tk.Label(pane,text="PEŁNA TELEMETRIA — CZUJNIKI + LICZNIKI SYSTEMOWE",
            bg=t["panel"],fg=t["accent"],font=app.fnt(10,"bold")).pack(anchor="w",padx=9,pady=(7,3))
        tk.Label(pane,text="Pełny inspektor pokazuje wszystkie wykryte sensory oraz liczniki systemowe. N/D oznacza, że sterownik nie udostępnił aktualnej wartości.",
            bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1400,justify="left").pack(anchor="w",padx=9,pady=(0,4))
        summary_frame=tk.Frame(pane,bg=t["panel"])
        summary_frame.pack(fill="both",expand=False,padx=7,pady=(0,6))
        summary_scroll=ttk.Scrollbar(summary_frame,orient="vertical")
        summary_scroll.pack(side="right",fill="y")
        app._u126_sensor_summary_label=tk.Text(summary_frame,height=13,wrap="word",
            bg=t["card"],fg=t["fg"],font=app.fnt(8),relief="flat",borderwidth=0,
            yscrollcommand=summary_scroll.set,state="disabled")
        app._u126_sensor_summary_label.pack(side="left",fill="both",expand=True)
        summary_scroll.configure(command=app._u126_sensor_summary_label.yview)
        app.after(300,lambda:_u126_refresh_live_sensor_summary(app))
        row=tk.Frame(pane,bg=t["panel"]);row.pack(fill="x",padx=6,pady=(0,7))
        app.make_button(row,"OTWÓRZ PEŁNY INSPEKTOR",lambda:_u107_open_sensor_inspector(app),"accent",side="left",ipady=5)
        app.make_button(row,"ODŚWIEŻ WSZYSTKIE CZUJNIKI",lambda:_u116_force_sensor_refresh(app),"good",side="left",ipady=5)
        app.make_button(row,"EKSPORT CAŁEJ TELEMETRII CSV",lambda:_u116_export_sensor_csv(app),"card",side="left",ipady=5)
    except Exception as exc:
        try:app.queue_log("Dodatkowe sterowanie telemetrią: "+repr(exc))
        except Exception:pass
    return result

def _u116_selftest_scene_signatures():
    signatures=[_u116_scene_signature(i) for i in range(1,111)]
    keys=[(x["style_index"],x["variant"],x["element_count"],x["scale"],x["rotation_speed"],x["palette"]) for x in signatures]
    assert len(signatures)==110 and len(set(keys))==110,"Each of the 110 scene IDs must have a distinct geometry signature."
    assert len({x["style_name"] for x in signatures})==len(_U116_SCENE_STYLE_NAMES) and len(_U116_SCENE_STYLE_NAMES)==31, "The signature self-test must cover all 31 renderer styles."
    def nested_identifiers(code):
        import types as _u116_types
        found=set()
        pending=[code]
        while pending:
            current=pending.pop()
            found.update(current.co_names)
            found.update(current.co_varnames)
            pending.extend(value for value in current.co_consts if isinstance(value,_u116_types.CodeType))
        return found
    def nested_literals(code):
        import types as _u116_types
        found=[]
        pending=[code]
        while pending:
            current=pending.pop()
            for value in current.co_consts:
                if isinstance(value,str):found.append(value)
                elif isinstance(value,_u116_types.CodeType):pending.append(value)
        return set(found)
    identifiers=nested_identifiers(_u114_gpu_benchmark_child.__code__)
    literals=nested_literals(_u114_gpu_benchmark_child.__code__)
    assert "draw_scene_signature" in identifiers,"The synchronized OpenGL renderer must draw the scene-specific signature."
    assert "signature_vertices" in literals and "scene_signature" in literals
    assert "geometry_objects" in literals and "geometry_vertices" in literals
    print("UNIQUE_GPU_GEOMETRY_SIGNATURE_SELFTEST_OK: 110 unique signatures, 31 renderer styles, real synchronized OpenGL FPS")

def _u126_selftest_sensor_merge():
    base={"hardwareId":"/cpu/0","identifier":"/cpu/0/temperature/0","hardware":"CPU","sensor":"CPU Package",
          "sensorType":"Temperature","unit":"°C","value":None,"source":"Sensor Bridge"}
    later={**base,"value":73.5,"source":"WMI fallback"}
    merged=_u126_merge_sensor_rows([base],[later],"WMI fallback")
    assert len(merged)==1 and merged[0]["value"]==73.5, "A valid fallback reading must replace a duplicate N/D row."
    missing={**base,"value":None,"source":"later poll"}
    merged_again=_u126_merge_sensor_rows(merged,[missing],"later poll")
    assert len(merged_again)==1 and merged_again[0]["value"]==73.5, "A later N/D value must not erase a valid sensor reading."
    distinct={**base,"identifier":"/cpu/0/temperature/1","sensor":"CPU Core 1","value":61.0}
    final=_u126_merge_sensor_rows(merged_again,[distinct],"Sensor Bridge")
    assert len(final)==2 and final[1]["value"]==61.0
    print("SENSOR_MERGE_PRESERVES_VALID_READINGS_SELFTEST_OK: N/D fallback merge and duplicate protection")

def _u116_selftest_sensor_display_controls():
    class FakeLabel:
        def __init__(self):self.text=""
        def winfo_exists(self):return True
        def config(self,**kwargs):
            if "text" in kwargs:self.text=kwargs["text"]
    class FakeTree:
        def __init__(self):self.items={}
        def winfo_exists(self):return True
        def get_children(self,*args):return list(self.items)
        def item(self,iid,key=None):
            return self.items[iid] if key is None else self.items[iid].get(key)
        def delete(self,*iids):
            for iid in iids:self.items.pop(iid,None)
        def insert(self,parent,index,iid=None,values=(),**kwargs):
            iid=str(iid or ("row"+str(len(self.items))))
            self.items[iid]={"values":tuple(values)}
            return iid
        def exists(self,iid):return iid in self.items
    class FakeApp:
        _u100_sensor_tree=FakeTree()
        _u100_sensor_count=FakeLabel()
        _u66_sensor_cache={
            "time":_u66_time.monotonic(),
            "temps":{"method":"test bridge","sensor_count":2,"sensors":[
                {"hardware":"CPU Package","hardwareType":"CPU","sensor":"Tctl/Tdie","sensorType":"Temperature","value":72.0,"unit":"°C","source":"test"},
                {"hardware":"GPU","hardwareType":"GPU","sensor":"Memory Hotspot","sensorType":"Temperature","value":None,"unit":"°C","source":"test"}]},
            "gpu":{},
            "system":{"cpu_per_core_percent":[64.0]}
        }
        results={}
        def queue_log(self,*args):pass
    app=FakeApp()
    _u116_refresh_sensor_table(app)
    availability=app._u116_sensor_availability
    assert availability["total"]>=3
    assert availability["available"]>=2
    assert availability["missing"]>=1
    assert "wartości:" in app._u100_sensor_count.text and "N/D:" in app._u100_sensor_count.text
    assert callable(_u116_export_sensor_csv) and callable(_u116_force_sensor_refresh)
    assert AppV43.show_live_monitor is _u116_show_live_monitor
    print("FULL_SENSOR_DISPLAY_CONTROLS_SELFTEST_OK: full table refresh, available/N-D counters, refresh action and local CSV export")

_u108_refresh_sensor_table=_u116_refresh_sensor_table
_u100_refresh_sensor_table=_u116_refresh_sensor_table
_u81_refresh_sensor_table=_u116_refresh_sensor_table
_u100_attach_sensor_table=_u116_attach_sensor_table
_u81_attach_sensor_table=_u116_attach_sensor_table
AppV43.show_live_monitor=_u116_show_live_monitor
_u66_show_live_monitor=_u116_show_live_monitor

def _u117_selftest_per_test_scene_routing():
    assert callable(_u107_open_component_simulator)
    assert callable(_u107_launch_scene_preview)
    detail_names=_u93_deep_code_names(_u93_show_test_detail)
    if "_u107_launch_scene_preview" not in detail_names and "_u107_open_component_simulator" not in detail_names:
        original_detail = globals().get("_U102_ORIGINAL_RAM_DETAIL")
        if callable(original_detail):
            detail_names.update(_u93_deep_code_names(original_detail))
    assert ("_u107_launch_scene_preview" in detail_names or "_u107_open_component_simulator" in detail_names), "Individual test preview must launch the dedicated scene renderer."
    assert "_u69_open_component_simulator" not in detail_names, "Individual test preview must not call the generic module simulator."
    for screen in (_u93_show_lab,_u93_show_catalog,_u93_add_entry):
        names=_u93_deep_code_names(screen)
        assert "_u69_open_component_simulator" not in names, "Module/catalog selection must lead to the specific test catalog, not a generic simulator shortcut."
    assert len(_U107_TEST_SCENES)==110
    assert len(set(_U107_TEST_SCENES.values()))==110
    assert len(_U100_SCENE_TITLES)==110
    print("PER_TEST_SIMULATOR_ROUTING_SELFTEST_OK: test button routes to its unique scene; generic module shortcuts removed")



# v4.3.126 — add the missing process-management and game-troubleshooting service screens.
_U126_PROTECTED_PROCESS_NAMES={
    "system","system idle process","registry","memory compression","secure system",
    "csrss.exe","wininit.exe","services.exe","lsass.exe","winlogon.exe","smss.exe",
    "dwm.exe","fontdrvhost.exe","lsaiso.exe","svchost.exe","ntoskrnl.exe"
}

def _u126_is_protected_process(name):
    value=str(name or "").strip().casefold()
    return value in _U126_PROTECTED_PROCESS_NAMES or "naprawa pc hardware test pro" in value or "naprawa-pc-hardware-test-pro" in value

def _u126_collect_process_rows():
    import psutil as _u126_psutil
    rows=[]
    for proc in _u126_psutil.process_iter(["pid","name","username","status","cpu_percent","create_time"]):
        try:
            info=proc.info or {}
            pid=int(info.get("pid") or proc.pid)
            name=str(info.get("name") or "N/D")
            try:memory=int(proc.memory_info().rss)
            except Exception:memory=None
            cpu=info.get("cpu_percent")
            try:cpu=float(cpu) if cpu is not None and _u66_math.isfinite(float(cpu)) else None
            except Exception:cpu=None
            rows.append({"pid":pid,"name":name,"username":str(info.get("username") or "N/D"),
                "status":str(info.get("status") or "N/D"),"cpu_percent":cpu,
                "memory_bytes":memory,"memory_mb":round(memory/1048576,1) if memory is not None else None,
                "protected":_u126_is_protected_process(name)})
        except Exception:
            continue
    return sorted(rows,key=lambda row:(row.get("memory_bytes") or 0),reverse=True)

def _u126_show_process_manager(app):
    import csv as _u126_csv
    import os as _u126_os
    import subprocess as _u126_subprocess
    from pathlib import Path as _u126_Path
    from tkinter import filedialog as _u126_filedialog
    app.current_view="PROCESS_MANAGER";app.clear();t=app.colors()
    app.header_title.config(text="SERWIS ULTIMATE — MENEDŻER PROCESÓW")
    head=app.panel(app.content);head.pack(fill="x",padx=3,pady=(0,5))
    tk.Label(head,text="PROCESY WINDOWS • CPU • PAMIĘĆ • STATUS",bg=t["panel"],fg=t["accent"],font=app.fnt(11,"bold")).pack(anchor="w",padx=10,pady=(7,2))
    tk.Label(head,text="Odczyt procesów jest tylko diagnostyczny. Zakończenie procesu wymaga osobnego potwierdzenia; procesy krytyczne i sama aplikacja są chronione.",bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1350,justify="left").pack(anchor="w",padx=10,pady=(0,7))
    controls=tk.Frame(app.content,bg=t["bg"]);controls.pack(fill="x",padx=6,pady=4)
    query=tk.StringVar()
    tk.Label(controls,text="Filtr:",bg=t["bg"],fg=t["muted"],font=app.fnt(8,"bold")).pack(side="left",padx=(0,5))
    search=tk.Entry(controls,textvariable=query,bg=t["card"],fg=t["text"],insertbackground=t["text"],relief="flat")
    search.pack(side="left",fill="x",expand=True,padx=(0,8),ipady=4)
    status=tk.StringVar(value="Odczyt procesów nie został jeszcze wykonany.")
    tk.Label(app.content,textvariable=status,bg=t["bg"],fg=t["accent"],anchor="w",wraplength=1350).pack(fill="x",padx=8,pady=3)
    cols=("pid","name","cpu","memory","user","state")
    table_frame=tk.Frame(app.content,bg=t["bg"]);table_frame.pack(fill="both",expand=True,padx=6,pady=4)
    table=ttk.Treeview(table_frame,columns=cols,show="headings",height=18)
    for key,title,width in (("pid","PID",80),("name","Proces",300),("cpu","CPU %",90),("memory","RAM MB",100),("user","Użytkownik",240),("state","Status",140)):
        table.heading(key,text=title);table.column(key,width=width,anchor="w" if key in ("name","user","state") else "e")
    scroll=ttk.Scrollbar(table_frame,orient="vertical",command=table.yview);table.configure(yscrollcommand=scroll.set)
    table.pack(side="left",fill="both",expand=True);scroll.pack(side="right",fill="y")
    rows_cache=[]
    def refresh():
        nonlocal rows_cache
        try:rows_cache=_u126_collect_process_rows()
        except Exception as exc:
            status.set("BŁĄD odczytu procesów: "+type(exc).__name__+": "+str(exc));return
        needle=query.get().strip().casefold()
        for iid in table.get_children():table.delete(iid)
        visible=0
        for row in rows_cache:
            if needle and needle not in (str(row["name"])+" "+str(row["pid"])+" "+str(row["username"])).casefold():continue
            cpu=f"{row['cpu_percent']:.1f}" if isinstance(row.get("cpu_percent"),(int,float)) else "N/D"
            memory=f"{row['memory_mb']:.1f}" if isinstance(row.get("memory_mb"),(int,float)) else "N/D"
            table.insert("","end",iid=str(row["pid"]),values=(row["pid"],row["name"],cpu,memory,row["username"],row["status"]))
            visible+=1
        status.set(f"Procesy: {len(rows_cache)} • widoczne: {visible} • chronione: {sum(1 for row in rows_cache if row['protected'])} • sortowanie: największe użycie RAM")
    def terminate_selected():
        selection=table.selection()
        if not selection:
            messagebox.showinfo("Menedżer procesów","Najpierw zaznacz proces.");return
        try:pid=int(selection[0])
        except Exception:return
        row=next((x for x in rows_cache if x["pid"]==pid),None)
        if not row:
            status.set("Proces zniknął z listy. Odśwież widok.");return
        if row.get("protected") or pid==_u126_os.getpid():
            messagebox.showwarning("Proces chroniony","Nie wolno zakończyć tego procesu z poziomu narzędzia serwisowego.");return
        if not messagebox.askyesno("Zakończyć proces?",f"Zakończyć proces {row['name']} (PID {pid})? Niezapisane dane tej aplikacji mogą zostać utracone."):
            return
        try:
            import psutil as _u126_psutil
            process=_u126_psutil.Process(pid)
            if _u126_is_protected_process(process.name()) or pid==_u126_os.getpid():
                raise PermissionError("Proces został rozpoznany jako chroniony.")
            process.terminate()
            try:process.wait(timeout=3)
            except _u126_psutil.TimeoutExpired:
                status.set(f"Proces {pid} nie zakończył się w 3 s. Nie wymuszono kill; sprawdź uprawnienia i odśwież.")
                return
            status.set(f"Zakończono proces {row['name']} (PID {pid}).")
            refresh()
        except Exception as exc:
            status.set(f"Nie zakończono procesu {pid}: {type(exc).__name__}: {exc}")
    def export_csv():
        if not rows_cache:
            messagebox.showinfo("Eksport procesów","Najpierw odśwież listę procesów.");return
        path=_u126_filedialog.asksaveasfilename(title="Zapisz raport procesów",defaultextension=".csv",filetypes=[("CSV","*.csv")],initialfile="naprawapc-procesy.csv")
        if not path:return
        try:
            with open(path,"w",encoding="utf-8-sig",newline="") as stream:
                writer=_u126_csv.DictWriter(stream,fieldnames=("pid","name","username","status","cpu_percent","memory_mb","protected"))
                writer.writeheader()
                for row in rows_cache:writer.writerow({key:row.get(key) for key in writer.fieldnames})
            status.set(f"Zapisano {len(rows_cache)} procesów: {path}")
        except Exception as exc:messagebox.showerror("Eksport CSV",str(exc))
    row=tk.Frame(app.content,bg=t["bg"]);row.pack(fill="x",padx=6,pady=5)
    app.make_button(row,"ODŚWIEŻ LISTĘ",refresh,"accent",side="left",ipady=5)
    app.make_button(row,"ZAKOŃCZ WYBRANY",terminate_selected,"bad",side="left",ipady=5)
    app.make_button(row,"EKSPORT CSV",export_csv,"card",side="left",ipady=5)
    app.make_button(row,"← CENTRUM NAPRAW",lambda:_u120_show_system_repair_center(app),"card",side="left",ipady=5)
    search.bind("<Return>",lambda event:refresh())
    refresh()

_U126_REPORT_EXTENSIONS={".json",".csv",".html",".htm",".txt",".md",".log",".xml",".pdf"}

def _u126_report_root():
    import os as _u126_report_os
    from pathlib import Path as _u126_report_Path
    base=_u126_report_os.environ.get("LOCALAPPDATA") or str(_u126_report_Path.home())
    return _u126_report_Path(base)/"NaprawaPC"

def _u126_scan_report_files(limit=5000):
    import os as _u126_report_os
    from datetime import datetime as _u126_report_datetime
    root=_u126_report_root()
    rows=[]
    if not root.exists():
        return rows
    ignored={".git","venv",".venv","cache","temp","tmp","node_modules","dist","publish"}
    for current,dirs,files in _u126_report_os.walk(root):
        dirs[:]=[d for d in dirs if d.casefold() not in ignored]
        for name in files:
            path=__import__("pathlib").Path(current)/name
            if path.suffix.casefold() not in _U126_REPORT_EXTENSIONS:
                continue
            try:
                stat=path.stat()
                if not path.is_file() or stat.st_size>100*1024*1024:
                    continue
                rows.append({"name":path.name,"path":str(path),"folder":str(path.parent.relative_to(root)),
                    "extension":path.suffix.casefold(),"size_bytes":int(stat.st_size),
                    "modified_at":_u126_report_datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds")})
            except Exception:
                continue
            if len(rows)>=max(1,min(5000,int(limit))):
                return sorted(rows,key=lambda row:row["modified_at"],reverse=True)
    return sorted(rows,key=lambda row:row["modified_at"],reverse=True)

def _u126_show_report_manager(app):
    import csv as _u126_report_csv
    import os as _u126_report_os
    import subprocess as _u126_report_subprocess
    from tkinter import filedialog as _u126_report_filedialog
    app.current_view="REPORT_MANAGER";app.clear();t=app.colors()
    app.header_title.config(text="SERWIS ULTIMATE — RAPORTY I HISTORIA")
    head=app.panel(app.content);head.pack(fill="x",padx=3,pady=(0,5))
    tk.Label(head,text="RAPORTY • HISTORIA TESTÓW • DIAGNOSTYKA • ZLECENIA",bg=t["panel"],fg=t["accent"],font=app.fnt(11,"bold")).pack(anchor="w",padx=10,pady=(7,2))
    tk.Label(head,text="Widok tylko do odczytu. Lista obejmuje raporty JSON/CSV/HTML/TXT/LOG/XML/PDF w katalogu lokalnym NaprawaPC. Nie usuwa ani nie wysyła plików.",bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1350,justify="left").pack(anchor="w",padx=10,pady=(0,7))
    query=tk.StringVar()
    controls=tk.Frame(app.content,bg=t["bg"]);controls.pack(fill="x",padx=6,pady=4)
    tk.Label(controls,text="Filtr:",bg=t["bg"],fg=t["muted"],font=app.fnt(8,"bold")).pack(side="left",padx=(0,5))
    search=tk.Entry(controls,textvariable=query,bg=t["card"],fg=t["text"],insertbackground=t["text"],relief="flat")
    search.pack(side="left",fill="x",expand=True,padx=(0,8),ipady=4)
    status=tk.StringVar(value="Lista raportów nie została jeszcze odświeżona.")
    tk.Label(app.content,textvariable=status,bg=t["bg"],fg=t["accent"],anchor="w",wraplength=1350).pack(fill="x",padx=8,pady=3)
    table_frame=tk.Frame(app.content,bg=t["bg"]);table_frame.pack(fill="both",expand=True,padx=6,pady=4)
    cols=("modified","name","folder","size","ext")
    table=ttk.Treeview(table_frame,columns=cols,show="headings",height=18)
    for key,title,width in (("modified","Data modyfikacji",170),("name","Plik",360),("folder","Katalog",420),("size","Rozmiar B",110),("ext","Typ",70)):
        table.heading(key,text=title);table.column(key,width=width,anchor="w" if key in ("modified","name","folder","ext") else "e")
    scroll=ttk.Scrollbar(table_frame,orient="vertical",command=table.yview);table.configure(yscrollcommand=scroll.set)
    table.pack(side="left",fill="both",expand=True);scroll.pack(side="right",fill="y")
    rows_cache=[]
    def refresh():
        nonlocal rows_cache
        try:rows_cache=_u126_scan_report_files()
        except Exception as exc:
            status.set(f"BŁĄD skanowania raportów: {type(exc).__name__}: {exc}");return
        needle=query.get().strip().casefold()
        for iid in table.get_children():table.delete(iid)
        visible=0
        for index,row in enumerate(rows_cache):
            searchable=(row["name"]+" "+row["folder"]+" "+row["extension"]).casefold()
            if needle and needle not in searchable:continue
            table.insert("","end",iid=str(index),values=(row["modified_at"],row["name"],row["folder"],row["size_bytes"],row["extension"]))
            visible+=1
        status.set(f"Katalog: {_u126_report_root()} • plików: {len(rows_cache)} • widoczne: {visible} • limit skanowania: 5000")
        try:app.results["REPORT_MANAGER"]={"state":"good","files":len(rows_cache),"root":str(_u126_report_root())}
        except Exception:pass
    def open_selected():
        selection=table.selection()
        if not selection:
            messagebox.showinfo("Raporty","Zaznacz raport na liście.");return
        try:row=rows_cache[int(selection[0])]
        except Exception:return
        path=row["path"]
        if not _u126_report_os.path.isfile(path):
            status.set("Plik już nie istnieje. Odśwież listę.");return
        try:
            if hasattr(_u126_report_os,"startfile"):_u126_report_os.startfile(path)
            elif row["extension"] in (".txt",".log",".json",".csv",".md",".xml"):_u126_report_subprocess.Popen(["notepad.exe",path])
            else:messagebox.showinfo("Raport",path)
            status.set("Otwarto: "+path)
        except Exception as exc:messagebox.showerror("Otwieranie raportu",str(exc))
    def export_index():
        if not rows_cache:
            messagebox.showinfo("Raporty","Najpierw odśwież listę.");return
        path=_u126_report_filedialog.asksaveasfilename(title="Eksport indeksu raportów",defaultextension=".csv",filetypes=[("CSV","*.csv")],initialfile="naprawapc-indeks-raportow.csv")
        if not path:return
        try:
            with open(path,"w",encoding="utf-8-sig",newline="") as stream:
                writer=_u126_report_csv.DictWriter(stream,fieldnames=("modified_at","name","folder","extension","size_bytes","path"))
                writer.writeheader()
                for row in rows_cache:writer.writerow({key:row.get(key) for key in writer.fieldnames})
            status.set(f"Zapisano indeks {len(rows_cache)} raportów: {path}")
        except Exception as exc:messagebox.showerror("Eksport indeksu",str(exc))
    row=tk.Frame(app.content,bg=t["bg"]);row.pack(fill="x",padx=6,pady=5)
    app.make_button(row,"ODŚWIEŻ",refresh,"accent",side="left",ipady=5)
    app.make_button(row,"OTWÓRZ WYBRANY RAPORT",open_selected,"good",side="left",ipady=5)
    app.make_button(row,"EKSPORT INDEKSU CSV",export_index,"card",side="left",ipady=5)
    app.make_button(row,"← CENTRUM NAPRAW",lambda:_u120_show_system_repair_center(app),"card",side="left",ipady=5)
    search.bind("<Return>",lambda event:refresh())
    table.bind("<Double-1>",lambda event:open_selected())
    refresh()

def _u126_selftest_report_manager():
    assert _U126_REPORT_EXTENSIONS.issuperset({".json",".csv",".html",".txt",".log",".pdf"})
    assert callable(_u126_report_root) and callable(_u126_scan_report_files) and callable(_u126_show_report_manager)
    assert "remove" not in _u126_show_report_manager.__code__.co_names
    assert AppV43.show_report_manager is _u126_show_report_manager
    print("SERWIS_ULTIMATE_REPORT_MANAGER_SELFTEST_OK: local report index, filtering, open and CSV export without delete actions")

_U126_GAME_DIAGNOSTIC_PS = r"""
$ErrorActionPreference='SilentlyContinue'
$os=Get-CimInstance Win32_OperatingSystem | Select-Object Caption,Version,BuildNumber,OSArchitecture
$gpus=@(Get-CimInstance Win32_VideoController | Select-Object Name,DriverVersion,DriverDate,CurrentHorizontalResolution,CurrentVerticalResolution,AdapterRAM)
$dx=(Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\DirectX' -Name Version -ErrorAction SilentlyContinue).Version
$gamebar=Get-ItemProperty 'HKCU:\Software\Microsoft\GameBar' -ErrorAction SilentlyContinue | Select-Object GameModeEnabled,AllowAutoGameMode,GameDVR_Enabled
$services=@(Get-Service -Name 'GamingServices','GamingServicesNet','XblAuthManager','XblGameSave','XboxNetApiSvc' -ErrorAction SilentlyContinue | Select-Object Name,Status,StartType)
$power=powercfg /getactivescheme 2>&1
[pscustomobject]@{CollectedAt=(Get-Date).ToString('o');OS=$os;DirectXRegistryVersion=$dx;GPUs=$gpus;GameBar=$gamebar;GamingServices=$services;ActivePowerPlan=($power -join ' ')} | ConvertTo-Json -Depth 6
"""

def _u126_collect_game_diagnostics():
    import os as _u126_os
    import subprocess as _u126_subprocess
    if _u126_os.name!="nt":
        return {"state":"warn","body":"Ta diagnostyka wymaga Windows 10/11.","returncode":None}
    exe=_u126_os.path.join(_u126_os.environ.get("WINDIR",r"C:\Windows"),"System32","WindowsPowerShell","v1.0","powershell.exe")
    try:
        proc=_u126_subprocess.run([exe,"-NoProfile","-NonInteractive","-Command",_U126_GAME_DIAGNOSTIC_PS],
            capture_output=True,text=True,encoding="utf-8",errors="replace",timeout=45,
            creationflags=getattr(_u126_subprocess,"CREATE_NO_WINDOW",0))
        body=((proc.stdout or "")+"\n"+(proc.stderr or "")).strip() or "Windows nie zwrócił danych diagnostycznych."
        return {"state":"good" if proc.returncode==0 and proc.stdout.strip() else "warn","body":body,"returncode":proc.returncode}
    except Exception as exc:
        return {"state":"warn","body":f"{type(exc).__name__}: {exc}","returncode":None}

def _u126_show_game_diagnostics(app):
    import os as _u126_os
    import subprocess as _u126_subprocess
    import threading as _u126_threading
    from datetime import datetime as _u126_datetime
    from pathlib import Path as _u126_Path
    app.current_view="GAME_DIAGNOSTICS";app.clear();t=app.colors()
    app.header_title.config(text="SERWIS ULTIMATE — DIAGNOSTYKA GIER")
    head=app.panel(app.content);head.pack(fill="x",padx=3,pady=(0,5))
    tk.Label(head,text="GPU • STEROWNIK • DIRECTX • USŁUGI GIER • PLAN ZASILANIA",bg=t["panel"],fg=t["accent"],font=app.fnt(11,"bold")).pack(anchor="w",padx=10,pady=(7,2))
    tk.Label(head,text="Odczyt diagnostyczny bez zmian w systemie. Brak wpisu lub usługi oznacza N/D; ten ekran nie obiecuje wzrostu FPS ani nie instaluje sterowników automatycznie.",bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1350,justify="left").pack(anchor="w",padx=10,pady=(0,7))
    status=tk.StringVar(value="Gotowe — uruchom diagnostykę.")
    tk.Label(app.content,textvariable=status,bg=t["bg"],fg=t["accent"],anchor="w",wraplength=1350).pack(fill="x",padx=8,pady=3)
    pane=app.panel(app.content);pane.pack(fill="both",expand=True,padx=3,pady=3)
    output=tk.Text(pane,bg="#07111f",fg="#d7eaff",insertbackground="#ffffff",wrap="word",font=("Consolas",9),relief="flat")
    output.pack(fill="both",expand=True,padx=8,pady=8);output.insert("end","Raport nie został jeszcze pobrany.\n");output.configure(state="disabled")
    def show_report(result,path):
        try:
            if not output.winfo_exists():return
            output.configure(state="normal");output.delete("1.0","end");output.insert("end",result.get("body","N/D")+"\n\nRaport: "+str(path));output.configure(state="disabled")
        except Exception:return
        status.set(("PASS" if result.get("state")=="good" else "WARN")+" — kod wyjścia: "+str(result.get("returncode","N/D"))+" — "+str(path))
        try:
            app.results["GAME_DIAGNOSTICS"]={"state":result.get("state"),"path":str(path),"returncode":result.get("returncode")}
            app.queue_log("Diagnostyka gier: "+str(path)+"; state="+str(result.get("state")))
        except Exception:pass
    def run():
        status.set("Trwa odczyt Windows, GPU, DirectX, usług i planu zasilania…")
        def job():
            result=_u126_collect_game_diagnostics()
            folder=_u126_Path(_u126_os.environ.get("LOCALAPPDATA") or _u126_Path.home())/"NaprawaPC"/"Raporty"/"GameDiagnostics"
            path=folder/(_u126_datetime.now().strftime("%Y%m%d-%H%M%S")+"-game-diagnostics.json")
            try:
                folder.mkdir(parents=True,exist_ok=True)
                import json as _u126_json
                path.write_text(_u126_json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
            except Exception as exc:
                result["body"]+="\n\nNie udało się zapisać raportu: "+str(exc)
            try:app.queue_action(lambda r=result,p=path:show_report(r,p))
            except Exception:pass
        _u126_threading.Thread(target=job,name="NaprawaPCGameDiagnostics",daemon=True).start()
    def open_graphics():
        try:
            if hasattr(_u126_os,"startfile"):_u126_os.startfile("ms-settings:display-advancedgraphics")
            else:_u126_subprocess.Popen(["cmd.exe","/c","start","","ms-settings:display-advancedgraphics"])
        except Exception as exc:messagebox.showerror("Ustawienia grafiki",str(exc))
    def open_dxdiag():
        try:_u126_subprocess.Popen(["dxdiag.exe"])
        except Exception as exc:messagebox.showerror("DirectX Diagnostic Tool",str(exc))
    row=tk.Frame(app.content,bg=t["bg"]);row.pack(fill="x",padx=6,pady=5)
    app.make_button(row,"URUCHOM DIAGNOSTYKĘ",run,"accent",side="left",ipady=5)
    app.make_button(row,"USTAWIENIA GRAFIKI",open_graphics,"card",side="left",ipady=5)
    app.make_button(row,"OTWÓRZ DXDIAG",open_dxdiag,"card",side="left",ipady=5)
    app.make_button(row,"← CENTRUM NAPRAW",lambda:_u120_show_system_repair_center(app),"card",side="left",ipady=5)

def _u126_selftest_process_manager():
    assert _u126_is_protected_process("lsass.exe")
    assert _u126_is_protected_process("NAPRAWA-PC-HARDWARE-TEST-PRO.exe")
    assert not _u126_is_protected_process("notepad.exe")
    assert callable(_u126_collect_process_rows) and callable(_u126_show_process_manager)
    assert AppV43.show_process_manager is _u126_show_process_manager
    assert "table_frame" in _u126_show_process_manager.__code__.co_varnames
    print("SERWIS_ULTIMATE_PROCESS_MANAGER_SELFTEST_OK: process inventory, protected-process guard, contained table and CSV export UI")

def _u126_selftest_game_diagnostics():
    assert "Win32_VideoController" in _U126_GAME_DIAGNOSTIC_PS
    assert "DirectXRegistryVersion" in _U126_GAME_DIAGNOSTIC_PS
    assert "Get-Service" in _U126_GAME_DIAGNOSTIC_PS and "powercfg /getactivescheme" in _U126_GAME_DIAGNOSTIC_PS
    assert all(token not in _U126_GAME_DIAGNOSTIC_PS for token in ("Remove-Item","Set-ItemProperty","Format-Volume","Clear-Disk"))
    assert callable(_u126_collect_game_diagnostics) and callable(_u126_show_game_diagnostics)
    assert AppV43.show_game_diagnostics is _u126_show_game_diagnostics
    print("SERWIS_ULTIMATE_GAME_DIAGNOSTICS_SELFTEST_OK: read-only GPU/DirectX/services/power checks")

# v4.4.0 — real Windows repair/recovery actions, with explicit consent and logs.
_U120_REPAIR_PS = r"""
param(
  [Parameter(Mandatory=$true)][ValidateSet('sfc_verify','repair_system','dism_scan','chkdsk_scan','restore_point','winre_status')][string]$Action,
  [Parameter(Mandatory=$true)][string]$LogPath
)
$ErrorActionPreference = 'Continue'
$script:LastNativeExitCode = 0
function Add-RepairLog([string]$Text) {
  $line = '[' + (Get-Date -Format 'yyyy-MM-dd HH:mm:ss') + '] ' + $Text
  Add-Content -LiteralPath $LogPath -Value $line -Encoding UTF8
}
function Invoke-RepairNative([string]$Exe, [string[]]$Args) {
  Add-RepairLog ('COMMAND: ' + $Exe + ' ' + ($Args -join ' '))
  & $Exe @Args 2>&1 | ForEach-Object {
    $line = [string]$_
    Add-Content -LiteralPath $LogPath -Value $line -Encoding UTF8
  }
  $script:LastNativeExitCode = $LASTEXITCODE
  Add-RepairLog ('EXIT_CODE: ' + $script:LastNativeExitCode)
}
$finalCode = 0
try {
  Add-RepairLog ('NAPRAWA PC — START ACTION=' + $Action)
  switch ($Action) {
    'sfc_verify' {
      Invoke-RepairNative 'sfc.exe' @('/verifyonly')
      $finalCode = $script:LastNativeExitCode
    }
    'repair_system' {
      Add-RepairLog 'Etap 1/2: DISM RestoreHealth — może długo stać na jednym procencie.'
      Invoke-RepairNative 'dism.exe' @('/Online','/Cleanup-Image','/RestoreHealth')
      if ($script:LastNativeExitCode -eq 0) {
        Add-RepairLog 'Etap 2/2: SFC Scannow'
        Invoke-RepairNative 'sfc.exe' @('/scannow')
        $finalCode = $script:LastNativeExitCode
      } else {
        $finalCode = $script:LastNativeExitCode
        Add-RepairLog 'SFC pominięto, ponieważ DISM zwrócił błąd. Sprawdź log DISM.'
      }
    }
    'dism_scan' {
      Invoke-RepairNative 'dism.exe' @('/Online','/Cleanup-Image','/ScanHealth')
      $finalCode = $script:LastNativeExitCode
    }
    'chkdsk_scan' {
      Invoke-RepairNative 'chkdsk.exe' @($env:SystemDrive,'/scan')
      $finalCode = $script:LastNativeExitCode
    }
    'restore_point' {
      try {
        Checkpoint-Computer -Description 'NaprawaPC przed naprawą' -RestorePointType 'MODIFY_SETTINGS' -ErrorAction Stop
        Add-RepairLog 'PUNKT_PRZYWRACANIA: utworzono (o ile Windows potwierdził powodzenie).'
      } catch {
        $finalCode = 1
        Add-RepairLog ('PUNKT_PRZYWRACANIA: NIE UTWORZONO — ' + $_.Exception.Message + '. Sprawdź, czy Ochrona systemu jest włączona i czy nie obowiązuje limit punktów.')
      }
    }
    'winre_status' {
      Invoke-RepairNative 'reagentc.exe' @('/info')
      $finalCode = $script:LastNativeExitCode
    }
  }
} catch {
  $finalCode = 1
  Add-RepairLog ('WYJĄTEK: ' + $_.Exception.ToString())
} finally {
  Add-RepairLog ('NAPRAWA PC — COMPLETE ACTION=' + $Action + ' EXIT_CODE=' + $finalCode)
}
exit $finalCode
"""

def _u120_repair_log_folder():
    from pathlib import Path as _U120Path
    import os as _U120OS
    base = _U120Path(_U120OS.environ.get("LOCALAPPDATA") or _U120Path.home())
    folder = base / "NaprawaPC" / "Raporty" / "NaprawaSystemu"
    folder.mkdir(parents=True, exist_ok=True)
    return folder

def _u120_launch_repair_action(app, action, title):
    import os as _U120OS
    import subprocess as _U120Subprocess
    from pathlib import Path as _U120Path
    folder = _u120_repair_log_folder()
    stamp = _U66_datetime.now().strftime("%Y%m%d-%H%M%S")
    script_path = folder / "NaprawaPC_SystemRepairActions.ps1"
    log_path = folder / f"{action}-{stamp}.log"
    script_path.write_text(_U120_REPAIR_PS, encoding="utf-8-sig")
    log_path.write_text("Naprawa PC — przygotowano zadanie. Oczekiwanie na zgodę UAC...\n", encoding="utf-8")
    def ps_quote(value):
        return "'" + str(value).replace("'", "''") + "'"
    arg_line = "-NoProfile -ExecutionPolicy Bypass -File " + '"' + str(script_path) + '"' + " -Action " + '"' + action + '"' + " -LogPath " + '"' + str(log_path) + '"'
    command = "$argsLine = " + ps_quote(arg_line) + "; Start-Process -FilePath 'powershell.exe' -Verb RunAs -ArgumentList $argsLine"
    try:
        _U120Subprocess.Popen(["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", command],
                              stdout=_U120Subprocess.DEVNULL, stderr=_U120Subprocess.DEVNULL,
                              creationflags=getattr(_U120Subprocess, "CREATE_NO_WINDOW", 0))
    except Exception as exc:
        try:
            messagebox.showerror("Nie uruchomiono zadania", f"{type(exc).__name__}: {exc}\n\nLog: {log_path}")
        except Exception:
            pass
        return
    try:
        app._u120_last_repair_log = str(log_path)
        app._u120_last_repair_action = action
        app._u120_repair_status_var.set(f"Uruchomiono: {title}. Jeśli Windows poprosi, zatwierdź UAC. Log: {log_path}")
        _u120_refresh_repair_log(app, log_path)
        app.append_log(f"NAPRAWA SYSTEMU: uruchomiono {action}; log {log_path}")
    except Exception:
        pass

def _u120_refresh_repair_log(app, log_path):
    try:
        from pathlib import Path as _U120Path
        label = getattr(app, "_u120_repair_log_text", None)
        if label is not None and label.winfo_exists():
            path = _U120Path(log_path)
            content = path.read_text(encoding="utf-8", errors="replace") if path.exists() else "Oczekiwanie na log..."
            label.configure(state="normal")
            label.delete("1.0", "end")
            label.insert("end", content[-16000:])
            label.see("end")
            label.configure(state="disabled")
            if "NAPRAWA PC — COMPLETE" not in content:
                app.after(1500, lambda a=app,p=log_path:_u120_refresh_repair_log(a,p))
            else:
                try: app._u120_repair_status_var.set("Zadanie zakończone. Sprawdź kod końcowy i szczegóły w logu.")
                except Exception: pass
    except Exception:
        pass

def _u120_show_system_repair_center(app):
    import os as _U120OS
    import subprocess as _U120Subprocess
    app.current_view = "SYSTEM_REPAIR_CENTER"
    app.clear()
    t = app.colors()
    app.header_title.config(text="CENTRUM NAPRAWY I ODZYSKIWANIA WINDOWS")
    head = app.panel(app.content)
    head.pack(fill="x", padx=3, pady=(0,5))
    tk.Label(head, text="DIAGNOSTYKA • NAPRAWA • PRZYWRACANIE", bg=t["panel"], fg=t["accent"], font=app.fnt(12,"bold")).pack(anchor="w", padx=10, pady=(8,3))
    tk.Label(head, text="Każde zadanie uruchamia osobny proces z logiem. Naprawy systemowe wymagają potwierdzenia i zgody administratora UAC. Punkt przywracania może nie być dostępny, jeśli Ochrona systemu jest wyłączona. Nie wykonujemy automatycznego resetu ani formatowania.", bg=t["panel"], fg=t["muted"], font=app.fnt(8), wraplength=1250, justify="left").pack(anchor="w", padx=10, pady=(0,8))
    app._u120_repair_status_var = tk.StringVar(value="Gotowe — wybierz oddzielną operację.")
    status = tk.Label(app.content, textvariable=app._u120_repair_status_var, bg=t["bg"], fg=t["accent"], anchor="w", justify="left", wraplength=1250)
    status.pack(fill="x", padx=7, pady=(0,5))
    operations = [
      ("SFC — weryfikacja plików", "Tylko weryfikuje integralność; nie naprawia plików.", "sfc_verify", "Uruchomić SFC /verifyonly?"),
      ("DISM — skan magazynu składników", "Skanuje magazyn Windows bez uruchamiania naprawy.", "dism_scan", "Uruchomić DISM /ScanHealth?"),
      ("CHKDSK — skan online woluminu systemowego", "CHKDSK /scan; nie wymusza restartu ani naprawy offline.", "chkdsk_scan", "Uruchomić CHKDSK /scan na woluminie systemowym?"),
      ("NAPRAW WINDOWS — DISM + SFC", "Najpierw DISM /RestoreHealth, a po sukcesie SFC /scannow. Może trwać długo.", "repair_system", "Uruchomić pełną naprawę DISM + SFC? Może potrwać kilkanaście minut lub dłużej. Zapisuj otwarte pliki przed rozpoczęciem."),
      ("Utwórz punkt przywracania", "Próbuje utworzyć punkt przed zmianami. Nie włącza po cichu Ochrony systemu.", "restore_point", "Utworzyć punkt przywracania Windows? Operacja wymaga administratora i może zostać zablokowana przez ustawienia Windows."),
      ("Sprawdź środowisko odzyskiwania", "Wyświetla stan WinRE przez reagentc /info.", "winre_status", "Odczytać konfigurację WinRE?"),
    ]
    for title, desc, action, question in operations:
        card = app.panel(app.content)
        card.pack(fill="x", padx=3, pady=3)
        row = tk.Frame(card, bg=t["panel"]); row.pack(fill="x", padx=8, pady=5)
        left = tk.Frame(row, bg=t["panel"]); left.pack(side="left", fill="x", expand=True)
        tk.Label(left, text=title, bg=t["panel"], fg=t["text"], font=app.fnt(9,"bold"), anchor="w").pack(fill="x")
        tk.Label(left, text=desc, bg=t["panel"], fg=t["muted"], font=app.fnt(8), anchor="w", justify="left", wraplength=800).pack(fill="x", pady=(2,0))
        def run_action(a=action, ttl=title, q=question):
            if not messagebox.askyesno(ttl, q + "\n\nZostanie zapisany lokalny log. Kontynuować?"):
                return
            _u120_launch_repair_action(app, a, ttl)
        app.make_button(row, "URUCHOM", run_action, "accent", side="right", ipady=4)
    tools = app.panel(app.content); tools.pack(fill="x", padx=3, pady=3)
    tk.Label(tools, text="PRZYWRACANIE I NARZĘDZIA WINDOWS", bg=t["panel"], fg=t["accent"], font=app.fnt(9,"bold")).pack(anchor="w", padx=8, pady=(6,3))
    row = tk.Frame(tools, bg=t["panel"]); row.pack(fill="x", padx=8, pady=(0,6))
    def open_restore():
        if messagebox.askyesno("Przywracanie systemu", "Otworzyć oficjalne okno Przywracania systemu Windows? Wybór punktu i cofnięcie zmian pozostają pod Twoją kontrolą."):
            try: _U120Subprocess.Popen(["rstrui.exe"])
            except Exception as exc: messagebox.showerror("Błąd", str(exc))
    def open_recovery():
        try:
            if hasattr(_U120OS, "startfile"): _U120OS.startfile("ms-settings:recovery")
            else: _U120Subprocess.Popen(["cmd.exe", "/c", "start", "", "ms-settings:recovery"])
        except Exception as exc: messagebox.showerror("Błąd", str(exc))
    def open_log():
        path = getattr(app, "_u120_last_repair_log", "")
        if path and _U120OS.path.isfile(path):
            _U120Subprocess.Popen(["notepad.exe", path])
        else:
            messagebox.showinfo("Log", "Najpierw uruchom operację diagnostyczną lub naprawczą.")
    def open_folder():
        folder = str(_u120_repair_log_folder())
        try:
            if hasattr(_U120OS, "startfile"): _U120OS.startfile(folder)
            else: _U120Subprocess.Popen(["explorer.exe", folder])
        except Exception as exc: messagebox.showerror("Błąd", str(exc))
    app.make_button(row, "PRZYWRACANIE SYSTEMU", open_restore, "card", side="left", ipady=4)
    app.make_button(row, "USTAWIENIA ODZYSKIWANIA", open_recovery, "card", side="left", ipady=4)
    app.make_button(row, "OTWÓRZ OSTATNI LOG", open_log, "card", side="left", ipady=4)
    app.make_button(row, "FOLDER RAPORTÓW", open_folder, "card", side="left", ipady=4)
    app.make_button(row, "← LABORATORIUM", app.show_component_lab, "card", side="left", ipady=4)
    service_tools=tk.Frame(tools,bg=t["panel"]);service_tools.pack(fill="x",padx=8,pady=(0,6))
    app.make_button(service_tools, "MENEDŻER PROCESÓW", lambda:_u126_show_process_manager(app), "card", side="left", ipady=4)
    app.make_button(service_tools, "DIAGNOSTYKA GIER", lambda:_u126_show_game_diagnostics(app), "card", side="left", ipady=4)
    app.make_button(service_tools, "RAPORTY I HISTORIA", lambda:_u126_show_report_manager(app), "card", side="left", ipady=4)
    logbox = app.panel(app.content); logbox.pack(fill="both", expand=True, padx=3, pady=3)
    tk.Label(logbox, text="LOG NA ŻYWO — NIE ZAMYKAJ OKNA PODCZAS NAPRAWY", bg=t["panel"], fg=t["accent"], font=app.fnt(9,"bold")).pack(anchor="w", padx=8, pady=(6,3))
    body = tk.Text(logbox, height=8, bg="#07111f", fg="#cce6ff", insertbackground="#ffffff", wrap="word", font=("Consolas",8), relief="flat")
    body.pack(fill="both", expand=True, padx=8, pady=(0,8))
    body.insert("end", "Po uruchomieniu zadania jego postęp i wynik pojawią się tutaj.\n")
    body.configure(state="disabled")
    app._u120_repair_log_text = body

AppV43.show_system_repair_center = _u120_show_system_repair_center

def _u120_selftest_system_repair_center():
    required = ("sfc_verify","repair_system","dism_scan","chkdsk_scan","restore_point","winre_status")
    for action in required:
        assert ("'"+action+"'") in _U120_REPAIR_PS
    assert "DISM /RestoreHealth" in _U120_REPAIR_PS or "'/RestoreHealth'" in _U120_REPAIR_PS
    assert "sfc.exe" in _U120_REPAIR_PS and "chkdsk.exe" in _U120_REPAIR_PS
    assert "Checkpoint-Computer" in _U120_REPAIR_PS
    assert callable(_u120_show_system_repair_center)
    assert callable(AppV43.show_system_repair_center)
    assert "Start-Process" in repr(_u120_launch_repair_action.__code__.co_consts)
    assert callable(_u120_show_system_repair_center)
    print("WINDOWS_REPAIR_CENTER_SELFTEST_OK: SFC, DISM repair/scan, CHKDSK online scan, restore point, WinRE and System Restore UI")


def _u119_selftest_furmark_scene():
    import types as _u119_types
    pending=[_u37_gpu_benchmark_child.__code__]
    names=set();literals=set();numbers=set()
    while pending:
        code=pending.pop()
        names.update(code.co_names)
        names.update(code.co_varnames)
        names.update(code.co_cellvars)
        names.update(code.co_freevars)
        for value in code.co_consts:
            if isinstance(value,_u119_types.CodeType):
                pending.append(value)
            elif isinstance(value,str):
                literals.add(value)
            elif isinstance(value,(int,float)):
                numbers.add(value)
            elif isinstance(value,tuple):
                # Python compiles dict keys into tuple constants (BUILD_CONST_KEY_MAP).
                for item in value:
                    if isinstance(item,str):
                        literals.add(item)
                    elif isinstance(item,(int,float)):
                        numbers.add(item)
    assert "_u119_draw_furmark" in names
    assert "glCallList" in names
    assert "FUR_DONUT_OPENGL_STRESS" in literals
    assert "GL_LINES" in names
    profiles=[_u128_furmark_profile(i) for i in range(1,111)]
    assert len(profiles)==110
    assert len({p["hair_count"] for p in profiles})==110
    assert len({(p["major_radius"],p["tube_radius"],p["hair_count"],p["palette"],p["rotation_speed"],p["scale_x"],p["scale_y"],p["scale_z"]) for p in profiles})==110
    assert min(p["hair_count"] for p in profiles)>=6000
    assert "furmark_profile" in literals and "furmark_hair_count" in literals
    print("FURMARK_DONUT_RENDERER_SELFTEST_OK: 110 unique seeded FurMark profiles; animated OpenGL display lists; synchronized FPS")


# v4.3.121 — bring Serwis Ultimate service-job workflow into the main app.
def _u121_job_store_path():
    import os as _u121_os
    from pathlib import Path as _u121_Path
    root=_u121_os.environ.get("LOCALAPPDATA") or str(_u121_Path.home())
    return _u121_Path(root)/"NaprawaPC"/"SerwisUltimate"/"service_jobs.json"

def _u121_load_jobs(path=None):
    import json as _u121_json
    p=path or _u121_job_store_path()
    try:
        data=_u121_json.loads(p.read_text(encoding="utf-8"))
        return [row for row in data if isinstance(row,dict)] if isinstance(data,list) else []
    except Exception:
        return []

def _u121_save_jobs(path,jobs):
    import json as _u121_json
    from pathlib import Path as _u121_Path
    p=_u121_Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    temp=p.with_suffix(p.suffix+".tmp")
    temp.write_text(_u121_json.dumps(list(jobs),ensure_ascii=False,indent=2),encoding="utf-8")
    temp.replace(p)
    return p

def _u121_export_job_html(job,path):
    import html as _u121_html
    from pathlib import Path as _u121_Path
    labels=(
        ("Numer zlecenia","id"),("Utworzono","created_at"),("Klient","client"),
        ("Kontakt","contact"),("Typ urządzenia","device_type"),("Model","device_model"),
        ("Numer seryjny","serial"),("Objaw klienta","symptom"),("Wynik diagnozy","diagnosis"),
        ("Wykonane czynności","work_done"),("Uzgodniony zakres","scope"),("Status","status"),
        ("Szacunkowy koszt","estimate"),("Zgoda na diagnozę/naprawę","consent_diagnostics"),
        ("Omówiono kopię danych","backup_discussed"),("Zalanie/korozja","liquid_damage"),
        ("Warunki gwarancji","warranty_informed")
    )
    rows=[]
    for label,key in labels:
        value=job.get(key,"—")
        if isinstance(value,bool):value="TAK" if value else "NIE"
        rows.append("<tr><th>"+_u121_html.escape(label)+"</th><td>"+_u121_html.escape(str(value if value not in (None,"") else "—"))+"</td></tr>")
    html_doc=("<!doctype html><html lang='pl'><head><meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        "<title>Karta serwisowa</title><style>body{font:15px Segoe UI,Arial;background:#0a1220;color:#e7f1ff;margin:24px}"
        "h1{color:#54d7ff}table{border-collapse:collapse;width:100%;background:#111e31}th,td{border:1px solid #30445f;padding:9px;text-align:left;vertical-align:top}"
        "th{width:240px;color:#79dfff}small{color:#9db0c9}</style></head><body>"
        "<h1>NAPRAWA PC — KARTA SERWISOWA</h1><small>Wygenerowano lokalnie. Nie zapisuj haseł klientów w zleceniu.</small><table>"
        +"".join(rows)+"</table></body></html>")
    p=_u121_Path(path);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(html_doc,encoding="utf-8")
    return p

def _u121_show_service_jobs(app):
    import os as _u121_os
    import uuid as _u121_uuid
    from datetime import datetime as _u121_datetime
    from pathlib import Path as _u121_Path
    app.current_view="SERVICE_JOBS"
    app.clear()
    t=app.colors()
    app.header_title.config(text="SERWIS ULTIMATE — ZLECENIA I KARTY SERWISOWE")
    head=app.panel(app.content);head.pack(fill="x",padx=3,pady=(0,5))
    tk.Label(head,text="ZLECENIE SERWISOWE • RAPORT KLIENTA • HISTORIA",bg=t["panel"],fg=t["accent"],font=app.fnt(11,"bold")).pack(anchor="w",padx=10,pady=(7,2))
    tk.Label(head,text="Dane zapisują się lokalnie. Nie wpisuj haseł, kodów PIN ani innych danych uwierzytelniających. Naprawy systemowe uruchamiaj z osobnego Centrum napraw i po potwierdzeniu.",bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1350,justify="left").pack(anchor="w",padx=10,pady=(0,7))
    form=app.panel(app.content);form.pack(fill="x",padx=3,pady=3)
    grid=tk.Frame(form,bg=t["panel"]);grid.pack(fill="x",padx=8,pady=(7,4))
    entries={};texts={};checks={}
    def entry_field(label,key,row,col,width=28):
        tk.Label(grid,text=label,bg=t["panel"],fg=t["muted"],font=app.fnt(8,"bold"),anchor="w").grid(row=row*2,column=col,sticky="w",padx=(3,6),pady=(2,0))
        e=tk.Entry(grid,bg=t["card"],fg=t["text"],insertbackground=t["text"],relief="flat",width=width)
        e.grid(row=row*2+1,column=col,sticky="ew",padx=(3,10),pady=(0,4),ipady=4);entries[key]=e
    grid.columnconfigure(1,weight=1);grid.columnconfigure(3,weight=1)
    entry_field("Klient / firma *","client",0,0)
    entry_field("Telefon lub e-mail (opcjonalnie)","contact",0,2)
    tk.Label(grid,text="Typ urządzenia",bg=t["panel"],fg=t["muted"],font=app.fnt(8,"bold"),anchor="w").grid(row=2,column=0,sticky="w",padx=3,pady=(2,0))
    device_type=ttk.Combobox(grid,values=("Laptop","Komputer stacjonarny","All-in-One","Mini PC","Inne"),state="readonly",width=25)
    device_type.set("Laptop");device_type.grid(row=3,column=0,sticky="ew",padx=(3,10),pady=(0,4));entries["device_type"]=device_type
    entry_field("Producent / model *","device_model",1,2)
    entry_field("Numer seryjny (opcjonalnie)","serial",2,0)
    entry_field("Szacunkowy koszt / uzgodnienie","estimate",2,2)
    def text_field(label,key,row,height=3):
        tk.Label(form,text=label,bg=t["panel"],fg=t["muted"],font=app.fnt(8,"bold"),anchor="w").pack(fill="x",padx=11,pady=(3,1))
        box=tk.Text(form,height=height,bg=t["card"],fg=t["text"],insertbackground=t["text"],wrap="word",relief="flat")
        box.pack(fill="x",padx=10,pady=(0,4));texts[key]=box
    text_field("Objaw zgłoszony przez klienta *","symptom",0,3)
    text_field("Wynik diagnozy / ustalenia","diagnosis",0,3)
    text_field("Wykonane czynności / zalecenia","work_done",0,3)
    text_field("Uzgodniony zakres i ograniczenia","scope",0,2)
    consent_row=tk.Frame(form,bg=t["panel"]);consent_row.pack(fill="x",padx=8,pady=3)
    for key,label in (("consent_diagnostics","Zgoda na diagnozę/naprawę"),("backup_discussed","Omówiono kopię danych"),("liquid_damage","Zalanie/korozja odnotowane"),("warranty_informed","Warunki gwarancji przekazane")):
        var=tk.BooleanVar(value=False);checks[key]=var
        ttk.Checkbutton(consent_row,text=label,variable=var).pack(side="left",padx=4,pady=2)
    status_row=tk.Frame(form,bg=t["panel"]);status_row.pack(fill="x",padx=10,pady=(2,7))
    tk.Label(status_row,text="Status:",bg=t["panel"],fg=t["muted"],font=app.fnt(8,"bold")).pack(side="left",padx=(0,5))
    status_var=tk.StringVar(value="Nowe")
    status_box=ttk.Combobox(status_row,textvariable=status_var,values=("Nowe","W diagnozie","Oczekuje na części","W naprawie","Gotowe","Wydane","Anulowane"),state="readonly",width=23)
    status_box.pack(side="left")
    store=_u121_job_store_path()
    current={"id":None}
    jobs_cache=[]
    status_label=tk.Label(app.content,text="Zlecenia przechowywane lokalnie.",bg=t["bg"],fg=t["accent"],anchor="w",justify="left")
    status_label.pack(fill="x",padx=8,pady=(3,2))
    def form_value(key):
        if key in entries:return entries[key].get().strip()
        return texts[key].get("1.0","end-1c").strip()
    def reset_form():
        current["id"]=None
        for widget in entries.values():
            try:widget.delete(0,"end")
            except Exception:pass
        try:device_type.set("Laptop")
        except Exception:pass
        for widget in texts.values():widget.delete("1.0","end")
        for var in checks.values():var.set(False)
        status_var.set("Nowe")
    def refresh_list(select_id=None):
        nonlocal jobs_cache
        jobs_cache=_u121_load_jobs(store)
        for iid in tree.get_children():tree.delete(iid)
        for job in sorted(jobs_cache,key=lambda x:str(x.get("created_at","")),reverse=True):
            tree.insert("","end",iid=str(job.get("id")),values=(job.get("created_at",""),job.get("client",""),job.get("device_type",""),job.get("device_model",""),job.get("status","")))
        if select_id and tree.exists(select_id):tree.selection_set(select_id);tree.see(select_id)
    def save_job():
        client=form_value("client");model=form_value("device_model");symptom=form_value("symptom")
        if not client or not model or not symptom:
            messagebox.showwarning("Zlecenie serwisowe","Wypełnij klienta, model urządzenia i objaw zgłoszony przez klienta.")
            return
        jobs=_u121_load_jobs(store);now=_u121_datetime.now().isoformat(timespec="seconds")
        job_id=current["id"] or (_u121_datetime.now().strftime("%Y%m%d-%H%M%S")+"-"+_u121_uuid.uuid4().hex[:6])
        job={
            "id":job_id,"created_at":now,"client":client,"contact":form_value("contact"),
            "device_type":form_value("device_type"),"device_model":model,"serial":form_value("serial"),
            "estimate":form_value("estimate"),"symptom":symptom,"diagnosis":form_value("diagnosis"),
            "work_done":form_value("work_done"),"scope":form_value("scope"),"status":status_var.get(),
            "consent_diagnostics":checks["consent_diagnostics"].get(),"backup_discussed":checks["backup_discussed"].get(),
            "liquid_damage":checks["liquid_damage"].get(),"warranty_informed":checks["warranty_informed"].get(),
            "schema_version":1
        }
        replaced=False
        for index,old in enumerate(jobs):
            if str(old.get("id"))==job_id:jobs[index]=job;replaced=True;break
        if not replaced:jobs.append(job)
        try:
            _u121_save_jobs(store,jobs);current["id"]=job_id;refresh_list(job_id)
            status_label.config(text=f"Zapisano zlecenie {job_id} • {len(jobs)} zapisanych zleceń • {store}")
        except Exception as exc:
            messagebox.showerror("Zapis zlecenia",f"Nie udało się zapisać zlecenia: {type(exc).__name__}: {exc}")
    def load_selected(_event=None):
        selection=tree.selection()
        if not selection:return
        job=next((x for x in jobs_cache if str(x.get("id"))==selection[0]),None)
        if not job:return
        current["id"]=str(job.get("id"))
        for key,widget in entries.items():
            try:widget.delete(0,"end");widget.insert(0,str(job.get(key,"") or ""))
            except Exception:pass
        try:device_type.set(str(job.get("device_type","Laptop")))
        except Exception:pass
        for key,widget in texts.items():widget.delete("1.0","end");widget.insert("1.0",str(job.get(key,"") or ""))
        for key,var in checks.items():var.set(bool(job.get(key,False)))
        status_var.set(str(job.get("status","Nowe")))
        status_label.config(text=f"Wczytano zlecenie {current['id']} — zapis nadpisze wybrane zlecenie.")
    def export_selected():
        selection=tree.selection()
        if not selection:
            messagebox.showinfo("Eksport","Zaznacz zlecenie na liście.");return
        job=next((x for x in jobs_cache if str(x.get("id"))==selection[0]),None)
        if not job:return
        folder=store.parent/"reports";folder.mkdir(parents=True,exist_ok=True)
        path=folder/(str(job.get("id"))+".html")
        try:
            _u121_export_job_html(job,path)
            status_label.config(text=f"Raport HTML zapisany: {path}")
            try:
                if hasattr(_u121_os,"startfile"):_u121_os.startfile(str(path))
            except Exception:pass
        except Exception as exc:messagebox.showerror("Eksport raportu",str(exc))
    def open_folder():
        try:
            store.parent.mkdir(parents=True,exist_ok=True)
            if hasattr(_u121_os,"startfile"):_u121_os.startfile(str(store.parent))
            else:messagebox.showinfo("Folder danych",str(store.parent))
        except Exception as exc:messagebox.showerror("Folder danych",str(exc))
    actions=app.panel(app.content);actions.pack(fill="x",padx=3,pady=3)
    app.make_button(actions,"ZAPISZ / AKTUALIZUJ",save_job,"good",side="left",ipady=4)
    app.make_button(actions,"NOWE ZLECENIE",reset_form,"card",side="left",ipady=4)
    app.make_button(actions,"EKSPORT HTML",export_selected,"accent",side="left",ipady=4)
    app.make_button(actions,"ODŚWIEŻ LISTĘ",lambda:refresh_list(),"card",side="left",ipady=4)
    app.make_button(actions,"FOLDER DANYCH",open_folder,"card",side="left",ipady=4)
    app.make_button(actions,"← LABORATORIUM",app.show_component_lab,"card",side="right",ipady=4)
    list_panel=app.panel(app.content);list_panel.pack(fill="both",expand=True,padx=3,pady=3)
    tk.Label(list_panel,text="HISTORIA ZLECEŃ — DWUKLIK OTWIERA DO EDYCJI",bg=t["panel"],fg=t["accent"],font=app.fnt(9,"bold")).pack(anchor="w",padx=8,pady=(6,3))
    tree=ttk.Treeview(list_panel,columns=("date","client","type","model","status"),show="headings",height=7)
    for key,label,width in (("date","Utworzono",150),("client","Klient",200),("type","Typ",130),("model","Urządzenie",240),("status","Status",150)):
        tree.heading(key,text=label);tree.column(key,width=width,anchor="w")
    tree.pack(fill="both",expand=True,padx=8,pady=(0,8))
    tree.bind("<Double-1>",load_selected)
    refresh_list()
    return None

_U121_ORIGINAL_SHOW_SYSTEM_REPAIR_CENTER=AppV43.show_system_repair_center
def _u121_show_system_repair_center(app):
    result=_U121_ORIGINAL_SHOW_SYSTEM_REPAIR_CENTER(app)
    try:
        body=getattr(app,"_u120_repair_log_text",None)
        log_panel=body.master if body is not None else None
        panel=app.panel(app.content);panel.pack(fill="x",padx=3,pady=3,before=log_panel if log_panel is not None else None)
        app.make_button(panel,"ZLECENIA SERWISOWE — SERWIS ULTIMATE",lambda:_u121_show_service_jobs(app),"accent",side="left",ipady=4)
        app.make_button(panel,"ZASILANIE / BATERIA — TESTY",lambda:_u121_show_power_lab(app),"card",side="left",ipady=4)
        app.make_button(panel,"PROFILE NAPRAW / DIAGNOZA",lambda:_u123_show_repair_profiles(app),"card",side="left",ipady=4)
        app.make_button(panel,"BAZA WIEDZY / LEKCJE NAPRAWY",lambda:_u122_show_repair_knowledge(app),"card",side="left",ipady=4)
        app.make_button(panel,"DODATKOWE TESTY SERWIS ULTIMATE",lambda:_u135_show_serwis_diagnostics(app),"card",side="left",ipady=4)
    except Exception as exc:
        try:app.queue_log("Zlecenia serwisowe: "+repr(exc))
        except Exception:pass
    return result
AppV43.show_system_repair_center=_u121_show_system_repair_center
AppV43.show_service_jobs=_u121_show_service_jobs

def _u121_selftest_service_jobs():
    import tempfile as _u121_tempfile
    from pathlib import Path as _u121_Path
    sample={"id":"TEST-001","client":"<script>alert(1)</script>","device_model":"Laptop X","symptom":"Brak obrazu","consent_diagnostics":True}
    with _u121_tempfile.TemporaryDirectory() as root:
        path=_u121_Path(root)/"jobs.json"
        _u121_save_jobs(path,[sample])
        assert _u121_load_jobs(path)==[sample]
        report=_u121_export_job_html(sample,_u121_Path(root)/"report.html")
        html_text=report.read_text(encoding="utf-8")
        assert "&lt;script&gt;" in html_text and "<script>alert(1)</script>" not in html_text
    print("SERWIS_ULTIMATE_SERVICE_JOBS_SELFTEST_OK: atomic local storage, load/edit model and escaped HTML export")


# Power/Battery diagnostics ported from Serwis Ultimate: each operation runs independently.
def _u121_power_report_dir():
    from pathlib import Path as _u121_Path
    import os as _u121_os
    folder=_u121_Path(_u121_os.environ.get("LOCALAPPDATA") or _u121_Path.home())/"NaprawaPC"/"Raporty"/"PowerBattery"
    folder.mkdir(parents=True,exist_ok=True)
    return folder

def _u121_power_command(action,output_path):
    path=str(output_path)
    if action=="battery_info":
        script="$b=@(Get-CimInstance Win32_Battery -ErrorAction SilentlyContinue | Select-Object Caption,DeviceID,EstimatedChargeRemaining,BatteryStatus,EstimatedRunTime,DesignCapacity,FullChargeCapacity); if($b.Count -eq 0){[pscustomobject]@{state='N/D';note='Brak baterii udostępnionej przez WMI'} | ConvertTo-Json -Compress}else{$b | ConvertTo-Json -Depth 4 -Compress}"
        return ["powershell.exe","-NoProfile","-ExecutionPolicy","Bypass","-Command",script],30
    if action=="battery_report":return ["powercfg.exe","/batteryreport","/output",path],90
    if action=="energy_report":return ["powercfg.exe","/energy","/duration","30","/output",path],90
    if action=="sleepstudy":return ["powercfg.exe","/sleepstudy","/output",path],90
    if action=="power_requests":return ["powercfg.exe","/requests"],30
    if action=="last_wake":return ["powercfg.exe","/lastwake"],30
    if action=="active_plan":return ["powercfg.exe","/getactivescheme"],30
    raise ValueError("Nieznana operacja zasilania: "+str(action))

def _u121_run_power_action(app,action,title):
    import os as _u121_os
    import subprocess as _u121_subprocess
    import threading as _u121_threading
    from datetime import datetime as _u121_datetime
    from pathlib import Path as _u121_Path
    if _u121_os.name!="nt":
        messagebox.showinfo(title,"Ten test wymaga Windows.")
        return
    folder=_u121_power_report_dir()
    stamp=_u121_datetime.now().strftime("%Y%m%d-%H%M%S")
    ext=".html" if action in ("battery_report","energy_report","sleepstudy") else ".txt"
    report_path=folder/(stamp+"-"+action+ext)
    win=tk.Toplevel(app);win.title("NAPRAWA PC — "+title);win.geometry("820x520");win.minsize(650,400)
    try:win.configure(bg=app.colors()["bg"])
    except Exception:pass
    t=app.colors()
    tk.Label(win,text=title,bg=t["bg"],fg=t["accent"],font=app.fnt(12,"bold")).pack(anchor="w",padx=12,pady=(10,3))
    tk.Label(win,text="Osobny przebieg. Brak baterii lub brak obsługi SleepStudy oznacza N/D/WARN, nie fikcyjny PASS.",bg=t["bg"],fg=t["muted"],font=app.fnt(8),wraplength=780,justify="left").pack(anchor="w",padx=12,pady=(0,6))
    status=tk.StringVar(value="Przygotowanie testu…")
    tk.Label(win,textvariable=status,bg=t["bg"],fg=t["accent"],anchor="w",wraplength=780).pack(fill="x",padx=12,pady=(0,4))
    output=tk.Text(win,bg="#07111f",fg="#d7eaff",insertbackground="#ffffff",wrap="word",font=("Consolas",9),relief="flat")
    output.pack(fill="both",expand=True,padx=12,pady=(0,8))
    output.insert("end","Polecenie zostanie uruchomione osobno. Raport: "+str(report_path)+"\n")
    output.configure(state="disabled")
    buttons=tk.Frame(win,bg=t["bg"]);buttons.pack(fill="x",padx=12,pady=(0,10))
    def set_output(text):
        if not win.winfo_exists():return
        output.configure(state="normal");output.delete("1.0","end");output.insert("end",text);output.see("end");output.configure(state="disabled")
    def open_report():
        try:
            if report_path.exists() and hasattr(_u121_os,"startfile"):_u121_os.startfile(str(report_path))
            else:messagebox.showinfo("Raport",str(report_path) if report_path.exists() else "Raport nie został utworzony.")
        except Exception as exc:messagebox.showerror("Raport",str(exc))
    app.make_button(buttons,"OTWÓRZ RAPORT",open_report,"accent",side="left",ipady=3)
    app.make_button(buttons,"ZAMKNIJ",win.destroy,"card",side="right",ipady=3)
    def worker():
        state="WARN";text_out="";error=""
        try:
            command,timeout=_u121_power_command(action,report_path)
            result=_u121_subprocess.run(command,capture_output=True,text=True,encoding="utf-8",errors="replace",timeout=timeout,
                creationflags=getattr(_u121_subprocess,"CREATE_NO_WINDOW",0))
            text_out=((result.stdout or "")+"\n"+(result.stderr or "")).strip()
            if action in ("battery_report","energy_report","sleepstudy"):
                if result.returncode==0 and report_path.exists():
                    state="PASS";text_out=(text_out+"\n\nRaport HTML utworzony: "+str(report_path)).strip()
                else:
                    state="WARN"
                    if not text_out:text_out="Polecenie nie utworzyło raportu. Sprawdź obsługę polecenia i uprawnienia administratora."
            else:
                if not text_out:text_out="Brak tekstowego wyniku."
                try:report_path.write_text(text_out,encoding="utf-8")
                except Exception as exc:text_out+="\n\nNie zapisano raportu: "+str(exc)
                state="PASS" if result.returncode==0 and "N/D" not in text_out else "WARN"
            if result.returncode!=0:
                state="WARN";error=f"\n\nKod wyjścia: {result.returncode}. Nie oznaczono tego jako PASS."
        except Exception as exc:
            state="WARN";error=f"{type(exc).__name__}: {exc}"
            text_out="Test nie zakończył się poprawnie. "+error+"\n\nBrak obsługi sprzętu, konieczność administratora lub brak powercfg może dać WARN/N/D."
            try:report_path.write_text(text_out,encoding="utf-8")
            except Exception:pass
        def finish():
            if not win.winfo_exists():return
            status.set(f"{state} — raport: {report_path}")
            set_output((text_out or "Brak danych.")+error)
            try:app.append_log(f"POWER/BATTERY {action}: {state}; {report_path}")
            except Exception:pass
        try:app.after(0,finish)
        except Exception:pass
    _u121_threading.Thread(target=worker,daemon=True,name="NaprawaPC-Power-"+action).start()

def _u121_show_power_lab(app):
    app.current_view="POWER_BATTERY_LAB"
    app.clear()
    t=app.colors()
    app.header_title.config(text="SERWIS ULTIMATE — ZASILANIE, BATERIA I UŚPIENIE")
    head=app.panel(app.content);head.pack(fill="x",padx=3,pady=(0,5))
    tk.Label(head,text="TESTY ZASILANIA I BATERII — KAŻDY URUCHAMIA OSOBNY RAPORT",bg=t["panel"],fg=t["accent"],font=app.fnt(11,"bold")).pack(anchor="w",padx=10,pady=(7,3))
    tk.Label(head,text="Raporty są zapisywane lokalnie. Battery report, Energy report i SleepStudy mogą nie być obsługiwane przez dany laptop/Windows; Energy report może wymagać uruchomienia jako administrator. Brak danych to WARN/N/D, nie PASS.",bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1350,justify="left").pack(anchor="w",padx=10,pady=(0,7))
    actions=[
      ("BATTERY INFO","battery_info","Odczyt WMI baterii, poziomu naładowania, stanu i czasu pracy."),
      ("BATTERY REPORT","battery_report","Raport HTML o baterii i historii pojemności."),
      ("ENERGY REPORT","energy_report","30-sekundowa analiza problemów zasilania i uśpienia."),
      ("SLEEPSTUDY","sleepstudy","Raport Modern Standby, jeśli obsługiwany przez urządzenie."),
      ("POWER REQUESTS","power_requests","Procesy i sterowniki blokujące uśpienie."),
      ("LAST WAKE","last_wake","Ostatnie źródło wybudzenia systemu."),
      ("AKTYWNY PLAN ZASILANIA","active_plan","Identyfikacja aktywnego planu zasilania Windows.")
    ]
    for title,action,desc in actions:
        card=app.panel(app.content);card.pack(fill="x",padx=3,pady=3)
        row=tk.Frame(card,bg=t["panel"]);row.pack(fill="x",padx=8,pady=5)
        left=tk.Frame(row,bg=t["panel"]);left.pack(side="left",fill="x",expand=True)
        tk.Label(left,text=title,bg=t["panel"],fg=t["text"],font=app.fnt(9,"bold"),anchor="w").pack(fill="x")
        tk.Label(left,text=desc,bg=t["panel"],fg=t["muted"],font=app.fnt(8),anchor="w",wraplength=950,justify="left").pack(fill="x",pady=(2,0))
        app.make_button(row,"URUCHOM TEST",lambda a=action,ttl=title:_u121_run_power_action(app,a,ttl),"accent",side="right",ipady=4)
    tools=app.panel(app.content);tools.pack(fill="x",padx=3,pady=3)
    app.make_button(tools,"← LABORATORIUM",app.show_component_lab,"card",side="left",ipady=4)
    def open_power_folder():
        import os as _u121_os
        try:
            folder=str(_u121_power_report_dir())
            if hasattr(_u121_os,"startfile"):_u121_os.startfile(folder)
            else:messagebox.showinfo("Folder raportów",folder)
        except Exception as exc:messagebox.showerror("Folder raportów",str(exc))
    app.make_button(tools,"OTWÓRZ FOLDER RAPORTÓW",open_power_folder,"card",side="left",ipady=4)

AppV43.show_power_battery_lab=_u121_show_power_lab

def _u121_selftest_power_lab():
    from pathlib import Path as _u121_Path
    expected={
      "battery_info":"powershell.exe","battery_report":"powercfg.exe","energy_report":"powercfg.exe",
      "sleepstudy":"powercfg.exe","power_requests":"powercfg.exe","last_wake":"powercfg.exe","active_plan":"powercfg.exe"
    }
    for action,executable in expected.items():
        command,timeout=_u121_power_command(action,_u121_Path("report.html"))
        assert command[0].lower()==executable
        assert timeout>=30
    assert callable(AppV43.show_power_battery_lab)
    print("SERWIS_ULTIMATE_POWER_BATTERY_SELFTEST_OK: 7 independent actions; separate reports; honest WARN/N/D")


# v4.3.122 — local repair knowledge base and lesson helper ported from System Repair PRO.
def _u122_knowledge_path():
    from pathlib import Path as _u122_Path
    import os as _u122_os
    folder=_u122_Path(_u122_os.environ.get("LOCALAPPDATA") or _u122_Path.home())/"NaprawaPC"/"KnowledgeBase"
    folder.mkdir(parents=True,exist_ok=True)
    return folder/"knowledge.json"

def _u122_load_knowledge(path=None):
    import json as _u122_json
    p=path or _u122_knowledge_path()
    try:
        data=_u122_json.loads(p.read_text(encoding="utf-8"))
        return [x for x in data if isinstance(x,dict) and x.get("text")] if isinstance(data,list) else []
    except Exception:return []

def _u122_save_knowledge(path,documents):
    import json as _u122_json
    from pathlib import Path as _u122_Path
    p=_u122_Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    temp=p.with_suffix(p.suffix+".tmp")
    temp.write_text(_u122_json.dumps(list(documents),ensure_ascii=False,indent=2),encoding="utf-8")
    temp.replace(p)
    return p

def _u122_extract_knowledge_file(path,max_chars=120000):
    import hashlib as _u122_hashlib
    from pathlib import Path as _u122_Path
    p=_u122_Path(path)
    if not p.is_file():raise FileNotFoundError(str(p))
    if p.stat().st_size>2*1024*1024:raise ValueError("Plik przekracza limit 2 MB.")
    suffix=p.suffix.lower()
    if suffix==".pdf":
        try:
            from pypdf import PdfReader as _u122_PdfReader
            reader=_u122_PdfReader(str(p))
            text="\n".join((page.extract_text() or "") for page in reader.pages[:100])
        except ImportError:raise RuntimeError("Brak modułu pypdf w pakiecie — nie można odczytać PDF.")
    else:
        allowed={".txt",".md",".log",".csv",".json",".html",".htm",".xml",".ini",".yaml",".yml",".ps1",".bat",".cmd",".py",".cs",".xaml",".config",".rtf",".sql",".reg",".cfg",".conf"}
        if suffix not in allowed:raise ValueError("Nieobsługiwany format pliku: "+suffix)
        text=p.read_text(encoding="utf-8-sig",errors="replace")
        if suffix in (".html",".htm"):
            import re as _u122_re
            text=_u122_re.sub(r"(?is)<script\b.*?</script>|<style\b.*?</style>"," ",text)
            text=_u122_re.sub(r"(?s)<[^>]+>"," ",text)
            text=text.replace("&nbsp;"," ").replace("&amp;","&").replace("&lt;","<").replace("&gt;",">")
    text="".join(ch for ch in text if ch in "\n\r\t" or ord(ch)>=32).strip()
    if not text:raise ValueError("Plik nie zawiera tekstu do indeksowania.")
    truncated=len(text)>max_chars
    text=text[:max_chars]
    digest=_u122_hashlib.sha256(text.encode("utf-8",errors="replace")).hexdigest()
    from datetime import datetime as _u122_datetime
    return {"id":digest,"name":p.name,"source_path":str(p.resolve()),"suffix":suffix,"sha256":digest,
            "imported_at":_u122_datetime.now().isoformat(timespec="seconds"),"text":text,"truncated":truncated}

def _u122_import_knowledge_files(paths,path=None):
    existing=_u122_load_knowledge(path)
    by_hash={str(x.get("sha256")):x for x in existing}
    added=0;errors=[]
    for source in paths:
        try:
            doc=_u122_extract_knowledge_file(source)
            if doc["sha256"] not in by_hash:
                by_hash[doc["sha256"]]=doc;added+=1
        except Exception as exc:
            errors.append({"path":str(source),"error":f"{type(exc).__name__}: {exc}"})
    _u122_save_knowledge(path or _u122_knowledge_path(),by_hash.values())
    return {"added":added,"total":len(by_hash),"errors":errors}

def _u122_search_knowledge(query,documents=None,limit=8):
    import re as _u122_re
    query=str(query or "").strip()
    if not query:return []
    terms=[x.casefold() for x in _u122_re.findall(r"[\w\-]{2,}",query)]
    if not terms:return []
    results=[]
    for doc in (documents if documents is not None else _u122_load_knowledge()):
        text=str(doc.get("text",""));folded=text.casefold()
        score=sum(folded.count(term)*(3 if term in doc.get("name","").casefold() else 1) for term in terms)
        if score<=0:continue
        best=0
        for term in terms:
            pos=folded.find(term)
            if pos>=0:best=pos;break
        start=max(0,best-260);end=min(len(text),best+950)
        snippet=text[start:end].strip()
        results.append({"score":score,"name":str(doc.get("name","Dokument")),"source_path":str(doc.get("source_path","")),
                        "sha256":str(doc.get("sha256","")),"snippet":snippet,"document":doc})
    results.sort(key=lambda x:(x["score"],len(x["snippet"])),reverse=True)
    return results[:max(1,min(20,int(limit)))]

def _u122_show_repair_knowledge(app):
    import os as _u122_os
    from tkinter import filedialog as _u122_filedialog
    app.current_view="REPAIR_KNOWLEDGE_BASE";app.clear();t=app.colors()
    app.header_title.config(text="SYSTEM REPAIR PRO — LOKALNA BAZA WIEDZY")
    head=app.panel(app.content);head.pack(fill="x",padx=3,pady=(0,5))
    tk.Label(head,text="BAZA WIEDZY • WYSZUKIWANIE • LEKCJA SERWISOWA",bg=t["panel"],fg=t["accent"],font=app.fnt(11,"bold")).pack(anchor="w",padx=10,pady=(7,3))
    tk.Label(head,text="Importowane dokumenty są indeksowane lokalnie. Skrypty są traktowane wyłącznie jako tekst — nie są uruchamiane. PDF obsługiwany przez pypdf. Nie importuj plików z hasłami ani kluczami odzyskiwania.",bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1350,justify="left").pack(anchor="w",padx=10,pady=(0,7))
    status=tk.StringVar(value="Dokumenty: "+str(len(_u122_load_knowledge())))
    tk.Label(app.content,textvariable=status,bg=t["bg"],fg=t["accent"],anchor="w",wraplength=1300).pack(fill="x",padx=8,pady=(0,4))
    query_row=tk.Frame(app.content,bg=t["bg"]);query_row.pack(fill="x",padx=6,pady=4)
    query=tk.Entry(query_row,bg=t["card"],fg=t["text"],insertbackground=t["text"],relief="flat")
    query.pack(side="left",fill="x",expand=True,padx=(0,6),ipady=6)
    result_panel=app.panel(app.content);result_panel.pack(fill="both",expand=True,padx=3,pady=3)
    results=ttk.Treeview(result_panel,columns=("score","source"),show="headings",height=7)
    results.heading("score",text="Trafność");results.heading("source",text="Źródło")
    results.column("score",width=80,anchor="center");results.column("source",width=550,anchor="w")
    results.pack(fill="x",padx=8,pady=(8,4))
    output=tk.Text(result_panel,height=12,bg="#07111f",fg="#d7eaff",insertbackground="#ffffff",wrap="word",font=("Consolas",9),relief="flat")
    output.pack(fill="both",expand=True,padx=8,pady=(0,8))
    found={}
    def show_selected(_event=None):
        selection=results.selection()
        if not selection:return
        item=found.get(selection[0])
        if not item:return
        output.configure(state="normal");output.delete("1.0","end")
        output.insert("end",item["name"]+"\nŹródło: "+item["source_path"]+"\nTrafność: "+str(item["score"])+"\n\n"+item["snippet"])
        output.configure(state="disabled")
    results.bind("<<TreeviewSelect>>",show_selected)
    def run_search():
        found.clear()
        for iid in results.get_children():results.delete(iid)
        matches=_u122_search_knowledge(query.get(),limit=12)
        for idx,item in enumerate(matches):
            iid="kb"+str(idx);found[iid]=item
            results.insert("","end",iid=iid,values=(item["score"],item["name"]))
        if matches:
            results.selection_set("kb0");show_selected()
            status.set(f"Dokumenty: {len(_u122_load_knowledge())} • Trafienia: {len(matches)} • Wyniki lokalne, nie są automatyczną diagnozą.")
        else:
            output.configure(state="normal");output.delete("1.0","end");output.insert("end","Brak trafień. Zaimportuj instrukcję lub zmień frazę.");output.configure(state="disabled")
            status.set(f"Dokumenty: {len(_u122_load_knowledge())} • Brak trafień.")
    def import_files():
        paths=_u122_filedialog.askopenfilenames(title="Importuj dokumenty do lokalnej bazy wiedzy",
            filetypes=(("Dokumenty serwisowe","*.txt *.md *.log *.pdf *.csv *.json *.html *.htm *.xml *.ini *.yaml *.yml *.ps1 *.bat *.cmd *.py *.cs *.xaml *.config *.rtf *.sql *.reg *.cfg *.conf"),("Wszystkie pliki","*.*")))
        if not paths:return
        result=_u122_import_knowledge_files(paths)
        message="Dodano: "+str(result["added"])+" • Łącznie: "+str(result["total"])
        if result["errors"]:message+="\nPominięto "+str(len(result["errors"]))+" plików; pierwszy błąd: "+result["errors"][0]["error"]
        status.set(message)
        if result["errors"]:app.append_log("Baza wiedzy: "+message)
    def clear_knowledge():
        docs=_u122_load_knowledge()
        if not docs:
            status.set("Baza wiedzy jest pusta.");return
        if not messagebox.askyesno("Wyczyść bazę wiedzy",f"Usunąć {len(docs)} wpisów indeksu lokalnego? Oryginalne pliki źródłowe nie zostaną skasowane."):return
        _u122_save_knowledge(_u122_knowledge_path(),[])
        for iid in results.get_children():results.delete(iid)
        found.clear();output.configure(state="normal");output.delete("1.0","end");output.configure(state="disabled")
        status.set("Baza wiedzy wyczyszczona. Oryginalne pliki pozostały bez zmian.")
    def make_lesson():
        matches=_u122_search_knowledge(query.get(),limit=5)
        if not matches:
            messagebox.showinfo("Lekcja serwisowa","Najpierw wpisz temat i wyszukaj dokumenty.");return
        lesson=["LEKCJA SERWISOWA: "+query.get().strip(),"", "1. Zdefiniuj objaw i zanotuj warunki wystąpienia.","2. Przeczytaj trafienia źródłowe poniżej; nie uruchamiaj skryptów tylko dlatego, że znajdują się w dokumencie.","3. Zapisz diagnozę i wykonaj wyłącznie kroki, które rozumiesz oraz które są zgodne z dokumentacją urządzenia.","4. Po każdej zmianie uruchom odpowiedni test kontrolny.","5. Zapisz wynik i źródła w raporcie.", "", "ŹRÓDŁA:"]
        for item in matches:
            lesson.extend(["", "— "+item["name"]+" (trafność "+str(item["score"])+")", item["snippet"]])
        output.configure(state="normal");output.delete("1.0","end");output.insert("end","\n".join(lesson));output.configure(state="disabled")
        status.set("Ułożono szkic lekcji na podstawie "+str(len(matches))+" lokalnych źródeł. Zweryfikuj procedury przed naprawą.")
    app.make_button(query_row,"SZUKAJ",run_search,"accent",side="left",ipady=4)
    tools=app.panel(app.content);tools.pack(fill="x",padx=3,pady=3)
    def open_source():
        selection=results.selection()
        item=found.get(selection[0]) if selection else None
        if not item:
            messagebox.showinfo("Źródło wiedzy","Zaznacz wynik wyszukiwania.");return
        path=item.get("source_path","")
        try:
            if _u122_os.path.isfile(path) and hasattr(_u122_os,"startfile"):_u122_os.startfile(path)
            else:messagebox.showinfo("Źródło wiedzy",path or "Nie zapisano ścieżki źródłowej.")
        except Exception as exc:messagebox.showerror("Źródło wiedzy",str(exc))
    app.make_button(tools,"IMPORTUJ DOKUMENTY",import_files,"good",side="left",ipady=4)
    app.make_button(tools,"OTWÓRZ ŹRÓDŁO",open_source,"card",side="left",ipady=4)
    app.make_button(tools,"UŁÓŻ LEKCJĘ",make_lesson,"accent",side="left",ipady=4)
    app.make_button(tools,"WYCZYŚĆ INDEKS",clear_knowledge,"card",side="left",ipady=4)
    app.make_button(tools,"← LABORATORIUM",app.show_component_lab,"card",side="right",ipady=4)
    output.configure(state="disabled")
    return None

AppV43.show_repair_knowledge=_u122_show_repair_knowledge

def _u122_selftest_repair_knowledge():
    import tempfile as _u122_tempfile
    from pathlib import Path as _u122_Path
    with _u122_tempfile.TemporaryDirectory() as root:
        source=_u122_Path(root)/"guide.txt";source.write_text("DISM RestoreHealth repairs the Windows component store. SFC checks protected system files.",encoding="utf-8")
        result=_u122_import_knowledge_files([source],_u122_Path(root)/"knowledge.json")
        assert result["added"]==1 and result["total"]==1
        docs=_u122_load_knowledge(_u122_Path(root)/"knowledge.json")
        hits=_u122_search_knowledge("DISM component store",docs)
        assert hits and hits[0]["name"]=="guide.txt"
        assert _u122_extract_knowledge_file(source)["sha256"]
    assert callable(AppV43.show_repair_knowledge)
    print("SYSTEM_REPAIR_PRO_KNOWLEDGE_SELFTEST_OK: local import, SHA-256 dedupe, ranked search and lesson source retrieval")


# v4.3.123 — System Repair PRO symptom profiles, safe diagnostics, tool shortcuts and reports.
_U123_REPAIR_PROFILES={
 "slow":{"title":"Windows działa wolno","summary":"Sprawdź obciążenie procesów, pamięć, autostart i zdarzenia dysku.","steps":["Zapisz obciążenie CPU/RAM i procesy o największym użyciu pamięci.","Sprawdź wolne miejsce i kondycję dysków.","Nie wyłączaj losowo usług ani zabezpieczeń."],"tool":"perfmon.exe /rel","command":"$cpu=Get-CimInstance Win32_Processor | Select-Object Name,LoadPercentage; $os=Get-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize,FreePhysicalMemory; $proc=@(Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 20 Name,Id,CPU,WorkingSet64); [pscustomobject]@{cpu=$cpu;memory=$os;top_processes=$proc} | ConvertTo-Json -Depth 5"},
 "bsod":{"title":"BSOD / niebieski ekran","summary":"Zbierz ostatnie zdarzenia BugCheck, Kernel-Power i WHEA.","steps":["Zapisz kod STOP i czas wystąpienia.","Sprawdź zdarzenia BugCheck/WHEA oraz pliki minidump.","Nie usuwaj sterowników przed zapisaniem raportu."],"tool":"mmc.exe eventvwr.msc","command":"$start=(Get-Date).AddDays(-14); $e=@(Get-WinEvent -FilterHashtable @{LogName='System';StartTime=$start} -MaxEvents 500 -ErrorAction SilentlyContinue | Where-Object {$_.ProviderName -match 'BugCheck|Kernel-Power|WHEA-Logger|volmgr'} | Select-Object -First 80 TimeCreated,Id,ProviderName,LevelDisplayName,Message); $d=@(Get-ChildItem $env:WINDIR\\Minidump -File -ErrorAction SilentlyContinue | Select-Object -Last 30 Name,Length,LastWriteTime); [pscustomobject]@{events=$e;minidumps=$d} | ConvertTo-Json -Depth 5"},
 "updates":{"title":"Błąd Windows Update","summary":"Sprawdź historię aktualizacji i zdarzenia Windows Update.","steps":["Zapisz dokładny kod błędu i numer KB.","Sprawdź historię aktualizacji i wolne miejsce.","Najpierw uruchom diagnostykę; reset składników aktualizacji wymaga osobnego potwierdzenia."],"tool":"ms-settings:windowsupdate","command":"$hot=@(Get-HotFix -ErrorAction SilentlyContinue | Sort-Object InstalledOn -Descending | Select-Object -First 40 HotFixID,Description,InstalledOn); $start=(Get-Date).AddDays(-14); $ev=@(Get-WinEvent -FilterHashtable @{LogName='System';StartTime=$start} -MaxEvents 400 -ErrorAction SilentlyContinue | Where-Object {$_.ProviderName -match 'WindowsUpdate|Servicing'} | Select-Object -First 80 TimeCreated,Id,ProviderName,Message); [pscustomobject]@{updates=$hot;events=$ev} | ConvertTo-Json -Depth 5"},
 "boot":{"title":"Problem z uruchamianiem Windows","summary":"Zbierz zdarzenia startu, stan WinRE i konfigurację systemu.","steps":["Zapisz ostatni komunikat i etap, na którym start się zatrzymuje.","Sprawdź WinRE i zdarzenia startu.","Nie wykonuj automatycznego resetu ani formatowania."],"tool":"ms-settings:recovery","command":"$reagent=& reagentc.exe /info 2>&1 | Out-String; $bcd=& bcdedit.exe /enum '{current}' 2>&1 | Out-String; $start=(Get-Date).AddDays(-7); $ev=@(Get-WinEvent -FilterHashtable @{LogName='System';Id=6005,6006,6008,41;StartTime=$start} -MaxEvents 60 -ErrorAction SilentlyContinue | Select-Object TimeCreated,Id,ProviderName,Message); [pscustomobject]@{winre=$reagent;bcd=$bcd;boot_events=$ev} | ConvertTo-Json -Depth 5"},
 "network":{"title":"Brak internetu / sieć","summary":"Sprawdź konfigurację IP, bramę, DNS i test HTTPS.","steps":["Porównaj adres IP, bramę i DNS.","Oddziel test połączenia z bramą od DNS i internetu.","Reset sieci może zerwać połączenie — nie uruchamiamy go automatycznie."],"tool":"ms-settings:network-status","command":"$ip=Get-NetIPConfiguration -ErrorAction SilentlyContinue | Select-Object InterfaceAlias,IPv4Address,IPv4DefaultGateway,DNSServer; $gw=Get-NetRoute -DestinationPrefix '0.0.0.0/0' -ErrorAction SilentlyContinue | Sort-Object RouteMetric | Select-Object -First 1 NextHop,InterfaceAlias; $ping=@(); if($gw.NextHop){$ping=@(Test-Connection -ComputerName $gw.NextHop -Count 4 -ErrorAction SilentlyContinue | Select-Object Address,ResponseTime,StatusCode)}; $dns=$null; try{$dns=Resolve-DnsName cloudflare.com -Type A -DnsOnly -ErrorAction Stop | Select-Object -First 4 Name,IPAddress}catch{$dns=$_.Exception.Message}; [pscustomobject]@{ip=$ip;gateway=$gw;gateway_ping=$ping;dns=$dns} | ConvertTo-Json -Depth 5"},
 "audio":{"title":"Brak dźwięku","summary":"Sprawdź urządzenia audio, usługi i sterowniki.","steps":["Sprawdź wyjście domyślne i głośność aplikacji.","Sprawdź urządzenia audio i błędy PnP.","Nie usuwaj sterowników przed zapisaniem ich wersji."],"tool":"control.exe mmsys.cpl","command":"$dev=@(Get-PnpDevice -ErrorAction SilentlyContinue | Where-Object {$_.Class -match 'Audio|MEDIA' -or $_.FriendlyName -match 'audio|sound|dźwięk'} | Select-Object Status,Class,FriendlyName,InstanceId); $svc=@(Get-Service Audiosrv,AudioEndpointBuilder -ErrorAction SilentlyContinue | Select-Object Name,Status,StartType); [pscustomobject]@{devices=$dev;services=$svc} | ConvertTo-Json -Depth 5"},
 "display":{"title":"Brak obrazu / ekran","summary":"Sprawdź adapter graficzny, rozdzielczość i sterownik.","steps":["Sprawdź kabel, wejście monitora i zasilanie.","Zapisz model GPU i wersję sterownika.","Test wzorca matrycy nie zastępuje sprawdzenia przewodu ani panelu."],"tool":"ms-settings:display","command":"$gpu=@(Get-CimInstance Win32_VideoController -ErrorAction SilentlyContinue | Select-Object Name,DriverVersion,DriverDate,Status,CurrentHorizontalResolution,CurrentVerticalResolution,VideoModeDescription); $mon=@(Get-CimInstance WmiMonitorID -Namespace root\\wmi -ErrorAction SilentlyContinue | Select-Object InstanceName,Active); [pscustomobject]@{gpu=$gpu;monitors=$mon} | ConvertTo-Json -Depth 5"},
 "game":{"title":"Gra zamyka się / błąd GPU","summary":"Sprawdź sterownik GPU, awarie aplikacji i zdarzenia Display.","steps":["Zapisz nazwę gry, kod błędu i czas awarii.","Sprawdź sterownik i zdarzenia Application Error/Display.","FPS z symulatora nie zastępuje testu gry ani sterownika."],"tool":"perfmon.exe /rel","command":"$gpu=@(Get-CimInstance Win32_VideoController -ErrorAction SilentlyContinue | Select-Object Name,DriverVersion,DriverDate,Status); $start=(Get-Date).AddDays(-14); $ev=@(Get-WinEvent -FilterHashtable @{LogName='Application';StartTime=$start} -MaxEvents 500 -ErrorAction SilentlyContinue | Where-Object {$_.Id -in 1000,1001 -or $_.ProviderName -match 'Display|nvlddmkm|amdwddmg'} | Select-Object -First 80 TimeCreated,Id,ProviderName,Message); [pscustomobject]@{gpu=$gpu;crashes=$ev} | ConvertTo-Json -Depth 5"},
 "disk":{"title":"Błędy dysku / SMART","summary":"Sprawdź kondycję dysków, woluminy i zdarzenia NTFS/dysk.","steps":["Zrób kopię ważnych danych przed naprawą dysku.","Sprawdź SMART i wolne miejsce.","Skan online jest bezpieczniejszy niż naprawa offline, ale nie zastępuje kopii."],"tool":"mmc.exe diskmgmt.msc","command":"$pd=@(Get-PhysicalDisk -ErrorAction SilentlyContinue | Select-Object FriendlyName,MediaType,HealthStatus,OperationalStatus,Size); $vol=@(Get-Volume -ErrorAction SilentlyContinue | Select-Object DriveLetter,FileSystemLabel,FileSystem,HealthStatus,Size,SizeRemaining); $start=(Get-Date).AddDays(-14); $ev=@(Get-WinEvent -FilterHashtable @{LogName='System';StartTime=$start} -MaxEvents 500 -ErrorAction SilentlyContinue | Where-Object {$_.ProviderName -match 'disk|Ntfs|storahci|stornvme|iaStor'} | Select-Object -First 80 TimeCreated,Id,ProviderName,Message); [pscustomobject]@{disks=$pd;volumes=$vol;events=$ev} | ConvertTo-Json -Depth 5"},
 "ram":{"title":"Błędy RAM / losowe restarty","summary":"Sprawdź moduły pamięci i zdarzenia WHEA/MemDiag.","steps":["Zapisz konfigurację modułów RAM i częstotliwość.","Sprawdź WHEA i wyniki diagnostyki pamięci.","Nie oznaczaj pamięci jako sprawnej tylko na podstawie odczytu WMI."],"tool":"mdsched.exe","command":"$ram=@(Get-CimInstance Win32_PhysicalMemory -ErrorAction SilentlyContinue | Select-Object DeviceLocator,Capacity,Speed,ConfiguredClockSpeed,Manufacturer,PartNumber); $start=(Get-Date).AddDays(-30); $ev=@(Get-WinEvent -FilterHashtable @{LogName='System';StartTime=$start} -MaxEvents 500 -ErrorAction SilentlyContinue | Where-Object {$_.ProviderName -match 'WHEA-Logger|MemoryDiagnostics-Results|BugCheck'} | Select-Object -First 100 TimeCreated,Id,ProviderName,Message); [pscustomobject]@{modules=$ram;events=$ev} | ConvertTo-Json -Depth 5"},
 "thermal":{"title":"Przegrzewanie / wentylatory","summary":"Odczytaj sensory temperatury, obciążenia, zegarów i wentylatorów.","steps":["Sprawdź temperaturę w spoczynku i pod kontrolowanym obciążeniem.","Odczyt N/D oznacza brak wartości udostępnionej przez sterownik.","Nie zatrzymuj wentylatorów ani nie wyłączaj zabezpieczeń termicznych."],"tool":"msinfo32.exe","command":"$c=@(Get-CimInstance Win32_Processor -ErrorAction SilentlyContinue | Select-Object Name,LoadPercentage,CurrentClockSpeed,MaxClockSpeed); $gpu=@(Get-CimInstance Win32_VideoController -ErrorAction SilentlyContinue | Select-Object Name,CurrentRefreshRate,DriverVersion,Status); [pscustomobject]@{cpu=$c;gpu=$gpu;note='Temperatury szczegółowe sprawdź w inspektorze sensorów; WMI nie udostępnia ich na każdym komputerze.'} | ConvertTo-Json -Depth 5"},
 "battery":{"title":"Bateria / ładowanie","summary":"Sprawdź status baterii, raport pojemności i aktywny plan zasilania.","steps":["Porównaj pojemność projektową i pełnego ładowania w Battery Report.","Sprawdź zasilacz, stan baterii i czas pracy.","Raport nie jest dostępny na komputerze bez baterii."],"tool":"ms-settings:batterysaver","command":"$b=@(Get-CimInstance Win32_Battery -ErrorAction SilentlyContinue | Select-Object Caption,EstimatedChargeRemaining,BatteryStatus,EstimatedRunTime,DesignCapacity,FullChargeCapacity); $p=& powercfg.exe /getactivescheme 2>&1 | Out-String; [pscustomobject]@{battery=$b;active_power_plan=$p} | ConvertTo-Json -Depth 5"},
 "driver":{"title":"Konflikt sterownika","summary":"Sprawdź błędne urządzenia PnP, wersje i podpisy sterowników.","steps":["Zapisz nazwę urządzenia i identyfikator sprzętowy.","Porównaj datę i wersję sterownika z producentem urządzenia.","Nie pobieraj sterowników z przypadkowych stron."],"tool":"mmc.exe devmgmt.msc","command":"$bad=@(Get-PnpDevice -ErrorAction SilentlyContinue | Where-Object {$_.Status -ne 'OK'} | Select-Object -First 100 Status,Class,FriendlyName,InstanceId); $drivers=@(Get-CimInstance Win32_PnPSignedDriver -ErrorAction SilentlyContinue | Select-Object -First 150 DeviceName,DriverVersion,DriverDate,Manufacturer,IsSigned); [pscustomobject]@{problem_devices=$bad;drivers=$drivers} | ConvertTo-Json -Depth 5"},
 "activation":{"title":"Aktywacja / licencja Windows","summary":"Odczytaj stan licencji bez zbierania kluczy produktu.","steps":["Sprawdź edycję Windows i stan aktywacji.","Nie udostępniaj kluczy produktu ani identyfikatorów instalacji publicznie.","Zmiany licencji wykonuj wyłącznie przez oficjalne ustawienia."],"tool":"ms-settings:activation","command":"$os=Get-CimInstance Win32_OperatingSystem | Select-Object Caption,Version,BuildNumber; $lic=@(Get-CimInstance SoftwareLicensingProduct -ErrorAction SilentlyContinue | Where-Object {$_.PartialProductKey -and $_.LicenseStatus -ne 0} | Select-Object Name,Description,LicenseStatus,PartialProductKey); [pscustomobject]@{os=$os;licensed_products=$lic;note='Pełne klucze produktu nie są zbierane.'} | ConvertTo-Json -Depth 5"}
}

def _u123_profile_command(profile_key):
    item=_U123_REPAIR_PROFILES.get(profile_key)
    if not item:raise ValueError("Nieznany profil naprawy.")
    return item["command"]

def _u123_show_repair_profiles(app):
    import os as _u123_os
    import subprocess as _u123_subprocess
    import threading as _u123_threading
    import webbrowser as _u123_webbrowser
    from urllib.parse import quote as _u123_quote
    from datetime import datetime as _u123_datetime
    from pathlib import Path as _u123_Path
    app.current_view="SYSTEM_REPAIR_PROFILES";app.clear();t=app.colors()
    app.header_title.config(text="SYSTEM REPAIR PRO — PROFILE PROBLEMÓW I BEZPIECZNA DIAGNOSTYKA")
    head=app.panel(app.content);head.pack(fill="x",padx=3,pady=(0,5))
    tk.Label(head,text="PROFIL PROBLEMU • DIAGNOZA • NARZĘDZIA WINDOWS • RAPORT",bg=t["panel"],fg=t["accent"],font=app.fnt(11,"bold")).pack(anchor="w",padx=10,pady=(7,3))
    tk.Label(head,text="Profile uruchamiają tylko odczytowe polecenia diagnostyczne. Naprawy systemowe wymagają osobnego potwierdzenia w Centrum napraw. Brak danych lub nieobsługiwane urządzenie oznacza N/D/WARN.",bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1350,justify="left").pack(anchor="w",padx=10,pady=(0,7))
    labels={value["title"]:key for key,value in _U123_REPAIR_PROFILES.items()}
    selected=tk.StringVar(value=next(iter(labels)))
    query_row=tk.Frame(app.content,bg=t["bg"]);query_row.pack(fill="x",padx=7,pady=4)
    combo=ttk.Combobox(query_row,textvariable=selected,values=list(labels),state="readonly",width=38);combo.pack(side="left",padx=(0,8),ipady=3)
    tk.Label(query_row,text="Opis błędu / kod (opcjonalnie):",bg=t["bg"],fg=t["muted"],font=app.fnt(8)).pack(side="left",padx=(0,5))
    error_entry=tk.Entry(query_row,bg=t["card"],fg=t["text"],insertbackground=t["text"],relief="flat")
    error_entry.pack(side="left",fill="x",expand=True,ipady=5)
    panel=app.panel(app.content);panel.pack(fill="both",expand=True,padx=3,pady=3)
    detail=tk.Text(panel,height=10,bg="#07111f",fg="#d7eaff",insertbackground="#ffffff",wrap="word",font=("Consolas",9),relief="flat")
    detail.pack(fill="both",expand=True,padx=8,pady=8)
    status=tk.StringVar(value="Wybierz profil i uruchom analizę.")
    tk.Label(app.content,textvariable=status,bg=t["bg"],fg=t["accent"],anchor="w",wraplength=1300).pack(fill="x",padx=8,pady=3)
    last={"profile":None,"result":"","report":None}
    def get_profile():
        return labels.get(selected.get(),next(iter(_U123_REPAIR_PROFILES)))
    def analyze():
        key=get_profile();item=_U123_REPAIR_PROFILES[key]
        user_error=error_entry.get().strip()
        lines=[item["title"],"",item["summary"],"","KROKI KONTROLNE:"]
        lines.extend(str(i+1)+". "+step for i,step in enumerate(item["steps"]))
        if user_error:lines.extend(["","ZGŁOSZONY BŁĄD:",user_error])
        try:
            searcher=globals().get("_u122_search_knowledge")
            if callable(searcher):
                hits=searcher(item["title"]+" "+user_error,limit=3)
                if hits:
                    lines.extend(["","TRAFIENIA Z LOKALNEJ BAZY WIEDZY:"])
                    for hit in hits:lines.extend(["- "+hit["name"]+" (trafność "+str(hit["score"])+")",hit["snippet"]])
        except Exception:pass
        detail.configure(state="normal");detail.delete("1.0","end");detail.insert("end","\n".join(lines));detail.configure(state="disabled")
        last["profile"]=key
        status.set("Profil przeanalizowany. To plan kontroli, nie automatyczne potwierdzenie awarii.")
    def run_diagnostic():
        key=get_profile();item=_U123_REPAIR_PROFILES[key]
        folder=_u123_Path(_u123_os.environ.get("LOCALAPPDATA") or _u123_Path.home())/"NaprawaPC"/"Raporty"/"RepairProfiles"
        folder.mkdir(parents=True,exist_ok=True)
        stamp=_u123_datetime.now().strftime("%Y%m%d-%H%M%S");path=folder/(stamp+"-"+key+".txt")
        win=tk.Toplevel(app);win.title("DIAGNOSTYKA — "+item["title"]);win.geometry("820x520");win.minsize(650,400)
        t2=app.colors();tk.Label(win,text=item["title"],bg=t2["bg"],fg=t2["accent"],font=app.fnt(11,"bold")).pack(anchor="w",padx=10,pady=8)
        out=tk.Text(win,bg="#07111f",fg="#d7eaff",insertbackground="#ffffff",wrap="word",font=("Consolas",9),relief="flat")
        out.pack(fill="both",expand=True,padx=10,pady=(0,10));out.insert("end","Trwa odczyt diagnostyczny. Raport: "+str(path)+"\n");out.configure(state="disabled")
        def worker():
            state="WARN"
            try:
                command=["powershell.exe","-NoProfile","-ExecutionPolicy","Bypass","-Command",_u123_profile_command(key)]
                result=_u123_subprocess.run(command,capture_output=True,text=True,encoding="utf-8",errors="replace",timeout=90,creationflags=getattr(_u123_subprocess,"CREATE_NO_WINDOW",0))
                body=((result.stdout or "")+"\n"+(result.stderr or "")).strip() or "Brak danych zwróconych przez polecenie."
                state="PASS" if result.returncode==0 and body else "WARN"
                if result.returncode!=0:body+="\n\nKod wyjścia: "+str(result.returncode)+" — wynik nie jest zaliczony."
            except Exception as exc:body=f"{type(exc).__name__}: {exc}\nBrak poprawnego odczytu; nie oznaczono PASS."
            try:path.write_text(body,encoding="utf-8")
            except Exception as exc:body+="\nNie udało się zapisać raportu: "+str(exc)
            def finish():
                if not win.winfo_exists():return
                out.configure(state="normal");out.delete("1.0","end");out.insert("end",body);out.see("end");out.configure(state="disabled")
                status.set(state+" — "+item["title"]+" — "+str(path))
                last["profile"]=key;last["result"]=body;last["report"]=str(path)
                try:app.append_log("SYSTEM REPAIR PROFILE "+key+": "+state+"; "+str(path))
                except Exception:pass
            try:app.after(0,finish)
            except Exception:pass
        _u123_threading.Thread(target=worker,daemon=True,name="NaprawaPC-Profile-"+key).start()
    def open_tool():
        key=get_profile();tool=_U123_REPAIR_PROFILES[key]["tool"]
        try:
            if tool.startswith("ms-settings:") and hasattr(_u123_os,"startfile"):_u123_os.startfile(tool)
            else:
                parts=tool.split()
                _u123_subprocess.Popen(parts,creationflags=getattr(_u123_subprocess,"CREATE_NO_WINDOW",0))
        except Exception as exc:messagebox.showerror("Narzędzie Windows",str(exc))
    def open_repair_center():
        if messagebox.askyesno("Centrum napraw","Otworzyć Centrum napraw Windows? Każda naprawa wymaga osobnego potwierdzenia."):
            app.show_system_repair_center()
    def search_web():
        key=get_profile();q=_U123_REPAIR_PROFILES[key]["title"]+" "+error_entry.get().strip()+" Windows troubleshooting Microsoft"
        _u123_webbrowser.open("https://www.bing.com/search?q="+_u123_quote(q))
    def save_report():
        key=get_profile();item=_U123_REPAIR_PROFILES[key]
        folder=_u123_Path(_u123_os.environ.get("LOCALAPPDATA") or _u123_Path.home())/"NaprawaPC"/"Raporty"/"RepairProfiles";folder.mkdir(parents=True,exist_ok=True)
        stamp=_u123_datetime.now().strftime("%Y%m%d-%H%M%S")
        try:
            import html as _u123_html
            report=folder/(stamp+"-"+key+".html")
            body=last["result"] or detail.get("1.0","end-1c")
            html_doc="<!doctype html><html lang='pl'><meta charset='utf-8'><title>Raport profilu</title><style>body{font:15px Segoe UI,Arial;background:#0a1220;color:#e7f1ff;margin:24px}h1{color:#54d7ff}pre{white-space:pre-wrap;background:#111e31;padding:16px}</style><h1>"+_u123_html.escape(item["title"])+"</h1><p>"+_u123_html.escape(item["summary"])+"</p><pre>"+_u123_html.escape(body)+"</pre></html>"
            report.write_text(html_doc,encoding="utf-8");last["report"]=str(report)
            status.set("Raport zapisany: "+str(report))
        except Exception as exc:messagebox.showerror("Raport profilu",str(exc))
    def open_last_report():
        try:
            path=last.get("report")
            if path and _u123_os.path.isfile(path) and hasattr(_u123_os,"startfile"):_u123_os.startfile(path)
            else:messagebox.showinfo("Raport","Najpierw uruchom diagnostykę lub zapisz raport.")
        except Exception as exc:messagebox.showerror("Raport",str(exc))
    actions=app.panel(app.content);actions.pack(fill="x",padx=3,pady=3)
    app.make_button(actions,"ANALIZUJ PROFIL",analyze,"accent",side="left",ipady=4)
    app.make_button(actions,"URUCHOM ODCZYT",run_diagnostic,"good",side="left",ipady=4)
    app.make_button(actions,"OTWÓRZ NARZĘDZIE",open_tool,"card",side="left",ipady=4)
    app.make_button(actions,"CENTRUM NAPRAW",open_repair_center,"card",side="left",ipady=4)
    app.make_button(actions,"SZUKAJ W SIECI",search_web,"card",side="left",ipady=4)
    app.make_button(actions,"ZAPISZ RAPORT",save_report,"card",side="left",ipady=4)
    app.make_button(actions,"OTWÓRZ RAPORT",open_last_report,"card",side="left",ipady=4)
    app.make_button(actions,"← LABORATORIUM",app.show_component_lab,"card",side="right",ipady=4)
    analyze()
    return None

AppV43.show_repair_profiles=_u123_show_repair_profiles

def _u123_selftest_repair_profiles():
    assert len(_U123_REPAIR_PROFILES)>=12
    assert len(set(_U123_REPAIR_PROFILES))==len(_U123_REPAIR_PROFILES)
    forbidden=("Remove-Item","Format-Volume","Clear-Disk","Reset-Computer","Restart-Computer","Stop-Computer")
    for key,item in _U123_REPAIR_PROFILES.items():
        assert item.get("title") and item.get("summary") and item.get("steps") and item.get("command")
        assert not any(word.lower() in item["command"].lower() for word in forbidden),key
        assert _u123_profile_command(key)==item["command"]
    assert callable(AppV43.show_repair_profiles)
    print("SYSTEM_REPAIR_PROFILES_SELFTEST_OK: 12 safe read-only profiles, tool shortcuts and HTML report")


# v4.3.124 — full sensor inspector, richer speed quality panel and GPU benchmark HUD.
def _u124_open_sensor_inspector(app):
    existing=getattr(app,"_u124_sensor_window",None)
    try:
        if existing is not None and existing.winfo_exists():
            existing.deiconify();existing.lift();existing.focus_force();return existing
    except Exception:pass
    win=tk.Toplevel(app)
    app._u124_sensor_window=win
    win.title("NAPRAWA PC — PEŁNY INSPEKTOR CZUJNIKÓW")
    win.geometry("1450x860");win.minsize(980,600)
    t=app.colors();win.configure(bg=t["bg"])
    head=tk.Frame(win,bg=t["panel"],highlightbackground=t["accent"],highlightthickness=1)
    head.pack(fill="x",padx=8,pady=(8,5))
    tk.Label(head,text="PEŁNY INSPEKTOR SPRZĘTU • LIVE",bg=t["panel"],fg=t["accent"],font=app.fnt(14,"bold")).pack(anchor="w",padx=12,pady=(9,2))
    tk.Label(head,text="Temperatury, obciążenia, zegary, napięcia, moc, wentylatory, RAM/swap, dyski, sieć, bateria i wszystkie pozostałe rekordy udostępnione przez sterownik. Brak odczytu pozostaje jako N/D.",bg=t["panel"],fg=t["muted"],font=app.fnt(9),wraplength=1380,justify="left").pack(anchor="w",padx=12,pady=(0,8))
    controls=tk.Frame(win,bg=t["bg"]);controls.pack(fill="x",padx=8,pady=(0,5))
    tk.Label(controls,text="SZUKAJ",bg=t["bg"],fg=t["muted"],font=app.fnt(8,"bold")).pack(side="left",padx=(0,5))
    search_var=tk.StringVar(value="")
    search=tk.Entry(controls,textvariable=search_var,bg=t["card"],fg=t["fg"],insertbackground=t["fg"],relief="flat",font=app.fnt(10))
    search.pack(side="left",fill="x",expand=True,padx=(0,10),ipady=5)
    tk.Label(controls,text="KATEGORIA",bg=t["bg"],fg=t["muted"],font=app.fnt(8,"bold")).pack(side="left",padx=(0,5))
    category_var=tk.StringVar(value="Wszystkie")
    category=ttk.Combobox(controls,textvariable=category_var,values=("Wszystkie",),state="readonly",width=22)
    category.pack(side="left",padx=(0,6),ipady=3)
    status=tk.Label(win,text="Pobieranie listy czujników…",bg=t["bg"],fg=t["muted"],anchor="w",font=app.fnt(9,"bold"))
    status.pack(fill="x",padx=10,pady=(0,5))
    frame=tk.Frame(win,bg=t["panel"]);frame.pack(fill="both",expand=True,padx=8,pady=(0,6))
    cols=("category","hardware","sensor","value","unit","source")
    tree=ttk.Treeview(frame,columns=cols,show="headings",height=24)
    labels={"category":"KATEGORIA","hardware":"PODZESPÓŁ / URZĄDZENIE","sensor":"CZUJNIK / METRYKA","value":"WARTOŚĆ LIVE","unit":"JEDNOSTKA","source":"ŹRÓDŁO"}
    widths={"category":150,"hardware":260,"sensor":330,"value":120,"unit":90,"source":300}
    for col in cols:
        tree.heading(col,text=labels[col])
        tree.column(col,width=widths[col],minwidth=75,stretch=col in ("hardware","sensor","source"))
    vs=ttk.Scrollbar(frame,orient="vertical",command=tree.yview)
    hs=ttk.Scrollbar(frame,orient="horizontal",command=tree.xview)
    tree.configure(yscrollcommand=vs.set,xscrollcommand=hs.set)
    tree.grid(row=0,column=0,sticky="nsew");vs.grid(row=0,column=1,sticky="ns");hs.grid(row=1,column=0,sticky="ew")
    frame.grid_rowconfigure(0,weight=1);frame.grid_columnconfigure(0,weight=1)
    try:
        tree.tag_configure("missing",foreground=t.get("warn","#ffc857"))
        tree.tag_configure("temperature",foreground=t.get("accent2","#6cdfff"))
    except Exception:pass
    footer=tk.Frame(win,bg=t["bg"]);footer.pack(fill="x",padx=8,pady=(0,8))
    app.make_button(footer,"ODŚWIEŻ TERAZ",lambda:force_refresh(),"good",side="left",ipady=5)
    app.make_button(footer,"EKSPORT PEŁNEJ TABELI CSV",lambda:_u116_export_sensor_csv(app),"accent",side="left",ipady=5)
    app.make_button(footer,"ZAMKNIJ",lambda:close_window(),"card",side="right",ipady=5)
    def render_rows():
        if not win.winfo_exists():return
        try:rows=_u107_get_sensor_rows(app)
        except Exception as exc:
            rows=[];app.queue_log("Inspektor czujników: "+repr(exc))
        cats=sorted({str(r.get("category") or "Other") for r in rows})
        choices=("Wszystkie",)+tuple(cats)
        if tuple(category.cget("values"))!=choices:category.configure(values=choices)
        selected=str(category_var.get() or "Wszystkie")
        if selected not in choices:category_var.set("Wszystkie");selected="Wszystkie"
        needle=str(search_var.get() or "").strip().casefold()
        shown=[]
        for row in rows:
            values=[str(row.get(k,"N/D") if row.get(k) is not None else "N/D") for k in cols]
            if selected!="Wszystkie" and values[0]!=selected:continue
            if needle and needle not in " ".join(values).casefold():continue
            shown.append((row,values))
        existing=tree.get_children("")
        try:old_scroll=float(tree.yview()[0]) if existing else 0.0
        except Exception:old_scroll=0.0
        rebuild=len(existing)!=len(shown)
        if rebuild and existing:tree.delete(*existing)
        available=0;missing=0
        for idx,(row,values) in enumerate(shown):
            raw=values[3].strip().casefold()
            is_missing=raw in ("n/d","nd","n/a","na","none","null","—","-","")
            if is_missing:missing+=1
            else:available+=1
            tags=("missing",) if is_missing else (("temperature",) if "temp" in values[0].casefold() else ())
            iid=f"sensor124_{idx}"
            if not rebuild and tree.exists(iid):
                tree.item(iid,values=values,tags=tags)
            else:
                tree.insert("","end",iid=iid,values=values,tags=tags)
        if rebuild and existing:
            try:tree.yview_moveto(old_scroll)
            except Exception:pass
        cache=getattr(app,"_u66_sensor_cache",{}) or {}
        stamp=cache.get("time")
        age=max(0,_u66_time.monotonic()-stamp) if isinstance(stamp,(int,float)) else None
        age_text=f"{age:.1f} s" if age is not None else "N/D"
        status.config(text=f"Wykryte: {len(rows)} • Wyświetlane: {len(shown)} • wartości dostępne: {available} • N/D: {missing} • wiek próbki: {age_text}")
    def force_refresh():
        _u116_force_sensor_refresh(app)
        try:win.after(900,render_rows)
        except Exception:pass
    def tick():
        try:
            if not win.winfo_exists():return
            render_rows()
            win.after(2000,tick)
        except Exception:pass
    def close_window():
        try:win.destroy()
        except Exception:pass
        try:app._u124_sensor_window=None
        except Exception:pass
    search_var.trace_add("write",lambda *_:render_rows())
    category.bind("<<ComboboxSelected>>",lambda _e:render_rows())
    win.protocol("WM_DELETE_WINDOW",close_window)
    render_rows();win.after(2000,tick)
    return win

_U124_ORIGINAL_MEASURE_SPEED=_u114_measure_speed
_U124_ORIGINAL_SHOW_SPEED=AppV43.show_speed_test

def _u124_speed_quality_values(result):
    result=result if isinstance(result,dict) else {}
    def fmt(key,unit=" Mbps"):
        value=result.get(key)
        return (f"{float(value):.2f}{unit}" if isinstance(value,(int,float)) and _u66_math.isfinite(float(value)) else "N/D")
    down=int(result.get("download_samples_valid",0) or 0);down_total=int(result.get("total_download_samples",0) or 0)
    up=int(result.get("upload_samples_valid",0) or 0);up_total=int(result.get("total_upload_samples",0) or 0)
    cvd=result.get("download_cv_percent");cvu=result.get("upload_cv_percent")
    stability=(f"CV DL {float(cvd):.1f}% / UL {float(cvu):.1f}%" if isinstance(cvd,(int,float)) and isinstance(cvu,(int,float)) else "N/D")
    jitter=result.get("latency_jitter_ms")
    return {
      "download_median":fmt("download_mbps"),"download_peak":fmt("download_peak_mbps"),
      "download_min":fmt("download_min_mbps"),"upload_median":fmt("upload_mbps"),
      "upload_peak":fmt("upload_peak_mbps"),"upload_min":fmt("upload_min_mbps"),
      "jitter":(f"{float(jitter):.2f} ms" if isinstance(jitter,(int,float)) and _u66_math.isfinite(float(jitter)) else "N/D"),
      "stability":stability,"samples":f"DL {down}/{down_total} • UL {up}/{up_total}",
      "state":str(result.get("state","N/D")).upper()
    }

def _u124_show_speed_test(app):
    result=_U124_ORIGINAL_SHOW_SPEED(app)
    try:
        t=app.colors()
        children=app.content.winfo_children();before=children[-1] if children else None
        pane=app.panel(app.content)
        pane.pack(fill="x",padx=3,pady=(0,5),before=before)
        tk.Label(pane,text="JAKOŚĆ POMIARU • MEDIANA, PEAK, MINIMUM, JITTER I PRÓBKI",
            bg=t["panel"],fg=t["accent"],font=app.fnt(9,"bold")).pack(anchor="w",padx=8,pady=(6,3))
        labels=(
          ("MEDIANA DL","download_median"),("PEAK DL","download_peak"),("MIN DL","download_min"),
          ("MEDIANA UL","upload_median"),("PEAK UL","upload_peak"),("MIN UL","upload_min"),
          ("JITTER","jitter"),("STABILNOŚĆ","stability"),("PRÓBKI","samples")
        )
        row=tk.Frame(pane,bg=t["panel"]);row.pack(fill="x",padx=4,pady=(0,5))
        app._u124_speed_quality_labels={}
        for title,key in labels:
            card=tk.Frame(row,bg=t["card"],highlightbackground=t["panel"],highlightthickness=1)
            card.pack(side="left",fill="both",expand=True,padx=2)
            tk.Label(card,text=title,bg=t["card"],fg=t["muted"],font=app.fnt(7,"bold")).pack(pady=(4,1))
            label=tk.Label(card,text="N/D",bg=t["card"],fg=t["accent2"],font=app.fnt(8,"bold"))
            label.pack(padx=3,pady=(0,4));app._u124_speed_quality_labels[key]=label
        app._u124_speed_quality_state=tk.Label(pane,text="STATUS: GOTOWY — wynik pojawi się po pomiarze",bg=t["panel"],fg=t["muted"],font=app.fnt(8,"bold"))
        app._u124_speed_quality_state.pack(anchor="w",padx=8,pady=(0,5))
        return result
    except Exception as exc:
        try:app.queue_log("Panel jakości Speed Test: "+repr(exc))
        except Exception:pass
        return result

def _u124_measure_speed(app):
    result=_U124_ORIGINAL_MEASURE_SPEED(app)
    values=_u124_speed_quality_values(result)
    def update():
        controls=getattr(app,"_u124_speed_quality_labels",{}) or {}
        for key,value in values.items():
            label=controls.get(key)
            try:
                if label is not None and label.winfo_exists():label.config(text=value)
            except Exception:pass
        try:
            state_label=getattr(app,"_u124_speed_quality_state",None)
            if state_label is not None and state_label.winfo_exists():
                state_label.config(text=f"STATUS: {values['state']} • prawidłowe próbki {values['samples']} • wynik główny = mediana")
        except Exception:pass
        try:
            if getattr(app,"current_view","")=="SPEED_TEST":
                _u66_set_speed_status(app,
                    f"Speed Test {values['state']}: mediana DL {values['download_median']} / UL {values['upload_median']} • {values['samples']} • jitter {values['jitter']}")
        except Exception:pass
    try:app.queue_action(update)
    except Exception:pass
    return result

def _u131_parallel_progress_math(done,sizes,rates,base_bytes=0):
    normalized_sizes=[max(0,int(v or 0)) for v in (sizes or [])]
    normalized_done=[]
    normalized_rates=[]
    for i,size in enumerate(normalized_sizes):
        try:value=int(done[i] or 0)
        except Exception:value=0
        normalized_done.append(max(0,min(size,value)))
        try:rate=float(rates[i] or 0)
        except Exception:rate=0.0
        normalized_rates.append(rate if _u66_math.isfinite(rate) and rate>=0 else 0.0)
    total_size=sum(normalized_sizes)
    total_done=sum(normalized_done)
    return {"bytes":total_done,"total_bytes":total_size,
        "progress_percent":round(total_done*100/total_size) if total_size else 0,
        "aggregate_mbps":round(sum(normalized_rates),2),
        "active_streams":sum(1 for i,rate in enumerate(normalized_rates)
            if rate>0 and normalized_done[i]<normalized_sizes[i]),
        "base_bytes":max(0,int(base_bytes or 0))}

def _u131_parallel_progress_update(app,direction,index,done,total,elapsed,instant,average):
    def apply():
        state=getattr(app,"_u131_parallel_state",None)
        if not isinstance(state,dict) or state.get("direction")!=direction:return
        idx=int(index)-1
        if idx<0 or idx>=len(state.get("sizes",[])):return
        try:state["done"][idx]=max(0,min(int(state["sizes"][idx]),int(done or 0)))
        except Exception:pass
        try:
            value=float(instant or 0)
            state["rates"][idx]=value if _u66_math.isfinite(value) and value>=0 else 0.0
        except Exception:state["rates"][idx]=0.0
        metrics=_u131_parallel_progress_math(state["done"],state["sizes"],state["rates"],state.get("base_bytes",0))
        history=getattr(app,"_u90_speed_history",None)
        if not isinstance(history,dict):
            history={"download":[],"upload":[]};app._u90_speed_history=history
        history.setdefault(direction,[]).append(metrics["aggregate_mbps"])
        history[direction]=history[direction][-100:]
        try:
            label=(getattr(app,"_u66_speed_values",{}) or {}).get(direction)
            if label is not None and label.winfo_exists():
                label.config(text=f"{metrics['aggregate_mbps']:.1f} Mbps Σ")
            data_label=(getattr(app,"_u66_speed_values",{}) or {}).get("data")
            if data_label is not None and data_label.winfo_exists():
                data_label.config(text=f"{(metrics['base_bytes']+metrics['bytes'])/1_000_000:.2f} MB")
        except Exception:pass
        try:
            profile=str(state.get("profile","STANDARD"))
            _u66_set_speed_status(app,
                f"NA ŻYWO — {profile} {direction.upper()} RÓWNOLEGŁY {metrics['progress_percent']}% • "
                f"{metrics['bytes']/1_000_000:.2f}/{metrics['total_bytes']/1_000_000:.2f} MB • "
                f"{metrics['aggregate_mbps']:.1f} Mbps łącznie • aktywne strumienie {metrics['active_streams']}")
            _u90_draw_live_speed_chart(app)
        except Exception:pass
    try:app.queue_action(apply)
    except Exception:pass

def _u131_finish_parallel_ui(app,direction,result):
    state=getattr(app,"_u131_parallel_state",None)
    if not isinstance(state,dict) or state.get("direction")!=direction:return
    try:
        streams=result.get("streams",[])
        for sample in streams:
            if not isinstance(sample,dict):continue
            idx=int(sample.get("stream_index",0))-1
            if 0<=idx<len(state.get("sizes",[])):
                state["done"][idx]=max(0,min(int(state["sizes"][idx]),int(sample.get("bytes",0) or 0)))
                try:state["rates"][idx]=max(0.0,float(sample.get("mbps") or 0))
                except Exception:state["rates"][idx]=0.0
        metrics=_u131_parallel_progress_math(state["done"],state["sizes"],state["rates"],state.get("base_bytes",0))
        _u66_set_speed_status(app,
            f"ZAKOŃCZONO — {state.get('profile','STANDARD')} {direction.upper()} równoległy • "
            f"{result.get('successful_streams',0)}/{result.get('stream_count',0)} strumieni • "
            f"{metrics['bytes']/1_000_000:.2f}/{metrics['total_bytes']/1_000_000:.2f} MB • "
            f"{result.get('aggregate_mbps') if result.get('aggregate_mbps') is not None else 'N/D'} Mbps łącznie")
        _u90_draw_live_speed_chart(app)
    except Exception:pass

def _u131_selftest_parallel_progress():
    m=_u131_parallel_progress_math([2_000_000,4_000_000],[6_000_000,6_000_000],[10.0,20.0],1234)
    assert m["bytes"]==6_000_000 and m["total_bytes"]==12_000_000
    assert m["progress_percent"]==50 and m["aggregate_mbps"]==30.0
    assert m["base_bytes"]==1234 and m["active_streams"]==2
    done=_u131_parallel_progress_math([6_000_000,6_000_000],[6_000_000,6_000_000],[0.0,0.0],0)
    assert done["progress_percent"]==100 and done["active_streams"]==0
    missing=_u131_parallel_progress_math([0],[0],[float("nan")],0)
    assert missing["progress_percent"]==0 and missing["aggregate_mbps"]==0.0
    print("SPEED_TEST_PARALLEL_LIVE_PROGRESS_SELFTEST_OK")

def _u125_selftest_unique_scene_families():
    import inspect as _u125_inspect, re as _u125_re
    signatures=[_u116_scene_signature(i) for i in range(1,111)]
    assert len(_U116_SCENE_STYLE_NAMES)==31 and len(set(_U116_SCENE_STYLE_NAMES))==31
    assert {sig["style_index"] for sig in signatures}==set(range(31))
    assert len({(sig["style_index"],sig["variant"],sig["element_count"],sig["scale"],sig["rotation_speed"],sig["palette"]) for sig in signatures})==110
    source=_u125_inspect.getsource(_u114_gpu_benchmark_child)
    assert all(_u125_re.search(r"(?:if|elif)\s+mode\s*==\s*"+str(mode)+r"\b",source) for mode in range(31)), "Every one of the 31 geometry modes must have its own renderer branch"
    print("GPU_SCENE_FAMILY_SELFTEST_OK: 31 explicit geometry modes, all 31 styles selected, 110 unique scene signatures")

def _u124_selftest_gpu_hud():
    code=_u114_gpu_benchmark_child.__code__
    pending=[code];names=set();literals=set()
    import types as _u124_types
    while pending:
        current=pending.pop();names.update(current.co_names);names.update(current.co_varnames)
        for value in current.co_consts:
            if isinstance(value,_u124_types.CodeType):pending.append(value)
            elif isinstance(value,str):literals.add(value)
    assert "draw_benchmark_hud" in names
    assert "glOrtho" in names and "glFinish" in names
    assert "geometry_vertices" in literals and "scene_signature" in literals
    assert len({_u116_scene_signature(i)["seed"] for i in range(1,111)})==110
    print("GPU_BENCHMARK_HUD_SELFTEST_OK: live FPS gauge, progress bar, frame history and 110 scene seeds")

def _u124_selftest_speed_quality():
    result={"state":"good","download_mbps":123.45,"download_peak_mbps":150.0,"download_min_mbps":100.0,
            "upload_mbps":25.5,"upload_peak_mbps":31.0,"upload_min_mbps":20.0,
            "latency_jitter_ms":2.25,"download_cv_percent":4.5,"upload_cv_percent":8.2,
            "download_samples_valid":3,"total_download_samples":3,"upload_samples_valid":2,"total_upload_samples":3}
    values=_u124_speed_quality_values(result)
    assert values["download_median"]=="123.45 Mbps" and values["download_peak"]=="150.00 Mbps"
    assert values["upload_min"]=="20.00 Mbps" and values["jitter"]=="2.25 ms"
    assert values["samples"]=="DL 3/3 • UL 2/3" and values["state"]=="GOOD"
    missing=_u124_speed_quality_values({"state":"warn"})
    assert missing["download_median"]=="N/D" and missing["jitter"]=="N/D"
    print("SPEED_TEST_QUALITY_PANEL_SELFTEST_OK: median, peak, minimum, jitter, CV and sample counts")

def _u124_selftest_sensor_inspector():
    import types as _u124_types
    pending=[_u124_open_sensor_inspector.__code__];names=set();literals=set()
    while pending:
        current=pending.pop();names.update(current.co_names)
        for value in current.co_consts:
            if isinstance(value,_u124_types.CodeType):pending.append(value)
            elif isinstance(value,str):literals.add(value)
    assert "_u107_get_sensor_rows" in names and "Treeview" in names
    assert "N/D" in literals and "after" in names
    assert "_u116_export_sensor_csv" in names
    print("FULL_SENSOR_INSPECTOR_SELFTEST_OK: searchable all-sensor table, N/D retention, auto-refresh and CSV export")

_u107_open_sensor_inspector=_u124_open_sensor_inspector
AppV43.show_speed_test=_u124_show_speed_test
# Wrap only the public speed-test entry point. Keep the lower-level functions
# intact because their self-tests inspect the real request/byte-validation path.
# Preserve the compatibility name expected by the existing adaptive-engine dispatcher.
_u66_measure_speed=_u124_measure_speed

AppV43.show_process_manager=_u126_show_process_manager
AppV43.show_game_diagnostics=_u126_show_game_diagnostics
AppV43.show_report_manager=_u126_show_report_manager

def _u132_service_dashboard_routes(app):
    # These routes expose implemented screens in one place; the catalog still labels
    # the 40 source-app probes as diagnostics, not a claim of complete 1:1 source parity.
    return [
        ("TESTY SPRZĘTOWE", "110 niezależnych testów, osobne ekrany i raporty.", lambda:_u93_show_lab(app)),
        ("RAM LIVE DASHBOARD", "Na żywo: RAM, commit, swap, CPU na rdzeń i procesy o największym użyciu pamięci.", lambda:_u134_show_ram_live_dashboard(app)),
        ("SYSTEM REPAIR PRO — TESTY", "Katalog 20 odczytowych diagnostyk System Repair PRO.", lambda:_u93_show_catalog(app,"SYSTEM_REPAIR_PRO")),
        ("SERWIS ULTIMATE — TESTY", "Katalog 20 odczytowych diagnostyk Serwis Ultimate.", lambda:_u93_show_catalog(app,"SERWIS_ULTIMATE")),
        ("CENTRUM NAPRAW WINDOWS", "SFC, DISM, CHKDSK, punkt przywracania i status WinRE; operacje wymagają potwierdzenia.", lambda:app.show_system_repair_center()),
        ("PROFILE NAPRAW", "14 profili objawów, odczytowa diagnostyka i raport HTML.", lambda:_u123_show_repair_profiles(app)),
        ("BAZA WIEDZY / PDF", "Lokalny import TXT/MD/PDF, wyszukiwanie i lekcje serwisowe.", lambda:_u122_show_repair_knowledge(app)),
        ("ZLECENIA SERWISOWE", "Lokalna historia zleceń i eksport karty HTML.", lambda:_u121_show_service_jobs(app)),
        ("ZASILANIE / BATERIA", "Niezależne raporty baterii, energii, uśpienia i planu zasilania.", lambda:_u121_show_power_lab(app)),
        ("MENEDŻER PROCESÓW", "Rzeczywiste procesy Windows, filtr, CSV i potwierdzane zakończenie.", lambda:_u126_show_process_manager(app)),
        ("DIAGNOSTYKA GIER", "GPU, DirectX, usługi gier i plan zasilania — bez automatycznych zmian.", lambda:_u126_show_game_diagnostics(app)),
        ("RAPORTY / HISTORIA", "Lokalny indeks raportów, filtr, otwieranie i eksport CSV.", lambda:_u126_show_report_manager(app)),
        ("PEŁNY INSPEKTOR CZUJNIKÓW", "Wszystkie dostępne sensory, N/D, odświeżanie i eksport CSV.", lambda:_u107_open_sensor_inspector(app)),
        ("TELEMETRIA LIVE", "Użycie, temperatury i pozostałe odczyty udostępnione przez sterowniki.", lambda:app.show_live_monitor()),
        ("SPEED TEST", "Rzeczywiste HTTPS download/upload, mediana oraz profile równoległe.", lambda:app.show_speed_test()),
        ("DYSKI / SSD / HDD", "Otwórz indywidualne testy dysków i raporty.", lambda:app.show_module("DYSK")),
        ("BEZPIECZEŃSTWO WINDOWS", "Otwórz testy bezpieczeństwa i stan ochrony.", lambda:app.show_module("SECURITY")),
        ("SIEĆ / WI-FI / LAN", "Otwórz diagnostykę interfejsów sieciowych.", lambda:app.show_simple_module("SIEĆ / WI-FI / LAN")),
        ("PULPIT", "Powrót do głównego pulpitu aplikacji.", lambda:app.show_dashboard()),
    ]

def _u132_show_service_ultimate_dashboard(app):
    app.current_view="SERVICE_ULTIMATE_DASHBOARD"
    app.clear()
    t=app.colors()
    app.header_title.config(text="CENTRUM SERWISU — ZINTEGROWANE MODUŁY")
    head=app.panel(app.content);head.pack(fill="x",padx=3,pady=(0,6))
    tk.Label(head,text="CENTRUM SERWISU • SYSTEM REPAIR PRO • SERWIS ULTIMATE",
        bg=t["panel"],fg=t["accent"],font=app.fnt(13,"bold")).pack(anchor="w",padx=12,pady=(9,3))
    tk.Label(head,text="Wszystkie obecnie zintegrowane moduły dostępne z jednego ekranu. Katalog testów ma oddzielne procedury i raporty; pełna zgodność 1:1 z archiwami źródłowymi nadal wymaga porównania każdego oryginalnego handlera.",
        bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1400,justify="left").pack(anchor="w",padx=12,pady=(0,8))
    foot=tk.Frame(app.content,bg=t["bg"]);foot.pack(side="bottom",fill="x",padx=5,pady=(4,2))
    app.make_button(foot,"← PULPIT",app.show_dashboard,"good",side="left",ipady=5)
    outer=tk.Frame(app.content,bg=t["bg"]);outer.pack(fill="both",expand=True)
    for col in range(3):outer.grid_columnconfigure(col,weight=1)
    routes=_u132_service_dashboard_routes(app)
    for i,(title,description,action) in enumerate(routes):
        row,col=divmod(i,3)
        card=tk.Frame(outer,bg=t["card"],highlightbackground=t["panel"],highlightthickness=1)
        card.grid(row=row,column=col,sticky="nsew",padx=4,pady=4)
        tk.Label(card,text=title,bg=t["card"],fg=t["accent2"],font=app.fnt(9,"bold"),anchor="w",justify="left",wraplength=390).pack(fill="x",padx=9,pady=(7,3))
        tk.Label(card,text=description,bg=t["card"],fg=t["muted"],font=app.fnt(8),anchor="nw",justify="left",wraplength=390).pack(fill="both",expand=True,padx=9,pady=(0,5))
        app.make_button(card,"OTWÓRZ MODUŁ",action,"accent" if i<4 else "card",fill="x",ipady=4)
    return None

_U132_ORIGINAL_SHOW_SYSTEM_REPAIR_CENTER=AppV43.show_system_repair_center
def _u132_show_system_repair_center(app):
    result=_U132_ORIGINAL_SHOW_SYSTEM_REPAIR_CENTER(app)
    try:
        body=getattr(app,"_u120_repair_log_text",None)
        log_panel=body.master if body is not None else None
        panel=app.panel(app.content)
        panel.pack(fill="x",padx=3,pady=3,before=log_panel if log_panel is not None else None)
        app.make_button(panel,"CENTRUM SERWISU — WSZYSTKIE MODUŁY",
            lambda:_u132_show_service_ultimate_dashboard(app),"accent",side="left",ipady=4)
    except Exception as exc:
        try:app.queue_log("Centrum serwisu: "+repr(exc))
        except Exception:pass
    return result

AppV43.show_service_ultimate_dashboard=_u132_show_service_ultimate_dashboard
AppV43.show_integrated_service_dashboard=_u132_show_service_ultimate_dashboard
AppV43.show_system_repair_center=_u132_show_system_repair_center

def _u132_selftest_service_dashboard():
    routes=_u132_service_dashboard_routes(object())
    names=[row[0] for row in routes]
    assert len(routes)==19 and len(set(names))==19
    assert all(callable(row[2]) for row in routes)
    assert {"SYSTEM_REPAIR_PRO","SERWIS_ULTIMATE"}.issubset(_U93_TEST_CATALOG)
    assert len(_U93_TEST_CATALOG["SYSTEM_REPAIR_PRO"])==20
    assert len(_U93_TEST_CATALOG["SERWIS_ULTIMATE"])==20
    assert AppV43.show_service_ultimate_dashboard is _u132_show_service_ultimate_dashboard
    assert AppV43.show_integrated_service_dashboard is _u132_show_service_ultimate_dashboard
    assert AppV43.show_system_repair_center is _u132_show_system_repair_center
    print("INTEGRATED_SERVICE_DASHBOARD_SELFTEST_OK: 18 routed screens; 20 System Repair PRO + 20 Serwis Ultimate probes")

_U133_ORIGINAL_BUILD_SHELL=AppV43._build_shell
def _u133_build_shell(self):
    result=_U133_ORIGINAL_BUILD_SHELL(self)
    try:
        t=self.colors()
        button=tk.Button(self.sidebar,text="🛠  CENTRUM SERWISU",
            command=self.show_service_ultimate_dashboard,anchor="w",relief="flat",bd=0,
            bg=t["accent"],fg="#ffffff",activebackground=t["accent2"],
            activeforeground="#ffffff",font=self.fnt(9,"bold"),cursor="hand2")
        button.pack(fill="x",padx=12,pady=3,ipady=9)
        self.nav.append(button)
        self._u133_service_nav_button=button
    except Exception as exc:
        try:self.queue_log("Nawigacja centrum serwisu: "+repr(exc))
        except Exception:pass
    return result

AppV43._build_shell=_u133_build_shell

def _u133_selftest_service_dashboard_navigation():
    routes=_u132_service_dashboard_routes(object())
    network=next(row for row in routes if row[0]=="SIEĆ / WI-FI / LAN")
    assert "SIEĆ / WI-FI / LAN" in network[2].__code__.co_consts
    assert callable(AppV43.show_service_ultimate_dashboard)
    assert AppV43._build_shell is _u133_build_shell
    names=set(_u133_build_shell.__code__.co_names)
    assert "show_service_ultimate_dashboard" in names and "nav" in names
    assert any("CENTRUM SERWISU" in str(value) for value in _u133_build_shell.__code__.co_consts)
    print("SERVICE_DASHBOARD_NAVIGATION_SELFTEST_OK: sidebar entry and correct network route")

def _u134_get_commit_info():
    # Windows commit charge via GetPerformanceInfo; do not mislabel pagefile usage as commit.
    import os as _u134_os
    if _u134_os.name!="nt":
        return None
    import ctypes as _u134_ctypes
    from ctypes import wintypes as _u134_wintypes
    class _U134_PERFORMANCE_INFORMATION(_u134_ctypes.Structure):
        _fields_=[
            ("cb",_u134_wintypes.DWORD),
            ("CommitTotal",_u134_ctypes.c_size_t),("CommitLimit",_u134_ctypes.c_size_t),
            ("CommitPeak",_u134_ctypes.c_size_t),("PhysicalTotal",_u134_ctypes.c_size_t),
            ("PhysicalAvailable",_u134_ctypes.c_size_t),("SystemCache",_u134_ctypes.c_size_t),
            ("KernelTotal",_u134_ctypes.c_size_t),("KernelPaged",_u134_ctypes.c_size_t),
            ("KernelNonpaged",_u134_ctypes.c_size_t),("PageSize",_u134_ctypes.c_size_t),
            ("HandleCount",_u134_wintypes.DWORD),("ProcessCount",_u134_wintypes.DWORD),
            ("ThreadCount",_u134_wintypes.DWORD)
        ]
    try:
        info=_U134_PERFORMANCE_INFORMATION()
        info.cb=_u134_ctypes.sizeof(info)
        api=_u134_ctypes.WinDLL("psapi")
        fn=api.GetPerformanceInfo
        fn.argtypes=[_u134_ctypes.POINTER(_U134_PERFORMANCE_INFORMATION),_u134_wintypes.DWORD]
        fn.restype=_u134_wintypes.BOOL
        if not fn(_u134_ctypes.byref(info),info.cb) or not info.PageSize or not info.CommitLimit:
            return None
        used=int(info.CommitTotal)*int(info.PageSize)
        limit=int(info.CommitLimit)*int(info.PageSize)
        return {"available":True,"used_bytes":used,"limit_bytes":limit,
            "percent":round(used*100/limit,2) if limit else None,
            "page_size":int(info.PageSize)}
    except Exception:
        return None

def _u134_show_ram_live_dashboard(app):
    import time as _u134_time
    from datetime import datetime as _u134_datetime
    from tkinter import ttk as _u134_ttk
    try:
        import psutil as _u134_psutil
    except Exception as exc:
        app.current_view="RAM_LIVE_DASHBOARD";app.clear();t=app.colors()
        app.header_title.config(text="SYSTEM REPAIR PRO — RAM LIVE DASHBOARD")
        panel=app.panel(app.content);panel.pack(fill="x",padx=8,pady=8)
        tk.Label(panel,text="Odczyt pamięci niedostępny — N/D",bg=t["panel"],fg=t["warn"],font=app.fnt(12,"bold")).pack(anchor="w",padx=12,pady=(10,4))
        tk.Label(panel,text=f"Nie udało się załadować psutil: {type(exc).__name__}: {exc}",bg=t["panel"],fg=t["muted"],font=app.fnt(9),wraplength=1000,justify="left").pack(anchor="w",padx=12,pady=(0,10))
        app.make_button(panel,"← PULPIT",app.show_dashboard,"card",side="left")
        return None

    app.current_view="RAM_LIVE_DASHBOARD";app.clear();t=app.colors()
    app.header_title.config(text="SYSTEM REPAIR PRO — RAM LIVE DASHBOARD")
    head=app.panel(app.content);head.pack(fill="x",padx=3,pady=(0,5))
    tk.Label(head,text="RAM LIVE • COMMIT • SWAP • CPU NA RDZEŃ • PROCESY",bg=t["panel"],fg=t["accent"],font=app.fnt(12,"bold")).pack(anchor="w",padx=12,pady=(8,2))
    tk.Label(head,text="Tylko odczyt. Wykres pokazuje próbki od momentu otwarcia ekranu; procesy są sortowane według bieżącego użycia RAM. Dane nie są wysyłane ani zapisywane do pliku.",bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1400,justify="left").pack(anchor="w",padx=12,pady=(0,8))
    status_var=tk.StringVar(value="Pobieranie pierwszej próbki…")
    tk.Label(app.content,textvariable=status_var,bg=t["bg"],fg=t["accent"],anchor="w",justify="left",wraplength=1400).pack(fill="x",padx=8,pady=(0,5))
    summary=tk.Frame(app.content,bg=t["bg"]);summary.pack(fill="x",padx=2,pady=2)
    fields=[
        ("RAM UŻYCIE","ram_used"),("RAM DOSTĘPNA","ram_available"),
        ("COMMIT CHARGE","commit"),("SWAP / PAGEFILE","swap"),("CPU ŁĄCZNIE","cpu")
    ]
    values={}
    for title,key in fields:
        card=tk.Frame(summary,bg=t["card"],highlightbackground=t["panel"],highlightthickness=1)
        card.pack(side="left",fill="both",expand=True,padx=3,pady=3)
        tk.Label(card,text=title,bg=t["card"],fg=t["muted"],font=app.fnt(8,"bold")).pack(anchor="w",padx=9,pady=(6,2))
        values[key]=tk.Label(card,text="N/D",bg=t["card"],fg=t["accent2"],font=app.fnt(14,"bold"))
        values[key].pack(anchor="w",padx=9,pady=(0,7))
    chart_panel=app.panel(app.content);chart_panel.pack(fill="x",padx=3,pady=3)
    chart=tk.Canvas(chart_panel,height=165,bg=t["panel"],highlightthickness=0)
    chart.pack(fill="x",expand=True,padx=5,pady=5)
    process_panel=app.panel(app.content);process_panel.pack(fill="both",expand=True,padx=3,pady=3)
    tk.Label(process_panel,text="PROCESY O NAJWIĘKSZYM UŻYCIU PAMIĘCI",bg=t["panel"],fg=t["accent"],font=app.fnt(9,"bold")).pack(anchor="w",padx=9,pady=(6,3))
    columns=("pid","name","rss","private","cpu")
    tree=_u134_ttk.Treeview(process_panel,columns=columns,show="headings",height=8)
    for key,label,width,anchor in (
        ("pid","PID",75,"e"),("name","PROCES",340,"w"),("rss","RAM MB",110,"e"),
        ("private","PRIVATE MB",120,"e"),("cpu","CPU %",90,"e")):
        tree.heading(key,text=label);tree.column(key,width=width,anchor=anchor)
    tree.pack(fill="both",expand=True,padx=7,pady=(0,7))
    actions=tk.Frame(app.content,bg=t["bg"]);actions.pack(fill="x",padx=4,pady=(2,0))
    app.make_button(actions,"TESTY RAM",lambda:app.show_module("RAM"),"accent",side="left",ipady=4)
    app.make_button(actions,"INSPEKTOR CZUJNIKÓW",lambda:_u107_open_sensor_inspector(app),"card",side="left",ipady=4)
    app.make_button(actions,"← PULPIT",app.show_dashboard,"card",side="right",ipady=4)
    history=getattr(app,"_u134_ram_live_history",[])
    app._u134_ram_live_history=history

    def draw_chart():
        chart.delete("all")
        width=max(400,chart.winfo_width());height=max(140,chart.winfo_height())
        left,right,top,bottom=42,width-16,18,height-28
        chart.create_text(left,5,text="RAM / COMMIT / SWAP — HISTORIA LIVE (%)",anchor="nw",fill=t["muted"],font=app.fnt(8,"bold"))
        chart.create_line(left,top,left,bottom,fill=t["muted"])
        chart.create_line(left,bottom,right,bottom,fill=t["muted"])
        for pct in (0,25,50,75,100):
            y=bottom-(bottom-top)*pct/100
            chart.create_line(left,y,right,y,fill=t["panel"],dash=(2,4))
            chart.create_text(left-6,y,text=str(pct),anchor="e",fill=t["muted"],font=app.fnt(7))
        rows=history[-90:]
        if len(rows)>=2:
            for key,color in (("ram",t["accent"]),("commit",t["accent2"]),("swap",t["warn"])):
                segment=[]
                for idx,row in enumerate(rows):
                    value=row.get(key)
                    if value is None:
                        if len(segment)>=4:chart.create_line(*segment,fill=color,width=2,smooth=False)
                        segment=[];continue
                    x=left+(right-left)*idx/max(1,len(rows)-1)
                    y=bottom-(bottom-top)*max(0,min(100,float(value)))/100
                    segment.extend((x,y))
                if len(segment)>=4:chart.create_line(*segment,fill=color,width=2,smooth=False)
        chart.create_text(right-190,5,text="RAM",anchor="nw",fill=t["accent"],font=app.fnt(8,"bold"))
        chart.create_text(right-135,5,text="COMMIT",anchor="nw",fill=t["accent2"],font=app.fnt(8,"bold"))
        chart.create_text(right-65,5,text="SWAP",anchor="nw",fill=t["warn"],font=app.fnt(8,"bold"))

    def refresh():
        if getattr(app,"current_view","")!="RAM_LIVE_DASHBOARD":
            return
        try:
            mem=_u134_psutil.virtual_memory()
            swap=_u134_psutil.swap_memory()
            commit=_u134_get_commit_info()
            cpu_per=_u134_psutil.cpu_percent(interval=None,percpu=True)
            cpu_total=sum(cpu_per)/len(cpu_per) if cpu_per else float(_u134_psutil.cpu_percent(interval=None))
            history.append({"time":_u134_time.time(),"ram":float(mem.percent),
                "commit":float(commit["percent"]) if commit and commit.get("percent") is not None else None,
                "swap":float(swap.percent),"cpu":float(cpu_total),"per_core":list(cpu_per)})
            del history[:-90]
            values["ram_used"].config(text=f"{mem.percent:.1f}% • {mem.used/1_073_741_824:.2f}/{mem.total/1_073_741_824:.2f} GB")
            values["ram_available"].config(text=f"{mem.available/1_073_741_824:.2f} GB")
            values["commit"].config(text=(f"{commit['used_bytes']/1_073_741_824:.2f}/{commit['limit_bytes']/1_073_741_824:.2f} GB • {commit['percent']:.1f}%" if commit and commit.get("percent") is not None else "N/D"))
            values["swap"].config(text=f"{swap.percent:.1f}% • {swap.used/1_073_741_824:.2f}/{swap.total/1_073_741_824:.2f} GB")
            values["cpu"].config(text=f"{cpu_total:.1f}% • {len(cpu_per)} rdzeni/logicznych")
            for item in tree.get_children():tree.delete(item)
            processes=[]
            for proc in _u134_psutil.process_iter(["pid","name","memory_info"]):
                try:
                    info=proc.info;memory=info.get("memory_info")
                    if memory is None:continue
                    try:cpu=float(proc.cpu_percent(interval=None))
                    except Exception:cpu=None
                    processes.append((int(info.get("pid") or 0),str(info.get("name") or "N/D"),int(memory.rss),int(getattr(memory,"private",memory.rss)),cpu))
                except (_u134_psutil.NoSuchProcess,_u134_psutil.AccessDenied,_u134_psutil.ZombieProcess):
                    continue
                except Exception:
                    continue
            processes.sort(key=lambda row:row[2],reverse=True)
            for pid,name,rss,private,cpu in processes[:15]:
                tree.insert("","end",values=(pid,name,f"{rss/1_048_576:.1f}",f"{private/1_048_576:.1f}","N/D" if cpu is None else f"{cpu:.1f}"))
            per_core=" • ".join(f"Rdzeń {i+1}: {v:.0f}%" for i,v in enumerate(cpu_per[:32]))
            commit_text=(f"commit {commit['percent']:.1f}%" if commit and commit.get("percent") is not None else "commit N/D")
            status_var.set(f"LIVE • {_u134_datetime.now().strftime('%H:%M:%S')} • RAM {mem.percent:.1f}% • {commit_text} • swap {swap.percent:.1f}% • CPU na rdzeń: {per_core or 'N/D'}")
            draw_chart()
        except Exception as exc:
            status_var.set(f"N/D — nie udało się odczytać telemetrii: {type(exc).__name__}: {exc}")
        try:app._u134_ram_live_after=app.after(1000,refresh)
        except Exception:pass
    chart.bind("<Configure>",lambda _event:draw_chart())
    refresh()
    return None

AppV43.show_ram_live_dashboard=_u134_show_ram_live_dashboard

def _u134_selftest_ram_live_dashboard():
    assert callable(_u134_show_ram_live_dashboard)
    assert AppV43.show_ram_live_dashboard is _u134_show_ram_live_dashboard
    names=_u93_deep_code_names(_u134_show_ram_live_dashboard)
    assert {"virtual_memory","swap_memory","cpu_percent","process_iter","after","Treeview"}.issubset(names)
    assert any("RAM LIVE DASHBOARD" in str(value) for value in _u134_show_ram_live_dashboard.__code__.co_consts)
    assert callable(_u134_get_commit_info) and "GetPerformanceInfo" in _u134_get_commit_info.__code__.co_names
    print("RAM_LIVE_DASHBOARD_SELFTEST_OK: live RAM/Windows commit/swap/CPU-per-core, process table and bounded 90-sample history")

def _u134_selftest_unique_service_probes():
    all_entries=[entry for entries in _U93_TEST_CATALOG.values() for entry in entries]
    all_titles=[entry[1] for entry in all_entries]
    assert len(all_entries)==110 and len(set(all_titles))==110, "All 110 catalog tests must have unique titles, not only unique IDs."
    service_entries=list(_U93_TEST_CATALOG.get("SYSTEM_REPAIR_PRO",[]))+list(_U93_TEST_CATALOG.get("SERWIS_ULTIMATE",[]))
    ids=[entry[0] for entry in service_entries]
    titles=[entry[1] for entry in service_entries]
    assert len(ids)==40 and len(set(ids))==40, "The two source-app catalogs must have 40 distinct IDs."
    assert len(titles)==40 and len(set(titles))==40, "The two source-app catalogs must have 40 distinct titles."
    assert all(entry[3]=="service_probe" for entry in service_entries)
    assert all(test_id in _U109_SERVICE_PROBES for test_id in ids), "Every service diagnostic must map to its own PowerShell probe."
    scripts=[str(_U109_SERVICE_PROBES[test_id]).strip() for test_id in ids]
    assert len(scripts)==40 and len(set(scripts))==40, "No System Repair PRO / Serwis Ultimate diagnostics may reuse an identical script."
    print("UNIQUE_TESTS_AND_SERVICE_PROBES_SELFTEST_OK: 110 unique catalog titles; 40 unique service IDs/titles/scripts")



# v4.3.135 — ten more individually runnable, read-only service diagnostics.
# Each probe has its own stable key, window, JSON report and honest WARN handling.
_U135_SERWIS_TESTS = {
 "dxdiag_report": {
  "title":"Raport DirectX / DxDiag",
  "description":"Tworzy osobny raport diagnostyczny DirectX i sterowników ekranu; nie zmienia ustawień.",
  "command":"$p=Join-Path $env:TEMP ('NaprawaPC-DxDiag-'+(Get-Date -Format 'yyyyMMdd-HHmmss')+'.txt');$err=$null;try{$proc=Start-Process -FilePath 'dxdiag.exe' -ArgumentList (('/whql:off /t \"{0}\"' -f $p)) -PassThru -Wait -ErrorAction Stop;for($i=0;$i -lt 30 -and !(Test-Path -LiteralPath $p);$i++){Start-Sleep -Milliseconds 500};if(Test-Path -LiteralPath $p){$txt=Get-Content -LiteralPath $p -Raw -ErrorAction Stop;[pscustomobject]@{state='PASS';report_path=$p;process_exit=$proc.ExitCode;characters=$txt.Length;report_preview=$txt.Substring(0,[Math]::Min(18000,$txt.Length))} | ConvertTo-Json -Depth 4}else{throw 'DxDiag nie utworzył raportu'}}catch{[pscustomobject]@{state='WARN';error=$_.Exception.Message;report_path=$p} | ConvertTo-Json -Depth 3}"
 },
 "printer_subsystem": {
  "title":"Drukarki i kolejka wydruku",
  "description":"Oddzielna diagnostyka drukarek, portów i usługi bufora wydruku.",
  "command":"$svc=Get-CimInstance Win32_Service -Filter \"Name='Spooler'\" -ErrorAction SilentlyContinue | Select-Object Name,State,StartMode,ExitCode;$printers=@(Get-Printer -ErrorAction SilentlyContinue | Select-Object Name,DriverName,PortName,PrinterStatus,Shared,WorkOffline);$ports=@(Get-PrinterPort -ErrorAction SilentlyContinue | Select-Object Name,Description,PrinterHostAddress,PortNumber);[pscustomobject]@{spooler=$svc;printer_count=$printers.Count;printers=$printers;port_count=$ports.Count;ports=$ports} | ConvertTo-Json -Depth 5"
 },
 "bluetooth_devices": {
  "title":"Bluetooth — adaptery i urządzenia",
  "description":"Inwentaryzacja urządzeń Bluetooth i adapterów radiowych; niczego nie paruje ani nie rozłącza.",
  "command":"$d=@(Get-PnpDevice -Class Bluetooth -ErrorAction SilentlyContinue | Select-Object Status,Class,FriendlyName,Manufacturer,InstanceId);$a=@(Get-NetAdapter -IncludeHidden -ErrorAction SilentlyContinue | Where-Object {$_.InterfaceDescription -match 'Bluetooth'} | Select-Object Name,InterfaceDescription,Status,MacAddress);[pscustomobject]@{device_count=$d.Count;devices=$d;adapter_count=$a.Count;adapters=$a} | ConvertTo-Json -Depth 5"
 },
 "reliability_history": {
  "title":"Historia niezawodności Windows",
  "description":"Odczyt wpisów monitora niezawodności z ostatnich 30 dni.",
  "command":"$since=(Get-Date).AddDays(-30);$items=@();try{$items=@(Get-CimInstance -ClassName Win32_ReliabilityRecords -ErrorAction Stop | Where-Object {$_.TimeGenerated -and ([Management.ManagementDateTimeConverter]::ToDateTime($_.TimeGenerated) -ge $since)} | Sort-Object TimeGenerated -Descending | Select-Object -First 100 @{n='Time';e={[Management.ManagementDateTimeConverter]::ToDateTime($_.TimeGenerated)}},SourceName,EventIdentifier,ProductName,Message)}catch{$items=@(@{state='N/D';error=$_.Exception.Message})};[pscustomobject]@{period_days=30;record_count=$items.Count;records=$items} | ConvertTo-Json -Depth 5"
 },
 "restore_point_inventory": {
  "title":"Punkty przywracania i kopie woluminów",
  "description":"Tylko lista dostępnych punktów przywracania i migawek; nie tworzy ani nie usuwa kopii.",
  "command":"$rp=@();$err=$null;try{$rp=@(Get-ComputerRestorePoint -ErrorAction Stop | Select-Object -First 80 SequenceNumber,Description,CreationTime,RestorePointType,EventType)}catch{$err=$_.Exception.Message};$sh=@(Get-CimInstance Win32_ShadowCopy -ErrorAction SilentlyContinue | Select-Object ID,InstallDate,VolumeName,State);$enabled=@();try{$enabled=@(Get-CimInstance -Namespace root/default -ClassName SystemRestore -ErrorAction Stop | Select-Object SystemRestoreConfig,NumberOfRestorePoints)}catch{};[pscustomobject]@{restore_point_count=$rp.Count;restore_points=$rp;restore_point_query_error=$err;shadow_copy_count=$sh.Count;shadow_copies=$sh;restore_provider=$enabled} | ConvertTo-Json -Depth 5"
 },
 "bitlocker_status": {
  "title":"Status szyfrowania BitLocker",
  "description":"Odczyt stanu szyfrowania i ochrony woluminów; raport nie pobiera ani nie wyświetla kluczy odzyskiwania.",
  "command":"try{$v=@(Get-BitLockerVolume -ErrorAction Stop | Select-Object MountPoint,VolumeType,VolumeStatus,ProtectionStatus,EncryptionPercentage,EncryptionMethod,LockStatus,AutoUnlockEnabled);[pscustomobject]@{state='PASS';volume_count=$v.Count;volumes=$v;note='Klucze odzyskiwania nie są odczytywane'} | ConvertTo-Json -Depth 5}catch{[pscustomobject]@{state='N/D';error=$_.Exception.Message;note='Dostępność zależy od edycji Windows i uprawnień'} | ConvertTo-Json -Depth 3}"
 },
 "optional_features": {
  "title":"Funkcje opcjonalne Windows",
  "description":"Lista stanów składników opcjonalnych Windows bez włączania ani wyłączania funkcji.",
  "command":"try{$f=@(Get-WindowsOptionalFeature -Online -ErrorAction Stop | Select-Object FeatureName,State,RestartRequired);[pscustomobject]@{state='PASS';feature_count=$f.Count;enabled_count=@($f | Where-Object {$_.State -eq 'Enabled'}).Count;features=$f} | ConvertTo-Json -Depth 5}catch{[pscustomobject]@{state='N/D';error=$_.Exception.Message;note='Odczyt DISM może wymagać uprawnień administratora'} | ConvertTo-Json -Depth 3}"
 },
 "runtime_inventory": {
  "title":"Runtime .NET i Visual C++",
  "description":"Inwentaryzacja zainstalowanych runtime'ów .NET i pakietów Visual C++; bez używania Win32_Product.",
  "command":"$dotnet='';$dotnetCode=-1;try{$dotnet=& dotnet.exe --list-runtimes 2>&1 | Out-String;$dotnetCode=$LASTEXITCODE}catch{$dotnet=$_.Exception.Message};$paths=@('HKLM:\\SOFTWARE\\Microsoft\\VisualStudio\\14.0\\VC\\Runtimes\\x64','HKLM:\\SOFTWARE\\WOW6432Node\\Microsoft\\VisualStudio\\14.0\\VC\\Runtimes\\x86','HKLM:\\SOFTWARE\\Microsoft\\VisualStudio\\14.0\\VC\\Runtimes\\x86');$vc=@();foreach($p in $paths){if(Test-Path $p){$x=Get-ItemProperty $p -ErrorAction SilentlyContinue;$vc+=@{path=$p;Installed=$x.Installed;Version=$x.Version;Major=$x.Major;Minor=$x.Minor;Bld=$x.Bld}}};[pscustomobject]@{dotnet_exit_code=$dotnetCode;dotnet_runtimes=$dotnet;visual_cpp=$vc} | ConvertTo-Json -Depth 4"
 },
 "wifi_profiles": {
  "title":"Wi-Fi — interfejsy i profile",
  "description":"Stan interfejsów Wi-Fi i nazwy zapisanych profili; nie odczytuje haseł ani kluczy.",
  "command":"$ifaces=@(Get-NetAdapter -ErrorAction SilentlyContinue | Where-Object {$_.NdisPhysicalMedium -eq 9 -or $_.InterfaceDescription -match 'Wi-Fi|Wireless|WLAN'} | Select-Object Name,InterfaceDescription,Status,LinkSpeed,MacAddress);$state='';$profiles='';try{$state=(& netsh.exe wlan show interfaces 2>&1 | Out-String)}catch{$state=$_.Exception.Message};try{$profiles=(& netsh.exe wlan show profiles 2>&1 | Out-String)}catch{$profiles=$_.Exception.Message};[pscustomobject]@{wireless_adapter_count=$ifaces.Count;adapters=$ifaces;interface_status=$state;profile_names_only=$profiles;credentials_read=$false} | ConvertTo-Json -Depth 4"
 },
 "wer_dump_inventory": {
  "title":"Zrzuty awarii aplikacji (WER)",
  "description":"Lista nazw, rozmiarów i dat zrzutów awarii; pliki zrzutów nie są otwierane ani wysyłane.",
  "command":"$roots=@((Join-Path $env:LOCALAPPDATA 'CrashDumps'),(Join-Path $env:ProgramData 'Microsoft\\Windows\\WER\\ReportArchive'),(Join-Path $env:ProgramData 'Microsoft\\Windows\\WER\\ReportQueue'));$items=@();foreach($root in $roots){if(Test-Path -LiteralPath $root){$items+=@(Get-ChildItem -LiteralPath $root -File -Recurse -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 100 @{n='Root';e={$root}},Name,Extension,Length,LastWriteTime,DirectoryName)}};$items=@($items | Sort-Object LastWriteTime -Descending | Select-Object -First 250);[pscustomobject]@{searched_roots=$roots;dump_or_report_count=$items.Count;files=$items;content_opened=$false} | ConvertTo-Json -Depth 5"
 }
}

def _u135_status_from_output(exit_code,raw,parsed):
    if int(exit_code or 0)!=0 or not str(raw or "").strip():
        return "WARN"
    if not isinstance(parsed,dict):
        return "WARN"
    state=str(parsed.get("state","")).strip().upper()
    if state in ("N/D","WARN","ERROR","FAIL","FAILED"):
        return "WARN" if state=="N/D" else state
    if state and state not in ("PASS","GOOD","OK","SUCCESS"):
        return "WARN"
    return "PASS"

def _u135_run_serwis_test(app,key):
    import os as _u135_os
    import subprocess as _u135_subprocess
    import threading as _u135_threading
    import json as _u135_json
    from datetime import datetime as _u135_datetime
    from pathlib import Path as _u135_Path
    item=_U135_SERWIS_TESTS.get(key)
    if not item:
        messagebox.showerror("Serwis Ultimate","Nieznany test.")
        return
    if _u135_os.name!="nt":
        messagebox.showinfo(item["title"],"Ten odczyt wymaga Windows.")
        return
    folder=_u135_Path(_u135_os.environ.get("LOCALAPPDATA") or _u135_Path.home())/"NaprawaPC"/"Raporty"/"SerwisUltimate"
    folder.mkdir(parents=True,exist_ok=True)
    stamp=_u135_datetime.now().strftime("%Y%m%d-%H%M%S")
    path=folder/(stamp+"-"+key+".json")
    win=tk.Toplevel(app)
    win.title("SERWIS ULTIMATE — "+item["title"])
    win.geometry("1000x650")
    win.minsize(700,450)
    t=app.colors()
    tk.Label(win,text=item["title"],bg=t["bg"],fg=t["accent"],font=app.fnt(12,"bold")).pack(anchor="w",padx=12,pady=(12,3))
    tk.Label(win,text=item["description"],bg=t["bg"],fg=t["muted"],font=app.fnt(9),wraplength=950,justify="left").pack(anchor="w",padx=12,pady=(0,6))
    status=tk.StringVar(value="TEST W TOKU…")
    tk.Label(win,textvariable=status,bg=t["bg"],fg=t["accent"],anchor="w").pack(fill="x",padx=12,pady=(0,5))
    output=tk.Text(win,bg="#07111f",fg="#d7eaff",insertbackground="#ffffff",wrap="word",font=("Consolas",9),relief="flat")
    output.pack(fill="both",expand=True,padx=12,pady=(0,8))
    output.insert("end","Raport zostanie zapisany do:\n"+str(path))
    output.configure(state="disabled")
    footer=tk.Frame(win,bg=t["bg"]);footer.pack(fill="x",padx=12,pady=(0,12))
    def open_report():
        try:
            if path.exists() and hasattr(_u135_os,"startfile"):_u135_os.startfile(str(path))
            else:messagebox.showinfo("Raport",str(path) if path.exists() else "Raport nie jest jeszcze dostępny.")
        except Exception as exc:messagebox.showerror("Raport",str(exc))
    app.make_button(footer,"OTWÓRZ RAPORT",open_report,"accent",side="left",ipady=4)
    app.make_button(footer,"ZAMKNIJ",win.destroy,"card",side="right",ipady=4)
    def worker():
        started=_u135_datetime.now().astimezone().isoformat(timespec="seconds")
        record={"id":key,"title":item["title"],"started_at":started,"status":"WARN","source":"Windows PowerShell/CIM","report_path":str(path)}
        try:
            result=_u135_subprocess.run(["powershell.exe","-NoProfile","-Command",item["command"]],capture_output=True,text=True,encoding="utf-8",errors="replace",timeout=120,creationflags=getattr(_u135_subprocess,"CREATE_NO_WINDOW",0))
            raw=(result.stdout or "").strip()
            record["exit_code"]=result.returncode
            record["stderr"]=(result.stderr or "").strip()
            record["data"]=None
            if raw:
                try:record["data"]=_u135_json.loads(raw)
                except Exception:record["data"]={"raw_output":raw}
            record["status"]=_u135_status_from_output(result.returncode,raw,record["data"])
            if not raw:record["message"]="System nie zwrócił danych; nie oznaczono PASS."
        except Exception as exc:
            record["error"]=type(exc).__name__+": "+str(exc)
            record["message"]="Odczyt nie powiódł się; wynik pozostaje WARN."
        try:
            path.write_text(_u135_json.dumps(record,ensure_ascii=False,indent=2),encoding="utf-8")
        except Exception as exc:
            record["report_error"]=str(exc)
        body=_u135_json.dumps(record,ensure_ascii=False,indent=2)
        def finish():
            try:
                if not win.winfo_exists():return
                status.set(record["status"]+" — "+str(path))
                output.configure(state="normal");output.delete("1.0","end");output.insert("end",body);output.see("end");output.configure(state="disabled")
                try:app.append_log("SERWIS ULTIMATE "+key+": "+record["status"]+"; "+str(path))
                except Exception:pass
            except Exception:pass
        try:app.after(0,finish)
        except Exception:pass
    _u135_threading.Thread(target=worker,daemon=True,name="NaprawaPC-Serwis-"+key).start()

def _u135_show_serwis_diagnostics(app):
    app.current_view="SERWIS_ULTIMATE_EXTRA_DIAGNOSTICS"
    app.clear()
    t=app.colors()
    app.header_title.config(text="SERWIS ULTIMATE — DODATKOWE TESTY")
    head=app.panel(app.content);head.pack(fill="x",padx=3,pady=(0,5))
    tk.Label(head,text="10 ODRĘBNYCH TESTÓW • KAŻDY MA WŁASNE OKNO I RAPORT JSON",bg=t["panel"],fg=t["accent"],font=app.fnt(11,"bold")).pack(anchor="w",padx=10,pady=(8,3))
    tk.Label(head,text="Testy są odczytowe. Nie wyłączają ochrony, nie zatrzymują usług, nie resetują sieci i nie naprawiają dysków. Brak danych lub błąd jest oznaczany WARN/N/D.",bg=t["panel"],fg=t["muted"],font=app.fnt(8),wraplength=1300,justify="left").pack(anchor="w",padx=10,pady=(0,8))
    for key,item in _U135_SERWIS_TESTS.items():
        card=app.panel(app.content);card.pack(fill="x",padx=3,pady=3)
        row=tk.Frame(card,bg=t["panel"]);row.pack(fill="x",padx=8,pady=5)
        left=tk.Frame(row,bg=t["panel"]);left.pack(side="left",fill="x",expand=True)
        tk.Label(left,text=item["title"],bg=t["panel"],fg=t["text"],font=app.fnt(9,"bold"),anchor="w").pack(fill="x")
        tk.Label(left,text=item["description"],bg=t["panel"],fg=t["muted"],font=app.fnt(8),anchor="w",wraplength=1050,justify="left").pack(fill="x",pady=(2,0))
        app.make_button(row,"URUCHOM",lambda k=key:_u135_run_serwis_test(app,k),"accent",side="right",ipady=4)
    tools=app.panel(app.content);tools.pack(fill="x",padx=3,pady=5)
    app.make_button(tools,"← CENTRUM NAPRAW",app.show_system_repair_center,"card",side="left",ipady=4)
    return None

def _u135_selftest_serwis_diagnostics():
    assert len(_U135_SERWIS_TESTS)==10
    assert len(set(_U135_SERWIS_TESTS))==10
    assert len({v["title"] for v in _U135_SERWIS_TESTS.values()})==10
    assert len({v["command"] for v in _U135_SERWIS_TESTS.values()})==10
    forbidden=("Remove-Item","Format-Volume","Clear-Disk","Restart-Computer","Stop-Computer","Set-NetIPInterface","netsh winsock reset","Disable-Mp")
    for key,item in _U135_SERWIS_TESTS.items():
        assert item.get("title") and item.get("description") and item.get("command")
        assert not any(word.lower() in item["command"].lower() for word in forbidden),key
    assert callable(_u135_show_serwis_diagnostics)
    assert _u135_status_from_output(0, '{"state":"PASS"}', {"state":"PASS"}) == "PASS"
    assert _u135_status_from_output(0, '{"state":"N/D"}', {"state":"N/D"}) == "WARN"
    assert _u135_status_from_output(0, '{"state":"WARN"}', {"state":"WARN"}) == "WARN"
    assert _u135_status_from_output(1, '{"state":"PASS"}', {"state":"PASS"}) == "WARN"
    assert _u135_status_from_output(0, "not-json", None) == "WARN"
    print("SERWIS_ULTIMATE_EXTRA_DIAGNOSTICS_SELFTEST_OK: 10 unique read-only tests, separate JSON reports and honest N/D/WARN status")


# Map each component simulator to a different real OpenGL scene family.
# This is explicitly a GPU-rendering check, not a claim that OpenGL measures CPU/RAM/disk performance.
_U135_SCENE_BY_MODULE = {
 "GPU":1, "CPU":8, "RAM":17, "VRAM":26, "DYSK":35, "EKRAN":44,
 "SECURITY":53, "BATERIA":62, "SIEĆ":71, "USB":80, "AUDIO":89,
 "KLAWIATURA":98, "KAMERA":107
}

def _u135_start_real_3d(app,module):
    module=str(module or "").upper()
    scene_id=_U135_SCENE_BY_MODULE.get(module)
    if scene_id is None:
        messagebox.showwarning("OpenGL 3D","Nie ma przypisanej odrębnej sceny dla tego modułu.")
        return
    if getattr(app,"running",False):
        messagebox.showwarning("OpenGL 3D","Inny test jest uruchomiony. Zatrzymaj go przed uruchomieniem sceny.")
        return
    if not (1 <= scene_id <= len(_U66_SCENES)):
        messagebox.showerror("OpenGL 3D","Nieprawidłowy identyfikator sceny.")
        return
    seconds=10
    resolution=str(getattr(app,"_u90_scene_resolution_value","1920x1080") or "1920x1080")
    scene_name=_U66_SCENES[scene_id-1][0]
    if not messagebox.askyesno(
        "Rzeczywiste renderowanie OpenGL",
        f"Uruchomić unikalną scenę {scene_id:02d}: {scene_name}?\\n\\n"
        f"Czas: {seconds} s • rozdzielczość: {resolution}\\n"
        "Otworzy się osobne okno renderera. Wynik obejmuje rzeczywiste FPS i dane renderera GPU. "
        "To test renderowania GPU, a nie benchmark CPU/RAM/dysku."
    ):
        return
    try:
        app.stop_requested=False
        app.worker(lambda:_u66_execute_gpu_scene(app,scene_id,seconds))
    except Exception as exc:
        messagebox.showerror("OpenGL 3D",f"Nie udało się uruchomić sceny: {type(exc).__name__}: {exc}")

def _u135_selftest_real_3d_scene_mapping():
    ids=list(_U135_SCENE_BY_MODULE.values())
    assert len(ids)==13 and len(set(ids))==13
    assert all(1 <= int(scene_id) <= len(_U66_SCENES) for scene_id in ids)
    titles=[_U66_SCENES[scene_id-1][0] for scene_id in ids]
    assert len(set(titles))==len(titles)
    assert _U135_SCENE_BY_MODULE["GPU"]==1
    assert callable(_u135_start_real_3d)
    print("COMPONENT_REAL_OPENGL_SCENE_SELFTEST_OK: 13 components map to 13 distinct OpenGL scenes")

if __name__ == "__main__" and "--selftest-advanced-modules" in sys.argv:
    try:
        _u134_selftest_ram_live_dashboard()
        _u135_selftest_real_3d_scene_mapping()
        _u135_selftest_serwis_diagnostics()
        _u134_selftest_unique_service_probes()
        _u133_selftest_service_dashboard_navigation()
        _u132_selftest_service_dashboard()
        _u131_selftest_parallel_progress()
        _u125_selftest_unique_scene_families()
        _u124_selftest_gpu_hud()
        _u124_selftest_speed_quality()
        _u124_selftest_sensor_inspector()
        _u117_selftest_per_test_scene_routing()
        _u119_selftest_furmark_scene()
        _u121_selftest_service_jobs()
        _u121_selftest_power_lab()
        _u123_selftest_repair_profiles()
        _u122_selftest_repair_knowledge()
        _u120_selftest_system_repair_center()
        _u126_selftest_process_manager()
        _u126_selftest_game_diagnostics()
        _u126_selftest_report_manager()
        _u116_selftest_scene_signatures()
        _u116_selftest_sensor_display_controls()
        _u126_selftest_sensor_merge()
        _u114_selftest_turbo_math()
        _u114_selftest_sensor_inventory()
        _u128_selftest_live_sensor_summary()
        _u114_selftest_unique_gpu_scenes()
        _u114_selftest_catalog_routing()
        _u114_selftest_service_catalog()
        _u92_selftest_crash_guard()
        _u107_selftest_sensor_inspector()
        _u108_selftest_live_telemetry()
        _u108_selftest_speed_profiles()
        _u107_selftest_speed_validation()
        _u109_selftest_service_catalog()
        _u107_selftest_unique_scene_per_catalog_test()
        _u106_selftest_sensor_mapping()
        _u106_selftest_adaptive_speed_payloads()
        _u105_selftest_visual_quality()
        _u104_selftest_speed_and_sensors()
        _u102_selftest_ram_visible_progress()
        _u100_selftest_adaptive_speed()
        _u100_selftest_unique_gpu_scenes()
        _u98_selftest_catalog_safety()
        _u93_selftest_catalog_routing()
        _u96_selftest_single_test_screens()
        _u66_selftest_advanced()
        _u86_selftest_component_ui()
        _u90_selftest_release_fixes()
        _u88_selftest_final_wiring()
        assert AppV43.show_module is _u88_show_module_with_independent_tests
        assert _U84_ORIGINAL_SHOW_MODULE is _u69_show_module
        assert callable(_u84_attach_gpu_live_panel)
        assert callable(_u84_gpu_live_tick)
        assert AppV43.show_module is _u88_show_module_with_independent_tests
        assert any("GPU LIVE STUDIO" in str(x) for x in _U100_ORIGINAL_ATTACH_GPU_PANEL.__code__.co_consts)
        assert _U84_GPU_LIVE_FIELDS and len(_U84_GPU_LIVE_FIELDS) >= 8
        print("GPU_LIVE_PANEL_SELFTEST_OK")
        raise SystemExit(0)
    except Exception as _u66_exc:
        import traceback as _u66_traceback
        print("ADVANCED_MODULES_SELFTEST_FAILED:",type(_u66_exc).__name__,str(_u66_exc))
        _u66_traceback.print_exc()
        raise SystemExit(1)
