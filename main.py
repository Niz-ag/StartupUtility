import os
import json
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

CONFIG_FILE = "utilities.json"

def load_utilities():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                data = f.read().strip()
                if not data:
                    return [] 
                return json.loads(data)
        except (json.JSONDecodeError, ValueError):            
            return []
    return []


def save_utilities():
    with open(CONFIG_FILE, "w") as f:
        json.dump(utilities, f, indent=4)

def add_utility():
    filepaths = filedialog.askopenfilenames(
        filetypes=[("Executables", "*.exe"), ("All files", "*.*")]
    )
    if filepaths:
        for filepath in filepaths:
            utilities.append({"name": os.path.basename(filepath), "path": filepath, "enabled": True})
        save_utilities()
        refresh_list()

def remove_selected():
    to_remove = []
    for i, (util, var) in enumerate(zip(utilities, checkbox_vars)):
        if var.get():
            to_remove.append(i)

    if not to_remove:
        messagebox.showinfo("Remove", "Tick at least one utility checkbox to remove.")
        return

    for index in reversed(to_remove):
        utilities.pop(index)

    save_utilities()
    refresh_list()

def launch_selected():
    for util, var in zip(utilities, checkbox_vars):
        if var.get():
            try:
                subprocess.Popen(util["path"], shell=True)
            except Exception as e:
                messagebox.showerror("Error", f"Could not open {util['path']}\n{e}")

def refresh_list():
    for widget in list_frame.winfo_children():
        widget.destroy()

    checkbox_vars.clear()

    for i, util in enumerate(utilities):
        var = tk.BooleanVar(value=util.get("enabled", False))

        def update_state(index=i, v=var):
            utilities[index]["enabled"] = v.get()
            save_utilities()

        chk = tk.Checkbutton(list_frame, text=util["name"], variable=var,
                             command=update_state)
        chk.pack(anchor="w")
        checkbox_vars.append(var)

root = tk.Tk()
root.title("Startup Utility Launcher")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

list_frame = tk.Frame(frame)
list_frame.pack(fill="both", expand=True)

checkbox_vars = []

btn_frame = tk.Frame(frame)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Utility", command=add_utility).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Remove Selected", command=remove_selected).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Launch Selected", command=launch_selected).pack(side=tk.LEFT, padx=5)

utilities = load_utilities()
refresh_list()

root.mainloop()
