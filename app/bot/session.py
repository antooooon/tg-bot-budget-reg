from aiogram.client.session.aiohttp import AiohttpSession


def create_session() -> AiohttpSession:
    return AiohttpSession()