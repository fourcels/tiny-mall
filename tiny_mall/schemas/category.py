from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    parent_id: Optional[int]


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    name: str
    sort: int
    created_at: datetime

    class Config:
        orm_mode = True
