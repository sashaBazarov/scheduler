import os
import json
from typing import Tuple
from task import Task

tasks_directory = "tasks/"

def load_tasks() -> Tuple[Task]:
    """
    Загрузка задач из JSON файлов в директории tasks.
    Эта функция читает все JSON файлы в указанной директории tasks,
    десериализует их в объекты Task и возвращает их в виде кортежа.
    Возвращает:
        Tuple[Task]: Кортеж, содержащий все успешно загруженные объекты Task.
    Вызывает:
        FileNotFoundError: Если директория tasks не существует.
        OSError: Если возникла проблема при чтении файлов в директории.
        json.JSONDecodeError: Если файл содержит некорректный JSON.
        TypeError: Если JSON не соответствует структуре объекта Task.
    """

    return tuple(
        task
        for file in os.listdir(tasks_directory) if file.endswith(".json")
        for task in [load_task(os.path.join(tasks_directory, file))]
        if task is not None
    )


def load_task(file_path):
    """
    Загрузка задачи из JSON файла.

    Аргументы:
        file_path (str): Путь к JSON файлу, содержащему данные задачи.

    Возвращает:
        Task: Экземпляр класса Task, заполненный данными из JSON файла.
        None: Если произошла ошибка при загрузке или декодировании JSON файла.

    Вызывает:
        json.JSONDecodeError: Если JSON файл не может быть декодирован.
        TypeError: Если данные JSON не соответствуют ожидаемому формату для класса Task.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return Task(**json.load(f))
    except (json.JSONDecodeError, TypeError) as e:
        print(f"Error loading task from '{file_path}': {e}")
        return None