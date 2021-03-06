from datetime import datetime
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from tiny_mall import libs, models, schemas


def get_categories(db: Session):
    db_categories = db.query(models.Category).\
        order_by(models.Category.sort.desc(), models.Category.id).\
        all()
    return db_categories


def get_category_by_name(db: Session, name: str):
    db_category = db.query(models.Category).\
        filter(models.Category.name == name). \
        first()
    return db_category


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = get_category_by_name(db, category.name)
    if db_category:
        raise HTTPException(
            status_code=400, detail="商品名称已存在")
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def update_category(db: Session, category_id: int, category: schemas.CategoryUpdate):
    db_category = db.query(models.Category).get(category_id)
    if not db_category:
        raise HTTPException(status_code=400, detail="商品分类不存在")
    if category.name and db_category.name != category.name:
        db_category2 = get_category_by_name(db, category.name)
        if db_category2:
            raise HTTPException(
                status_code=400, detail="分类名称已存在")
    category_data = category.dict(exclude_unset=True)
    for key, value in category_data.items():
        setattr(db_category, key, value)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int):
    db_category = db.query(models.Category).get(category_id)
    if not db_category:
        raise HTTPException(status_code=400, detail="商品分类不存在")

    db.delete(db_category)
    db.commit()
