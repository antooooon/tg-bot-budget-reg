import asyncio

from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

from app.bot.bot_main import create_bot
from app.bot.dispatcher_main import create_dispatcher
from app.config.settings import load_config
from app.db.init import db_init


async def main() -> None:

    await db_init()

    config = load_config()
    bot = create_bot(config)
    dp = create_dispatcher()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
