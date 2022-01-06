from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
from pydantic.fields import Field
from .user import User


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
    * `4` - 退款中
    * `10` - 交易完成
    * `11` - 交易取消
    '''
    pending = 1
    processing = 2
    shipping = 3
    refunding = 4
    finished = 10
    canceled = 11


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


class OrderItemCreate(BaseModel):
    product_sku_id: int
    num: int = Field(1, gt=0)


class OrderItem(BaseModel):
    product_id: int
    product_name: str
    product_sku_name: str
    price: int
    num: int
    image: Optional[str]
    total_price: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    pass


class OrderCreate(OrderBase):
    address_id: int
    items: List[OrderItemCreate]
    remarks: Optional[str]


class Order(OrderBase):
    id: int
    order_no: str
    status: OrderStatusEnum
    amount: int
    remarks: Optional[str]
    user_id: int
    created_at: datetime
    address: OrderAddress
    payment: Optional[OrderPayment]
    refund: Optional[OrderRefund]
    items: List[OrderItem]
    logs: List[OrderLog]
    user: User

    class Config:
        orm_mode = True
