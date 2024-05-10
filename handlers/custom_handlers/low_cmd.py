from aiogram.filters import StateFilter
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from api.custom_api.low import find_lowers_rated
from api.custom_api import low

from loader import dp


class Low(StatesGroup):
    item_low = State()
    coll_low = State()


@dp.message(Command('high'))
async def high_cmd(message: Message, state: FSMContext):
    await state.set_state(Low.item_low)
    await message.answer('Введите услугу')


@dp.message(Low.item_low)
async def high_item(message: Message, state: FSMContext):
    await state.update_data(item=message.text)
    await state.set_state(Low.coll_low)
    await message.answer('Введите кол-во')


@dp.message(Low.coll_low)
async def high_coll(message: Message, state: FSMContext):
    await state.update_data(coll=message.text)
    user_data = await state.get_data()
    items = user_data['item']
    coll_items = int(user_data['coll'])
    result = find_lowers_rated(coll_items, items)
    await message.answer(f'Вы выбрали {items} кол-во {coll_items}')
    print(result)
    await message.answer(result)

    await state.clear()
