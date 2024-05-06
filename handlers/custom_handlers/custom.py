from telebot.types import Message

from loader import bot
from api.custom import handle_custom_command


@bot.message_handler(commands=['custom'])
def bot_get_data(message: Message):
    data = handle_custom_command(user_input=message.text)
    bot.send_message(message, f'Получаем данные {data}')
