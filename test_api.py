import requests

url = "https://www.themealdb.com/api/json/v1/1/random.php"

response = requests.get(url)

print("Status code:", response.status_code)

data = response.json()

print(data)