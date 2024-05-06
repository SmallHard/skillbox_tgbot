from telebot.types import Message

from loader import bot
from api.getdata import get_data


@bot.message_handler(commands=['getdata'])
def bot_get_data(message: Message):
    data = fetch_and_insert_data()
    bot.send_message(message, f'Получаем данные {data}')
