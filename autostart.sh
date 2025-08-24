#!/bin/bash
# ===========================================
# Autostart Installer for StartupUtility.exe
# ===========================================

APP_NAME="StartupUtility"
EXE_NAME="StartupUtility.exe"

# Windows Startup folder path
STARTUP_DIR="$(powershell.exe -NoProfile -Command \
  '[Environment]::GetFolderPath(\"Startup\")' | tr -d '\r')"

# Ensure exe exists
if [ ! -f "$EXE_NAME" ]; then
    echo "[!] $EXE_NAME not found in current directory."
    echo "    Place this script in the same folder as $EXE_NAME and run again."
    exit 1
fi

# Create shortcut in Startup folder
echo "[*] Adding $EXE_NAME to Windows Startup..."
powershell.exe -NoProfile -Command \
  "\$s=(New-Object -COM WScript.Shell).CreateShortcut('$STARTUP_DIR\\$APP_NAME.lnk'); \
   \$s.TargetPath='$(pwd -W)/$EXE_NAME'; \
   \$s.WorkingDirectory='$(pwd -W)'; \
   \$s.Save()"

echo "[✓] $APP_NAME is now set to autostart on login."
