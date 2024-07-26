from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class OrderDetail(Base):
    # combine the order items together and give it a unique order number
    __tablename__ = "order_details"

    tracking_order_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dish_id = Column(Integer, ForeignKey("menu_item.dish_id"))
    price = Column(Integer, ForeignKey("menu_item.price"))

    menu_items = relationship("Items", back_populates="order_details")  # menu_items relation
    orders = relationship("Order", back_populates="order_details")  # orders relation

