# MASTER WORKLIST — NAPRAWA PC HARDWARE TEST PRO + SYSTEM REPAIR PRO + SERWIS ULTIMATE

**Stable online:** 4.3.157 — Setup x64 i All-in-One ZIP opublikowane; latest.json zawiera SHA-256 instalatora.
**Kandydat następny:** profile rzeczywistego benchmarku CPU+RAM+GPU: SZYBKI, STANDARD i ROZSZERZONY, z kontrolowanym STOP oraz jednym raportem JSON/HTML/CSV. Kandydat staje się stable dopiero po Windows CI, kompilacji EXE/Setup i publikacji manifestu.
**PC fizyczny:** odczyty czujników, limity pamięci i FPS OpenGL wymagają potwierdzenia na rzeczywistym sprzęcie.
**Parytet źródeł:** dołączenie System Repair PRO 5.6.16 nie oznacza zgodności 1:1 ze starszym archiwum 5.6.25; pełny Serwis Ultimate 1.15.3 wymaga osobnego porównania.

## Statusy — jak czytać listę
- **W kodzie / selftest** — istnieje implementacja i test automatyczny; nie oznacza działania na każdym sprzęcie.
- **CI / wydanie** — wymaga ukończonego builda Windows, testów, instalatora, ZIP-a i sprawdzenia manifestu.
- **PC fizyczny** — wymaga testu na rzeczywistym komputerze, czujnikach, sterownikach lub peryferiach.
- **Parzystość źródłowa** — wymaga porównania z oryginalnymi archiwami aplikacji i sprawdzenia każdego ekranu/handlera.
- **Otwarte** — nie wolno uznać za gotowe na podstawie samej nazwy, przycisku, opisu lub testu statycznego.

---

## 1. Hardware Test PRO — katalog i niezależne testy

### Aktualnie w kodzie
- [x] Katalog ma **110 odrębnych pozycji w 15 grupach**, z indywidualnymi ekranami, handlerami i raportami JSON.
- [x] Każdy test z katalogu jest mapowany do osobnego ID sceny; regresje sprawdzają unikalność identyfikatorów i routing.
- [x] Grupy: CPU (7), RAM (7), GPU (8), VRAM (6), dyski (7), ekran/EDID (5), bezpieczeństwo Windows (4), bateria (5), sieć (5), USB (4), audio (5), klawiatura/touchpad (4), kamera (3), System Repair PRO (20), Serwis Ultimate (20).
- [x] Testy można uruchamiać pojedynczo; wynik rozróżnia PASS, WARN, ERROR i N/D.
- [x] Raportowanie rozróżnia wynik testu od ograniczeń pomiaru. Brak czujnika nie może być fikcyjnym PASS.

### Do sprawdzenia
- [ ] Przejść przez wszystkie 110 pozycji i potwierdzić działanie każdego przycisku, handlera, ekranu, STOP, wyniku oraz zapisu raportu.
- [ ] Potwierdzić, że po zamknięciu testu nie zostają timery, okna, procesy ani wykresy poprzedniego testu.
- [ ] Dodać testy regresyjne dla każdego znalezionego błędu i ponawiać pełny zestaw selftestów po poprawce.

## 2. CPU
- [x] Osobny moduł i raport; obciążenie procesora i podstawowe metryki systemowe.
- [x] Użycie CPU per rdzeń/wątek, liczba rdzeni/wątków i dostępne zegary w telemetrii Windows.
- [ ] Na PC potwierdzić temperatury package/rdzeni/CCD, taktowanie pod obciążeniem, moc i limity dla różnych platform.
- [ ] Zweryfikować odrębne testy jednowątkowe i wielowątkowe, czas trwania, STOP oraz powtarzalny wynik.
- [ ] Sprawdzić, czy test nie raportuje wyniku, jeśli obciążenie nie wystartowało lub zostało przerwane.

## 3. RAM
- [x] Osobny moduł, raport i wzorce pamięci w przydzielonym buforze z weryfikacją.
- [x] Wykorzystanie, pamięć całkowita/dostępna/użyta oraz swap/pagefile w telemetrii.
- [ ] Sprawdzić wszystkie tryby wzorców, progres, przerwanie, błędy i historię.
- [ ] Dodać/weryfikować testy przepustowości z opisanym rozmiarem bufora i powtarzalnymi przebiegami.
- [ ] Nie deklarować sprawdzenia całej fizycznej pamięci, gdy test obejmuje tylko bufor procesu.

