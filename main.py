# Alexander Marshall

import metalinjection
import metalsucks
import metalarchives
import spotify

# print("articles from Metal Injection:")
newSongs = metalinjection.scrape_articles()
token = spotify.get_auth_token()

for s in newSongs:
    query = s[0]+' '+s[1]
    spotify.seek_and_destroy(token, query)

# print("\narticles from MetalSucks:")
# metalsucks.scrape_articles()

# metalarchives.scrape_releases()