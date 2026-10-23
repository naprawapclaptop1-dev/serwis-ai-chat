NAPRAWA PC HARDWARE TEST PRO — WINDOWS x64 / ALL-IN-ONE
==========================================================

KANAŁ ONLINE
Aktualna wersja jest publikowana w updates/hardware-test-pro/latest.json.
Aktualny numer wydania, link instalatora i SHA-256 odczytuj z manifestu stable — nie utrzymuj numeru wersji na sztywno w README.
Instalator i pełny pakiet ALL-IN-ONE są dostępne w GitHub Releases:
https://github.com/naprawapclaptop1-dev/serwis-ai-chat/releases

KATALOG DIAGNOSTYCZNY
- 15 grup i 110 odrębnych pozycji katalogu. Każdy wpis ma osobny ekran, własną procedurę i raport JSON.
- CPU (7), RAM (7), GPU (8), VRAM (6), dyski (7), ekran/EDID (5), bezpieczeństwo Windows (4), bateria (5), sieć (5), USB (4), audio (5), klawiatura/touchpad (4), kamera (3), System Repair PRO (20), Serwis Ultimate (20).
- 110 unikalnych układów renderowania OpenGL. ID 1–90 używają dziewięciu rodzin geometrii po dziesięć wariantów, a ID 91–110 — dwudziestu oddzielnych scen serwisowych. Dodatkowo każda scena dostaje własny podpis geometrii (wariant, liczba elementów, skala, szybkość obrotu i paleta) oraz akcent renderowany przez 31 trybów geometrii: orbity, turbiny, kryształy, kratownice, fale, cząstki, tunele siatek, kolumny termiczne, sfery, PCB, voxele, atomy, klatki, spirale, sieci, przekładnie, światłowody, fraktale i pozostałe odrębne układy. Renderer mierzy rzeczywiste FPS po synchronizacji GPU i zapisuje liczbę wierzchołków/obiektów sceny. To test renderera, nie prognoza FPS w konkretnej grze.
- 125 odrębnych motywów UI z różnymi układami, gęstością, kartami, wykresami i przyciskami.
- Każda procedura zapisuje swój wynik. N/D lub ostrzeżenie nie jest przedstawiane jako zaliczenie.

CPU / RAM / GPU / DYSKI
- CPU: identyfikacja, obciążenie oraz benchmark przepustowości SHA-256 single/multi-thread.
- RAM: odczyt stanu pamięci oraz wzorce i benchmarki bufora z kontrolą danych; nie jest to pełny test wszystkich fizycznych komórek.
- GPU/VRAM: 110 różnych układów renderowania OpenGL z rzeczywistym pomiarem FPS oraz testy alokacji/readback tekstur. Wynik zależy od GPU, sterownika i konfiguracji.
- Dyski: odczyt woluminów, dostępnych rekordów reliability/SMART oraz benchmark plikowy z plikiem tymczasowym usuwanym po teście.
- Ekran: EDID jest oddzielony od odczytu trybów; wizualna ocena martwych pikseli wymaga obserwacji operatora.

TELEMETRIA LIVE
Pełna tabela łączy czujniki z Sensor Bridge z odczytami systemowymi: temperatury, napięcia, zegary, wentylatory, moc, CPU na rdzeń, RAM/swap, I/O/IOPS dysków, transfer kart sieciowych i woluminy/partycje. Wykryty sensor bez aktualnej wartości nadal pozostaje na liście z N/D; licznik odrębnie pokazuje liczbę wszystkich pozycji, dostępnych wartości i N/D. Na pulpicie monitora są przyciski pełnego inspektora, wymuszenia świeżego odczytu oraz lokalnego eksportu całej tabeli do CSV (wraz z N/D). Eksport pozostaje na komputerze i nie jest wysyłany do sieci. Dane N/D nigdy nie są zamieniane na zero.

