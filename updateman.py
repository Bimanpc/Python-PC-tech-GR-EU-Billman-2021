Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import tkinter as tk
from tkinter import scrolledtext, messagebox
import subprocess

def run_command(command):
    try:
        result = subprocess.run(
            ["powershell", "-Command", command],
            capture_output=True, text=True, shell=True
        )
        return result.stdout.strip() if result.stdout else result.stderr.strip()
    except Exception as e:
        return str(e)

... def check_updates():
...     output = run_command("Get-WindowsUpdate")
...     text_area.delete(1.0, tk.END)
...     text_area.insert(tk.END, output)
... 
... def install_updates():
...     output = run_command("Install-WindowsUpdate -AcceptAll -AutoReboot")
...     messagebox.showinfo("Install Updates", "Installation started. Check the output for details.")
...     text_area.delete(1.0, tk.END)
...     text_area.insert(tk.END, output)
... 
... def update_history():
...     output = run_command("Get-WmiObject -Class Win32_QuickFixEngineering | Select-Object HotFixID, Description, InstalledOn")
...     text_area.delete(1.0, tk.END)
...     text_area.insert(tk.END, output)
... 
... # Create main window
... root = tk.Tk()
... root.title("Windows Update Manager")
... root.geometry("600x400")
... 
... # Buttons
... btn_check = tk.Button(root, text="Check for Updates", command=check_updates)
... btn_check.pack(pady=5)
... 
... btn_install = tk.Button(root, text="Install Updates", command=install_updates)
... btn_install.pack(pady=5)
... 
... btn_history = tk.Button(root, text="View Update History", command=update_history)
... btn_history.pack(pady=5)
... 
... # Output area
... text_area = scrolledtext.ScrolledText(root, width=70, height=15)
... text_area.pack(padx=10, pady=10)
... 
... # Run the GUI
