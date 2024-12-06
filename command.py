from typing import Callable, Any


class Command:
    def __init__(self, command: Callable[..., Any],  args, kwargs) -> None:
        self.command: Callable[..., Any] = command
        self.args = args
        self.kwargs = kwargs

    def execute(self):
        self.command(*self.args, **self.kwargs)
        