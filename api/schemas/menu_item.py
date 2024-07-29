from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ItemsBase(BaseModel):
    dish: str
    ingredients: str
    price: float
    calories: int
    category: str


class ItemsCreate(ItemsBase):
    pass


class ItemsUpdate(BaseModel):
    dish: Optional[str] = None
    ingredients: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    category: Optional[str] = None


class Items(ItemsBase):
    dish_id: int

    class Config:
        orm_mode = True
