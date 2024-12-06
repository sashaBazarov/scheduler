import os
import pytest
from unittest.mock import patch, MagicMock
from task import Task
from commands import delete_task


@patch("os.path.exists")
@patch("os.remove")
def test_delete_task_success(mock_remove, mock_exists):
    task = Task(id="123456")

    mock_exists.return_value = True

    delete_task(task)

    mock_exists.assert_called_once_with(f"tasks/{task.id}.json")
    mock_remove.assert_called_once_with(f"tasks/{task.id}.json")


@patch("os.path.exists")
def test_delete_task_file_not_found(mock_exists):
    task = Task(id="123456")

    mock_exists.return_value = False

    with pytest.raises(ValueError) as exc_info:
        delete_task(task)

    assert str(exc_info.value) == f"Task with id {task.id} does not exist."

    mock_exists.assert_called_once_with(f"tasks/{task.id}.json")
