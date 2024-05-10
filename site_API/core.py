import os

import requests
import json

url = os.getenv('URL')

headers = {
    "accept": "application/json",
    "X-API-KEY": "N5YXYK3-NY740B6-MVAH0P2-CM5RZAT"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Получаем данные в формате JSON
    data = response.json()

    # Записываем данные в JSON-файл
    with open('data_json.json', 'w', encoding='UTF-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    # Проверяем, что файл был успешно создан и данные записаны
    try:
        with open('data_json.json', 'r', encoding='UTF-8') as json_file:
            json_data = json.load(json_file)
            print("Данные успешно сохранены в файл.")
    except Exception as e:
        print("Ошибка при сохранении данных в файл:", e)
else:
    print('Ошибка получения данных с сайта. Статус код:', response.status_code)
    print('Текст ответа:', response.text)

