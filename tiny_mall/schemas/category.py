from typing import List, Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    desc: Optional[str]
    image: Optional[str]
    bg_image: Optional[str]
    bg_color: Optional[str]


class CategoryCreate(CategoryBase):
    parent_id: Optional[int]


class CategoryUpdate(CategoryBase):
    name: Optional[str]


class Category(CategoryBase):
    id: int
    name: str

    class Config:
        orm_mode = True


class CategoryWithChildren(Category):
    children: List[Category]
