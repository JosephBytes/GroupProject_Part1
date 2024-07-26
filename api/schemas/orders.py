from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class OrderBase(BaseModel):
    order_status: str
    description: str
    tracking_order_id: Optional[int] = None


class OrderCreate(OrderBase):
    order_id: int
    customer_name: str
    tracking_order_id: int


class OrderUpdate(BaseModel):
    order_id: Optional[int] = None
    customer_name: Optional[str] = None
    tracking_order_id: Optional[int] = None
    order_status: Optional[str] = None
    order_date: Optional[datetime] = None


class Order(OrderBase):
    account_id: int
    tracking_order_id: int

    class ConfigDict:
        from_attributes = True
