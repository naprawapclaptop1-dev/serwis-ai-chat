NAPRAWA PC HARDWARE TEST PRO — PAKIET ONLINE
===============================================

Aktualna wersja instalatora i jego SHA-256 są zawsze wskazywane w:
updates/hardware-test-pro/latest.json
Wersję ustala publikujący Windows CI. Nie wpisuj numeru wydania ręcznie i nie używaj pliku z niezweryfikowanej kompilacji.

ZAKRES DIAGNOSTYKI SPRZĘTOWEJ
- 125 motywów interfejsu, osobne ekrany testów, status, wykresy i raporty.
- 159 pozycji katalogu w 13 grupach, w tym 90 niezależnych wpisów scen GPU OpenGL z ustalonym mapowaniem ID 01–90.
- CPU: identyfikacja, jednowątkowy i wielowątkowy benchmark SHA-256, obciążenie/stabilność oraz dostępne czujniki.
- RAM: inwentarz wykorzystania pamięci, wzorce i benchmarki bufora, pełne przebiegi oraz raport ograniczeń pamięci procesu.
- GPU: identyfikacja/sterownik, odczyty GPU, sceny OpenGL z rzeczywistymi klatkami/FPS, zestawy standard/ultra/max, VRAM i osobna wizualizacja edukacyjna.
- Dyski: inwentarz woluminów, dane reliability/SMART udostępnione przez Windows, benchmark odczytu/zapisu na pliku tymczasowym.
- Ekran: EDID, bieżące/udostępnione tryby i pełnoekranowe wzorce do oceny przez użytkownika.
- Bateria, sieć, USB, audio, klawiatura/touchpad, kamera oraz bezpieczeństwo Windows mają osobne wpisy i raporty.
- Speed Test wykonuje realne transfery HTTPS Cloudflare, serię próbek, pomiar mediany/szczytu i zmienności RTT. Nie deklaruje sukcesu, gdy transfer nie został zmierzony.
- Monitor live zbiera OS/psutil, GPU oraz surowe wpisy udostępniane przez Sensor Bridge/WMI. Brak czujnika = N/D; aplikacja nie wymyśla temperatury, mocy ani obrotów.

CENTRUM SERWISU / SYSTEM REPAIR PRO
- Serwis Ultimate i System Repair PRO: osobne przestrzenie diagnostyki, napraw systemowych, narzędzi i zgłoszeń prywatnych.
- Offline / BCD / WinRE: wykrywanie instalacji Windows, odczyt BCD/WinRE i operacje naprawcze z potwierdzeniem.
- BIOS / LICENCJA: BIOS/UEFI, płyta, CPU, Secure Boot, TPM, wersja Windows i status aktywacji; pełny klucz produktu nie jest pobierany.
- Baza PDF / Nauka Live: lokalny indeks dokumentów, dodawanie PDF i instrukcji do lokalnej bazy oraz zapisywanie notatek diagnostycznych.
- Audyt systemu: sterowniki, urządzenia PnP z błędami, autostart, historia poprawek Windows, zdarzenia krytyczne/błędy, status Defendera i konfiguracja sieci.
- SFC /SCANNOW, DISM /RESTOREHEALTH, reset Winsock i skan Defendera wymagają oddzielnego potwierdzenia. Raporty zapisywane są lokalnie.

RAPORTY I PRYWATNOŚĆ
Raporty diagnostyczne zapisują się lokalnie pod %LOCALAPPDATA%\NaprawaPC. Zgłoszenia serwisowe są przechowywane lokalnie w postaci szyfrowanej. Pełny klucz Windows nie jest zapisywany. Operacje naprawcze mogą wymagać UAC i mogą zmienić stan systemu — czytaj potwierdzenie przed uruchomieniem.

OGRANICZENIA POMIARÓW
- CI na maszynie buildowej potwierdza kompilację i wbudowane testy, ale nie zastępuje testu konkretnego komputera.
- Czujniki temperatury, mocy, napięcia, zegarów i wentylatorów zależą od sprzętu, sterownika, WMI i Sensor Bridge; brak danych jest pokazywany jako N/D.
- Wzorce RAM/VRAM uruchamiane z procesu Windows nie są gwarancją sprawdzenia każdej fizycznej komórki.
- FPS scen OpenGL jest wynikiem syntetycznego benchmarku, nie prognozą wydajności każdej gry.
- Ocena pikseli, słyszalności dźwięku, jakości mikrofonu i fizycznej sprawności portów wymaga operatora.
- Raport testów w pliku ALL-IN-ONE ZIP jest tworzony dla dokładnego buildu po przejściu CI i zawiera identyfikator przebiegu oraz sumę SHA-256 instalatora.

BUDOWANIE / WYDANIA
Lokalny BUILD_WINDOWS.bat nie publikuje stable. Kanał online publikuje tylko GitHub Actions po poprawnej składni, selftestach, kompilacji EXE i kompilacji/weryfikacji Setup.exe.
Manifest: updates/hardware-test-pro/latest.json
Wydania: https://github.com/naprawapclaptop1-dev/serwis-ai-chat/releases
