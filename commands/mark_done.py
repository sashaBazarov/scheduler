from task_io import save_task
from find_task import find_task


def mark_done(task_id: str):
    
    task = find_task(task_id)

    if not task:
        raise ValueError(f"Task with ID {task_id} not found.")

    task.status = "Done"

    save_task(task)

    print(f"Task {task_id} marked as done.")