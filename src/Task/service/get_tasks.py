from src.Task.repository.base_tasks_repository import BaseTaskRepository
from src.Task.repository.tasks_repository import get_tasks_repository
from src.models import Task
from fastapi import Depends

class GetTasks:
    def __init__(self, tasks_repository: BaseTaskRepository) -> None:
        self._repository = tasks_repository

    async def get(self,task_id: int) -> Task:
        return await self._repository.get(task_id)


def get_tasks_service(tasks_repository: BaseTaskRepository = Depends(get_tasks_repository)) -> GetTasks:
    return GetTasks(tasks_repository=tasks_repository)