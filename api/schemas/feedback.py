from typing import Optional
from pydantic import BaseModel


class FeedbackBase(BaseModel):
    review_id: int
    rating: int


class FeedbackCreate(FeedbackBase):
    review_id: int
    description: str
    rating: int


class FeedbackUpdate(FeedbackBase):
    description: Optional[str] = None
    rating: Optional[int] = None


class Feedback(FeedbackBase):
    review_id: int
    description: str
    rating: int

    class Config:
        from_attributes = True
