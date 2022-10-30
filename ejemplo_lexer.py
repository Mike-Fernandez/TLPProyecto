# ------------------------------------------------------------
# Lexer para C++
# ------------------------------------------------------------

import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'keyword',
   'identificador',
   'inicioBloque',
   'finBloque',
   'finInstruccion',
   'asignacion',
   'comentario',
   'comentario_bloque',
   'cadena',
   'coma'
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_inicioBloque = r'\{'
t_finBloque = r'\}'
t_finInstruccion = r'\;'
t_asignacion = r'\='
t_coma= r'\,'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_keyword(t):
    r'(int)|(float)|(char)|(return)|(if)|(else)|(do)|(while)|(for)|(void)'
    return t

def t_identificador(t):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*'
    return t

def t_cadena(t):
    r'\".*\"'
    return t

def t_comentario(t):
    r'\/\/.*'
    return t

def t_comentario_bloque(t):
    r'\/\*(.|\n)*\*\/'
    #return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)    
    return t

# Build the lexer
lexer = lex.lex()

def miLexer():
    f = open('fuente.c','r')
    #lexer.input('3+4*_a23+-20*2')
    lexer.input(f.read())
    while True:
        tok=lexer.token()
        if not tok:
            break
        #print(tok)
        print(tok.type, tok.value, tok.lineno, tok.lexpos)
        # .lineno is Current line number
        # .lexpos is Current position in input text
        
miLexer()