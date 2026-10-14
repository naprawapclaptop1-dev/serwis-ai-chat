@echo off
setlocal
cd /d "%~dp0"
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
set "PY=py -3"
%PY% --version >nul 2>&1 || set "PY=python"
%PY% -m py_compile "NaprawaPC_Hardware_Test_PRO.pyw" || goto fail
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-core || goto fail
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-antivirus || goto fail
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-themes || goto fail
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-update-flow || goto fail
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-deep || goto fail
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-update || goto fail
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-launcher || goto fail
echo.
echo WSZYSTKIE TESTY ZRODLOWE ZAKONCZONE SUKCESEM.
pause
exit /b 0
:fail
echo.
echo TEST NIEUDANY. Zobacz powyzszy komunikat i BUILD_4_3_44.log.
pause
exit /b 1