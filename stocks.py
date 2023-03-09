import json
import os
import requests

class stocks():
    finnhub_api_url = "https://finnhub.io/api/v1/quote"
    finnhub_env_key = "FINNHUBKEY"

    def __init__(self):
        if stocks.finnhub_env_key not in os.environ:
            raise Exception("Finnhub API Key not set in environment var: " + stocks.finnhub_env_key)

    def request_data(self):
        params = dict (
                symbol="STEM",
                token=os.environ[stocks.finnhub_env_key]
            )
        response = requests.get(url=stocks.finnhub_api_url, params=params)
        response.raise_for_status()
        json_response = response.json()
        self.price = json_response["c"] if "c" in json_response else None
        self.change = json_response["dp"] if "dp" in json_response else None
        print("STEM price: " + str(self.price) + " change: " + str(self.change))
