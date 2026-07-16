from functools import wraps
from typing import Callable
from datetime import datetime
import traceback


def put_in_log(func: Callable):
    @wraps(func)
    async def wrapper(*args, **kwargs):

        # Ищем FSMContext среди аргументов
        state = kwargs.get("state")

        if state is None:
            for arg in args:
                if arg.__class__.__name__ == "FSMContext":
                    state = arg
                    break

        # Ищем CallbackQuery или Message
        event = None
        for arg in args:
            name = arg.__class__.__name__
            if name in ("CallbackQuery", "Message"):
                event = arg
                break

        user_id = None
        if event:
            if hasattr(event, "from_user"):
                user_id = event.from_user.id
            elif hasattr(event, "message"):
                user_id = event.message.from_user.id

        current_state = None
        state_data = None

        if state:
            current_state = await state.get_state()
            state_data = await state.get_data()

        try:

            result = await func(*args, **kwargs)

            with open("log_file.txt", "a", encoding="utf-8") as log:
                log.write(
                    f"""
{'=' * 60}
Время: {datetime.now()}
Функция: {func.__name__}
Пользователь: {user_id}
State: {current_state}
Data: {state_data}
Результат: OK
{'=' * 60}
                    """
                )

            return result

        except Exception:

            with open(LOG_FILE, "a", encoding="utf-8") as log:
                log.write(
                    f"""
{'=' * 60}
Время: {datetime.now()}
Функция: {func.__name__}
Пользователь: {user_id}
State: {current_state}
Data: {state_data}

ОШИБКА

{traceback.format_exc()}
{'=' * 60}
                    """
                )

            raise

    return wrapper

# 1/ res = func(*args, **kwargs) - получаем coroutine, а не результат выполнения функции
# поэтому async def wrapper(*args, **kwargs):
#     res = await func(*args, **kwargs)
# 2/ wraps нужно передать func ( не было )
# 3/ with open("log_file.txt") as log: - откроет в режиме чтения r
#  и log.write(...) вызовет исключение
#  нужно with open("log_file.txt", "a", encoding="utf-8") as log: / или w
# 4/ хендлер ничего не возвращает, поэтому res = await func(*args, **kwargs) = None
# 5/ файл созд в текущей рабочей директории. т.е рядом с main, если заупскаьб main
#  пример, чтобы создался файл рядом с модулем
#       from pathlib import Path
#       LOG_FILE = Path(__file__).parent / "log_file.txt"
#       with open(LOG_FILE, "a", encoding="utf-8") as log: