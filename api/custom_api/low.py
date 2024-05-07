from site_API import core


def handle_low_command(user_input):
    # Парсинг пользовательского ввода
    parts = user_input.split()
    if len(parts) != 3:
        return "Неправильный формат команды. Используйте: /low <товар> <количество>"

    product_type = parts[1]
    try:
        count = int(parts[2])
    except ValueError:
        return "Количество должно быть числом."

    # Получение данных из внешнего API
    products = core.response()

    # Проверка на ошибки при получении данных
    if products is None:
        return "Ошибка при получении данных с сервера."

    # Вывод результатов
    result = f"Товары '{product_type}' отсортированные по цене:\n"
    for product in products:
        result += f"{product['name']} - {product['price']} руб., Доступность: {'Да' if product['availability'] else 'Нет'}, " \
                  f"Местоположение: {product['location']}\n"

    return result
