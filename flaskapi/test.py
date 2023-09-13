import requests
import json

url = 'http://127.0.0.1:5000/similarity'
data = {
    "query": "Kids movies available on Disney+"
}
response = requests.post(url, json=data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {json.dumps(response.json(), indent=2)}")

