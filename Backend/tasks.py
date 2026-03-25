import json 
from pathlib import Path

DATA_FILE = ("task.json")

def load_tasks():
  if not DATA_FILE.exists():
    return[]
  
  with open(DATA_FILE, "r") as file:
    return json.load(file)

def save_tasks(tasks):
  with open(DATA_FILE, "w") as file:
    json.dump(tasks, file, indent=2)

tasks = load_tasks()

if tasks:
  next_id = max(task["id"] for task in tasks) + 1
else:
  next_id = 1

def add_task(title):
  global next_id

  task = {
    'id': next_id,
    'title': title,
    'completed': False
  }
  tasks.append(task)
  save_tasks(tasks)
  next_id += 1
  return task

def get_tasks():
  return tasks

def get_task(task_id):
  for task in tasks:
    if task["id"] == task_id:
      return task
  return None

def update_task(task_id, title, completed):
  for task in tasks:
    if task["id"] == task_id:
      task["title"] = title
      task["completed"] = completed
      save_tasks()
      return task
  return None

def delete_task(task_id):
  for i, task in enumerate(tasks): 
    if task["id"] == task_id:
      deleted_task = tasks.pop(i)
      save_tasks(tasks)
      return deleted_task
  return None