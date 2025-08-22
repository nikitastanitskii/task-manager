from pydantic import BaseModel
from enum import Enum


class TaskStatus(str, Enum):
    CREATED = "created"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskCreate(BaseModel):
    name: str
    description: str | None = None
    status: TaskStatus = TaskStatus.CREATED
