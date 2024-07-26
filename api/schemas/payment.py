from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    card_number: int


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):

class Payment(PaymentBase):
    code: int


    class ConfigDict:
        from_attributes = True