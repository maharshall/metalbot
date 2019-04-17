# Alexander Marshall

import requests
from bs4 import BeautifulSoup

def scrape_articles():
    page = requests.get('https://metalinjection.net/category/new-music')
    soup = BeautifulSoup(page.content, 'html.parser')

    articles = soup.find_all("h2", class_="title")
    for article in articles:
        print(article.text)

def scrape_tours():
    page = requests.get('https://metalinjection.net/category/tour-dates')
    soup = BeautifulSoup(page.content, 'html.parser')

    articles = soup.find_all("h2", class_="title")
    for article in articles:
        print(article.text) 