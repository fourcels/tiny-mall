from typing import Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    desc: Optional[str]
    image: Optional[str]


class CategoryCreate(CategoryBase):
    parent_id: Optional[int]


class CategoryUpdate(CategoryBase):
    name: Optional[str]


class Category(CategoryBase):
    id: int
    name: str

    class Config:
        orm_mode = True
