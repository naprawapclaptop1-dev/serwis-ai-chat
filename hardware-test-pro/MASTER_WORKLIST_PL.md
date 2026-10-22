# MASTER WORKLIST — NAPRAWA PC HARDWARE TEST PRO + SYSTEM REPAIR PRO + SERWIS ULTIMATE

Stan bazowy sprawdzony: online stable 4.3.127 (22.10.2026).  
Kandydat roboczy: 4.3.128 — **nie jest wydaniem, dopóki Windows CI nie zakończy się sukcesem i nie sprawdzimy manifestu, EXE oraz ALL-IN-ONE ZIP**.

## 1. Zmiany wykonane w kandydacie 4.3.128 — oczekują na test końcowy

- [x] Każda ze 110 scen GPU dostaje osobny, deterministyczny profil FurMark: promień/tuba torusa, gęstość włókien, paleta, animacja i skala.
- [x] Wszystkie sceny poza sceną bazową nakładają na własną geometrię osobny torus FurMark; nie są tylko zmianą tytułu ani ID.
- [x] Raport sceny zapisuje profil FurMark i liczbę włókien, a test regresyjny sprawdza 110 różnych profili.
- [x] Inspektor sensorów zachowuje identyfikatory czujników; dwa wentylatory/rdzenie o tej samej nazwie nie powinny być scalane w jeden rekord.
- [x] Podsumowanie live ma pokazywać przewijalną listę wszystkich kategorii telemetrii, nie tylko dwie długie linie temperatur i użycia.
- [ ] Końcowy Windows CI, kompilacja Sensor Bridge, EXE, instalator, ALL-IN-ONE ZIP, sumy SHA-256 i manifest.
- [ ] Jeśli CI zgłosi błąd: poprawka kodu i ponowne uruchomienie CI przed uznaniem wydania za gotowe.

## 2. Hardware Test PRO — pełna macierz testów sprzętowych

- [ ] CPU: identyfikacja, obciążenie wielowątkowe/jednowątkowe, temperatury, zegary, limity i osobny raport.
- [ ] RAM: wykrycie modułów, wzorce, obciążenie, przepustowość i raport; jasno oznaczyć, że test procesu nie sprawdza każdej fizycznej komórki.
- [ ] GPU: identyfikacja, sterownik, API/renderer, obciążenie, temperatury i zegary tam, gdzie są udostępnione.
- [ ] VRAM: osobny test wzorców/zapisu/odczytu; bez deklarowania pełnego testu całej fizycznej pamięci, jeśli zakres nie został pokryty.
- [ ] SSD/HDD/NVMe: SMART/reliability, woluminy, odczyt/zapis, I/O/IOPS, wolne miejsce i osobny raport.
- [ ] Matryca: EDID, rozdzielczość i tryby odświeżania, testy wzorców/kolorów; osobno test trybów i osobno EDID.
- [ ] Bateria i zasilanie: informacje baterii, kondycja jeśli dostępna, raporty Windows, ACPI i plan zasilania.
- [ ] Klawiatura/touchpad, audio/mikrofon, kamera, USB, sieć: niezależne ekrany i jawna zgoda przed odtwarzaniem dźwięku lub próbkowaniem mikrofonu.
- [ ] Bezpieczeństwo Windows: Defender, autostart, zdarzenia, usługi, firewall i inne odczytowe audyty.
- [ ] Każdy test uruchamiany osobno, z osobnym postępem, STOP, wynikiem, statusem PASS/WARN/ERROR/N/D oraz raportem; sprawdzić brak timerów/okien pozostawionych przez poprzedni test.
- [ ] Symulatory przy każdym odpowiednim teście muszą wykonywać rzeczywiste renderowanie/operację, a nie zastępować test fikcyjnym PASS.

## 3. GPU / FurMark / sceny 3D

- [ ] Zachować 110 osobnych testów i 110 mapowań scen; każde mapowanie ma działać od przycisku do właściwego handlera.
- [ ] 110 unikalnych profili FurMark w kodzie kandydata: geometra, gęstość, skala, paleta i ruch różnią się per ID.
- [ ] Prawdziwy OpenGL, glFinish przed pomiarem, FPS średni/szczytowy/próbki, renderer/API, rozdzielczość i bezpieczny ESC/STOP.
- [ ] Jeśli OpenGL nie wystartuje, raport WARN z błędem — nigdy udawany wynik FPS.
- [ ] Obejrzeć zrzuty wszystkich scen i sprawdzić rzeczywisty FPS na fizycznym GPU NVIDIA i AMD; CI nie potwierdza wyglądu na sprzęcie.
- [ ] Upewnić się, że testy CPU/RAM/dysku nie przedstawiają FPS GPU jako wyniku zdrowia danego podzespołu.

## 4. Pełna telemetria

- [ ] Wszystkie rekordy Sensor Bridge / LibreHardwareMonitor i fallbacki Windows: temperatury CPU package/rdzeni/CCD, GPU/hotspot/VRAM, płyty, dysków, kontrolerów i dostępnych pozostałych czujników.
- [ ] Użycie CPU per rdzeń, RAM/swap, GPU, VRAM, zegary, napięcia, moc, wentylatory, bateria, woluminy, sieć i per-dysk I/O/IOPS.
- [ ] Brak wartości zawsze jako N/D; nie zamieniać ACPI thermal zone na rzekomą temperaturę CPU ani nie wymyślać RPM/mocy.
- [ ] Pełna tabela z wyszukiwaniem, filtrem, przewijaniem, odświeżaniem, licznikiem dostępnych/N/D oraz eksportem CSV.
- [ ] Nie scalać dwóch sensorów o identycznej nazwie, gdy ich identyfikatory sprzętowe są różne.
- [ ] Sprawdzić, czy aktualizacje wartości nie powodują migotania ani utraty zaznaczenia/filtra.
- [ ] Testy na rzeczywistym komputerze: CPU/GPU AMD i NVIDIA, płyta główna, wentylatory, AIO/pompy, dyski i czujniki udostępniane przez sterowniki.

