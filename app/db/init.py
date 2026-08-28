from app.db.models import DataBase
from app.db.session import engine


async def db_init() -> None:
    await create_tables()


async def create_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(DataBase.metadata.create_all)
