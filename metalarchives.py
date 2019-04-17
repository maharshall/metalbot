# Alexander Marshall

import requests
from bs4 import BeautifulSoup

def scrape_releases():
    page = requests.get('https://www.metal-archives.com/release/upcoming', headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, 'html.parser')

    print(soup.prettify())