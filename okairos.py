import tkinter as tk
from tkinter import messagebox
import requests

# Replace 'your_api_key' with your actual API key from a weather service
API_KEY = 'your_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"Weather: {weather}\nTemperature: {temperature}°C"
    else:
        return "Could not retrieve weather data."

def send_message():
    city = entry.get()
    if city:
        weather_info = get_weather(city)
        chat_box.insert(tk.END, f"You: {city}\n")
        chat_box.insert(tk.END, f"Bot: {weather_info}\n")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

# Set up the main window
root = tk.Tk()
root.title("Weather Chatbot")

# Chat box
chat_box = tk.Text(root, height=15, width=50)
chat_box.pack(padx=10, pady=10)

# Entry widget for user input
entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Run the application
root.mainloop()
