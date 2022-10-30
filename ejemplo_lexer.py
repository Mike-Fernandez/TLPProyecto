# ------------------------------------------------------------
# Lexer para C++
# ------------------------------------------------------------

#El analizador léxico es la primera fase de un compilador. Su principal función consiste en leer los caracteres de entrada y elaborar como salida una secuencia de componentes léxicos que utiliza el analizador sintáctico para hacer el análisis.

import ply.lex as lex
from bstInorder import *

# List of token names.   This is always required
tokens = (
    'digito',
    'mas',
    'menos',
    'por',
    'entre',
    'parenIzq',
    'parenDer',
    'palabraReservada',
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

def t_palabraReservada(t):
    #10 palabras, máximo 15, agregue 4 palabras mas, esta abierto a modificación
    r'(const)|(struct)|(long)|(double)|(int)|(float)|(char)|(return)|(if)|(else)|(do)|(while)|(for)|(void)'
    return t

def t_identificador(t):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*'
    return t

def t_cadena(t):
    r'\".*\"'
    return t

#comentarios del lenguaje son ignorados/omitidos

def t_comentario(t):
    r'\/\/.*'
    #return t

def t_comentarioBloque(t):
    r'\/\*(.|\n)*\*\/'
    #return t

# Error handling rule

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    # en el caso que se detecten elementos no pertenecientes
    # al lenguaje, indicamos un error y omitimos el elemento.
    t.lexer.skip(1)
    return t

# Build the lexer
lexer = lex.lex()

#ejemplo del lexer en funcionamiento
def miLexer():
    #creando un contador
    contador = 0
    #declarando un arbol BST
    #creando nodo root
    root = None
    f = open('fuente.cpp', 'r')
    # lexer.input('3+4*_a23+-20*2')
    lexer.input(f.read())
    while True:
        tok = lexer.token()
        if not tok:
            break
        # mostrar la lista de elementos lexicográficos encontrados
        print("[Tipo:", tok.type, "]", "[Valor:", tok.value, "]","[Número de Línea:", tok.lineno, "]", "[Posición en texto:", tok.lexpos, "]")
        # aqui se deberia ir almacenando en cada paso del while
        # un token en un BST, el cual imprimiremos al final.
        # .lineno is Current line number
        # .lexpos is Current position in input text
        if root is None:
            root = Node(tokenInfo(contador,tok.type,tok.value,tok.lineno,tok.lexpos))
        else:
            insert(root, tokenInfo(contador,tok.type,tok.value,tok.lineno,tok.lexpos))
        contador += 1
    #tabla de simbolos imprimir
    print("******** Imprimiendo tabla de simbolos ********")
    printPreorder(root)

print("******** Ejecutando mi lexer ********")
miLexer()

# TODO tabla de símbolos construida 
