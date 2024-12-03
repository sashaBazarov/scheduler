import unittest
from unittest.mock import patch, MagicMock
from commands.add_task import add_task, get_input, validate_date
from task import Task
from task_io import save_task
from find_task import find_task

class TestAddTask(unittest.TestCase):

    @patch('commands.add_task.get_input')
    @patch('commands.add_task.save_task')
    @patch('commands.add_task.find_task')
    @patch('commands.add_task.Task')
    def test_add_task(self, MockTask, mock_find_task, mock_save_task, mock_get_input):
        # Mock inputs
        mock_get_input.side_effect = [
            "Test Task",  # title
            "Test Description",  # description
            "28 May 1994",  # date
            "Test Category",  # category
            "Высокий"  # priority
        ]

        # Mock find_task to return False (no task with the same ID exists)
        mock_find_task.return_value = False

        # Call the function
        add_task()

        # Check if Task was created with correct parameters
        MockTask.assert_called_once_with(
            id=unittest.mock.ANY,
            title="Test Task",
            description="Test Description",
            due_date="28 May 1994",
            category="Test Category",
            priority="Высокий"
        )

        # Check if save_task was called with the created task
        mock_save_task.assert_called_once_with(MockTask.return_value)

    def test_validate_date(self):
        self.assertTrue(validate_date("28 May 1994"))
        self.assertFalse(validate_date("1994-05-28"))
        self.assertFalse(validate_date("28/05/1994"))
        self.assertFalse(validate_date("invalid date"))


if __name__ == '__main__':
    unittest.main()