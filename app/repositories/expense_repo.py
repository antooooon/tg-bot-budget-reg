from app.db.session import async_session
from app.db.models import Transaction


class ExpenseRepository:
    def __init__(self, dp_type, dto):
        self.dp_type = dp_type
        self.dto = dto

    async def create(self, dto, budget):
        async with async_session() as session:
            expense = Transaction(
                user_id=dto.user_id,
                amount=dto.amount,
                category=dto.category,
                type_exp=dto.type_exp,
                budget=budget
            )

            session.add(expense)
            await session.commit()  # сохранение изменений
            # await session.refresh(expense)

            return expense

    async def get_budget_by_week(self, week_start):
        async with async_session() as session:
            result = await session.execute(
                #запрос к баджет
            )
            return result.scalar_one_or_none()