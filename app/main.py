import asyncio
import logging
import sys

from dotenv import load_dotenv
from os import getenv

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.handlers.start import router as start_router
from app.handlers.expenses import router as expenses_router
from app.handlers.stats import router as stats_router
from app.handlers.settings import router as settings_router

from app.db.init import db_init


load_dotenv()
TOKEN = getenv("BOT_TOKEN")

def create_dispatcher() -> Dispatcher:
    dp = Dispatcher()           # Dispatcher в aiogram ведёт себя как словарь (dict-like storage)

    dp.include_router(start_router)
    dp.include_router(expenses_router)
    dp.include_router(stats_router)
    dp.include_router(settings_router)

    return dp


async def main() -> None:
    # await create_tables()
    await db_init()
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )
    # And the run events dispatching
    dp = create_dispatcher()

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main(), debug=True) 