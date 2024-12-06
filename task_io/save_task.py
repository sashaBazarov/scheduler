from task import Task


def save_task(task: Task):
    """
    Сохранить задачу в файл JSON.

    Аргументы:
        task (Task): Объект задачи, который нужно сохранить. Он должен иметь атрибут `id` и метод `to_json`.

    Исключения:
        IOError: Если произошла ошибка при записи в файл.
    """
    with open(f"tasks/{task.id}.json", "w+", encoding="utf-8") as f:
        f.write(task.to_json())
