from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from tasks import add_task, get_tasks, complete_task,delete_task 

app = FastAPI(title="StudyOS API")

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)


@app.get("/")
def root(): 
    return {"message": "studyOS API is running"}

@app.get("/tasks")
def read_tasks():
    return {"tasks": get_tasks()}


@app.post("/tasks", status_code=201)
def root():
    return {"message": "studyOS API is running"}

@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = add_task(task.title)
    return {"message": "Task created successfully", "task": new_task}

@app.put("/tasks/{task_id}")
def mark_task_complete(task_id: int):
    updated_task = complete_task(task_id)

    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return {"message": "Task completed", "task": updated_task}

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    deleted_task = delete_task(task_id)

    if deleted_task is None: 
      raise HTTPException(status_code=404, detail="Task not found")
    
    return {"message": "Task deleted", "task": deleted_task}


class TaskUpdate(BaseModel):
    title: str
    completed: bool

@app.put("/tasks/{task_id}")
def update_task_endpoint(task_id: int, updated: TaskUpdate):
    task = update_task(task_id, updated.title, updated.completed)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return {"message": "Task updated", "task": task}