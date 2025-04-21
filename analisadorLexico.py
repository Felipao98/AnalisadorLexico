import re

token_specification = [
    ('NUM',     r'\d+'),                 
    ('ID',      r'[A-Za-z_]\w*'),        
    ('OP',      r'[+\-*/=]'),            
    ('LPAREN',  r'\('),                  
    ('RPAREN',  r'\)'),                  
    ('SEMI',    r';'),                   
    ('SKIP',    r'[ \t]+'),              
    ('NEWLINE', r'\n'),                  
    ('MISMATCH',r'.'),                   
]

token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

def lexer(code):
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'NUM':
            value = int(value)
        elif kind == 'SKIP' or kind == 'NEWLINE':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Token inválido: {value}')
        tokens.append((kind, value))
    return tokens

codigo = "x = 42 + y1 * (z2 - 3);"
resultado = lexer(codigo)

for token in resultado:
    print(token)
