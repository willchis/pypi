import json
import os
import requests

class weather():
    weather_api_url = "https://api.openweathermap.org/data/2.5/weather"
    weather_env_key = "WEATHERKEY"

    def __init__(self):
        if weather.weather_env_key not in os.environ:
            raise Exception("Weather API Key not set in environment var: " + weather.weather_env_key)

    def request_data(self):
        params = dict (
                lat="40.002538",
                lon="-105.1399453",
                appId=os.environ[weather.weather_env_key]
            )

        response = requests.get(url=weather.weather_api_url, params=params)
        response.raise_for_status()
        self.data = response.json()["main"]
        print("temp: " + str(self.data["temp"]))

    def tempF(self):
        tempF = None
        if ("temp" in self.data):
            kelvin = self.data["temp"]
            tempF = (9.0 / 5) * (kelvin - 273.15) + 32
        return tempF
    
    def humidity(self):
        return self.data["humidity"] if "humidity" in self.data else None
