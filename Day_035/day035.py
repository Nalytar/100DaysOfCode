# udemy Course - 100 Days of Code - Python

import json
import requests
import os


with open("data.json", "r") as data:
    json_data = json.load(data)
    LAT = json_data["data"]["LAT"]
    LON = json_data["data"]["LON"]
    UNITS = json_data["data"]["UNITS"]
    MODE = json_data["data"]["MODE"]
    LANG = json_data["data"]["LANG"]
    COUNTS = json_data["data"]["COUNTS"]
    API_KEY = json_data["data"]["API_KEY"]

api_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}&mode={MODE}&lang={LANG}&units={UNITS}&cnt={COUNTS}"

respond = requests.get(api_url)
respond.raise_for_status()

wheater_json = respond.json()

rain = False
for weather in wheater_json["list"]:
    if rain:
        break

    for condition in weather["weather"]:
        if rain:
            break

        if int(condition["id"]) < 700:
            print("Wir brauchen einen Regenschirm")
            rain = True

# Create an environment variable
# export NAME_OF_ENV=VALUE
#
# Show environment variables
# env
#
# for PythonAnywhere we need to 'export ENV_VARIABLE=VALUE;'
# ';' for newline/separator for multiple commands

print(os.environ.get("COMPUTERNAME"))
