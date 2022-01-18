from datetime import datetime
from fastapi.exceptions import HTTPException
from fastapi import UploadFile
from sqlalchemy.orm import Session
from datetime import datetime
import os
from uuid import uuid4
from PIL import Image

from tiny_mall import libs, models, schemas


def get_location(filename):
    date_str = datetime.now().strftime('%Y%m%d')
    dir = f"uploads/{date_str}"
    os.makedirs(dir, exist_ok=True)
    _, ext = os.path.splitext(filename)
    filename = uuid4()
    return f"{dir}/{filename}{ext}"


def create_image(db: Session, file: UploadFile):
    if not file.content_type.startswith('image/'):
        raise HTTPException(400, '上传文件必须为图片')
    img = Image.open(file.file)
    file_location = get_location(file.filename)
    img.save(file_location)
    db_image = models.Image(
        name=file.filename,
        url=file_location,
        size=os.path.getsize(file_location),
        width=img.width,
        height=img.height,
    )
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image


def update_image(db: Session, image_id: int, image: schemas.ImageUpdate):
    db_image = db.query(models.Image).get(image_id)
    if not db_image:
        raise HTTPException(status_code=400, detail="图片不存在")
    image_data = image.dict(exclude_unset=True)
    for key, value in image_data.items():
        setattr(db_image, key, value)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image


def delete_image(db: Session, image_id: int):
    db_image = db.query(models.Image).get(image_id)
    if not db_image:
        raise HTTPException(status_code=400, detail="图片不存在")

    db.delete(db_image)
    db.commit()
