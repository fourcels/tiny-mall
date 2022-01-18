from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from tiny_mall.models.base import Base


class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    size = Column(Integer)
    width = Column(Integer)
    height = Column(Integer)
    url = Column(String)
    is_favorite = Column(String, default=False)
    created_at = Column(DateTime, default=datetime.now)
