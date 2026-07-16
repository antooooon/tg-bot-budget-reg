from pydantic import BaseModel
from datetime import datetime

class CreateBudgetDTO(BaseModel):
    user_id:int
    # date_beg:datetime
    # date_end:datetime
    amount:int