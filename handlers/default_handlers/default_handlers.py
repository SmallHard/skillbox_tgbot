from aiogram import F
from aiogram.filters.command import Command
from aiogram.types import Message
import sqlite3 as sq

import keyboards.reply.reply_keyboard as kb_r
from api.custom_api.history import history
from config_data.config import DEFAULT_COMMANDS
from database.core import db_start
from handlers.custom_handlers.custom_cmd import custom_cmd
from handlers.custom_handlers.high_cmd import high_cmd
from handlers.custom_handlers.history_cmd import history_cmd
from handlers.custom_handlers.low_cmd import low_cmd
from loader import dp, db_storage


@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(f'Привет {message.from_user.username}',
                         reply_markup=kb_r.main_button)
    await db_start(message.from_user.username)
    await history(message.from_user.username, message.text)


@dp.message(F.text.lower() == 'старт')
async def key_start(message: Message):
    await cmd_start(message)
    await history(message.from_user.username, message.text)


@dp.message(Command('help'))
async def cmd_help(message: Message):
    text = [f'/{command} - {desk}' for command, desk in DEFAULT_COMMANDS]
    await message.answer('\n'.join(text))
    await db_start(message.from_user.username)
    await history(message.from_user.username, message.text)


@dp.message(F.text.lower() == 'помощь')
async def key_help(message: Message):
    await cmd_help(message)
    await history(message.from_user.username, message.text)


@dp.message(F.text.lower() == 'поиск по своему рейтингу')
async def key_help(message: Message):
    await custom_cmd(message)
    await history(message.from_user.username, message.text)


@dp.message(F.text.lower() == 'история запросов')
async def key_history(message: Message):
    await history_cmd(message)
    await history(message.from_user.username, message.text)


@dp.message(F.text.lower() == 'поиск от наибольшего рейтинга к наименьшему')
async def key_low(message: Message):
    await high_cmd(message)
    await history(message.from_user.username, message.text)


@dp.message(F.text.lower() == 'поиск от наименьшего рейтинга к наибольшему')
async def key_low(message: Message):
    await low_cmd(message)
    await history(message.from_user.username, message.text)