## 4. GPU, VRAM i 3D/FurMark
- [x] Katalog zawiera 110 ID scen OpenGL z odrębnymi profilami parametrów FurMark; selftest sprawdza różne profile.
- [x] Renderer mierzy FPS z synchronizacją renderowania; wynik obejmuje ograniczenia środowiska i rozdzielczości.
- [x] GPU ma osobny ekran, telemetrię i akcje skanowania/benchmarku/symulatora.
- [x] VRAM ma odrębny profil diagnostyczny i raport; zakres nie jest przedstawiany jako test każdej fizycznej komórki pamięci.
- [ ] Na fizycznym GPU obejrzeć sceny, potwierdzić różnorodność geometrii, oświetlenia, materiałów, cieni, animacji, HUD, płynność oraz bezpieczny STOP.
- [ ] Sprawdzić renderer/API, rozdzielczość, FPS, czas klatki i błędy inicjalizacji na kartach NVIDIA oraz AMD.
- [ ] Jeśli OpenGL nie wystartuje, pokazać WARN z przyczyną — nigdy symulowany FPS.
- [ ] Oddzielić wynik syntetycznego renderowania od rzeczywistego FPS w grach i od testów CPU/RAM/dysku.
- [ ] Sprawdzić tekstury/wzorce VRAM, rozmiar przydziału, read-back, wykrywanie błędów i ograniczenia sterownika.

## 5. Dyski SSD/HDD/NVMe
- [x] Osobny moduł i raport; wykrywanie woluminów oraz podstawowy benchmark pliku tymczasowego.
- [x] Telemetria ma globalne i per-dysk odczyty/zapisy, I/O i IOPS tam, gdzie Windows udostępnia liczniki.
- [ ] Sprawdzić SMART/reliability/temperatury dla NVMe, SATA i USB, opisując niedostępne atrybuty jako N/D.
- [ ] Sprawdzić odczyt/zapis, czas dostępu, IOPS, wielkość próbek, miejsce docelowe i usuwanie pliku tymczasowego.
- [ ] Upewnić się, że benchmark nie zapisuje na błędnie wybrany dysk i nie wykonuje destrukcyjnego testu sektorów.
- [ ] Zweryfikować raporty partycji, wolnego miejsca, kondycji i błędów nośnika.

## 6. Matryca / ekran / EDID
- [x] Osobny moduł, identyfikacja EDID i wzorce obrazu.
- [ ] Oddzielnie sprawdzić rozdzielczość, częstotliwości odświeżania, profile kolorów, gradienty, gamma, kontrast i wzorce jednolite.
- [ ] Wykrywanie martwych/zablokowanych pikseli musi wymagać wzrokowego potwierdzenia — nie da się go wiarygodnie zaliczyć automatycznie.
- [ ] Przetestować przełączanie scen, skalowanie Windows, wiele monitorów i przywracanie poprzedniego trybu.

## 7. Bateria, zasilanie, płyta główna i chłodzenie
- [x] Moduły baterii/zasilania oraz raporty Windows; telemetria pokazuje dostępne dane ACPI.
- [ ] Kandydat 4.3.130 rozszerza Sensor Bridge o grupy baterii, PSU i monitorów zasilania — nowy CI ma potwierdzić kompilację i obecność wymaganych właściwości.
- [ ] Zweryfikować napięcia, moc, temperatury płyty, VRM, chipsetu i kontrolerów tylko tam, gdzie źródło je udostępnia.
- [ ] Zweryfikować wszystkie wykryte wentylatory i pompy AIO; zachować odrębne identyfikatory przy takich samych nazwach.
- [ ] Sprawdzić, czy obroty i temperatura pochodzą z rzeczywistego sensora, a nie z założenia lub wartości zastępczej.
- [ ] Testy baterii na laptopie: kondycja jeśli dostępna, stan ładowania, raport baterii, Energy Report, SleepStudy, Power Requests, Last Wake i aktywny plan zasilania.
- [ ] PC stacjonarny bez baterii ma otrzymać N/D / „nie dotyczy”, a nie fałszywy błąd.

