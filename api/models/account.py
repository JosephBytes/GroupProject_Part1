from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Account(Base):
    __tablename__ = "account"

    account_id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    customer_name = Column(String(100), nullable=False)
    email = Column(String(100))
    phone = Column(Integer)
    address = Column(String(100))

    orders = relationship("Order", back_populates="account")


