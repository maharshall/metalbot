# Alexander Marshall

import requests
from bs4 import BeautifulSoup
import re

def scrape_articles():
    # page = requests.get('https://metalinjection.net/category/new-music')
    # soup = BeautifulSoup(page.content, 'html.parser')
    # soup = BeautifulSoup(open("metalinjection.html"), 'html.parser')
    with open('metalinjection.html', 'rb') as html:
        soup = BeautifulSoup(html)

    articles = soup.find_all("h2", class_="title")
    songs = []
    for article in articles:
        if "Track" in article.text or "Song" in article.text:
            title = re.sub(r" ?\([^)]+\)", "", article.text)
            
            artist = re.findall(r"\b[0-9A-Z]{2,}\b", title)
            track = re.findall(r"\"(.+?)\"", article.text)
            
            artist = ' '.join(map(str, artist))
            track = ''.join(map(str, track))
            
            if track:
                # print(artist+" - "+track)
                songs.append([artist, track])
    
    return songs