@echo off
setlocal
cd /d "%~dp0"
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
set "PY=py -3"
%PY% --version >nul 2>&1 || set "PY=python"
echo [1/10] Syntax
%PY% -m py_compile "NaprawaPC_Hardware_Test_PRO.pyw" || goto fail
echo [2/10] Core
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-core || goto fail
echo [3/10] Deep
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-deep || goto fail
echo [4/10] Update
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-update || goto fail
echo [5/10] Launcher
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-launcher || goto fail
echo [6/10] Antivirus
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-antivirus || goto fail
echo [7/10] Themes
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-themes || goto fail
echo [8/10] Service center
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-service-center || goto fail
echo [9/10] Update flow
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-update-flow || goto fail
echo [10/10] Advanced modules, sequential diagnostics and 3D crash guards
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-advanced-modules || goto fail
echo.
echo WSZYSTKIE TESTY ZRODLOWE ZAKONCZONE SUKCESEM.
pause
exit /b 0
:fail
set "ERR=%errorlevel%"
echo.
echo TEST NIEUDANY. Nie publikuj wydania. Kod bledu: %ERR%
pause
exit /b 1
