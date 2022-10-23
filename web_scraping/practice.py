import re

import bs4
import requests

URL = "https://habr.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-User': '?1',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Cache-Control': 'max-age=0',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    # 'Dnt': '1',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Connection': 'keep-alive',
    # 'Accept': '*/*',
    # 'Upgrade-Insecure-Requests': '1',
    # 'Referer': 'https://google.com',
    # 'Pragma': 'no-cache',

}

response = requests.get(URL, headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")
KEYWORDS = ['Python', 'IT', 'Java', 'Физика', 'Philips']

articles = soup.find_all("article")
for article in articles:

    title = article.find("h2").find("span").text.strip()
    href = article.find(class_="tm-article-snippet__title-link").attrs["href"]

    data = article.find("time").attrs["title"]
    username = article.find(class_="tm-user-info__username")
    snippet = article.find(class_="tm-article-snippet").text

    for keyword in KEYWORDS:

        regex = re.search(rf'\b{keyword}[^-]\b', snippet)
        if regex:
            print(f'{data} | {title}: {URL}{href}')
            break
