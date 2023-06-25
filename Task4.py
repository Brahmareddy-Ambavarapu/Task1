

import requests

api_key = 'eb9b2cfd75d7c16d614594a0fe2eb3af'

city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    humid = data['main']['humidity']
    wind_speed = data['wind']['speed'] * 3.6
    
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} K')
    print(f'Humiduity : {humid}%')
    print(f'Wind speed is: {wind_speed}')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')
