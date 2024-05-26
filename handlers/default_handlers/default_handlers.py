from aiogram.filters.command import Command
from aiogram.types import Message

import keyboards.reply.reply_keyboard as kb_r
import keyboards.inline.buttons as kb_i
from api.custom_api.history import history
from config_data.config import DEFAULT_COMMANDS
from loader import dp


@dp.message(Command('start'))
async def cmd_start(message: Message):
    await history(message.from_user.id, message.from_user.full_name, message.chat)
    await message.answer(f'Привет {message.from_user.username}',
                         reply_markup=kb_r.main_button)
    


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await history(message.from_user.id, message.from_user.full_name, message.chat)
    text = [f'/{command} - {desk}' for command, desk in DEFAULT_COMMANDS]
    await message.answer('\n'.join(text), reply_markup=kb_i.menu)
    