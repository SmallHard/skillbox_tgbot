from site_API.core import api_core


def find_custom_rated(custom_low, custom_high, category, count):
    films_custom = []
    data = api_core()
    for value in data['docs']:
        if value['genres'][0]['name'] == category and (custom_low <= value['rating']['kp'] <= custom_high)\
                or custom_low >= value['rating']['kp'] >= custom_high:
            films_custom.append((value['name'], value['rating']['kp']))

            if len(films_custom) == count:
                break

    films_custom.sort(key=lambda x: x[1])

    return films_custom

