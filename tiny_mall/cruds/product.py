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


def generate_skus(current_skus: List[models.ProductSku], data: List[schemas.ProductSkuCreate]):
    res = []
    for item in data:
        sku = next(
            (item2 for item2 in current_skus if item2.name == item.name), None)
        if not sku:
            sku = models.ProductSku(**item.dict())
        else:
            item_data = item.dict()
            for key, value in item_data.items():
                setattr(sku, key, value)
        res.append(sku)
    return res


def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = db.query(models.Product).get(product_id)
    if not db_product:
        raise HTTPException(status_code=400, detail="商品不存在")

    product.category_id = check_category(db, product.category_id)

    product_data = product.dict(exclude_unset=True)
    for key, value in product_data.items():
        if key == 'skus':
            value = generate_skus(db_product.skus, product.skus)
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


def get_product(db: Session, product_id: int):
    db_product = db.query(models.Product).get(product_id)
    if not db_product:
        raise HTTPException(status_code=400, detail="商品不存在")

    return db_product
