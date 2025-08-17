
import requests
import json

API_KEY = "701d451fbc50116f85c794132dd8b89a"

# Get latitude and longitude from user
lat = input("Enter latitude: ")
lon = input("Enter longitude: ")

# Construct the API URL using coordinates
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

# Make the API request
response = requests.get(url)

# Check response and print weather data
if response.status_code == 200:
    data = response.json()
    print("\n📍 Location:", data["name"])
    print("🌡️ Temperature:", data["main"]["temp"], "°C")
    print("💧 Humidity:", data["main"]["humidity"], "%")
    print("☁️ Weather:", data["weather"][0]["description"])
else:
    print("Error:", response.status_code, response.text)