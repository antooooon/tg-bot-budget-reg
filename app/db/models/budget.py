from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Date
from datetime import date
from .base import DataBase


class Budget(DataBase):
    __tablename__ = "budget"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]    = mapped_column(Integer)
    date_beg: Mapped[date] = mapped_column(Date)
    date_end: Mapped[date] = mapped_column(Date)
    amount: Mapped[int] = mapped_column(Integer)
