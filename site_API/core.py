import os
from requests import status_codes
import requests


def api_core():
    url = os.getenv('URL')
    api_key = os.getenv('API_KEY')

    headers = {
        "accept": "application/json",
        "X-API-KEY": api_key
    }

    response = requests.get(url, headers=headers, timeout=5)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Ошибка получения данных с сайта. Статус код:', response.status_code)
        print('Текст ответа:', response.text)