## 8. Pełna telemetria — użycie, temperatury, wentylatory i pompy
- [x] Sensor Bridge korzysta z LibreHardwareMonitor i rekurencyjnie czyta podzespoły oraz ich subhardware.
- [x] Tabela łączy sensory z licznikami Windows: CPU per-core, RAM/swap, I/O/IOPS dysków, interfejsy sieciowe, woluminy, baterię i dostępne temperatury.
- [x] Rekordy z niedostępną bieżącą wartością mogą pozostać na liście jako N/D; deduplikacja ma zachowywać identyfikator sprzętowy.
- [x] Inspektor ma wyszukiwanie/filtry, odświeżanie, liczniki i eksport CSV.
- [ ] Po nowym buildzie sprawdzić, czy bateria, PSU i power monitor pojawiają się w wykrytych grupach.
- [ ] Na rzeczywistym PC potwierdzić CPU package/rdzenie, GPU core/hotspot/VRAM, płytę, dyski, napięcia, moc, zegary, wentylatory i pompy.
- [ ] Sprawdzić, czy lista nie traci sensorów o tej samej nazwie i czy aktualizacje nie migoczą ani nie kasują filtrów.
- [ ] Sprawdzić różne źródła/sterowniki i uprawnienia; brak danych musi wskazywać źródło i powód, jeśli jest znany.
- [ ] Nie przedstawiać ACPI Thermal Zone jako temperatury rdzenia CPU. Nie wymyślać RPM, napięcia ani poboru mocy.
- [ ] Potwierdzić odświeżanie na żywo na ekranie głównym, w ekranie testu i w tabeli sensorów; wykresy mają dostawać próbki podczas działania.

## 9. Sieć i Speed Test
- [x] Rzeczywisty transport HTTPS do Cloudflare z walidacją statusu, czasu, bajtów i odrzucaniem niepełnych próbek.
- [x] Profile QUICK, STANDARD, MAX, TURBO i ULTRA; wyniki bazowe i równoległe są osobnymi polami.
- [x] STANDARD korzysta z 2 równoległych strumieni; MAX/TURBO z 4; ULTRA z 8 i wymaga potwierdzenia większego transferu.
- [x] Wynik główny korzysta z mediany udanych próbek; są osobne wartości peak/minimum, jitter i historia.
- [ ] Zmierzyć na wolnym i szybkim łączu, Wi-Fi i Ethernet; porównać z niezależnym testem internetowym.
- [ ] Pokazać próbki, progres, rzeczywiste bajty, czas, liczbę poprawnych/nieudanych transferów i powód błędu.
- [ ] Rozdzielić HTTPS RTT od ICMP ping i wyraźnie to opisać; nie raportować strat pakietów bez faktycznego pomiaru.
- [ ] Potwierdzić, że wybrany profil jest faktycznie przekazywany do silnika testu i że historia zapisuje cały wynik.
- [ ] Sprawdzić endpointy blokowane przez firewall/proxy, przerwanie połączenia, timeout, HTTP error i brak internetu.
- [ ] W profilach MAX/TURBO/ULTRA pokazywać szacowany dodatkowy transfer i wymagać zgody przed jego rozpoczęciem.

## 10. Pozostałe urządzenia i peryferia
- [ ] USB: osobne wykrywanie kontrolerów i urządzeń, statusy, raport oraz ograniczenie — enumeracja nie mierzy prądu portu.
- [ ] Audio: wykrywanie urządzeń wejścia/wyjścia, test głośnika, mikrofonu i poziomów; jawna zgoda przed odtworzeniem dźwięku lub próbkowaniem mikrofonu.
- [ ] Klawiatura/touchpad: test każdej funkcji i wizualne potwierdzenie wejść.
- [ ] Kamera: wykrywanie, podgląd, uprawnienia i jawna zgoda przed włączeniem.
- [ ] Sieć/Wi-Fi/LAN: adaptery, adresy, stan, prędkość łącza i oddzielny Speed Test.
- [ ] Sprawdzić te moduły na urządzeniach fizycznych — selftest nie potwierdza działania peryferiów.

