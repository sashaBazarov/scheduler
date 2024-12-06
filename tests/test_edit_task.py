import pytest
from unittest.mock import patch, MagicMock
from commands.edit_task import edit_task


@pytest.fixture
def mock_find_task():
    with patch('commands.edit_task.find_task') as mock:
        yield mock


def test_edit_task_not_found(mock_find_task):
    """
    Тест, проверяющий поведение при отсутствии задачи с указанным ID.
    """
    mock_find_task.return_value = None

    with patch('builtins.print') as mocked_print:
        with pytest.raises(ValueError) as context:
            edit_task(1)

        assert str(context.value) == "Task 1 was not found"
        mock_find_task.assert_called_once_with(1)
        mocked_print.assert_not_called()
        