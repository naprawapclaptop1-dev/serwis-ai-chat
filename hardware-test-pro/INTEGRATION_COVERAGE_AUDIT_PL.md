# Audyt integracji — NAPRAWA PC HARDWARE TEST PRO

Data audytu: 2026-10-22
**Stable online:** 4.3.133 — Windows CI zakończyło się sukcesem.
**Kandydat roboczy:** 4.3.134 — RAM Live Dashboard oraz testy unikalności testów/procedur; nie jest wydaniem, dopóki CI nie zakończy się sukcesem.

## Co jest obecnie w kodzie online

### Hardware Test PRO
- 110 pozycji katalogu testów w 15 grupach, oddzielne ekrany i 110 identyfikatorów scen OpenGL.
- Renderer ma 31 jawnych rodzin geometrii, a każda z 110 scen otrzymuje własny profil FurMark (promień, tuba, włókna, paleta, animacja i skala). FPS jest mierzony z synchronizacją renderowania; to nadal wymaga wizualnego testu na fizycznych GPU NVIDIA i AMD.
- Pełny inspektor sensorów i przewijalne podsumowanie telemetrii łączą dane LibreHardwareMonitor/Sensor Bridge oraz liczniki Windows. Pokazują użycie CPU na rdzeń, RAM/swap, I/O dysków, sieć, woluminy oraz dostępne temperatury, napięcia, zegary, moc i wentylatory. Brak wartości jest oznaczany N/D.
- Speed Test mierzy rzeczywiste transfery HTTPS do Cloudflare. STANDARD dodaje 2 strumienie równoległe, MAX/TURBO po 4, ULTRA 8; wynik bazowy (mediana) i wynik równoległy są raportowane osobno. Równoległe fazy pokazują transfer łączny, postęp i aktywne strumienie.
- Każdy test katalogowy ma własny identyfikator, ekran i procedurę; automatyczne testy sprawdzają unikalność scen i tras.
- W stable 4.3.133 dodano widoczny przycisk CENTRUM SERWISU na pasku bocznym oraz poprawiono trasę do sieci Wi-Fi/LAN.

### Moduły System Repair PRO / Serwis Ultimate już włączone do Hardware Test PRO
- Katalog 20 odczytowych diagnostyk System Repair PRO i 20 odczytowych diagnostyk Serwis Ultimate (łącznie 40 sond).
- Centrum napraw Windows: SFC, DISM, CHKDSK, punkt przywracania i status WinRE; operacje naprawcze wymagają potwierdzenia/UAC.
- 14 profili problemów System Repair PRO, osobne skany diagnostyczne, skróty do narzędzi Windows i raporty HTML.
- Lokalna baza wiedzy z importem TXT/MD/PDF, deduplikacją SHA-256 i wyszukiwaniem.
- Zlecenia serwisowe z lokalną historią i eksportem HTML; 7 raportów/akcji zasilania i baterii.
- Menedżer procesów z ochroną procesów krytycznych, odczytowa diagnostyka gier oraz lokalny menedżer raportów z filtrem i eksportem CSV.
- Pulpit centrum serwisu ma 18 tras w kodzie stable 4.3.132; po dodaniu RAM Live Dashboard w kandydacie 4.3.134 będzie miał 19 tras.

## Źródła użytkownika i ograniczenia porównania

- W rozmowie wskazano archiwum NAPRAWA_PC_SYSTEM_REPAIR_PRO_5.6.25_RAM_LIVE_DASHBOARD_ULTIMATE_FULL_PROJECT.zip o rozmiarze 166 715 344 B oraz NAPRAWA_PC_SERWIS_ULTIMATE_v1_15_3_FIX (2).zip o rozmiarze 5 710 073 B.
- W bibliotece dostępne są także starsze źródła: System Repair PRO 5.6.0 i patche do 5.6.19/5.6.24 oraz Serwis Ultimate 1.4.2. To nie są te same wersje co 5.6.25 i 1.15.3.
- Pełny ZIP System Repair PRO 5.6.25 został zidentyfikowany, ale jego rozpakowana zawartość nie była dostępna dla bieżącego buildera. Nie wykonano porównania plik-po-pliku. Nie wolno deklarować pełnej zgodności 1:1 na podstawie samego numeru wersji ani obecności 40 sond.

