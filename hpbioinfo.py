import tkinter as tk
from tkinter import ttk

def get_bios_info():
    # Placeholder function to get BIOS information
    # In a real application, you would retrieve this information from the system
    return {
        "Vendor": "HP",
        "Version": "F.20",
        "Release Date": "01/01/2023",
        "BIOS Revision": "1.0"
    }

def display_info():
    bios_info = get_bios_info()
    info_text = "\n".join([f"{key}: {value}" for key, value in bios_info.items()])
    info_label.config(text=info_text)

# Create the main window
root = tk.Tk()
root.title("HP BIOS Info")

# Create a frame for the content
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create a label to display the BIOS information
info_label = ttk.Label(frame, text="", justify=tk.LEFT)
info_label.grid(row=1, column=0, padx=10, pady=10)

# Create a button to refresh the BIOS information
refresh_button = ttk.Button(frame, text="Refresh BIOS Info", command=display_info)
refresh_button.grid(row=2, column=0, pady=10)

# Display the BIOS information when the application starts
display_info()

# Run the application
root.mainloop()
