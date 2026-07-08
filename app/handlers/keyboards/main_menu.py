from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💵 Финансы"),
            KeyboardButton(text="📊 Статистика"),
            KeyboardButton(text="📋 to-do лист"),
            KeyboardButton(text="⚙️ Настройка")
            ]
            ],
        resize_keyboard=True
    )