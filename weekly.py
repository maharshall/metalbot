# Alexander Marshall

import metalinjection
import spotify

token = spotify.get_auth_token()
newReleasesMI = metalinjection.scrape_releases()
spotify.add_tracks(token, newReleasesMI, False)