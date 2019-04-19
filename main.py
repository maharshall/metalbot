# Alexander Marshall

import metalinjection
import decibel
import spotify

# Metal Injection
print('getting Metal Injection headlines...')
newSongsMI = metalinjection.scrape_articles()
token = spotify.get_auth_token()

for s in newSongsMI:
    query = s[0]+' '+s[1]
    spotify.seek_and_destroy(token, query)

# Decibel Magazine
print('getting Decibel Megazine headlines...')
newSongsDB = decibel.scrape_articles()
for s in newSongsDB:
    query = s[0]+' '+s[1]
    spotify.seek_and_destroy(token, query)

print('Done!')