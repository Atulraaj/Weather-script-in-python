import requests

api_key = "f82acd8ebdfbfa9b1939da060e7a5701"

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    a = round((temp - 32) * 5.0/9.0)
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {a}ºC")