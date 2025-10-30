import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")


def load_data(city):
    response = requests.get(API_URL, params={'key': API_KEY, 'q': city, 'days': 1, 'aqi': 'yes'})
    data = response.json()

    # Оставляем основную информацию по погодным условиям, без прогнозов и графиков
    city_name = data['location']['name']
    temp = data['current']['temp_c']
    condition = data['current']['condition']['text']
    icon = data['current']['condition']['icon']
    wind_speed = data['current']['wind_kph'] / 3.6

    # Качество воздуха по часам
    forecast_hours = data['forecast']['forecastday'][0]['hour']
    hours = [hour['time'][-5:] for hour in forecast_hours]

    pm25_hours = [hour['air_quality']['pm2_5'] for hour in forecast_hours]
    pm10_hours = [hour['air_quality']['pm10'] for hour in forecast_hours]
    co_hours = [hour['air_quality']['co'] for hour in forecast_hours]
    no2_hours = [hour['air_quality']['no2'] for hour in forecast_hours]
    o3_hours = [hour['air_quality']['o3'] for hour in forecast_hours]
    so2_hours = [hour['air_quality']['so2'] for hour in forecast_hours]

    return {
        'city_name': city_name,
        'temp': temp,
        'condition': condition,
        'icon': icon,
        'wind_speed': round(wind_speed, 1),

        'hours': hours,
        'pm25_hours': pm25_hours,
        'pm10_hours': pm10_hours,
        'co_hours': co_hours,
        'no2_hours': no2_hours,
        'o3_hours': o3_hours,
        'so2_hours': so2_hours

    }
