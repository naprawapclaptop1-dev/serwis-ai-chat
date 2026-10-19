NAPRAWA PC HARDWARE TEST PRO — PAKIET ŹRÓDŁOWY
================================================

WERSJA / KANAŁ STABLE
To repozytorium źródłowe i materiały do lokalnego builda. Aktualną wersję publiczną odczytuj z updates/hardware-test-pro/latest.json. Ostatnie zweryfikowane wydanie przed tą aktualizacją dokumentacji: 4.3.98 (19.10.2026). Numer następnego builda online jest nadawany automatycznie — nie wpisuj go ręcznie.

ZAKRES FUNKCJI
- 125 motywów UI; wyszukiwarka i podgląd skórki.
- 13 grup laboratoriów i 70 niezależnych pozycji katalogu testów:
  CPU (7), RAM (7), GPU (8), VRAM (6), dyski (7), ekran/EDID (5),
  bezpieczeństwo Windows (4), bateria (5), sieć (5), USB (4), audio (5),
  klawiatura/touchpad (4), kamera (3).
- Każdy wpis katalogu prowadzi do oddzielnego ekranu testu, własnego uruchomienia i raportu.
- CPU: skan, obciążenie i przepustowość SHA-256 single/multi-thread.
- RAM: skan stanu systemu i wzorce/benchmark bufora z kontrolą danych; nie dowodzi to sprawdzenia wszystkich fizycznych komórek.
- GPU: 60 nazwanych scen OpenGL, pojedyncza scena i zestawy benchmarkowe. FPS zależy od GPU, sterownika i rozdzielczości.
- VRAM: inwentarz i testy alokacji/readback tekstur; ograniczenia sterownika są raportowane.
- Dyski: skan woluminu, dostępne dane reliability/SMART i benchmark plikowy z tymczasowym plikiem usuwanym po teście.
- Ekran: skan EDID oraz oddzielny odczyt bieżących/udostępnionych trybów ekranu.
- Sieć: adaptery, DNS/HTTPS, transfer download/upload i pomiary opóźnień opisane zgodnie z metodą.
- Peryferia: USB, audio, klawiatura/touchpad i kamera; testy interaktywne wskazują potrzebne potwierdzenie.
- Centrum Serwis Ultimate / System Repair PRO, raporty, aktualizator globalny HTTPS i pomocniczy Sensor Bridge.

BUDOWANIE LOKALNE
1. Wypakuj pełne repozytorium źródłowe. Wymagane są: NaprawaPC_Hardware_Test_PRO.pyw, ui_reference.png, app_icon.png, app.ico, SUITE_SETUP.iss, folder SensorBridge i powiązane zasoby.
2. Na Windows 10/11 x64 zainstaluj Python 3 x64, .NET SDK 10 i Inno Setup 6/7.
3. Uruchom BUILD_WINDOWS.bat. Skrypt odczytuje wersję ze źródła, uruchamia selftesty, buduje Sensor Bridge, EXE, Setup oraz pakiet ALL-IN-ONE.
4. Lokalny skrypt NIE publikuje do GitHub ani NIE zmienia manifestu stable. Publikację wersji online wykonuje zweryfikowany workflow GitHub Actions.
5. Wyniki trafiają do folderu dist, a log do BUILD_LOCAL.log. W razie niepowodzenia skrypt zwraca kod błędu.

TESTY I GRANICE
- Sukces CI potwierdza wyłącznie kroki i selftesty zapisane w workflow. Nie zastępuje testu sprzętu użytkownika.
- Temperatura, moc, zegary, wentylatory, VRAM i użycie GPU zależą od czujników, sterowników i Sensor Bridge. Brak danych musi pozostać N/D, bez zgadywania.
- RAM/VRAM testowane z poziomu procesu nie są pełnym testem wszystkich fizycznych komórek.
- Test audio, kamery, klawiatury i matrycy może wymagać potwierdzenia operatora. Samo wykrycie urządzenia nie potwierdza sprawności fizycznej.
- Speed Test przesyła rzeczywiste dane i zależy od sieci oraz endpointu.
- Schemat 3D jest wizualizacją edukacyjną; nie jest benchmarkiem, jeśli dany test nie wykonuje rzeczywistego pomiaru.

KANAŁ ONLINE
Manifest stable: updates/hardware-test-pro/latest.json
Wydania i instalatory: https://github.com/naprawapclaptop1-dev/serwis-ai-chat/releases
Manifest aktualizuje workflow wyłącznie po poprawnych testach, kompilacji Setup.exe i publikacji assetów.
