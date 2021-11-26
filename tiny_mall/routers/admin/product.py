from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from tiny_mall import models, schemas, cruds
from tiny_mall.deps import get_db


router = APIRouter(prefix="/products")


@router.post("/", response_model=schemas.Product)
async def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
):
    db_product = cruds.product.create_product(db, product)
    return db_product


@router.get("/category/{category_id}", response_model=List[schemas.Product])
async def get_products_by_category_id(
    category_id: int,
    db: Session = Depends(get_db),
):
    """根据分组id获取商品"""
    products = cruds.product.get_products_by_category_id(db, category_id)
    return products
