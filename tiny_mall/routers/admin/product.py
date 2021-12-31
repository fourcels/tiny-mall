from typing import List
from fastapi import APIRouter, Depends
from fastapi.params import Query
from sqlalchemy.orm import Session

from tiny_mall import models, schemas, cruds
from tiny_mall.deps import PaginateParams, get_db
from tiny_mall.models.product import ProductSku


router = APIRouter(prefix="/products")


@router.post("/", response_model=schemas.Product)
async def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db),
):
    db_product = cruds.product.create_product(db, product)
    return db_product


@router.get("/", response_model=List[schemas.Product])
async def get_products(
    *,
    db: Session = Depends(get_db),
    params: PaginateParams = Depends(),
    name: str = None,
    category_id: int = None,
    status: bool = None,
    sn: str = None,
):
    """获取商品列表"""
    filter = []
    if name is not None:
        filter.append(models.Product.name.contains(name))
    if category_id is not None:
        filter.append(models.Product.category_id == category_id)
    if status is not None:
        filter.append(models.Product.status == status)
    if sn is not None:
        filter.append(models.Product.skus.any(
            models.ProductSku.sn.contains(sn)))

    query = db.\
        query(models.Product).\
        order_by(
            models.Product.sort.desc(),
            models.Product.id
        ).\
        filter(models.Product.deleted_at == None, *filter)
    return params.paginate(query)


@router.get("/{product_id}", response_model=schemas.Product)
async def get_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    """获取商品详情"""
    return cruds.product.get_product(db, product_id)


@router.patch("/{product_id}", response_model=schemas.Product)
async def update_product(
    product_id: int,
    product: schemas.ProductUpdate,
    db: Session = Depends(get_db),
):
    db_product = cruds.product.update_product(db, product_id, product)
    return db_product


@router.delete("/{product_id}")
async def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    cruds.product.delete_product(db, product_id)
    return {"ok": True}
