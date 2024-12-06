import pytest
from unittest.mock import patch, MagicMock
from commands.remove_task import remove_task


@pytest.fixture
def mock_find_task():
    with patch("commands.remove_task.find_task") as mock:
        yield mock


def test_remove_task_not_found(mock_find_task):
    # Мокируем отсутствие задачи
    mock_find_task.return_value = None

    # Вызываем remove_task и проверяем, что выбрасывается ValueError
    with pytest.raises(ValueError) as context:
        remove_task("123")

    # Access the exception message correctly
    assert str(context.value) == "Task with id 123 not found."
    mock_find_task.assert_called_once_with("123")
