from typing import Optional
from pydantic import BaseModel


class AccountBase(BaseModel):
    account_id: int
    customer_name: str


class AccountCreate(AccountBase):
    account_id: int
    customer_name: str
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
    customer_name: str
    email: str
    phone: int
    address: str

    class Config:
        from_attributes = True


class Feedback:
    pass