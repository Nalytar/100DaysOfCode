from bs4 import BeautifulSoup
import requests
import operator

# Fetch Side - Public Information
site = requests.get('https://news.ycombinator.com/')

# Create Soup
soup = BeautifulSoup(site.text, 'html.parser')

result_title = soup.select('td.title span.titleline > a')
result_score = soup.select('td.subtext span.subline span.score')

result_dict = {}

print(len(result_title))
print(len(result_score))

# Add Title and current Score
for n in range(0, len(result_title) - 1):
	result_dict[result_title[n].text] = int(result_score[n].text.split()[0])

# Sort by Score
sorted_dict = sorted(result_dict.items(), key=operator.itemgetter(1), reverse=True)

print(sorted_dict)

"""
check site/robots.txt and add delay when scraping websites
"""