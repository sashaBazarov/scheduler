from datetime import datetime
from uuid import uuid1
from task import Task
from task_io import save_task
from find_task import find_task


def add_task():
    """
    Запрашивает у пользователя ввод данных для новой задачи, проверяет ввод, 
    создает объект Task и сохраняет его.

    Функция запросит следующие данные:
    - Название задачи
    - Описание задачи
    - Дата выполнения задачи (в формате '28 May 1994')
    - Категория задачи
    - Приоритет задачи (например, 'High', 'Medium', 'Low')

    Каждый ввод проверяется с использованием предоставленных валидаторов. 
    Если ввод недействителен, будет отображено сообщение об ошибке, и 
    пользователю будет предложено ввести информацию снова.

    После того как все вводы будут действительными, создается объект Task 
    с уникальным идентификатором и предоставленными данными, и задача сохраняется.

    Наконец, выводится сообщение подтверждения "Task created".
    """

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
    """
    Генерирует уникальный идентификатор задачи длиной 6 символов.

    Эта функция генерирует уникальный идентификатор задачи, создавая UUID и 
    беря первые 6 символов. Она гарантирует уникальность идентификатора, 
    проверяя его по существующим идентификаторам задач и регенерируя при необходимости.

    Возвращает:
        str: Уникальный идентификатор задачи длиной 6 символов.
    """

    while find_task(task_id := str(uuid1())[:6]):
        pass
    return task_id



def get_input(prompt, validator=None, error_message="Invalid input, please try again:"):
    """
    Постоянно запрашивает ввод пользователя, пока не будет предоставлен допустимый ввод.

    Аргументы:
        prompt (str): Сообщение, отображаемое пользователю при запросе ввода.
        validator (callable, optional): Функция, которая принимает ввод пользователя в качестве аргумента и возвращает True, если ввод допустим, и False в противном случае. По умолчанию None.
        error_message (str, optional): Сообщение, отображаемое пользователю, когда ввод недействителен. По умолчанию "Invalid input, please try again:".

    Возвращает:
        str: Допустимый ввод пользователя.
    """

    while True:
        try:
            user_input = input(prompt).strip()
            if validator and not validator(user_input):
                raise ValueError
            return user_input
        except ValueError:
            print(error_message)


def validate_date(date_string):
    """
    Проверяет, является ли данная строка даты в формате "dd MMMM yyyy".

    Аргументы:
        date_string (str): Строка даты для проверки.

    Возвращает:
        bool: True, если строка даты действительна, иначе False.
    """

    try:
        datetime.strptime(date_string, "%d %B %Y")
        return True
    except ValueError:
        return False
    
def null_validator(string):
    """
    Проверяет, что данная строка не пуста.

    Аргументы:
        string (str): Строка для проверки.

    Возвращает:
        bool: True, если строка не пуста, иначе False.
    """
    return string != ""
