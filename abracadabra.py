import os
import tkinter as tk
from tkinter import filedialog, messagebox

class JunkCleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PC Junk Cleaner")

        self.label = tk.Label(root, text="Select a directory to clean up:")
        self.label.pack(pady=10)

        self.directory_path = tk.StringVar()
        self.directory_entry = tk.Entry(root, textvariable=self.directory_path, width=50)
        self.directory_entry.pack(pady=10)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_directory)
        self.browse_button.pack(pady=5)

        self.clean_button = tk.Button(root, text="Clean Junk Files", command=self.clean_junk_files)
        self.clean_button.pack(pady=20)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_path.set(directory)

    def clean_junk_files(self):
        directory = self.directory_path.get()
        if not directory:
            messagebox.showwarning("Warning", "Please select a directory first.")
            return

        junk_files = self.find_junk_files(directory)
        if not junk_files:
            messagebox.showinfo("Info", "No junk files found.")
            return

        confirm = messagebox.askyesno("Confirm", f"Found {len(junk_files)} junk files. Do you want to delete them?")
        if confirm:
            self.delete_files(junk_files)
            messagebox.showinfo("Success", "Junk files have been deleted.")

    def find_junk_files(self, directory):
        junk_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if self.is_junk_file(file):
                    junk_files.append(os.path.join(root, file))
        return junk_files

    def is_junk_file(self, file_name):
        # Define your criteria for junk files here
        junk_extensions = ['.tmp', '.log', '.bak', '.old']
        return any(file_name.endswith(ext) for ext in junk_extensions)

    def delete_files(self, files):
        for file in files:
            try:
                os.remove(file)
            except Exception as e:
                print(f"Error deleting file {file}: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = JunkCleanerApp(root)
    root.mainloop()
