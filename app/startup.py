from app.db.init import db_init


async def startup(bot, config):
    await db_init()

    await bot.set_webhook(
        url=config.telegram.webhook_url,
        secret_token=config.telegram.webhook_secret,
        drop_pending_updates=True,
    )