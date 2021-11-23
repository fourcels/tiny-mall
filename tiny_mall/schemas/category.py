from datetime import datetime
from pydantic import BaseModel
from uuid import UUID


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: UUID
    name: str
    sort: int
    created_at: datetime

    class Config:
        orm_mode = True
