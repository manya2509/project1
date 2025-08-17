import requests

API_KEY = "701d451fbc50116f85c794132dd8b89a"

locality = input("Enter locality name: ")

# Step 1: Get latitude & longitude of locality
geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={locality}&limit=1&appid={API_KEY}"
geo_response = requests.get(geo_url)

if geo_response.status_code == 200 and len(geo_response.json()) > 0:
    geo_data = geo_response.json()[0]
    lat, lon = geo_data["lat"], geo_data["lon"]

    # Step 2: Get weather using coordinates
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    weather_response = requests.get(weather_url)

    if weather_response.status_code == 200:
        data = weather_response.json()
        print(f"\n📍 Current Weather in {locality}")
        print(f"🌡️ Temperature: {data['main']['temp']} °C")
        print(f"💧 Humidity: {data['main']['humidity']} %")
        print(f"☁️ Weather: {data['weather'][0]['description']}")
    else:
        print("Weather API Error:", weather_response.status_code, weather_response.text)
else:
    print("Locality not found or Geocoding API Error:", geo_response.text)