## 11. System Repair PRO 5.6.25 — pełna parzystość funkcji
- [x] W zintegrowanym katalogu jest 20 odczytowych diagnostyk System Repair PRO i 14 profili problemów z analizą oraz raportem HTML.
- [x] Istnieje centrum napraw Windows i dostępne narzędzia systemowe, w tym ścieżki SFC/DISM, CHKDSK, sieci, WinRE/BCD oraz raporty.
- [ ] **Otwarty zakres krytyczny:** porównać pełny ZIP NAPRAWA_PC_SYSTEM_REPAIR_PRO_5.6.25_RAM_LIVE_DASHBOARD_ULTIMATE_FULL_PROJECT.zip plik po pliku i ekran po ekranie z integracją.
- [ ] Odtworzyć i sprawdzić wszystkie widoki, nawigację, przyciski, handlery, ustawienia, dashboard, RAM Live Dashboard, Repair Center, logi i raporty.
- [ ] Sprawdzić funkcje sterowników/aktualizacji, BIOS/UEFI/TPM/Secure Boot, licencji, usług, aktualizacji Windows, logów, napraw rozruchu, PDF/bazy wiedzy i aktualizatora.
- [ ] Każdą naprawę wymagającą zmian systemowych opatrzyć potwierdzeniem, UAC, kodem wyjścia, logiem, obsługą anulowania i zabezpieczeniem danych.
- [ ] Nie uznawać 20 sond diagnostycznych za pełną kopię aplikacji. Zgodność 1:1 pozostaje niepotwierdzona.

## 12. Serwis Ultimate 1.15.3 — pełna parzystość funkcji
- [x] W katalogu jest 20 odczytowych diagnostyk Serwis Ultimate.
- [x] Są zintegrowane: lokalne zlecenia serwisowe z eksportem HTML, menedżer procesów, diagnostyka gier i menedżer raportów.
- [ ] **Otwarty zakres krytyczny:** porównać ZIP NAPRAWA_PC_SERWIS_ULTIMATE_v1_15_3_FIX (2).zip z każdym widokiem i handlerem zintegrowanym.
- [ ] Dashboard, sprzęt, dyski/SMART, laptop/bateria, Windows, bezpieczeństwo, sieć, gry, procesy, zlecenia, raporty i wszystkie ustawienia.
- [ ] Zachować formularze, pola, filtry, walidację, akcje, eksporty, statusy, historię i zachowanie po błędzie.
- [ ] Menedżer procesów musi korzystać z rzeczywistych procesów, potwierdzać zakończenie i chronić procesy krytyczne.
- [ ] Formularz zlecenia musi mieć walidację, zapis, historię i raporty; nie może być statycznym formularzem demonstracyjnym.
- [ ] Nie uznawać 20 sond diagnostycznych za pełną kopię aplikacji. Zgodność 1:1 pozostaje niepotwierdzona.

## 13. Integracja trzech aplikacji
- [ ] Przygotować macierz: nazwa funkcji źródłowej → plik/handler źródła → ekran w aplikacji głównej → test automatyczny → dowód działania.
- [ ] Nie gubić funkcji obecnych wcześniej w Hardware Test PRO.
- [ ] Unikać pustych przycisków, duplikatów, fałszywych PASS, martwych ekranów i zadań działających po zmianie widoku.
- [ ] Wspólna nawigacja, wyszukiwarka narzędzi, grupy, statusy, historia i raporty.
- [ ] Sprawdzić błędy, anulowanie, brak uprawnień, brak urządzenia, niepełne dane i nieobsługiwane wersje Windows.
- [ ] Udokumentować funkcje, których nie da się przenieść 1:1 i wyjaśnić dlaczego, zamiast oznaczać je jako wykonane.

## 14. Raporty, historia i bezpieczeństwo
- [x] Indywidualne raporty JSON testów oraz lokalna historia Speed Testu.
- [x] Lokalne zlecenia serwisowe, raporty HTML i CSV oraz baza wiedzy.
- [ ] Każdy raport powinien mieć unikalne ID, czas, wersję aplikacji, test, surowe metryki, status, błędy i ograniczenia.
- [ ] Menedżer raportów musi otwierać, filtrować i eksportować rzeczywiste pliki, nie tylko wpisy listy.
- [ ] Naprawy systemowe nie mogą uruchamiać się bez potwierdzenia; operacje destrukcyjne muszą być osobno chronione.
- [ ] Sprawdzić prywatność raportów i zgłoszeń, lokalne ścieżki, uprawnienia i zachowanie po usunięciu danych.

