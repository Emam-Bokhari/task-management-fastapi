from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.task import Task
from app.schema.task_schema import TaskSchema
from app.utils.send_response import send_response


class TaskService:
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, body: TaskSchema):
        data = body.model_dump()
        new_task = Task(
            title=data["title"],
            description=data["description"],
            is_completed=data["is_completed"],
        )
        self.db.add(new_task)
        self.db.commit()
        self.db.refresh(new_task)

        return send_response(
            success=True,
            status_code=status.HTTP_201_CREATED,
            message="Task is created successfully",
            data=data,
        )

    def get_tasks(self):
        data = self.db.query(Task).all()
        return send_response(
            success=True,
            status_code=status.HTTP_200_OK,
            message="Task are retrieved successfully",
            data=data,
        )

    def get_task_by_id(self, task_id: int):
        data = self.db.get(Task, task_id)
        if data is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task is not found",
            )
        return send_response(
            success=True,
            status_code=status.HTTP_200_OK,
            message="Task is retrieved successfully",
            data=data,
        )

    def update_task_by_id(self, task_id: int, payload: TaskSchema):
        task = self.db.get(Task, task_id)
        if task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task is not found",
            )
        task.title = payload.title
        task.description = payload.description
        task.is_completed = payload.is_completed

        self.db.commit()
        self.db.refresh(task)

        return send_response(
            success=True,
            status_code=status.HTTP_200_OK,
            message="Task is updated successfully",
            data=task,
        )

    def delete_task_by_id(self, task_id: int):
        task = self.db.get(Task, task_id)
        if task is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task is not found",
            )
        self.db.delete(task)
        self.db.commit()

        return send_response(
            success=True,
            status_code=status.HTTP_200_OK,
            message="Task is deleted successfully",
            data={},
        )


# Functional wrappers for convenience
def create_task(body: TaskSchema, db: Session):
    return TaskService(db).create_task(body)


def get_tasks(db: Session):
    return TaskService(db).get_tasks()


def get_task_by_id(task_id: int, db: Session):
    return TaskService(db).get_task_by_id(task_id)


def update_task_by_id(task_id: int, payload: TaskSchema, db: Session):
    return TaskService(db).update_task_by_id(task_id, payload)


def delete_task_by_id(task_id: int, db: Session):
    return TaskService(db).delete_task_by_id(task_id)
