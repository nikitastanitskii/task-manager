from src.Task.repository.base_tasks_repository import BaseTaskRepository
from src.Task.repository.tasks_repository import get_tasks_repository
from src.models import Task
from fastapi import Depends

class GetAllTasks:
    def __init__(self, tasks_repository: BaseTaskRepository) -> None:
        self._repository = tasks_repository

    async def get_all(self) -> list[Task]:
        return await self._repository.get_all()


def get_all_task_service(tasks_repository: BaseTaskRepository = Depends(get_tasks_repository)) -> GetAllTasks:
    return GetAllTasks(tasks_repository=tasks_repository)
