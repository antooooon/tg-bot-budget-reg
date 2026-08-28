from sqlalchemy import select, func, and_
from app.db.models import Transaction, Budget


class StatRepository():

    def __init__(self, session):
        self.session = session


    async def get_stats(self, user_id: int):

        _sql = (
            select(
                Transaction.category,
                Transaction.type_exp,
                func.sum(Transaction.amount).label("total"),
                Budget.amount.label("budget"),
                Budget.date_beg,
                Budget.date_end
            )
            .select_from(Transaction)
            .join(
                Budget,
                and_(
                    Transaction.user_id == Budget.user_id,
                    func.date(Transaction.date).between(
                        Budget.date_beg,
                        Budget.date_end
                    )
                ),
                isouter=True
            )
            .where(
                and_(
                    Transaction.date >= func.date('now', 'start of month'),
                    Transaction.date <= func.date(
                        'now',
                        'start of month',
                        '+1 month',
                        '-1 day'
                    )
                )
            )
            .group_by(
                Transaction.category,
                Transaction.type_exp,
                Budget.date_beg,
                func.strftime('%Y-%m', Transaction.date)
            )
        )

        result = await self.session.execute(_sql)

        return result.all()
