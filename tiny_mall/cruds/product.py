from datetime import datetime
from typing import List, Optional
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from tiny_mall import libs, models, schemas


def check_category(db: Session, category_id: Optional[int]):
    if category_id is not None:
        if category_id <= 0:
            category_id = None
        else:
            db_category = db.query(models.Category).get(category_id)
            if not db_category:
                raise HTTPException(
                    status_code=400, detail="商品分类不存在")
    return category_id


def create_product(db: Session, product: schemas.ProductCreate):
    product.category_id = check_category(db, product.category_id)
    db_product = models.Product(**product.dict())

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = db.query(models.Product).get(product_id)
    if not db_product:
        raise HTTPException(status_code=400, detail="商品不存在")

    product.category_id = check_category(db, product.category_id)

    product_data = product.dict(exclude_unset=True)
    model_columns = db_product.__mapper__.columns
    relationships = db_product.__mapper__.relationships
    for key, val in product_data.items():
        if key in model_columns:
            setattr(db_product, key, val)
            continue

        if key in relationships:
            relation_cls = relationships[key].mapper.entity

            if isinstance(val, list):
                instances = [relation_cls(**elem) for elem in val]
                setattr(db_product, key, instances)

            elif isinstance(val, dict):
                instance = relation_cls(**val)
                setattr(db_product, key, instance)

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


def get_product(db: Session, product_id: int):
    db_product = db.query(models.Product).get(product_id)
    if not db_product:
        raise HTTPException(status_code=400, detail="商品不存在")

    return db_product