## 15. Build, instalator i publikacja online
- [x] Workflow Windows buduje Sensor Bridge, EXE, Setup.exe i ALL-IN-ONE ZIP oraz uruchamia testy automatyczne.
- [x] Manifest stable jest publikowany dopiero po udanym buildzie i publikacji.
- [ ] Kandydat 4.3.130: przejść kompilację Sensor Bridge po rozszerzeniu grup czujników, składnię i wszystkie selftesty.
- [ ] Potwierdzić zgodność wersji EXE/Setup/ZIP, kompletność zasobów i sum SHA-256.
- [ ] Potwierdzić, że linki Release i manifest wskazują ten sam instalator i sumę.
- [ ] Sprawdzić instalację na czysto, aktualizację istniejącej wersji, uruchamianie bez okna CMD i odinstalowanie.
- [ ] Nie nadpisywać stabilnego manifestu po nieudanym buildzie.
- [ ] Nie publikować jako „pełna integracja 1:1”, dopóki nie zostanie wykonane porównanie źródeł obu aplikacji.

## 16. Test końcowy na rzeczywistym PC
- [ ] Sprawdzić numer wersji w pasku tytułu po instalacji.
- [ ] Uruchomić osobno każdy test i sprawdzić wynik, raport, STOP oraz przejście do kolejnego testu.
- [ ] Potwierdzić wszystkie czujniki, temperatury, użycie, wentylatory i pompę AIO dostępne na komputerze.
- [ ] Obejrzeć benchmarki 3D i sprawdzić FPS, płynność, temperatury oraz bezpieczne przerwanie.
- [ ] Wykonać Speed Test QUICK/STANDARD i opcjonalnie MAX/TURBO/ULTRA na łączu bez limitu transferu.
- [ ] Przejść wszystkie ekrany i funkcje System Repair PRO oraz Serwis Ultimate po porównaniu źródeł.
- [ ] Zebrać logi i raporty z testów oraz poprawić każde wykryte odstępstwo.

## Kolejność wykonania
1. Rozszerzyć Sensor Bridge i zabezpieczyć to testem CI.
2. Zbudować i zweryfikować kandydata online.
3. Sprawdzić telemetrię, Speed Test i 110 scen w pełnym Windows CI.
4. Wykonać porównanie źródeł obu aplikacji i utworzyć macierz parzystości funkcji.
5. Przenosić brakujące funkcje partiami, każdą z testem i dowodem działania.
6. Ponowić wszystkie selftesty po każdej większej integracji.
7. Opublikować nową stabilną wersję dopiero po udanym buildzie.
8. Wykonać test fizycznego komputera — CI nie potwierdzi wszystkich czujników ani jakości wizualnej GPU.

**Zasada prawdy:** obecność kodu nie oznacza testu na sprzęcie; udany CI nie oznacza pełnej zgodności 1:1; kafelek nie oznacza działającej funkcji. Otwarte punkty pozostają otwarte do czasu uzyskania dowodu.


## Kandydat 4.3.131 — widoczny postęp równoległego Speed Testu
- [x] Transport równoległy przekazuje postęp każdego strumienia do wspólnego panelu live.
- [x] Panel pokazuje łączny transfer odebranych/wysłanych bajtów, procent, sumę chwilowych Mbps i liczbę aktywnych strumieni podczas faz MAX/TURBO/ULTRA.
- [x] Po zakończeniu fazy wynik jest podsumowany liczbą poprawnych strumieni i rzeczywistymi bajtami; nieudany strumień nie jest zaliczany jako poprawny.
- [x] Dodano test matematyki progresu, ograniczeń bajtów, sumowania strumieni i obsługi wartości nieprawidłowych.
- [ ] Uruchomić pełny Windows CI i sprawdzić, że zmiana nie psuje testów profili ani instalatora.
- [ ] Na prawdziwym łączu porównać STANDARD/MAX/TURBO/ULTRA z niezależnym testem i zapisać logi.
- [ ] Nadal otwarta: parzystość 1:1 obu oryginalnych aplikacji; ta zmiana jej nie zamyka.


