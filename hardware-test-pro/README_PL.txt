NAPRAWA PC HARDWARE TEST PRO — PAKIET ŹRÓDŁOWY
==============================================

DOKUMENTACJA PAKIETU Z KODEM — NIE JEST TO NUMER WERSJI APLIKACJI
Aktualny publiczny kanał stable należy sprawdzać w updates/hardware-test-pro/latest.json.
Na dzień 2026-10-19 manifest stable wskazuje wydanie 4.3.94.

WERSJA WYDANIA 4.3.94 — FUNKCJE ZINTEGROWANE
- 125 skórek graficznych w jednym programie: 10 dotychczasowych i 115 nowych motywów.
- Wyszukiwarka skórek, podgląd wektorowy dashboardu, zastosowanie całej palety i zapamiętywanie wyboru.
- Skórki różnią się paletą UI: tło, panele, karty, akcenty, statusy oraz grafika pulpitu.
- Aktualizator globalny HTTPS sprawdza rozmiar, SHA-256 i nagłówek PE. Wydania zgodne ze starszymi wersjami używają osobnego pomocnika, który weryfikuje instalator, pokazuje postęp i zapisuje log instalacji.
- Wersja zawiera osobne testy CPU/GPU/RAM/VRAM/dysków/ekranu/peryferiów, sekwencyjny przebieg zaznaczonych testów, panel telemetrii, Speed Test, AI Reader online i centrum serwisu/System Repair PRO. Wyniki czujników nieobsługiwanych muszą pokazywać N/D.
- GPU ma 60 nazwanych scen OpenGL; liczba FPS zależy od faktycznego renderera, sterownika i ustawień.
- Pomiary aplikacyjne RAM/VRAM nie gwarantują sprawdzenia każdej fizycznej komórki.

BUDOWANIE ŹRÓDEŁ
1. Rozpakuj cały pakiet.
2. Uruchom SELFTEST_ALL.bat.
3. BUILD_WINDOWS.bat uruchamiaj na Windows 10/11 x64 z Python x64 i Inno Setup; skrypt przygotowania wydania odtwarza źródło i grafikę z fragmentów Base64 oraz dołącza ADVANCED_MODULES_PATCH.py.
4. EXE i Setup są zapisywane do folderu dist.
5. Publikacja nowego wydania wymaga sukcesu wszystkich testów oraz weryfikacji rozmiaru i SHA-256 instalatora. Manifest latest.json należy aktualizować dopiero po poprawnej publikacji obu assetów.

AKTUALIZACJE Z INNEGO KOMPUTERA
- Zainstalowana aplikacja sprawdza manifest latest.json przez HTTPS i pobiera opublikowany instalator.
- Należy weryfikować wersję, rozmiar oraz SHA-256 względem manifestu i nie ogłaszać aktualizacji jako opublikowanej, zanim istnieje rzeczywisty plik instalatora.
- Windows może wyświetlić monit UAC przy uruchamianiu instalatora.

TESTY I GRANICE
- SELFTEST_ALL.bat uruchamia składnię Python oraz testy core, deep, updatera, launchera, antywirusa, motywów, centrum serwisowego, ścieżki aktualizacji i modułów zaawansowanych.
- Sukces GitHub Actions potwierdza kroki automatycznego builda i testy zapisane w workflow. Nie potwierdza, że każdy czujnik działa na każdym fizycznym komputerze.
- Temperatury, moc, zegary, wentylatory, VRAM oraz GPU utilization zależą od sprzętu, sterowników i Sensor Bridge. Brak wiarygodnego odczytu musi być N/D, nie wartością zgadywaną.
- Testy urządzeń wejścia/wyjścia zależą od dostępności urządzenia i interakcji użytkownika. Brak odpowiedzi nie powinien być przedstawiany jako zaliczony test funkcjonalny.
- Test sieci wykonuje rzeczywisty transfer i zużywa dane; jest uzależniony od dostępności endpointów i sieci.

LABORATORIUM PODZESPOŁÓW
Otwórz Centrum Testów i wybierz „LABORATORIUM PODZESPOŁÓW — 13 MODUŁÓW”. Moduły mają niezależne przyciski SKAN, TEST/BENCHMARK i SYMULATOR 3D. Profile obejmują 15, 60, 180, 300, 600 i 900 sekund. Wizualizacja 3D jest odrębna od wyniku rzeczywistego pomiaru. Zobacz CHECKLISTA_INTEGRACJI_HARDWARE_TEST_PRO_ULTIMATE_PL.md.
