import json

import requests

url = "https://api.kinopoisk.dev/v1.4/movie"

headers = {
    "accept": "application/json",
    "X-API-KEY": "N5YXYK3-NY740B6-MVAH0P2-CM5RZAT"
}
response = requests.get(url, headers=headers)
data_response = response.json()


def data_to_json():
    with open('../data.json', 'w', encoding='UTF-8') as outfile:
        json.dump(data_response, outfile)

