from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime

from datetime import datetime

from tiny_mall.models.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    balance = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now)
    login_at = Column(DateTime, nullable=True)


class BalanceLog(Base):
    __tablename__ = "balance_logs"
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    amount = Column(Integer)
    current_balance = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))
