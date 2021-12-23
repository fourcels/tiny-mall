from datetime import datetime
from sqlalchemy import Column, ForeignKey, ARRAY, Boolean, DateTime, Integer, String, JSON
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from tiny_mall.models.base import BaseModel


class ProductSku(BaseModel):
    __tablename__ = "product_skus"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    stock = Column(Integer)
    image = Column(String)
    sn = Column(String)
    product_id = Column(Integer, ForeignKey("products.id"))


class Product(BaseModel):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)
    detail = Column(String)
    images = Column(ARRAY(String))
    sales = Column(Integer, default=0)
    sort = Column(Integer, index=True, default=0)
    status = Column(Boolean, default=True)
    category_id = Column(
        Integer,
        ForeignKey("categories.id", ondelete='SET NULL')
    )
    created_at = Column(DateTime, default=datetime.now)
    attrs = Column(JSONB)
    skus = relationship("ProductSku")
