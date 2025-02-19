from fastapi import APIRouter, HTTPException, BackgroundTasks
from ..models.task import Task
from ..core.database import db

router = APIRouter()

@router.post("/", response_model=Task)
async def create_task(task: Task, background_tasks: BackgroundTasks):
    task_dict = task.dict()
    task_dict["id"] = str(task_dict["id"])
    await db.db.tasks.insert_one(task_dict)
    background_tasks.add_task(notify_task_creation, task_dict)
    return task_dict

@router.get("/{task_id}", response_model=Task)
async def read_task(task_id: str):
    task = await db.db.tasks.find_one({"id": task_id})
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")

async def notify_task_creation(task: dict):
    # Здесь можно добавить логику уведомления
    print(f"Task created: {task}")