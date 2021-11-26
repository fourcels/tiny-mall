from datetime import datetime
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from tiny_mall import libs, models, schemas


def create_category(db: Session, category: schemas.CategoryCreate):
    type = 1
    if category.pid is not None:
        p_category = db.query(models.Category).get(category.pid)
        if not p_category:
            raise HTTPException(
                status_code=400, detail="Parent category not found")
        type = p_category.type + 1
    db_category = models.Category(type=type, **category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def update_category(db: Session, category_id: int, category: schemas.CategoryUpdate):
    db_category = db.query(models.Category).get(category_id)
    if not db_category:
        raise HTTPException(status_code=400, detail="Category not found")
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
        raise HTTPException(status_code=400, detail="Category not found")

    db.delete(db_category)
    db.commit()


def get_root_categories(db: Session):
    top_categories = db.query(models.Category).\
        filter(models.Category.type == 1).\
        order_by(models.Category.id).\
        all()
    return top_categories


def get_categories_by_pid(db: Session, pid: int):
    categories = db.query(models.Category).\
        filter(models.Category.pid == pid).\
        order_by(models.Category.id).\
        all()
    return categories
