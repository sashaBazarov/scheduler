from task_io import save_task
from find_task import find_task


def mark_done(task_id: str):
    """
    Отмечает задачу как выполненную на основе предоставленного идентификатора задачи.
    Аргументы:
        task_id (str): Идентификатор задачи, которую нужно отметить как выполненную.
    Исключения:
        ValueError: Если задача с данным идентификатором не найдена.
    Возвращает:
        None
    """
    
    task = find_task(task_id)

    if not task:
        raise ValueError(f"Task with ID {task_id} not found.")

    task.status = "Done"

    save_task(task)

    print(f"Task {task_id} marked as done.")