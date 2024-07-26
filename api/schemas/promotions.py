from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromotionsBase(BaseModel):
    expiration_date: datetime

class PromotionsCreate(PromotionsBase):
    pass

class Promotions(PromotionsBase):
    code: int

    class Config:
        orm_mode = True