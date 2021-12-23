from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger
from sqlalchemy.orm import relationship
from tiny_mall.models.base import Base


class OrderAddress(Base):
    __tablename__ = "order_addresses"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    location = Column(String)
    detail = Column(String)
    order_id = Column(Integer, ForeignKey("orders.id"))


class OrderLog(Base):
    __tablename__ = "order_logs"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    order_id = Column(Integer, ForeignKey("orders.id"))


class OrderPayment(Base):
    __tablename__ = "order_payments"
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    amount = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    order_id = Column(Integer, ForeignKey("orders.id"))


class OrderRefund(Base):
    __tablename__ = "order_refunds"
    id = Column(Integer, primary_key=True)
    reason = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    order_id = Column(Integer, ForeignKey("orders.id"))


class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    product_sku_id = Column(Integer, ForeignKey("product_skus.id"))
    product_name = Column(String)
    product_sku_name = Column(String)
    price = Column(Integer)
    num = Column(Integer)
    total_price = Column(Integer)
    order_id = Column(Integer, ForeignKey("orders.id"))


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    order_no = Column(BigInteger, unique=True)
    status = Column(Integer, default=1)
    amount = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))
    address = relationship("OrderAddress", uselist=False)
    payment = relationship("OrderPayment", uselist=False)
    refund = relationship("OrderRefund", uselist=False)
    items = relationship("OrderItem")
    logs = relationship("OrderLog")
