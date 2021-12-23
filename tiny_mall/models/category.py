from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy import select, func
from sqlalchemy.orm import column_property
from tiny_mall.models.base import BaseModel
from tiny_mall.models.product import Product


class Category(BaseModel):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    sort = Column(Integer, default=0)
    product_count = column_property(
        select(func.count(Product.id)).
        where(Product.category_id == id).
        correlate_except(Product).
        scalar_subquery()
    )
