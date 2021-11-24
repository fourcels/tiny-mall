from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    parent_id: Optional[int]


class CategoryUpdate(CategoryBase):
    name: Optional[str]
    sort: Optional[int]


class Category(CategoryBase):
    id: int
    name: str
    sort: int
    created_at: datetime

    class Config:
        orm_mode = True
