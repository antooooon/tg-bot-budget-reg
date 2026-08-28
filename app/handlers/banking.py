from aiogram import Router
from aiogram.types import Message
from app.parsers.bank_message_parser import parse_bank_message
from app.schemas.expense import CreateExpenseDTO
from app.services.container import expense_service


router = Router()


@router.message()
async def bank_message(message: Message):

    if message.text.startswith("Payment"):

        parsed = parse_bank_message(message.text)

        dto = CreateExpenseDTO(
            user_id=message.from_user.id,
            amount=parsed.amount,
            category=parsed.category,
            type_exp="type_expense",
            date=parsed.payment_date
        )

        await expense_service.create_expense(dto=dto)
