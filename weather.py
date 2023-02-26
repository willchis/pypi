import json
import os
import requests

weather_api_url = "https://api.openweathermap.org/data/2.5/weather"
weather_env_key = "WEATHERKEY"

if weather_env_key not in os.environ:
    raise Exception("Weather API Key not in environment var: " + weather_env_key)

params = dict (
        lat="40.002538",
        lon="-105.1399453",
        appId=os.environ[weather_env_key]
    )

response = requests.get(url=weather_api_url, params=params)

response.raise_for_status()

weather_data = response.json()

print("temp: " + str(weather_data["main"]["temp"]))
