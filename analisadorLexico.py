import re

# Definições dos padrões de tokens
token_specification = [
    ('NUM',     r'\d+'),                 # Número inteiro
    ('ID',      r'[A-Za-z_]\w*'),        # Identificadores
    ('OP',      r'[+\-*/=]'),            # Operadores
    ('LPAREN',  r'\('),                  # Parêntese esquerdo
    ('RPAREN',  r'\)'),                  # Parêntese direito
    ('SEMI',    r';'),                   # Ponto e vírgula
    ('SKIP',    r'[ \t]+'),              # Espaços/tabs
    ('NEWLINE', r'\n'),                  # Nova linha
    ('MISMATCH',r'.'),                   # Qualquer outro caractere (erro)
]

# Compila o padrão regex
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

# Teste
codigo = "x = 42 + y1 * (z2 - 3);"
resultado = lexer(codigo)

# Exibir tokens
for token in resultado:
    print(token)
