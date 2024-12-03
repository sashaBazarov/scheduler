import unittest
from unittest.mock import patch, MagicMock
from process_command import *
from exceptions.commandexception import CommandException


class TestProcessCommand(unittest.TestCase):

    @patch("process_command.execute.load_command")
    @patch("process_command.execute.parse_tokens")
    def test_process_command_success(self, mock_parse_tokens, mock_load_command):
        # Mock parsed tokens
        mock_parse_tokens.return_value = {
            "command": "test_command",
            "args": ["arg1", "arg2"],
            "kwargs": {"key1": "value1"}
        }

        # Mock the loaded command to be a callable
        mock_command = MagicMock()
        mock_load_command.return_value = mock_command

        # Call the execute function
        execute("test_command arg1 arg2 key1=value1")

        # Assertions
        mock_parse_tokens.assert_called_once_with(
            "test_command arg1 arg2 key1=value1")
        mock_load_command.assert_called_once_with("test_command")
        mock_command.assert_called_once_with("arg1", "arg2", key1="value1")

    @patch("process_command.execute.load_command")
    @patch("process_command.execute.parse_tokens")
    def test_process_command_invalid_command(self, mock_parse_tokens, mock_load_command):
        # Mock data
        mock_parse_tokens.return_value = {
            "command": "invalid_command",
            "args": [],
            "kwargs": {}
        }
        mock_load_command.return_value = None

        # Execute and assert exception
        with self.assertRaises(CommandException) as context:
            execute("invalid_command")

        exception = context.exception
        self.assertEqual(exception.message, "Invalid command input")
        self.assertEqual(exception.command, "invalid_command")
        self.assertEqual(exception.args, ())
        self.assertEqual(exception.kwargs, {})
        mock_parse_tokens.assert_called_once_with("invalid_command")
        mock_load_command.assert_called_once_with("invalid_command")

    @patch("process_command.execute.load_command")
    @patch("process_command.execute.parse_tokens")
    def test_process_command_execution_error(self, mock_parse_tokens, mock_load_command):
        # Mock data
        mock_parse_tokens.return_value = {
            "command": "test_command",
            "args": [],
            "kwargs": {}
        }
        mock_command = MagicMock()
        mock_command.side_effect = Exception("Execution error")
        mock_load_command.return_value = mock_command

        # Execute and assert exception
        with self.assertRaises(Exception) as context:
            execute("test_command")

        self.assertEqual(str(context.exception), "Execution error")
        mock_parse_tokens.assert_called_once_with("test_command")
        mock_load_command.assert_called_once_with("test_command")
        mock_command.assert_called_once()


if __name__ == '__main__':
    unittest.main()
