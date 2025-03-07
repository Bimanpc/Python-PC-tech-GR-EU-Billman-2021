import tkinter as tk
from tkinter import messagebox
import threading
import http.server
import socketserver
import os

class SimpleServerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Local Server GUI")
        self.root.geometry("300x200")
        
        self.port_label = tk.Label(root, text="Port:")
        self.port_label.pack()
        
        self.port_entry = tk.Entry(root)
        self.port_entry.pack()
        self.port_entry.insert(0, "8000")  # Default port
        
        self.start_button = tk.Button(root, text="Start Server", command=self.start_server)
        self.start_button.pack(pady=5)
        
        self.stop_button = tk.Button(root, text="Stop Server", command=self.stop_server, state=tk.DISABLED)
        self.stop_button.pack(pady=5)
        
        self.server = None
        self.server_thread = None
    
    def start_server(self):
        try:
            port = int(self.port_entry.get())
            handler = http.server.SimpleHTTPRequestHandler
            self.server = socketserver.TCPServer(("", port), handler)
            
            self.server_thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            self.server_thread.start()
            
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            messagebox.showinfo("Success", f"Server started on port {port}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start server: {e}")
    
    def stop_server(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.server = None
            
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            messagebox.showinfo("Stopped", "Server has been stopped")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleServerGUI(root)
    root.mainloop()
