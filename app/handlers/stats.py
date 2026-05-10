from aiogram.types import Message
from aiogram import Router, F, Dispatcher


router = Router()

@router.message(F.text.contains("Статистика"))
async def stats_handler(message: Message, dp: Dispatcher):

    service = dp["stats_service"]
    text = await service.get_stats(
        user_id=message.from_user.id
    )

    await message.answer(text)


