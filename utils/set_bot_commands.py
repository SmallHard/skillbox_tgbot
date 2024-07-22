from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config_data.config import DEFAULT_COMMANDS


async def set_default_commands(bot):
    await bot.set_my_commands(
        [BotCommand(command=command, description=description) for command, description in DEFAULT_COMMANDS]
    )
