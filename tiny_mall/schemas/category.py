from typing import List, Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    name: Optional[str]


class Category(CategoryBase):
    id: int
    name: str
    sort: int
    product_count: int

    class Config:
        orm_mode = True


class CategoryWithChildren(Category):
    children: List[Category]
