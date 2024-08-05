from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from decimal import Decimal


class ItemsBase(BaseModel):
    dish: str
    ingredients: str
    price: Decimal
    calories: int
    category: str


class ItemsCreate(ItemsBase):
    dish_id: int
    dish: str
    ingredients: Optional[str] = None
    price: Decimal
    calories: Optional[int] = None
    category: Optional[str] = None


class ItemsUpdate(BaseModel):
    dish: Optional[str] = None
    ingredients: Optional[str] = None
    price: Optional[Decimal] = None
    calories: Optional[int] = None
    category: Optional[str] = None


class Items(ItemsBase):
    dish_id: int

    class Config:
        from_attributes = True
