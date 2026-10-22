import utils.session
from fastapi import FastAPI
from src.utils.db import Base, engine
from src.task.router import routes as task_routes
from src.product.router import routes as product_routes
from src.user.router import routes as user_routes

Base.metadata.create_all(engine)

app=FastAPI()

app.include_router(task_routes)
app.include_router(product_routes)
app.include_router(user_routes)