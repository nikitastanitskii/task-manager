from abc import ABC, abstractmethod
from src.models import Task

class BaseTaskRepository(ABC):
    @abstractmethod
    async def create(self,task_data: Task) -> None:
        pass

    @abstractmethod
    async def update(self,task_id: int, task_data: Task) -> Task:
        pass

    @abstractmethod
    async def get(self,task_id: int) -> Task | None:
        pass

    @abstractmethod
    async def get_all(self) -> list[Task]:
        pass

    @abstractmethod
    async def delete(self,task_id: int) -> bool:
        pass