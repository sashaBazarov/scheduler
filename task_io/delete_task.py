from task import Task
import os


def delete_task(task: Task):
    path = f"tasks/{task.id}.json"

    if not os.path.exists(path):
        raise ValueError(f"Task with id {task.id} does not exist.")

    os.remove(path)
