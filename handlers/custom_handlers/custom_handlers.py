from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from api.custom_api.high import find_highest_priced
from loader import dp


class Form(StatesGroup):
    category = State()
    price = State()


# @dp.message(Command('custom'))
# async def cmd_custom(message: Message):
#     await message.answer(f'Привет {message.from_user.username}')


@dp.message(Command('high'))
async def cmd_high(message: Message):
    await Form.category.set()
    await message.answer('Введите категорию товара: ')


@dp.message(Form.category)
async def process_category(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await Form.next()
    await message.answer('Введите кол-во товаров: ')


@dp.message(lambda message: message.text.isdigit(), Form.price)
async def process_price(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = int(message.text)

    async with state.proxy() as data:
        category = data['category']
        price = data['price']

    await state.finish()
    await message.answer(f'Ищем по параметрам: категория {category}, цена {price}')

    await message.answer(find_highest_priced(category, price))


@dp.message(Command('low'))
async def cmd_start(message: Message):
    await message.answer(f'Привет {message.from_user.username}')


@dp.message(Command('history'))
async def cmd_start(message: Message):
    await message.answer(f'Привет {message.from_user.username}')
