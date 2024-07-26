from typing import Optional
from pydantic import BaseModel
from .payment import Payment


class PaymentBase(BaseModel):
    card_number: int


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[float] = None


class Payment(PaymentBase):
    id: int

    class ConfigDict:
        from_attributes = True