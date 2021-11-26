from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from tiny_mall import models, schemas, cruds
from tiny_mall.deps import get_db


router = APIRouter(prefix="/categories")


@router.get("/", response_model=List[schemas.Category])
async def get_root_categories(db: Session = Depends(get_db)):
    """获取商品分组"""
    top_categories = cruds.category.get_root_categories(db)
    return top_categories


@router.get("/{pid}", response_model=List[schemas.CategoryWithChildren])
async def get_categories_by_pid(pid: int, db: Session = Depends(get_db)):
    """获取下级商品分组"""
    categories = cruds.category.get_categories_by_pid(db, pid)
    return categories
