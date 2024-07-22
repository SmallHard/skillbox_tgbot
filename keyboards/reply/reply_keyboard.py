from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Старт'), KeyboardButton(text='Помощь'), KeyboardButton(text='История запросов')],
    [KeyboardButton(text='Поиск от наименьшего рейтинга к наибольшему')],
    [KeyboardButton(text='Поиск от наибольшего рейтинга к наименьшему')],
    [KeyboardButton(text='Поиск по своему рейтингу')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню')
