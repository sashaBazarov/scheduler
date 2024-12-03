import pytest
from unittest.mock import patch, MagicMock
from task import Task
from exceptions import CommandException
from commands.edit_task import edit_task


@patch('commands.edit_task.find_task')
@patch('commands.edit_task.save_task')
def test_edit_task_success(mock_save_task, mock_find_task):
    """
    Тест успешного редактирования задачи.
    Проверяет, что атрибуты задачи обновляются, и изменения сохраняются.
    """
    mock_task = MagicMock(spec=Task)
    mock_task.get_attrs.return_value = ['name', 'description']
    mock_find_task.return_value = mock_task

    edit_task(1, name="New Task Name", description="New Description")

    mock_find_task.assert_called_once_with(1)
    assert mock_task.name == "New Task Name"
    assert mock_task.description == "New Description"
    mock_save_task.assert_called_once_with(mock_task)


@patch('commands.edit_task.find_task')
def test_edit_task_not_found(mock_find_task):
    """
    Тест, проверяющий поведение при отсутствии задачи с указанным ID.
    """
    mock_find_task.return_value = None

    with patch('builtins.print') as mocked_print:
        edit_task(1)
        mocked_print.assert_called_once_with("Task not found")


def test_edit_task_no_args():
    """
    Тест, проверяющий выброс исключения, если не переданы аргументы.
    """
    with pytest.raises(CommandException) as exc_info:
        edit_task()

    exception = exc_info.value
    assert exception.message == "No required arguments"
    assert exception.command == "edittasks"
    assert exception.args == ()
    assert exception.kwargs == {}
