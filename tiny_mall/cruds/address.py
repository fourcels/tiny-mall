from datetime import datetime
from typing import List
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from tiny_mall import libs, models, schemas


def create_address(db: Session, address: schemas.AddressCreate, user_id: int):
    db_address = models.Address(
        user_id=user_id,
        **address.dict()
    )
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def get_addresses(db: Session, user_id: int):
    db_addresses = db.query(models.Address).\
        filter(models.Address.user_id == user_id).\
        order_by(models.Address.is_default.desc(), models.Address.id).\
        all()
    return db_addresses
