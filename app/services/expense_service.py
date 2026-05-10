from app.repositories.expense_repo import ExpenseRepository
from app.services.budget_service import BudgetService
from app.utils.dates import get_week_start

from datetime import date


class ExpenseService:
    def __init__(self):
        self.repo = ExpenseRepository()

    async def create_expense(self, dto):
        return await self.repo.create(dto=dto)


# handler → DTO → service → repo → DB
# expense_service → budget_service → budget_repo