import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Ακούω...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language="el-GR")
            text_entry.delete(0, tk.END)
            text_entry.insert(0, text)
            status_label.config(text="Έτοιμο!")
        except sr.UnknownValueError:
            messagebox.showerror("Σφάλμα", "Δεν καταλάβαμε τον ήχο.")
        except sr.RequestError:
            messagebox.showerror("Σφάλμα", "Σφάλμα σύνδεσης με την υπηρεσία αναγνώρισης.")

def text_to_speech():
    engine = pyttsx3.init()
    text = text_entry.get()
    if text:
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("Προσοχή", "Παρακαλώ εισάγετε κείμενο.")

# Δημιουργία GUI
root = tk.Tk()
root.title("Βοηθός για Κωφούς")
root.geometry("400x300")

title_label = tk.Label(root, text="Βοηθός για Κωφούς", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

text_entry = tk.Entry(root, font=("Arial", 14))
text_entry.pack(pady=10, fill=tk.X, padx=20)

speech_button = tk.Button(root, text="Ομιλία σε Κείμενο", command=speech_to_text)
speech_button.pack(pady=5)

speak_button = tk.Button(root, text="Κείμενο σε Ομιλία", command=text_to_speech)
speak_button.pack(pady=5)

status_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
status_label.pack(pady=10)

root.mainloop()
