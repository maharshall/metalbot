# Alexander Marshall

import requests
import random
import webbrowser
import pprint
import spotipy
import spotipy.util as util

username = 'username'
playlist_id = 'playlsit_id'
client_id = 'client_id'
client_secret='client_secret'
redirect_uri='redirect_uri'

def get_auth_token():
    scope = ('playlist-read-private playlist-read-collaborative '
             'playlist-modify-public playlist-modify-private')

    token = util.prompt_for_user_token(
        username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri
    )

    if token:
        return token
    else:
        return None

def seek_and_destroy(token, query):
    sp = spotipy.Spotify(auth=token)
    result = sp.search(query, limit=1, type='track')
    
    if len(result['tracks']['items']) > 0:
        track_uri = result['tracks']['items'][0]['uri']
        results = sp.user_playlist_add_tracks(username, playlist_id, {track_uri})