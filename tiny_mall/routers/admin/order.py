from datetime import date, datetime
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from tiny_mall import models, schemas, cruds
from tiny_mall import deps
from tiny_mall.deps import PaginateParams, get_db


router = APIRouter(prefix="/orders")


@router.get("/", response_model=List[schemas.Order])
async def get_orders(
    *,
    db: Session = Depends(get_db),
    params: PaginateParams = Depends(),
    user: models.User = Depends(deps.get_current_user),
    order_no: int = None,
    status: int = None,
    name: str = None,
    phone: str = None,
    start: date = None,
    end: date = None,
):
    filter = []
    if order_no is not None:
        filter.append(models.Order.order_no == order_no)
    if status is not None:
        filter.append(models.Order.status == status)
    if name is not None:
        filter.append(models.Order.address.has(
            models.OrderAddress.name.contains(name)))
    if phone is not None:
        filter.append(models.Order.address.has(
            models.OrderAddress.phone.contains(phone)))
    if start is not None:
        filter.append(models.Order.created_at >= start)
    if end is not None:
        filter.append(models.Order.created_at < end)

    query = db.\
        query(models.Order).\
        order_by(
            models.Order.id.desc()
        ).\
        filter(models.Order.user_id == user.id, *filter)
    return params.paginate(query)


@router.get("/{order_no}", response_model=schemas.Order)
async def get_order(
    order_no: str,
    db: Session = Depends(get_db),
    user: models.User = Depends(deps.get_current_user)
):
    """获取订单详情"""
    return cruds.order.get_order(db, order_no, user)
