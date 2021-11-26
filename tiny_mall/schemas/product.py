from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic.fields import Field


class ProductAttrValueBase(BaseModel):
    value: str
    image: Optional[str]


class ProductAttrValueCreate(ProductAttrValueBase):
    pass


class ProductAttrValue(ProductAttrValueBase):

    class Config:
        orm_mode = True


class ProductAttrBase(BaseModel):
    name: str


class ProductAttrCreate(ProductAttrBase):
    items: List[ProductAttrValueCreate]


class ProductAttr(ProductAttrBase):
    id: int
    items: List[ProductAttrValue]

    class Config:
        orm_mode = True


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
