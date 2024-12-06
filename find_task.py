from task_io import load_tasks

def find_task(task_id):
    """
    Найти задачу по её ID.
    Аргументы:
        task_id (int): ID задачи, которую нужно найти.
    Возвращает:
        Task: Задача с указанным ID, если найдена, иначе None.
    """
    tasks = load_tasks()

    for task in tasks:
        if task.id == task_id:
            return task
        else:
            continue
    
    return None
