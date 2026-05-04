from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.data.models import DataBase

DATABASE_URL = "sqlite+aiosqlite:///./expenses.db"      # - здесь путь к БД локально

engine = create_async_engine(url=DATABASE_URL, echo=True)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def create_tables():
    async with engine.begin() as conn:                          # with закроет соединения самостоятельно
        await conn.run_sync(DataBase.metadata.create_all)       # тут создается база