## 5. Speed Test

- [ ] Prawdziwe bajty HTTPS, status HTTP, czas, pełność transferu i odrzucanie błędnych próbek.
- [ ] QUICK, STANDARD, MAX i TURBO; większy transfer ma jasne potwierdzenie, a wynik bazowy pozostaje oddzielny od wyniku równoległego.
- [ ] Mediana, średnia, minimum, peak, jitter/rozpiętość RTT, CV/stabilność, liczba próbek i transferów oraz historia.
- [ ] Pokazać postęp i kierunek transferu, a nie tylko końcowy numer.
- [ ] Porównać pomiary na wolnym i szybkim łączu; wyniki zależą od serwera, tras i warunków sieci.

## 6. System Repair PRO 5.6.25 — wymagane przeniesienie funkcji

- [ ] Porównanie plik po pliku i ekran po ekranie z oryginalnym projektem, a nie tylko 20 sond diagnostycznych.
- [ ] Główny panel, nawigacja, wszystkie ekrany, przyciski, handlery, profile problemów i pełny Repair Center.
- [ ] SFC/DISM/CHKDSK, sieć/DNS/Winsock, sterowniki/aktualizacje, BIOS/UEFI/TPM/Secure Boot, licencja Windows, WinRE/BCD, logi, raporty i historia.
- [ ] Aktualizator aplikacji, baza wiedzy, PDF, import/eksport, logowanie i raporty zgodne z oryginałem.
- [ ] Każda naprawa systemowa: potwierdzenie, UAC, kod wyjścia, log, anulowanie i brak destrukcyjnych działań bez zgody.
- [ ] Aktualnie w repozytorium są starszy projekt bazowy i patche do 5.6.24; pełne źródło ZIP 5.6.25 ma 166 715 344 B i nie zostało rozpakowane przez builder. Pełna zgodność 1:1 pozostaje niepotwierdzona.

## 7. Serwis Ultimate 1.15.3 — wymagane przeniesienie funkcji

- [ ] Porównanie źródła 1.15.3 z każdym ekranem i handlerem; istniejące sondy nie są dowodem zgodności 1:1.
- [ ] Dashboard, sprzęt, dyski/SMART, laptop/bateria, Windows, bezpieczeństwo, sieć, diagnostyka gier, procesy, zlecenia i raporty.
- [ ] Wszystkie formularze, pola, filtry, akcje, eksporty, raporty, statusy, historię i nawigację.
- [ ] Menedżer procesów: realne dane, filtrowanie, eksport i potwierdzenie zakończenia; ochrona procesów krytycznych.
- [ ] Zlecenia serwisowe/karta klienta: formularz, walidacja, lokalny zapis, HTML/CSV i historia.
- [ ] W repozytorium są obecnie częściowe ekrany i 20 odczytowych sond; zgodność 1:1 z ZIP-em 1.15.3 nadal wymaga audytu źródła.

## 8. Raporty, bezpieczeństwo i aktualizacje

- [ ] Każdy test zapisuje własny raport z unikalnym ID, datą, czasem, surowymi metrykami, błędami, ścieżką i stanem.
- [ ] Menedżer raportów otwiera/filtruje/eksportuje realne pliki, a nie tylko statyczną listę.
- [ ] Aktualizator HTTPS sprawdza SHA-256, wersję i UAC; awaria aktualizacji nie uszkadza istniejącej instalacji.
- [ ] Setup.exe i ALL-IN-ONE ZIP zawierają zgodne wersje, źródła/zasoby wymagane do pracy, Sensor Bridge i dokumentację.
- [ ] Manifest stable aktualizuje się wyłącznie po udanym Windows buildzie; weryfikacja rozmiaru i SHA-256 po publikacji.

## 9. Końcowa kolejność weryfikacji

1. Dokończyć wszystkie zmiany kodu i dokumentacji.
2. Uruchomić składnię, wszystkie selftesty core/deep/update/launcher/antivirus/themes/service-center/update-flow/advanced-modules.
3. Naprawić każdy błąd automatyczny i ponowić testy.
4. Zbudować Sensor Bridge, EXE, Setup.exe i ALL-IN-ONE ZIP na Windows x64.
5. Sprawdzić rozmiary, SHA-256, zawartość ZIP-a, wersje i manifest.
6. Dopiero wtedy uznać wydanie online za poprawne.
7. Osobno wykonać testy fizycznego sprzętu, bo CI nie może potwierdzić wszystkich czujników, peryferiów ani wyglądu 3D na komputerze użytkownika.

## Zasada statusu

„W kodzie” nie znaczy „przetestowane”; „CI zaliczone” nie znaczy „sprawdzone na fizycznym PC”; „kafelek istnieje” nie znaczy „funkcja źródłowa została przeniesiona”. Pełna integracja pozostaje otwarta do czasu wypełnienia powyższej macierzy dowodami.
