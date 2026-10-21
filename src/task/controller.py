from src.task.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.task.models import Task 

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
    
    return {
        "status_code":200,
        "success":True,
        "message":"Task created successfully",
        "data":new_task
    }