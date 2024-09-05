import requests

endpoint = 'http://localhost:8000/api/register/'

user = {'username': 'admin', 'password':'superuser'}

try:
    response = requests.post(endpoint, json=user)
    print(response.json(), response.status_code)
except:
    if response.status_code == 400:
        print(f"A username with this field already exists")

