from datetime import datetime
import requests
from config import API
from pprint import pprint

def get_weather(city, API):
    code_to_smile = {
        'Clear': "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Ливень \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        a = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric'
        )
        data = a.json()
        pprint(data)
        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['wind']['speed']
        wind = data['wind']['speed']
        sunrise_timepesp = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timepesp = datetime.fromtimestamp((data['sys']['sunset']))
        length_of_the_day = datetime.fromtimestamp(data['sys']['sunset']) - datetime.fromtimestamp(
                data['sys']['sunrise'])
        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'посмтори в окно, не пойму какая погода там!'


        return    f'''
            Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            погода в городе: {city}
            температура: {cur_weather} C {wd}
            влажность: {humidity}
            давление: {pressure} мм.pт.ст
            скорость ветра: {wind}
            восход: {sunrise_timepesp}
            продолжительность дня: {length_of_the_day}
            закат: {sunset_timepesp}'''


    except Exception as ex:
        return 'correct City!!!!!'