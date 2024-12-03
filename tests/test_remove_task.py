import unittest
from unittest.mock import patch, MagicMock
from commands.remove_task import remove_task


class TestRemoveTask(unittest.TestCase):

    @patch("commands.remove_task.delete_task")
    @patch("commands.remove_task.find_task")
    def test_remove_task_success(self, mock_find_task, mock_delete_task):
        # Mock the task to be found
        mock_task = MagicMock()
        mock_task.id = "123"
        mock_find_task.return_value = mock_task

        with patch("builtins.print") as mock_print:
            # Call remove_task
            remove_task("123")

            # Assertions
            mock_find_task.assert_called_once_with("123")
            mock_delete_task.assert_called_once_with(mock_task)
            mock_print.assert_called_once_with("Task with id 123 has been deleted.")

    @patch("commands.remove_task.find_task")
    def test_remove_task_not_found(self, mock_find_task):
        # Mock task not found
        mock_find_task.return_value = None

        # Call remove_task and assert it raises ValueError
        with self.assertRaises(ValueError) as context:
            remove_task("123")

        self.assertEqual(str(context.exception), "Task with id 123 not found.")
        mock_find_task.assert_called_once_with("123")


if __name__ == '__main__':
    unittest.main()
