from tiny_mall.database import SessionLocal
from tiny_mall.config import settings
from tiny_mall import cruds, schemas


def init_db():
    with SessionLocal() as db:
        db_user = cruds.user.get_user_by_username(db, settings.admin_username)
        if not db_user:
            user = schemas.UserCreate(
                username=settings.admin_username,
                password=settings.admin_password,
            )
            cruds.user.create_user(db, user, True)
