from .parse_tokens import parse_command
from .commands import load_command
from exceptions import CommandException

def execute(string: str):   
    """
    Разбирает строку команды, загружает соответствующую командную функцию и выполняет ее с предоставленными аргументами.

    Аргументы:
        string (str): Строка команды для разбора и выполнения.

    Исключения:
        CommandException: Если команда недействительна или не может быть загружена.
    Возвращает:
        None
    """
    
    command = parse_command(string)
    command.execute()
