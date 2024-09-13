import requests
import os

response = requests.post(
    "https://restdev.bluetrax.co.ke/api/BankApp/getStatus", json={'regNos': ['KCV 292Z']})

print(response.json()['data'][0]['vehicle_status'][0]['lon'])
