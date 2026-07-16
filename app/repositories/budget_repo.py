from sqlalchemy import select, extract
# from app.db.session import async_session
from app.db.models import Budget


class BudgetRepository:

    def __init__(self, session):
        self.session = session  #repo живет, пока живет session

    async def create_many(self, budget_data):
        # async with async_session() as session:
        budgets = [
            Budget(**data)      # распаковка словаря в именованные аргументы
            for data in budget_data
            ]
        # for data in budget_data:
        #     budgets.append(Budget(**data))

        self.session.add_all(budgets)
        await self.session.commit()

        return budgets

    async def get(self):
        pass
    # async def exists_for_month(self, user_id: int, year: int, month: int):
    #     # start = datetime(year, month, 1)
    #     #
    #     # if month == 12:
    #     #     end = datetime(year + 1, 1, 1)
    #     # else:
    #     #     end = datetime(year, month + 1, 1)
    #     #
    #     # stmt = select(self.model).where(
    #     #     # self.model.user_id == user_id,
    #     #     self.model.date_beg >= start,
    #     #     self.date_beg < end
    #     # )
    #     #
    #     # result = await self.session.execute(stmt)
    #     # return result.scalars().first() is not None
    #     result = await self.session.execute(
    #         select(Budget).where(
    #             extract("year", Budget.date_beg) == year,
    #             extract("month", Budget.date_end) == month
    #         )
    #     )
    #     return result.scalar_one_or_none() is not None
        # obj = result.scalar_one_or_none()
        # if obj is not None:
        #     return True
        # else:
        #     return False

    # async def get(self, dto):
    #     async with async_session() as session:
    #         result = await session.execute(
    #             # запрос к баджет
    #         )
    #         return result.scalar_one_or_none()
