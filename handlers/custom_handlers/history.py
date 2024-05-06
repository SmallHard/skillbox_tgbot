from telebot.types import Message

from loader import bot

from telebot.types import Message

from loader import bot
from database.core import get_history


@bot.message_handler(commands=['getdata'])
def bot_get_data(message: Message):
    data = get_history(user_id=message.from_user.id)
    bot.send_message(message, f'Получаем данные {data}')
