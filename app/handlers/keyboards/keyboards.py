from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def income_expense_keyboard() -> InlineKeyboardMarkup:
    '''Inline keyboard test'''
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💰 Доход", callback_data="type_income")],
            [InlineKeyboardButton(text="💸 Расход", callback_data="type_expense")]
        ]
    )


def category_select_expense_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Продукты", callback_data="store")],
            [InlineKeyboardButton(text="Ежемес.платежи", callback_data="utility")],
            [InlineKeyboardButton(text="McD", callback_data="mcd")],
            [InlineKeyboardButton(text="Досуг/Другое", callback_data="others")]
        ]
    )


def category_select_income_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Зарплата", callback_data="salary")],
            [InlineKeyboardButton(text="Аренда квартир", callback_data="renting")],
            [InlineKeyboardButton(text="Другое", callback_data="others")]
        ]
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


def settings_family_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Указать состав")],
            [KeyboardButton(text="Посмотреть состав")]
        ],
        resize_keyboard=True
    )
