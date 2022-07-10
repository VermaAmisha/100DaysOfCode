import requests

response = requests.get(url="http://open-notify.org/Open-Notify-API/ISS-Location-Now/.json")
response.raise_for_status()

data = response.json()

longitude = data["ISS_position"]["longitude"]
latitude = ["ISS_position"]["latitude"]

ISS_position = (longitude , latitude)

print(ISS_position)

