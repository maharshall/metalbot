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

def add_tracks(token, queries, isSingle):
    sp = spotipy.Spotify(auth=token)
    playlist_id = singles if isSingle else releases

    for q in queries:
        query = q[0]+' '+q[1]
        album = sp.search(query, limit=1, type='album')
        if len(album['albums']['items']) > 0:
            result = sp.album_tracks(album['albums']['items'][0]['uri'])

            if len(result['items']) > 0:
                if track_not_in_playlist(sp, playlist_id, result['items'][0]['id']):
                    track_uri = result['items'][0]['uri']
                    sp.user_playlist_add_tracks(username, playlist_id, {track_uri})
                    
                    if isSingle:
                        print('-> added \''+result['items'][0]['name']+'\' to singles')
                    else:
                        print('-> added \''+result['items'][0]['name']+'\' to releases')

def track_not_in_playlist(sp, playlist_id, track_id):
    total_tracks = sp.user_playlist(username, playlist_id)['tracks']['total']
    
    for i in range(0, total_tracks, 100):
        tracks = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=i)
        for track in tracks['items']:
            if track['track']['id'] == track_id:
                return False
    return True