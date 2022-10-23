from pprint import pprint
import bs4
from requests import get
import requests
from fake_headers import Headers

# ссылка с которой будет скрапиться информация
URL = "https://habr.com"

# фейк заголовки для обхода ограничений на сайте
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

# хабы для сравнения в цикле поиска
HUBS = ['Криптовалюты', 'IT-компании', 'Конференции', 'Космонавтика']

# get запрос с выводом в текстовом режиме
response = requests.get(URL, headers=HEADERS)
text = response.text
# в features указываем что парсинг идёт в html странице
soup = bs4.BeautifulSoup(text, features="html.parser")

articles = soup.find_all("article")  # тег в котором будет поиск
for article in articles:
    hubs = article.find_all(class_="tm-article-snippet__hubs-item-link")  # следующий необходимый тег
    hubs = [hub.text.strip() for hub in hubs]  # создаем список с хабами
    print(hubs)
    for hub in hubs:
        if hub in HUBS:
            href = article.find(class_="tm-article-snippet__title-link").attrs["href"]
            title = article.find("h2").find("span").text
            result = f"{title} ==> {URL}{href}"
            print(result)
            # если будет совпадения хабов из сайта с нашими хабами из списка
            # то программа обратится к тегу article и по тегу выведет необходимую нам информацию
            # в нашем случае это название статьи и ссылка на неё
