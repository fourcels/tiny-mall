from datetime import datetime
from typing import Any, List, Optional
from pydantic import BaseModel
from pydantic.fields import Field
from .category import Category


class ProductAttrItem(BaseModel):
    value: str
    image: Optional[str]


class ProductAttr(BaseModel):
    name: str
    items: List[ProductAttrItem]


class ProductSkuBase(BaseModel):
    name: str
    price: int = Field(1000, gt=0)
    stock: int = Field(10000, ge=0)
    image: Optional[str]
    sn: Optional[str]


class ProductSkuCreate(ProductSkuBase):
    pass


class ProductSku(ProductSkuBase):
    id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    desc: Optional[str]
    detail: Optional[str]
    images: Optional[List[str]] = []
    attrs: Optional[List[ProductAttr]]
    category_id: Optional[int]


class ProductCreate(ProductBase):
    skus: List[ProductSkuCreate]


class ProductUpdate(BaseModel):
    name: Optional[str]
    desc: Optional[str]
    detail: Optional[str]
    images: Optional[List[str]]
    sort: Optional[int]
    status: Optional[bool]
    skus: Optional[List[ProductSkuCreate]]
    attrs: Optional[List[ProductAttr]]
    category_id: Optional[int]


class Product(ProductBase):
    id: int
    sort: int
    status: bool
    created_at: datetime
    skus: List[ProductSku]
    category: Optional[Category]

    class Config:
        orm_mode = True
