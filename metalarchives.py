# Alexander Marshall

import re
import datetime
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def scrape_new_releases():
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get('https://www.metal-archives.com/release/upcoming')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    songs = []

    now = datetime.datetime.now()
    today = str(now.day)
    if len(today) == 1:
        today = '0'+today

    table = soup.find_all("tbody")
    releases = table[0].find_all("tr")
    for r in releases:
        date = r.find_all("td")[4].text
        day = re.findall(r'\d+', date.split(' ')[1])[0]
        if len(day) == 1:
            day = '0'+day

        if day == today:
            a = r.find_all("a")
            songs.append([a[0].text, a[1].text])
        else:
            break

    driver.quit()
    return songs