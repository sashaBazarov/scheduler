```markdown
# Task Manager CLI Documentation

## Overview

This Task Manager CLI allows you to manage tasks through a command-line interface. You can create, view, edit, delete, and filter tasks with ease. 

## Commands

### 1. `addtask`
Creates a new task.

**Usage:**
```bash
addtask
```
You will be prompted to input task details such as title, description, category, priority, etc.

---

### 2. `tasks [filters]`
Displays a list of tasks filtered by optional criteria.

**Usage:**
```bash
tasks [--category CATEGORY] [--status STATUS] [--keywords KEYWORDS] [--priority PRIORITY]
```

**Filters:**
- `--category` - Filter tasks by category.
- `--status` - Filter tasks by status.
- `--keywords` - Filter tasks containing specific keywords in their title or description.
- `--priority` - Filter tasks by priority.

**Example:**
```bash
tasks --category Work --status Completed
```

---

### 3. `done task_id`
Marks a task as completed.

**Usage:**
```bash
done <task_id>
```

**Example:**
```bash
done 1
```

---

### 4. `del task_id`
Deletes a task.

**Usage:**
```bash
del <task_id>
```

**Example:**
```bash
del 1
```

---

### 5. `edittask task_id [values]`
Edits an existing task by updating specified attributes.

**Usage:**
```bash
edittask <task_id> [attribute=value ...]
```

**Attributes:**
- `title` - Update the title of the task.
- `description` - Update the task's description.
- `category` - Update the task's category.
- `priority` - Update the task's priority.
- `status` - Update the task's status.

**Example:**
```bash
edittask 1 title="New Title" priority="High"
```

---

### 6. `clear`
Deletes all tasks from the task list.

**Usage:**
```bash
clear
```

---

## Task Viewing Example
The `tasks` command will output tasks in a tabular format. For example:

```bash
tasks --priority High
```
## Task Attributes

Each task includes the following attributes:

- `id` *(str)*: A unique identifier for the task.
- `title` *(str)*: The name of the task.
- `description` *(str)*: A detailed description of the task.
- `category` *(str)*: The category the task belongs to.
- `due_date` *(str)*: The deadline for the task in the format `dd Month yyyy`.
- `priority` *(str)*: The priority level of the task (`Low`, `Medium`, `High`).
- `status` *(str)*: The current status of the task (`Not done`, `In progress`, `Completed`).

---

**Output:**
```
+--------+-------------------+------------+---------------------+----------+-----------+----+
| Title  | Description       | Category   | Date                | Priority | Status    | ID |
+--------+-------------------+------------+---------------------+----------+-----------+----+
| Task 1 | Example Task      | Work       | 2024-12-08 10:00    | High     | In Progress | 1 |
+--------+-------------------+------------+---------------------+----------+-----------+----+
```

---

## Exception Handling
The CLI handles errors gracefully:
- If required arguments are missing, it will prompt you for proper usage.
- Invalid attributes for `edittask` will raise an error with the invalid attribute name.

**Example Error:**
```bash
Invalid attribute: due_date
```

---

## Dependencies
- Python Libraries:
  - `tabulate` (for rendering tables in the terminal)
  - `find_task`, `task`, `task_io` (custom modules for task operations)
- Ensure proper setup of the `Task` class and related modules.

---

## Notes
- Tasks are saved automatically after modifications using the `save_task` function.
- Task data is loaded dynamically from storage using `load_tasks`.

---

## Future Enhancements
- Add support for recurring tasks.
- Include task reminders and notifications.
```
