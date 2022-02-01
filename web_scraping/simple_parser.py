from turtle import title
import bs4
import requests


LINK = 'https://stawiszynski.org/podcasty/skadinad/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}

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