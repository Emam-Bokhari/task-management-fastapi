from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class TaskSchema(BaseModel):
    title: str
    description: str
    is_completed: bool = False


class TaskResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: Optional[str] = None
    is_completed: bool
    created_at: Optional[datetime] = None
