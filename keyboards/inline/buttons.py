from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from handlers.custom_handlers import custom_cmd, low_cmd, history_cmd, high_cmd


menu = [
    [InlineKeyboardButton(text="Поиск по своему рейтингу", callback_data="custom_cmd"),
     InlineKeyboardButton(text="Поиск от наивысшего рейтинга к нижнему", callback_data="high_cmd")],
    [InlineKeyboardButton(text="Поиск от низшего рейтинга к низшему", callback_data="low_cmd"),
     InlineKeyboardButton(text="История запросов", callback_data="history_cmd")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
i_exit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])
