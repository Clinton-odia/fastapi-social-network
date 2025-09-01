from sqlalchemy.orm.session import Session
from schema import UserBase
from .models import User
from .hash import Hash
from fastapi import HTTPException


def create_user(db: Session, request: UserBase):
    new_user = User(
        username=request.username,
        email=request.email,
        password=Hash(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
