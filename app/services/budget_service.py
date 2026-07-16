from app.repositories.budget_repo import BudgetRepository
from app.db.session import async_session
from datetime import date, timedelta
from app.utils.dates import get_first_monday

class BudgetService:

    # def __init__(self):
    #     self.repo = BudgetRepository()
    #     self.session = ... плохо, потому что будет многопоточность,
    #                    проблемы с rollback, может протухнуть

    async def set_the_budget(self, dto):

        # Почему service слой создает session?
        # потому что service знает границы бизнес операций
        async with async_session() as session:    # dependency lifetime
            repo = BudgetRepository(session=session)

            today = date.today()
            year = today.year
            month = today.month

            start = get_first_monday(year, month)

            budgets=[]

            current = start

            while True:

                week_start = current
                week_end = current + timedelta(days=6)
                # week_end += timedelta(days=1)

                # break, когда неделя полностью ушла за месяц
                if week_start.month > month + 1 and week_end.month > month + 1:
                    break

                budgets.append(
                        {
                        "user_id": dto.user_id,
                        "amount": dto.amount,
                        "date_beg": week_start,
                        "date_end": week_end
                        }
                    )
                current += timedelta(days=7)

            await repo.create_many(budget_data=budgets)

    async def get_the_budget(self):
        pass


    # async def budget_per_week(self, week_start):
    #     result = await session.execute(
    #         select(Budget).where(
    #             # Budget.user_id == user_id,
    #             Budget.date_beg == week_start
    #         )
    #     )
    #     budget = result.scalar_one_or_none()


    # async def get_week_budget(self):






