from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from tiny_mall.database import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)
    image = Column(String)
    parent_id = Column(Integer, ForeignKey("categories.id"))
    children = relationship("Category")
