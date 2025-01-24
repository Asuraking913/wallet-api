from django.conf import settings
import requests
from uuid import uuid4


def generate_id():
    return uuid4().hex

class FlutterwaveService:
    secret_key = settings.FLUTTERWAVE_SECRET_KEY
    base_url = "https://api.flutterwave.com"

    def initiate_transaction(self, amount, email):
        headers = {
            "Authorization" : f'Bearer {self.secret_key}', 
            "Content_Type" : "application/json"
        }

        new_id = generate_id()

        data = {
            "amount" : amount, 
            "email" : email, 
            "tx_ref" : new_id, 
            "redirect_url" : "http://localhost:5173/", 
            "currency" : "NGN", 
            "customer": {
            "email": "israelshedrack913@gmail.com"
        }
        }

        response = requests.post(
            f"{self.base_url}/v3/payments", json=data, headers=headers
        )

        print(response.json())

        return response.json()

        