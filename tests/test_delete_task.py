import os
import pytest
from unittest.mock import patch, MagicMock
from task import Task
from commands import delete_task


@patch("os.path.exists")
@patch("os.remove")
def test_delete_task_success(mock_remove, mock_exists):
    # Mock task object
    task = Task(id="123456")

    # Mock `os.path.exists` to simulate the file exists
    mock_exists.return_value = True

    # Call the function
    delete_task(task)

    # Assert that the path existence was checked and the file was removed
    mock_exists.assert_called_once_with(f"tasks/{task.id}.json")
    mock_remove.assert_called_once_with(f"tasks/{task.id}.json")


@patch("os.path.exists")
def test_delete_task_file_not_found(mock_exists):
    # Mock task object
    task = Task(id="123456")

    # Mock `os.path.exists` to simulate the file does not exist
    mock_exists.return_value = False

    # Verify that the function raises a ValueError
    with pytest.raises(ValueError) as exc_info:
        delete_task(task)

    # Check the exception message
    assert str(exc_info.value) == f"Task with id {task.id} does not exist."

    # Assert `os.remove` is not called
    mock_exists.assert_called_once_with(f"tasks/{task.id}.json")
