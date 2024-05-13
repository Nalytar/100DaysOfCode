# udemy Course - 100 Days of Code - Python
import json
import datetime

import requests as r

with open('data.json', 'r') as json_file:
	data = json.load(json_file)
	url = data['URL']
	headers = {}
	for key, value in data['HEADER_PARAM'].items():
		headers[key] = value
	print(headers)

query = input("What did you do today as workout?")
response = r.post(url, headers=headers, json={"query": query})

if response.status_code == 200:
	response = response.json()
	print(response)
else:
	print(str(response.status_code) + " " + response.text)

values = {"tabellenblatt1": {
	"date": datetime.datetime.today().strftime("%d/%m/%Y"),
	"time": datetime.datetime.today().strftime("%H:%M:%S"),
	"exercise": response["exercises"][0]["name"],
	"calories": response["exercises"][0]["nf_calories"],
	"duration": response["exercises"][0]["duration_min"]
	}
}

print("--------------------------------------------------------------------------------------------")

with open('data.json', 'r') as json_file:
	data = json.load(json_file)
	url = data["SHEETY"]["URL"]
	headers = {}
	for key, value in data['SHEETY']['HEADER_PARAM'].items():
		headers[key] = value

response = r.post(url, headers=headers, json=values)

if response.status_code == 200:
	r = response.json()
	print(r)
