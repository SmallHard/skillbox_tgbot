from aiogram.filters import StateFilter
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from api.custom_api.custom import find_custom_rated
from api.custom_api import custom

from loader import dp


class Custom(StatesGroup):
    item_custom = State()
    coll_custom_low = State()
    coll_custom_high = State()
    count_custom = State()


@dp.message(Command('custom'))
async def custom_cmd(message: Message, state: FSMContext):
    await state.set_state(Custom.item_custom)
    await message.answer('Введите услугу')


@dp.message(Custom.count_custom)
async def item_custom(message: Message, state: FSMContext):
    await state.update_data(count_custom=message.text)
    await state.set_state(Custom.count_custom)
    await message.answer('Введите кол-во элементов:')


@dp.message(Custom.item_custom)
async def item_custom(message: Message, state: FSMContext):
    await state.update_data(item_custom=message.text)
    await state.set_state(Custom.coll_custom_low)
    await message.answer('Введите минимальный рейтинг:')


@dp.message(Custom.coll_custom_low)
async def coll_low_custom(message: Message, state: FSMContext):
    await state.update_data(coll_custom_low=message.text)
    await state.set_state(Custom.coll_custom_high)
    await message.answer('Введите максимальный рейтинг:')


@dp.message(Custom.coll_custom_high)
async def coll_high_custom(message: Message, state: FSMContext):
    await state.update_data(coll_custom_high=message.text)
    user_data = await state.get_data()
    items_custom = user_data['item_custom']
    coll_low = float(user_data['coll_custom_low'])
    coll_high = float(user_data['coll_custom_high'])
    count_custom = int(user_data['count_custom'])
    result = find_custom_rated(coll_low, coll_high, items_custom, count_custom)
    await message.answer(f'Вы выбрали {items_custom} кол-во от {coll_low} до {coll_high}')
    print(result)
    await message.answer(str(result))

    await state.clear()
