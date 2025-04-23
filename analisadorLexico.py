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

testes = [
    ("x = 42 + y1 * (z2 - 3);", "Expressão válida com identificadores e operadores"),
    ("int x = 42 + y1 * (z2 - 3);", "Palavra-chave 'int' como identificador"),
    ("float def = 42;", "Palavra-chave 'float' e 'def' como identificadores"),
    ("3.14", "Número decimal (não suportado)"),
    ("#", "Comentário inválido (erro esperado)"),
    ("@#$%", "Caracteres especiais (erro esperado)"),
    ("x >= 3", "Operador composto (não suportado)")
]

for codigo, descricao in testes:
    print(f"\n🧪 Teste: {descricao}")
    print(f"Entrada: {codigo}")
    try:
        resultado = lexer(codigo)
        print("Saída (tokens):")
        for token in resultado:
            print("  ", token)
    except RuntimeError as e:
        print("Erro:", e)
