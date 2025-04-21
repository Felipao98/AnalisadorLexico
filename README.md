# Analisador Léxico em Python
  Este projeto é um analisador léxico simples escrito em Python, projetado para dividir uma entrada de código-fonte em tokens léxicos, como identificadores, números inteiros, operadores e pontuações básicas.

# Funcionalidades
  - Reconhece identificadores (variáveis, x, total, etc.).
  - Reconhece números inteiros (123, 42, etc.).
  - Suporte a operadores básicos (+, -, *, /, =).
  - Identifica parêntes e ponto e vírgula.
  - Ignora espaços e quebra de linha.
  - Gera erro para tokens inválidos (não reconhecidos).
  
# Atalhos
  - A estrutura " (?P<TOKEN>padrão) " nomeia cada expressão regular, facilitando a identificação do tipo de token capturado.
  - O uso de " token_specification " como lista de tuplas torna fácil a adição e manutenção de novos tokens.
  - A função " re.finditer() " percorre a entrada buscando todos os tokens de forma contínua e eficiente.
  - Tokens como espaços e quebras de linhas são ignorados diretamente dentro do loop, simplificando o fluxo de análise.

# Especificações
  - Linguagem: Python
  - Bibliotecas: re (expressões regulares)
  - Tokens suportados:
      - ID -> identificadores
      - NUM -> números inteiros
      - OP -> operadores matemáticos e de atribuição
      - LPAREN, RPAREN -> parênteses
      - SEMI -> ponto e vírgula
  - Saída: lista de tuplas (tipo, valor)

# Limitações
  - Não reconhece números decimais (EX: 3.14, causa erro).
  - Palavras-chave (if, else, while) são tratados como identificadores comuns.
  - Não há suporte para strings, comentários, caracteres especiais, nem operadores compostos (>=, ==, etc.),
  - O analisador é apenas léxico, não possui análise sintática ou semântica.
  - A entrada precisa estar em formato texto simples, lida diretamente como string ou com pequena adaptação para ler arquivos.
