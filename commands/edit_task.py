from find_task import find_task
from task import Task
from task_io import save_task
from exceptions import CommandException


from find_task import find_task
from task import Task
from task_io import save_task
from exceptions import CommandException


def edit_task(*args, **kwargs):
    
    if not args:
        raise CommandException("No required arguments", "edittasks", *args, **kwargs)

    task_id = args[0]

    task: Task = find_task(task_id)
    if not task:
        print("Task not found")
        return 
    
    for attr in task.get_attrs():
        if attr in kwargs:
            setattr(task, attr, kwargs[attr])

    save_task(task)

    print("Task updated")
