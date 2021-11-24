from datetime import datetime
from sqlalchemy.orm import Session

from tiny_mall import libs, models, schemas


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate, is_admin: bool = False):
    db_user = models.User(
        username=user.username,
        hashed_password=libs.security.get_password_hash(user.password),
        is_admin=is_admin,
    )
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


def update_login_at(db: Session, db_user: models.User):
    db_user.login_at = datetime.now()
    db.commit()
