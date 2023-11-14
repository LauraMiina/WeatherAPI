import requests
#1. API documentation: https://www.weatherapi.com/docs/

from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("API_KEY")
#2: printing out the current weather of Helsinki
url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Helsinki'
response = requests.get(url)

data = response.json()
print(data)

#print(data.keys())

#3 printing out the country
#print(data['location'].keys())
print(data['location']['country'])

#4 Print out the difference between the current temperature and how warm it feels. Use "It feels ___ degrees colder"
#or "It feels ___ degrees warmer," not negative numbers.
real_temp = data['current']['temp_c']
feel_temp = data['current']['feelslike_c']
temp_difference = real_temp - feel_temp

if temp_difference > 0:
    print(f"It feels {temp_difference:.1f} degrees colder.")
elif temp_difference < 0:
    print(f"It feels {abs(temp_difference):.1f} degrees warmer.")
else:
    print("It feels exactly the same.")

#5 What's the current temperature at Heathrow International Airport? Use the airport's IATA code to search.
url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=iata:LHR'
response2 = requests.get(url)

data2 = response2.json()
#print(data2)

print("The current temperature at Heathrow Airport is", data['current']['temp_c'], "degrees Celcius.")

#6 What URL would I use to request a 3-day forecast at Heathrow?
url = f'http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q=iata:LHR&days=3'

response3 = requests.get(url)
data3= response3.json()
#print(data3)
#print(data3.keys())
print(data3['forecast']['forecastday'])

#7 Print the date of each of the 3 days you're getting a forecast for.
heath_weather = data3['forecast']['forecastday']
for heath in heath_weather:
    print(heath['date'])

#8 Print the maximum temperature of each of the days.
heath_weather = data3['forecast']['forecastday']
for heath in heath_weather:
    date = heath['date']
    max_temp_c = heath['day']['maxtemp_c']
    print(f"In the day of {date}, the maximum temperature is {max_temp_c} Celcius.")

#9 Print only the day with the highest maximum temperature.
heath_weather = data3['forecast']['forecastday']
max_temp = heath_weather[0]['day']['maxtemp_c']
date_temp = heath_weather[0]['date']
for heath in heath_weather[1:]:
        current_max_temp = heath['day']['maxtemp_c']
        if current_max_temp > max_temp:
            max_temp = current_max_temp
            date_temp = heath['date']
print(f"It will be warmest on {date_temp}, and the temperature is estimated to be {max_temp} Celsius.")
