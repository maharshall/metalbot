# Alexander Marshall

import metalinjection
import decibel
import spotify

# Metal Injection
print('getting Metal Injection headlines...')
newSongsMI = metalinjection.scrape_articles()
token = spotify.get_auth_token()

spotify.seek_and_destroy(token, newSongsMI)

# Decibel Magazine
print('getting Decibel Megazine headlines...')
newSongsDB = decibel.scrape_articles()
spotify.seek_and_destroy(token, newSongsDB)

print('Done!')