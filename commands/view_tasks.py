from task_io import load_tasks
from tabulate import tabulate
from .filter_task import filter_tasks


def view_tasks(category=None, status=None, keywords=None, priority=None):

    tasks = load_tasks()
    filtered_tasks = list(map(lambda task: task.to_list(), filter_tasks(tasks, category, status, keywords, priority)))

    headers = ["Title", "Description", "Category",
               "Date", "Priority", "Status", "ID"]

    print(tabulate(filtered_tasks, headers, tablefmt="grid"))
