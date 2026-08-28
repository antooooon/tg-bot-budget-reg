from pydantic import BaseModel
from datetime import datetime


class CreateExpenseDTO(BaseModel):
    user_id:int
    amount:float
    type_exp:str
    category:str
    date: datetime | None = None # поле может быть либо datetime, либо None
