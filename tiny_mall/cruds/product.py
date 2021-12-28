from datetime import datetime
from typing import List
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from tiny_mall import libs, models, schemas


def create_product(db: Session, product: schemas.ProductCreate):

    if product.category_id is not None:
        if product.category_id <= 0:
            product.category_id = None
        else:
            db_category = db.query(models.Category).get(product.category_id)
            if not db_category:
                raise HTTPException(
                    status_code=400, detail="商品分类不存在")

    db_product = models.Product(**product.dict())

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = db.query(models.Product).get(product_id)
    if not db_product:
        raise HTTPException(status_code=400, detail="商品不存在")

    product_data = product.dict(exclude_unset=True)
    for key, value in product_data.items():
        setattr(db_product, key, value)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = db.query(models.Product).get(product_id)
    if not db_product:
        raise HTTPException(status_code=400, detail="商品不存在")

    db_product.deleted_at = datetime.now()
    db.add(db_product)
    db.commit()
