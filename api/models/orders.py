from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(Integer, ForeignKey("account.name"))
    tracking_order_id = Column(Integer, ForeignKey("order_details.tracking_order_id"))
    order_status = Column(String(15))
    price = Column(Integer, ForeignKey("order_details.amount"))
    description = Column(String(300))

    account = relationship("Account", back_populates="order")  # account relation
    menu_item = relationship("Items", back_populates="order")  # menu_items relation
    order_details = relationship("OrderDetail", back_populates="order")  # order_details relation

