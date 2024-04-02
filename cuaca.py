import requests
from datetime import datetime, timedelta

# API key OpenWeatherMap (dapat diperoleh setelah registrasi di website OpenWeatherMap)
api_key = '08a9f96ef7aa83bfcb1506aea3e18da3'

# ID kota Jakarta di OpenWeatherMap (ID kota Jakarta adalah 1642911)
city_id = '1642911'

# URL endpoint untuk mendapatkan ramalan cuaca
url = f'http://api.openweathermap.org/data/2.5/forecast?id={city_id}&appid={api_key}&units=metric'

# Mendapatkan data cuaca dari API
response = requests.get(url)
data = response.json()

# Mendapatkan ramalan cuaca untuk 5 hari ke depan
forecast = {}
for item in data['list']:
    timestamp = datetime.fromtimestamp(item['dt'])
    date = timestamp.date()
    if date not in forecast:
        forecast[date] = item['main']['temp']

# Menampilkan ramalan cuaca untuk 5 hari ke depan
print("Ramalan Cuaca untuk Jakarta (Suhu dalam Celcius):")
for date, temperature in forecast.items():
    formatted_date = date.strftime("%a, %d %b %Y")
    print(f"{formatted_date}: {temperature}°C")