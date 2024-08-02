from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promotions(Base):
    __tablename__ = "promotions"

    promotion_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    code = Column(Integer, index=True, autoincrement=True, nullable=False)
    expiration_date = Column(DATETIME)
