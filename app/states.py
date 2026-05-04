from aiogram.fsm.state import State, StatesGroup

class AddExpense(StatesGroup):
    waiting_for_type = State()
    waiting_for_amount = State()
    waiting_for_category = State()
    post_to_db = State()


class AddSettings(StatesGroup):
    waiting_for_settings_type = State()         # ждем выбора типа настроек     - бюджет/семья
    waiting_for_budget_type = State()           # состояние - бюджет. Показать/установить
    waiting_for_family_type = State()
    waiting_for_budget_amount = State()
    getting_budget_amount = State()
    post_to_db = State()
    requesting_from_db = State()

class AddStatistics(StatesGroup):
    waiting_for_stat_type = State()
