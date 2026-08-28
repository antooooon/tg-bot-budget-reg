from pydantic import BaseModel


class CreateBudgetDTO(BaseModel):
    user_id:int
    # date_beg:datetime
    # date_end:datetime
    amount:int
