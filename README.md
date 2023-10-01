# MusicalTimeMacchine
Use Beautiful Soup to scrap the top 100 songs from a particular website from a given date and then creates a playlist in Spotify

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


####Using the Spotipy documentation, create a list of Spotify song URIs for the list of song names
# you found from step 1 (scraping billboard 100).
###Spotify URI - The resource identifier that you can enter, for example, in the
# Spotify Desktop client’s search box to locate an artist, album,
# or track. Example: spotify:track:6rqhFgbbKwnb9MLmUQDhG6

#### Using the Spotipy documentation, create a new private playlist with the name "YYYY-MM-DD Billboard 100",
# where the date is the date you inputted in step 1.
# HINT: You'll need the user id you got from Step 2.
# 2. Add each of the songs found in Step 3 to the new playlist.
# HINT: You'll need the playlist id which is returned as an output once you've successfully
# created a new playlist.
