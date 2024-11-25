from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

balance = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
    [KeyboardButton(text="Balance"), KeyboardButton(text='My Ref')]
])
