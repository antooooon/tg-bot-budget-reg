from aiohttp.web_response import Response
from flask import Flask, Response, request
from app.main import WEBHOOK_PATH

flask_app = Flask()

@flask_app.route(WEBHOOK_PATH, methods=["POST"])
def webhook():
    if request.headers.get("X-Telegram-Bot-Api-Secret-Token") != WEBHOOK_SECRET:
        return Response("Forbidden", status=403)
    # update = Update.model_validate(request.json)
    # asyncio.run(dp.feed_update(bot=bot, update=update))
    return Response("ok", status=200)

@flask_app.route("/", methods=["GET"])
def health():
    return Response("Bot is alive", status=200)