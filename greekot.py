import tkinter as tk
from tkinter import scrolledtext

def respond():
    user_input = user_entry.get().strip().lower()
    user_entry.delete(0, tk.END)
    
    responses = {
        "γεια": "Γεια σου! Πώς μπορώ να σε βοηθήσω;",
        "τι κάνεις": "Είμαι ένα bot, οπότε πάντα καλά!",
        "ποιο είναι το όνομά σου": "Με λένε GROK BOT!",
        "αντίο": "Αντίο! Να έχεις μια υπέροχη μέρα!",
    }
    
    response = responses.get(user_input, "Συγγνώμη, δεν καταλαβαίνω. Μπορείς να επαναλάβεις;")
    chat_area.insert(tk.END, f"Εσύ: {user_input}\nGROK BOT: {response}\n\n")
    chat_area.yview(tk.END)

# Δημιουργία παραθύρου
root = tk.Tk()
root.title("GROK BOT")
root.geometry("400x500")

# Περιοχή συνομιλίας
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
chat_area.pack(pady=10)

# Πεδίο εισαγωγής χρήστη
user_entry = tk.Entry(root, width=40)
user_entry.pack(pady=5)

# Κουμπί αποστολής
send_button = tk.Button(root, text="Αποστολή", command=respond)
send_button.pack()

# Εκκίνηση της εφαρμογής
root.mainloop()
