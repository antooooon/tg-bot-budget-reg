from app.repositories.expense_repo import ExpenseRepository


class ExpenseService:
    def __init__(self):
        self.repo = ExpenseRepository()

    async def create_expence(self, dto):
        # валидация (проверка на количество и тип)
        # доп. логика (округление, конвертация и т.д.)
        # вызов репозитория
        return await self.repo.create()

