#Analizador Lexico para lenguaje c++

# Integrantes
#   Miguel Enrique Fernández Azucena 00145518
#   Julio Alfredo Machado Olivo 00039718
#   Saúl Ernesto Orellana Jiménez 00180718
#   Nuria Melissa Rivas Canjura 00041517
#   Miguel Ernesto Rivas Serrano 00087518

import ply.lex as lex
from bstInorder import *

# Tokens a utilizar
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
    'coma',
    'gt',
    'lt',
    'ge',
    'le',
    'num'
)

# Tokens descritos en su version de expresion regular
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
t_gt = r'\>'
t_lt = r'\<'
t_ge = r'\>\='
t_le = r'\<\='
t_num = r'\#'

# Define el token de un digito con su valor

def t_digito(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Para leer el número de línea

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Permite ignorar espacios y tabs en el codigo
t_ignore = ' \t'

# Token para palabras reservadas especificas a c++
def t_palabraReservada(t):
    #Utilizado el maximo de 15 palabras, aunque siguen sin ser s
    r'(const)|(struct)|(long)|(double)|(int)|(float)|(char)|(return)|(if)|(else)|(do)|(while)|(for)|(void)|(include)'
    return t

# Token para los identificadores, deben de iniciar con una letra mayuscula o minuscula o un guión bajo
def t_identificador(t):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*'
    return t

# Token de una cadena string
def t_cadena(t):
    r'\".*\"'
    return t

#Ignoramos comentarios al no regresar el token en cuestion
# Permite ignorar los comentarios del lenguaje
def t_comentario(t):
    r'\/\/.*'
    #return t

# Para comentarios de bloque
def t_comentarioBloque(t):
    r'\/\*(.|\n)*\*\/'
    #return t

# Manejo de errores
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    return t

# Buildeando el lexer
lexer = lex.lex()

# Funcion para echar el lexer en funcionamiento
def miLexer():
    contador = 0
    #declarando un arbol BST
    #creando nodo root
    root = None
    f = open('fuente.cpp', 'r')
    lexer.input(f.read())
    while True:
        tok = lexer.token()
        if not tok:
            break
        # mostrar la lista de elementos lexicográficos encontrados
        print("[Tipo:", tok.type, "]", "[Valor:", tok.value, "]","[Número de Línea:", tok.lineno, "]", "[Posición en texto:", tok.lexpos, "]")
        # aqui se almacena en cada paso del while
        # un token en un BST, el cual imprimiremos al final.
        if root is None:
            root = Node(tokenInfo(contador,tok.type,tok.value,tok.lineno,tok.lexpos))
        else:
            root = insert(root, tokenInfo(contador,tok.type,tok.value,tok.lineno,tok.lexpos))
        contador += 1
    #tabla de simbolos imprimir
    print("******** Imprimiendo tabla de simbolos ********")
    printInorder(root)

print("******** Ejecutando mi lexer ********")
miLexer()
