from find_task import find_task
from task_io import delete_task


def remove_task(task_id):
    """
    Удалить задачу по её ID.

    Аргументы:
        task_id (int): ID задачи, которую нужно удалить.

    Исключения:
        ValueError: Если задача с данным ID не найдена.

    Возвращает:
        None
    """
    task = find_task(task_id)
    if not task:
        raise ValueError(f"Task with id {task_id} not found.")
    delete_task(task)
    print(f"Task with id {task.id} has been deleted.")
