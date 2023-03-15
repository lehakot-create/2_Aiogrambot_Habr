import requests
from bs4 import BeautifulSoup


def get_habr_themes():
    habr_url = 'https://habr.com/ru/hubs/'

    req = requests.get(habr_url)

    # with open('index.html', 'w') as f:
    #     f.write(req.text)

    with open('index.html', 'r') as f:
        data = f.read()

    soup = BeautifulSoup(data, 'lxml')
    # soup = BeautifulSoup(req.content, 'lxml')

    all_hubs = soup.find('div', class_='tm-hubs-list')
    for hub in all_hubs:
        url = hub.find('a', class_='tm-hub__title').get('href')
        title = hub.find('a', class_='tm-hub__title').text
