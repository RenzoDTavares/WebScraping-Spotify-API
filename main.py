from logging import exception
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import requests

# BeautifulSoup with Billboard site
def get_data(date):
    response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
    soup = BeautifulSoup(response.text, 'html.parser')
    song_names_h = soup.find_all("h3", {"class": "u-max-width-230@tablet-only"})
    song_names = [song.getText() for song in song_names_h]
    return song_names
  

date = input("What time do you want to travel? Format YYYY-MM-DD: ")
list_of_musics = get_data(date)

# Spotipy API
client_id = 'b5453d04bffd49399d37ea9644b554b3'
client_secret = 'b13f6c0781f7467b952bdee78c6df493'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
playlist_name = f"{date} Billboard 100"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
playlist_id = playlist['id']

for track in list_of_musics:
    try:
        results = sp.search(q='track:' + track, type='track', limit=1)
        URI_track = results['tracks']['items'][0]['uri']          
        playlist_add = sp.playlist_add_items(playlist_id=playlist_id, items=[URI_track], position=None)
    except:
        print("I can't get this music, let's try the next!")
        


