# CHECKLISTA INTEGRACJI — NAPRAWA PC HARDWARE TEST PRO ULTIMATE

## Zweryfikowany stan wydania
- [x] Wydanie 4.3.98 opublikowane przez GitHub Actions: https://github.com/naprawapclaptop1-dev/serwis-ai-chat/actions/runs/39310567796
- [x] Setup.exe i ALL-IN-ONE ZIP opublikowane.
- [x] Manifest stable zaktualizowany dopiero po poprawnej kompilacji i publikacji.
- [x] Windows CI zaliczył składnię, selftesty, budowę EXE i weryfikację Inno Setup.
- [x] Katalog ma 70 unikalnych pozycji i oddzielne ekrany uruchamiania testów.
- [x] Test „Tryby ekranu” jest oddzielony od skanu EDID.
- [x] Mikrofon i głośniki wymagają potwierdzenia przed odczytem próbek lub odtworzeniem tonu.
- [x] Wyniki rozróżniają stan, ostrzeżenie, błąd i brak danych.

## Katalog testów
- [x] CPU — 7 wpisów: identyfikacja, single-thread, multi-thread, obciążenie, stabilność, czujniki i symulator.
- [x] RAM — 7 wpisów: skan, bufory 512/1024/2048 MB, przepustowość, dłuższy przebieg i symulator.
- [x] GPU — 8 wpisów: skan, pojedyncza scena, 3 zestawy 60 scen, telemetria, doradca gier i symulator.
- [x] VRAM — 6 wpisów: inwentarz, testy 64/128/256 MB, stabilność i symulator.
- [x] Dyski — 7 wpisów: skan, SMART/reliability, 512 MB/2 GB/4 GB, długi benchmark i symulator.
- [x] Ekran — 5 wpisów: EDID, tryby, wzorce, RGB/gradienty i symulator.
- [x] Bezpieczeństwo — 4 wpisy: skan, autostart, diagnostyka systemu i symulator.
- [x] Bateria — 5 wpisów: skan, monitor 180/600 s, raport powercfg i symulator.
- [x] Sieć — 5 wpisów: adaptery, DNS/HTTPS, Speed Test, zmienność czasów DNS i symulator.
- [x] USB — 4 wpisy; audio — 5; klawiatura/touchpad — 4; kamera — 3.

## Budowanie lokalne
- [ ] Pełny build na komputerze użytkownika z Python x64, .NET 10 i Inno Setup.
- [ ] Uruchomienie GUI na fizycznym komputerze i potwierdzenie nawigacji.
- [ ] Osobne uruchomienie skanów i benchmarków na realnym sprzęcie.
- [ ] Potwierdzenie odczytów CPU/GPU/VRAM/fan/power dla faktycznie dostępnych sterowników.
- [ ] Weryfikacja instalacji oraz aktualizacji nad istniejącą instalacją.

## Granice pomiaru
- Symulator 3D jest wizualizacją edukacyjną, chyba że uruchomiono odrębny test renderowania.
- RAM/VRAM testowane z procesu Windows nie obejmują gwarantowanie wszystkich fizycznych komórek.
- Benchmark dysku korzysta z pliku tymczasowego; nie wykonuje destrukcyjnego testu sektorów.
- Pusta lista USB/audio/kamery nie dowodzi sprawności fizycznego urządzenia.
- FPS scen OpenGL nie jest prognozą FPS konkretnej gry.
