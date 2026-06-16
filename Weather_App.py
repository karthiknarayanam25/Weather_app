import urllib.request
import json

city = input("Enter City Name: ")

try:
    url = f"https://wttr.in/{city}?format=j1"

    response = urllib.request.urlopen(url)

    data = json.loads(response.read())

    temp = data["current_condition"][0]["temp_C"]
    humidity = data["current_condition"][0]["humidity"]
    weather = data["current_condition"][0]["weatherDesc"][0]["value"]

    print("\n------ Weather Report ------")
    print("City:", city)
    print("Temperature:", temp, "°C")
    print("Humidity:", humidity, "%")
    print("Weather:", weather)

except Exception as e:
    print("Error:", e)