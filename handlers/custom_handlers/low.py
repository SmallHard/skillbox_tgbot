from telebot.types import Message

from loader import bot
from api.getdata import fetch_and_insert_data


@bot.message_handler(commands=['getdata'])
def bot_low_data(message: Message):
    data = fetch_and_insert_data()
    bot.send_message(message, f'Получаем данные {data}')
