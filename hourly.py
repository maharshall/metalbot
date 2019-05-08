# Alexander Marshall

import metalinjection
import decibel
import spotify

token = 'redacted'
newSongsMI = metalinjection.scrape_headlines()
spotify.add_tracks(token, newSongsMI, True)
newSongsDB = decibel.scrape_headlines()
spotify.add_tracks(token, newSongsDB, True)
