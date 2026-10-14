@echo off
setlocal EnableExtensions DisableDelayedExpansion
cd /d "%~dp0"
echo Test global updater and UAC installer launch...
where py >nul 2>&1
if not errorlevel 1 (py -3 "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-update && py -3 "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-launcher) else (python "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-update && python "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-launcher)
if errorlevel 1 echo TEST FAILED
pause