from datetime import datetime
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from tiny_mall import libs, models, schemas


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        password=libs.security.get_password_hash(user.password),
        role=user.role.value,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int,  user: schemas.UserUpdate):
    db_user = db.query(models.User).get(user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="用户不存在")
    uesr_data = user.dict(exclude_unset=True)
    for key, value in uesr_data.items():
        if key == 'password':
            value = libs.security.get_password_hash(user.password)
        setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_balance_log(
    db: Session,
    amount: int,
    type: int,
    db_user: models.User
):
    db_user.balance += amount
    db_balance_log = models.BalanceLog(
        user_id=db_user.id,
        amount=amount,
        type=type,
        current_balance=db_user.balance
    )

    db.add(db_balance_log)
    db.commit()
    db.refresh(db_user)
    return db_balance_log
