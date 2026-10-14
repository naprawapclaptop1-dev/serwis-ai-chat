param([Parameter(Mandatory=$true)][string]$Version)
$ErrorActionPreference = "Stop"
if ($Version -notmatch '^\d+\.\d+\.\d+$') { throw 'Podaj wersję w formacie X.Y.Z, np. 4.3.42' }
$source = Join-Path $PSScriptRoot 'NaprawaPC_Hardware_Test_PRO.pyw'
if (-not (Test-Path -LiteralPath $source)) { throw "Brak pliku źródłowego: $source" }
$utf8 = [System.Text.UTF8Encoding]::new($false)
$py = [System.IO.File]::ReadAllText($source, [System.Text.Encoding]::UTF8)
$match = [regex]::Match($py, '(?m)^VERSION = "(?<version>\d+\.\d+\.\d+) (?<description>[^"]*GLOBAL HTTPS UPDATER[^"]*)"$')
if (-not $match.Success) { throw 'Nie znaleziono wpisu VERSION głównej aplikacji; nie zmieniono plików.' }
$currentVersion = $match.Groups['version'].Value
$newLine = 'VERSION = "' + $Version + ' ' + $match.Groups['description'].Value + '"'
$updated = [regex]::Replace($py, '(?m)^VERSION = "\d+\.\d+\.\d+ [^"]*GLOBAL HTTPS UPDATER[^"]*"$', [System.Text.RegularExpressions.MatchEvaluator]{ param($m) $newLine }, 1)
if ($updated -eq $py) { throw 'Nie zmieniono wpisu VERSION; przerwano.' }
[System.IO.File]::WriteAllText($source, $updated, $utf8)
$files = @('BUILD_WINDOWS.bat','SUITE_SETUP.iss','README_PL.txt','START_PROGRAM.bat','FUNKCJE_ZINTEGROWANE.txt','TEST_REPORT_PL.txt','AKTUALIZACJA_INNY_PC_PL.txt','LATEST_JSON_EXAMPLE.json')
foreach ($file in $files) {
    $path = Join-Path $PSScriptRoot $file
    if (-not (Test-Path -LiteralPath $path)) { continue }
    $text = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
    $text = $text.Replace($currentVersion, $Version)
    $text = $text.Replace($currentVersion.Replace('.', '_'), $Version.Replace('.', '_'))
    [System.IO.File]::WriteAllText($path, $text, $utf8)
}
Write-Host "Zmieniono projekt na wersję $Version."
Write-Host '1) Uruchom BUILD_WINDOWS.bat.'
Write-Host '2) Opublikuj wydanie globalne, po zalogowaniu GitHub CLI:'
Write-Host "   .\PUBLISH_GLOBAL_UPDATE.ps1 -Version $Version -InstallerPath .\dist\NAPRAWA-PC-HARDWARE-TEST-PRO-Setup-$Version.exe"