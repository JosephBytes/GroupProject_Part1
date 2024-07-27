from datetime import datetime
from typing import Optional
from pydantic import BaseModel


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
    dish_id: int
    resource_id: int

    class ConfigDict:
        from_attributes = True
