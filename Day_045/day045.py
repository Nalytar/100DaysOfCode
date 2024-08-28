# udemy Course - 100 Days of Code - Python

"""
Use beatuiful spoup to get Data from Websites, besides from API-Calls.
Used to pull data from html or xml files.
"""
from bs4 import BeautifulSoup

with open("website.html") as file:
	content = file.read()

soup = BeautifulSoup( content, "html.parser" )

for h3 in soup.findAll("h3"):
	print(h3.getText())
	print(h3.get('class'))

header = soup.find("h1", id="name")
print(header)

a_tag = soup.select_one("body p em strong a")
print(a_tag)