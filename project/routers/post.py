from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from schema import PostBase, PostDisplay
from database import db_post
from database.database import get_db

router = APIRouter(
    prefix="/post",
    tags=[
        "post",
    ],
)


@router.post("/new", response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create_post(db, request)
