from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, CallbackQuery
from aiogram_calendar import SimpleCalendar, SimpleCalendarCallback

from .keyboards.common import cancel_kb
from .keyboards.keyboards import income_expense_keyboard
from app.states import AddExpense

from app.schemas.expense import CreateExpenseDTO

from app.services.container import expense_service


router = Router()


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

    print(F.data)

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
    # state_data = await state.get_data()
    # expense_type = state_data.get("type_exp")
    await state.update_data(amount=int(message.text))
    # await state.set_state(AddExpense.waiting_for_category)
    await state.set_state(AddExpense.waiting_for_date)
    await message.answer(text=f"Выберете дату:",
                         reply_markup=await SimpleCalendar().start_calendar()
                         )
    # message_str = "Выберите категорию:"
    # if expense_type == "type_expense":
    #     await message.answer(
    #         message_str,
    #         reply_markup=ReplyKeyboardMarkup(
    #             keyboard=[
    #                 [KeyboardButton(text="Продукты")],
    #                 [KeyboardButton(text="Ежемес.платежи")],
    #                 # [KeyboardButton(text="Коты")],
    #                 [KeyboardButton(text="Досуг/Другое")],
    #                 [KeyboardButton(text="McD")]
    #             ],
    #             resize_keyboard=True
    #         )
    #     )
    # elif expense_type == "type_income":
    #     await message.answer(
    #         message_str,
    #         reply_markup=ReplyKeyboardMarkup(
    #             keyboard=[
    #                 [KeyboardButton(text="Зарплата")],
    #                 [KeyboardButton(text="Аренда квартир")],
    #                 [KeyboardButton(text="Другое")]
    #             ],
    #             resize_keyboard=True
    #         )
    #     )

@router.callback_query(SimpleCalendarCallback.filter())
async def process_calendar(
        callback: CallbackQuery,
        callback_data: SimpleCalendarCallback,
        state: FSMContext
):

    selected, date = await SimpleCalendar().process_selection(
        callback,
        callback_data
    )

    print(selected, date)

    if selected:
        await state.update_data(date=date)

        # await callback.message.answer(
        #     f"Выбрана дата {date.strftime('%d.%m.%Y')}"
        # )

        await state.set_state(AddExpense.waiting_for_category)

    state_data = await state.get_data()
    expense_type = state_data.get("type_exp")
    message_str = "Выберите категорию:"
    if expense_type == "type_expense":
        await callback.message.answer(
            message_str,
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text="Продукты")],
                    [KeyboardButton(text="Ежемес.платежи")],
                    # [KeyboardButton(text="Коты")],
                    [KeyboardButton(text="Досуг/Другое")],
                    [KeyboardButton(text="McD")]
                ],
                resize_keyboard=True
            )
        )
    elif expense_type == "type_income":
        await callback.message.answer(
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

    # await callback.message.answer(text=f"Введите сумму:",
    #                               reply_markup=ReplyKeyboardRemove()
    #                               )
    await callback.answer()


@router.message(AddExpense.waiting_for_category)
async def input_category(message: Message, state: FSMContext):
    # await state.update_data(category=message.text)

    state_data = await state.get_data()     # готовим данные для отправки в БД

    dto = CreateExpenseDTO(
        user_id=message.from_user.id,
        amount=state_data["amount"],
        type_exp=state_data["type_exp"],
        category=message.text,
        date=state_data["date"]
        )

    await expense_service.create_expense(dto)
    await message.answer(f'Данные отправлены ✅',
                         reply_markup=ReplyKeyboardRemove()
                         #reply_markup=cancel_kb()
                         )
    await state.clear()

#
# @router.callback_query()
# async def handle_callback(callback: CallbackQuery):
#     data = callback.data
