from aiogram.filters import Command
from aiogram.types import Message
from api.custom_api.history import history, history_exited

from loader import dp


@dp.message(Command('history'))
async def history_cmd(message: Message):
    await history(message.from_user.id, message.from_user.full_name, message.chat)
    result_history = await history_exited(message.from_user.id, message.from_user.full_name, message.chat)
    await message.answer(str(result_history))
