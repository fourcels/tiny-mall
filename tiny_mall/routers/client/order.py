from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from tiny_mall import models, schemas, cruds
from tiny_mall.deps import get_current_user, get_db


router = APIRouter(prefix="/orders")


@router.post("/", response_model=schemas.Order)
async def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    """创建订单"""
    db_order = cruds.order.create_order(db, order, user.id)
    return db_order
