import commands


def load_command(command: str):
    return {
        "exit": exit,
        "addtask": commands.add_task,
        "clear": commands.clear,
        "tasks": commands.view_tasks,
        "edittask": commands.edit_task,
        "done": commands.mark_done,
        "del": commands.remove_task
    }.get(command)
