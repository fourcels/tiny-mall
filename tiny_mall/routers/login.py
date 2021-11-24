from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from tiny_mall import schemas, cruds, libs, deps

router = APIRouter()


@router.post("/signup", response_model=schemas.User)
async def signup(
    user: schemas.UserCreate,
    db: Session = Depends(deps.get_db),
):
    db_user = cruds.user.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered")
    return cruds.user.create_user(db=db, user=user)


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(deps.get_db),
):
    db_user = cruds.user.get_user_by_username(db, username=form_data.username)

    if not db_user or not libs.security.verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(
            status_code=400,
            detail="Username or password invalid"
        )
    access_token = libs.security.create_access_token(
        data={"sub": str(db_user.id)}
    )
    cruds.user.update_login_at(db, db_user)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
