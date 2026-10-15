NAPRAWA PC HARDWARE TEST PRO 4.3.44
===================================

WERSJA 4.3.44 — 125 SKÓREK + GLOBALNY AKTUALIZATOR
- 125 skórek graficznych w jednym programie: 10 dotychczasowych i 115 nowych motywów.
- Wyszukiwarka skórek, podgląd wektorowy dashboardu, zastosowanie całej palety i zapamiętywanie wyboru.
- Skórki różnią się pełną paletą UI: tło, panele, karty, akcenty, statusy oraz grafika pulpitu.
- Aktualizator globalny HTTPS sprawdza rozmiar, SHA-256 i nagłówek PE. Wydania zgodne ze starszymi wersjami używają osobnego pomocnika, który weryfikuje właściwy instalator, pokazuje postęp i zapisuje log instalacji.
- Instalator ma zamknąć starsze procesy aplikacji przed zastąpieniem wersji i usunąć poprzednie pliki EXE z katalogu instalacji.
- Utrzymano rozszerzone wykrywanie antywirusów, diagnostykę GPU, rozszerzony test VRAM i testy RAM.

BUDOWANIE
1. Rozpakuj całą paczkę do folderu.
2. Uruchom SELFTEST_THEMES_UPDATE.bat.
3. Uruchom BUILD_WINDOWS.bat na Windows 10/11 x64. Kompilacja wymaga Python 3 x64 oraz Inno Setup 6/7; skrypt pobiera wymagane biblioteki Python.
4. Instalator i EXE są zapisywane w folderze dist.
5. Aby opublikować wydanie w globalnym kanale z komputera serwisowego, skonfiguruj GitHub CLI (gh auth login), następnie zbuduj i opublikuj instalator. Manifest aktualizacji musi wskazywać rzeczywisty plik Setup.exe i jego SHA-256.

AKTUALIZACJE Z INNEGO KOMPUTERA
- Drugi komputer nie pobiera kodu źródłowego; pobiera opublikowany instalator z manifestu latest.json przez HTTPS.
- Wersja może być pokazana jako dostępna dopiero wtedy, gdy wydanie i instalator są prawidłowo opublikowane. Jeśli manifest wskazuje starą wersję, najpierw trzeba opublikować nowy instalator.
- Podczas instalacji Windows może wyświetlić UAC. Nie odrzucaj monitu, jeśli chcesz kontynuować aktualizację.

TESTY I GRANICE
- SELFTEST_THEMES_UPDATE.bat sprawdza liczbę i unikalność skórek, logikę updatera oraz test nazw antywirusów.
- Zestaw wymaga testów końcowych na prawdziwym Windows. Pomiary GPU/VRAM zależą od sterownika i dostępnej pamięci i nie gwarantują sprawdzenia każdej fizycznej komórki VRAM.