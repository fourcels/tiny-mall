from fastapi.exceptions import HTTPException
from fastapi.param_functions import Query
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi import status, Response
from jose.exceptions import JWTError
from tiny_mall.database import SessionLocal
from tiny_mall import models, libs

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/authenticate")


# Dependency
def get_db():
    with SessionLocal() as db:
        yield db


async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = libs.security.decode_access_token(token)
        id: str = payload.get("sub")
        if id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(models.User).get(id)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: models.User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def get_current_active_admin(current_user: models.User = Depends(get_current_active_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=400, detail="Invalid admin")
    return current_user


class PaginateParams:
    def __init__(
        self,
        response: Response,
        page: int = Query(1, ge=1),
        page_size: int = Query(10, ge=1, le=100),
    ):
        self.response = response
        self.page = page
        self.page_size = page_size

    def paginate(
        self,
        query,
    ):
        items = query.limit(self.page_size).offset(
            (self.page - 1) * self.page_size).all()
        total = query.order_by(None).count()

        self.response.headers["X-Total"] = str(total)
        return items
