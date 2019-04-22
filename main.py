# Alexander Marshall

import metalinjection
import metalarchives
import metalstorm
import decibel
import spotify

# Metal Injection
print('getting Metal Injection headlines...')
newSongsMI = metalinjection.scrape_headlines()
token = spotify.get_auth_token()
spotify.add_single(token, newSongsMI)

# Decibel Magazine
print('\ngetting Decibel Megazine headlines...')
newSongsDB = decibel.scrape_headlines()
spotify.add_single(token, newSongsDB)

# MetalStorm
print('\ngetting new releases from MetalStorm')
newRealeasesMS = metalstorm.scrape_new_releases()
spotify.add_release(token, newRealeasesMS)

# Metal Archives
print('\ngetting new releases from Metal Archives...')
newRealeasesMA = metalarchives.scrape_new_releases()
spotify.add_release(token, newRealeasesMA)

print('Done!')