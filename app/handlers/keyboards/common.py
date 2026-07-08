from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def cancel_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Вернуться в меню")]
        ],
        resize_keyboard=True
    )
