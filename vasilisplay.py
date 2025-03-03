import tkinter as tk
from tkinter import ttk, filedialog
import vlc

class VLCPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("VLC-like Media Player")
        self.root.geometry("600x400")
        
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        
        self.create_widgets()
    
    def create_widgets(self):
        self.video_frame = ttk.Frame(self.root)
        self.video_frame.pack(fill=tk.BOTH, expand=True)
        
        self.open_button = ttk.Button(self.root, text="Open File", command=self.open_file)
        self.open_button.pack(pady=5)
        
        self.play_button = ttk.Button(self.root, text="Play", command=self.play)
        self.play_button.pack(pady=5)
        
        self.pause_button = ttk.Button(self.root, text="Pause", command=self.pause)
        self.pause_button.pack(pady=5)
        
        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack(pady=5)
        
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Media Files", "*.mp4;*.mp3;*.avi;*.mkv;*.flv;*.mov")])
        if file_path:
            media = self.instance.media_new(file_path)
            self.player.set_media(media)
            self.player.set_hwnd(self.video_frame.winfo_id())
    
    def play(self):
        self.player.play()
    
    def pause(self):
        self.player.pause()
    
    def stop(self):
        self.player.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = VLCPlayer(root)
    root.mainloop()
