# ------------------------------------------------------------
# Lexer para C++
# ------------------------------------------------------------

import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'digito',
    'mas',
    'menos',
    'por',
    'entre',
    'parenIzq',
    'parenDer',
    'palaraClave',
    'identificador',
    'inicioBloque',
    'finBloque',
    'finInstruccion',
    'asignacion',
    'comentario',
    'comentarioBloque',
    'cadena',
    'coma'
)

# Regular expression rules for simple tokens
t_mas = r'\+'
t_menos = r'-'
t_por = r'\*'
t_entre = r'/'
t_parenIzq = r'\('
t_parenDer = r'\)'
t_inicioBloque = r'\{'
t_finBloque = r'\}'
t_finInstruccion = r'\;'
t_asignacion = r'\='
t_coma = r'\,'

# A regular expression rule with some action code

def t_digito(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

def t_palaraClave(t):
    r'(int)|(float)|(char)|(return)|(if)|(else)|(do)|(while)|(for)|(void)'
    return t

def t_identificador(t):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*'
    return t

def t_cadena(t):
    r'\".*\"'
    return t

#comentarios del lenguaje son ignorados

def t_comentario(t):
    r'\/\/.*'
    #return t

def t_comentarioBloque(t):
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
    f = open('fuente.cpp', 'r')
    # lexer.input('3+4*_a23+-20*2')
    lexer.input(f.read())
    while True:
        tok = lexer.token()
        if not tok:
            break
        print("[Tipo:", tok.type, "]", "[Valor:", tok.value, "]","[Número de Línea:", tok.lineno, "]", "[Posición:", tok.lexpos, "]")
        # .lineno is Current line number
        # .lexpos is Current position in input text

miLexer()