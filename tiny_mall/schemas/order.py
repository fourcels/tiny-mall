from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
from pydantic.fields import Field


class OrderPaymentTypeEnum(Enum):
    '''
    * `1` - 余额
    * `2` - 支付宝
    * `3` - 微信
    * `4` - 其他
    '''
    balance = 1
    alipay = 2
    weixin = 3
    other = 4


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


class OrderAddress(BaseModel):
    name: str
    phone: str
    location: str
    detail: str

    class Config:
        orm_mode = True


class OrderLog(BaseModel):
    name: str
    created_at: datetime

    class Config:
        orm_mode = True


class OrderPayment(BaseModel):
    type: OrderPaymentTypeEnum
    amount: int
    created_at: datetime

    class Config:
        orm_mode = True


class OrderRefund(BaseModel):
    reason: str
    created_at: datetime

    class Config:
        orm_mode = True


class OrderItemBase(BaseModel):
    product_sku_id: int
    num: int = Field(1, gt=0)


class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    product_id: int
    product_name: str
    product_sku_id: int
    product_sku_name: str
    price: int
    num: int
    total_price: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    pass


class OrderCreate(OrderBase):
    address_id: int
    items: List[OrderItemCreate]


class Order(OrderBase):
    id: int
    order_no: str
    status: OrderStatusEnum
    amount: int
    user_id: int
    created_at: datetime
    address: OrderAddress
    payment: Optional[OrderPayment]
    refund: Optional[OrderRefund]
    items: List[OrderItem]
    logs: List[OrderLog]

    class Config:
        orm_mode = True