SPEED TEST
- QUICK: mały transfer; STANDARD: mediana bazowych próbek plus 2 równoległe strumienie HTTPS (6 MB download + 2 MB upload na strumień); MAX: dłuższe próbki i 4 strumienie równoległe (do 64 MB dodatkowego transferu, po potwierdzeniu); TURBO: profil bazowy STANDARD plus 4 strumienie (do 128 MB dodatkowego transferu, po osobnym potwierdzeniu). Wynik równoległy jest raportowany osobno, nie zastępuje mediany.
- Pomiar używa rzeczywistych odpowiedzi HTTP, wielu próbek download/upload oraz czasu odpowiedzi. Nie jest to test sieci LAN bez transferu; wynik zależy od łącza i endpointu.
- Wyniki zawierają profil, próbki i podsumowanie; historia jest zapisywana lokalnie.

SYSTEM REPAIR PRO / SERWIS ULTIMATE
40 testów odczytowych — 20 poprzednich oraz 20 dodatkowych kontroli w tym wydaniu: wersja i status licencji Windows (bez kluczy), BIOS/UEFI/Secure Boot/TPM, PnP i sterowniki, stan Windows Update, błędy dziennika, usługi krytyczne, woluminy/nośniki, BCD/WinRE, usługi sieciowe, DISM CheckHealth, inwentarz sprzętu i oprogramowania, autostart/zadania, historia awarii, konfiguracja IP/DNS, WMI, lista hotfixów, usługi automatyczne, lokalne raporty i wykrywanie instalacji Windows na widocznych woluminach. Każdy ma swój raport. Test DISM CheckHealth wymaga potwierdzenia i nie naprawia automatycznie.
Centrum serwisu zawiera narzędzia SFC/DISM RestoreHealth, CHKDSK, DNS/Winsock, raport baterii, offline DISM/SFC, BCD/WinRE, lokalne szyfrowane zgłoszenia, menedżer procesów z filtrem/CSV i ochroną procesów krytycznych, odczytową diagnostykę gier (GPU, sterownik, DirectX, usługi gier i plan zasilania) oraz menedżer lokalnych raportów z filtrem, otwieraniem plików i eksportem indeksu CSV.

BUDOWANIE LOKALNE
1. Użyj pełnego checkoutu repozytorium z NaprawaPC_Hardware_Test_PRO.pyw, zasobami graficznymi, SUITE_SETUP.iss i folderem SensorBridge.
2. Wymagane: Windows 10/11 x64, Python 3 x64, .NET SDK 10 oraz Inno Setup 6/7.
3. Uruchom BUILD_WINDOWS.bat. Skrypt buduje lokalnie z aktualnej wersji źródła i NIE publikuje release ani nie modyfikuje manifestu stable.
4. Wyniki trafiają do dist, a log do BUILD_LOCAL.log. Publikację online wykonuje GitHub Actions po zaliczeniu selftestów i kompilacji instalatora.

WAŻNE GRANICE
- Windows CI potwierdza określone testy i budowę; nie jest testem fizycznego komputera użytkownika.
- Temperatura, moc, wentylatory, napięcia, zegary i VRAM zależą od sterowników oraz sensorów faktycznie dostępnych na danym sprzęcie.
- Testy RAM/VRAM wykonywane z poziomu procesu nie gwarantują sprawdzenia wszystkich fizycznych komórek.
- Wyniki scen OpenGL nie przewidują FPS każdej gry; edukacyjny symulator nie jest pomiarem, jeśli jego test nie wykonuje realnego renderowania.
- Kanał stable jest opisany w updates/hardware-test-pro/latest.json. W repozytorium jest 40 odczytowych sond diagnostycznych i rozbudowane centrum napraw. To nie jest potwierdzenie pełnej kopii 1:1 każdego wewnętrznego modułu z archiwów System Repair PRO 5.6.25 i Serwis Ultimate 1.15.3; kompletna zgodność źródłowa wymaga przeglądu każdego pliku i każdej funkcji tych projektów.

