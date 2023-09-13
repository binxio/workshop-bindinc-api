import requests
import json

url = 'https://flaskapi.com/similarity'
data = {
    "query": "Kids movies available on Disney+"
}
response = requests.post(url, json=data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {json.dumps(response.json(), indent=2)}")

