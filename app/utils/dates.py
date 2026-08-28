from datetime import date, timedelta


def get_week_start(today: date) -> date:
    return today - timedelta(days=today.weekday())


def get_first_monday(year: int, month: int) -> 'date':
    start = date(year, month, 1)  # первый день месяца

    # ищем первый понедельник
    while start.weekday() != 0:  # 0 - понедельник
        start -= timedelta(days=1)

    return start
