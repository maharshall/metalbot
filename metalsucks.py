# Alexander Marshall

import requests
from bs4 import BeautifulSoup

def scrape_articles():
    page = requests.get('http://www.metalsucks.net/')
    soup = BeautifulSoup(page.content, 'html.parser')

    articles = soup.find_all("span", class_="post-title")
    for article in articles:
        print(article.text)