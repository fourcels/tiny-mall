from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from tiny_mall import models, schemas, cruds
from tiny_mall.deps import PaginateParams, get_db


router = APIRouter(prefix="/users")


@router.post("/", response_model=schemas.User)
async def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
):
    """创建用户"""
    db_user = cruds.user.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=400, detail="用户名已存在")
    return cruds.user.create_user(db=db, user=user)


@router.get("/", response_model=List[schemas.User])
async def get_users(
    *,
    db: Session = Depends(get_db),
    params: PaginateParams = Depends(),
):
    """获取用户列表"""
    query = db.\
        query(models.User).\
        order_by(
            models.User.role,
            models.User.id
        )
    return params.paginate(query)


@router.patch("/{user_id}", response_model=schemas.User)
async def update_user(
    user_id: int,
    user: schemas.UserUpdate,
    db: Session = Depends(get_db),
):
    db_user = cruds.user.update_user(db, user_id, user)
    return db_user
