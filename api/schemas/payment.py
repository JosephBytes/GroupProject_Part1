from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class PaymentBase(BaseModel):
    card_number: int


class PaymentCreate(PaymentBase):
    payment_type: Optional[str]


class PaymentUpdate(BaseModel):
    status: Optional[str]


class Payment(PaymentBase):
    card_number: int
    status: str
    payment_type: str
    date: datetime

    class ConfigDict:
        from_attributes = True
