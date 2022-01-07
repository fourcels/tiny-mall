from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from tiny_mall import models, schemas, cruds, libs, deps

router = APIRouter(prefix="/auth")


@router.post("/token")
async def token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(deps.get_db),
):
    db_user = cruds.user.get_user_by_username(db, username=form_data.username)

    if not db_user or not libs.security.verify_password(form_data.password, db_user.password):
        raise HTTPException(
            status_code=400,
            detail="Username or password invalid"
        )
    access_token = libs.security.create_access_token(
        data={"sub": str(db_user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/user", response_model=schemas.User)
async def user(
    db: Session = Depends(deps.get_db),
    user: models.User = Depends(deps.get_current_user)
):
    return user
