from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from .base import DataBase


class Role(DataBase):
    __tablename__ = "user_roles"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str] = mapped_column(String)
    non_active: Mapped[bool] = mapped_column(Boolean)