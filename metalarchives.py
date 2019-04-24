# Alexander Marshall

from bs4 import BeautifulSoup
import datetime
import dryscrape
import pprint
import re
import requests

def scrape_new_releases():
    sess = dryscrape.Session()
    sess.set_attribute('auto_load_images', False)
    sess.visit('https://www.metal-archives.com/release/upcoming')
    sess.wait_for(lambda: sess.at_css("tr.odd"))
    soup = BeautifulSoup(sess.body(), 'html.parser')
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