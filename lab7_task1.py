import requests
import json

city = input()
API_KEY = '0b5c832585a4f4400fe6a951d59ac01c'
BASE_URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'


def get_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'ru',
    }

    response = requests.get(BASE_URL,params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)


def parse_weather(data):
    if not data:
        return None

    weather_info = {
        'city': data['name'],
        'temp': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'pressure': int((data['main']['pressure'])//(1.33)),
    }

    return weather_info


def main():

    raw_data = get_weather_data(city)
    if raw_data:
        weather = parse_weather(raw_data)

        print(f'Weather in {city}:')
        print(f'Temperature: {weather["temp"]}°C')
        print(f'Description: {weather["description"]}')
        print(f'Humidity: {weather["humidity"]}%')
        print(f'Pressure: {weather["pressure"]}mm Hg')



if __name__ == '__main__':
    main()


