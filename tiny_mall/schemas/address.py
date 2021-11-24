from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class AddressBase(BaseModel):
    name: str
    phone: str
    location: str
    detail: Optional[str]


class AddressCreate(AddressBase):
    pass


class Address(AddressBase):
    id: int
    is_default: bool

    class Config:
        orm_mode = True
