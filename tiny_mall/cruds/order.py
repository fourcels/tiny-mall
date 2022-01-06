from datetime import datetime
from typing import List
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session, aliased
from sqlalchemy.sql.functions import func

from tiny_mall import libs, models, schemas


def create_order_item(db: Session, item: schemas.OrderItemCreate):
    db_product_sku = db.query(models.ProductSku).get(item.product_sku_id)
    if not db_product_sku:
        raise HTTPException(
            status_code=400, detail="商品规格不存在")
    db_product = db.query(models.Product).get(db_product_sku.product_id)
    return models.OrderItem(
        product_id=db_product.id,
        product_name=db_product.name,
        product_sku_name=db_product_sku.name,
        image=db_product_sku.image if db_product_sku.image else db_product.images[0] if len(
            db_product.images) > 0 else '',
        price=db_product_sku.price,
        num=item.num,
        total_price=db_product_sku.price*item.num,
    )


def create_order(db: Session, order: schemas.OrderCreate, user_id: int):
    db_address = db.query(models.Address).get(order.address_id)
    if not db_address:
        raise HTTPException(
            status_code=400, detail="用户地址不存在")
    db_order_address = models.OrderAddress(
        name=db_address.name,
        phone=db_address.phone,
        location=db_address.location,
        detail=db_address.detail,
    )

    db_order_items = [create_order_item(db, item) for item in order.items]

    amount = sum([item.total_price for item in db_order_items])

    db_logs = [models.OrderLog(name="创建订单")]

    db_order = models.Order(
        user_id=user_id,
        order_no=libs.order_no.generate_order_no(),
        amount=amount,
        address=db_order_address,
        items=db_order_items,
        logs=db_logs
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def get_order(db: Session, order_no: int, user: models.User):
    db_order = db.\
        query(models.Order).\
        filter(
            models.Order.order_no == order_no,
            models.Order.user_id == user.id,
        ).\
        first()
    if not db_order:
        raise HTTPException(status_code=400, detail="订单不存在")

    return db_order


def get_stats(db: Session, day: int):
    offs = aliased(func.generate_series(0, day - 1))
    d = db.\
        query(func.to_char(func.current_date() - offs.table_valued(), 'YYYY-MM-DD').label('date')).\
        select_from(offs).\
        subquery()
    return db.\
        query(func.substr(d.c.date, 6).label('date'), func.count(models.Order.id).label('count')).\
        select_from(d).\
        outerjoin(models.Order, d.c.date == func.to_char(models.Order.created_at, 'YYYY-MM-DD')).\
        group_by(d.c.date).\
        order_by(d.c.date).\
        all()
