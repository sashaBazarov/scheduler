import unittest
from unittest.mock import patch, MagicMock
from commands.view_tasks import view_tasks
from task import Task

class TestViewTasks(unittest.TestCase):

    @patch('commands.view_tasks.load_tasks')
    @patch('commands.view_tasks.filter_tasks')
    @patch('commands.view_tasks.tabulate')
    def test_view_tasks(self, mock_tabulate, mock_filter_tasks, mock_load_tasks):

        task1 = MagicMock(spec=Task)
        task1.to_list.return_value = ["Task 1", "Description 1", "Work", "2023-10-01", "High", "Pending", 1]
        task2 = MagicMock(spec=Task)
        task2.to_list.return_value = ["Task 2", "Description 2", "Home", "2023-10-02", "Low", "Completed", 2]

        mock_load_tasks.return_value = [task1, task2]
        mock_filter_tasks.return_value = [task1]
        mock_tabulate.return_value = "Mocked Table"

        with patch('builtins.print') as mock_print:
            view_tasks(category="Work", status="Pending")

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


if __name__ == '__main__':
    unittest.main()
