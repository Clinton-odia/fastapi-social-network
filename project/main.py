from fastapi import FastAPI
from routers import user, post
from database import models
from database.database import engine

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)


@app.get("/hello")
def get_hello():
    return {"message": "hello world"}


models.Base.metadata.create_all(engine)
