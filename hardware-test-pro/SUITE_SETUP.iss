#ifndef AppVersion
  #define AppVersion "4.3.42"
#endif
#ifndef SourceDir
  #define SourceDir "dist"
#endif
#define AppName "NAPRAWA PC HARDWARE TEST PRO"
#define ExeName "NAPRAWA-PC-HARDWARE-TEST-PRO-4.3.42.exe"

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

[Files]
Source: "{#SourceDir}\{#ExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "README_PL.txt"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\NAPRAWA PC HARDWARE TEST PRO"; Filename: "{app}\{#ExeName}"
Name: "{autodesktop}\NAPRAWA PC HARDWARE TEST PRO"; Filename: "{app}\{#ExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#ExeName}"; Description: "Uruchom NAPRAWA PC HARDWARE TEST PRO"; Flags: postinstall nowait skipifsilent