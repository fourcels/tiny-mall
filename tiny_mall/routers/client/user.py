from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.params import Body
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from tiny_mall import models, schemas, cruds, deps


router = APIRouter(prefix="/users")


@router.post("/charge", response_model=schemas.BalanceLog)
async def balance_charge(
    amount: int = Body(..., ge=1, embed=True),
    user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
):
    db_balance_log = cruds.user.create_balance_log(
        db, amount, models.BalanceLogTypeEnum.charge, user)
    return db_balance_log
