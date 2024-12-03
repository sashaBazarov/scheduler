import os
import json
import pytest
from unittest.mock import patch, mock_open
from task import Task
from commands.load_tasks import load_tasks


@patch("os.listdir")
@patch("builtins.open", new_callable=mock_open)
def test_load_tasks_success(mock_open, mock_listdir):
    # Arrange: Mock directory listing and file contents
    mock_listdir.return_value = ["task1.json", "task2.json"]
    task_data_1 = {"id": "1", "name": "Task 1"}
    task_data_2 = {"id": "2", "name": "Task 2"}
    mock_open.side_effect = [
        mock_open(read_data=json.dumps(task_data_1)).return_value,
        mock_open(read_data=json.dumps(task_data_2)).return_value,
    ]

    # Act: Call load_tasks
    tasks = load_tasks()

    # Assert: Tasks are loaded correctly
    assert len(tasks) == 2
    assert tasks[0].id == "1"
    assert tasks[0].name == "Task 1"
    assert tasks[1].id == "2"
    assert tasks[1].name == "Task 2"


@patch("os.listdir")
@patch("builtins.open", new_callable=mock_open)
def test_load_tasks_with_invalid_json(mock_open, mock_listdir):
    # Arrange: Mock directory listing and file contents (one invalid JSON)
    mock_listdir.return_value = ["task1.json", "invalid_task.json"]
    valid_task_data = {"id": "1", "name": "Task 1"}
    mock_open.side_effect = [
        mock_open(read_data=json.dumps(valid_task_data)).return_value,
        mock_open(read_data="Invalid JSON").return_value,
    ]

    # Act: Call load_tasks and capture print output
    with patch("builtins.print") as mock_print:
        tasks = load_tasks()

    # Assert: Only the valid task is loaded
    assert len(tasks) == 1
    assert tasks[0].id == "1"
    assert tasks[0].name == "Task 1"

    # Assert: Error message is printed for invalid JSON
    mock_print.assert_called_with("Error loading task from 'tasks/invalid_task.json': Expecting value: line 1 column 1 (char 0)")


@patch("os.listdir")
@patch("builtins.open", new_callable=mock_open)
def test_load_tasks_no_files(mock_open, mock_listdir):
    # Arrange: Mock an empty directory
    mock_listdir.return_value = []

    # Act: Call load_tasks
    tasks = load_tasks()

    # Assert: No tasks are loaded
    assert len(tasks) == 0
