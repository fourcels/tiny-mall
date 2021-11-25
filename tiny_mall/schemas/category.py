from typing import List, Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    desc: Optional[str]
    image: Optional[str]
    bg_image: Optional[str]
    bg_color: Optional[str]


class CategoryCreate(CategoryBase):
    pid: Optional[int]


class CategoryUpdate(CategoryBase):
    name: Optional[str]


class Category(CategoryBase):
    id: int
    name: str
    type: int

    class Config:
        orm_mode = True


class CategoryWithChildren(Category):
    children: List[Category]
