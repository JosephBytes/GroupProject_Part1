from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Account(Base):
    __tablename__ = "account"

    account_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    email = Column(String(100))
    phone = Column(Integer)
    address = Column(String(100))

    orders = relationship("Order", back_populates="Account")


