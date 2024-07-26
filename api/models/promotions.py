from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Promotions(Base):
    __tablename__ = "promotions"

    code = Column(Integer, primary_key=True, index=True, autoincrement=True)
    expiration_date = Column(DATETIME)
