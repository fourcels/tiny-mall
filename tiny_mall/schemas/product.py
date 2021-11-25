from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from tiny_mall.models import category


class ProductAttrBase(BaseModel):
    name: str
    values: List[str]
    image: Optional[str]
    product_id: int


class ProductAttrCreate(ProductAttrBase):
    pass


class ProductAttr(ProductAttrBase):
    id: int

    class Config:
        orm_mode = True


class ProductSkuBase(BaseModel):
    name: str
    price: int
    stock: int
    image: Optional[str]
    sn: Optional[str]
    product_id: int


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
    category_id: int


class ProductCreate(ProductBase):
    attrs: Optional[List[ProductAttrCreate]]
    skus: List[ProductSkuCreate]


class Product(ProductBase):
    id: int
    sort: int
    status: bool
    sort: int
    status: bool
    category_root_id: int
    created_at: datetime
    attrs: Optional[List[ProductAttr]]
    skus: List[ProductSku]

    class Config:
        orm_mode = True
