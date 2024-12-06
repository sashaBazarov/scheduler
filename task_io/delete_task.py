from task import Task
import os


def delete_task(task: Task):
    """
    Удаляет задачу, удаляя соответствующий JSON файл.

    Аргументы:
        task (Task): Объект задачи, который нужно удалить, содержащий атрибут 'id'.

    Исключения:
        ValueError: Если файл задачи не существует.
    """
    path = f"tasks/{task.id}.json"

    if not os.path.exists(path):
        raise ValueError(f"Task with id {task.id} does not exist.")

    os.remove(path)
