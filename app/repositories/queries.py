from sqlalchemy import select, func
from app.db.models.transaction import Transaction
#from sqlalchemy.ext.asyncio import AsyncSession

async def get_stats(session):
    result = await session.execute(
        select(
            Transaction.category,
            Transaction.type_exp,
            func.sum(Transaction.amount).label("total")
        )
        .group_by(Transaction.category, Transaction.type_exp)
    )

    return result.all()

#SQL аналог:
#SELECT category, SUM(amount)
#FROM expenses
#.where(Expense.user_id == user_id)  -> WHERE user_id = ?
#GROUP BY category;

# select(func.sum(Expense_DB.amount))       # - сумма
# .where(Expense.type == "expense")         # - отбор по типу

# from datetime import datetime                     # - за месяц
#
# start_month = datetime.now().replace(day=1)
#
# .where(Expense.date >= start_month)



# date_from: datetime | None = None,                            # отбор по дате
#     date_to: datetime | None = None,
# ):
#     query = select(
#         Expance_DB.category,
#         Expance_DB.type_exp,
#         func.sum(Expance_DB.amount).label("total")
#     ).group_by(
#         Expance_DB.category,
#         Expance_DB.type_exp
#     )
#
#     if date_from:
#         query = query.where(Expance_DB.created_at >= date_from)
#
#     if date_to:
#         query = query.where(Expance_DB.created_at <= date_to)