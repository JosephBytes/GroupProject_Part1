from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Items(Base):
    __tablename__ = "items"

    dish_id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    dish = Column(String(100), nullable=False, unique=True)
    ingredients = Column(String(100))
    price = Column(DECIMAL(4, 2), nullable=False)
    calories = Column(Integer)
    category = Column(String(100))

    recipes = relationship("Recipe", back_populates="items")
    order_details = relationship("OrderDetail", back_populates="items")






