from aiogram import Router, F, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, CallbackQuery

from app.handlers.keyboards import main_menu_kb, income_expense_keyboard
from app.states import AddExpense

from app.schemas.expense import CreateExpenseDTO


router = Router()


#@router.message(Command("add"))
@router.message(F.text.contains("Финансы"))
async def add_expense(message: Message, state: FSMContext):
    await state.set_state(AddExpense.waiting_for_type)    # здесь установили состояние
    # await message.answer(
    #     reply_markup=ReplyKeyboardRemove()
    # )
    await message.answer(
        f'Укажите тип движения:',
        reply_markup=income_expense_keyboard()
    )


@router.callback_query(AddExpense.waiting_for_type)                     # callback хендлер для inline клавы
async def input_type(callback: CallbackQuery, state: FSMContext):

    type_exp = ""
    if callback.data == "type_income":
        type_exp="type_income"
    elif callback.data == "type_expense":
        type_exp="type_expense"
    await state.update_data(type_exp=type_exp)

    await state.set_state(AddExpense.waiting_for_amount)
    await callback.message.answer(text=f"Введите сумму:",
                                  reply_markup=ReplyKeyboardRemove()
                                  )
    await callback.answer()


@router.message(AddExpense.waiting_for_amount)
async def input_amount(message: Message, state: FSMContext) -> None:
    state_data = await state.get_data()
    expense_type = state_data.get("type_exp")
    await state.update_data(amount=int(message.text))
    await state.set_state(AddExpense.waiting_for_category)
    message_str = "Выберите категорию:"
    if expense_type == "type_expense":
        await message.answer(
            message_str,
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text="Чек")],
                    [KeyboardButton(text="Ком.услуги")],
                    [KeyboardButton(text="Оплата квартиры")],
                    [KeyboardButton(text="Досуг/Другое")]
                ],
                resize_keyboard=True
            )
        )
    elif expense_type == "type_income":
        await message.answer(
            message_str,
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text="Зарплата")],
                    [KeyboardButton(text="Аренда квартир")],
                    [KeyboardButton(text="Другое")]
                ],
                resize_keyboard=True
            )
        )


@router.message(AddExpense.waiting_for_category)
async def input_category(message: Message, state: FSMContext, dp: Dispatcher):
    await state.update_data(category=message.text)

    state_data = await state.get_data()     # готовим данные для отправки в БД

    dto = CreateExpenseDTO(
        user_id=message.from_user.id,
        amount=state_data["amount"],
        type_exp=state_data["type_exp"],
        category=message.text
        )

    service = dp["expense_service"]
    await service.create_expense(dto)
    await message.answer(f'Данные отправлены ✅',
                         reply_markup=ReplyKeyboardRemove()
                         )
    await state.clear()


@router.callback_query()
async def handle_callback(callback: CallbackQuery):
    data = callback.data


@router.message(Command("Cancel"))
async def cancel_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Действие отменено",
        reply_markup=main_menu_kb()
    )