## Kandydat 4.3.132 — wspólny pulpit zintegrowanego centrum serwisu
- [x] Dodano jeden ekran z 18 bezpośrednimi trasami do obecnie zintegrowanych modułów: katalog testów, oba katalogi diagnostyczne, centrum napraw Windows, profile napraw, baza wiedzy, zlecenia, zasilanie/bateria, procesy, diagnostyka gier, raporty, pełny inspektor czujników, telemetria live, Speed Test, dyski, bezpieczeństwo i sieć.
- [x] Dodano bezpośredni przycisk do pulpitu zintegrowanego centrum z ekranu napraw Windows.
- [x] Dodano test, który sprawdza liczbę i unikalność tras, dostępność handlerów oraz 20+20 pozycji w katalogach System Repair PRO / Serwis Ultimate.
- [ ] Uruchomić pełny Windows CI, zweryfikować instalator/ZIP/manifest.
- [ ] Sprawdzić wizualnie na Windows, czy wszystkie kafle są widoczne przy różnych skalach i rozdzielczościach.
- [ ] Ten pulpit poprawia nawigację, ale nie zamyka otwartego porównania 1:1 źródeł obu archiwów.


## Kandydat 4.3.133 — nawigacja centrum serwisu
- [x] Dodano widoczny przycisk „CENTRUM SERWISU” na pasku bocznym głównego okna.
- [x] Poprawiono trasę „SIEĆ / WI-FI / LAN”, aby otwierała istniejący ekran pod właściwą nazwą.
- [x] Dodano test regresyjny wpisu paska bocznego i trasy sieci.
- [ ] Pełny Windows CI, EXE, Setup, ALL-IN-ONE ZIP i zgodność manifestu/SHA-256.
- [ ] Wizualny test centrum serwisu na różnych rozdzielczościach i skalach Windows.
- [ ] Parzystość 1:1 obu aplikacji źródłowych pozostaje otwarta.


## Kandydat 4.3.134 — RAM Live Dashboard i unikalność testów
- [x] Dodano ekran RAM Live Dashboard: użycie RAM, dostępna pamięć, rzeczywisty Windows commit charge przez GetPerformanceInfo, swap/pagefile, CPU na rdzeń, lista 15 procesów z największym użyciem RAM oraz przewijalna historia 90 próbek.
- [x] Ekran aktualizuje odczyty co sekundę, nie zapisuje danych do pliku i zatrzymuje odświeżanie po opuszczeniu widoku. Gdy Windows API nie zwraca commit charge, wartość jest N/D.
- [x] Dodano test unikalności tytułów wszystkich 110 testów.
- [x] Dodano test, że 40 sond System Repair PRO / Serwis Ultimate ma 40 unikalnych ID, nazw i skryptów PowerShell.
- [ ] Pełny Windows CI, Setup, ALL-IN-ONE ZIP, manifest i SHA-256.
- [ ] Sprawdzenie RAM Live Dashboard na rzeczywistym Windows i pod dużym obciążeniem pamięci.
- [ ] Pełna parzystość 1:1 obu aplikacji źródłowych nadal otwarta.


## Naprawa testu CI dla kandydata 4.3.134
- [x] Pierwszy workflow 39778215930 zatrzymał się na asercji selftestu, który sprawdzał nazwy wyłącznie w kodzie zewnętrznej funkcji, a pomijał zagnieżdżony timer odświeżania.
- [x] Asercja została poprawiona, aby analizowała także zagnieżdżone funkcje; dodano osobny odczyt Windows commit charge.
- [ ] Ponowić pełny Windows CI przed publikacją; stable pozostaje 4.3.133 do czasu sukcesu.


## Kandydat 4.3.144 — testy CPU/RAM/GPU i jedna paczka
- [x] Centrum Serwisu ma wyszukiwane trasy modułów i pełny System Repair PRO 5.6.16, uruchamiany po SHA-256/ShellExecuteW.
- [x] Jeden Setup instaluje companion WPF i Hardware Test PRO; All-in-One zawiera pliki aplikacji oraz manifest.
- [x] Testy CPU mają obciążenie jednowątkowe/wielowątkowe i tryby stabilności 60/300 s z próbkami CPU/rdzeni.
- [x] Testy RAM pokazują progres faktycznych wzorców, pamięć dostępną, bufor i końcową przepustowość zapisu/weryfikacji.
- [x] GPU pokazuje postęp sceny, FPS i renderer z rzeczywistego raportu OpenGL; brak sensora pozostaje N/D.
- [ ] Na fizycznym Windows potwierdzić UAC, instalację/aktualizację, czujniki i długie testy stabilności.
- [ ] Otwarty: porównanie wszystkich widoków System Repair PRO 5.6.25 z companion 5.6.16.
- [ ] Otwarty: odzyskanie i porównanie pełnego ZIP Serwis Ultimate 1.15.3. Istniejące sondy nie dowodzą pełnego parytetu 1:1.


