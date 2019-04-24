# Alexander Marshall

import requests
import random
import spotipy
import spotipy.util as util
import pprint

username = 'username'
singles = 'playlist_id'
releases = 'playlist_id'
client_id = 'client_id'
client_secret = 'client_secret'
redirect_uri = 'redirect_uri'

def get_auth_token():
    scope = ('playlist-read-private playlist-read-collaborative '
             'playlist-modify-public playlist-modify-private')

    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

    if token:
        return token
    else:
        return None

def add_single(token, queries):
    sp = spotipy.Spotify(auth=token)

    for q in queries:
        query = q[0]+' '+q[1]
        album = sp.search(query, limit=1, type='album')
        if len(album['albums']['items']) > 0:
            result = sp.album_tracks(album['albums']['items'][0]['uri'])

            if len(result['items']) > 0:
                if track_not_in_playlist(sp, singles, result['items'][0]['id']):
                    track_uri = result['items'][0]['uri']
                    sp.user_playlist_add_tracks(username, singles, {track_uri})
                    print('-> added \''+result['items'][0]['name']+'\' to singles')
        else:
            print('-x \''+q[1]+'\' not found on spotify')

def add_release(token, queries):
    sp = spotipy.Spotify(auth=token)

    for q in queries:
        query = q[0]+' '+q[1]
        album = sp.search(query, limit=1, type='album')
        if len(album['albums']['items']) > 0:
            result = sp.album_tracks(album['albums']['items'][0]['uri'], 1, 1)

            if len(result['items']) > 0:
                if track_not_in_playlist(sp, releases, result['items'][0]['id']):
                    track_uri = result['items'][0]['uri']
                    sp.user_playlist_add_tracks(username, releases, {track_uri})
                    print('-> added \''+result['items'][0]['name']+'\' to releases')
        else:
            print('-x \''+q[1]+'\' not found on spotify')

def track_not_in_playlist(sp, playlist_id, track_id):
    tracks = sp.user_playlist_tracks(username, playlist_id)
    for track in tracks['items']:
        if track['track']['id'] == track_id:
            return False
    return True