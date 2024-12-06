from task_io import load_tasks
from tabulate import tabulate
from .filter_task import filter_tasks


def view_tasks(category: str = None, status: str = None, keywords: str = None, priority: str = None):
    """
    Отображает список задач, отфильтрованных по заданным критериям.

    Аргументы:
        category (str, optional): Категория для фильтрации задач. По умолчанию None.
        status (str, optional): Статус для фильтрации задач. По умолчанию None.
        keywords (str, optional): Ключевые слова для фильтрации задач. По умолчанию None.
        priority (str, optional): Приоритет для фильтрации задач. По умолчанию None.

    Возвращает:
        None
    """

    tasks = load_tasks()
    # Фильтрует задачи по аргументам
    filtered_tasks = list(map(lambda task: task.to_list(), filter_tasks(tasks, category, status, keywords, priority)))

    headers = ["Title", "Description", "Category",
               "Date", "Priority", "Status", "ID"]

    print(tabulate(filtered_tasks, headers, tablefmt="grid")) #Выводим таблицу