## Kandydat 4.3.144 — naprawy rzeczywistych testów CPU/RAM/GPU
- [x] RAM: pełny zapis wzorca do każdego bajtu bufora i porównanie SHA-256; stare sprawdzanie rzadkich próbek co 4 KB nie jest już używane.
- [x] RAM: postęp, STOP, bezpieczne ograniczenie rozmiaru oraz raport z faktycznie testowanym buforem i prędkością weryfikacji.
- [x] CPU: pomiary obciążenia systemu i taktowania w trakcie każdego etapu 10/25/50/75/100%, z operacjami SHA-256 i per-core gdy dostępne.
- [x] GPU: wynik OpenGL mapowany do GPU_3D, raportu modułu i lokalnego JSON. Przycisk OpenGL widoczny tylko na ekranie GPU.
- [ ] Windows CI musi zaliczyć QUALITY_TESTS_SELFTEST_OK, kompilację EXE/Setup, ZIP, SHA-256 i manifest.
- [ ] Na fizycznym PC potwierdzić CPU, RAM, FPS/renderer OpenGL oraz osobny test VRAM.


## Kandydat 4.3.145 — korekta cyklu wykonania CPU/RAM/GPU
- [x] CPU nie próbuje wywołać niezdefiniowanego _set_stage; wskaźnik etapów korzysta z istniejącego draw_stage_progress tylko wtedy, gdy płótno jest dostępne.
- [x] RAM synchronizuje główny raport w czasie postępu i po zakończeniu testu, zamiast zostawiać komunikat „test nie został jeszcze uruchomiony”.
- [x] GPU przesuwa kamerę po każdym resecie macierzy model-view na odległość -7, aby pełna scena mieściła się w kadrze.
- [x] Osobny test CI weryfikuje synchronizację RAM, callback CPU i ustawienie kamery OpenGL.
- [ ] Test wizualny, telemetryczny i wydajnościowy na komputerze użytkownika pozostaje do wykonania; CI nie ma dostępu do jego fizycznego GPU/sensorów.


## Kandydat 4.3.146 — dopięcie wyników RAM i kadru GPU
- [x] GPU: usunięto podwójną transformację; odległość kamery jest dokładnie -7, nie -17.
- [x] RAM: przekazywany jest końcowy raport zwrócony przez silnik, niezależnie od kolejności aktualizacji app.results.
- [x] RAM: selftest potwierdza, że świeży wynik FAIL o 64 MB nadpisuje stary pozytywny wynik 128 MB, a postęp w trakcie testu pokazuje status RUNNING.
- [ ] Na fizycznym PC potwierdzić większy kadr GPU, końcowy raport RAM i tabelę CPU na ekranach użytkownika.


## Kandydat 4.3.150 — jawny panel wyników na ekranach CPU/RAM/GPU
- [x] Na ekranach głównych CPU/RAM/GPU dodano panel pokazujący bieżące odczyty systemu oraz ostatni zakończony benchmark.
- [x] CPU: SHA-256/s, obciążenie systemu, liczba workerów/etapów, zegar i dostępna temperatura.
- [x] RAM: bufor faktycznie sprawdzony, ukończone wzorce, MiB/s zapisu/weryfikacji i zweryfikowane bajty.
- [x] GPU: FPS/peak/klatki i renderer z raportu rzeczywistego procesu OpenGL; niedostępne sensory pozostają N/D.
- [x] Dodano skróty do katalogu testów i historii/CSV; na świeżym uruchomieniu panel może odczytać ostatni raport lokalny.
- [x] Przerwanie testu CPU jest rozpoznawane na podstawie rzeczywistego zdarzenia zatrzymania i nie daje fałszywego statusu sukcesu.
- [ ] Na fizycznym PC sprawdzić panel podczas testu, po kliknięciu STOP oraz przy niedostępnych czujnikach.


