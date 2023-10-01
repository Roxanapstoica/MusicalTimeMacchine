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
import pprint
from datetime import datetime

URL = "https://www.billboard.com/charts/hot-100/"
date = input("Which year would you like to travel to? (Type the data in this format: YYYY-MM-DD) ")
year = date.split("-")[0]
print(year)
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
    # music_file.write("Position || Song title || Artist\n")
    for i in range(0,len(songs_titles_list)):
        if i%2 == 0:
            song_title_artist = songs_titles_list[i].split('\t')
            music_file.write(f"{song_title_artist[9]} | {song_title_artist[14]}\n")
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


####Using the Spotipy documentation, create a list of Spotify song URIs for the list of song names
# you found from step 1 (scraping billboard 100).
###Spotify URI - The resource identifier that you can enter, for example, in the
# Spotify Desktop client’s search box to locate an artist, album,
# or track. Example: spotify:track:6rqhFgbbKwnb9MLmUQDhG6

user_id = sp.current_user()["id"]

song_uris = []
tracks = []

pp = pprint.PrettyPrinter(indent=4)
with open(file_name,"r") as songs:
    track = songs.readlines()
    # new_playlist = sp.playlist_add_items(playlistid,songs)

for t in track:
    stripped_track = t.strip().split('|')
    track_uri = stripped_track[0]
    tracks.append(track_uri)
# track_uri = list(track_uri)
print(tracks)
print("********************************************************")
print("********************************************************")
for song in tracks:
    print(song)
    result = sp.search(q=f'track:{song} year:{year}', type='track')
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pp.pprint(f"Song {song} doesn't exist in Spotify library. Skipped.")

print(song_uris)

#### Using the Spotipy documentation, create a new private playlist with the name "YYYY-MM-DD Billboard 100",
# where the date is the date you inputted in step 1.
# HINT: You'll need the user id you got from Step 2.
# 2. Add each of the songs found in Step 3 to the new playlist.
# HINT: You'll need the playlist id which is returned as an output once you've successfully
# created a new playlist.

new_playlist = sp.user_playlist_create(user_id, f"{date} Billboard 100", public=False)
playlistid = new_playlist["id"]
print(playlistid)
sp.playlist_add_items(playlistid, song_uris)

# for su in song_uris:
#     sp.playlist_add_items(playlistid,su)