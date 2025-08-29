import requests

API_KEY = "1855275c54cdcd4f86767ab9f0718501"
CITY = "Shahjahanpur"

def get_weather():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        weather = data['weather'][0]['main']
        temp = data['main']['temp']
        return f"{CITY}: {weather}, {temp}°C"
    except:
        return "Weather not available"
