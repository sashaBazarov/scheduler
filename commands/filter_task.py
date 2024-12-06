from typing import Set
from task import Task
from task_io import load_tasks
from difflib import get_close_matches


def filter_tasks(tasks: Set[Task], category: str= None, status: str = None, keywords: str = None, priority:str = None):
    """
    Фильтрует набор задач на основе предоставленных критериев.

    Аргументы:
        tasks (Set[Task]): Набор объектов Task для фильтрации.
        category (str, optional): Категория для фильтрации задач. По умолчанию None.
        status (str, optional): Статус для фильтрации задач. По умолчанию None.
        keywords (str, optional): Строка ключевых слов, разделенных пробелами, для фильтрации задач. По умолчанию None.
        priority (str, optional): Приоритет для фильтрации задач. По умолчанию None.

    Возвращает:
        List[Task]: Список задач, соответствующих предоставленным критериям.
    """
    if keywords:
        keyword_list = keywords.lower().split()
        tasks = filter_tasks_by_keyword(tasks, keyword_list)

    filtered_tasks = [
        task
        for task in tasks
        if (category is None or task.category.lower() == category.lower()) and
           (status is None or task.status.lower() == status.lower()) and
           (priority is None or task.priority.lower() == priority.lower())
    ] 

    return filtered_tasks


def filter_tasks_by_keyword(tasks, keyword_list):
    """
    Фильтрует список задач на основе списка ключевых слов.

    Аргументы:
        tasks (list): Список объектов задач, где каждая задача имеет атрибут 'title'.
        keyword_list (list): Список ключевых слов для фильтрации задач.

    Возвращает:
        list: Список задач, содержащих любое из ключевых слов в их заголовке.
    """
    similarity_threshold = 0.6

    return [
        task
        for task in tasks
        if any(
            get_close_matches(keyword, task.title.lower(
            ).split(), cutoff=similarity_threshold)
            for keyword in keyword_list
        )
    ]
