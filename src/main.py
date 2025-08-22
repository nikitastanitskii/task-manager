from fastapi import FastAPI, APIRouter
import uvicorn
from src.Task.views import tasks_router

app = FastAPI()

api_router = APIRouter()
api_router.include_router(tasks_router, tags=["Task Manager Service"])
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )