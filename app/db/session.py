from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


DATABASE_URL = "sqlite+aiosqlite:///./expenses.db"      # - здесь путь к БД локально

engine = create_async_engine(url=DATABASE_URL, echo=True)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)
