@echo off
setlocal EnableExtensions DisableDelayedExpansion
cd /d "%~dp0"
title NAPRAWA PC HARDWARE TEST PRO 4.3.41 GLOBAL UPDATE BUILD
set "LOG=%~dp0BUILD_4_3_41.log"
set "PY="
where py >nul 2>&1
if not errorlevel 1 set "PY=py -3"
if not defined PY (
  where python >nul 2>&1
  if not errorlevel 1 set "PY=python"
)
>"%LOG%" echo NAPRAWA PC HARDWARE TEST PRO 4.3.41 GLOBAL UPDATE BUILD
if not defined PY (
  echo ERROR: Python 3 x64 was not found.
  >>"%LOG%" echo ERROR: Python 3 x64 was not found.
  goto fail
)
for %%F in ("NaprawaPC_Hardware_Test_PRO.pyw" "ui_reference.png" "app.ico" "SUITE_SETUP.iss" "PUBLISH_GLOBAL_UPDATE.ps1") do if not exist %%F goto missing
echo [1/8] Python
%PY% --version >>"%LOG%" 2>&1
if errorlevel 1 goto fail
echo [2/8] Install build and hardware-test libraries
%PY% -m pip install --upgrade pyinstaller psutil pillow numpy pygame-ce PyOpenGL sounddevice opencv-python >>"%LOG%" 2>&1
if errorlevel 1 goto fail
echo [3/8] Python syntax check
%PY% -m py_compile "NaprawaPC_Hardware_Test_PRO.pyw" >>"%LOG%" 2>&1
if errorlevel 1 goto fail
echo [4/8] CPU, RAM, VRAM-helper and global-updater helper self tests
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-core >>"%LOG%" 2>&1
if errorlevel 1 goto fail
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-deep >>"%LOG%" 2>&1
if errorlevel 1 goto fail
%PY% "NaprawaPC_Hardware_Test_PRO.pyw" --selftest-update >>"%LOG%" 2>&1
if errorlevel 1 goto fail
echo [5/8] Build single EXE with GPU/camera/audio libraries
if exist "build" rmdir /s /q "build" 2>nul
if exist "dist" rmdir /s /q "dist" 2>nul
%PY% -m PyInstaller --noconfirm --clean --noconsole --onefile --name "NAPRAWA-PC-HARDWARE-TEST-PRO-4.3.41" --icon "app.ico" --add-data "ui_reference.png;." --add-data "app_icon.png;." --hidden-import psutil --hidden-import PIL --hidden-import PIL.Image --hidden-import PIL.ImageTk --hidden-import PIL.ImageOps --hidden-import numpy --hidden-import pygame --hidden-import OpenGL --hidden-import OpenGL.GL --hidden-import OpenGL.GLU --hidden-import sounddevice --hidden-import cv2 --collect-all PIL --collect-all numpy --collect-all pygame --collect-all OpenGL --collect-all sounddevice --collect-all cv2 "NaprawaPC_Hardware_Test_PRO.pyw" >>"%LOG%" 2>&1
if errorlevel 1 goto fail
if not exist "dist\NAPRAWA-PC-HARDWARE-TEST-PRO-4.3.41.exe" goto fail
echo [6/8] Create portable ZIP
mkdir "dist\NAPRAWA-PC-HARDWARE-TEST-PRO-PORTABLE" 2>nul
copy /y "dist\NAPRAWA-PC-HARDWARE-TEST-PRO-4.3.41.exe" "dist\NAPRAWA-PC-HARDWARE-TEST-PRO-PORTABLE\NAPRAWA-PC-HARDWARE-TEST-PRO.exe" >nul
if errorlevel 1 goto fail
copy /y "app.ico" "dist\NAPRAWA-PC-HARDWARE-TEST-PRO-PORTABLE\app.ico" >nul
copy /y "README_PL.txt" "dist\NAPRAWA-PC-HARDWARE-TEST-PRO-PORTABLE\README_PL.txt" >nul
copy /y "START_PROGRAM.bat" "dist\NAPRAWA-PC-HARDWARE-TEST-PRO-PORTABLE\START_PROGRAM.bat" >nul
powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'dist\NAPRAWA-PC-HARDWARE-TEST-PRO-PORTABLE\*' -DestinationPath 'dist\NAPRAWA-PC-HARDWARE-TEST-PRO-PORTABLE.zip' -Force" >>"%LOG%" 2>&1
if errorlevel 1 goto fail
echo [7/8] Build installer Setup.exe
set "ISCC="
if exist "%ProgramFiles(x86)%\Inno Setup 7\ISCC.exe" set "ISCC=%ProgramFiles(x86)%\Inno Setup 7\ISCC.exe"
if not defined ISCC if exist "%ProgramFiles%\Inno Setup 7\ISCC.exe" set "ISCC=%ProgramFiles%\Inno Setup 7\ISCC.exe"
if not defined ISCC if exist "%ProgramFiles(x86)%\Inno Setup 6\ISCC.exe" set "ISCC=%ProgramFiles(x86)%\Inno Setup 6\ISCC.exe"
if not defined ISCC if exist "%ProgramFiles%\Inno Setup 6\ISCC.exe" set "ISCC=%ProgramFiles%\Inno Setup 6\ISCC.exe"
if not defined ISCC for /f "delims=" %%I in ('where ISCC.exe 2^>nul') do set "ISCC=%%I"
if not defined ISCC (
  echo ERROR: EXE and portable ZIP were created, but Inno Setup 6/7 was not found.
  >>"%LOG%" echo ERROR: Inno Setup 6/7 was not found. Installer was not compiled.
  goto fail
)
"%ISCC%" /DAppVersion=4.3.41 "/DSourceDir=%CD%\dist" /O"%CD%\dist" "SUITE_SETUP.iss" >>"%LOG%" 2>&1
if errorlevel 1 goto fail
if not exist "dist\NAPRAWA-PC-HARDWARE-TEST-PRO-Setup-4.3.41.exe" goto fail
echo [8/8] Global publication (only if GitHub CLI is authenticated)
where gh >nul 2>&1
if errorlevel 1 goto publish_manual
 gh auth status >>"%LOG%" 2>&1
