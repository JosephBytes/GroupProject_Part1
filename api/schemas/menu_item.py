from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    dish: str
    ingredients: str
    price: float
    calories: int
    category: str

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    dish: Optional[str] = None
    ingredients: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    category: Optional[str] = None

class Item(ItemBase):
    dish_id: int

    class Config:
        orm_mode = True
