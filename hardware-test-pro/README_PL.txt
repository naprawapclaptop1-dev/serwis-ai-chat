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
