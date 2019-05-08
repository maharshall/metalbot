# Alexander Marshall

import metalstorm
import metalarchives
import spotify

token = 'redacted'
newRealeasesMS = metalstorm.scrape_new_releases()
spotify.add_tracks(token, newRealeasesMS, False)
newRealeasesMA = metalarchives.scrape_new_releases()
spotify.add_tracks(token, newRealeasesMA, False)
