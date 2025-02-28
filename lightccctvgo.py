import tkinter as tk
from tkinter import messagebox

class CCTVDesignerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CCTV Designer App")

        # Create a canvas for designing the CCTV layout
        self.canvas = tk.Canvas(root, width=800, height=600, bg="lightgray")
        self.canvas.pack()

        # Buttons for adding cameras
        self.add_camera_button = tk.Button(root, text="Add Camera", command=self.add_camera)
        self.add_camera_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Save layout button
        self.save_button = tk.Button(root, text="Save Layout", command=self.save_layout)
        self.save_button.pack(side=tk.LEFT, padx=10, pady=10)

    def add_camera(self):
        # Add a camera (a circle) to the canvas
        x, y = 100, 100
        radius = 20
        camera = self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill="blue", outline="black")
        self.canvas.tag_bind(camera, "<B1-Motion>", self.move_camera)
        messagebox.showinfo("Info", "Drag the camera to position it.")

    def move_camera(self, event):
        # Move the camera (circle) with mouse drag
        widget = event.widget
        x, y = event.x, event.y
        widget.coords(tk.CURRENT, x-20, y-20, x+20, y+20)

    def clear_canvas(self):
        # Clear all items on the canvas
        self.canvas.delete("all")
        messagebox.showinfo("Info", "Canvas cleared.")

    def save_layout(self):
        # Save the current layout (for simplicity, just a message for now)
        messagebox.showinfo("Info", "Layout saved successfully!")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CCTVDesignerApp(root)
    root.mainloop()
