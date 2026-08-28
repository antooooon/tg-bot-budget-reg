from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine

from app.config.settings import load_config


config = load_config()

engine = create_async_engine(url=config.database.url, echo=True)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)
