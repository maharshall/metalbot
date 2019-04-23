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
client_secret='client_secret'
redirect_uri='redirect_uri'

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
    tracks = sp.user_playlist_tracks(username, singles)

    for q in queries:
        query = q[0]+' '+q[1]
        album = sp.search(query, limit=1, type='album')
        if len(album['albums']['items']) > 0:
            result = sp.album_tracks(album['albums']['items'][0]['id'])

            if len(result['items']) > 0:
                for track in tracks['items']:
                    if track['track']['name'] == result['items'][0]['name']:
                        return None

                track_uri = result['items'][0]['uri']
                sp.user_playlist_add_tracks(username, singles, {track_uri})
                print('-> added \''+result['items'][0]['name']+'\' to singles')
        else:
            print('-x \''+q[1]+'\' not found on spotify')

def add_release(token, queries):
    sp = spotipy.Spotify(auth=token)
    tracks = sp.user_playlist_tracks(username, releases)

    for q in queries:
        query = q[0]+' '+q[1]
        album = sp.search(query, limit=1, type='album')
        if len(album['albums']['items']) > 0:
            result = sp.album_tracks(album['albums']['items'][0]['uri'], 1, 1)

            if len(result['items']) > 0:
                for track in tracks['items']:
                    if track['track']['name'] == result['items'][0]['name']:
                        return None

                track_uri = result['items'][0]['uri']
                sp.user_playlist_add_tracks(username, releases, {track_uri})
                print('-> added \''+result['items'][0]['name']+'\' to releases')
        else:
            print('-x \''+q[1]+'\' not found on spotify')

def check_track_correct(artist, track, result):
    if track.lower().strip() == result['items'][0]['name'].lower().strip():
        if artist.lower().strip() == result['items'][0]['artists'][0]['name'].lower().strip():
            return True
        else:
            return False
    else:
        return False