import requests
import json


url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
data = response.json()

print('Сurrent location of the ISS')
print(f"Time:{data['timestamp']}")
print(f"Latitude{data['iss_position']['latitude']}")
print(f"Longitude{data['iss_position']['longitude']}")
print(f"URL:{url}")

input('Press enter')
url2 = "http://api.open-notify.org/astros.json"
response2 = requests.get(url2)
data2 = response2.json()

print('Ppeople in space')
print(f"Number of people in space: {data2['number']}")
for i, person in enumerate(data2['people'], 1):
    print(f"{i} - {person['name']}; {person['craft']} ")
print(f"URL:{url2}")



