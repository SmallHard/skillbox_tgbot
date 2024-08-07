from aiogram import F
from aiogram.filters import StateFilter
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from api.custom_api.high import find_highest_rated
from api.custom_api import high
from api.custom_api.history import history

from loader import dp


class High(StatesGroup):
    item_high = State()
    coll_high = State()


@dp.message(Command('high'))
async def high_cmd(message: Message, state: FSMContext):
    await state.set_state(High.item_high)
    await message.answer('Введите категорию фильмов')


@dp.message(High.item_high)
async def high_item(message: Message, state: FSMContext):
    await state.update_data(item_high=message.text)
    await state.set_state(High.coll_high)
    await message.answer('Введите кол-во')


@dp.message(High.coll_high)
async def high_coll(message: Message, state: FSMContext):
    await state.update_data(coll_high=message.text)
    user_data = await state.get_data()
    items = user_data['item_high']
    coll_items = int(user_data['coll_high'])
    result = find_highest_rated(coll_items, items)
    await message.answer(f'Вы выбрали {items} кол-во {coll_items}')
    await history(message.from_user.username, message.text)
    await message.answer(str(result))

    await state.clear()


