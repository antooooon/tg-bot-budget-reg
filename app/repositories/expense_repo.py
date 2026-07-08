from app.db.session import async_session
from app.db.models import Transaction


class ExpenseRepository:

    async def create(self, dto):
        async with async_session() as session:
            expense = Transaction(
                user_id=dto.user_id,
                amount=dto.amount,
                category=dto.category,
                type_exp=dto.type_exp,
                date=dto.date
            )

            session.add(expense)
            await session.commit()  # сохранение изменений
            # await session.refresh(expense)

            return expense