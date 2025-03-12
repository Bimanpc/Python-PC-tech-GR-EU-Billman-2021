import tkinter as tk

def create_easter_greeting():
    # Δημιουργία του κύριου παραθύρου
    root = tk.Tk()
    root.title("Καλό Πάσχα 2025")

    # Ρύθμιση των διαστάσεων του παραθύρου
    root.geometry("300x200")

    # Δημιουργία ετικέτας με το μήνυμα καλωσορίσματος
    greeting_label = tk.Label(root, text="Καλό Πάσχα 2025!", font=("Helvetica", 16))
    greeting_label.pack(pady=20)

    # Δημιουργία κουμπιού για κλείσιμο του παραθύρου
    close_button = tk.Button(root, text="Κλείσιμο", command=root.destroy)
    close_button.pack(pady=10)

    # Εκκίνηση του κύριου βρόχου εφαρμογής
    root.mainloop()

create_easter_greeting()
