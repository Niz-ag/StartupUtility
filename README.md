# StartupUtility# 🚀 Startup Utility Launcher

A simple Python-based **Startup Utility Launcher** with a GUI (Tkinter) that lets you:

- Add frequently used executables (.exe)  
- Toggle them on/off for autostart  
- Launch selected apps with one click  
- Persist your configuration across sessions  

This repo provides the compiled `StartupUtility.exe` along with helper scripts to configure **autostart on Windows login**.

---

## 📦 Contents
- `startup_utility.zip` → Contains `StartupUtility.exe` (the app).  
- `autostart.sh` → Script to **install autostart**.  
- `remove_autostart.sh` → Script to **remove autostart**.  

---


⚙️ Installation & Usage
------------------------

1. Extract the app
   unzip startup_utility.zip -d startup_utility
   cd startup_utility

2. Run the app (Windows .exe)
   - Double-click startup_utility.exe
   - Or from terminal:
     ./startup_utility.exe

3. Enable auto-start on boot
   bash autostart.sh

4. Remove from auto-start
   bash remove_autostart.sh
