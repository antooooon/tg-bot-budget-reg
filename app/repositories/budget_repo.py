from sqlalchemy import select


class BudgetRepository:

    def __init__(self):
        self.model = Budget

    async def exists_for_month(self, session, user_id: int, year: int, month: int):
        start = datetime(year, month, 1)

        if month == 12:
            end = datetime(year + 1, 1, 1)
        else:
            end = datetime(year, month + 1, 1)

        stmt = select(self.model).where(
            # self.model.user_id == user_id,
            self.model.date_beg >= start,
            self.model.date_beg < end
        )

        result = await session.execute(stmt)
        return result.scalars().first() is not None