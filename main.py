from fastapi import FastAPI
from src.utils.db import Base, engine
from src.task.router import routes

Base.metadata.create_all(engine)

app=FastAPI()

app.include_router(routes)