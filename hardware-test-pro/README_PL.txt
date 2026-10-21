NAPRAWA PC HARDWARE TEST PRO — WINDOWS x64 / ALL-IN-ONE
==========================================================

KANAŁ ONLINE
Aktualna wersja jest publikowana w updates/hardware-test-pro/latest.json.
Ostatnie zweryfikowane wydanie: 4.3.112, opublikowane 2026-10-21.
Instalator i pełny pakiet ALL-IN-ONE są dostępne w GitHub Releases:
https://github.com/naprawapclaptop1-dev/serwis-ai-chat/releases

KATALOG DIAGNOSTYCZNY
- 15 grup i 90 odrębnych pozycji katalogu. Każdy wpis ma osobny ekran, własną procedurę i raport JSON.
- CPU (7), RAM (7), GPU (8), VRAM (6), dyski (7), ekran/EDID (5), bezpieczeństwo Windows (4), bateria (5), sieć (5), USB (4), audio (5), klawiatura/touchpad (4), kamera (3), System Repair PRO (10), Serwis Ultimate (10).
- 90 unikalnych przypisań scen OpenGL dla katalogu; 30 bazowych rodzin geometrii z różnymi układami i animacją. Scena 3D jest odrębną wizualizacją i nie zastępuje wyniku testu sprzętowego.
- 125 odrębnych motywów UI z różnymi układami, gęstością, kartami, wykresami i przyciskami.
- Każda procedura zapisuje swój wynik. N/D lub ostrzeżenie nie jest przedstawiane jako zaliczenie.

CPU / RAM / GPU / DYSKI
- CPU: identyfikacja, obciążenie oraz benchmark przepustowości SHA-256 single/multi-thread.
- RAM: odczyt stanu pamięci oraz wzorce i benchmarki bufora z kontrolą danych; nie jest to pełny test wszystkich fizycznych komórek.
- GPU/VRAM: odrębne sceny OpenGL mierzące rzeczywiste FPS, zestawy 90 scen i testy alokacji/readback tekstur. Wynik zależy od GPU, sterownika i konfiguracji.
- Dyski: odczyt woluminów, dostępnych rekordów reliability/SMART oraz benchmark plikowy z plikiem tymczasowym usuwanym po teście.
- Ekran: EDID jest oddzielony od odczytu trybów; wizualna ocena martwych pikseli wymaga obserwacji operatora.

TELEMETRIA LIVE
Tabela łączy czujniki z Sensor Bridge z odczytami systemowymi, jeśli są dostępne: temperatury, napięcia, zegary, wentylatory, moc, obciążenie CPU na rdzeń, RAM/swap, I/O i IOPS dysków, transfer kart sieciowych, woluminy/partycje oraz inne zgłoszone sensory. Brak danych sterownika oznacza N/D; aplikacja nie zgaduje odczytów.

SPEED TEST
- Profil QUICK (mniejszy transfer), STANDARD (adaptacyjny) i MAX (dłuższe próbki; prosi o zgodę przed większym transferem).
- Pomiar używa rzeczywistych odpowiedzi HTTP, wielu próbek download/upload oraz czasu odpowiedzi. Nie jest to test sieci LAN bez transferu; wynik zależy od łącza i endpointu.
- Wyniki zawierają profil, próbki i podsumowanie; historia jest zapisywana lokalnie.

SYSTEM REPAIR PRO / SERWIS ULTIMATE
Dodatkowe 20 testów odczytowych: wersja i status licencji Windows (bez kluczy), BIOS/UEFI/Secure Boot/TPM, PnP i sterowniki, stan Windows Update, błędy dziennika, usługi krytyczne, woluminy/nośniki, BCD/WinRE, usługi sieciowe, DISM CheckHealth, inwentarz sprzętu i oprogramowania, autostart/zadania, historia awarii, konfiguracja IP/DNS, WMI, lista hotfixów, usługi automatyczne, lokalne raporty i wykrywanie instalacji Windows na widocznych woluminach. Każdy ma swój raport. Test DISM CheckHealth wymaga potwierdzenia i nie naprawia automatycznie.
Centrum serwisu zawiera także istniejące narzędzia SFC/DISM RestoreHealth, CHKDSK, DNS/Winsock, raport baterii, narzędzia Windows, offline DISM/SFC, BCD/WinRE oraz lokalne szyfrowane zgłoszenia.

BUDOWANIE LOKALNE
1. Użyj pełnego checkoutu repozytorium z NaprawaPC_Hardware_Test_PRO.pyw, zasobami graficznymi, SUITE_SETUP.iss i folderem SensorBridge.
2. Wymagane: Windows 10/11 x64, Python 3 x64, .NET SDK 10 oraz Inno Setup 6/7.
3. Uruchom BUILD_WINDOWS.bat. Skrypt buduje lokalnie z aktualnej wersji źródła i NIE publikuje release ani nie modyfikuje manifestu stable.
4. Wyniki trafiają do dist, a log do BUILD_LOCAL.log. Publikację online wykonuje GitHub Actions po zaliczeniu selftestów i kompilacji instalatora.

WAŻNE GRANICE
- Windows CI potwierdza określone testy i budowę; nie jest testem fizycznego komputera użytkownika.
- Temperatura, moc, wentylatory, napięcia, zegary i VRAM zależą od sterowników oraz sensorów faktycznie dostępnych na danym sprzęcie.
- Testy RAM/VRAM wykonywane z poziomu procesu nie gwarantują sprawdzenia wszystkich fizycznych komórek.
- Wyniki scen OpenGL nie przewidują FPS każdej gry; edukacyjny symulator nie jest pomiarem, jeśli jego test nie wykonuje realnego renderowania.
- Wydanie 4.3.112 dodaje 20 diagnostycznych sond opartych na zakresie tych aplikacji. Nie jest to potwierdzenie pełnej kopii 1:1 każdego wewnętrznego modułu z archiwów System Repair PRO 5.6.25 i Serwis Ultimate 1.15.3; kompletna zgodność źródłowa wymaga osobnego przeglądu wszystkich plików tych projektów.
