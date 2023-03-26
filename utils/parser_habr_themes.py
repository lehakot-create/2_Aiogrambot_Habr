import requests
from bs4 import BeautifulSoup


def get_habr_themes():
    habr_url = 'https://habr.com/ru/hubs/'

    all_themes = []

    req = requests.get(habr_url)

    soup = BeautifulSoup(req.content, 'lxml')

    all_hubs = soup.find('div', class_='tm-hubs-list')
    for hub in all_hubs:
        url = hub.find('a', class_='tm-hub__title').get('href')
        title = hub.find('a', class_='tm-hub__title').text
        all_themes.append({'url': url, 'title': title})

    return all_themes
