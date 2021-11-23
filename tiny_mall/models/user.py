from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.expression import null

from tiny_mall.database import Base
from datetime import datetime
import uuid
import enum


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


class BalanceLogTypeEnum(enum.Enum):
    '''
    * `1` - 充值
    * `2` - 支付
    * `3` - 退款
    * `4` - 其他
    '''
    charge = 1
    pay = 2
    refund = 3
    other = 4


class BalanceLog(Base):
    __tablename__ = "balance_logs"
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    amount = Column(Integer)
    current_balance = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))
