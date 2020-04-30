#! python3

import json, requests, sys
from datetime import datetime

def timeextractor(timeStamp):
    dt_object = datetime.fromtimestamp(timeStamp)
    hour = str(dt_object.hour)
    minutes = str(dt_object.minute)
    timeString = hour + ":" + minutes
    return timeString


if len(sys.argv) < 2:
    print("For proper use from comamnd line enter: weather.py {city,country code}")
    sys.exit()

city = ' '.join(sys.argv[1:]).title()


api_key = "d48c35669a96dfa7f24b6e6a7259261e"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
w = weatherData['main']
temp = '{:.1f}'.format(float(w['temp']) - 273.15)
pressure = str(w['pressure'])
humidity = str(w['humidity'])

sunrise = timeextractor(weatherData['sys']['sunrise'])
sunset = timeextractor(weatherData['sys']['sunset'])

description1 = weatherData['weather'][0]['description']
wind = str(weatherData['wind']['speed']) + ' m/s'

print(f"\nCurrent weather for {city}\n")
print(f"General description: {description1}")
print(f"Temp =      {temp} °C")
print(f"Pressure =  {pressure} hPa")
print(f"Humidity =  {humidity} % \n")
print(f"Sunrise =   {sunrise}")
print(f"Sunset =    {sunset}")


