import urllib.request as getWeather
import json
from datetime import datetime
def getWeatherInCity(city = "Moscow"):
    url = configureUrl(city)
    data = getWeather.urlopen(url).read().decode()
    return data

def configureUrl(city):
    baseUrl = 'https://api.openweathermap.org/data/2.5/weather?'
    units = 'metric'
    language = 'ru'
    appId = 'c341e34f9b7c327502cde34aa7817c5f'
    result = baseUrl + makeParams('q', city) + makeParams('units', units) + makeParams('lang', language) + makeParams('appId', appId)
    return result

def makeParams(keyName, data):
    result =  str('&'+keyName+'='+data)
    return result

weather = json.loads(getWeatherInCity())
now = datetime.now()
timetostr = now.strftime("%H:%M:%S")
print(f"Город: {weather['name']} Время: {timetostr}" )
print(f"Температура: {weather['main']['temp']} Влажность: {weather['main']['humidity']} Скорость ветра: {weather['wind']['speed']} Атмосферное давление: {weather['main']['pressure']}")
