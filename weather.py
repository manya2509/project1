
import requests
import json

API_KEY = "701d451fbc50116f85c794132dd8b89a"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("\n📍 City:", data["name"])
    print("🌡️ Temperature:", data["main"]["temp"], "°C")
    print("💧 Humidity:", data["main"]["humidity"], "%")
    print("☁️ Weather:", data["weather"][0]["description"])
else:
    print("Error:", response.status_code, response.text)
