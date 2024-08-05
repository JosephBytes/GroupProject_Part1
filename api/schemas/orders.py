from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel


class OrderBase(BaseModel):
    order_status: str
    description: str


class OrderCreate(OrderBase):
    order_id: int
    customer_name: str
    tracking_order_id: int
    price: Decimal
    description: str
    order_status: str


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    tracking_order_id: Optional[int] = None
    order_status: Optional[str] = None
    price: Optional[Decimal] = None
    description: Optional[str] = None


class Order(OrderBase):
    order_id: int
    tracking_order_id: int
    customer_name: str
    price: Decimal
    order_date: datetime

    class ConfigDict:
        from_attributes = True
