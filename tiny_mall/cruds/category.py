from datetime import datetime
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from tiny_mall import libs, models, schemas


def create_category(db: Session, category: schemas.CategoryCreate):
    if category.parent_id is not None:
        db_category = db.query(models.Category).get(category.parent_id)
        if not db_category:
            raise HTTPException(
                status_code=400, detail="Parent category not found")
    db_category = models.Category(**category.dict())
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


def get_top_categories(db: Session):
    top_categories = db.query(models.Category).\
        filter(models.Category.type == 1).\
        order_by(models.Category.id).\
        all()
    return top_categories


def get_categories_by_parent_id(db: Session, parent_id: int):
    categories = db.query(models.Category).\
        filter(models.Category.pid == parent_id).\
        order_by(models.Category.id).\
        all()
    return categories
