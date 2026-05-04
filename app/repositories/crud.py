from app.db.models import Transaction, Budget
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import date, timedelta


async def create_expense(
    session: AsyncSession,
    user_id: int,
    amount: int,
    category: str,
    type_exp: str
    ):

    today = date.today()
    # тут логика определения текущей недели
    week_start = get_week_start(today)  # лучше сделать норм функцию (ниже покажу)

    result = await session.execute(
        select(Budget).where(
            # Budget.user_id == user_id,
            Budget.date_beg == week_start
        )
    )

    budget = result.scalar_one_or_none()

    expense = Transaction(
        user_id=user_id,
        amount=amount,
        category=category,
        type_exp=type_exp,
        budget=budget
        )

    session.add(expense)
    await session.commit()      # сохранение изменений
    await session.refresh(expense)

# CRUD - сокращение от create, read, update, delete


def get_week_start(today: date):
    return today - timedelta(days=today.weekday())
