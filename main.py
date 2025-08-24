import os
import json
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

CONFIG_FILE = "utilities.json"

def load_utilities():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return []

def save_utilities(utils):
    with open(CONFIG_FILE, "w") as f:
        json.dump(utils, f, indent=4)

def add_utility():
    filepath = filedialog.askopenfilename(filetypes=[("Executables", "*.exe"), ("All files", "*.*")])
    if filepath:
        utilities.append({"name": os.path.basename(filepath), "path": filepath})
        save_utilities(utilities)
        refresh_list()

def remove_selected():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        utilities.pop(index)
        save_utilities(utilities)
        refresh_list()

def launch_selected():
    for i in listbox.curselection():
        path = utilities[i]["path"]
        try:
            subprocess.Popen(path)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open {path}\n{e}")

def refresh_list():
    listbox.delete(0, tk.END)
    for util in utilities:
        listbox.insert(tk.END, util["name"])

# Tkinter UI
root = tk.Tk()
root.title("Startup Utility Launcher")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE, width=40, height=10)
listbox.pack()

btn_frame = tk.Frame(frame)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Add Utility", command=add_utility).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Remove Selected", command=remove_selected).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Launch Selected", command=launch_selected).pack(side=tk.LEFT, padx=5)

# Load saved utilities
utilities = load_utilities()
refresh_list()

root.mainloop()
