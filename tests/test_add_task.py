import pytest
from unittest.mock import patch, MagicMock, ANY
from commands.add_task import add_task
from task import Task


@pytest.fixture
def mock_inputs():
    with patch('commands.add_task.get_input') as mock_get_input:
        mock_get_input.side_effect = [
            "Test Task",
            "Test Description",
            "28 May 1994", 
            "Test Category",
            "Высокий"
        ]
        yield mock_get_input


@pytest.fixture
def mock_find_task():
    with patch('commands.add_task.find_task') as mock:
        mock.return_value = False
        yield mock


@pytest.fixture
def mock_save_task():
    with patch('commands.add_task.save_task') as mock:
        yield mock


@pytest.fixture
def mock_task():
    with patch('commands.add_task.Task') as MockTask:
        yield MockTask


def test_add_task(mock_task, mock_find_task, mock_save_task, mock_inputs):
    add_task()

    mock_task.assert_called_once_with(
        id=ANY,
        title="Test Task",
        description="Test Description",
        due_date="28 May 1994",
        category="Test Category",
        priority="Высокий"
    )

    mock_save_task.assert_called_once_with(mock_task.return_value)
