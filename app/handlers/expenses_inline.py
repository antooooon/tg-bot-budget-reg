from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_calendar import SimpleCalendar, SimpleCalendarCallback

from app.states import AddExpense
from app.schemas.expense import CreateExpenseDTO
from app.services.container import expense_service
from app.services.logging import put_in_log
from .keyboards.keyboards import income_expense_keyboard, category_select_expense_keyboard, category_select_income_keyboard


router = Router()


@router.callback_query(F.data == "finance")
async def add_expense(callback: CallbackQuery,
                      state: FSMContext):
    await state.update_data(section="finance")
    await state.set_state(AddExpense.waiting_for_type)    # здесь установили состояние
    await callback.message.edit_text(
        f'Укажите тип движения:',
        reply_markup=income_expense_keyboard()
    )
    await callback.answer()


@router.callback_query(AddExpense.waiting_for_type)
async def input_type(callback: CallbackQuery,
                     state: FSMContext):
    await state.update_data(type_exp=callback.data)
    await state.set_state(AddExpense.waiting_for_amount)
    await callback.message.edit_text(text=f"Введите сумму:")
    await callback.answer()


@router.message(AddExpense.waiting_for_amount)
async def input_amount(message: Message,
                       state: FSMContext) -> None:
    await state.update_data(amount=int(message.text))
    await state.set_state(AddExpense.waiting_for_date)
    await message.answer(text=f"Выберете дату:",
                         reply_markup=await SimpleCalendar().start_calendar()
                         )


@router.callback_query(SimpleCalendarCallback.filter())
@put_in_log
async def input_calendar(
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
        await state.set_state(AddExpense.waiting_for_category)

        state_data = await state.get_data()
        expense_type = state_data.get("type_exp")
        message_str = "Выберите категорию:"

        if expense_type == "type_expense":
            await callback.message.edit_text(
                text=message_str,
                reply_markup=category_select_expense_keyboard()
            )

        elif expense_type == "type_income":
            await callback.message.edit_text(
                text=message_str,
                reply_markup=category_select_income_keyboard()
            )

    await callback.answer()


@router.callback_query(AddExpense.waiting_for_category)
@put_in_log
async def input_category(callback: CallbackQuery,
                         state: FSMContext):

    state_data = await state.get_data()
    amount = state_data["amount"]
    type_exp = state_data["type_exp"]
    date = state_data["date"]
    category = callback.data

    dto = CreateExpenseDTO(
        user_id=callback.message.from_user.id,
        amount=amount,
        type_exp=type_exp,
        category=category,
        date=date
        )

    output_message = (f"Данные отправлены ✅\n"
                      f"\tдата:       {date.strftime('%d.%m.%Y')}\n"
                      f"\tсумма:      {amount}\n"
                      f"\tкатегория:  {category}\n")

    await expense_service.create_expense(dto)
    await callback.message.edit_text(text=output_message)
    await callback.answer()
    await state.clear()
