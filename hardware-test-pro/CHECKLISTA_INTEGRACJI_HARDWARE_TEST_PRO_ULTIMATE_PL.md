# CHECKLISTA INTEGRACJI — HARDWARE TEST PRO + SYSTEM REPAIR PRO + SERWIS ULTIMATE

## Katalog / GPU 3D
- [x] Zachowano 70 dotychczasowych wpisów hardware.
- [x] Dodano 10 osobnych pozycji SYSTEM REPAIR PRO i 10 SERWIS ULTIMATE.
- [x] Każdy z 90 wpisów ma własny identyfikator oraz mapowanie do profilu OpenGL 1–90.
- [x] 90 profili w 30 rodzinach geometrycznych — trzy odmienne układy na rodzinę.
- [ ] Windows CI potwierdza wszystkie selftesty i raporty renderera.
- [ ] Potwierdzić render i FPS na fizycznych komputerach z różnymi sterownikami.

## System Repair PRO
- [x] Informacje Windows/build/architektura.
- [x] Status licencji bez ujawniania pełnego klucza.
- [x] BIOS/UEFI, Secure Boot, TPM, moduły RAM.
- [x] Inwentarz sterowników PnP i błędy urządzeń.
- [x] DxDiag/DirectX.
- [x] SFC /verifyonly oraz DISM /ScanHealth — bez /RestoreHealth.
- [x] Dziennik błędów z ostatnich 72 h.
- [x] Punkty przywracania — tylko odczyt.
- [x] Lokalna baza wiedzy i wyszukiwanie artykułów.

## Serwis Ultimate
- [x] Pełny inspektor czujników/CSV.
- [x] VRAM i raport baterii.
- [x] Kamera, klawiatura/mysz, tryby ekranu, audio, USB.
- [x] Inwentarz modeli CIM/WMI z filtrowaniem.
- [x] UEFI/RAM readiness i jawne otwarcie Windows Memory Diagnostic.

## Telemetria / Speed Test
- [x] CPU per-core i agregat CPU/RAM/swap.
- [x] I/O poszczególnych urządzeń dyskowych i wolne/zajęte miejsce woluminów.
- [x] RX/TX per interfejs i agregat sieci.
- [x] Rekordy Sensor Bridge/LibreHardwareMonitor, dodatkowe temperatury psutil/ACPI.
- [x] Speed Test adaptacyjny z HTTPS RTT, warm-up, median/peak/jitter, realny payload i historia.
- [ ] Zweryfikować odczyty na fizycznym sprzęcie; N/D oznacza brak źródła.

## Bezpieczeństwo
- SFC/DISM wymagają administratora i nie wykonują automatycznych napraw.
- Brak czujnika lub klatek nie jest zaliczeniem.
- Aplikacja nie wykonuje samoczynnego restartu i nie edytuje BCD.
