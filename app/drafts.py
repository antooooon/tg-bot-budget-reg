from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Form(StatesGroup):
    add = State()
    movement_type = State()
    category = State()

@form_router.message(CommandStart())

def main_menu_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Добавить расход/доход", callback_data="fin"),
            InlineKeyboardButton(text="📊 Статистика", callback_data="stats"),
            InlineKeyboardButton(text="to-do лист", callback_data="todo"),
            InlineKeyboardButton(text="Календарь событий", callback_data="events")
            ]
            ],
        #resize_keyboard=True
    )