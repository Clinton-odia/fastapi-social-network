from fastapi import APIRouter, Depends
from schema import UserDisplay, UserBase
from sqlalchemy.orm import Session
from database.database import get_db
from database import db_user

router = APIRouter(
    prefix="/user",
    tags=[
        "user",
    ],
)


@router.post("new", response_model=UserDisplay)
def create_user(db: Session, request=Depends(UserBase)):
    return db_user.create_user(db, request)
