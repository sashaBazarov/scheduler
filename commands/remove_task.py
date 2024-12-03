from find_task import find_task
from task_io import delete_task


def remove_task(task_id):
    task = find_task(task_id)
    if not task:
        raise ValueError(f"Task with id {task_id} not found.")
    delete_task(task)
    print(f"Task with id {task.id} has been deleted.")
