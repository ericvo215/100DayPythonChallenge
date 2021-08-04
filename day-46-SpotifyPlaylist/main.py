import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
SPOTIFY_CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
#test = "2017-05-15"
URL = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(URL)
print(response)
website_html = response.text
# print(website_html)

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

all_top_songs = soup.find_all("span", class_="chart-element__information__song")
print(all_top_songs[0].string)

artist = soup.find_all("span", class_="chart-element__information__artist")
print(artist[0].string)

songs = [movie.getText() for movie in all_top_songs]

with open("top_song.txt", mode="w") as file:
    for song in songs:
        file.write(f"{song}\n")

# chart-element__information__song font--semi-bold color--primary text--truncate

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
