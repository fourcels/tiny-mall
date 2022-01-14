from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ImageBase(BaseModel):
    pass


class Image(ImageBase):
    id: int
    name: str
    url: str
    size: int
    width: int
    height: int
    created_at: datetime

    class Config:
        orm_mode = True
