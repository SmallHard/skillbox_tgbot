import os

import requests
import json

url = os.getenv('URL')

headers = {
    "accept": "application/json",
    "API_KEY": os.getenv('API_KEY')
}

response = requests.get(url, headers=headers, timeout=15)


def api_core():
    if response.status_code == 200:    
        data = response.json()
        return data
    else:
        print('Ошибка получения данных с сайта. Статус код:', response.status_code)
        print('Текст ответа:', response.text)

