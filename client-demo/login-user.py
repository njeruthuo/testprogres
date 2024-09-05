import requests

endpoint = 'http://localhost:8000/api/login/'

user = {'username': 'admin@admin.com', 'password': 'superuser'}

response = requests.post(endpoint, json=user)

print(response.json(), response.status_code)
