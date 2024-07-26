from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, EmailStr



class AccountBase(BaseModel):
    email: EmailStr
    phone: int
    address: str

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    account_id: int

    class Config:
        orm_mode = True