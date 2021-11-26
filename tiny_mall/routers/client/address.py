from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from tiny_mall import models, schemas, cruds
from tiny_mall.deps import get_current_user, get_db


router = APIRouter(prefix="/addresses")


@router.post("/", response_model=schemas.Address)
async def create_address(
    address: schemas.AddressCreate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    """创建用户地址"""
    db_address = cruds.address.create_address(db, address, user.id)
    return db_address


@router.get("/", response_model=List[schemas.Address])
async def get_addresses(
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user),
):
    """获取用户地址列表"""
    db_addresses = cruds.address.get_addresses(db, user.id)
    return db_addresses