KANDYDAT 4.3.124 — POPRAWKI WIZUALNE I TELEMETRII
------------------------------------------------
- Benchmark OpenGL ma dodatkowy HUD renderowany w tej samej klatce: pasek postępu, miernik FPS oraz historię ostatnich próbek. Pomiar synchronizuje klatkę przez glFinish; HUD nie zastępuje pomiaru.
- Każda z 110 scen zachowuje własny identyfikator i podpis geometrii. Scena FurMark-style pozostaje osobnym testem obciążeniowym; pozostałe sceny mają inne układy i akcenty geometryczne.
- Pełny inspektor czujników jest osobnym, dużym oknem z wyszukiwaniem, filtrem kategorii, automatycznym odświeżaniem, licznikami wartości/N/D oraz eksportem CSV. Pokazuje wyłącznie dane udostępnione przez Sensor Bridge, sterownik i Windows.
- Panel Speed Test pokazuje medianę, peak, minimum, jitter, współczynnik zmienności i liczbę udanych próbek dla download/upload. Najlepsza pojedyncza próbka nie zastępuje mediany.
- Wbudowane testy obejmują HUD GPU, 110 podpisów scen, tabelę sensorów i prezentację jakości Speed Testu. CI nie zastępuje testu na fizycznym GPU i komputerze użytkownika.

RENDERER GPU — 31 RODZIN GEOMETRII
-------------------------------------------
- Renderer 3D ma 31 jawnie rozdzielonych trybów geometrii: orbity, turbiny, kryształy, kratownice, fale, cząstki, wieże voxel, atomy, klatki, schody spiralne, sieci, przekładnie, światłowody, tunele, fraktale, strumienie danych i osobny wariant PCB.
- Wszystkie 110 ID scen korzystają z 31 trybów, ale mają unikalną kombinację parametrów, palety, liczby elementów i prędkości obrotu.
- Nowy test regresyjny sprawdza, że każdy tryb 0–30 ma własną gałąź renderera, wszystkie 31 stylów są wybierane i 110 sygnatur jest unikalnych.
- Szczegóły wydania i dostępność aktualnego pakietu potwierdza manifest stable; nie opieraj numeru wersji na tym opisie.

RENDERER GPU — 31 RODZIN GEOMETRII
-------------------------------------------
- Renderer 3D ma 31 jawnie rozdzielonych trybów geometrii: orbity, turbiny, kryształy, kratownice, fale, cząstki, wieże voxel, atomy, klatki, schody spiralne, sieci, przekładnie, światłowody, tunele, fraktale, strumienie danych i osobny wariant PCB.
- Wszystkie 110 ID scen korzystają z 31 trybów, ale mają unikalną kombinację parametrów, palety, liczby elementów i prędkości obrotu.
- Nowy test regresyjny sprawdza, że każdy tryb 0–30 ma własną gałąź renderera, wszystkie 31 stylów są wybierane i 110 sygnatur jest unikalnych.
- Szczegóły wydania i dostępność aktualnego pakietu potwierdza manifest stable; nie opieraj numeru wersji na tym opisie.


INTEGRACJA ONLINE — DODATKOWE TESTY SERWIS ULTIMATE
---------------------------------------------------
Dodano 10 odrębnych diagnostyk odczytowych z własnym ekranem i raportem JSON: raport DxDiag, drukarki i bufor wydruku, Bluetooth, historia niezawodności, punkty przywracania/migawki, status BitLocker bez kluczy odzyskiwania, funkcje opcjonalne Windows, runtime'y .NET/Visual C++, profile Wi-Fi bez haseł oraz inwentarz raportów/zrzutów WER.
Testy są dostępne z Centrum napraw i nie zastępują oryginalnych modułów aplikacji źródłowych. Nie wyłączają ochrony, nie zmieniają konfiguracji sieci i nie naprawiają dysków. Wyniki niedostępne są oznaczane WARN/N/D, a nieprawidłowy JSON lub kod wyjścia nie może otrzymać PASS. Przycisk RZECZYWISTE OPENGL / FPS w 13 symulatorach uruchamia 13 odrębnych scen renderowania w osobnym oknie; jest to pomiar renderowania GPU, nie wynik testu CPU/RAM/dysku. Raport DxDiag zapisuje plik tymczasowy z poprawnym cytowaniem ścieżki z odstępami. Pełna zgodność 1:1 z oryginalnymi archiwami nie jest deklarowana bez porównania dokładnych źródeł.

Windows CI dla pull requestów wykonuje testy i budowanie bez publikowania stable. Po scaleniu do main publikacja Setup.exe, ALL-IN-ONE ZIP i manifestu następuje dopiero po pomyślnym buildzie i weryfikacji SHA-256.

