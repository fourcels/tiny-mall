from datetime import datetime
from typing import Optional
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


class UserRoleEnum(Enum):
    '''
    * `1` - 超级管理员
    * `2` - 管理员
    * `10` - 普通用户
    '''
    superadmin = 1
    admin = 2
    user = 10


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str
    role: UserRoleEnum = UserRoleEnum.user

    class Config:
        use_enum_values = True


class UserUpdate(BaseModel):
    password: Optional[str]
    is_active: Optional[bool]
    balance: Optional[int]


class User(UserBase):
    id: int
    is_active: bool
    role: UserRoleEnum
    created_at: datetime
    balance: int
    order_count: int

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
