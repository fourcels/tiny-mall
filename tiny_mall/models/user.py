from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy import select, func
from sqlalchemy.orm import column_property
from datetime import datetime

from tiny_mall.models.base import Base
from tiny_mall.models.order import Order


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(Integer, default=10)
    balance = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now)
    order_count = column_property(
        select(func.count(Order.id)).
        where(Order.user_id == id).
        correlate_except(Order).
        scalar_subquery()
    )


class BalanceLog(Base):
    __tablename__ = "balance_logs"
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    amount = Column(Integer)
    current_balance = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))
