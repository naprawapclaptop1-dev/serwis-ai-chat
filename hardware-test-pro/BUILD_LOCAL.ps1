# Version-aware local Windows build. Never publish or change the stable manifest.
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
$log = Join-Path $PSScriptRoot "BUILD_LOCAL.log"
Start-Transcript -LiteralPath $log -Force | Out-Null
$tempIss = $null
try {
    $required = @("NaprawaPC_Hardware_Test_PRO.pyw","ui_reference.png","app_icon.png","app.ico",
        "SUITE_SETUP.iss","SensorBridge\HardwareSensorBridge.csproj","README_PL.txt")
    $missing = @($required | Where-Object { !(Test-Path -LiteralPath $_) })
    if ($missing.Count) {
        throw ("Brak wymaganych plikow zrodla: " + ($missing -join ", ") +
            ". Uzyj pelnego repozytorium/checkout, nie samego folderu dist.")
    }
    $source = [IO.File]::ReadAllText((Join-Path $PSScriptRoot "NaprawaPC_Hardware_Test_PRO.pyw"), [Text.Encoding]::UTF8)
    $versions = [regex]::Matches($source, '(?m)^VERSION = "(\d+\.\d+\.\d+)(?: [^"]*)?"\s*$')
    if ($versions.Count -eq 0) { throw "Nie mozna odczytac wersji zrodla. Build zatrzymany." }
    $appVersion = $versions[$versions.Count - 1].Groups[1].Value
    if ($appVersion -notmatch '^\d+\.\d+\.\d+$') { throw "Nieprawidlowy format wersji: $appVersion" }
    $exeName = "NAPRAWA-PC-HARDWARE-TEST-PRO-$appVersion.exe"
    $setupName = "NAPRAWA-PC-HARDWARE-TEST-PRO-Setup-$appVersion.exe"
    $bundleName = "NAPRAWA-PC-HARDWARE-TEST-PRO-ALL-IN-ONE-$appVersion.zip"
    Write-Host "Build lokalny wersji $appVersion. Manifest stable pozostaje bez zmian."

    $pythonCommand = $null; $pythonPrefix = @()
    if (Get-Command py.exe -ErrorAction SilentlyContinue) {
        $pythonCommand = "py.exe"; $pythonPrefix = @("-3")
    } elseif (Get-Command python.exe -ErrorAction SilentlyContinue) {
        $pythonCommand = "python.exe"
    } else { throw "Nie znaleziono Python 3 x64." }
    $arch = & $pythonCommand @pythonPrefix -c "import struct; print(struct.calcsize('P')*8)"
    if ($LASTEXITCODE -ne 0 -or "$arch".Trim() -ne "64") { throw "Wymagany jest Python x64. Wykryto: $arch bit." }
    & $pythonCommand @pythonPrefix --version
    if ($LASTEXITCODE -ne 0) { throw "Nie udalo sie uruchomic Python." }

    Write-Host "[1/8] Zaleznosci Python"
    & $pythonCommand @pythonPrefix -m pip install --upgrade pyinstaller psutil pillow numpy pygame-ce PyOpenGL sounddevice opencv-python cryptography
    if ($LASTEXITCODE -ne 0) { throw "Instalacja zaleznosci Python nie powiodla sie." }

    Write-Host "[2/8] Sensor Bridge (.NET 10)"
    if (!(Get-Command dotnet.exe -ErrorAction SilentlyContinue)) { throw "Brak dotnet.exe/.NET SDK 10." }
    & dotnet publish ".\SensorBridge\HardwareSensorBridge.csproj" -c Release -r win-x64 --self-contained true /p:PublishSingleFile=true -o ".\SensorBridge\publish"
    if ($LASTEXITCODE -ne 0) { throw "Build Sensor Bridge nie powiodl sie." }
    $bridge = Join-Path $PSScriptRoot "SensorBridge\publish\NAPRAWA-PC-HARDWARE-SENSOR-BRIDGE.exe"
    if (!(Test-Path -LiteralPath $bridge) -or (Get-Item -LiteralPath $bridge).Length -lt 1MB) {
        throw "Sensor Bridge EXE jest brakujacy lub niekompletny."
    }

    Write-Host "[3/8] Skladnia Python"
    & $pythonCommand @pythonPrefix -m py_compile ".\NaprawaPC_Hardware_Test_PRO.pyw"
    if ($LASTEXITCODE -ne 0) { throw "Kontrola skladni Python nie powiodla sie." }

    Write-Host "[4/8] Selftesty"
    $checks = @("--selftest-core","--selftest-deep","--selftest-update","--selftest-launcher",
        "--selftest-antivirus","--selftest-themes","--selftest-service-center",
        "--selftest-update-flow","--selftest-advanced-modules")
    foreach ($check in $checks) {
        Write-Host "SELFTEST: $check"
        & $pythonCommand @pythonPrefix ".\NaprawaPC_Hardware_Test_PRO.pyw" $check
        if ($LASTEXITCODE -ne 0) { throw "Selftest $check nie powiodl sie (kod $LASTEXITCODE)." }
    }

    Write-Host "[5/8] EXE"
    $dist = Join-Path $PSScriptRoot "dist"
    New-Item -ItemType Directory -Path $dist -Force | Out-Null
    $exePath = Join-Path $dist $exeName
    $pyinstallerArgs = @("-m","PyInstaller","--noconfirm","--clean","--noconsole","--onefile",
        "--name",("NAPRAWA-PC-HARDWARE-TEST-PRO-"+$appVersion),"--icon",".\app.ico",
        "--add-data","ui_reference.png;.","--add-data","app_icon.png;.",
        "--add-binary",($bridge+";."),
        "--hidden-import","psutil","--hidden-import","PIL","--hidden-import","PIL.Image",
        "--hidden-import","PIL.ImageTk","--hidden-import","PIL.ImageOps","--hidden-import","numpy",
        "--hidden-import","pygame","--hidden-import","OpenGL","--hidden-import","OpenGL.GL",
        "--hidden-import","OpenGL.GLU","--hidden-import","sounddevice","--hidden-import","cv2",
        "--hidden-import","cryptography","--hidden-import","cryptography.fernet",
        "--hidden-import","cryptography.hazmat.primitives.kdf.pbkdf2",
        "--collect-all","PIL","--collect-all","numpy","--collect-all","pygame",
        "--collect-all","OpenGL","--collect-all","sounddevice","--collect-all","cv2",
        "--collect-all","cryptography",".\NaprawaPC_Hardware_Test_PRO.pyw")
    & $pythonCommand @pythonPrefix @pyinstallerArgs
    if ($LASTEXITCODE -ne 0 -or !(Test-Path -LiteralPath $exePath)) { throw "PyInstaller nie utworzyl $exeName." }

    Write-Host "[6/8] Wersja pliku Inno Setup"
    $iss = [IO.File]::ReadAllText((Join-Path $PSScriptRoot "SUITE_SETUP.iss"), [Text.Encoding]::UTF8)
    $iss = [regex]::Replace($iss, '(?m)^(\s*#define AppVersion\s+")\d+\.\d+\.\d+(".*)$',
        [System.Text.RegularExpressions.MatchEvaluator]{param($m) $m.Groups[1].Value+$appVersion+$m.Groups[2].Value}, 1)
    $iss = [regex]::Replace($iss, '(?m)^(\s*#define ExeName\s+"NAPRAWA-PC-HARDWARE-TEST-PRO-)\d+\.\d+\.\d+(\.exe".*)$',
        [System.Text.RegularExpressions.MatchEvaluator]{param($m) $m.Groups[1].Value+$appVersion+$m.Groups[2].Value}, 1)
    $expectedDefine = '#define ExeName "NAPRAWA-PC-HARDWARE-TEST-PRO-' + $appVersion + '.exe"'
    if (!$iss.Contains($expectedDefine)) { throw "Nie zsynchronizowano nazwy EXE w skrypcie Inno Setup." }
    $tempIss = Join-Path $PSScriptRoot ("SUITE_SETUP.local." + $PID + ".iss")
    [IO.File]::WriteAllText($tempIss, $iss, [Text.UTF8Encoding]::new($false))

    Write-Host "[7/8] Setup.exe"
    $iscc = (Get-Command "ISCC.exe" -ErrorAction SilentlyContinue).Source
    $pf86 = [Environment]::GetEnvironmentVariable("ProgramFiles(x86)")
    $pf = [Environment]::GetEnvironmentVariable("ProgramFiles")
    if (!$iscc -and (Test-Path "$pf86\Inno Setup 6\ISCC.exe")) { $iscc = "$pf86\Inno Setup 6\ISCC.exe" }
    if (!$iscc -and (Test-Path "$pf\Inno Setup 6\ISCC.exe")) { $iscc = "$pf\Inno Setup 6\ISCC.exe" }
    if (!$iscc -and (Test-Path "$pf86\Inno Setup 7\ISCC.exe")) { $iscc = "$pf86\Inno Setup 7\ISCC.exe" }
    if (!$iscc -and (Test-Path "$pf\Inno Setup 7\ISCC.exe")) { $iscc = "$pf\Inno Setup 7\ISCC.exe" }
    if (!$iscc) { throw "Brak ISCC.exe. Zainstaluj Inno Setup 6/7." }
    & $iscc "/DAppVersion=$appVersion" "/DSourceDir=$dist" "/O$dist" $tempIss
    if ($LASTEXITCODE -ne 0) { throw "Inno Setup nie skompilowal instalatora." }
    $installer = Join-Path $dist $setupName
    if (!(Test-Path -LiteralPath $installer) -or (Get-Item -LiteralPath $installer).Length -lt 1MB) { throw "Instalator jest brakujacy lub niekompletny." }

    Write-Host "[8/8] ALL-IN-ONE i SHA-256"
    $bundle = Join-Path $dist $bundleName
    if (Test-Path -LiteralPath $bundle) { Remove-Item -LiteralPath $bundle -Force }
    $packageFiles = @($installer,$exePath,(Join-Path $PSScriptRoot "README_PL.txt"),
        (Join-Path $PSScriptRoot "app.ico"),(Join-Path $PSScriptRoot "NaprawaPC_Hardware_Test_PRO.pyw"))
    foreach ($file in $packageFiles) { if (!(Test-Path -LiteralPath $file)) { throw "Brak pliku pakietu: $file" } }
    Compress-Archive -Path $packageFiles -DestinationPath $bundle -CompressionLevel Optimal
    if (!(Test-Path -LiteralPath $bundle) -or (Get-Item -LiteralPath $bundle).Length -lt 100MB) { throw "Pakiet ALL-IN-ONE ZIP jest niekompletny." }
    Write-Host "BUILD LOCAL OK — wersja $appVersion"
    Write-Host "EXE: $exePath"
    Write-Host "SETUP: $installer"
    Write-Host "ALL-IN-ONE: $bundle"
    Write-Host ("SETUP SHA256: " + (Get-FileHash -LiteralPath $installer -Algorithm SHA256).Hash.ToLowerInvariant())
    Write-Host ("ZIP SHA256: " + (Get-FileHash -LiteralPath $bundle -Algorithm SHA256).Hash.ToLowerInvariant())
    Write-Host "Manifest stable nie zostal zmieniony. Niczego nie opublikowano."
}
catch {
    Write-Error $_
    exit 1
}
finally {
    if ($tempIss -and (Test-Path -LiteralPath $tempIss)) { Remove-Item -LiteralPath $tempIss -Force -ErrorAction SilentlyContinue }
    try { Stop-Transcript | Out-Null } catch {}
}
