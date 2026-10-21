from fastapi import APIRouter,Depends
from src.task import controller
from src.task.dtos import TaskSchema
from src.utils.db import get_db

routes=APIRouter(prefix="/api/v1")

@routes.post("/tasks")
def create_task(body:TaskSchema,db=Depends(get_db)):
    return controller.create_task(body,db)

