from src.Task.repository.base_tasks_repository import BaseTaskRepository
from src.Task.repository.tasks_repository import get_tasks_repository
from src.Task.tasks_exception import TasksNotFoundException, TasksNameCannotBeEmpty
from fastapi import Depends

class DeleteTasks:
    def __init__(self,tasks_repository: BaseTaskRepository) -> None:
        self._repository = tasks_repository

    async def delete(self,task_id: int) -> bool:
        if await self._repository.get(task_id):
            await self._repository.delete(task_id)
            return True
        elif not task_id:
            raise TasksNameCannotBeEmpty("ID задачи обязателен для удаления.")
        else:
            raise TasksNotFoundException("Задача не найдена.")

def get_delete_task_service(tasks_repository: BaseTaskRepository = Depends(get_tasks_repository)) -> DeleteTasks:
    return DeleteTasks(tasks_repository=tasks_repository)