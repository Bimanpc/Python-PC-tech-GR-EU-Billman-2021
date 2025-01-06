import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import platform

class NetworkManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Manager")
        self.root.geometry("500x400")
        
        self.networks = []
        self.selected_network = tk.StringVar()
        
        # UI Components
        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Network Manager", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Network List
        self.network_listbox = tk.Listbox(self.root, height=10, width=50, selectmode=tk.SINGLE)
        self.network_listbox.pack(pady=10)
        
        # Refresh Button
        refresh_button = tk.Button(self.root, text="Refresh", command=self.scan_networks)
        refresh_button.pack(pady=5)
        
        # Connect Button
        connect_button = tk.Button(self.root, text="Connect", command=self.connect_to_network)
        connect_button.pack(pady=5)

        # Password Entry
        password_label = tk.Label(self.root, text="Enter Password:")
        password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*", width=30)
        self.password_entry.pack(pady=5)

    def scan_networks(self):
        """Scans for available Wi-Fi networks."""
        try:
            self.network_listbox.delete(0, tk.END)  # Clear existing entries
            if platform.system() == "Windows":
                # Windows command to list available networks
                result = subprocess.check_output("netsh wlan show networks", shell=True, text=True)
                networks = [line.split(":")[1].strip() for line in result.splitlines() if "SSID" in line]
            elif platform.system() == "Linux":
                # Linux command to list available networks
                result = subprocess.check_output(["nmcli", "-t", "-f", "SSID", "dev", "wifi"], text=True)
                networks = [line.strip() for line in result.splitlines() if line]
            else:
                networks = []
            
            self.networks = networks
            for network in networks:
                self.network_listbox.insert(tk.END, network)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to scan networks: {e}")

    def connect_to_network(self):
        """Connects to the selected network."""
        try:
            selected_index = self.network_listbox.curselection()
            if not selected_index:
                messagebox.showwarning("Warning", "Please select a network.")
                return
            
            selected_network = self.networks[selected_index[0]]
            password = self.password_entry.get()
            if not password:
                messagebox.showwarning("Warning", "Please enter a password.")
                return

            if platform.system() == "Windows":
                # Command for Windows (netsh wlan)
                subprocess.run(f"netsh wlan connect name=\"{selected_network}\"", shell=True)
            elif platform.system() == "Linux":
                # Command for Linux (nmcli)
                subprocess.run(["nmcli", "dev", "wifi", "connect", selected_network, "password", password])
            else:
                messagebox.showerror("Error", "Unsupported operating system.")
                return

            messagebox.showinfo("Success", f"Connected to {selected_network}!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to connect to network: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkManagerApp(root)
    root.mainloop()
