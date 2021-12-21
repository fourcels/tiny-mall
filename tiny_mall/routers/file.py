import os
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session

from tiny_mall import models, schemas, cruds, libs, deps
from datetime import datetime
import shutil
from uuid import uuid4

router = APIRouter(prefix="/files")


def get_location(filename):
    date_str = datetime.now().strftime('%Y%m%d')
    dir = f"uploads/{date_str}"
    os.makedirs(dir, exist_ok=True)
    _, ext = os.path.splitext(filename)
    filename = uuid4()
    return f"{dir}/{filename}{ext}"


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = get_location(file.filename)
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    return {"url": file_location}
