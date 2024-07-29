from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ResourceBase(BaseModel):
    item: str
    amount: int


class ResourceCreate(ResourceBase):
    resource_id: int


class ResourceUpdate(BaseModel):
    item: Optional[str] = None
    amount: Optional[int] = None


class Resource(ResourceBase):
    resource_id: int
    id: int

    class ConfigDict:
        from_attributes = True
