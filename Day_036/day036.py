# udemy Course - 100 Days of Code - Python

# Starting File
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

import requests, json, datetime
from newsapi import NewsApiClient


def printNews(apikey):
	newsapi = NewsApiClient(apikey)
	all_articles = newsapi.get_everything(q=COMPANY_NAME, language="de")

	for num in range(0, len(all_articles["articles"]) - 1):
		if num < 3:
			string = f"""
			Titel: {all_articles[num]["title"]}
			Beschreibung: {all_articles[num]["description"]}
			"""

			print(string)
		else:
			break


with open("data.json", "r") as auth_data:
	data = json.load(auth_data)
	function = data["STOCK_API"]["FUNCTION"]
	symbol = data["STOCK_API"]["SYMBOL"]
	stock_apikey = data["STOCK_API"]["API_KEY"]

	news_apikey = data["NEWS_API"]["API_KEY"]

url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={stock_apikey}"
"""
https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=DTVEAZDX9PDRU42M
"""
requested_data = requests.get(url)
requested_data.raise_for_status()

data = requested_data.json()
# print(data)

yesterday = (datetime.datetime.now() - datetime.timedelta(1)).strftime('%Y-%m-%d')
day_before = (datetime.datetime.now() - datetime.timedelta(2)).strftime('%Y-%m-%d')

open_yesterday = round(float(data["Time Series (Daily)"][yesterday]["1. open"]), 2)
open_day_before = round(float(data["Time Series (Daily)"][day_before]["1. open"]), 2)
percentage = round((open_day_before * 100 / open_yesterday) - 100, 2)
# print(percentage)


if open_yesterday > open_day_before:
	print(f"Stock went up 🔺{percentage}%")
	printNews(news_apikey)
elif open_yesterday < open_day_before:
	print(f"Stock went down🔻{percentage}%")
	printNews(news_apikey)
else:
	print("No Changes")
