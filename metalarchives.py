# Alexander Marshall

import requests
import datetime
from bs4 import BeautifulSoup
import re
import pprint

def scrape_new_releases():
    # page = requests.get('https://metalinjection.net/category/new-music', headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(open('metalarchives.html'), 'html.parser')
    songs = []

    now = datetime.datetime.now()
    today = str(now.day)
    if len(today) == 1:
        today = '0'+today

    table = soup.find_all("tbody")
    releases = table[0].find_all("tr")
    for r in releases:
        date = r.find_all("td")[4].text
        day = re.findall('\d+', date.split(' ')[1])[0]
        if len(day) == 1:
            day = '0'+day

        if day == today:
            a = r.find_all("a")
            songs.append([a[0].text, a[1].text])
        else:
            break

    return songs