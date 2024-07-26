from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class PaymentBase(BaseModel):
    card_number: int


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    pass

class Payment(PaymentBase):
    card_number: int
    status: str
    payment_type: str
    date: datetime



    class ConfigDict:
        from_attributes = True