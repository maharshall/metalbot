# Alexander Marshall

import requests
from bs4 import BeautifulSoup
import re

def scrape_headlines():
    page = requests.get('https://metalinjection.net/category/new-music', headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, 'html.parser')
    
    file = open('metalinjection.txt', 'r')
    headline = file.readline()
    file.close()
    
    articles = soup.find_all("h2", class_="title")
    songs = []
    
    for article in articles:
        if article.text == headline:
            break
        if "Track" in article.text or "Song" in article.text:
            title = re.sub(r" ?\([^)]+\)", "", article.text)
            
            artist = re.findall(r"\b[0-9A-Z]{2,}\b", title)
            track = re.findall(r"\"(.+?)\"", article.text)
            
            artist = ' '.join(map(str, artist))
            track = ''.join(map(str, track))
            
            if track:
                songs.append([artist, track])

    file = open('metalinjection.txt', 'w')
    file.write(articles[0].text)
    file.close()
    
    return songs