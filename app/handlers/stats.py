from aiogram.types import Message
from aiogram import Router, F

from app.services.container import stats_service


router = Router()


@router.message(F.text.contains("Статистика"))
async def stats_handler(message: Message):

    text = await stats_service.get_stats(
        user_id=message.from_user.id
    )

    await message.answer(text)
