from task_io import load_tasks

def find_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task.id == task_id:
            return task
        else:
            continue
    
    return None
