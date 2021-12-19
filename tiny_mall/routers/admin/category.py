from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from tiny_mall import models, schemas, cruds
from tiny_mall.deps import PaginateParams, get_current_user, get_db


router = APIRouter(prefix="/categories")


@router.get("/", response_model=List[schemas.Category])
async def get_categories(
    db: Session = Depends(get_db),
    params: PaginateParams = Depends(PaginateParams)
):
    query = db.\
        query(models.Category).\
        order_by(
            models.Category.sort.desc(),
            models.Category.id
        )
    return params.paginate(query)


@router.post("/", response_model=schemas.Category)
async def create_category(
    category: schemas.CategoryCreate,
    db: Session = Depends(get_db),
):
    db_category = cruds.category.create_category(db, category)
    return db_category


@router.patch("/{category_id}", response_model=schemas.Category)
async def update_category(
    category_id: int,
    category: schemas.CategoryUpdate,
    db: Session = Depends(get_db),
):
    db_category = cruds.category.update_category(db, category_id, category)
    return db_category


@router.delete("/{category_id}")
async def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
):
    cruds.category.delete_category(db, category_id)
    return {"ok": True}
