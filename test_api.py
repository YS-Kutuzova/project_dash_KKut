# test_api.py
from utils.data_loader import load_data

# Тестируем с разными городами
test_cities = ["Moscow", "London", "Paris", "InvalidCity123"]

for city in test_cities:
    print(f"\n{'='*50}")
    print(f"Тестируем город: {city}")
    print(f"{'='*50}")
    
    data = load_data(city)
    
    if data:
        print(f"✅ Успешно! Город: {data['city_name']}")
        print(f"🌡️  Температура: {data['temp']}°C")
        print(f"☁️  Состояние: {data['condition']}")
        print(f"📊 Количество точек данных: {len(data['hours'])}")
    else:
        print(f"❌ Не удалось загрузить данные для {city}")