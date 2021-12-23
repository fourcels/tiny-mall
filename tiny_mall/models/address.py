from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean
from tiny_mall.models.base import BaseModel


class Address(BaseModel):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    location = Column(String)
    detail = Column(String)
    is_default = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
