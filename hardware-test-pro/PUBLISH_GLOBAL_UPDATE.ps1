param(
    [Parameter(Mandatory=$true)][string]$Version,
    [Parameter(Mandatory=$true)][string]$InstallerPath,
    [string]$Notes = "NAPRAWA PC HARDWARE TEST PRO 4.3.42 — global updater UAC launch fix."
)
$ErrorActionPreference = "Stop"
$Repository = "naprawapclaptop1-dev/serwis-ai-chat"
$ManifestPath = "updates/hardware-test-pro/latest.json"
$DownloadName = "NAPRAWA-PC-HARDWARE-TEST-PRO-Setup-$Version.exe"
$Tag = "hardware-test-pro-v$Version"
if ($Version -notmatch '^\d+\.\d+\.\d+$') { throw "Wersja musi mieć format X.Y.Z." }
$InstallerPath = (Resolve-Path -LiteralPath $InstallerPath).Path
if ((Split-Path -Leaf $InstallerPath) -ne $DownloadName) { throw "Plik musi nazywać się dokładnie: $DownloadName" }
$file = Get-Item -LiteralPath $InstallerPath
if ($file.Length -lt 1MB) { throw "Plik jest za mały jak na instalator; przerwano publikowanie." }
$hash = (Get-FileHash -LiteralPath $InstallerPath -Algorithm SHA256).Hash.ToLowerInvariant()
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { throw "Brak GitHub CLI (gh). Zainstaluj GitHub CLI i wykonaj jednorazowo gh auth login na komputerze serwisowym." }
& gh auth status *> $null
if ($LASTEXITCODE -ne 0) { throw "Zaloguj komputer serwisowy: gh auth login. Token pozostaje poza kodem programu." }

# Confirm manifest exists and can be updated BEFORE making/updating a public release.
$existing = & gh api "repos/$Repository/contents/$ManifestPath" --jq .sha
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($existing)) { throw "Nie można odczytać SHA manifestu $ManifestPath; instalator nie został opublikowany." }

$release = & gh release view $Tag --repo $Repository 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "Wydanie $Tag już istnieje — aktualizuję asset o tej samej nazwie, aby ponowienie po błędzie było bezpieczne."
    & gh release upload $Tag $InstallerPath --repo $Repository --clobber
} else {
    Write-Host "Publikowanie nowego globalnego wydania $Version..."
    & gh release create $Tag $InstallerPath --repo $Repository --title "NAPRAWA PC HARDWARE TEST PRO $Version" --notes $Notes
}
if ($LASTEXITCODE -ne 0) { throw "Nie udało się opublikować pliku instalatora w publicznym wydaniu GitHub." }

$manifest = [ordered]@{
    app = "NAPRAWA PC HARDWARE TEST PRO"
    channel = "stable"
    version = $Version
    release_ready = $true
    filename = $DownloadName
    download_url = "https://github.com/$Repository/releases/download/$Tag/$DownloadName"
    sha256 = $hash
    size = [long]$file.Length
    minimum_supported_version = "4.3.39"
    notes = $Notes
    published_at = [DateTime]::UtcNow.ToString("o")
}
$json = $manifest | ConvertTo-Json -Depth 8
$contentBase64 = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($json))
& gh api --method PUT "repos/$Repository/contents/$ManifestPath" `
    -f message="Publish Hardware Test PRO $Version global update" `
    -f content="$contentBase64" -f sha="$existing" -f branch="main" | Out-Null
if ($LASTEXITCODE -ne 0) { throw "Wydanie istnieje, ale aktualizacja manifestu nie powiodła się. Popraw uprawnienia GitHub i uruchom ten sam skrypt ponownie — podmieni ten sam asset i ponowi manifest." }
Write-Host ""
Write-Host "OPUBLIKOWANO GLOBALNIE: $Version"
Write-Host "SHA-256: $hash"
Write-Host "Rozmiar: $($file.Length) bajtów"
Write-Host "Komputery z aktualizatorem pobierają instalator przez HTTPS; nie wpisuje się żadnych linków."