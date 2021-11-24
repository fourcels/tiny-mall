from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class BalanceLogTypeEnum(Enum):
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


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    login_at: datetime
    balance: int

    class Config:
        orm_mode = True


class BalanceLog(BaseModel):
    id: int
    type: BalanceLogTypeEnum
    amount: int
    current_balance: int
    created_at: datetime

    class Config:
        orm_mode = True
