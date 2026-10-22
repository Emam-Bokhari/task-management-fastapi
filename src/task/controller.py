from src.task.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.task.models import Task 
from fastapi import HTTPException
from src.utils.send_response import send_response

def create_task(body:TaskSchema,db:Session):

    data=body.model_dump()

    new_task=Task(
        title=data["title"], 
        description=data["description"], 
        is_completed=data["is_completed"]
        )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return send_response(
        success=True,
        status_code=201,
        message="Task is created successfully",
        data=data
    )

def get_tasks(db:Session):

    data=db.query(Task).all()

    return send_response(
        success=True,
        status_code=200,
        message="Task are retrieved successfully",
        data=data
    )

def get_task_by_id(task_id:int,db:Session):

    # legacy
    # data=db.query(Task).get(task_id)
    data=db.get(Task,task_id)

    return send_response(
        success=True,
        status_code=200,
        message="Task is retrieved successfully",
        data=data
    )

def update_task_by_id(task_id:int,payload:TaskSchema,db:Session):
    task=db.get(Task,task_id)

    if task is None:
       raise HTTPException(
        status_code=404,
        detail="Task is not found"
    )

    task.title=payload.title 
    task.description=payload.description
    task.is_completed=payload.is_completed

    db.commit()
    db.refresh(task)

    return send_response(
        success=True,
        status_code=200,
        message="Task is updated successfully",
        data=task
    )


def delete_task_by_id(task_id:int,db:Session):
    task=db.get(Task,task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task is not found"
        )

    db.delete(task)
    db.commit()

    return send_response(
        success=True,
        status_code=200,
        message="Task is deleted successfully",
        data={}
    )