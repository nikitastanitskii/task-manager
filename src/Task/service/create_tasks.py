from src.Task.repository.base_tasks_repository import BaseTaskRepository
from src.Task.repository.tasks_repository import get_tasks_repository
from src.models import Task
from src.Task.tasks_exception import TasksNameCannotBeEmpty
from fastapi import Depends

class CreateTasks:
    def __init__(self, tasks_repository: BaseTaskRepository) -> None:
        self._repository = tasks_repository

    async def create(self, task_data: Task) -> None:
        if not task_data.name:
            raise TasksNameCannotBeEmpty("Название задачи не может быть пустым!")
        await self._repository.create(task_data)

def get_create_tasks_service(tasks_repository: BaseTaskRepository = Depends(get_tasks_repository)) -> CreateTasks:
    return CreateTasks(tasks_repository=tasks_repository)