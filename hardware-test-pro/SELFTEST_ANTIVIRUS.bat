@echo off
setlocal
cd /d "%~dp0"
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
where py >nul 2>&1
if not errorlevel 1 (py -3 "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-antivirus) else (python "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-antivirus)
if errorlevel 1 echo TEST NIEUDANY — sprawdz interpreter Python.
pause