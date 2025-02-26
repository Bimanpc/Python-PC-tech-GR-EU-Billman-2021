import tkinter as tk
from telegram import Bot
from telegram.error import TelegramError

# Replace with your Telegram bot token
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"  # Replace with your Telegram chat ID

bot = Bot(token=BOT_TOKEN)

def send_message():
    message = entry.get()
    if message:
        try:
            bot.send_message(chat_id=CHAT_ID, text=message)
            status_label.config(text="Message Sent!", fg="green")
        except TelegramError as e:
            status_label.config(text=f"Error: {e}", fg="red")
    else:
        status_label.config(text="Message cannot be empty!", fg="red")

# GUI Setup
root = tk.Tk()
root.title("Telegram Bot Messenger")
root.geometry("400x200")

tk.Label(root, text="Enter your message:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=10)

status_label = tk.Label(root, text="", fg="black")
status_label.pack()

root.mainloop()
