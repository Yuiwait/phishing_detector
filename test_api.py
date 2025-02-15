import requests

url = "http://127.0.0.1:5000/predict"
data = {"email": "Your Netflix account is locked. Update your payment details now."}

response = requests.post(url, json=data)
print(response.json())
