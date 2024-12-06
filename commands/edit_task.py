from find_task import find_task
from task import Task
from task_io import save_task
from exceptions import CommandException
from find_task import find_task
from task import Task
from task_io import save_task
from exceptions import CommandException


def edit_task(*args, **kwargs):
    """
    Редактировать существующую задачу с заданными атрибутами.

    Аргументы:
        *args: Позиционные аргументы, где первый аргумент - это ID задачи.
        **kwargs: Именованные аргументы, представляющие атрибуты для обновления и их новые значения.

    Исключения:
        CommandException: Если не предоставлены аргументы.
        ValueError: Если предоставлен недопустимый атрибут в kwargs.

    Возвращает:
        None

    Пример:
        edit_task(1, name="Новое имя задачи", priority="Высокий")
    """
    if not args:
        raise CommandException("No required arguments", "edittasks", *args, **kwargs)

    task_id = args[0]

    task: Task = find_task(task_id)
    if not task:
        raise ValueError(f"Task {task_id} was not found")
        return 

    attrs = task.get_attrs()

    for kwarg in kwargs: # Проходим по массиву аргументов и проверяем правильноть аргументов
        if kwarg not in attrs: 
            raise ValueError(f"Invalid attribute: {kwarg}")
        setattr(task, kwarg, kwargs[kwarg])

    save_task(task)

    print("Task updated")
