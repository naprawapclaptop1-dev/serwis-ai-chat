# CHECKLISTA INTEGRACJI — NAPRAWA PC HARDWARE TEST PRO ULTIMATE

Cel: następne wydanie po opublikowanym 4.3.77; skrypt wydania wyznaczy numer automatycznie.

## Funkcje potwierdzone w kodzie źródłowym
- [x] Jedna strona „Laboratorium podzespołów” dostępna z Centrum Testów oraz ekranów poszczególnych modułów.
- [x] 13 niezależnych modułów: CPU, RAM, GPU, VRAM, SSD/HDD/NVMe, matryca/EDID, bezpieczeństwo Windows, bateria/zasilanie, sieć, USB, audio, klawiatura/touchpad i kamera.
- [x] Każdy moduł ma trzy oddzielne akcje: „Skan + live 3D”, „Test/benchmark lub test funkcjonalny” i „Sam symulator 3D”.
- [x] Profile benchmarków SZYBKI 15 s / STANDARD 60 s / ULTRA 180 s / MAX 300 s.
- [x] Test CPU wykonuje obciążenie i zapis próbek; brak czujnika temperatury nie jest zamieniany na fikcyjną wartość.
- [x] Test RAM wykonuje wzorce zapisu/odczytu i weryfikację SHA-256 w ograniczonym buforze; nie deklaruje sprawdzenia całej pamięci fizycznej.
- [x] Test dysku mierzy zapis/odczyt unikalnego pliku tymczasowego na wybranym woluminie i usuwa plik po teście.
- [x] Test GPU udostępnia 46 nazwanych scen OpenGL i raportuje zmierzony FPS, renderer oraz czas.
- [x] Test VRAM ma oddzielny test wzorców/odczytu zwrotnego; inwentarz VRAM jest skanem, nie benchmarkiem.
- [x] Sieć ma niezależny pomiar download/upload; bateria, matryca, bezpieczeństwo i peryferia mają testy właściwe dla danego typu modułu.
- [x] Raporty komponentów rozróżniają stan/ostrzeżenie/brak danych; wizualizacja schematyczna 3D nie jest opisywana jako pomiar FPS.
- [x] Zachowane są istniejące połączenia Centrum Serwisu/System Repair, Czytnika AI i kanału globalnych aktualizacji w jednej aplikacji.

## Do potwierdzenia na komputerze użytkownika
- [ ] Zainstalować najnowsze wydanie i potwierdzić numer wersji w pasku tytułu.
- [ ] Uruchomić po jednym skanie CPU, RAM, GPU, VRAM, dysku, matrycy, baterii, sieci, USB, audio, klawiatury, kamery i bezpieczeństwa.
- [ ] Uruchomić benchmarki obsługiwane przez moduły; zachować logi błędów zamiast oznaczać brak pomiaru jako PASS.
- [ ] Potwierdzić dostępność temperatur/obrotów/zegarów na konkretnych sterownikach — nie każdy komputer udostępnia wszystkie sensory.
- [ ] Zweryfikować rekomendacje gier na rzeczywistych benchmarkach konkretnych gier. FPS gry nie jest gwarantowany przez scenę syntetyczną.

## Granice pomiaru
Schemat 3D dla CPU/RAM/dysku/ekranu/peryferiów jest wizualizacją edukacyjną. Tylko testy wykonujące realną operację i zapisujące próbki (np. sceny GPU, RAM, plikowy benchmark dysku, Speed Test) mogą dostarczyć liczbowy wynik benchmarku. Nie jest wykonywany destrukcyjny test sektorów fizycznego dysku ani pełny test całego RAM-u z poziomu procesu Windows.
