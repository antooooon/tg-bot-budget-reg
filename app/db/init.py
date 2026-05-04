from app.repositories.base import create_tables

async def db_init() -> None:
    await create_tables()