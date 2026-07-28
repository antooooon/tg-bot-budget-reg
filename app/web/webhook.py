from aiogram.types import Update
from aiohttp.web_response import Response
import asyncio
from flask import Flask, Response, request

from app.bot.bot_main import create_bot
from app.bot.dispatcher_main import create_dispatcher
from app.config.settings import load_config

# from app.bot.runtime import bot, dp, config

config = load_config()

bot = create_bot(config)
dp = create_dispatcher()

flask_app = Flask(__name__)


@flask_app.post(config.telegram.webhook_path)
def webhook():

    if request.headers.get("X-Telegram-Bot-Api-Secret-Token") != config.telegram.webhook_secret:
        return Response("Forbidden", status=403)

    update = Update.model_validate(request.json)
    asyncio.run(dp.feed_update(bot=bot, update=update))

    return Response("ok", status=200)


@flask_app.get("/")
def health():
    return Response("Bot is alive", status=200)


# dp.feed_update() - асинхронный, Flask - синхронный, требуется делать мостик между асинх и синх
# Update - класс для работы с JSON через aiogram(aiogram работает с объектами)
# Update.model_validate(...) - создает dict и Dispatcher понимает этот объект