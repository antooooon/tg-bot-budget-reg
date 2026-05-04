from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, DateTime
from datetime import datetime
from .base import DataBase


class Budget(DataBase):
    __tablename__ = "budget"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]    = mapped_column(Integer)
    date_beg: Mapped[datetime] = mapped_column(DateTime)
    date_end: Mapped[datetime] = mapped_column(DateTime)
    amount: Mapped[int] = mapped_column(Integer)
