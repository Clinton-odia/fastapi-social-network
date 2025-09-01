from schema import PostBase
from .models import Post
from sqlalchemy.orm.session import Session


def create_post(db: Session, request: PostBase):
    new_post = Post(
        title=request.title,
        content=request.content,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post
