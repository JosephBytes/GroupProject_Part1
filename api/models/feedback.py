from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Feedback(Base):
    __tablename__ = "feedback"

    review_id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    description = Column(String(100), nullable=False)
    rating = Column(Integer)

    orders = relationship("Order", back_populates="feedback")
    account = relationship("Account", back_populates="feedback")


