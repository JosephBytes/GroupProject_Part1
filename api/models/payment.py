from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payment"

    card_number = Column(Integer, primary_key=True, index=True, autoincrement=False)
    status = Column(String(100))
    payment_type = Column(String(100))
    date = Column(DATETIME)

