from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    account_id = Column(Integer, ForeignKey("account.account_id"), nullable=False)
    tracking_order_id = Column(Integer, ForeignKey("order_details.tracking_order_id"), nullable=False)
    order_status = Column(String(15), nullable=False)
    description = Column(String(300), nullable=False)
    order_date = Column(DATETIME, default=datetime.now())

    account = relationship("Account", back_populates="orders")  # account relation
    order_details = relationship("OrderDetail", back_populates="orders")  # order_details relation
    payment = relationship("Payment", back_populates="order")
