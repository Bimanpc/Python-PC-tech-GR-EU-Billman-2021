import tkinter as tk
from tkinter import messagebox

def safe_search():
    query = entry.get()
    if query.lower() in forbidden_words:
        messagebox.showwarning("Warning", "Your search query contains inappropriate content.")
    else:
        # Simulate a safe search by displaying a message
        messagebox.showinfo("Search Result", f"Search results for: {query}")

# Initialize the main window
root = tk.Tk()
root.title("Safe Web Search")

# List of forbidden words (for demonstration purposes)
forbidden_words = ["badword1", "badword2", "badword3"]

# Create and place the widgets
label = tk.Label(root, text="Enter your search query:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

search_button = tk.Button(root, text="Search", command=safe_search)
search_button.pack(pady=10)

# Run the application
root.mainloop()
