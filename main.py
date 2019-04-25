# Alexander Marshall

import metalinjection
import metalarchives
import metalstorm
import decibel
import spotify

# Metal Injection
print('getting new singles from Metal Injection...')
newSongsMI = metalinjection.scrape_headlines()
token = spotify.get_auth_token()
spotify.add_tracks(token, newSongsMI, True)
print('\ngetting new releases from Metal Injection...')
newReleasesMI = metalinjection.scrape_releases()
spotify.add_tracks(token, newReleasesMI, False)

# Decibel Magazine
print('\ngetting Decibel Megazine headlines...')
newSongsDB = decibel.scrape_headlines()
spotify.add_tracks(token, newSongsDB, True)

# MetalStorm
print('\ngetting new releases from MetalStorm...')
newRealeasesMS = metalstorm.scrape_new_releases()
spotify.add_tracks(token, newRealeasesMS, False)

# Metal Archives
print('\ngetting new releases from Metal Archives...')
newRealeasesMA = metalarchives.scrape_new_releases()
spotify.add_tracks(token, newRealeasesMA, False)

print('Done!')