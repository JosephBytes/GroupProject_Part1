from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class AccountBase(BaseModel):
    customer_name: str


class AccountCreate(AccountBase):
    account_id: int
    email: str
    phone: int
    address: str


class AccountUpdate(AccountBase):
    customer_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[int] = None
    address: Optional[str] = None


class Account(AccountBase):
    account_id: int
    orders: int

    class Config:
        from_attributes = True