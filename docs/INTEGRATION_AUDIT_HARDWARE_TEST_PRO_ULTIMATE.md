# Lista kontrolna integracji — NAPRAWA PC HARDWARE TEST PRO ULTIMATE

Ta lista służy do odhaczania funkcji według **rzeczywistego kodu, wyniku kompilacji i testu na Windows**. Sam przycisk/menu nie wystarcza, aby oznaczyć test jako zweryfikowany.

## A. Zmiany kodu wersji 4.3.86

- [x] Rozbudować studio GPU z 46 do 60 nazwanych scen OpenGL.
- [x] Dodać profile 600 s EXTREME i 900 s TEST TERMICZNY oraz podnieść limity czasu testów obsługujących długie profile.
- [x] Dodać wspólny panel bieżących metryk i sześć wykresów do ekranów podzespołów oraz etapów pełnej diagnostyki.
- [x] Panel odświeża próbki CPU/RAM/GPU, temperatury, moc, napięcia, zegary, wentylatory, odczyt/zapis dysku i transfer sieci w zakresie, w jakim system udostępnia pomiary.
- [x] Dodać w ekranach podzespołów bezpośrednie akcje: SKAN, BENCHMARK ULTRA/MAX i SYMULATOR 3D.
- [x] Zmienić pusty wykres tak, aby jasno informował, że test jeszcze nie został wykonany, zamiast sugerować awarię lub sprawność.
- [x] Dodać panel ostatniego wyniku z woluminem, czasem, przebiegami, odczytem/zapisem i komunikatem o ograniczeniach testu.
- [x] Rozszerzyć wbudowany self-test o asercje dla 60 scen, długiego profilu i nowego panelu.

## B. Moduły Hardware Test PRO — dostępność kodu i zakres pomiaru

- [x] CPU — osobny skan, obciążenie, próbki; temperatura i moc tylko wtedy, gdy czujnik jest dostępny.
- [x] RAM — osobny skan i benchmark wzorców w przydzielonym buforze z weryfikacją; nie udaje pełnego testu całej fizycznej pamięci.
- [x] GPU — identyfikacja, telemetria dostępna ze sterownika i sceny OpenGL z pomiarem FPS.
- [x] VRAM — oddzielny inwentarz oraz test tekstur/wzorców/odczytu zwrotnego, jeśli dostępny renderer obsługuje test.
- [x] SSD/HDD/NVMe — skan woluminu/nośników, dostępne dane SMART/reliability i benchmark pliku tymczasowego na wybranym woluminie.
- [x] Matryca/monitor — EDID oraz wzorce obrazu; martwe piksele wymagają wzrokowego potwierdzenia.
- [x] Bateria/zasilanie — monitoring dostępnych danych; brak baterii w PC stacjonarnym nie jest awarią testu.
- [x] Sieć/Wi-Fi/LAN — lista interfejsów oraz osobny Speed Test download/upload/ping.
- [x] USB — enumeracja urządzeń i raportowanie dostępnych kodów stanu; sama enumeracja nie mierzy zasilania portu.
- [x] Audio/mikrofon/głośniki — wykrywanie i testy funkcjonalne; słyszalność wymaga potwierdzenia.
- [x] Klawiatura/touchpad — wykrywanie i test funkcjonalny.
- [x] Kamera — wykrywanie i dostępność; prawidłowy obraz wymaga podglądu.
- [x] Bezpieczeństwo Windows — dostępny audyt stanu ochrony, autostartu i narzędzi systemowych.
- [x] 13 niezależnych modułów w Laboratorium Podzespołów; testy uruchamiane oddzielnie.
- [x] Każdy moduł ma schematyczną wizualizację 3D. Tylko renderowane sceny GPU są benchmarkiem FPS; schemat CPU/RAM/dysku nie jest pomiarem wydajności 3D danego podzespołu.

## C. Osobne aplikacje / funkcje naprawy — wymagają audytu względem oryginałów

- [ ] Porównać wszystkie ekrany i funkcje oryginalnego **System Repair PRO** z wersją zintegrowaną; odnotować każdą różnicę.
- [ ] Porównać wszystkie ekrany i funkcje oryginalnego **Serwis Ultimate** z wersją zintegrowaną; odnotować każdą różnicę.
- [ ] Przejść po kolei każdą kategorię naprawy Windows, narzędzia systemowe, dzienniki, sterowniki, aktualizacje, raporty i funkcje serwisowe.
- [ ] Sprawdzić, czy wszystkie funkcje działają z menu głównego, a nie tylko że link/przycisk istnieje.
- [ ] Sprawdzić zachowanie przy braku uprawnień, braku czujnika, błędzie komendy, anulowaniu i nieudanym pomiarze.

**Uwaga:** dostępny kod zawiera punkty wejścia do Centrum Serwisu/System Repair i część źródeł hotfix, ale ta lista nie oznacza jeszcze, że każda funkcja obu oddzielnych aplikacji została porównana i zweryfikowana. Te pozycje pozostają otwarte do audytu funkcja-po-funkcji.

## D. Weryfikacja wydania

- [ ] Przejść kontrolę składni Python po odtworzeniu źródeł.
- [ ] Uruchomić wszystkie wbudowane testy, w tym `--selftest-advanced-modules`.
- [ ] Zbudować główny EXE i skompilować instalator Setup.exe.
- [ ] Potwierdzić rozmiar i SHA-256 pliku instalatora względem manifestu globalnego.
- [ ] Potwierdzić opublikowaną wersję w `updates/hardware-test-pro/latest.json`.
- [ ] Na komputerze użytkownika potwierdzić numer wersji w pasku tytułu i wykonać po jednym teście każdego modułu.
- [ ] Potwierdzić, że wykresy otrzymują próbki na żywo; niedostępne czujniki mają pokazywać N/D.
- [ ] Przeprowadzić test długiego profilu z nadzorem temperatury i sprawdzić działanie STOP.

## E. Zasady raportowania

- PASS oznacza wyłącznie sukces konkretnego testu w opisanym zakresie.
- WARN/N/D oznacza brak czujnika, ograniczenie pomiaru, przerwanie albo niejednoznaczny wynik — nie jest zaliczeniem.
- Syntetyczne FPS z OpenGL nie są gwarantowanym FPS w konkretnej grze.
- Benchmark dysku korzysta z tymczasowego pliku; nie jest destrukcyjnym testem sektorów fizycznych.
- Długi test obciążeniowy może mocno nagrzać i obciążyć komputer; przed uruchomieniem należy zachować możliwość przerwania.
