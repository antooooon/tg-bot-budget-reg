from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.config import DATABASE_URL


# BASE_DIR = Path(__file__).resolve().parent.parent

# DATABASE_URL = "sqlite+aiosqlite:///./expenses.db"      # - здесь путь к БД локально
# DATABASE_URL = (
#     f"sqlite+aiosqlite:///{BASE_DIR / 'expenses.db'}"
# )   # - замена на более боевой вариант. теперь база всегда в одном месте независимо от способа запуска


engine = create_async_engine(url=DATABASE_URL, echo=True)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)
