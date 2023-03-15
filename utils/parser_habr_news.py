import requests
from bs4 import BeautifulSoup


def get_habr_news(url_theme: str) -> dict:
    habr_url = 'https://habr.com' + url_theme

    req = requests.get(habr_url)

    soup = BeautifulSoup(req.content, 'lxml')

    all_articles = soup.find_all('article', class_='tm-articles-list__item')
    for article in all_articles[:3]:
        url = article.find('a', class_='tm-article-snippet__title-link').get('href')
        title = article.find('a', class_='tm-article-snippet__title-link').find('span').text

    return {'url': url, 'title': title}


# /ru/hub/programming/
# Программирование

# /ru/hub/python/
# Python
