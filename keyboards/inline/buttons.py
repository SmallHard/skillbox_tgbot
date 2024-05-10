from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


menu = [
    [InlineKeyboardButton(text="Поиск по своему рейтингу", callback_data="custom"),
     InlineKeyboardButton(text="Поиск от наивысшего рейтинга к нижнему", callback_data="high")],
    [InlineKeyboardButton(text="Поиск от низшего рейтинга к низшему", callback_data="low"),
     InlineKeyboardButton(text="История запросов", callback_data="history")],
    [InlineKeyboardButton(text="🔎 Помощь", callback_data="help")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])
