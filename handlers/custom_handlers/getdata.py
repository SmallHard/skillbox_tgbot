import json

from telebot.types import Message

from loader import bot


@bot.message_handler(commands=['getdata'])
def bot_get_data(message: Message):
    file_path = '../../data.json'
    with open(file_path, 'r') as data_file_json:
        data = json.load(data_file_json)

    for key, value in data.items():
        bot.reply_to(message, f'{key}: {value}')

        print(key, ':', value)

