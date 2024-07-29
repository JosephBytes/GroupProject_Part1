from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromotionsBase(BaseModel):
    expiration_date: datetime


class PromotionsCreate(PromotionsBase):
    promotion_id: int
    code: int


class PromotionsUpdate(BaseModel):
    promotion_id: Optional[int] = None
    code: Optional[int] = None
    expiration_date: Optional[datetime] = None


class Promotions(PromotionsBase):
    promotion_id: int

    class ConfigDict:
        from_attributes = True
