tasks = []
next_id = 1

def add_task(title):
  global next_id
  task = {
    'id': next_id,
    'title': title,
    'completed': False
  }
  tasks.append(task)
  next_id += 1

def get_tasks():
  return tasks

def complete_task(task_id):
  for task in tasks:
    if task['id'] == task_id:
      task['completed'] = True
      return None
  print(f"Task with id {task_id} not found.")

def delete_task(task_id):
  for i, task in enumerate(tasks): 
    if task['id'] == task_id:
      tasks.pop(i)
      return None
  print(f"Task with id {task_id} not found.")