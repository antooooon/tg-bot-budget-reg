from rich.console import Console
from rich.table import Table


def format_stats(stats: list[tuple]) -> str:
    income = {}
    expense = {}

    total_income = 0
    total_expense = 0
    budget = 0
    balance = 0

    lines = []
    lines.append(f"📊 Финансы за месяц:")
    lines.append("")
    # lines.append(f"Установленный бюджет: {budget}/неделю")
    for row in stats:

        lines.append("-" * 50)

        category, type_exp, amount, budget, budget_beg, budget_end = row

        if type_exp == "type_income":
            income[category] = amount
            total_income += amount
        elif type_exp == "type_expense":
            expense[category] = amount
            total_expense += amount

        balance = budget - total_expense

        lines.append(f"Бюджет с <u>{budget_beg}</u> по <u>{budget_end}</u>: \n= <b>{budget}</b>")
        lines.append("")
        # total = total_income - total_expense

        lines.append(f"💰 Доход:")
        if income:
            for cat, amt in income.items():
                lines.append(f" - {cat}: {amt}".replace(",", " "))
        else:
            lines.append("нет данных")

        lines.append("")

        lines.append("💸 Расход:")
        if expense:
            for cat, amt in expense.items():
                lines.append(f"{cat}: {amt}".replace(",", " "))
        else:
            lines.append("нет данных")

        lines.append(f"Бюджет - Расход:\n= <b>{balance}</b>")

    # < b > Жирный < / b >
    # < i > Курсив < / i >
    # < u > Подчёркнутый < / u >
    # < s > Зачёркнутый < / s >

    # lines.append(f"Доход: {total_income}")
    # lines.append(f"Расход: {total_expense}")
    # lines.append(f"Бюджет: {budget}/неделю")

    # lines.append(f"Доход - Расход = {total_income} - {total_expense} = {total}")
    # lines.append(f"Бюджет - Расход = {budget} - {total_expense} = {balance}")
    # lines.append("")

    return "\n".join(lines)