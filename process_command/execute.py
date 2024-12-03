from .parse_tokens import parse_tokens
from .commands import load_command
from exceptions import CommandException

def execute(string: str):
    tokens = parse_tokens(string)
    command = tokens["command"]
    args = tokens["args"]
    kwargs = tokens["kwargs"]

    loaded_command = load_command(command)

    if not loaded_command:
        raise CommandException("Invalid command input", command, *args, **kwargs)
    
    loaded_command(*args, **kwargs)
