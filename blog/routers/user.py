
from fastapi import APIRouter

from fastapi import Depends, status, HTTPException
from .. import schemas

from ..database import engine, get_db
from sqlalchemy.orm import Session
from typing import List
from ..repository import user


router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)

