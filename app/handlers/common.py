from aiogram import Router, F
from aiogram.types import Message

from aiogram.fsm.context import FSMContext

from .keyboards.main_menu import main_menu_kb


router = Router()


@router.message(F.text == "Отмена")
async def cancel_handler(message: Message, state: FSMContext):

    await state.clear()

    await message.answer(
        "Действие отменено ✅",
        reply_markup=main_menu_kb()
    )
