import urllib.request as weather
def configureurl(city = "Moscow"):
    baseurl = "https://api.openweathermap.org/data/2.5/weather?"
    units = "metric"
    lang = "ru"
    appid = "c341e34f9b7c327502cde34aa7817c5f"
    result =
    return result

print(weather.urlopen("https://api.openweathermap.org/data/2.5/weather?q=Moscow&units=metric&lang=ru&appid=c341e34f9b7c327502cde34aa7817c5f").read().decode());
