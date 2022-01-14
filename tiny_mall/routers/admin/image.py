from typing import List
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session

from tiny_mall import models, schemas, cruds
from tiny_mall.deps import PaginateParams, get_db


router = APIRouter(prefix="/images")


@router.post("/", response_model=schemas.Image)
async def create_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    return cruds.image.create_image(db=db, file=file)


@router.get("/", response_model=List[schemas.Image])
async def get_images(
    *,
    db: Session = Depends(get_db),
    params: PaginateParams = Depends(),
):
    """获取图片列表"""
    query = db.\
        query(models.Image).\
        order_by(
            models.Image.id.desc()
        )
    return params.paginate(query)


@router.delete("/{image_id}")
async def delete_image(
    image_id: int,
    db: Session = Depends(get_db),
):
    cruds.image.delete_image(db, image_id)
    return {"ok": True}
