import asyncio
import logging
import sys

from dotenv import load_dotenv
from os import getenv

from aiogram import Dispatcher, Bot, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.handlers.expenses import router as expenses_router
from app.handlers.stats import router as stats_router
from app.handlers.settings import router as settings_router
from app.handlers.keyboards import main_menu_kb


from app.db.init import db_init
from app.services.expense_service import ExpenseService


load_dotenv()
TOKEN = getenv("BOT_TOKEN")


# dp = Dispatcher()
# dp.include_router(expenses_router)
# dp.include_router(stats_router)
# dp.include_router(settings_router)
def create_dispatcher() -> Dispatcher:
    dp = Dispatcher()

    dp["expenses_router"] = ExpenseService()
    dp["stats_router"] = ExpenseService()
    dp["settings_router"] = ExpenseService()

    # dp.include_router(expenses_router)
    # dp.include_router(stats_router)
    # dp.include_router(settings_router)
    return dp



#@form_router.message(CommandStart())
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    '''
    This handler receives messages with `/start` command
    '''
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(
                    f"Добро пожаловать в ТГ Бот, {html.bold(message.from_user.full_name)}! 👋",
                         reply_markup=main_menu_kb(),
                         resize_keyboard=True
                         )





async def main() -> None:
    # await create_tables()
    await db_init()
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    dp = create_dispatcher()
    await dp.start_polling(bot)
    await command_start_handler


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main(), debug=True) 