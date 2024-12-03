from datetime import datetime
from uuid import uuid1
from task import Task
from task_io import save_task
from find_task import find_task


def add_task():
    title = get_input("Enter the task name: ", null_validator)
    description = get_input("Enter the task description: ", null_validator)
    date = get_input(
        "Enter the task due date (in format '28 May 1994'): ",
        validator=validate_date,
        error_message="The date must be in the format '28 May 1994'."
    )
    category = get_input("Enter the task category: ", null_validator)
    priority = get_input(
        "Enter the task priority (e.g., 'High', 'Medium', 'Low'): ",
        null_validator,
        error_message="Priority must be one of: 'High', 'Medium', 'Low'."
    )

    task = Task(
        id=get_id(),
        title=title,
        description=description,
        due_date=date,
        category=category,
        priority=priority
    )

    save_task(task)

    print("Task created")


def get_id():
    task_id = str(uuid1())[:6]

    while find_task(task_id):
        task_id = str(uuid1())[:6]
    return task_id


def get_input(prompt, validator=None, error_message="Invalid input, please try again:"):

    while True:
        try:
            user_input = input(prompt).strip()
            if validator and not validator(user_input):
                raise ValueError
            return user_input
        except ValueError:
            print(error_message)


def validate_date(date_string):

    try:
        datetime.strptime(date_string, "%d %B %Y")
        return True
    except ValueError:
        return False
    
def null_validator(string):
    return string != ""
