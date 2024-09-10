import requests
import os

response = requests.post(
    "https://restdev.bluetrax.co.ke/api/BankApp/getStatus", json={'regNos': ['KCV 292Z']})

print(response.json())
