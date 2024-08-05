from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payment"

    card_number = Column(Integer, primary_key=True, index=True, autoincrement=False, nullable=False)
    order_id = Column(Integer, ForeignKey("order.id"), nullable=False)
    status = Column(String(100))
    payment_type = Column(String(100))
    date = Column(DATETIME)

    order = relationship("Order", back_populates="payment")
