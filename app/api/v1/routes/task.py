from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schema.task_schema import TaskSchema
from app.services.task_service import TaskService

router = APIRouter(tags=["Tasks"])


def get_task_service(db: Annotated[Session, Depends(get_db)]) -> TaskService:
    """Dependency to get task service"""
    return TaskService(db=db)


@router.post("", summary="Create a new task")
@router.post("/", include_in_schema=False)
def create_task(
    body: TaskSchema,
    task_service: Annotated[TaskService, Depends(get_task_service)],
):
    """Create a new task"""
    return task_service.create_task(body)


@router.get("", summary="Get all tasks")
@router.get("/", include_in_schema=False)
def get_tasks(
    task_service: Annotated[TaskService, Depends(get_task_service)],
):
    """Get all tasks"""
    return task_service.get_tasks()


@router.get("/{task_id}", summary="Get task by ID")
def get_task_by_id(
    task_id: int,
    task_service: Annotated[TaskService, Depends(get_task_service)],
):
    """Get a task by its ID"""
    return task_service.get_task_by_id(task_id)


@router.put("/{task_id}", summary="Update task by ID")
def update_task_by_id(
    task_id: int,
    payload: TaskSchema,
    task_service: Annotated[TaskService, Depends(get_task_service)],
):
    """Update a task by its ID"""
    return task_service.update_task_by_id(task_id, payload)


@router.delete("/{task_id}", summary="Delete task by ID")
def delete_task_by_id(
    task_id: int,
    task_service: Annotated[TaskService, Depends(get_task_service)],
):
    """Delete a task by its ID"""
    return task_service.delete_task_by_id(task_id)
