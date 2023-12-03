# udemy Course - 100 Days of Code - Python
# Send E-Mail

import smtplib as smtp
import json
import datetime as dt
import random as rng

"""
! Important !
To Use this Programm create a maildata.json like this:
{
	"Email": {
		"eMailFrom": "yourMail",
		"eMailTo": "receiverMail",
		"passwordPy": "password",
		"host": "smtp.yourSerivce.com",
		"port": 587
	}
}
For host settings and password, pls check your provider information
"""

with open("./maildata.json", "r") as data:
	mailData = json.load(data)

with open("./quotes.txt", "r") as qoute:
	quotes = qoute.readlines()

# Mail Data
eMailFrom = mailData["Email"]["eMailFrom"]
eMailTo = mailData["Email"]["eMailTo"]
passwordPy = mailData["Email"]["passwordPy"]
host = mailData["Email"]["host"]
port = mailData["Email"]["port"]

now = dt.datetime.now()

if now.weekday() == 0:
	quote = rng.choice(quotes)

	# Mail Message
	message = f"""From: {eMailFrom}
	To: {eMailTo}
	Subject: New Week Motivation Quote
	
	Motivationquote: 
	{quote}
	"""

	with smtp.SMTP(host, port) as connection:
		# makes the connection secure
		connection.starttls()
		connection.login(eMailFrom, passwordPy)
		#connection.sendmail(from_addr=eMailFrom, to_addrs=eMailTo, msg=message)
