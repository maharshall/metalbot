# Alexander Marshall

import requests
import random
import spotipy
import spotipy.util as util

username = 'username'
playlist_id = 'playlist_id'
client_id = 'client_id'
client_secret = 'client_secret'
redirect_uri = 'redirect_uri'

def get_auth_token():
    scope = ('playlist-read-private playlist-read-collaborative '
             'playlist-modify-public playlist-modify-private'
    )

    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

    if token:
        return token
    else:
        return None

def seek_and_destroy(token, queries):
    sp = spotipy.Spotify(auth=token)
    tracks = sp.user_playlist_tracks(username, playlist_id)

    for q in queries:
        query = q[0]+' '+q[1]
        result = sp.search(query, limit=1, type='track')

        if len(result['tracks']['items']) > 0:
            for track in tracks['items']:
                if track['track']['name'] == result['tracks']['items'][0]['name']:
                    return None

            track_uri = result['tracks']['items'][0]['uri']
            sp.user_playlist_add_tracks(username, playlist_id, {track_uri})