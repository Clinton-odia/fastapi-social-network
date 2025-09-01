from fastapi import FastAPI
from routers import user
from database import models
from database.database import engine

app = FastAPI()

app.include_router(user.router)


@app.get("/hello")
def get_hello():
    return {"message": "hello world"}


models.Base.metadata.create_all(engine)
