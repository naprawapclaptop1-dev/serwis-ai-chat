# NAPRAWA PC HARDWARE TEST PRO ULTIMATE — lista integracji

Wydanie docelowe: **4.3.72** (na podstawie manifestu 4.3.71). Ta lista jest utrzymywana razem ze źródłami, a nie na podstawie samego tekstu okna aplikacji.

## Integracja dwóch programów

- [x] Dołączono źródła i testy centrum Serwis Ultimate: naprawy systemu Windows, narzędzia serwisowe, prywatne zgłoszenia z szyfrowaniem.
- [x] Dodano osobny wpis w Centrum testów uruchamiający pełny natywny System Repair PRO.
- [x] Konfiguracja instalatora kopiuje katalog `SystemRepair` do folderu aplikacji.
- [x] Pipeline budowania odtwarza źródłowe ZIP-y System Repair PRO 5.6.16, publikuje aplikację self-contained win-x64 i wykonuje test XAML smoke.
- [x] Pakiet ALL-IN-ONE ma zawierać również cały katalog System Repair PRO.
- [ ] Potwierdzić w CI: System Repair PRO publikuje się bez błędów, przechodzi XAML smoke i jest obecny w instalatorze końcowym.
- [ ] Po instalacji przetestować przycisk uruchamiania pełnego System Repair PRO na komputerze Windows.

## Testy niezależne — każdy moduł osobno

- [x] Wspólny panel akcji na modułach: **SKANUJ**, **BENCHMARK / ULTRA**, **SYMULATOR 3D**.
- [x] CPU: skan, benchmark czasowy i scena 3D CPU Core/Thread/Vector.
- [x] RAM: wzorce i rzeczywisty bufor pamięci, profile większych testów i scena 3D RAM Address/Bitfield/Bandwidth.
- [x] Dysk SSD/HDD/NVMe: rzeczywisty test pliku tymczasowego i profile 256 MB–4 GB oraz scena 3D Sequential/Random I/O.
- [x] GPU: osobny test adaptera i benchmark OpenGL mierzący FPS.
- [x] VRAM: osobna trasa do testu alokacji/odczytu oraz sceny 3D VRAM Texture Tiles/Fillrate.
- [x] Matryca/EDID, bateria/zasilanie, bezpieczeństwo, audio, klawiatura/touchpad, USB i sieć mają niezależne akcje w odpowiednich ekranach.
- [ ] Potwierdzić w CI: wszystkie testy składni i zaawansowanych modułów przechodzą.
- [ ] Testy ręczne: sprawdzić, czy każdy przycisk wykonuje pomiar i zapisuje wynik na fizycznym PC/laptopie, nie tylko otwiera ekran.

## Grafika, wykresy i sceny 3D

- [x] Studio 3D rozszerzone z 20 do **40 scen** z profilami czasu 5, 15, 30, 60, 120 i 300 sekund na scenę.
- [x] Wzmocniono użycie parametru złożoności w renderowaniu zamiast wyświetlać deklarowaną złożoność bez renderowania odpowiadającej liczby obiektów/trójkątów.
- [x] Sceny dedykowane CPU, RAM, SSD/NVMe, VRAM, GPU, PCIe, matrycy i chłodzeniu.
- [x] Dodano panel wskazówek ustawień dla ponad 30 gier; jasno opisuje się je jako profile startowe, nie jako zmierzone FPS w samej grze.
- [ ] Potwierdzić w CI: test źródeł sprawdza 40 scen i dostępność profili ULTRA/MAX.
- [ ] Test ręczny na Windows: uruchomić kilka scen i suite 40 scen, potwierdzić FPS/renderer i STOP.
- [ ] Test ręczny: potwierdzić wykresy na żywo i odczyty temperatur/czujników; brak dostępnego czujnika musi pokazywać N/D.

## Wydanie i bezpieczeństwo

- [ ] Budowanie wersji 4.3.72 zakończone sukcesem.
- [ ] Wszystkie testy wbudowane zakończone kodem 0.
- [ ] Instalator Setup.exe zawiera SystemRepair oraz główny Hardware Test PRO.
- [ ] SHA-256 i rozmiar instalatora zgodne z manifestem globalnym.
- [ ] Zawartość ALL-IN-ONE ZIP sprawdzona; nie wskazuje się nieistniejących plików.
- [ ] Nie omijać Bitdefendera ani nie przywracać automatycznie plików z kwarantanny.
- [ ] Potwierdzenie użytkownika: zainstalowana wersja i testy działają na jego Windows.

## Kryterium końcowe

Nie oznaczać projektu jako kompletnego tylko dlatego, że pojawiło się wydanie lub kafel. Kompletność wymaga zielonego CI, kontroli zawartości instalatora oraz potwierdzenia działania na docelowym Windows.
