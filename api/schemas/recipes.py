from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .resources import Resource
from .sandwiches import Sandwich
from ..models.menu_item import Items


class RecipeBase(BaseModel):
    amount: int


class RecipeCreate(RecipeBase):
    dish_id: int
    resource_id: int


class RecipeUpdate(BaseModel):
    dish_id: Optional[int] = None
    resource_id: Optional[int] = None
    cost: Optional[int] = None


class Recipe(RecipeBase):
    recipe_id: int
    item: Items = None
    resource: Resource = None

    class ConfigDict:
        from_attributes = True
