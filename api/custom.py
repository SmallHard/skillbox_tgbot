from site_API import core


def handle_custom_command(user_input):
    # Парсинг пользовательского ввода
    parts = user_input.split()
    if len(parts) != 5:
        return "Неправильный формат команды. Используйте: /custom <товар> <цена_от> <цена_до> <количество>"

    product_type = parts[1]
    try:
        price_from = float(parts[2])
        price_to = float(parts[3])
        count = int(parts[4])
    except ValueError:
        return "Неверный формат входных данных. Цена должна быть числом, количество - целым числом."

    # Получение данных из внешнего API
    products = core.response()

    # Проверка на ошибки при получении данных
    if products is None:
        return "Ошибка при получении данных с сервера."

    # Вывод результатов
    result = f"Товары '{product_type}' в диапазоне цен от {price_from} до {price_to} руб.:\n"
    for product in products:
        result += f"{product['name']} - {product['price']} руб., Доступность: {'Да' if product['availability'] else 'Нет'}, " \
                  f"Местоположение: {product['location']}\n"

    return result