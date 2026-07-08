from app.repositories.expense_repo import ExpenseRepository
from datetime import datetime


class ExpenseService:
    def __init__(self):
        self.repo = ExpenseRepository()

    async def create_expense(self, dto):
        if dto.date is None:
            dto.date = datetime.now()
        return await self.repo.create(dto=dto)


# handler → DTO → service → repo → DB
# expense_service → budget_service → budget_repo