import requests

url = "https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=10&query=%D0%A0%D1%8D%D0%BC%D0%B1%D0%BE"

headers = {
    "accept": "application/json",
    "X-API-KEY": "N5YXYK3-NY740B6-MVAH0P2-CM5RZAT"
}

response = requests.get(url, headers=headers)

print(response.text)

