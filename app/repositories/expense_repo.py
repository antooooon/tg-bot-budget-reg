from app.db.session import async_session
from app.db.models import Transaction


class ExpenseRepository:


    # def __init__(self, session):
    #     self.session = session


    async def create(self, dto):
        async with async_session() as session:
            expense = Transaction(
                user_id=dto.user_id,
                amount=dto.amount,
                category=dto.category,
                type_exp=dto.type_exp
                # budget=budget
            )

            session.add(expense)
            await session.commit()  # сохранение изменений
            # await session.refresh(expense)

            return expense