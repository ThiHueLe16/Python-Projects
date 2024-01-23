import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID="Your Client ID"
CLIENT_SECRET="Your Client secret"
user_input_date= input("Which year do you want to have the top 100 Billboard song ? Type the date in this format YYYY-MM-DD:")
url_link=f"https://www.billboard.com/charts/hot-100/{user_input_date}/"
# url_link=f"https://www.billboard.com/charts/billboard-vietnam-top-vietnamese-songs/{user_input_date}/"

# ----------------------------- Create top 100 Song -----------------------------
response=requests.get(url_link)
contents=response.text
# print(contents)

soup= BeautifulSoup(contents, "html.parser")
data=soup.select("li ul li h3")
top100Musics=[music.getText().strip() for music in data]
print(top100Musics)

# ----------------------------- Spotify authentication with spotipy- GET USER ID -----------------------------
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private ",
        redirect_uri="https://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="your User Name ",
    )
)
#
user_id = sp.current_user()["id"]

# ----------------------------- Search Spotify for the Songs from top100Musics-----------------------------

song_uris = []
year = user_input_date.split("-")[0]
for song in top100Musics:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f"{song} exists in Spotify")
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# -----------------------------Add top100Musics to song playlist-----------------------------

playlist = sp.user_playlist_create(user=user_id, name=f"{user_input_date} Billboard vietnam 100", public=False)
# print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

current_playlist=sp.current_user_playlists()
print(current_playlist)