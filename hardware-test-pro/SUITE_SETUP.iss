#ifndef AppVersion
  #define AppVersion "4.3.44"
#endif
#ifndef SourceDir
  #define SourceDir "dist"
#endif
#define AppName "NAPRAWA PC HARDWARE TEST PRO"
#define ExeName "NAPRAWA-PC-HARDWARE-TEST-PRO-4.3.44.exe"

[Setup]
AppId={{BC4F6B0C-0B6A-43FD-91E8-68FE0D2B9512}
AppName={#AppName}
AppVersion={#AppVersion}
AppVerName={#AppName} {#AppVersion}
AppPublisher=NAPRAWA PC - Serwis Rafal Jarosz
DefaultDirName={autopf64}\NAPRAWA PC\Hardware Test PRO
DefaultGroupName=NAPRAWA PC\Hardware Test PRO
OutputBaseFilename=NAPRAWA-PC-HARDWARE-TEST-PRO-Setup-{#AppVersion}
SetupIconFile={#SourceDir}\..\app.ico
UninstallDisplayIcon={app}\{#ExeName}
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=admin
WizardStyle=modern
Compression=lzma2/ultra64
SolidCompression=yes
DisableProgramGroupPage=yes
CloseApplications=yes
OutputDir=dist

[Languages]
Name: "polish"; MessagesFile: "compiler:Languages\Polish.isl"

[Tasks]
Name: "desktopicon"; Description: "Utworz ikone programu na pulpicie"; GroupDescription: "Dodatkowe ikony:"; Flags: unchecked

[InstallDelete]
; After terminating the old app, remove previous versioned executables before copying the current one.
Type: files; Name: "{app}\NAPRAWA-PC-HARDWARE-TEST-PRO-*.exe"
Type: filesandordirs; Name: "{app}\Companions\SystemRepairPRO"

[Files]
Source: "{#SourceDir}\{#ExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "README_PL.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "{#SourceDir}\Companions\*"; DestDir: "{app}\Companions"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\NAPRAWA PC HARDWARE TEST PRO"; Filename: "{app}\{#ExeName}"
Name: "{autodesktop}\NAPRAWA PC HARDWARE TEST PRO"; Filename: "{app}\{#ExeName}"; Tasks: desktopicon
Name: "{group}\NAPRAWA PC SYSTEM REPAIR PRO 5.6.16"; Filename: "{app}\Companions\SystemRepairPRO\NAPRAWA-PC-SYSTEM-REPAIR-PRO.exe"; WorkingDir: "{app}\Companions\SystemRepairPRO"; IconFilename: "{app}\Companions\SystemRepairPRO\naprawa-pc.ico"

[Run]
Filename: "{app}\{#ExeName}"; Description: "Uruchom NAPRAWA PC HARDWARE TEST PRO"; Flags: postinstall nowait skipifsilent


[Code]
function PrepareToInstall(var NeedsRestart: Boolean): String;
var
  ResultCode: Integer;
begin
  Result := '';
  { Stop only this product's versioned executables; do not spawn PowerShell or bypass its policy. }
  if FileExists(ExpandConstant('{sys}\taskkill.exe')) then
  begin
    Exec(ExpandConstant('{sys}\taskkill.exe'),
      '/F /T /FI "IMAGENAME eq NAPRAWA-PC-HARDWARE-TEST-PRO-*.exe" /IM *',
      '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
    Sleep(600);
  end;
end;
