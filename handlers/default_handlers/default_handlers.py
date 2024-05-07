
from aiogram.filters.command import Command
from aiogram.types import Message


from config_data.config import DEFAULT_COMMANDS
from loader import dp


@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(f'Привет {message.from_user.username}')


@dp.message(Command('help'))
async def cmd_help(message: Message):
    text = [f'/{command} - {desk}' for command, desk in DEFAULT_COMMANDS]
    await message.answer('\n'.join(text))


@dp.message(lambda message: message not in (None, DEFAULT_COMMANDS))
async def cmd_echo(message: Message):
    await message.answer('Команды не существует')
