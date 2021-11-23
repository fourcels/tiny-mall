from pydantic import BaseModel
from uuid import UUID


class ShopBase(BaseModel):
    name: str
    address: str
    detail: str


class ShopCreate(ShopBase):
    pass


class Shop(ShopBase):
    id: UUID
    status: bool

    class Config:
        orm_mode = True
