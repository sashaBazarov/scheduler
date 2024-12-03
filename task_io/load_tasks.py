import os
import json
from typing import Tuple
from task import Task

def load_tasks() -> Tuple[Task]:
    tasks_directory = "tasks/"
    
    def load_task(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return Task(**json.load(f))
        except (json.JSONDecodeError, TypeError) as e:
            print(f"Error loading task from '{file_path}': {e}")
            return None

    return tuple(
        task
        for file in os.listdir(tasks_directory) if file.endswith(".json")
        for task in [load_task(os.path.join(tasks_directory, file))]
        if task is not None
    )
