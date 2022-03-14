import requests
BASIC_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'
res = requests.delete(BASIC_URL+ENDPOINT)
data = res.json()
print(data)
