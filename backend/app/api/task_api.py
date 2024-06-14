from fastapi import APIRouter, HTTPException
from app.crud.task_crud import create_task
from app.schemas.task_schemas import TaskCreateRequest, TaskResponse

router = APIRouter()

@router.post("/tasks/", response_model=TaskResponse)
def create_task_endpoint(task: TaskCreateRequest):
    result = create_task(task_title=task.task_title, task_description=task.task_description)
    if isinstance(result, str):
        raise HTTPException(status_code=400, detail=result)
    return result
