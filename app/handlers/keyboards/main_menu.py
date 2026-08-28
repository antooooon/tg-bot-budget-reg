from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, InlineKeyboardButton


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

def main_menu_inlinekb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💵 Финансы", callback_data="finance")],
            [InlineKeyboardButton(text="📊 Статистика", callback_data="stat")],
            [InlineKeyboardButton(text="📋 to-do лист", callback_data="todo")],
            [InlineKeyboardButton(text="⚙️ Настройка", callback_data="settings")]
        ]
    )
