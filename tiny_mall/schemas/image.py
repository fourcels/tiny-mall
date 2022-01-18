from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ImageBase(BaseModel):
    pass


class ImageUpdate(ImageBase):
    name: Optional[str]
    is_favorite: Optional[bool]


class Image(ImageBase):
    id: int
    name: str
    url: str
    size: int
    width: int
    height: int
    is_favorite: bool
    created_at: datetime

    class Config:
        orm_mode = True
