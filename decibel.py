# Alexander Marshall

import requests
from bs4 import BeautifulSoup
import re

def scrape_articles():
    page = requests.get('https://www.decibelmagazine.com/category/track-premiere/', headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, 'html.parser')
    
    file = open('decibel.txt', 'r')
    headline = file.readline()
    file.close()
    
    articles = soup.find_all("h3")
    songs = []
    
    for article in articles:
        if article.text == headline:
            break
        title = article.a.text.strip()
        if "Track" in title:
            artist = re.findall(r"(?<=: )[a-zA-Z0-9\s]+(?= -)", title)
            track = re.findall(r"(?<=\‘)[a-zA-Z0-9\s]+(?=\’)", title)
            
            artist = ''.join(map(str, artist))
            track = ''.join(map(str, track))
            
            if track:
                songs.append([artist, track])

    file = open('decibel.txt', 'w')
    file.write(articles[0].a.text.strip())
    file.close()
    
    return songs