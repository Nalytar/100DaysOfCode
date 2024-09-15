# udemy Course - 100 Days of Code - Python
import json

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# URL Top 100 Songs 2020.08.01
url = 'https://www.billboard.com/charts/hot-100/2020-08-01/'

# Fetch Top 100 Songs
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
content = soup.select('.o-chart-results-list__item h3#title-of-a-story')

# for c in content:
# 	print(c.text.strip())

with open('data.json', 'r') as f:
    json_data = json.load(f)
    client_id = json_data.get('client_id')
    client_secret = json_data.get('client_secret')

scope = "playlist-read-private, " \
        "user-read-currently-playing, " \
        "user-read-currently-playing, " \
        "user-follow-read, playlist-modify-private"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        redirect_uri="https://spotify.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username='Nalytar',
    )
)

# Skipped this day, coudnt finish with success after multiplay trys (days)
