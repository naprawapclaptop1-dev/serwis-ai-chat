# NAPRAWA PC HARDWARE TEST PRO — backlog pełnej integracji
Data audytu: 2026-10-22

## Zasada
Nie uznajemy funkcji za gotową tylko dlatego, że istnieje przycisk, nazwa, karta, symulator albo test statyczny. Każda pozycja musi mieć własną procedurę, prawdziwe dane/rezultat, obsługę błędu, zapis wyniku i test regresyjny. `N/D` nie jest `PASS`.

## Stan potwierdzony w repozytorium
- Ostatnie potwierdzone wydanie: 4.3.127.
- GitHub Actions run 39735656033: build, selftesty, EXE, Inno Setup, publikacja release i manifest — SUCCESS.
- W repozytorium zadeklarowano 15 grup i 110 wpisów katalogu:
  CPU 7, RAM 7, GPU 8, VRAM 6, dyski 7, ekran/EDID 5, bezpieczeństwo Windows 4, bateria 5, sieć 5, USB 4, audio 5, klawiatura/touchpad 4, kamera 3, System Repair PRO 20, Serwis Ultimate 20.
- Kod zawiera Sensor Bridge oparty na LibreHardwareMonitor, pełną tabelę czujników z N/D, eksport CSV, profile Speed Test oraz 110 ID scen OpenGL i 31 rodzin geometrii.
- Istnieją ekrany Centrum napraw Windows, zleceń serwisowych, menedżera procesów, diagnostyki gier i menedżera raportów.
- CI potwierdza budowę i selftesty kodu, ale nie testuje wszystkich czujników na komputerze użytkownika ani nie zastępuje ręcznego porównania FPS z FurMarkiem.

## P0 — źródła i parytet obu aplikacji
- [ ] Odzyskać i porównać dokładne źródła System Repair PRO 5.6.25 plik-po-pliku.
- [ ] Odzyskać i porównać dokładne źródła Serwis Ultimate 1.15.3 plik-po-pliku.
- [ ] Zrobić tabelę parytetu: oryginalny ekran/funkcja/test → moduł w Hardware Test PRO → handler → raport → test automatyczny.
- [ ] Przenieść brakujące procedury, ustawienia, formularze, katalogi, profile, raporty, historię, aktualizacje i obsługę błędów — nie tylko wygląd.
- [ ] Potwierdzić, że żadna funkcja z obu aplikacji nie jest wyłącznie linkiem do osobnego EXE ani atrapą.
- [ ] Obecnie dostępne w bibliotece pliki są starsze/częściowe: patch System Repair PRO 5.6.19, mały patch 5.6.24 i źródło Serwis Ultimate v1.4.2. Nie są dowodem parytetu z wersjami 5.6.25 i 1.15.3. W repozytorium jest również plik SHA-256 dla dawnej paczki integracyjnej, ale sam plik hash nie zawiera źródeł.

## P0 — GPU, benchmark i symulatory
- [ ] Zweryfikować każdy z 110 ID scen w uruchomionym rendererze, nie tylko unikalność nazw i sygnatur.
- [ ] Potwierdzić, że przycisk pojedynczego testu otwiera właściwą, odrębną scenę i nie wraca do generycznego symulatora modułu.
- [ ] Sprawdzić oddzielne rodziny: FurMark-style furry torus, PCB/komponenty, turbiny/wentylatory, siatki termiczne, kryształy, fraktale, sieci/ścieżki, tunele, cząstki, chłodzenie cieczą, zasilacz/transformator, CPU mesh i pozostałe sceny.
- [ ] Każda scena musi różnić się rzeczywistą geometrią, materiałami, oświetleniem, animacją i profilem pracy GPU — sama zmiana koloru lub tytułu nie wystarcza.
- [ ] Mierzyć rzeczywiste FPS, czas klatki, peak/średnią, liczbę wierzchołków/obiektów, czas trwania, renderer i rozdzielczość; zapisywać przerwania i błędy jako WARN/ERROR.
- [ ] Porównać obciążenie, temperaturę i stabilność na fizycznych kartach NVIDIA i AMD z niezależnym narzędziem. Bez tego nie deklarować równoważności z FurMarkiem.
- [ ] Rozdzielić GPU stress, benchmark FPS, test VRAM i wizualne symulatory komponentów — nie używać jednego wyniku do zaliczania różnych testów.

