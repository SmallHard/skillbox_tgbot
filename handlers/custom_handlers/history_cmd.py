from aiogram.filters import Command
from aiogram.types import Message
import sqlite3 as sq

from api.custom_api.history import history
from loader import dp, db_storage


@dp.message(Command('history'))
async def history_cmd(message: Message):
    await history(message.from_user.username, message.text)
    with sq.connect(db_storage) as dbcon:
        c = dbcon.cursor()
        c.execute(f"SELECT * FROM {message.from_user.username}")

        for usr, com in c.fetchall():
            print(f'Имя пользователя:{usr}, команда:{com}')
            await message.answer(str(f'Имя пользователя:{usr}, команда:{com}'))

