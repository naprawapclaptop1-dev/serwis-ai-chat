# CHECKLISTA INTEGRACJI — NAPRAWA PC HARDWARE TEST PRO

## Wydanie online 4.3.114
- [x] Windows CI zakończył się sukcesem: https://github.com/naprawapclaptop1-dev/serwis-ai-chat/actions/runs/39673844878
- [x] Setup.exe oraz ALL-IN-ONE ZIP opublikowane.
- [x] Manifest stable aktualizowany po udanej budowie i publikacji.
- [x] 15 grup katalogu i 110 unikalnych testów.
- [x] 110 odrębnych ID scen OpenGL — unikalny layout dla każdego ID.
- [x] 40 diagnostyk integracyjnych dla grup SYSTEM REPAIR PRO i SERWIS ULTIMATE (po 20 w każdej grupie).
- [x] Pełna tabela live: sensory, CPU per-core, RAM/swap, I/O i IOPS dysków, karty sieciowe i woluminy — tam, gdzie dane są dostępne.
- [x] Speed Test QUICK/STANDARD/MAX/TURBO; TURBO mierzy 4 równoległe strumienie HTTPS po potwierdzeniu i zapisuje wynik oddzielnie.
- [x] Test trybów ekranu oddzielony od EDID; audio wymaga jawnego potwierdzenia przed próbkowaniem/tonem.
- [x] Wyniki katalogu są zapisywane jako indywidualne raporty JSON.
- [x] Sensor Bridge zachowuje wykryte czujniki bez aktualnego odczytu jako N/D.

## Liczebność katalogu
- [x] CPU — 7; RAM — 7; GPU — 8; VRAM — 6; dyski — 7; ekran — 5.
- [x] Bezpieczeństwo — 4; bateria — 5; sieć — 5; USB — 4; audio — 5; klawiatura/touchpad — 4; kamera — 3.
- [x] System Repair PRO — 10 diagnostyk.
- [x] Serwis Ultimate — 10 diagnostyk.

## Diagnostyka serwisowa
- [x] Windows: wersja/status licencji, BIOS/UEFI/TPM/Secure Boot, PnP/sterowniki, Windows Update, zdarzenia błędów, usługi, storage, WinRE/BCD, usługi sieciowe, DISM CheckHealth.
- [x] Serwis: sprzęt, oprogramowanie, autostart/zadania, historia awarii, konfiguracja sieci, WMI, hotfixy, usługi automatyczne, lokalne raporty, instalacje Windows offline.
- [x] Nowe sondy są odczytowe; nie zmieniają samodzielnie konfiguracji Windows.
- [x] Istniejące centrum zachowuje SFC/DISM naprawcze, CHKDSK, DNS/Winsock, raport baterii, narzędzia Windows i offline BCD/WinRE/DISM/SFC.

## Do wykonania na rzeczywistym PC
- [ ] Przetestować UI, nawigację i wszystkie moduły na sprzęcie użytkownika.
- [ ] Potwierdzić czujniki w konkretnych sterownikach CPU/GPU/EC.
- [ ] Osobno sprawdzić audio, kamerę, matrycę, klawiaturę/touchpad i porty USB.
- [ ] Sprawdzić aktualizację nad istniejącą instalacją.
- [ ] Porównać plik po pliku wszystkie funkcje z obu ZIP-ów źródłowych, aby potwierdzić pełną zgodność 1:1. Obecne 40 sond nie jest deklaracją pełnego przeniesienia każdego ekranu i każdej funkcji.

## Granice
- CI nie potwierdza wszystkich fizycznych urządzeń ani czujników.
- RAM/VRAM testowane z procesu nie są pełnym testem wszystkich fizycznych komórek.
- FPS OpenGL nie jest prognozą FPS w konkretnej grze.
- Nowe 20 sond to integracja diagnostyczna w ramach znanego zakresu funkcji; nie jest to deklaracja pełnej kopi źródeł obu archiwów.


## Kandydat 4.3.135 — dodatkowe sondy Serwis Ultimate
- [x] Dodano 10 unikalnych sond odczytowych bez powielania istniejących 40 sond: DxDiag, drukarki/spooler, Bluetooth, historia niezawodności, punkty przywracania/migawki, BitLocker bez kluczy, funkcje opcjonalne, runtime'y .NET/VC++, profile Wi-Fi bez haseł oraz raporty/zrzuty WER.
- [x] Przycisk modułu podłączony do Centrum napraw.
- [x] Dodano selftest unikalnych ID/tytułów/poleceń i zakaz destrukcyjnych komend.
- [ ] Windows CI, instalator i ALL-IN-ONE ZIP — do potwierdzenia po uruchomieniu workflow.
- [ ] Test GUI i rzeczywistych wyników na fizycznym Windows — wymaga walidacji sprzętowej.
- [ ] Porównanie wszystkich ekranów i handlerów z oryginalnym Serwis Ultimate 1.15.3 — nadal otwarte.
