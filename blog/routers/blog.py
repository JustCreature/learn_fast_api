from fastapi import APIRouter
from typing import List
from .. import schemas, database, models, oauth2
from fastapi import Depends
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, status, Response, HTTPException
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db, current_user)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(
        request: schemas.Blog,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(oauth2.get_current_user)
):
    return blog.create(request, db, current_user)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db, current_user)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(
        id,
        request: schemas.Blog,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(oauth2.get_current_user)
):
    return blog.update(id, request, db, current_user)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db, current_user)
