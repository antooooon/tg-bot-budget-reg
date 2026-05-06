from app.repositories.expense_repo import ExpenseRepository
from app.schemas.expense import CreateExpenseDTO


class ExpenseService:
    def __init__(self):
        self.repo = ExpenseRepository()

    async def create_expense(self, dto):
        # валидация (проверка на количество и тип)
        # доп. логика (округление, конвертация и т.д.)
        # вызов репозитория
        budget = 0

        return await self.repo.create(
                        dto=dto,
                        budget=budget)


# handler → DTO → service → repo → DB