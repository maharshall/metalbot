# Alexander Marshall

import metalstorm
import metalarchives
import spotify

token = spotify.get_auth_token()
newRealeasesMS = metalstorm.scrape_new_releases()
spotify.add_tracks(token, newRealeasesMS, False)
newRealeasesMA = metalarchives.scrape_new_releases()
spotify.add_tracks(token, newRealeasesMA, False)