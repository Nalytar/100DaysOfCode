# udemy Course - 100 Days of Code - Python
import json

import requests
import datetime
import smtplib
import time

parameter = {
	"lat": 51.339695,
	"lng": 12.373075,
	"formatted": 0
}

while True:
	respnse = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
	data = respnse.json()
	# print(data)
	sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
	sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

	time_now = datetime.datetime.now()

	issResponse = requests.get(url="http://api.open-notify.org/iss-now.json")
	issResponse.raise_for_status()

	issData = issResponse.json()
	issLat = float(issData["iss_position"]["latitude"])
	issLng = float(issData["iss_position"]["longitude"])
	# print(issLat)
	# print(issLng)

	if parameter["lat"]-5 <= issLat <= parameter["lat"]+5 and parameter["lng"]-5 <= issLng <= parameter["lng"]+5:
		if sunset <= time_now.hour or time_now.hour <= sunrise:
			with open("../Day_032/maildata.json") as data:
				mailData = json.load(data)

			message = \
	f"""From: {mailData["eMailFrom"]}
	To: {mailData["eMailTo"]}
	Subject: ISS is here!
	
	You look up the ISS is near your place!
	Longitude: {issLng}
	Latitude: {issLat}
	"""
			with smtplib.SMTP(mailData["host"], mailData["port"]) as connection:
				connection.starttls()
				connection.login(mailData["eMailFrom"], mailData["passwordPy"])
				connection.sendmail(from_addr=mailData["eMailFrom"], to_addrs=mailData["eMailTo"], msg=message)
		else:
			print("Its not dark enough!")
	else:
		print("ISS is not close enough!")
	time.sleep(60)

# If the ISS is close to my current position, and it is currently dark
# Then send me an email to tel me to look up
# BONUS: run the code every 60 seconds
