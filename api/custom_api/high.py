import os.path
import sys

import json


def find_highest_priced(category, quantity):
    script_dir = os.path.dirname(sys.argv[0])
    with open((os.path.join(script_dir, 'data_json.json')), 'rt', encoding='UTF-8') as json_file:
        data = json.load(json_file)

    if category not in data:
        return f'Категория {category} не найдена.'
    items = sorted(data[category], key=lambda x: x['year']['rating'], reverse=True)[:quantity]

    response = f"Товары или услуги с максимальной стоимостью в категории '{category}':\n"
    for item in items:
        response += f"{item['year']}: {item['rating']}\n"

    return response
