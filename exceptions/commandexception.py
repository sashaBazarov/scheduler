class CommandException(Exception):
    """
    Исключение, возникающее при ошибках выполнения команды.
    Атрибуты:
        message (str): Объяснение ошибки.
        command (str): Команда, вызвавшая ошибку.
        args (tuple): Дополнительные позиционные аргументы.
        kwargs (dict): Дополнительные именованные аргументы.
    Методы:
        __str__(): Возвращает строковое представление CommandException.
    """
    def __init__(self, message: str, command: str, *args, **kwargs) -> None:
        self.message = message
        self.command = command
        self.args = args
        self.kwargs = kwargs
        super().__init__(*args)

    def __str__(self) -> str:
  
        return f"CommandException: {self.message} (Command: {self.command}, Arguments: {self.args} {self.kwargs})"
