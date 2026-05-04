from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
    # return InlineKeyboardMarkup(
    #     inline_keyboard=[
    #         [InlineKeyboardButton(text="💵 Финансы", callback_data="main_fin"),
    #          InlineKeyboardButton(text="📊 Статистика", callback_data="main_stat"),
    #          InlineKeyboardButton(text="📋 to-do лист", callback_data="main_todo"),
    #          InlineKeyboardButton(text="📅 Календарь событий", callback_data="main_events")]
    #     ]
    # )

def cancel_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Вернуться в меню")]
        ],
        resize_keyboard=True
    )

def income_expense_keyboard():
    '''Inline keyboard test'''
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💰 Доход", callback_data="type_income"),
             InlineKeyboardButton(text="💸 Расход", callback_data="type_expense")
             ]
        ],
        resize_keyboard=True
    )

def settings_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Настройки бюджета")],
            [KeyboardButton(text="Настройки состава семьи")]
            # [show_admin_keyboard()]
        ],
        resize_keyboard=True
    )


def settings_budget_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Указать бюджет")],
            [KeyboardButton(text="Посмотреть бюджет")]
        ],
        resize_keyboard=True
    )


def settings_budget_refresh():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Обновить бюджет")]
        ],
        resize_keyboard=True
    )


def settings_family_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Указать состав")],
            [KeyboardButton(text="Посмотреть состав")]
        ],
        resize_keyboard=True
    )


def show_admin_keyboard() -> 'KeyboardButton':
    return [KeyboardButton(text="out of order")]