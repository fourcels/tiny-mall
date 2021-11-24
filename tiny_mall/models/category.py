from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from tiny_mall.database import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    sort = Column(Integer, index=True, default=0)
    created_at = Column(DateTime, default=datetime.now)
    parent_id = Column(Integer, ForeignKey("categories.id"))
