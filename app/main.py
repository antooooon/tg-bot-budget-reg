import asyncio
import logging
import sys

from dotenv import load_dotenv
from os import getenv

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from app.handlers.start import router as start_router
from app.handlers.stats import router as stats_router
from app.handlers.settings import router as settings_router
from app.handlers.common import router as common_router
from app.handlers.banking import router as banking_router

from app.handlers.expenses_inline import router as expenses_router

from app.db.init import db_init
from app.config import load_config


load_dotenv() # после load_dotenv() переменные уже лежат в os.environ, как будто их изначально передала операционная система.

TOKEN = getenv("BOT_TOKEN")

WEBHOOK_HOST = getenv("WEBHOOK_HOST")
WEBHOOK_PATH = getenv("WEBHOOK_PATH", "/webhook")
WEBHOOK_SECRET = getenv("WEBHOOK_SECRET")  # любая случайная строка

logger = logging.getLogger(__name__)

# эта функция нужна для PythonAnywhere (wsgi.py будет её вызывать)
def create_app() -> web.Application:
    """Создаём aiohttp-приложение."""
    # config = load_config()

    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )
    dp = create_dispatcher()

    async def on_startup(bot: Bot) -> None:
        await db_init()
        await bot.set_webhook(
            url=f"{WEBHOOK_HOST}{WEBHOOK_PATH}",
            secret_token=WEBHOOK_SECRET,
            drop_pending_updates=True,
        )
        logger.info(f"Webhook set to {WEBHOOK_HOST}{WEBHOOK_PATH}")

    async def on_shutdown(bot: Bot) -> None:
        await bot.delete_webhook()
        logger.info("Webhook deleted")

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    app = web.Application()
    SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET,
    ).register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)

    return app
    #
    # # Сохраняем config в dp для доступа из хендлеров через bot.get
    # dp["config"] = config


def create_dispatcher() -> Dispatcher:
    dp = Dispatcher()           # Dispatcher в aiogram ведёт себя как словарь (dict-like storage)

    dp.include_router(expenses_router)
    dp.include_router(start_router)
    dp.include_router(stats_router)
    dp.include_router(settings_router)
    dp.include_router(common_router)
    dp.include_router(banking_router)

    return dp


async def main() -> None:
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