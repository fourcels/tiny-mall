from datetime import datetime
from typing import Any, List, Optional
from pydantic import BaseModel
from pydantic.fields import Field, Json


class ProductAttrItem(BaseModel):
    value: str
    image: Optional[str]


class ProductAttr(BaseModel):
    name: str
    items: List[ProductAttrItem]


class ProductSkuBase(BaseModel):
    name: str
    price: int = Field(100, gt=0)
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
    images: Optional[List[str]]
    attrs: Optional[List[ProductAttr]]
    category_id: Optional[int]


class ProductCreate(ProductBase):
    skus: List[ProductSkuCreate]


class Product(ProductBase):
    id: int
    sort: int
    status: bool
    sort: int
    status: bool
    created_at: datetime
    skus: List[ProductSku]

    class Config:
        orm_mode = True
