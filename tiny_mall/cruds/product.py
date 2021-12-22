from datetime import datetime
from typing import List
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from tiny_mall import libs, models, schemas


def create_sku(sku: schemas.ProductSkuCreate):
    return models.ProductSku(**sku.dict())


def create_product(db: Session, product: schemas.ProductCreate):
    if product.category_id is not None:
        db_category = db.query(models.Category).get(product.category_id)
        if not db_category:
            raise HTTPException(
                status_code=400, detail="商品分类不存在")

    skus = [create_sku(item) for item in product.skus] \
        if product.skus else []

    db_product = models.Product(
        skus=skus,
        **product.dict(exclude={'skus'})
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products_by_category_id(db: Session, category_id: int):
    top_categories = db.query(models.Product).\
        order_by(models.Product.sort.desc(), models.Product.id).\
        filter(models.Product.category_id == category_id).\
        all()
    return top_categories
