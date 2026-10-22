from fastapi import APIRouter,Depends
from src.task import controller
from src.task.dtos import TaskSchema
from src.utils.db import get_db

routes=APIRouter(prefix="/api/v1")

@routes.post("/tasks")
def create_task(body:TaskSchema,db=Depends(get_db)):
    return controller.create_task(body,db)

@routes.get("/tasks")
def get_tasks(db=Depends(get_db)):
    return controller.get_tasks(db)

@routes.get("/tasks/{task_id}")
def get_task_by_id(task_id:int,db=Depends(get_db)):
    return controller.get_task_by_id(task_id,db)

@routes.put("/tasks/{task_id}")
def update_task_by_id(task_id:int,payload:TaskSchema,db=Depends(get_db)):
    return controller.update_task_by_id(task_id,payload,db)

@routes.delete("/tasks/{task_id}")
def delete_task_by_id(task_id:int,db=Depends(get_db)):
    return controller.delete_task_by_id(task_id,db)

