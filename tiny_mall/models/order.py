from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger
from sqlalchemy.orm import relationship
from tiny_mall.database import Base
from enum import Enum


class OrderAddress(Base):
    __tablename__ = "order_addresses"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    location = Column(String)
    detail = Column(String)
    order_id = Column(Integer, ForeignKey("order.id"))


class OrderLog(Base):
    __tablename__ = "order_logs"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    order_id = Column(Integer, ForeignKey("order.id"))


class OrderPaymentTypeEnum(Enum):
    '''
    * `1` - 余额
    * `2` - 支付宝
    * `3` - 微信
    '''
    balance = 1
    alipay = 2
    weixin = 3


class OrderPayment(Base):
    __tablename__ = "order_payments"
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    amount = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    order_id = Column(Integer, ForeignKey("order.id"))


class OrderRefund(Base):
    __tablename__ = "order_refunds"
    id = Column(Integer, primary_key=True)
    reason = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    order_id = Column(Integer, ForeignKey("order.id"))


class OrderStatusEnum(Enum):
    '''
    * `1` - 待支付
    * `2` - 待发货
    * `3` - 待收货
    * `4` - 待评价
    * `10` - 已完成
    * `11` - 已取消
    * `12` - 已退款
    '''
    pending = 1
    processing = 2
    delivered = 3
    arrived = 4
    finished = 10
    canceled = 11
    refunded = 12


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    no = Column(BigInteger)
    status = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))
    address = relationship("OrderAddress", uselist=False)
    payment = relationship("OrderPayment", uselist=False)
    refund = relationship("OrderRefund", uselist=False)
    logs = relationship("OrderLog")
