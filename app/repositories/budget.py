from sqlalchemy import select
from datetime import datetime, timedelta
import calendar

from sqlalchemy.sql.functions import current_time

from app.db.models import Budget
from sqlalchemy.ext.asyncio import AsyncSession

# class BudgetRepository:
#
#     def __init__(self):
#         self.model = Budget
#
#     async def exists_for_month(self, session, user_id: int, year: int, month: int):
#         start = datetime(year, month, 1)
#
#         if month == 12:
#             end = datetime(year + 1, 1, 1)
#         else:
#             end = datetime(year, month + 1, 1)
#
#         stmt = select(self.model).where(
#             # self.model.user_id == user_id,
#             self.model.date_beg >= start,
#             self.model.date_beg < end
#         )
#
#         result = await session.execute(stmt)
#         return result.scalars().first() is not None


async def set_the_budget(
    session: AsyncSession,
    user_id: int,
    amount: int
    ) -> None:

    repo = BudgetRepository()

    now = datetime.now()
    year = now.year
    month = now.month

    exists = await repo.exists_for_month(session=session,
                                         user_id=user_id,
                                         year=year,
                                         month=month)


    # ищем первый понедельник
    start = get_first_monday(year, month)

    budgets = []

    current = start
    # генерируем недели
    while True:
        week_start = current
        week_end = current + timedelta(days=6)
        week_end += timedelta(days=1)

        # break, когда неделя полностью ушла за месяц
        if week_start.month > month+1 and week_end.month > month+1:
            break

        budgets.append(
            Budget(
                user_id=user_id,
                amount=amount,
                date_beg=week_start,
                date_end=week_end
            )
        )

        current += timedelta(days=7)

    session.add_all(budgets)
    await session.commit()      # сохранение изменений


def get_first_monday(year: int, month: int) -> 'datetime':
    start = datetime(year, month, 1) # первый день месяца

    # ищем первый понедельник
    while start.weekday() != 0: # 0 - понедельник
        start -= timedelta(days=1)

    return start
