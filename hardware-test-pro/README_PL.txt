NAPRAWA PC — HARDWARE TEST PRO 4.3.41
=====================================
JEDNA APLIKACJA. Nie instaluje drugiego programu serwisowego.

NOWOŚCI 4.3.41
--------------
• Własny test RAM: 26 pełnych przebiegów obejmujących wartości stałe, naprzemienne bajty
  55/AA, wzorzec adresowy 32-bit, chodzące bity 1/0 oraz sekwencję pseudolosową.
  Program zapisuje i sprawdza każdy bajt przydzielonego bufora, pokazuje postęp i offset błędu.
• GPU/VRAM: osobny test pamięci tekstur OpenGL. Przydziela 32–256 MB tekstur w sterowniku,
  zapisuje 6 wzorców, odczytuje tekstury i porównuje wszystkie bajty. Wyniki zapisywane są
  w historii i raporcie. Nie jest to pełny test każdej fizycznej komórki VRAM.
• Telemetria GPU: nie ufa już bezwarunkowo 32-bitowemu polu Win32_VideoController.AdapterRAM,
  które na kartach z ponad 4 GB potrafi błędnie pokazywać około 4 GB. W takim wypadku pokazuje
  N/D, dopóki licznik sterownika nie poda wiarygodnej pojemności.
• Globalny aktualizator HTTPS bez pola URL. Właściciel publikuje instalator przez skrypt
  PUBLISH_GLOBAL_UPDATE.ps1; klienci nie muszą być w tej samej sieci.

Zawartość
--------
• CPU — obciążenie etapami, historia próbek zegara i raport.
• GPU — renderer OpenGL, FPS sceny, dostępna telemetria zegarów/VRAM oraz osobny test pamięci tekstur.
• RAM — własny programowy test 26 wzorców bufora.
• SSD/HDD — plik testowy odczytu/zapisu oraz SMART, gdy kontroler udostępnia dane.
• Matryca — 20 wzorców kolorów, gradienty, siatki, pasy, ruch/smużenie i EDID.
• Klawiatura i mysz — rejestracja rzeczywistych wejść zgłaszanych przez Windows.
• Kamera — podgląd; mikrofon — analiza próbki w RAM; głośniki — ton testowy i potwierdzenie słyszalności.
• Sieć, USB, bezpieczeństwo oraz narzędzia naprawy Windows w tym samym oknie.
• Raporty, historia wyników i aktualizator globalny.

WAŻNE OGRANICZENIA DIAGNOSTYKI
------------------------------
RAM: program testuje przydzielony bufor swojego procesu. Działając wewnątrz Windows nie
może przejąć pamięci używanej przez jądro i inne procesy, więc wynik nie gwarantuje sprawdzenia
każdej komórki fizycznej RAM.

VRAM: OpenGL sprawdza pamięć tekstur dostępną przez sterownik i porównuje dane odczytane z GPU.
Sterownik może zarządzać pamięcią lub stronicować zasoby; nie jest to test całej pamięci GPU.
Nieudana alokacja/nieobsługiwane OpenGL nie oznacza automatycznie uszkodzonej karty.

DANE PRODUCENTA: jeśli sterownik nie udostępnia zegarów, temperatury, ECC lub pojemności VRAM,
program pokazuje N/D, a nie zmyśloną wartość. FPS to wynik danej sceny, nie gwarantowane maksimum
każdej gry. Matryca pokazuje wzorce; martwe piksele trzeba obejrzeć wzrokowo. Test audio wymaga
odsłuchu; kamera wymaga potwierdzenia ostrości.

BUDOWANIE WINDOWS
-----------------
Wymagania: Windows 10/11 x64, Python 3 x64, Internet do pobrania bibliotek oraz Inno Setup 6/7.
1. Rozpakuj cały ZIP do folderu.
2. Uruchom BUILD_WINDOWS.bat.
3. Pliki znajdziesz w DIST:
   • NAPRAWA-PC-HARDWARE-TEST-PRO-4.3.41.exe
   • NAPRAWA-PC-HARDWARE-TEST-PRO-Setup-4.3.41.exe
   • NAPRAWA-PC-HARDWARE-TEST-PRO-PORTABLE.zip
4. Szczegóły kompilacji są zapisywane w BUILD_4_3_41.log.

AKTUALIZACJA GLOBALNA
---------------------
Aplikacja sprawdza publiczny manifest HTTPS wbudowany w program. Użytkownik nie wpisuje adresu.
Wersje 4.3.38 i starsze trzeba raz ręcznie uaktualnić do wydania z globalnym updaterem.

Aby opublikować rzeczywistą aktualizację (komputer serwisowy, nie laptop klienta):
1. Zbuduj instalator przez BUILD_WINDOWS.bat.
2. Na komputerze serwisowym skonfiguruj GitHub CLI i wykonaj jednorazowo `gh auth login`.
3. Dla tego wydania uruchom:
   .\PUBLISH_GLOBAL_UPDATE.ps1 -Version "4.3.41" -InstallerPath ".\dist\NAPRAWA-PC-HARDWARE-TEST-PRO-Setup-4.3.41.exe"
4. Skrypt umieści instalator w publicznym wydaniu i ustawi latest.json z rozmiarem oraz SHA-256.
Po publikacji komputery na całym świecie pobierają wydanie przez HTTPS, nie przez LAN.

Bez zbudowanego i opublikowanego instalatora latest.json może odpowiadać, ale nie będzie dostępna
aktualizacja do pobrania. Nie wbudowano tokenów ani haseł do aplikacji.