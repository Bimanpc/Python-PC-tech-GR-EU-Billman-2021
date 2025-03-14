import tkinter as tk
from tkinter import scrolledtext

class SimpleChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Chatbot")

        # Create a scrolled text widget for displaying the conversation
        self.conversation = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
        self.conversation.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create an entry widget for user input
        self.entry = tk.Entry(root)
        self.entry.pack(padx=10, pady=10, fill=tk.X)

        # Create a send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        # Bind the Enter key to the send_message method
        self.entry.bind("<Return>", lambda event: self.send_message())

    def send_message(self):
        user_input = self.entry.get()
        if user_input.strip():
            self.display_message(f"You: {user_input}")
            response = self.get_chatbot_response(user_input)
            self.display_message(f"Chatbot: {response}")
            self.entry.delete(0, tk.END)

    def display_message(self, message):
        self.conversation.config(state=tk.NORMAL)
        self.conversation.insert(tk.END, message + "\n")
        self.conversation.config(state=tk.DISABLED)
        self.conversation.yview(tk.END)

    def get_chatbot_response(self, user_input):
        # Here you can add your chatbot logic
        # For now, it just echoes the user's input
        return f"Echo: {user_input}"

if __name__ == "__main__":
    root = tk.Tk()
    chatbot = SimpleChatbot(root)
    root.mainloop()
