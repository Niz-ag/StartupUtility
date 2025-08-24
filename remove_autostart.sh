#!/bin/bash
# ===========================================
# Autostart Remover for StartupUtility.exe
# ===========================================

APP_NAME="StartupUtility"

# Windows Startup folder path
STARTUP_DIR="$(powershell.exe -NoProfile -Command \
  '[Environment]::GetFolderPath(\"Startup\")' | tr -d '\r')"

SHORTCUT="$STARTUP_DIR\\$APP_NAME.lnk"

echo "[*] Removing $APP_NAME from Windows Startup..."

powershell.exe -NoProfile -Command \
  "if (Test-Path '$SHORTCUT') { Remove-Item '$SHORTCUT' -Force }"

echo "[✓] Autostart entry removed (if it existed)."
