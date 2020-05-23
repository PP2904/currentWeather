import requests

########
# Script returns current temperature from http://api.openweathermap.org
########



# Make a get request to get the current weather
response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=<CityName>&units=metric&appid=<yourAPI-key>")


# Print the status code of the response.
data = response.json()
print(data["main"]["temp"])




{'coord': {'lon': 11.58, 'lat': 48.14}, 
'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 
'base': 'stations', 
'main': {'temp': 23.2, 'feels_like': 19.66, 'temp_min': 21.67, 'temp_max': 25.56, 'pressure': 1019, 'humidity': 59}, 
'wind': {'speed': 7.23, 'deg': 286}, 'rain': {'1h': 0.85}, 'clouds': {'all': 98}, 'dt': 1590234522, 
'sys': {'type': 3, 'id': 2002112, 'country': 'DE', 'sunrise': 1590204309, 'sunset': 1590260164}, 
'timezone': 7200, 'id': 2867714, 'name': 'Munich', 'cod': 200}