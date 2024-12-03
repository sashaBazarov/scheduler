import re

def parse_tokens(string: str):

    tokens = re.findall(r"<.*?>|\b\w+\b|\".*?\"|[.,!?;:(){}[\]=+\-*/<>]", string)
    tokens = [token.strip('"') for token in tokens]  

    command = tokens.pop(0)
    
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
    
    return {
        "command": command,
        "args": args,
        "kwargs": kwargs
    }


