import pytest
from unittest.mock import patch, MagicMock
from commands.view_tasks import view_tasks
from task import Task

@pytest.fixture
def mock_load_tasks():
    with patch('commands.view_tasks.load_tasks') as mock:
        yield mock

@pytest.fixture
def mock_filter_tasks():
    with patch('commands.view_tasks.filter_tasks') as mock:
        yield mock

@pytest.fixture
def mock_tabulate():
    with patch('commands.view_tasks.tabulate') as mock:
        yield mock

@pytest.fixture
def mock_print():
    with patch('builtins.print') as mock:
        yield mock


def test_view_tasks(mock_load_tasks, mock_filter_tasks, mock_tabulate, mock_print):
    # Create mocked tasks
    task1 = MagicMock(spec=Task)
    task1.to_list.return_value = ["Task 1", "Description 1", "Work", "2023-10-01", "High", "Pending", 1]
    task2 = MagicMock(spec=Task)
    task2.to_list.return_value = ["Task 2", "Description 2", "Home", "2023-10-02", "Low", "Completed", 2]

    # Mock the return values
    mock_load_tasks.return_value = [task1, task2]
    mock_filter_tasks.return_value = [task1]
    mock_tabulate.return_value = "Mocked Table"

    # Call the view_tasks function
    view_tasks(category="Work", status="Pending")

    # Asserts for mock calls
    mock_load_tasks.assert_called_once()
    mock_filter_tasks.assert_called_once_with(
        [task1, task2], "Work", "Pending", None, None
    )
    mock_tabulate.assert_called_once_with(
        [["Task 1", "Description 1", "Work", "2023-10-01", "High", "Pending", 1]],
        ["Title", "Description", "Category", "Date", "Priority", "Status", "ID"],
        tablefmt="grid"
    )
    mock_print.assert_called_once_with("Mocked Table")
