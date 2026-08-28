from sqlalchemy import select, extract
# from app.db.session import async_session
from app.db.models import Budget


class BudgetRepository:

    def __init__(self, session):
        self.session = session  #repo живет, пока живет session


    async def create_many(self, budget_data):

        budgets = [
            Budget(**data)
            for data in budget_data
            ]

        self.session.add_all(budgets)
        await self.session.commit()

        return budgets


    # async def get(self):
    #     ...
