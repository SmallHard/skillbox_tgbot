
from site_API.core import json_data


def find_highest_rated(quantity_of_goods, category):
    films = []
    rating = []
    for value in json_data['docs']:
        if value['genres'][0]['name'] == category:
            films.append(value['name'])
            rating.append(value['rating']['kp'])

            if len(rating) == quantity_of_goods:
                break

    films, rating = zip(*sorted(zip(films, rating), key=lambda x: x[1], reverse=True))
    return list(zip(films, rating))


