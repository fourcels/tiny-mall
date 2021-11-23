from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from tiny_mall import models, schemas, cruds
from tiny_mall.deps import get_current_user, get_db


router = APIRouter(prefix="/categories")


@router.post("/", response_model=schemas.Category)
async def create_category(
    category: schemas.CategoryCreate,
    db: Session = Depends(get_db),
):
    pass
    # db_shop = cruds.shop.create_shop(db, category, db_user.id)
    # return db_shop
