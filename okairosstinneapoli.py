import tkinter as tk
from tkinter import ttk

# Function to fetch weather data (replace with actual API call)
def fetch_weather():
    # Static weather data for demonstration
    weather_data = {
        "temperature": "18°C",
        "condition": "Partly cloudy",
        "humidity": "68%",
        "wind_speed": "4 Km/h",
        "precipitation": "0.0 mm"
    }
    return weather_data

# Function to update the weather display
def update_weather():
    weather_data = fetch_weather()
    temperature_label.config(text=f"Temperature: {weather_data['temperature']}")
    condition_label.config(text=f"Condition: {weather_data['condition']}")
    humidity_label.config(text=f"Humidity: {weather_data['humidity']}")
    wind_speed_label.config(text=f"Wind Speed: {weather_data['wind_speed']}")
    precipitation_label.config(text=f"Precipitation: {weather_data['precipitation']}")

# Create the main window
root = tk.Tk()
root.title("Weather in Neapolis, Lakonia, Greece")

# Create and place the labels
ttk.Label(root, text="Weather in Neapolis, Lakonia, Greece", font=("Helvetica", 16)).grid(column=0, row=0, columnspan=2, pady=10)

temperature_label = ttk.Label(root, text="Temperature: ", font=("Helvetica", 14))
temperature_label.grid(column=0, row=1, sticky=tk.W, padx=10)

condition_label = ttk.Label(root, text="Condition: ", font=("Helvetica", 14))
condition_label.grid(column=0, row=2, sticky=tk.W, padx=10)

humidity_label = ttk.Label(root, text="Humidity: ", font=("Helvetica", 14))
humidity_label.grid(column=0, row=3, sticky=tk.W, padx=10)

wind_speed_label = ttk.Label(root, text="Wind Speed: ", font=("Helvetica", 14))
wind_speed_label.grid(column=0, row=4, sticky=tk.W, padx=10)

precipitation_label = ttk.Label(root, text="Precipitation: ", font=("Helvetica", 14))
precipitation_label.grid(column=0, row=5, sticky=tk.W, padx=10)

# Create and place the update button
update_button = ttk.Button(root, text="Update Weather", command=update_weather)
update_button.grid(column=0, row=6, columnspan=2, pady=20)

# Initialize the weather display
update_weather()

# Run the application
root.mainloop()
