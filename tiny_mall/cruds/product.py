from datetime import datetime
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from tiny_mall import libs, models, schemas


def create_product(db: Session, product: schemas.ProductCreate):
    if product.attrs:
        attrs = [models.ProductAttr(**item.dict()) for item in product.attrs]
    if product.skus:
        skus = [models.ProductSku(**item.dict()) for item in product.skus]
