@echo off
setlocal
cd /d "%~dp0"
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
set PY=py -3
%PY% --version >nul 2>&1 || set PY=python
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-themes || goto fail
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-update-flow || goto fail
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-antivirus || goto fail
echo OK: SKORKI / AKTUALIZACJA / ANTYWIRUS
pause
exit /b 0
:fail
echo TEST NIEUDANY
pause
exit /b 1