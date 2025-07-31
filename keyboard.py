from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/en")],
        [KeyboardButton(text="/zh-cn"), KeyboardButton(text="/ru")]
    ],
    resize_keyboard=True
)