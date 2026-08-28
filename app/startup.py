from app.db.init import db_init


async def start_up(bot, config):
    await db_init()

    await bot.set_webhook(
        url=config.webhook_url,
        secret_token=config.telegram.webhook_secret,
        drop_pending_updates=True,
    )