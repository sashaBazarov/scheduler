class CommandException(Exception):
    def __init__(self, message: str, command: str, *args, **kwargs) -> None:
        self.message = message
        self.command = command
        self.args = args
        self.kwargs = kwargs
        super().__init__(*args)

    def __str__(self) -> str:
  
        return f"CommandException: {self.message} (Command: {self.command}, Arguments: {self.args} {self.kwargs})"
