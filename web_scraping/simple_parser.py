from turtle import title
import bs4
import requests


LINK = 'https://stawiszynski.org/podcasty/skadinad/'

res = requests.get(LINK)
if res.status_code == 200:
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    els = soup.select('div.raven-post-content')
    for el in els:
        date = el.select_one('a.raven-post-meta-item.raven-post-date')
        title = el.select_one('a.raven-post-title-link')
        if title:
            print(title.text)
        else:
            print(el)
        if date:
            print(date.text)
        print()