# udemy Course - 100 Days of Code - Python
import json
import requests as r

with open('data.json', 'r') as json_file:
	data = json.load(json_file)
	url = data['URL']
	headers = {}
	for key, value in data['HEADER_PARAM'].items():
		headers[key] = value
	print(headers)

query = input("What did you do today as workout?")
r = r.post(url, headers=headers, json={"query": query})

if r.status_code == 200:
	print(r.json())
else:
	print(str(r.status_code) + " " + r.text)

#ToDo GoogleSheet API