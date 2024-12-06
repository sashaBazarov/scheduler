import commands

def load_command(command: str):
    """
    Загрузите соответствующую функцию для данной командной строки.

    Аргументы:
        command (str): Командная строка для загрузки функции.

    Возвращает:
        function: Функция, соответствующая данной командной строке, или None, если команда не распознана.
    """
    return {
        "exit": exit,
        "addtask": commands.add_task,
        "clear": commands.clear,
        "tasks": commands.view_tasks,
        "edittask": commands.edit_task,
        "done": commands.mark_done,
        "del": commands.remove_task
    }.get(command)
