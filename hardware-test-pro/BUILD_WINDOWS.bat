@echo off
setlocal EnableExtensions
cd /d "%~dp0"
title NAPRAWA PC HARDWARE TEST PRO - BUILD LOKALNY
echo.
echo NAPRAWA PC HARDWARE TEST PRO - BUILD LOKALNY
echo Wersja zostanie odczytana ze zrodla. Ten skrypt NIE publikuje aktualizacji stable.
echo.
where powershell.exe >nul 2>&1
if errorlevel 1 (
  echo BLAD: Brak Windows PowerShell.
  exit /b 1
)
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0BUILD_LOCAL.ps1"
set "RC=%ERRORLEVEL%"
echo.
if not "%RC%"=="0" (
  echo BUILD NIEUDANY. Szczegoly: %~dp0BUILD_LOCAL.log
) else (
  echo BUILD ZAKONCZONY. Pliki znajduja sie w folderze dist.
)
pause
exit /b %RC%
