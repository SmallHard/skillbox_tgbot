from api.custom_api.history import history
from loader import dp
from aiogram.types import Message


@dp.message()
async def echo_handler(message: Message) -> None:
    await history(message.from_user.username, message.text)
    try:
        await message.send_copy(chat_id=message.chat.id)
        await message.answer('Такой команды не существует!')
        await message.answer('Введите другую команду!')
    except TypeError:
        await message.answer("Ошибка типа данных")