Wersjonowanie wydań: pipeline pobiera najnowszy manifest z main przed wyliczeniem kolejnego numeru, aby nie odtworzyć starego tagu, gdy poprzednie wydanie zostało opublikowane po utworzeniu commita wyzwalającego build.


AUDYT WINDOWS / STEROWNIKÓW — NOWY MODUŁ
-----------------------------------------
Centrum Testów zawiera audyt odczytowy Windows, który sprawdza bieżący stan urządzeń PnP i kody problemów, sterowniki bez raportowanego podpisu, stan Microsoft Defender, profile zapory, Secure Boot/UEFI, TPM, dostępny stan dysków fizycznych, wolne miejsce, znaczniki oczekującego restartu, zdarzenia System z ostatnich 24 godzin, podstawowe usługi/Windows Update, presję RAM, adaptery sieciowe i stan baterii.
Po zakończeniu tworzone są raporty HTML oraz JSON w %LOCALAPPDATA%\\NaprawaPC\\WindowsAudits. Raport zawiera stan PASS/WARN/INFO/N/D, szczegóły oraz zalecenia. Niepodpisany sterownik nie jest automatycznie uznawany za malware, N/D nie jest zaliczeniem, a odczyt SMART/WMI nie zastępuje testu fizycznego.


HISTORIA AUDYTÓW WINDOWS — NOWE FUNKCJE
--------------------------------------
W module AUDYT WINDOWS / STEROWNIKI dostępne są trzy dodatkowe akcje:
- HISTORIA RAPORTÓW: lista lokalnych audytów z datą, komputerem, liczbą PASS/WARN/FAIL/N/D i ścieżkami HTML/JSON; można otworzyć wybrany raport.
- PORÓWNAJ 2 OSTATNIE: porównuje poszczególne kontrole ze starszego i nowszego audytu; wykrywa pogorszenia, poprawy, nowe/brakujące kontrole oraz zmienione wyniki.
- EKSPORT HISTORII CSV: zapisuje lokalny indeks raportów do CSV w kodowaniu UTF-8 z BOM; pola tekstowe są zabezpieczane przed interpretacją jako formuły arkusza.
Raporty i historia pozostają lokalne w %LOCALAPPDATA%\\NaprawaPC\\WindowsAudits. Dopiero po wykonaniu co najmniej dwóch audytów porównanie może pokazać zmiany. N/D oznacza brak odczytu, a nie pozytywny wynik.


Rozszerzenie 4.3.143: w historii raportów można zaznaczyć dowolne dwa audyty (Ctrl/Shift), porównać ich wyniki i wyeksportować pełną tabelę wszystkich kontroli z wybranego raportu do CSV.


INTEGRACJA JEDNEJ SUITY — KANDYDAT 4.3.144
- Jeden instalator dołącza pełny program WPF NAPRAWA PC SYSTEM REPAIR PRO 5.6.16, budowany z wersjonowanych źródeł repozytorium.
- Przycisk „CENTRUM SERWISU” otwiera wyszukiwane centrum modułów; pełny WPF startuje jako własne okno. SHA-256 jest sprawdzany przed startem, a UAC obsługuje Windows.
- Ekrany CPU/RAM/GPU pokazują progres i wykresy rzeczywistych odczytów. CPU pokazuje obciążenie systemu/procesu i przepustowość SHA-256; RAM — rzeczywisty postęp wzorców, sprawdzony bufor oraz zapis/weryfikację; GPU — FPS i renderer z raportu procesu OpenGL. Brak sensora jest N/D.
- Moduły Serwis Ultimate pozostają zintegrowane w Hardware Test PRO. Pełna zgodność 1:1 ze starszym archiwum Serwis Ultimate 1.15.3 nie jest deklarowana bez jego źródeł.


