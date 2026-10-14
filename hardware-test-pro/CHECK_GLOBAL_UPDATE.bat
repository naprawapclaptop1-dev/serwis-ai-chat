@echo off
setlocal EnableExtensions DisableDelayedExpansion
cd /d "%~dp0"
echo Checking global NAPRAWA PC update endpoint...
where py >nul 2>&1
if not errorlevel 1 (py -3 "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-global-online) else (python "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-global-online)
echo.
pause