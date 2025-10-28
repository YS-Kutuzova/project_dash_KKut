import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")


def load_data(city):
    response = requests.get(API_URL, params={'key': API_KEY, 'q': city, 'days': 1, 'aqi': 'yes'})
    data = response.json()
    city_name = data['location']['name']
    temp = data['current']['temp_c']
    condition = data['current']['condition']['text']
    icon = data['current']['condition']['icon']

    forecast_hours = data['forecast']['forecastday'][0]['hour']
    hours = [hour['time'][-5:] for hour in forecast_hours]
    temps = [hour['temp_c'] for hour in forecast_hours]
    ap = [hour['pressure_mb'] * 0.75 for hour in forecast_hours]
    wind = [hour['wind_kph'] / 3.6 for hour in forecast_hours]
    wind_dirs = [hour['wind_degree'] for hour in forecast_hours]
    air_quality = data['current']['air_quality']

    return {
        'city_name': city_name,
        'temp': temp,
        'condition': condition,
        'icon': icon,
        'temps': temps,
        'ap': ap,
        'wind': wind,
        'wind_dirs': wind_dirs,
        'hours': hours,
        'air_quality': air_quality #для задания
    }