import sys
import asyncio
import logging
from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, r"C:\Users\Anton\PycharmProjects\PythonProject\TG_Bot") # ← то же самое

logging.basicConfig(level=logging.INFO)

from flask import Flask, request, Response
from aiogram.types import Update
from app.main import TOKEN, WEBHOOK_PATH, WEBHOOK_SECRET, create_dispatcher
from app.db.init import db_init
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = create_dispatcher()

asyncio.run(db_init())
asyncio.run(bot.set_webhook(
    url=f"{__import__('os').getenv('WEBHOOK_HOST')}{WEBHOOK_PATH}",
    secret_token=WEBHOOK_SECRET,
    drop_pending_updates=True,
))

flask_app = Flask(__name__)

@flask_app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    if request.headers.get("X-Telegram-Bot-Api-Secret-Token") != WEBHOOK_SECRET:
        return Response("Forbidden", status=403)
    update = Update.model_validate(request.json)
    asyncio.run(dp.feed_update(bot=bot, update=update))
    return Response("ok", status=200)

@flask_app.route("/", methods=["GET"])
def health():
    return Response("Bot is alive", status=200)

application = flask_app
# Это нужно WSGI-серверу.
# Когда PythonAnywhere запускает приложение, он делает "import wsgi"
# Дальше он ищет в модуле переменную "application" (потому что по стандарту WSGI приложение называется именно так.)
# и начинает передавать ей HTTP-запросы.