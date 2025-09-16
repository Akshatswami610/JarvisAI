import os
import requests
from dotenv import load_dotenv

# Load secrets
load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city: str) -> str:
    try:
        if not WEATHER_API_KEY:
            return "Weather API key is missing. Please check your .env file."

        url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no"
        response = requests.get(url).json()

        if "error" in response:
            return f"Error: {response['error']['message']}"

        location = response["location"]["name"]
        temp = response["current"]["temp_c"]
        condition = response["current"]["condition"]["text"]

        return f"The weather in {location} is {condition} with {temp}°C."
    except Exception as e:
        return f"Error fetching weather: {e}"
