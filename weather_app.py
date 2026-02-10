import win32com.client
import requests

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def weather(query):
    city = ' '.join(query.split('weather at')[1:]).strip()
    print(f"Weather at {city}:")
    speaker.speak(f"The weather at {city} is")

    url = (
        "http://api.openweathermap.org/data/2.5/weather?q="
        + city +
        "&appid=b144a088954018157e4e940f2e272d7d"
    )

    weather_data = requests.get(url).json()

    if weather_data.get("cod") != 200:
        print("City not found.")
        speaker.speak("Sorry, I couldn't find the weather for that city.")
        return

    celsius = int(weather_data['main']['temp'] - 273.15)
    fahrenheit = int(celsius * 9 / 5 + 32)
    humidity = weather_data['main']['humidity']
    windspeed = weather_data['wind']['speed']
    clouds = weather_data['weather'][0]['description']

    print(f"The temperature is {celsius} degree Celsius and {fahrenheit} degree Fahrenheit")
    speaker.speak(f"The temperature is {celsius} degree Celsius and {fahrenheit} degree Fahrenheit")

    print(f"Humidity is {humidity}%")
    speaker.speak(f"Humidity is {humidity} percent")

    print(f"Windspeed is {windspeed} kilometers per hour")
    speaker.speak(f"Windspeed is {windspeed} kilometers per hour")

    print(f"Clouds are {clouds}")
    speaker.speak(f"Clouds are {clouds}")
