
def format_stats(stats: list[tuple]) -> str:
    income = {}
    expense = {}

    total_income = 0
    total_expense = 0
    total_budget = 0

    lines = []
    for row in stats:

        category, type_exp, amount = row

        if type_exp == "type_income":
            income[category] = amount
            total_income += amount
        elif type_exp == "type_expense":
            expense[category] = amount
            total_expense += amount

        total = total_income - total_expense

        lines.append(f"📊 Твои Финансы за месяц:")
        lines.append(f"Установленный бюджет: {total_budget}")
        lines.append(f"Доход - Расход = {total_income} - {total_expense} = {total}")
        lines.append("")

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
                lines.append(f"- {cat}: {amt}".replace(",", " "))
        else:
            lines.append("нет данных")

    return "\n".join(lines)