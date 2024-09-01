from bs4 import BeautifulSoup
import requests

url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

list_of_title = soup.select('h3.title')
list_of_title.reverse()

if len(list_of_title) > 0:
	with open('100_movies_to_watch.txt', 'w', encoding='utf-8') as file:

		print('Start writing to file...')

		for title in list_of_title:
			file.write(title.text + '\n')

		print('Finished writing to file...')

print("Finish")
