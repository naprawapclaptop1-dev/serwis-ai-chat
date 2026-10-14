@echo off
setlocal EnableExtensions DisableDelayedExpansion
cd /d "%~dp0"
if exist "NAPRAWA-PC-HARDWARE-TEST-PRO.exe" (
 start "" "%~dp0NAPRAWA-PC-HARDWARE-TEST-PRO.exe"
 exit /b 0
)
if exist "dist\NAPRAWA-PC-HARDWARE-TEST-PRO-4.3.41.exe" (
 start "" "%~dp0dist\NAPRAWA-PC-HARDWARE-TEST-PRO-4.3.41.exe"
 exit /b 0
)
echo ERROR: EXE not found. Run BUILD_WINDOWS.bat first.
pause
exit /b 1