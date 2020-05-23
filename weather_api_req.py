import requests

########
# Script returns current temperature from http://api.openweathermap.org
########



# Make a get request to get the current weather
response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=<CityName>&units=metric&appid=<yourAPI-key>")


# Print the status code of the response.
data = response.json()
print(data["main"]["temp"])
