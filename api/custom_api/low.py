from site_API.core import api_core


def find_lowers_rated(quantity_of_goods, category):
    films_low = []
    rating_low = []
    data = api_core()
    for value in data['docs']:
        if value['genres'][0]['name'] == category:
            films_low.append(value['name'])
            rating_low.append(value['rating']['kp'])

            if len(rating_low) == quantity_of_goods:
                break

    films_low, rating_low = zip(*sorted(zip(films_low, rating_low), key=lambda x: x[1]))
    result_low = list(zip(films_low, rating_low))
    return result_low
