# Macierz parytetu źródeł — Hardware Test PRO + System Repair PRO + Serwis Ultimate

Wersja robocza dla kandydata 4.3.124. Ta macierz jest listą kontroli, a nie deklaracją ukończenia. Moduł można oznaczyć jako zakończony dopiero po wskazaniu handlera źródłowego, wejścia z UI, wyniku/raportu oraz przejściu testu.

## A. System Repair PRO 5.6.25 — archiwum źródłowe użytkownika

Plik źródłowy: `NAPRAWA_PC_SYSTEM_REPAIR_PRO_5.6.25_RAM_LIVE_DASHBOARD_ULTIMATE_FULL_PROJECT.zip` (166 715 344 B).

| Obszar | Aktualna integracja w Hardware Test PRO | Wymagane potwierdzenie |
|---|---|---|
| Panel główny i nawigacja | Częściowo: wspólne centrum napraw i katalog modułów | Porównać wszystkie ekrany, przyciski i akcje z MainWindow.xaml / MainWindow.xaml.cs |
| Diagnostyka Windows | Częściowo: odczytowe skany i 20 pozycji katalogu System Repair PRO | Zmapować każdą procedurę źródłową na unikalny handler i test |
| Profile problemów | Częściowo: 14 profili objawów | Porównać pełną listę profili, kroki i polecenia z oryginałem |
| SFC / DISM / CHKDSK | Dostępne skróty/akcje diagnostyczne w centrum napraw | Testować osobno, sprawdzić kody wyjścia, logi, UAC i anulowanie |
| Sieć / DNS / Winsock | Częściowo: diagnostyka sieci i skróty do narzędzi Windows | Sprawdzić wszystkie akcje, raport przed/po i obsługę błędów |
| Sterowniki i aktualizacje | Częściowo: narzędzia Windows i własny updater Hardware Test PRO | Porównać aktualizator, źródła, rollback i obsługę błędów aplikacji źródłowej |
| BIOS / UEFI / licencja | Niepotwierdzona zgodność 1:1 | Przenieść odczytowe funkcje źródłowe i testować na Windows |
| Raporty i logi napraw | Częściowo: logi, JSON/HTML, baza wiedzy | Porównać pola, formaty, eksport i historię |
| Baza wiedzy / PDF | Częściowo: lokalny import, deduplikacja i wyszukiwanie | Porównać wszystkie źródłowe funkcje importu, wyszukiwania i zapisu |
| Aktualizator System Repair PRO | Niepotwierdzona parzystość | Sprawdzić pełny AppUpdateService i nie mieszać go z updaterem Hardware Test PRO |
| UAC / bezpieczeństwo napraw | Częściowo: część akcji wymaga potwierdzenia | Sprawdzić każdą operację naprawczą, uprawnienia, rollback i brak destrukcyjnych akcji bez zgody |

## B. Serwis Ultimate 1.15.3 — archiwum źródłowe użytkownika

Plik źródłowy: `NAPRAWA_PC_SERWIS_ULTIMATE_v1_15_3_FIX (2).zip` (5 710 073 B).

| Ekran / funkcja źródłowa | Aktualna integracja w Hardware Test PRO | Wymagane potwierdzenie |
|---|---|---|
| ShowDashboard | Wspólny pulpit Hardware Test PRO | Porównać wszystkie kafle i akcje |
| ShowHardware | Częściowo: inwentarz i testy sprzętu | Zweryfikować każdy typ urządzenia i raport |
| ShowDisks / SMART | Częściowo: testy dysków i dostępne SMART/reliability | Sprawdzić wszystkie widoki, woluminy, ostrzeżenia i eksport |
| ShowLaptop | Częściowo: bateria, zasilanie i peryferia | Sprawdzić modele laptopów, baterię, ACPI i brak baterii w PC |
| ShowWindows | Częściowo: centrum napraw i narzędzia Windows | Porównać wszystkie źródłowe procedury |
| ShowGameTroubleshooting | Niepotwierdzona parzystość | Zidentyfikować wszystkie akcje i bezpieczne testy |
| ShowSecurity | Częściowo: audyt Windows/Defender/autostart | Porównać skany, wyniki i raporty |
| ShowNetwork | Częściowo: interfejsy i Speed Test | Porównać wszystkie testy sieciowe i raporty |
| ShowProcesses | Niepotwierdzona parzystość | Dodać widok procesów, filtrowanie i bezpieczne akcje, jeśli są w źródle |
| ShowJobs | Częściowo: lokalna historia zleceń i eksport HTML | Porównać pola, statusy, edycję, usuwanie, eksport i historię |
| ShowReports | Częściowo: raporty JSON/HTML/CSV | Porównać wszystkie raporty i ich zawartość |
| USB / audio / obraz / sieć | Częściowo: niezależne testy i enumeracja | Zweryfikować każdą funkcję na fizycznym urządzeniu |
| Laboratorium zasilania | Częściowo: 7 akcji raportowych Windows | Porównać wszystkie polecenia i wyniki z oryginałem |
| Formularz zlecenia / karta klienta | Częściowo: lokalny zapis i HTML | Porównać wszystkie pola, zgody i eksport |

## C. Hardware Test PRO — wymagania wspólne

- [ ] Każdy test ma osobny ekran, handler, postęp, wynik i raport.
- [ ] Każdy z 110 wpisów katalogu ma własne ID sceny; unikalność ID nie zastępuje wizualnej kontroli geometrii.
- [ ] Sceny 3D wykonują rzeczywisty OpenGL, synchronizują pomiar i pokazują FPS/renderer/rozdzielczość; brak renderera oznacza WARN, nie PASS.
- [ ] Pełny inspektor sensorów pokazuje wszystkie rekordy udostępnione przez Sensor Bridge/Windows, wraz z N/D, wyszukiwaniem i eksportem CSV.
- [ ] Speed Test raportuje medianę, peak, minimum, jitter, zmienność, poprawne próbki i bajty transferu; wynik równoległy TURBO pozostaje osobny.
- [ ] Naprawy wymagające uprawnień, zmian systemu lub potencjalnie destrukcyjnych działań mają jasne potwierdzenie i log.
- [ ] Build Windows x64, instalator EXE, ALL-IN-ONE ZIP, manifest i SHA-256 są zgodne.
- [ ] Poza CI trzeba wykonać test na fizycznym PC: temperatury, wentylatory, moc, VRAM, ekran, bateria i peryferia.

## D. Ograniczenia dowodowe

Archiwa 5.6.25 i 1.15.3 zostały wskazane w bibliotece użytkownika. W tej sesji plik System Repair PRO o rozmiarze 166,7 MB nie został udostępniony do rozpakowania przez lokalny builder, więc nie można uczciwie potwierdzić zgodności 1:1 każdej klasy i metody. Kod istniejących integracji i katalogów nie jest dowodem pełnej parytetu z oryginałami. Nie oznaczać całej integracji jako zakończonej, dopóki macierz nie zostanie wypełniona na podstawie zawartości obu źródeł i testów.
