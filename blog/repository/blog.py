from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas


def get_all(db: Session, current_user):
    blogs = db.query(models.Blog)\
        .filter(models.Blog.user_id == current_user.id)\
        .all()
    return blogs


def create(request: schemas.Blog, db: Session, current_user):
    new_blog = models.Blog(
        title=request.title,
        body=request.body,
        user_id=current_user.id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id, db: Session, current_user):
    blog = db.query(models.Blog)\
        .filter(models.Blog.user_id == current_user.id)\
        .filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return {'done'}


def update(id, request: schemas.Blog, db: Session, current_user):
    blog = db.query(models.Blog)\
        .filter(models.Blog.user_id == current_user.id)\
        .filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    blog.update(request.dict())
    db.commit()
    return 'updated'


def show(id, db: Session, current_user):
    blog = db.query(models.Blog)\
        .filter(models.Blog.user_id == current_user.id)\
        .filter(models.Blog.id == id)\
        .first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return blog

