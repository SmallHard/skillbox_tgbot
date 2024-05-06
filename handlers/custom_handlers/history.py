from telebot.types import Message

from loader import bot

from telebot.types import Message

from loader import bot
from database.core import create_base


@bot.message_handler(commands=['getdata'])
def bot_history_data(message: Message):
    data = create_base(user_id=message.from_user.id)
    bot.send_message(message, f'Получаем данные {data}')
