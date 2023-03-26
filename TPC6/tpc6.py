import ply.lex as lex

# Define the reserved keywords
reserved = {
    'int': 'INT',
    'function': 'FUNCTION',
    'while': 'WHILE',
    'for': 'FOR',
    'in': 'IN',
    'program': 'PROGRAM',
    'print': 'PRINT'
}

# Define the token names
tokens = [
    'ID', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'COMMA', 'SEMI',
    'LT', 'GT', 'EQ', 'LE', 'GE', 'NE', 'LBRACKET', 'RBRACKET'
] + list(reserved.values())

# Define regular expressions for simple tokens
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMI = r';'
t_LT = r'<'
t_GT = r'>'
t_EQ = r'='
t_LE = r'<='
t_GE = r'>='
t_NE = r'!='

# Define regular expressions for more complex tokens
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule to ignore whitespace and comments
def t_ignore_WHITESPACE(t):
    r'\s+'
    pass

def t_ignore_COMMENT(t):
    r'\/\/.*'
    pass

# Define a rule to handle errors
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

program_string = """
int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
"""

lexer.input(program_string)
for tok in lexer:
    print(tok)
