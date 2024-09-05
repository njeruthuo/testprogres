import requests

endpoint1 = "http://localhost:8000/api/token-auth/"

user = {'username':'julius', 'password':'superuser'}

get_response = requests.post(endpoint1, json=user)

print(get_response.json())
