import requests
from datetime import datetime

def get_coordinates(api_key, city):
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    response = requests.get(geocode_url)
    response.raise_for_status()
    data = response.json()
    if not data:
        raise ValueError("City not found")
    return data[0]['lat'], data[0]['lon']

def get_current_weather(api_key, lat, lon):
    current_weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}"
    response = requests.get(current_weather_url)
    response.raise_for_status()
    return response.json()

def get_3hour_forecast(api_key, lat, lon):
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={api_key}"
    response = requests.get(forecast_url)
    response.raise_for_status()
    return response.json()

def display_current_weather(weather_data):
    temp = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    print(f"Current Temperature: {temp}°C")
    print(f"Weather Description: {description.capitalize()}")

def display_3hour_forecast(forecast_data):
    print("\n3-Hour Forecast for 5 Days:")
    for forecast in forecast_data['list']:
        date_time = datetime.utcfromtimestamp(forecast['dt']).strftime('%Y-%m-%d %H:%M:%S')
        temp = forecast['main']['temp']
        description = forecast['weather'][0]['description']
        print(f"{date_time} - Temp: {temp}°C, Weather: {description.capitalize()}")

def main():
    api_key = '93befe4d689430c8b2526fcf825268c4'  
    city = input("Enter city name: ")

    try:
        lat, lon = get_coordinates(api_key, city)
        current_weather_data = get_current_weather(api_key, lat, lon)
        forecast_data = get_3hour_forecast(api_key, lat, lon)
        display_current_weather(current_weather_data)
        display_3hour_forecast(forecast_data)
    except ValueError as ve:
        print(ve)
    except requests.exceptions.RequestException as re:
        print(f"Request error: {re}")

if __name__ == "__main__":
    main()






