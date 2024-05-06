import telebot

from api import high, low, custom, getdata
from database.core import add_to_history
from loader import bot


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Введите /help для получения списка команд.")


@bot.message_handler(commands=['low'])
def low_command(message):
    result = low
    bot.reply_to(message, result)
    add_to_history(message.chat.id, '/low')


@bot.message_handler(commands=['high'])
def high_command(message):
    result = high
    bot.reply_to(message, result)
    add_to_history(message.chat.id, '/high')


@bot.message_handler(commands=['custom'])
def custom_command(message):
    result = custom
    bot.reply_to(message, result)
    add_to_history(message.chat.id, '/custom')


@bot.message_handler(commands=['history'])
def history_command(message):
    history = add_to_history(message.chat.id)
    bot.reply_to(message, '\n'.join(history))


bot.polling()
