# Status integracji — NAPRAWA PC HARDWARE TEST PRO 4.3.130

Data sprawdzenia: 2026-10-22.

## Wydanie online

- Stable: **4.3.130**.
- Windows CI: sukces, run: https://github.com/naprawapclaptop1-dev/serwis-ai-chat/actions/runs/39766232986
- Instalator Setup.exe: https://github.com/naprawapclaptop1-dev/serwis-ai-chat/releases/download/hardware-test-pro-v4.3.130/NAPRAWA-PC-HARDWARE-TEST-PRO-Setup-4.3.130.exe
- ALL-IN-ONE ZIP: https://github.com/naprawapclaptop1-dev/serwis-ai-chat/releases/download/hardware-test-pro-v4.3.130/NAPRAWA-PC-HARDWARE-TEST-PRO-ALL-IN-ONE-4.3.130.zip
- SHA-256 Setup.exe: 792cf6d2862cb760d9e66d8cf6a46e645304df8b426989395d90be36752b8060
- Rozmiar Setup.exe: 142,765,571 bajtów.
- SHA-256 ALL-IN-ONE ZIP: e84d7fcf8d585a535129deee8f763acf97d3db6f6ccd4cc95ffcdc07cad934de
- Rozmiar ALL-IN-ONE ZIP: 286,271,064 bajtów.
- Manifest stable: updates/hardware-test-pro/latest.json; jego SHA-256 i rozmiar instalatora są zgodne z opublikowanym artefaktem.

## Co zostało zbudowane i sprawdzone

- Sensor Bridge z LibreHardwareMonitor; rozszerzono aktywne grupy o baterię, PSU i monitory zasilania, jeżeli są obsługiwane przez bibliotekę/sprzęt.
- Mostek zwraca także liczbę wykrytych identyfikatorów sprzętowych i listę nazw sprzętu, aby ułatwić diagnozę brakujących grup.
- Windows CI sprawdza wymagane grupy Sensor Bridge oraz identyfikatory sensorów.
- Kompilacja Sensor Bridge zakończona sukcesem.
- Składnia i wbudowane selftesty zakończone sukcesem.
- Główny EXE zbudowany; Setup.exe skompilowany i zweryfikowany.
- Setup.exe i ALL-IN-ONE ZIP opublikowane; manifest aktualizacji opublikowany po sukcesie wydania.
- W kodzie pozostają: 110 indywidualnych testów w 15 grupach, 110 profili scen OpenGL/FurMark oraz profile Speed Test QUICK/STANDARD/MAX/TURBO/ULTRA.

## Co nadal jest otwarte — nie uznawać za skończone

### 1. Pełna zgodność źródłowa System Repair PRO 5.6.25
- Porównać wszystkie pliki, ekrany, przyciski, handlery, ustawienia i raporty oryginalnego archiwum z integracją.
- Zweryfikować dashboard/RAM Live Dashboard, Repair Center, narzędzia Windows, sterowniki/aktualizacje, BIOS/UEFI/TPM/Secure Boot, licencję, naprawę rozruchu, bazę wiedzy/PDF, aktualizator i pozostałe funkcje.
- Obecne 20 sond diagnostycznych i 14 profili problemów nie są dowodem pełnej zgodności 1:1.

### 2. Pełna zgodność źródłowa Serwis Ultimate 1.15.3
- Porównać wszystkie widoki, przyciski, handlery, formularze, filtry, akcje, eksporty i historię.
- Zweryfikować dashboard, sprzęt, dyski/SMART, laptop/baterię, Windows, bezpieczeństwo, sieć, gry, procesy, zlecenia i raporty.
- Obecne 20 sond diagnostycznych i częściowe ekrany nie są dowodem pełnej zgodności 1:1.

### 3. Testy fizycznego sprzętu
- Potwierdzić rzeczywiste temperatury CPU/GPU/hotspot/VRAM, wszystkie dostępne wentylatory/pompy AIO, napięcia, zegary i moc na komputerze użytkownika.
- Obejrzeć sceny 3D i sprawdzić rzeczywisty FPS, płynność i bezpieczny STOP na fizycznym GPU.
- Przejść każdy z 110 testów na Windows, sprawdzić raport, historię, brak timerów pozostających po teście i działanie peryferiów.
- Porównać Speed Test z niezależnym pomiarem na łączach o różnej przepustowości.

## Zasada statusu

Udany CI potwierdza kompilację i automatyczne testy tego wydania, ale nie zastępuje testów na rzeczywistym komputerze ani porównania źródeł aplikacji. Dopóki punkty otwarte nie zostaną wykonane i udokumentowane, projektu nie należy opisywać jako pełnej integracji 1:1 wszystkich funkcji obu aplikacji.
