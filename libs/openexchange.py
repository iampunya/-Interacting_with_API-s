import requests
import functools

APP_ID = "72dba35060b54cf9ad3ffbdc68de9174"
ENDPOINT = "https://openexchangerates.org/api/latest.json"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rates = response.json()

usd_amount = 1000
gbp_amount = usd_amount * exchange_rates['rates']['GBP']

print(f"USD{usd_amount} is GBP{gbp_amount}")

class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api/"

    def __init__(self, app_id):
        self.app_id = app_id
    
    @property
    def latest(self):
        return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.app_id}").json()
    
    def convert(self, from_amount, from_currency, to_currency):
        rates = self.latest['rates']
        to_rate = rates[to_currency]

        if from_currency == 'USD':
            return from_amount * to_rate
        else:
            from_in_usd = from_amount / rates[from_currency]
            return from_in_usd * to_rate
