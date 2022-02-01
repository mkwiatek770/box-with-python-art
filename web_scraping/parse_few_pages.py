"""
HTML Parser, which asynchrously fetches results from many pages
Then parsing is done, which retrieves all article titles.
Finally all retrieved titles are dumped into file.
"""
# TODO: links to articles next to titles
from collections import defaultdict
from requests_html import AsyncHTMLSession


LINK = 'https://www.polskieradio.pl/7/5102/Strona'
IGNORED_TEXTS = ('Dorota Truszczak', 'Historia żywa')
ARTICLES = defaultdict(list)
asession = AsyncHTMLSession()


async def get_page(page_num: int = 1):
    url = f'{LINK}/{page_num}'
    print(f"Fetching {url} ...")
    return await asession.get(url)


def parse_titles(result):
    if result.status_code == 200:
        page_num = int(result.html.url.split(result.html.base_url)[1])
        for h2 in result.html.find(".article h2"):
            text = h2.text
            if h2.text not in IGNORED_TEXTS:
                ARTICLES[page_num].append(h2.text)


def dump_titles_to_file(name):
    with open(name, 'w', encoding='utf-8') as f:
        f.write('Historia żywa - podcasty\n\n')
        for page_num in range(1, len(ARTICLES) + 1):
            articles = ARTICLES.get(page_num, [])
            f.write(f'{page_num}. {LINK}/{page_num}\n')
            for article in articles:
                f.write(f'- {article}\n')
            f.write('\n')


if __name__ == '__main__':    
    page_nums = list(range(1, 23))
    results = asession.run( *[lambda page_num=page_num: get_page(page_num) for page_num in page_nums])

    for result in results:
        parse_titles(result)

    dump_titles_to_file('test.txt')
