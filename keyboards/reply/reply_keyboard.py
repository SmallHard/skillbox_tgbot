from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Старт'), KeyboardButton(text='Помощь'), KeyboardButton(text='История')],
    [KeyboardButton(text='Поиск от минимального к максимальному'),
     KeyboardButton(text='Поиск от максимального к минимальному')],
    [KeyboardButton(text='Поиск по своим значениям')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню')
