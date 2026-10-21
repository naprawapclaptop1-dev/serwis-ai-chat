# Audyt integracji — NAPRAWA PC HARDWARE TEST PRO

Data audytu: 2026-10-22  
Baza online sprawdzona: release 4.3.120 i źródło `hardware-test-pro/ADVANCED_MODULES_PATCH.py`.

## Co już znajduje się w źródle Hardware Test PRO

- 110 pozycji katalogu testów w 15 grupach.
- 110 identyfikatorów scen OpenGL, osobny wynik i osobny ekran szczegółów.
- Renderer OpenGL synchronizuje pomiar FPS; wyniki są zależne od GPU, sterownika, rozdzielczości i dostępności kontekstu OpenGL.
- Tabela sensorów łączy dane LibreHardwareMonitor/bridge i metryki systemowe: użycie CPU na rdzeń, RAM/swap, I/O dysków, sieć, woluminy oraz czujniki temperatury/napięć/zegarów/wentylatorów, jeśli są dostępne. Brak wartości ma być oznaczony N/D.
- Speed Test ma profile QUICK/STANDARD/MAX/TURBO; profil TURBO dodaje cztery równoległe strumienie HTTPS i raportuje ich wynik osobno.
- Katalog zawiera 20 testów diagnostycznych System Repair PRO i 20 Serwis Ultimate. To obecnie zestaw procedur diagnostycznych, a nie potwierdzona zgodność funkcja-w-funkcję z oryginalnymi aplikacjami.
- W buildzie 4.3.121 dodano lokalną historię zleceń serwisowych z eksportem HTML oraz 7 niezależnych akcji zasilania/baterii: Battery Info, Battery Report, Energy Report, SleepStudy, Power Requests, Last Wake i aktywny plan zasilania.
- W przygotowywanym buildzie 4.3.122 dodawana jest lokalna baza wiedzy: import dokumentów tekstowych/PDF, deduplikacja SHA-256, wyszukiwanie źródeł i szkic lekcji serwisowej.
- W przygotowywanym buildzie 4.3.123 dodawany jest asystent profili napraw System Repair PRO: 14 profili objawów, osobne odczytowe skany PowerShell, skróty do narzędzi Windows, wyszukiwanie sieciowe i raport HTML.
- W przygotowywanym buildzie 4.3.124 dodawanych jest 10 niezależnych testów Serwis Ultimate: PnP, sterowniki, aplikacje, usługi, procesy, TCP/UDP, Defender, brama/DNS, błędy systemowe i szybka inwentaryzacja.

## Źródła z biblioteki użytkownika odnalezione do porównania

- System Repair PRO: pełny projekt bazowy 5.6.0 oraz pakiet aktualizacji źródła do 5.6.19 (m.in. `MainWindow.xaml`, `MainWindow.xaml.cs`, `MainWindow.Features.cs`, `App.xaml.cs`, `AppUpdateService.cs`, `BUILD.cmd`).
- Serwis Ultimate: źródło 1.4.2 (`Program.cs`, `AllInOneUltimate.csproj`, `BUILD_WINDOWS.bat`, `app.manifest`).
- Dodatkowo znaleziono małe patche System Repair PRO 5.6.23/5.6.24, ale same patche nie są pełnym projektem.
- W dostępnych plikach biblioteki nie potwierdzono pełnych źródeł dokładnie wersji 5.6.25 i 1.15.3. Nie wolno deklarować ich pełnej zgodności na podstawie samego numeru wersji.

## Najważniejsze pozostałe prace — nie oznaczać jako zakończone bez testu

1. **Parzystość System Repair PRO:** porównać wszystkie przyciski i procedury źródła 5.6.19 z katalogiem; przenieść brakujące procedury do wspólnego wykonawcy, osobnych ekranów, raportów i logów. Obejmuje m.in. interaktywny Repair Center, profile problemów, wyszukiwanie rozwiązań, BIOS/licencję, aktualizator i funkcje wiedzy/PDF. Operacje naprawcze wymagają potwierdzenia i UAC.
2. **Parzystość Serwis Ultimate:** odwzorować wszystkie strony i operacje `ShowDashboard`, `ShowHardware`, `ShowDisks`, `ShowLaptop`, `ShowWindows`, `ShowGameTroubleshooting`, `ShowSecurity`, `ShowNetwork`, `ShowProcesses`, `ShowJobs`, `ShowReports`, a także skany sprzętu, baterii, dysków, USB, audio, urządzeń obrazujących, sieci, SMART, raportów i formularzy zleceń. Nie wystarczy pokazać kafelka ani uruchomić linku.
3. **GPU:** porównać wizualnie wszystkie 110 scen; testować na fizycznych kartach NVIDIA i AMD. Wymagany jest realny render, rzeczywisty FPS, widoczny renderer/API oraz bezpieczny STOP. Scena edukacyjna nie może być raportowana jako wynik FPS.
4. **Sensory:** na rzeczywistym komputerze sprawdzić temperatury CPU package/rdzeni, GPU/hotspot/VRAM, płytę, dyski i pozostałe sensory, a także load, zegary, moc, napięcia, wentylatory i pamięć. N/D jest poprawne, jeśli sprzęt lub sterownik nie udostępnia wartości.
5. **Speed Test:** sprawdzić wyniki na łączach wolnych i szybkich; zweryfikować rzeczywiste bajty, status HTTP, medianę próbek, jitter, błędne odpowiedzi oraz rozdzielenie wyniku bazowego od TURBO.
6. **Izolacja ekranów:** uruchomić każdy test z osobna, zatrzymać go i przejść do kolejnego; potwierdzić, że żadne okna, wykresy ani timery nie zostają po poprzednim teście.
7. **Raporty:** potwierdzić unikalny identyfikator, czas, stan PASS/WARN/ERROR/N/D, surowe metryki, ścieżkę raportu i brak fikcyjnego PASS.
8. **Wydanie online:** budować tylko z tej samej gałęzi, która przeszła selftesty; sprawdzić zgodność wersji instalatora, ZIP-a, manifestu i SHA-256. Nie publikować manifestu przed zakończonym buildem.
9. **Testy sprzętowe i wizualne:** CI może sprawdzić składnię, katalog, raportowanie i budowę, ale nie zastępuje fizycznego testu GPU, sensorów, baterii ani peryferiów.

## Zmiana w tym commicie

Przywrócono właściwy test regresyjny unikalnego mapowania 110 pozycji katalogu do 110 różnych scen. Wcześniej nazwa tego testu była nadpisywana aliasem do testu katalogu usług, przez co nie wykonywała asercji unikalności scen. Ten test ma teraz sprawdzać rzeczywiste mapowanie podczas kolejnego builda Windows.

## Status prawdy

Buildy online 4.3.119 i 4.3.120 zakończyły się sukcesem w GitHub Actions. To potwierdza build i testy automatyczne z tego przebiegu, nie test fizycznego komputera. Pełna zgodność 1:1 obu aplikacji źródłowych nie jest jeszcze potwierdzona.
