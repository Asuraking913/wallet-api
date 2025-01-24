from django.conf import settings
import requests

class FlutterwaveService:
    secret_key = settings.FLUTTERWAVE_SECRET_KEY
    base_url = "https://api.flutterwave.com"

    def initiate_transaction(self, amount, email):
        headers = {
            "Authorization" : f'Bearer {self.secret_key}', 
            "Content_Type" : "application/json"
        }

        data = {
            "amount" : amount, 
            "email" : email
        }

        response = requests.post(
            f"{self.base_url}/v3/transaction/initialize", json=data, headers=headers
        )

        return response.json()

        