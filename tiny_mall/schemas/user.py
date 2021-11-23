from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from uuid import UUID

from tiny_mall import models


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: UUID
    is_active: bool
    created_at: datetime
    login_at: datetime

    class Config:
        orm_mode = True


class BalanceLog(BaseModel):
    id: UUID
    type: models.BalanceLogTypeEnum
    amount: int
    current_balance: int
    created_at: datetime

    class Config:
        orm_mode = True
