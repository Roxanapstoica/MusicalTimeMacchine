### Spotify uses OAuth to allow third-party applications (e.g. our Python code) to access
# a Spotify user's account without giving them the username or password;
## it’s an open standard for authorization and anyone can implement it;
## OAuth is a standard that apps can use to provide client applications with “secure delegated access”.
# OAuth works over HTTPS and authorizes devices, APIs, servers, and applications with access tokens rather than credentials;
## OAuth was created as a response to the direct authentication pattern;
## This pattern was made famous by HTTP Basic Authentication, where the user is prompted for a username and password.
# Basic Authentication is still used as a primitive form of API authentication for server-side applications:
# instead of sending a username and password to the server with each request, the user sends an API key ID and secret.

### Python Spotify modules - Spotipy


from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"
date = input("Which year would you like to travel to? (Type the data in this format: YYYY-MM-DD) ")
CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
URI = os.environ["SPOTIPY_REDIRECT_URI"]
url_date = f"{URL}{date}"

response = requests.get(url_date)
webpage = response.text
soup = BeautifulSoup(webpage,"html.parser")

songs_titles = soup.find_all(name="li", class_='lrv-u-width-100p')
songs_titles_list = [t.getText().replace('\n',' ') for t in songs_titles] ###.replace('\n',' ').replace('\t','')

index = 1
file_name = f"Music_Top_100_{date}.txt"
with open(file_name, "w", encoding="utf-8") as music_file:
    music_file.write("Position || Song title || Artist\n")
    for i in range(0,len(songs_titles_list)):
        if i%2 == 0:
            song_title_artist = songs_titles_list[i].split('\t')
            music_file.write(f"{index}. {song_title_artist[9]}, {song_title_artist[14]}\n")
            index +=1

### solutie Angela:
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]
## string >> Removes spaces at the beginning and at the end of the string

### PART II: Using the Spotipy documentation >>
# to authenticate our Python project with Spotify using the above unique Client ID/ Client Secret
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri= URI,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    show_dialog=True,
    cache_path="token.txt",
    username="b6m4wncptmodxgivjkixv35x5"
))

user_id = sp.current_user()["id"]

####Using the Spotipy documentation, create a list of Spotify song URIs for the list of song names
# you found from step 1 (scraping billboard 100).
sp.user_playlist_create(user_id, "Playlist1", public=False)