KOREKTA TESTÓW CPU / RAM / GPU — KANDYDAT 4.3.144
- RAM: naprawiono błędne porównywanie próbek ze starym wzorcem; test zapisuje i weryfikuje cały bufor wzorcami 00/FF/AA/55, pokazuje postęp, obsługuje STOP i zapisuje JSON.
- CPU: etapy 10/25/50/75/100% mierzą obciążenie systemu podczas testu, operacje SHA-256, taktowanie i per-core tam, gdzie dostępne.
- GPU: przycisk rzeczywistego OpenGL pokazuje się tylko w module GPU; wynik sceny trafia do GPU_3D i raportu modułu. Scena wypełnia większą część okna renderowania.
- Nowy selftest jakości musi przejść przed budowaniem EXE/Setup. Test CI nie zastępuje sprawdzenia czujników na fizycznym komputerze.


KOREKTA TESTÓW CPU / RAM / GPU — KANDYDAT 4.3.145
-------------------------------------------------
- RAM: po każdej próbce oraz po zakończeniu aktualizowany jest główny raport ekranu RAM, nie tylko osobny panel postępu.
- CPU: wskaźnik etapów nie wywołuje nieistniejącej metody UI; ewentualna niedostępność paska nie przerywa testu ani raportowania.
- GPU: renderer OpenGL przesuwa kamerę w głąb sceny. Poprzedni kod resetował macierz model-view bez przesunięcia kamery, więc geometria była przycinana i wyglądała jak mały fragment na czarnym tle.
- Windows CI uruchamia osobny test synchronizacji RAM, bezpiecznego callbacku CPU i kamery OpenGL. Ostateczna kontrola wizualna oraz odczyty sensorów wymagają uruchomienia na realnym sprzęcie.


KOREKTA TESTÓW CPU / RAM / GPU — KANDYDAT 4.3.146
-------------------------------------------------
- GPU/OpenGL: usunięto nałożone przesunięcie kamery. Poprzednia wersja dodawała -7 do istniejącego -10, więc finalna odległość wynosiła -17. Teraz scena ma pojedyncze przesunięcie z=-7 i powinna zajmować większą część okna.
- RAM: końcowy obiekt raportu trafia bezpośrednio do funkcji aktualizacji widoku. UI nie musi czekać na asynchroniczne zapisanie app.results, więc komunikat „test nie został jeszcze uruchomiony” nie powinien przykrywać nowszego raportu.
- RAM: rozpoznawane są etykiety widoku RAM, PAMIĘĆ RAM i MEMORY; postęp wyświetla „TEST W TOKU”, a wynik końcowy używa świeżego statusu i rozmiaru faktycznie sprawdzonego bufora.
- Windows CI sprawdza dokładną transformację kamery, brak starej transformacji -10, priorytet świeżego raportu RAM i przejście statusu z postępu do wyniku.


POPRAWKA 4.3.147 — SYNCHRONIZACJA WYNIKÓW RAM
--------------------------------------------
Ekran główny RAM, polskie warianty widoku i ekran szczegółów katalogu RAM korzystają ze wspólnej ścieżki aktualizacji wyniku. Po zakończeniu testu końcowy raport (PASS/WARN/FAIL, rozmiar bufora, szczegóły i ewentualny offset błędu) ma pierwszeństwo nad starym wynikiem z cache. Dla widoków katalogowych nie jest już wymagany dokładny tekst current_view == "RAM"; test regresyjny sprawdza aktualizację statusu na zlokalizowanym ekranie i w szczegółach katalogu.


PANEL WYNIKÓW CPU / RAM / GPU — WYDANIE 4.3.150
------------------------------------------------
Na ekranie głównym CPU, RAM i GPU widoczny jest panel, który co sekundę odświeża dostępne odczyty Windows/czujników oraz ostatni rzeczywiście zapisany benchmark.
- CPU: bieżące obciążenie i zegar, dostępna temperatura, wynik SHA-256/s, średnie obciążenie i liczba wątków.
- RAM: zajętość, pamięć dostępna/całkowita, rozmiar faktycznie sprawdzonego bufora, ukończone wzorce, zapis/weryfikacja i zweryfikowane bajty.
- GPU: bieżące obciążenie/temperatura/zegar tylko z dostępnych czujników oraz średni/peak FPS, wyrenderowane klatki i renderer ostatniej sceny OpenGL.
Skróty prowadzą do katalogu testów i historii pomiarów/CSV. Po ponownym uruchomieniu panel może odczytać ostatni raport z lokalnej historii. Niewykonany benchmark jest opisany jako „NIE WYKONANO”; brak sensora pozostaje N/D.
Test CPU po użyciu STOP kończy się ostrzeżeniem, jeśli pomiar został rzeczywiście przerwany; nie jest przedstawiany jako pełne zaliczenie.


