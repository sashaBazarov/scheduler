import re
from command import Command
from .commands import load_command

def parse_command(string: str):
    """
    Разбирает данную строку на команду, аргументы и именованные аргументы.
    Функция токенизирует входную строку и выделяет первый токен как команду.
    Затем она обрабатывает оставшиеся токены для идентификации аргументов и именованных аргументов.
    Аргументы:
        string (str): Входная строка для разбора.
    Возвращает:
        dict: Словарь, содержащий:
            - "command" (str): Первый токен, определенный как команда.
            - "args" (list): Список аргументов.
            - "kwargs" (dict): Словарь именованных аргументов.
    """
    tokens = re.findall(r"<.*?>|\b\w+\b|\".*?\"|=", string)
    tokens = [token.strip('"') for token in tokens]  

    command_name = tokens.pop(0)
    command = load_command(command_name)

    if not command:
        raise ValueError(f"Command '{command_name}' not found.")
    
    kwargs = {}
    args = []
    i = 0

    while i < len(tokens):
        if i + 2 < len(tokens) and tokens[i + 1] == '=':
            key = tokens[i]
            value = tokens[i + 2]
            kwargs[key] = value
            i += 3 
        else:
            args.append(tokens[i])
            i += 1
    
    return Command(command, args, kwargs)
