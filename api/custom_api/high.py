from site_API.core import api_core


def find_highest_rated(quantity_of_goods, category):
    films = []
    rating = []
    data = api_core()
    for value in data['docs']:
        if value['genres'][0]['name'] == category:
            films.append(value['name'])
            rating.append(value['rating']['kp'])

            if len(rating) == quantity_of_goods:
                break

    films, rating = zip(*sorted(zip(films, rating), key=lambda x: x[1], reverse=True))
    result_high = list(zip(films, rating))

    return result_high
