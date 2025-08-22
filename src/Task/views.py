from fastapi import APIRouter, Depends, HTTPException

from src.Task.service.create_tasks import CreateTasks, get_create_tasks_service
from src.Task.service.delete_tasks import DeleteTasks, get_delete_task_service
from src.Task.service.get_all_tasks import GetAllTasks, get_all_task_service
from src.Task.service.get_tasks import GetTasks, get_tasks_service
from src.Task.service.update_tasks import get_update_tasks_service, UpdateTasks
from src.Task.status_model import TaskCreate
from src.Task.tasks_exception import TasksAlreadyExists, TasksNotFoundException

tasks_router = APIRouter(prefix="/api/v1")


@tasks_router.post("/create", summary="Метод для создания задачи")
async def create_tasks(user_data: TaskCreate, create_task_service: CreateTasks = Depends(get_create_tasks_service)):
    try:
        await  create_task_service.create(user_data)
        return {"message": "Задача успешно создана"}
    except TasksAlreadyExists:
        raise HTTPException(status_code=409, detail="Такая задача уже существует")


@tasks_router.patch("/update", summary="Метод для обновления задачи")
async def update_tasks(user_id: int, user_data: TaskCreate, update_task_service: UpdateTasks = Depends(get_update_tasks_service)):
    try:
        await update_task_service.update(user_id,user_data)
        return {"message": "Задача успешно обновлена"}
    except TasksNotFoundException:
        raise HTTPException(status_code=404, detail="Задача не найдена")


@tasks_router.get("/get_all", summary="Метод для получения всех задач")
async def get_all_tasks(get_all_tasks_service: GetAllTasks = Depends(get_all_task_service)):
    tasks = await get_all_tasks_service.get_all()
    return tasks

@tasks_router.get("/get",summary="Метод для получения задачи")
async def get_tasks(user_id: int, get_task_service: GetTasks = Depends(get_tasks_service)):
    try:
        tasks = await get_task_service.get(user_id)
        return tasks
    except TasksNotFoundException:
        raise HTTPException(status_code=404, detail="Задача не найдена")

@tasks_router.delete("/delete", summary="Метод для удаления задачи")
async def delete_tasks(user_id: int, delete_task_service: DeleteTasks = Depends(get_delete_task_service)):
    try:
        await delete_task_service.delete(user_id)
        return {"message": "Задача успешно удалена"}
    except TasksNotFoundException:
        raise HTTPException(status_code=404, detail="Задача не найдена")