## P0 — telemetryka i prawdziwe odczyty
- [ ] Zweryfikować uruchamianie Sensor Bridge w instalatorze, EXE i na komputerze bez zainstalowanego SDK.
- [ ] Wyświetlić wszystkie rekordy czujników udostępnione przez sterownik/LibreHardwareMonitor: CPU package/rdzenie, GPU core/hotspot/memory, płyta, chipset, VRM, dyski, wentylatory, pompy, napięcia, zegary, moce i pozostałe typy.
- [ ] Nie scalać różnych wentylatorów/pomp tylko dlatego, że mają podobne nazwy; identyfikować je po sprzęcie, identyfikatorze, typie i źródle.
- [ ] Odczyty CPU: całkowite i per-core, temperatury per-core, taktowanie, moc i napięcie — jeżeli provider je udostępnia.
- [ ] Odczyty GPU: każda karta, obciążenie, VRAM użyte/wolne, temperatura core/hotspot/memory, zegary, moc, wentylatory i limity — z oznaczeniem providera.
- [ ] RAM/swap/commit, I/O/IOPS i przepustowość każdego fizycznego dysku, każdy wolumin/partycja, transfer każdej karty sieciowej, bateria/ładowanie, audio i pozostałe wykryte urządzenia.
- [ ] Zachować czujniki z brakiem wartości jako N/D, pokazać źródło, czas ostatniego odświeżenia, błędy providera i liczniki dostępne/N/D.
- [ ] Dodać/zweryfikować alarmy nieprawidłowych odczytów, przeterminowanych próbek i jednostek; nie zastępować braku danych wartością 0.
- [ ] Porównać na żywym komputerze z niezależnym monitorem sprzętu. Lista „wszystkich” oznacza wszystkie udostępnione przez dany sprzęt i sterowniki, nie gwarancję istnienia czujnika, którego producent nie wystawia.

## P1 — Speed Test
- [ ] Sprawdzić pobieranie i wysyłanie na rzeczywistych odpowiedziach HTTPS i liczyć faktycznie przesłane bajty.
- [ ] Zweryfikować QUICK/STANDARD/MAX/TURBO, rozmiary próbek, limity transferu, timeouty, błędy endpointów i anulowanie.
- [ ] Raportować medianę jako wynik główny, minimum/peak, liczbę próbek udanych/wszystkich, jitter, zmienność i opóźnienie HTTPS; nie nazywać RTT HTTPS pingiem ICMP.
- [ ] Osobno pokazywać wynik transferu równoległego, nie zastępować nim mediany.
- [ ] Dodać czytelny wykres na żywo i historię lokalną; wyświetlać ostrzeżenie o transferze w profilach MAX/TURBO.
- [ ] Zweryfikować realistyczność na wolnym i szybkim łączu oraz przy nieudanych/niepełnych próbkach.

## P1 — kompletność testów sprzętu
- [ ] CPU: identyfikacja, single/multi-thread, stabilność, temperatury i taktowanie pod obciążeniem.
- [ ] RAM: wzorce, losowe i adresowe, wieloprzebiegowe, przepustowość, weryfikacja danych i bezpieczny limit przydziału.
- [ ] GPU/VRAM: test rendererem, alokacja/readback VRAM, wykrywanie błędów i brak fałszywego PASS przy niedostępnym OpenGL.
- [ ] Dyski: SMART/reliability, sekwencyjny/losowy odczyt i zapis, IOPS/latencja, pojemność, woluminy, kontrola błędów i bezpieczne usuwanie plików tymczasowych.
- [ ] Matryca/monitor: EDID i tryby oddzielnie od testu wizualnego pikseli; nie deklarować automatycznego wykrycia martwych pikseli bez odpowiedniej metody.
- [ ] Bateria/zasilanie: zdrowie, pojemność, cykle i stan ładowania, gdy dostępne.
- [ ] Klawiatura/touchpad, audio/mikrofon, kamera, USB/PCI, sieć LAN/Wi-Fi i bezpieczeństwo Windows — osobne ekrany, procedury i raporty.
- [ ] Każdy test ma działać niezależnie, bez konieczności uruchamiania całego zestawu.

