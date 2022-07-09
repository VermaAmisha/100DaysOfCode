import requests

response = requests.get(url="http://open-notify.org/Open-Notify-API/ISS-Location-Now/")

print(response.status_code)
if response.status_code != 200:
    raise Exception("Bad response from ISS API")
    
elif response.status_code == 404:
    raise Exception("That resource does not exist")
 
elif response.status_code == 401:
    raise Exception("You are not authorised to access data")

