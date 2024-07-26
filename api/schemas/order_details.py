from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from ..models.menu_item import Items


class OrderDetailBase(BaseModel):
    price: int


class OrderDetailCreate(OrderDetailBase):
    tracking_order_id: int
    dish_id: int


class OrderDetailUpdate(BaseModel):
    tracking_order_id: Optional[int] = None
    dish_id: Optional[int] = None
    price: Optional[int] = None


class OrderDetail(OrderDetailBase):
    tracking_order_id: int
    dish_id: int
    items: Items = None

    class ConfigDict:
        from_attributes = True