## P1 — naprawa Windows i narzędzia serwisowe
- [ ] SFC/DISM/CHKDSK: osobno skan odczytowy i naprawa, jawne potwierdzenie przed zmianą, pełny log i kod wyjścia.
- [ ] BCD/WinRE, punkt przywracania, historia aktualizacji, sterowniki/PnP, usługi, Defender/zapora, BitLocker, TPM/Secure Boot i oczekujący restart.
- [ ] SMART/dyski, sieć/DNS/stos TCP/IP, WMI/CIM, zdarzenia błędów, uruchamianie/autostart i zadania harmonogramu.
- [ ] Raporty, baza wiedzy, profile problemów, rekomendacje naprawy i historia wykonanych działań.
- [ ] Zlecenia serwisowe, dane urządzenia, karta naprawy, eksport raportu klienta, historia i wyszukiwanie.
- [ ] Menedżer procesów z ochroną procesów krytycznych, diagnostyka gier/awarii, katalog programów/sterowników i narzędzia diagnostyczne.
- [ ] Zweryfikować pełną listę oryginalnych ekranów i akcji obu aplikacji z ich źródłami — lista powyżej jest zakresem prac, nie twierdzeniem, że każdy element został już przeniesiony.

## P1 — interfejs i nawigacja
- [ ] Każdy test otwiera swój własny ekran z opisem, postępem, wykresem, wynikiem, logiem i przyciskiem zatrzymania.
- [ ] Naprawić przejścia między ekranami, nakładanie paneli, nieaktualne etykiety, martwe przyciski i automatyczne otwieranie nie tego testu.
- [ ] Ujednolicić jasny/ciemny motyw, skalowanie DPI, rozmiar okna i zachowanie na laptopie.
- [ ] W wynikach rozróżniać PASS/WARN/FAIL/N/D/ANULOWANO i nigdy nie oznaczać testu niedostępnego jako PASS.

## P1 — raporty, regresja i bezpieczeństwo
- [ ] Każdy wynik zapisuje identyfikator testu, datę, czas, parametry, rzeczywiste pomiary, źródło danych i szczegóły błędu.
- [ ] Testy automatyczne sprawdzają routing każdego testu, handler, raport, N/D, błędy i zamknięcie okna.
- [ ] Testy Windows CI: składnia, selftesty, build x64, Sensor Bridge, PyInstaller, Inno Setup, manifest, SHA-256 i kompletność ZIP.
- [ ] Testy fizyczne: NVIDIA/AMD, różne CPU, płyty, AIO/wentylatory, dyski i laptopy.
- [ ] Nie wyłączać antywirusa i nie omijać kwarantanny; podpisywać binaria, jeśli jest dostępny prawidłowy certyfikat.
- [ ] Naprawy systemowe wymagają potwierdzenia; bez automatycznego formatowania, resetowania czy niszczenia danych.

## P1 — pakiet online
- [ ] Jedna zgodna wersja: kod, EXE, Setup, ALL-IN-ONE ZIP, README, manifest i SHA-256.
- [ ] Nie publikować nowego manifestu przed udanym buildem i testami.
- [ ] Wydanie ma zawierać właściwe pliki źródłowe i zależności potrzebne do odtworzenia kompilacji; nie opisywać samego EXE jako pełnych źródeł.
- [ ] Po publikacji sprawdzić pobieranie plików i zgodność sum kontrolnych.
- [ ] Nie uznawać za zakończone, dopóki krytyczne zadania P0 nie są zamknięte i istnieją dowody z testów na sprzęcie.

## Blokery i uczciwy stan
1. W obecnie dostępnych plikach nie znaleziono dokładnych archiwów źródłowych System Repair PRO 5.6.25 i Serwis Ultimate 1.15.3. Są starsze/częściowe pliki oraz hash wcześniejszej paczki integracyjnej.
2. CI dla 4.3.127 zakończyło się sukcesem, ale nie dowodzi to pełnej zgodności 1:1 z tymi aplikacjami ani poprawności wszystkich czujników na konkretnym PC.
3. Żadne wydanie nie powinno być nazwane „w pełni ukończone”, dopóki powyższe krytyczne pozycje nie zostaną rzeczywiście wykonane i sprawdzone.