if errorlevel 1 goto publish_manual
powershell -NoProfile -ExecutionPolicy Bypass -File ".\PUBLISH_GLOBAL_UPDATE.ps1" -Version "4.3.41" -InstallerPath ".\dist\NAPRAWA-PC-HARDWARE-TEST-PRO-Setup-4.3.41.exe" >>"%LOG%" 2>&1
if errorlevel 1 goto publish_failed
echo.
echo GLOBAL UPDATE PUBLISHED: 4.3.41
goto build_done
:publish_manual
echo GLOBAL UPDATE NOT PUBLISHED: GitHub CLI is not authenticated.
echo After one-time setup, run gh auth login and run BUILD_WINDOWS.bat again.
echo Manual command: powershell -ExecutionPolicy Bypass -File .\PUBLISH_GLOBAL_UPDATE.ps1 -Version 4.3.41 -InstallerPath ".\dist\NAPRAWA-PC-HARDWARE-TEST-PRO-Setup-4.3.41.exe"
goto build_done
:publish_failed
echo WARNING: EXE and Setup were built, but global publication failed. See BUILD_4_3_41.log.
echo Do not tell clients an update is available until the manifest is marked release_ready=true.
:build_done
echo.
echo BUILD OUTPUTS:
echo EXE:       %CD%\dist\NAPRAWA-PC-HARDWARE-TEST-PRO-4.3.41.exe
echo INSTALLER: %CD%\dist\NAPRAWA-PC-HARDWARE-TEST-PRO-Setup-4.3.41.exe
echo PORTABLE:  %CD%\dist\NAPRAWA-PC-HARDWARE-TEST-PRO-PORTABLE.zip
echo LOG:       %LOG%
pause
exit /b 0
:missing
echo ERROR: Required project file is missing.
>>"%LOG%" echo ERROR: Required project file is missing.
goto fail
:fail
echo.
echo BUILD FAILED. Details: %LOG%
if exist "%LOG%" type "%LOG%"
pause
exit /b 1