from sqlalchemy.dialects.mysql import NUMERIC
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime
from datetime import datetime
from sqlalchemy import func
from decimal import Decimal

from .base import DataBase


class Transaction(DataBase):
    __tablename__ = "transactions"

    id: Mapped[int]         = mapped_column(primary_key=True)
    user_id: Mapped[int]    = mapped_column(Integer)
    date: Mapped[datetime]  = mapped_column(DateTime, server_default=func.now())
    amount: Mapped[Decimal] = mapped_column(NUMERIC(10, 2))
    category: Mapped[str]   = mapped_column(String)
    type_exp: Mapped[str]   = mapped_column(String)

# '''from datetime import datetime
# from sqlalchemy import func
#
# date: Mapped[datetime] = mapped_column(
#     DateTime,
#     default=func.now(),
#     nullable=False
# )'''