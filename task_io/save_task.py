from task import Task


def save_task(task: Task):
    with open(f"tasks/{task.id}.json", "w+", encoding="utf-8") as f:
        f.write(task.to_json())
