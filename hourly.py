# Alexander Marshall

import metalinjection
import decibel
import spotify

token = spotify.get_auth_token()
newSongsMI = metalinjection.scrape_headlines()
spotify.add_tracks(token, newSongsMI, True)
newSongsDB = decibel.scrape_headlines()
spotify.add_tracks(token, newSongsDB, True)