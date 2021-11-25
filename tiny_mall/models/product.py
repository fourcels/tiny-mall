from datetime import datetime
from sqlalchemy import Column, ForeignKey, ARRAY, Boolean, DateTime, Integer, String
from sqlalchemy.orm import relationship
from tiny_mall.database import Base


class ProductAttr(Base):
    __tablename__ = "product_attrs"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    values = Column(ARRAY(String))
    image = Column(String)
    product_id = Column(Integer, ForeignKey("products.id"))


class ProductSku(Base):
    __tablename__ = "product_skus"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    stock = Column(Integer)
    image = Column(String)
    sn = Column(String)
    product_id = Column(Integer, ForeignKey("products.id"))


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)
    detail = Column(String)
    images = Column(ARRAY(String))
    sales = Column(Integer, default=0)
    sort = Column(Integer, index=True, default=0)
    status = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category_root_id = Column(Integer, ForeignKey("categories.id"))
    created_at = Column(DateTime, default=datetime.now)
    attrs = relationship("ProductAttr")
    skus = relationship("ProductSku")
