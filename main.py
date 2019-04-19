# Alexander Marshall

import metalinjection
import metalstorm
import decibel
import spotify

# Metal Injection
print('getting Metal Injection headlines...')
newSongsMI = metalinjection.scrape_headlines()
token = spotify.get_auth_token()
spotify.add_single(token, newSongsMI)

# Decibel Magazine
print('getting Decibel Megazine headlines...')
newSongsDB = decibel.scrape_headlines()
spotify.add_single(token, newSongsDB)

# MetalStorm
print('getting MetalStorm new releases...')
newRealeasesMS = metalstorm.scrape_new_releases()
spotify.add_release(token, newRealeasesMS)

print('Done!')