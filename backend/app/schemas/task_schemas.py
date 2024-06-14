from pydantic import BaseModel

class TaskCreateRequest(BaseModel):
    task_title: str
    task_description: str

class TaskResponse(BaseModel):
    task_id: int
    task_title: str
    task_description: str
