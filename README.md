# 🧠 Analisador Léxico em Python

Este projeto é um analisador léxico simples escrito em Python, projetado para dividir uma entrada de código-fonte em **tokens léxicos**, como identificadores, números inteiros, operadores e pontuações básicas.

---

## ✅ Funcionalidades

- Reconhece identificadores (`variáveis`, `x`, `total`, etc.).
- Reconhece números inteiros (`123`, `42`, etc.).
- Suporte a operadores básicos (`+`, `-`, `*`, `/`, `=`).
- Identifica parênteses e ponto e vírgula.
- Ignora espaços e quebras de linha.
- Gera erro para tokens inválidos (não reconhecidos).

---

## ⚡ Atalhos

- A estrutura `(?P<TOKEN>padrão)` nomeia cada expressão regular, facilitando a identificação do tipo de token capturado.
- O uso de `token_specification` como lista de tuplas torna fácil a adição e manutenção de novos tokens.
- A função `re.finditer()` percorre a entrada buscando todos os tokens de forma contínua e eficiente.
- Tokens como espaços e quebras de linhas são ignorados diretamente dentro do loop, simplificando o fluxo de análise.

---

## 📐 Especificações

- **Linguagem:** Python
- **Bibliotecas:** `re` (expressões regulares)
- **Tokens suportados:**
  - `ID` → identificadores
  - `NUM` → números inteiros
  - `OP` → operadores matemáticos e de atribuição
  - `LPAREN`, `RPAREN` → parênteses
  - `SEMI` → ponto e vírgula
- **Saída:** lista de tuplas `(tipo, valor)`

---

## 🚫 Limitações

- Não reconhece números decimais (ex: `3.14` causa erro).
- Palavras-chave (`if`, `else`, `while`) são tratadas como identificadores comuns.
- Não há suporte para:
  - Strings
  - Comentários
  - Caracteres especiais
  - Operadores compostos (`>=`, `==`, etc.)
- O analisador é **apenas léxico**, não possui análise sintática ou semântica.
- A entrada precisa estar em **formato texto simples**, lida diretamente como `string` ou com pequena adaptação para leitura de arquivos.

---

# 📘 Analisador Sintático LL(1)

Este projeto também inclui um **analisador sintático** baseado em **gramática LL(1)** que utiliza a saída do analisador léxico para validar estruturas sintáticas de uma linguagem simples.

---

## 🔧 Funcionalidades

- Recebe como entrada a lista de tokens do analisador léxico.
- Permite definir sua própria **gramática** com produções e regras.
- Calcula automaticamente os conjuntos `FIRST` e `FOLLOW`.
- Gera e exibe a **tabela preditiva (tabela M)** para análise LL(1).
- Informa os passos para transformar a gramática para forma LL(1), se necessário.
- Pode ser expandido para reconhecer várias sentenças a partir da gramática fornecida.

---

## 💡 Exemplo de uso

```python
from lexer import lexer
from parser_ll1 import ParserGenerator

tokens = lexer("x = 3 + y * (2 - z);")

grammar = {
    'S': [['ID', 'OP', 'E', 'SEMI']],
    'E': [['T', 'E_']],
    'E_': [['OP', 'T', 'E_'], ['ε']],
    'T': [['F', 'T_']],
    'T_': [['OP', 'F', 'T_'], ['ε']],
    'F': [['NUM'], ['ID'], ['LPAREN', 'E', 'RPAREN']]
}

pg = ParserGenerator(grammar, start_symbol='S')
pg.print_first_follow()
pg.print_parse_table()
