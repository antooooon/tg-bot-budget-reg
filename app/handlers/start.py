from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.handlers.keyboards.main_menu import main_menu_inlinekb

router = Router()

#@form_router.message(CommandStart())
@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    '''
    This handler receives messages with `/start` command
    '''
    await state.clear()
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(
                    f"Добро пожаловать в ТГ Бот, {html.bold(message.from_user.full_name)}! 👋",
                         reply_markup=main_menu_inlinekb()
                         )