# Alexander Marshall

import requests
from bs4 import BeautifulSoup
import re

def scrape_headlines():
    page = requests.get('https://metalinjection.net/category/new-music', headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, 'html.parser')
    
    file = open('txt/mi_headlines.txt', 'r')
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

    file = open('txt/mi_headlines.txt', 'w')
    file.write(articles[0].text)
    file.close()
    
    return songs

def scrape_releases():
    page = requests.get('https://metalinjection.net/category/upcoming-releases/heavy-new-releases', headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, 'html.parser')
    
    file = open('txt/mi_releases.txt', 'r')
    headline = file.readline()
    file.close()

    articles = soup.find_all("h2", class_="title")
    songs = []

    for article in articles:
        if article.text == headline:
            break

        a = article.find('a')
        page2 = requests.get(a['href'], headers={'User-Agent':'Mozilla/5.0'})
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        releases = soup2.find_all('h3')

        for i in range(4, len(releases)):
            if releases[i].text == 'Related Posts':
                break

            title = releases[i].text.replace(u'\xa0',' ')
            release = title.split(' – ')
            if len(release) == 2:
                songs.append([release[0], release[1]])
        

    file = open('txt/mi_releases.txt', 'w')
    file.write(articles[0].text)
    file.close()

    return songs