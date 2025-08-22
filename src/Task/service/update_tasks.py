from src.Task.repository.base_tasks_repository import BaseTaskRepository
from src.Task.repository.tasks_repository import get_tasks_repository
from src.Task.tasks_exception import TasksNameCannotBeEmpty
from src.models import Task
from fastapi import Depends

class UpdateTasks:
    def __init__(self,tasks_repository: BaseTaskRepository) -> None:
        self._repository = tasks_repository

    async def update(self,task_id: int, task_data: Task) -> None:
        if task_data.name is not None:
            raise TasksNameCannotBeEmpty("Название задачи не может быть пустым.")
        await self._repository.update(task_id, task_data)

def get_update_tasks_service(tasks_repository: BaseTaskRepository = Depends(get_tasks_repository)) -> UpdateTasks:
    return UpdateTasks(tasks_repository=tasks_repository)