from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy import select, func
from sqlalchemy.orm import column_property
from tiny_mall.models.base import Base
from tiny_mall.models.product import Product


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    sort = Column(Integer, index=True, default=0)
    product_count = column_property(
        select(func.count(Product.id)).
        where(Product.category_id == id, Product.deleted_at == None).
        correlate_except(Product).
        scalar_subquery()
    )