## Kandydat 4.3.151 — oddzielny GPU stress i niepowtarzalne symulatory
- [x] Dodano ekran GPU FURMARK-STYLE STRESS z czasem, rozdzielczością, START/STOP, prawdziwym FPS i zapisem raportu.
- [x] Ograniczono FurMark-style donut do sceny 01; pozostałe 109 scen nie otrzymują wspólnego overlay.
- [x] Dodano osobne modele CPU, RAM, GPU, VRAM, dysku, ekranu, bezpieczeństwa, baterii, sieci, USB, audio, klawiatury i kamery.
- [x] Zwykłe ekrany testów nie dostawiają już generycznego przycisku tego samego symulatora; wpisy rodzaju simulator otwierają właściwy model komponentu.
- [ ] Windows CI musi zaliczyć nowy self-test. FPS/UAC/odczyt temperatur wymagają późniejszego sprawdzenia na fizycznym komputerze.


## Kandydat 4.3.152 — rzeczywiste wyniki komponentów i raporty
- [x] CPU workbench benchmark mierzy SHA-256 ops/s, MiB/s, wątki, wielkość danych i czas; przerwany test pozostaje WARN.
- [x] Wynik pojedynczej sceny GPU trafia do klucza GPU_REAL_RENDER oraz głównego raportu GPU.
- [x] Każdy run z workbencha zapisuje raport JSON+HTML.
- [x] Workbench zawiera historię raportów, otwarcie folderu oraz eksport CSV z ochroną przed formułami.
- [x] Windows CI sprawdza historię, pliki raportów, sortowanie i CSV przed publikacją.
- [ ] Na fizycznym PC sprawdzić pracę sensorów i OpenGL na aktualnych sterownikach.


**Stable online przed tym kandydatem:** 4.3.152 — Windows Setup i All-in-One opublikowane.
**Kandydat 4.3.153:** na głównych ekranach CPU/RAM/GPU dodano bezpośrednie uruchomienia testów, widoczny postęp i raport końcowy. Windows CI musi zaliczyć benchmark CPU, wynik testu RAM, wynik OpenGL oraz zapis historii JSON/HTML/CSV.


## Kandydat 4.3.157 — niezawodność cyklu START → POMIAR → RAPORT
- [x] Wykrywanie świeżego wyniku uwzględnia nowy słownik i modyfikację istniejącego słownika.
- [x] Raport końcowy z callbacka pracownika może zostać pokazany, jeśli zapis do `app.results` dotrze później.
- [x] Ekran zachowuje stan STARTUJĘ/OCZEKIWANIE/SAVING przez ograniczony czas; nie usuwa aktywnego testu przy pierwszym odczycie `running=False`.
- [x] Windows CI sprawdza świeży raport, fallback i fazy cyklu pracy testu.
- [ ] Po instalacji 4.3.157 na fizycznym komputerze należy powtórzyć CPU 15 s, RAM 256 MB i GPU OpenGL 10 s, sprawdzić wartości i zapisać raport.


## Następny kandydat — profile testów CPU/RAM/GPU
- [x] Dodano wybór profilu SZYBKI / STANDARD / ROZSZERZONY na ekranie TESTY i ekranach CPU/RAM/GPU.
- [x] Profil uruchamia rzeczywiste handlery CPU SHA-256, testu zapisu/weryfikacji bufora RAM oraz oddzielnych scen OpenGL; nie zalicza testu na podstawie animacji.
- [x] Połączony raport przechowuje etap, status, faktyczny czas, ustawienia, wynik GPU i ścieżki raportów; zapisuje JSON + HTML + CSV.
- [x] STOP przekazuje sygnał do bieżącego handlera i zatrzymuje rozpoczęcie kolejnych etapów.
- [ ] Windows CI musi zaliczyć selftest profili i pełny build instalatora.
- [ ] Na fizycznym PC potwierdzić pomiar CPU/RAM/GPU oraz zakończenie/STOP przy prawdziwych sterownikach.


## Kandydat 4.3.159 — automatyczna aktualizacja po wykryciu nowej stable
- [x] Usunięto dodatkowe pytanie przed pobieraniem; wykrycie nowszej wersji uruchamia istniejący pobieracz SHA-256/rozmiar/PE.
- [x] Po weryfikacji instalator uruchamia się automatycznie przez ShellExecuteExW/runas; standardowy monit UAC pozostaje wymagany.
- [x] Usunięto otwieranie folderu pobierania w Explorer po prawidłowym pobraniu.
- [x] Dodano test porównania wersji, release_ready, użycia zweryfikowanego download handlera oraz ścieżki UAC.
- [ ] Windows CI musi przejść pełne testy i opublikować nowy manifest stable przed wdrożeniem na komputerach użytkowników.
