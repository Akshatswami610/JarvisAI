import requests
from Core.config import WEATHER_API_KEY
from Core.speaker import speak


def get_weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        if "current" in data:
            condition = data['current']['condition']['text']
            temp = data['current']['temp_c']
            speak(f"It is {condition} with {temp} degrees Celsius in {city}.")
        else:
            speak(f"Sorry, I couldn't retrieve weather data for {city}.")

    except requests.exceptions.RequestException as e:
        speak("There was a problem connecting to the weather service.")
        print(f"[Error] {e}")
    except KeyError as e:
        speak("There was a problem interpreting the weather data.")
        print(f"[KeyError] Missing field: {e}")
