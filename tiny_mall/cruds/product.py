from datetime import datetime
from typing import List
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from tiny_mall import libs, models, schemas


def create_attr(attr: schemas.ProductAttrCreate):
    items = [models.ProductAttrValue(**item.dict()) for item in attr.items]
    return models.ProductAttr(items=items, **attr.dict(exclude={'items'}))


def create_sku(sku: schemas.ProductSkuCreate):
    return models.ProductSku(**sku.dict())


def get_category_root_id(db: Session, category: models.Category):
    if not category.pid:
        return category.id
    db_category = db.query(models.Category).get(category.pid)
    return get_category_root_id(db, db_category)


def create_product(db: Session, product: schemas.ProductCreate):
    db_category = db.query(models.Category).get(product.category_id)
    if not db_category:
        raise HTTPException(
            status_code=400, detail="category not found")

    category_root_id = get_category_root_id(db, db_category)

    attrs = [create_attr(item) for item in product.attrs] \
        if product.attrs else []
    skus = [create_sku(item) for item in product.skus] \
        if product.skus else []

    db_product = models.Product(
        attrs=attrs,
        skus=skus,
        category_root_id=category_root_id,
        **product.dict(exclude={'attrs', 'skus'})
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
