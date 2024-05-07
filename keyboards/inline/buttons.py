from telebot import types

from loader import bot
from handlers.custom_handlers import custom, low, high, history
from handlers.default_handlers.default_handlers import help


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для работы с API.")
    markup = types.ReplyKeyboardMarkup()
    btn_help = types.KeyboardButton('Помощь по командам')
    btn_low = types.KeyboardButton('Самая низкая стоимость')
    markup.row(btn_help, btn_low)
    btn_high = types.KeyboardButton('Самая высокая стоимость')
    btn_custom = types.KeyboardButton('Поиск по диапазону значений и кол-ва единиц')
    btn_history = types.KeyboardButton('Показать историю запросов')
    markup.row(btn_high, btn_custom, btn_history)
    bot.send_message(message.chat.id, 'Жду комманду.', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Помощь по командам':
        return help
    elif message.text == 'Самая низкая стоимость':
        return low
    elif message.text == 'Самая высокая стоимость':
        return high
    elif message.text == 'Поиск по диапазону значений и кол-ва единиц':
        return custom
    elif message.text == 'Показать историю запросов':
        return history
