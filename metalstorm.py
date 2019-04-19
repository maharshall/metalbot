# Alexander Marshall

import re
import datetime
import requests
import datetime
from bs4 import BeautifulSoup
import pprint

def scrape_new_releases():
    page = requests.get('http://www.metalstorm.net/events/new_releases.php', headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(page.content, 'html.parser')

    now = datetime.datetime.now()
    date = str(now.day)
    if len(date) == 1:
        date = '0'+date
    
    div = soup.find_all("div", class_="padding-10")
    table = div[2].find_all("td")
    songs = []
    
    for i in range(len(table)):
        if i%2 == 0:
            # check date, break if not today
            if table[i].text[:2] != date:
                break
        else:
            # add to list, no regex necesarry
            song = table[i].text.split(' - ')
            songs.append([song[0], song[1]])
    
    return songs