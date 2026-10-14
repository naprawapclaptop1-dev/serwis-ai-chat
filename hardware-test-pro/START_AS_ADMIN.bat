@echo off
setlocal EnableExtensions DisableDelayedExpansion
cd /d "%~dp0"
set "EXE=%~dp0dist\NAPRAWA-PC-HARDWARE-TEST-PRO-4.3.37.exe"
if not exist "%EXE%" (
 echo ERROR: EXE not found. Run BUILD_WINDOWS.bat first.
 pause
 exit /b 1
)
powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process -FilePath '%EXE%' -Verb RunAs"