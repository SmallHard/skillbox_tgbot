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


@dp.message(Command('low'))
async def high_cmd(message: Message, state: FSMContext):
    await state.set_state(Low.item_low)
    await message.answer('Введите услугу')


@dp.message(Low.item_low)
async def high_item(message: Message, state: FSMContext):
    await state.update_data(item_low=message.text)
    await state.set_state(Low.coll_low)
    await message.answer('Введите кол-во')


@dp.message(Low.coll_low)
async def high_coll(message: Message, state: FSMContext):
    await state.update_data(coll_low=message.text)
    user_data_low = await state.get_data()
    items = user_data_low['item_low']
    coll_items = int(user_data_low['coll_low'])
    print(items, coll_items)
    result_low = find_lowers_rated(coll_items, items)
    await message.answer(f'Вы выбрали {items} кол-во {coll_items}')
    print(result_low)
    await message.answer(str(result_low))

    await state.clear()
