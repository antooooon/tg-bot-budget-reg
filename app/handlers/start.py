from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.handlers.keyboards.main_menu import main_menu_inlinekb


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    '''
    This handler receives messages with `/start` command
    '''
    await state.clear()
    await message.answer(
                    f"Добро пожаловать в ТГ Бот, {html.bold(message.from_user.full_name)}! 👋",
                         reply_markup=main_menu_inlinekb()
                         )
