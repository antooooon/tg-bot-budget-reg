from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Boolean
from datetime import datetime
from .base import DataBase


class Family(DataBase):
    __tablename__ = "family"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    family_with: Mapped[str] = mapped_column(String)
    reg_date: Mapped[datetime] = mapped_column(DateTime)
    not_active: Mapped[bool] = mapped_column(Boolean)
