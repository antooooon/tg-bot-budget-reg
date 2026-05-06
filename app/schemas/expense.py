from pydantic import BaseModel


class CreateExpenseDTO(BaseModel):
    user_id:int
    amount:int
    type_exp:str
    category:str