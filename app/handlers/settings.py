from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from app.states import AddSettings

from app.handlers.keyboards import settings_type_keyboard
from app.handlers.keyboards import settings_budget_type_keyboard
from app.handlers.keyboards import settings_family_type_keyboard

from app.schemas.budget import CreateBudgetDTO

from app.services.container import budget_service


router = Router()


@router.message(F.text.contains("⚙️ Настройка"))
async def set_settings(message: Message, state: FSMContext):
    await state.set_state(AddSettings.waiting_for_settings_type)
    await message.answer(text='Что нужно настроить?',
        reply_markup=settings_type_keyboard()
    )


@router.message(AddSettings.waiting_for_settings_type)
async def settings_type(message: Message, state: FSMContext):
    if message.text == "Настройки бюджета":
        await state.set_state(AddSettings.waiting_for_budget_type)
        await message.answer(text='Выберите тип настроек бюджета',
            reply_markup=settings_budget_type_keyboard()
        )
    elif message.text == "Настройки состава семьи":
        await state.set_state(AddSettings.waiting_for_family_type)
        await message.answer(text='Выберите тип настроек состава семьи',
            reply_markup=settings_family_type_keyboard()
        )


@router.message(AddSettings.waiting_for_budget_type)
async def settings_budget_types(message: Message, state: FSMContext):
    if message.text == "Указать бюджет":
        await state.set_state(AddSettings.getting_budget_amount)
        await message.answer(text=f"Введите сумму бюджета на каждую неделю месяца:",
                             reply_markup=ReplyKeyboardRemove()
                             )
    elif message.text == "Посмотреть бюджет":
        await state.set_state(AddSettings.requesting_from_db)
        await message.answer(text=f"Бюджет указан в разрезе недели",
                             reply_markup=ReplyKeyboardRemove()
                             )


@router.message(AddSettings.getting_budget_amount, F.text.regexp(r"^\d*$"))
async def settings_processing_amount(message: Message, state: FSMContext):

    if not message.text.isdigit():
        await message.answer(
            "Введите число"
        )
        return

    await state.update_data(
        budget_amount=int(message.text)
    )

    state_data = await state.get_data()

    # date_beg=datetime.now()
    # date_end=datetime.now()

    # по умолчанию заполняется текущий и следующий месяц в разрезе недель
    dto = CreateBudgetDTO(
        user_id=message.from_user.id,
        # date_beg=date_beg,
        # date_end=date_end,
        amount=state_data["budget_amount"]
        )

    await budget_service.set_the_budget(dto=dto)

    # await state.set_state(AddSettings.post_to_db)
    await message.answer(f'Данные отправлены ✅',
                         reply_markup=ReplyKeyboardRemove()
                         )
    await state.clear()


@router.message(AddSettings.getting_budget_amount)
async def invalid_amount(message: Message):

    await message.answer(
        "Введите корректное число"
    )