WYDANIE 4.3.151 — FURMARK-STYLE GPU STRESS I NIEPOWTARZALNE SYMULATORY
----------------------------------------------------------------------
- Osobny ekran GPU FURMARK-STYLE STRESS dostępny jest z centrum testów i ekranu GPU. Start uruchamia scenę OpenGL 01, pokazuje FPS zmierzony przez renderer oraz zapisuje raport JSON/HTML. Temperatura/obciążenie pozostają N/D, jeśli sterownik nie udostępnia czujnika.
- Futrzasty donut FurMark-style jest zarezerwowany dla sceny 01; pozostałe 109 scen OpenGL zachowują swoje indywidualne geometrie bez wspólnego, powtarzanego obiektu.
- Laboratorium zawiera 13 osobnych schematów: CPU, RAM, GPU, VRAM, SSD/NVMe, ekran, bezpieczeństwo, bateria, sieć, USB, audio, klawiatura i kamera.
- Ogólny przycisk „UNIKALNA SCENA OPENGL / FPS” jest usuwany z ekranów zwykłych testów. Tylko pozycje symulatorów otwierają właściwy model podzespołu.
- Nazwa FurMark-style oznacza autorski renderer OpenGL inspirowany testami obciążeniowymi; nie jest to oficjalny silnik FurMark 2.


WYDANIE 4.3.152 — BENCHMARK CPU, RAPORT GPU I HISTORIA TESTÓW
------------------------------------------------------------
- Główny przycisk BENCHMARK ULTRA/MAX na stronie CPU uruchamia wielowątkowy benchmark SHA-256 i zapisuje operacje/s, MiB/s, liczbę wątków, ilość danych oraz czas. Długi test wymaga potwierdzenia; STOP pozostawia wynik WARN.
- Wynik pojedynczej sceny OpenGL przekazuje średni FPS, peak FPS 1 s, liczbę klatek, renderer i wersję OpenGL do głównego panelu wyniku GPU. To nie jest szacunek FPS w grze.
- Każdy test uruchamiany z workbencha zapisuje lokalne raporty JSON+HTML do %LOCALAPPDATA%\NaprawaPC\Raporty\ComponentWorkbench.
- Panel raportu ma HISTORIA TESTÓW, OTWÓRZ FOLDER RAPORTÓW i EKSPORT CSV. CSV zawiera datę, komponent, tryb, stan i ścieżki oraz zabezpiecza pola przed formułami arkusza.
- Testy automatyczne sprawdzają zapis i odczyt raportów, kolejność historii, eksport CSV i ochronę przed formułami. Nie zastępują testu na fizycznym CPU/GPU.


WŁASNE TESTY NA GŁÓWNYCH EKRANACH CPU/RAM/GPU — 4.3.153
--------------------------------------------------------
- CPU: przycisk „BENCHMARK CPU SHA-256” na głównej karcie CPU wykonuje rzeczywiste wielowątkowe obliczenia SHA-256 i pokazuje postęp, operacje/s, MiB/s, liczbę wątków, czas i status przerwania.
- RAM: główny ekran korzysta bezpośrednio z testu wzorców przydzielonego bufora, pokazuje postęp i końcowe bajty zapisane/zweryfikowane, wielkość faktycznie testowanego bufora oraz prędkość.
- GPU: główny ekran udostępnia rzeczywiste renderowanie OpenGL oraz oddzielny krótki test FurMark-style. Raport zawiera FPS, liczbę klatek, renderer, wersję OpenGL i rozdzielczość. Renderer otwiera własne okno, ale wynik wraca na główną kartę GPU.
- Wszystkie trzy ekrany udostępniają lokalną historię raportów JSON+HTML oraz eksport CSV. Brak sensora lub wyniku nie jest zamieniany na PASS.
- SHA-256 jest pomiarem przerobu software, RAM testuje przydzielony bufor procesu, a FPS OpenGL opisuje renderowanie — nie gwarantuje pełnej sprawności każdego bloku GPU.