## Pełna lista otwartych prac

1. **System Repair PRO — parzystość źródła:** porównać każdy przycisk, ekran, handler, usługę i raport z oryginalnym 5.6.25. Przenieść brakujące funkcje, w tym pełny RAM Live Dashboard, naprawy, profile problemów, BIOS/UEFI, licencję, aktualizator, bazę wiedzy i procedury z potwierdzeniem/UAC. RAM Live Dashboard z kandydata 4.3.134 nie oznacza pełnej parytetu źródła.
2. **Serwis Ultimate — parzystość źródła:** porównać wszystkie oryginalne metody ShowDashboard, ShowHardware, ShowDisks, ShowLaptop, ShowWindows, ShowGameTroubleshooting, ShowSecurity, ShowNetwork, ShowProcesses, ShowJobs i ShowReports z wersją 1.15.3. Obecne ekrany nie potwierdzają zgodności 1:1.
3. **GPU / FurMark:** obejrzeć wszystkie sceny na prawdziwych GPU NVIDIA i AMD, sprawdzić renderowanie, FPS, rozdzielczość, pamięć VRAM, STOP i brak fikcyjnego PASS. Każda scena musi różnić się faktyczną geometrią/profilami, nie tylko tytułem.
4. **Sensory:** na fizycznych komputerach sprawdzić temperatury CPU package/rdzeni, GPU/hotspot/VRAM, płyty, dysków, baterii i pozostałych czujników oraz load, zegary, moc, napięcia, wentylatory, RAM/swap i I/O. N/D jest poprawne, gdy sprzęt/sterownik nie podaje wartości.
5. **Speed Test:** sprawdzić profile QUICK/STANDARD/MAX/TURBO/ULTRA na wolnych i szybkich łączach; potwierdzić rzeczywiste bajty, status HTTP, medianę, peak, minimum, jitter, błędy i zgodność licznika danych. Porównać wynik z niezależnym pomiarem.
6. **RAM Live Dashboard:** sprawdzić aktualizację co sekundę, prawidłowe wartości RAM/swap, CPU na rdzeń, tabelę procesów i zatrzymanie timera po wyjściu z ekranu.
7. **Izolacja ekranów:** uruchomić każdy test osobno, zatrzymać i przejść do kolejnego; sprawdzić brak wiszących okien, wykresów, timerów i procesów potomnych.
8. **Raporty:** potwierdzić unikalny identyfikator, czas, stan PASS/WARN/ERROR/N/D, surowe metryki, źródła sensorów, ścieżkę raportu i brak fikcyjnych wyników.
9. **Centrum serwisu / nawigacja:** uruchomić wszystkie trasy z paska bocznego i sprawdzić każdy ekran na różnych skalach/rozdzielczościach.
10. **Wydanie online:** po każdej zmianie sprawdzić Windows CI, EXE, Setup, ALL-IN-ONE ZIP, manifest i SHA-256. Manifest może zostać opublikowany dopiero po udanym buildzie.
11. **Test fizyczny:** CI nie zastępuje testu na prawdziwym komputerze: czujniki, bateria, peryferia, GPU, sterowniki, UAC i przerwanie testów wymagają walidacji na Windows.

## Weryfikacja wydania 4.3.133

- GitHub Actions: workflow 39777246173 — sukces.
- Opublikowano Windows x64 Setup i ALL-IN-ONE ZIP; manifest stable został zaktualizowany dopiero po ukończeniu workflow.
- To potwierdza budowę i automatyczne testy, ale nie test fizycznego sprzętu ani pełną parzystość źródeł obu aplikacji.
