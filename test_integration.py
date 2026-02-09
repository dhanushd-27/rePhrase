import requests
import json

url = "http://localhost:8000/rewrite"
payload = {
    "Intent": "Make it more formal",
    "Text": "Hey wats up, wanna hang out?",
    "Style": "unchanged"
}
headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    print("Response Code:", response.status_code)
    print("Response JSON:", response.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)
