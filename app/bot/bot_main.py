from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


def create_bot(config) -> Bot:

    # print(config.telegram.bot_token)
    return Bot(
        token=config.telegram.bot_token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )