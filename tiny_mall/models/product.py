from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import ARRAY, Boolean, DateTime, Integer, String
from tiny_mall.database import Base
import uuid


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)
    images = Column(ARRAY(String))
    sort = Column(Integer, index=True, default=0)
    status = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    created_at = Column(DateTime, default=datetime.now)
