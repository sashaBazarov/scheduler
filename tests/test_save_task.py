from task_io import save_task, load_tasks
from task import Task

# Save a sample task
task = Task(id="123", name="Sample Task", description="This is a test task")
save_task(task)

# Load tasks and verify the saved task is present
tasks = load_tasks()
assert len(tasks) > 0
assert tasks[0].id == "123"
assert tasks[0].name == "Sample Task"
print("Save and load tasks test passed.")
