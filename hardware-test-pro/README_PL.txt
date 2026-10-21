NAPRAWA PC HARDWARE TEST PRO — PAKIET ŹRÓDŁOWY / ONLINE
=========================================================

KANAŁ ONLINE
Wydanie stabilne określa manifest updates/hardware-test-pro/latest.json.
Build Windows x64, Setup.exe i pakiet ALL-IN-ONE powstają w GitHub Actions po zaliczeniu wbudowanych testów.
Repozytorium: https://github.com/naprawapclaptop1-dev/serwis-ai-chat

ZINTEGROWANE LABORATORIA I TESTY
- Katalog 90 niezależnych pozycji: 70 testów sprzętowych oraz 10 procedur SYSTEM REPAIR PRO i 10 SERWIS ULTIMATE.
- Każdy wpis ma osobny ekran, osobne uruchomienie i raport JSON. Każdy wpis jest przypisany do własnego profilu OpenGL.
- GPU: 90 nazwanych profili w 30 rodzinach geometrycznych; rzeczywisty FPS, peak, klatki, renderer, OpenGL i rozdzielczość.
- CPU: identyfikacja, obciążenie, zegary i syntetyczny throughput single/multi-thread.
- RAM: inwentarz, wzorce/benchmark bufora; test procesu Windows nie gwarantuje sprawdzenia wszystkich fizycznych komórek.
- GPU/VRAM: karta, sterownik, dostępne czujniki i testy rzeczywistej alokacji/readback tekstur OpenGL.
- Dyski: woluminy, wolne/zajęte miejsce, per-device read/write oraz SMART/reliability, gdy Windows je udostępnia.
- Telemetria: surowe rekordy Sensor Bridge/LibreHardwareMonitor, temperatury psutil/ACPI, CPU per-core, RAM/swap, per-disk I/O, woluminy, per-adapter RX/TX, bateria oraz dostępne GPU/VRAM/fan/power/voltage/clock.
- Speed Test: HTTPS Cloudflare, RTT, rozgrzewka, download/upload dopasowane do łącza, mediana/peak/jitter, bajty i historia.
- SYSTEM REPAIR PRO: stan Windows, status licencji bez pełnego klucza, BIOS/UEFI/TPM/Secure Boot/RAM, inwentarz sterowników, DxDiag/DirectX, SFC /verifyonly, DISM /ScanHealth, dziennik zdarzeń, punkty przywracania i lokalna baza wiedzy.
- SERWIS ULTIMATE: pełny inspector/CSV, VRAM, raport baterii, kamera, klawiatura/mysz, tryby ekranu, audio, USB, inwentarz modeli CIM/WMI i gotowość UEFI/Windows Memory Diagnostic.
- SFC/DISM wymagają administratora. Nie uruchamiają /RestoreHealth, automatycznego restartu ani zmian w BCD.

BUDOWANIE / PUBLIKACJA
1. Workflow Windows odtwarza źródło i zasoby z repozytorium.
2. Następuje kontrola składni, selftesty, budowa Sensor Bridge, EXE i instalatora.
3. Release oraz manifest stable są publikowane wyłącznie po sukcesie całego procesu.
4. Testy CI nie zastępują sprawdzenia odczytów na docelowym sprzęcie użytkownika.

GRANICE POMIARU
- FPS OpenGL zależy od sceny, sterownika, renderera i rozdzielczości; nie oznacza FPS w prawdziwej grze.
- Brak temperatury CPU/GPU, mocy, napięcia lub RPM oznacza N/D, a nie wartość zero.
- Pamięć testowana z procesu nie zastępuje pełnego offline memtestu.
- Odczyt PnP dowodzi wykrycia urządzenia przez Windows, nie sprawności fizycznej portu lub przetwornika.
- SFC /verifyonly i DISM /ScanHealth to diagnostyka bez automatycznej naprawy.

Raporty: CHECKLISTA_INTEGRACJI_HARDWARE_TEST_PRO_ULTIMATE_PL.md, TEST_REPORT_PL.txt i FUNKCJE_ZINTEGROWANE.txt
