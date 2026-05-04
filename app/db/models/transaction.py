from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime
from datetime import datetime
from .base import DataBase
from sqlalchemy import func

class Transaction(DataBase):
    __tablename__ = "transactions"

    id: Mapped[int]         = mapped_column(primary_key=True)
    user_id: Mapped[int]    = mapped_column(Integer)
    #date: Mapped[datetime] = mapped_column(DateTime)
    date: Mapped[datetime]  = mapped_column(DateTime, default=func.now())   # для прода лучше server_default=func.now()
    amount: Mapped[int]     = mapped_column(Integer)
    category: Mapped[str]   = mapped_column(String)
    type_exp: Mapped[str]   = mapped_column(String)
    budget: Mapped[int]     = mapped_column(Integer)

'''from datetime import datetime
from sqlalchemy import func

date: Mapped[datetime] = mapped_column(
    DateTime,
    default=func.now(),
    nullable=False
)'''