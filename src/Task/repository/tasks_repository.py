from src.Task.repository.base_tasks_repository import BaseTaskRepository
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from src.Task.status_model import TaskStatus
from src.db.base import get_session
from src.models import Task
from sqlalchemy import select, update

class TaskRepository(BaseTaskRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, task_data: Task) -> None:
        task = Task(
            name=task_data.name,
            description=task_data.description,
            status=task_data.status,
        )
        self._session.add(task)
        await self._session.commit()
        await self._session.refresh(task)

    async def update(self,task_id: int, task_data: Task) -> Task:
        db_task = await self._session.get(Task, task_id)

        if db_task.name is not None:
            db_task.name = task_data.name
        if db_task.description is not None:
            db_task.description = task_data.description

        await self._session.commit()
        await self._session.refresh(db_task)
        return db_task

    async def get(self,task_id: int) -> Task | None:
        task_stmt = select(Task).filter(Task.id == task_id)
        result = await self._session.execute(task_stmt)
        return result.scalar_one_or_none()

    async def get_all(self) -> list[Task]:
        task_stmt = select(Task)
        task = await self._session.execute(task_stmt)
        return task.scalars().all()

    async def delete(self,task_id: int) -> bool:
        # Обновляем статус на done и помечаем как удалённую
        update_stmt = (
            update(Task)
            .where(Task.id == task_id)
            .values(status=TaskStatus.DONE, is_deleted=True)
        )
        await self._session.execute(update_stmt)
        await self._session.commit()
        return True

def get_tasks_repository(session: AsyncSession = Depends(get_session)) -> TaskRepository:
    return TaskRepository(session=session)
