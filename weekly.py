# Alexander Marshall

import metalinjection
import spotify

token = 'redacted'
newReleasesMI = metalinjection.scrape_releases()
spotify.add_tracks(token, newReleasesMI, False)
