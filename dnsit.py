import tkinter as tk
from tkinter import messagebox
import subprocess

# Function to get network adapters
def get_adapters():
    try:
        output = subprocess.check_output("netsh interface ipv4 show interfaces", shell=True, text=True)
        lines = output.split("\n")
        adapters = []
        for line in lines:
            if "Connected" in line:
                parts = line.split()
                adapters.append(" ".join(parts[4:]))  # Extract adapter name
        return adapters
    except Exception as e:
        return []

# Function to change DNS settings
def change_dns(primary, secondary):
    adapter = adapter_var.get()
    if not adapter:
        messagebox.showerror("Error", "No network adapter selected.")
        return

    try:
        # Set DNS addresses
        subprocess.run(f'netsh interface ipv4 set dns name="{adapter}" static {primary}', shell=True, check=True)
        subprocess.run(f'netsh interface ipv4 add dns name="{adapter}" {secondary} index=2', shell=True, check=True)
        status_label.config(text=f"Applied: {primary}, {secondary}", fg="green")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to change DNS. Run as Administrator.")

# Function to reset to default DNS (automatic)
def reset_dns():
    adapter = adapter_var.get()
    if not adapter:
        messagebox.showerror("Error", "No network adapter selected.")
        return

    try:
        subprocess.run(f'netsh interface ipv4 set dns name="{adapter}" dhcp', shell=True, check=True)
        status_label.config(text="DNS Reset to Default", fg="blue")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to reset DNS. Run as Administrator.")

# GUI Setup
root = tk.Tk()
root.title("Yandex DNS Changer")
root.geometry("350x300")

# Network adapter selection
adapter_var = tk.StringVar()
adapters = get_adapters()
adapter_menu = tk.OptionMenu(root, adapter_var, *adapters)
adapter_menu.pack(pady=10)

# Buttons to apply different DNS modes
tk.Button(root, text="Set Yandex Basic", command=lambda: change_dns("77.88.8.8", "77.88.8.1"), width=25).pack(pady=5)
tk.Button(root, text="Set Yandex Safe", command=lambda: change_dns("77.88.8.88", "77.88.8.2"), width=25).pack(pady=5)
tk.Button(root, text="Set Yandex Family", command=lambda: change_dns("77.88.8.7", "77.88.8.3"), width=25).pack(pady=5)
tk.Button(root, text="Reset to Default", command=reset_dns, width=25).pack(pady=5)

# Status label
status_label = tk.Label(root, text="Select an adapter and choose DNS", fg="black")
status_label.pack(pady=10)

root.mainloop()
