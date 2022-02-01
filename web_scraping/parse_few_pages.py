from requests_html import AsyncHTMLSession


LINK = 'https://www.polskieradio.pl/7/5102/Strona'
asession = AsyncHTMLSession()


async def get_page(page_num: int = 1):
    url = f'{LINK}/{page_num}'
    print(f"Fetching {url} ...")
    return await asession.get(url)


if __name__ == '__main__':    
    page_nums = list(range(1, 23))
    result = asession.run( *[lambda page_num=page_num: get_page(page_num) for page_num in page_nums])
