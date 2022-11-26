# ------------------------------------------------------------
# Parser para subset de C
# ------------------------------------------------------------
import ply.lex as lex
from bstInorder import *

#Non-terminal symbols from grammar
Start=0
callF=1
comment=2
declare=3
branch=4
params=5
var_params=6
eq=7
cm=8
var_fin=9
tipo=10
var=11
eol=12
stmt=13
returnStmt=14
expStmt=15
var_stmt=16
ifStmt=17
els=18
iterStmt=19
op=20
expr=21
expr_tail=22
ASimpleExp=23
simpleExp=24

# List of token names
tokens = (
    'digito',
    'mas',#• Cuatro operadores aritméticos y tres operados lógicos
    'menos',
    'por',
    'entre',
    'parenIzq',
    'parenDer',
    'palabraReservada',# Tipos de datos: int, char, float. | Palabras claves o reservadas: char, int, float, return, void, if, else
    'identificador',#Utilización de variables
    'inicioBloque',
    'finBloque',
    'finInstruccion',
    'asignacion',
    'comentarioL',#Manejo de comentarios 
    'comentarioB',#Manejo de comentarios 
    'cadena',
    'coma',
    'gt',#• Cuatro operadores aritméticos y tres operados lógicos
    'lt',
    'ge',
    'le',
    'tInt',
    'tChar',
    'tFloat',
    'tVoid',
    'tLong',
    'tDouble',
    'numeral',
    'text',
    'tOR',
    'tAND',
    'tNOT',
    'tTRUE',
    'tFALSE',
    'tReturn',
    'tIf',
    'tElse',
    'tWhile',
    'tDo',
    'tFor',
    'doubleEq',
    'vacia',
    'eof'
)

# Regular expression rules for simple tokens
t_mas = r'\+'#• Cuatro operadores aritméticos y tres operados lógicos
t_menos = r'-'
t_por = r'\*'
t_entre = r'/'
t_parenIzq = r'\('
t_parenDer = r'\)'
t_inicioBloque = r'\{'
t_finBloque = r'\}'
t_finInstruccion = r'\;'
t_asignacion = r'\='
t_doubleEq = r'\=\='
t_tOR = r'\|\|'
t_tAND = r'\&\&'
t_tNOT = r'\!'
t_coma = r'\,'
t_gt = r'\>'#• Cuatro operadores aritméticos y tres operados lógicos
t_lt = r'\<'
t_ge = r'\>\='
t_le = r'\<\='
t_numeral = r'\#'
t_vacia = r'\'\''
t_eof = r'\$'

def t_digito(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Permite ignorar espacios y tabs en el codigo
t_ignore = ' \t'

def t_tInt(t):
    r'(int)'
    return t

def t_tChar(t):
    r'(char)'
    return t

def t_tFloat(t):
    r'(float)'
    return t

def t_tVoid(t):
    r'(void)'
    return t

def t_tLong(t):
    r'(long)'
    return t

def t_tDouble(t):
    r'(double)'
    return t

def t_tTRUE(t):
    r'(TRUE)'
    return t

def t_tFALSE(t):
    r'(FALSE)'
    return t

def t_tReturn(t):
    r'(return)'
    return t

def t_tIf(t):
    r'(if)'
    return t

def t_tElse(t):
    r'(else)'
    return t

def t_tWhile(t):
    r'(while)'
    return t

def t_tDo(t):
    r'(do)'
    return t

def t_tFor(t):
    r'(for)'
    return t

# Token para los identificadores, deben de iniciar con una letra mayuscula o minuscula o un guión bajo
#Utilización de variables
def t_identificador(t):
    r'([a-z]|[A-Z]|_)([a-z]|[A-Z]|\d|_)*'
    return t

# Token de una cadena string
def t_cadena(t):
    r'\".*\"'
    return t

#Ignoramos comentarios al no regresar el token en cuestion
# Permite ignorar los comentarios del lenguaje
# Manejo de comentarios 
def t_comentarioL(t):
    r'\/\/.*'
    return t

# Para comentarios de bloque
# Manejo de comentarios 
def t_comentarioB(t):
    r'\/\*(.|\n)*\*\/'
    return t

# Manejo de errores
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    return t

def t_text(t):
    r'\'([a-z]|[A-Z]|)+\''
    return t

#Tabla correspondiente a gramatica hecha
tabla2 = [ [Start, 'parenIzq', None ],
        [Start, 'parenDer', None ],
        [Start, 'comentarioL', [comment,Start] ],
        [Start, 'comentarioB', [comment,Start] ],
        [Start, 'inicioBloque', None],
        [Start, 'finBloque', None],
        [Start, 'asignacion', None],
        [Start, 'coma', None],
        [Start, 'text', None],
        [Start, 'digito', None],
        [Start, 'tInt', [declare] ],
        [Start, 'tChar', [declare] ],
        [Start, 'tFloat', [declare] ],
        [Start, 'tVoid', [declare] ],
        [Start, 'tLong', [declare] ],
        [Start, 'tDouble', [declare] ],
        [Start, 'identificador', [declare]],
        [Start, 'finInstruccion', None],
        [Start, 'tReturn', None],
        [Start, 'tIf', None],
        [Start, 'tElse', None],
        [Start, 'tWhile', None],
        [Start, 'tDo', None],
        [Start, 'tFor', None],
        [Start, 'lt', None],
        [Start, 'le', None],
        [Start, 'gt', None],
        [Start, 'ge', None],
        [Start, 'doubleEq', None],
        [Start, 'tOR', None],
        [Start, 'tAND', None],
        [Start, 'mas', None],
        [Start, 'menos', None],
        [Start, 'por', None],
        [Start, 'entre', None],
        [Start, 'tTRUE', None],
        [Start, 'tFALSE', None],
        [Start, 'tNOT', None],
        [Start, 'eof', None],
        [callF, 'parenIzq', ['parenIzq',params,'parenDer'] ],
        [callF, 'parenDer', None ],
        [callF, 'comentarioL', None ],
        [callF, 'comentarioB', None ],
        [callF, 'inicioBloque', None],
        [callF, 'finBloque', None],
        [callF, 'asignacion', None],
        [callF, 'coma', None],
        [callF, 'text', None],
        [callF, 'digito', None],
        [callF, 'tInt', None],
        [callF, 'tChar', None],
        [callF, 'tFloat', None],
        [callF, 'tVoid', None],
        [callF, 'tLong', None],
        [callF, 'tDouble', None],
        [callF, 'identificador', None],
        [callF, 'finInstruccion', None],
        [callF, 'tReturn', None],
        [callF, 'tIf', None],
        [callF, 'tElse', None],
        [callF, 'tWhile', None],
        [callF, 'tDo', None],
        [callF, 'tFor', None],
        [callF, 'lt', None],
        [callF, 'le', None],
        [callF, 'gt', None],
        [callF, 'ge', None],
        [callF, 'doubleEq', None],
        [callF, 'tOR', None],
        [callF, 'tAND', None],
        [callF, 'mas', None],
        [callF, 'menos', None],
        [callF, 'por', None],
        [callF, 'entre', None],
        [callF, 'tTRUE', None],
        [callF, 'tFALSE', None],
        [callF, 'tNOT', None],
        [callF, 'eof', None],
        [comment, 'parenIzq', None ],
        [comment, 'parenDer', None ],
        [comment, 'comentarioL', ['comentarioL'] ],
        [comment, 'comentarioB', ['comentarioB'] ],
        [comment, 'inicioBloque', None],
        [comment, 'finBloque', None],
        [comment, 'asignacion', None],
        [comment, 'coma', None],
        [comment, 'text', None],
        [comment, 'digito', None],
        [comment, 'tInt', None],
        [comment, 'tChar', None],
        [comment, 'tFloat', None],
        [comment, 'tVoid', None],
        [comment, 'tLong', None],
        [comment, 'tDouble', None],
        [comment, 'identificador', None],
        [comment, 'finInstruccion', None],
        [comment, 'tReturn', None],
        [comment, 'tIf', None],
        [comment, 'tElse', None],
        [comment, 'tWhile', None],
        [comment, 'tDo', None],
        [comment, 'tFor', None],
        [comment, 'lt', None],
        [comment, 'le', None],
        [comment, 'gt', None],
        [comment, 'ge', None],
        [comment, 'doubleEq', None],
        [comment, 'tOR', None],
        [comment, 'tAND', None],
        [comment, 'mas', None],
        [comment, 'menos', None],
        [comment, 'por', None],
        [comment, 'entre', None],
        [comment, 'tTRUE', None],
        [comment, 'tFALSE', None],
        [comment, 'tNOT', None],
        [comment, 'eof', None],
        [declare, 'parenIzq', None ],
        [declare, 'parenDer', None ],
        [declare, 'comentarioL', None ],
        [declare, 'comentarioB', None ],
        [declare, 'inicioBloque', None],
        [declare, 'finBloque', None],
        [declare, 'asignacion', None],
        [declare, 'coma', None],
        [declare, 'text', None],
        [declare, 'digito', None],
        [declare, 'tInt', [tipo,var,branch]],
        [declare, 'tChar', [tipo,var,branch]],
        [declare, 'tFloat', [tipo,var,branch]],
        [declare, 'tVoid', [tipo,var,branch]],
        [declare, 'tLong', [tipo,var,branch]],
        [declare, 'tDouble', [tipo,var,branch]],
        [declare, 'identificador', [var,'parenIzq',params,'parenDer',eol]],
        [declare, 'finInstruccion', None],
        [declare, 'tReturn', None],
        [declare, 'tIf', None],
        [declare, 'tElse', None],
        [declare, 'tWhile', None],
        [declare, 'tDo', None],
        [declare, 'tFor', None],
        [declare, 'lt', None],
        [declare, 'le', None],
        [declare, 'gt', None],
        [declare, 'ge', None],
        [declare, 'doubleEq', None],
        [declare, 'tOR', None],
        [declare, 'tAND', None],
        [declare, 'mas', None],
        [declare, 'menos', None],
        [declare, 'por', None],
        [declare, 'entre', None],
        [declare, 'tTRUE', None],
        [declare, 'tFALSE', None],
        [declare, 'tNOT', None],
        [declare, 'eof', None],
        [branch, 'parenIzq', ['parenIzq',params,'parenDer','inicioBloque',stmt,'finBloque'] ],
        [branch, 'parenDer', None ],
        [branch, 'comentarioL', None ],
        [branch, 'comentarioB', None ],
        [branch, 'inicioBloque', None],
        [branch, 'finBloque', None],
        [branch, 'asignacion', [eq,var_fin,eol]],
        [branch, 'coma', [eq,var_fin,eol]],
        [branch, 'text', None],
        [branch, 'digito', None],
        [branch, 'tInt', None],
        [branch, 'tChar', None],
        [branch, 'tFloat', None],
        [branch, 'tVoid', None],
        [branch, 'tLong', None],
        [branch, 'tDouble', None],
        [branch, 'identificador', None],
        [branch, 'finInstruccion', None],
        [branch, 'tReturn', None],
        [branch, 'tIf', None],
        [branch, 'tElse', None],
        [branch, 'tWhile', None],
        [branch, 'tDo', None],
        [branch, 'tFor', None],
        [branch, 'lt', None],
        [branch, 'le', None],
        [branch, 'gt', None],
        [branch, 'ge', None],
        [branch, 'doubleEq', None],
        [branch, 'tOR', None],
        [branch, 'tAND', None],
        [branch, 'mas', None],
        [branch, 'menos', None],
        [branch, 'por', None],
        [branch, 'entre', None],
        [branch, 'tTRUE', None],
        [branch, 'tFALSE', None],
        [branch, 'tNOT', None],
        [branch, 'eof', None],
        [params, 'parenIzq', None ],
        [params, 'parenDer', ['vacia'] ],
        [params, 'comentarioL', None ],
        [params, 'comentarioB', None ],
        [params, 'inicioBloque', None],
        [params, 'finBloque', None],
        [params, 'asignacion', None],
        [params, 'coma', None],
        [params, 'text', None],
        [params, 'digito', None],
        [params, 'tInt', [tipo,var,cm,var_params]],
        [params, 'tChar', [tipo,var,cm,var_params]],
        [params, 'tFloat', [tipo,var,cm,var_params]],
        [params, 'tVoid', [tipo,var,cm,var_params]],
        [params, 'tLong', [tipo,var,cm,var_params]],
        [params, 'tDouble', [tipo,var,cm,var_params]],
        [params, 'identificador', None],
        [params, 'finInstruccion', None],
        [params, 'tReturn', None],
        [params, 'tIf', None],
        [params, 'tElse', None],
        [params, 'tWhile', None],
        [params, 'tDo', None],
        [params, 'tFor', None],
        [params, 'lt', None],
        [params, 'le', None],
        [params, 'gt', None],
        [params, 'ge', None],
        [params, 'doubleEq', None],
        [params, 'tOR', None],
        [params, 'tAND', None],
        [params, 'mas', None],
        [params, 'menos', None],
        [params, 'por', None],
        [params, 'entre', None],
        [params, 'tTRUE', None],
        [params, 'tFALSE', None],
        [params, 'tNOT', None],
        [params, 'eof', None],
        [var_params, 'parenIzq', None ],
        [var_params, 'parenDer', [params] ],
        [var_params, 'comentarioL', None ],
        [var_params, 'comentarioB', None ],
        [var_params, 'inicioBloque', None],
        [var_params, 'finBloque', None],
        [var_params, 'asignacion', None],
        [var_params, 'coma', None],
        [var_params, 'text', None],
        [var_params, 'digito', None],
        [var_params, 'tInt', [params]],
        [var_params, 'tChar', [params]],
        [var_params, 'tFloat', [params]],
        [var_params, 'tVoid', [params]],
        [var_params, 'tLong', [params]],
        [var_params, 'tDouble', [params]],
        [var_params, 'identificador', None],
        [var_params, 'finInstruccion', None],
        [var_params, 'tReturn', None],
        [var_params, 'tIf', None],
        [var_params, 'tElse', None],
        [var_params, 'tWhile', None],
        [var_params, 'tDo', None],
        [var_params, 'tFor', None],
        [var_params, 'lt', None],
        [var_params, 'le', None],
        [var_params, 'gt', None],
        [var_params, 'ge', None],
        [var_params, 'doubleEq', None],
        [var_params, 'tOR', None],
        [var_params, 'tAND', None],
        [var_params, 'mas', None],
        [var_params, 'menos', None],
        [var_params, 'por', None],
        [var_params, 'entre', None],
        [var_params, 'tTRUE', None],
        [var_params, 'tFALSE', None],
        [var_params, 'tNOT', None],
        [var_params, 'eof', None],
        [eq, 'parenIzq', None ],
        [eq, 'parenDer', None ],
        [eq, 'comentarioL', None ],
        [eq, 'comentarioB', None ],
        [eq, 'inicioBloque', None],
        [eq, 'finBloque', None],
        [eq, 'asignacion', ['asignacion']],
        [eq, 'coma', ['coma']],
        [eq, 'text', None],
        [eq, 'digito', None],
        [eq, 'tInt', None],
        [eq, 'tChar', None],
        [eq, 'tFloat', None],
        [eq, 'tVoid', None],
        [eq, 'tLong', None],
        [eq, 'tDouble', None],
        [eq, 'identificador', None],
        [eq, 'finInstruccion', None],
        [eq, 'tReturn', None],
        [eq, 'tIf', None],
        [eq, 'tElse', None],
        [eq, 'tWhile', None],
        [eq, 'tDo', None],
        [eq, 'tFor', None],
        [eq, 'lt', None],
        [eq, 'le', None],
        [eq, 'gt', None],
        [eq, 'ge', None],
        [eq, 'doubleEq', None],
        [eq, 'tOR', None],
        [eq, 'tAND', None],
        [eq, 'mas', None],
        [eq, 'menos', None],
        [eq, 'por', None],
        [eq, 'entre', None],
        [eq, 'tTRUE', None],
        [eq, 'tFALSE', None],
        [eq, 'tNOT', None],
        [eq, 'eof', None],
        [cm, 'parenIzq', None ],
        [cm, 'parenDer', ['vacia'] ],
        [cm, 'comentarioL', None ],
        [cm, 'comentarioB', None ],
        [cm, 'inicioBloque', None],
        [cm, 'finBloque', None],
        [cm, 'asignacion', None],
        [cm, 'coma', ['coma']],
        [cm, 'text', None],
        [cm, 'digito', None],
        [cm, 'tInt', ['vacia']],
        [cm, 'tChar', ['vacia']],
        [cm, 'tFloat', ['vacia']],
        [cm, 'tVoid', ['vacia']],
        [cm, 'tLong', ['vacia']],
        [cm, 'tDouble', ['vacia']],
        [cm, 'identificador', None],
        [cm, 'finInstruccion', None],
        [cm, 'tReturn', None],
        [cm, 'tIf', None],
        [cm, 'tElse', None],
        [cm, 'tWhile', None],
        [cm, 'tDo', None],
        [cm, 'tFor', None],
        [cm, 'lt', None],
        [cm, 'le', None],
        [cm, 'gt', None],
        [cm, 'ge', None],
        [cm, 'doubleEq', None],
        [cm, 'tOR', None],
        [cm, 'tAND', None],
        [cm, 'mas', None],
        [cm, 'menos', None],
        [cm, 'por', None],
        [cm, 'entre', None],
        [cm, 'tTRUE', None],
        [cm, 'tFALSE', None],
        [cm, 'tNOT', None],
        [cm, 'eof', None],
        [var_fin, 'parenIzq', [branch] ],
        [var_fin, 'parenDer', None ],
        [var_fin, 'comentarioL', None ],
        [var_fin, 'comentarioB', None ],
        [var_fin, 'inicioBloque', None],
        [var_fin, 'finBloque', None],
        [var_fin, 'asignacion', [branch]],
        [var_fin, 'coma', [branch]],
        [var_fin, 'text', ['text']],
        [var_fin, 'digito', ['digito']],
        [var_fin, 'tInt', None],
        [var_fin, 'tChar', None],
        [var_fin, 'tFloat', None],
        [var_fin, 'tVoid', None],
        [var_fin, 'tLong', None],
        [var_fin, 'tDouble', None],
        [var_fin, 'identificador', None],
        [var_fin, 'finInstruccion', ['vacia']],
        [var_fin, 'tReturn', None],
        [var_fin, 'tIf', None],
        [var_fin, 'tElse', None],
        [var_fin, 'tWhile', None],
        [var_fin, 'tDo', None],
        [var_fin, 'tFor', None],
        [var_fin, 'lt', None],
        [var_fin, 'le', None],
        [var_fin, 'gt', None],
        [var_fin, 'ge', None],
        [var_fin, 'doubleEq', None],
        [var_fin, 'tOR', None],
        [var_fin, 'tAND', None],
        [var_fin, 'mas', None],
        [var_fin, 'menos', None],
        [var_fin, 'por', None],
        [var_fin, 'entre', None],
        [var_fin, 'tTRUE', None],
        [var_fin, 'tFALSE', None],
        [var_fin, 'tNOT', None],
        [var_fin, 'eof', None],
        [tipo, 'parenIzq', None ],
        [tipo, 'parenDer', None ],
        [tipo, 'comentarioL', None ],
        [tipo, 'comentarioB', None ],
        [tipo, 'inicioBloque', None],
        [tipo, 'finBloque', None],
        [tipo, 'asignacion', None],
        [tipo, 'coma', None],
        [tipo, 'text', None],
        [tipo, 'digito', None],
        [tipo, 'tInt', ['tInt']],
        [tipo, 'tChar', ['tChar']],
        [tipo, 'tFloat', ['tFloat']],
        [tipo, 'tVoid', ['tFloat']],
        [tipo, 'tLong', ['tFloat']],
        [tipo, 'tDouble', ['tDouble']],
        [tipo, 'identificador', None],
        [tipo, 'finInstruccion', None],
        [tipo, 'tReturn', None],
        [tipo, 'tIf', None],
        [tipo, 'tElse', None],
        [tipo, 'tWhile', None],
        [tipo, 'tDo', None],
        [tipo, 'tFor', None],
        [tipo, 'lt', None],
        [tipo, 'le', None],
        [tipo, 'gt', None],
        [tipo, 'ge', None],
        [tipo, 'doubleEq', None],
        [tipo, 'tOR', None],
        [tipo, 'tAND', None],
        [tipo, 'mas', None],
        [tipo, 'menos', None],
        [tipo, 'por', None],
        [tipo, 'entre', None],
        [tipo, 'tTRUE', None],
        [tipo, 'tFALSE', None],
        [tipo, 'tNOT', None],
        [tipo, 'eof', None],
        [var, 'parenIzq', None ],
        [var, 'parenDer', None ],
        [var, 'comentarioL', None ],
        [var, 'comentarioB', None ],
        [var, 'inicioBloque', None],
        [var, 'finBloque', None],
        [var, 'asignacion', None],
        [var, 'coma', None],
        [var, 'text', None],
        [var, 'digito', None],
        [var, 'tInt', None],
        [var, 'tChar', None],
        [var, 'tFloat', None],
        [var, 'tVoid', None],
        [var, 'tLong', None],
        [var, 'tDouble', None],
        [var, 'identificador', ['identificador']],
        [var, 'finInstruccion', None],
        [var, 'tReturn', None],
        [var, 'tIf', None],
        [var, 'tElse', None],
        [var, 'tWhile', None],
        [var, 'tDo', None],
        [var, 'tFor', None],
        [var, 'lt', None],
        [var, 'le', None],
        [var, 'gt', None],
        [var, 'ge', None],
        [var, 'doubleEq', None],
        [var, 'tOR', None],
        [var, 'tAND', None],
        [var, 'mas', None],
        [var, 'menos', None],
        [var, 'por', None],
        [var, 'entre', None],
        [var, 'tTRUE', None],
        [var, 'tFALSE', None],
        [var, 'tNOT', None],
        [var, 'eof', None],
        [eol, 'parenIzq', None ],
        [eol, 'parenDer', None ],
        [eol, 'comentarioL', None ],
        [eol, 'comentarioB', None ],
        [eol, 'inicioBloque', None],
        [eol, 'finBloque', None],
        [eol, 'asignacion', None],
        [eol, 'coma', None],
        [eol, 'text', None],
        [eol, 'digito', None],
        [eol, 'tInt', None],
        [eol, 'tChar', None],
        [eol, 'tFloat', None],
        [eol, 'tVoid', None],
        [eol, 'tLong', None],
        [eol, 'tDouble', None],
        [eol, 'identificador', None],
        [eol, 'finInstruccion', ['finInstruccion']],
        [eol, 'tReturn', None],
        [eol, 'tIf', None],
        [eol, 'tElse', None],
        [eol, 'tWhile', None],
        [eol, 'tDo', None],
        [eol, 'tFor', None],
        [eol, 'lt', None],
        [eol, 'le', None],
        [eol, 'gt', None],
        [eol, 'ge', None],
        [eol, 'doubleEq', None],
        [eol, 'tOR', None],
        [eol, 'tAND', None],
        [eol, 'mas', None],
        [eol, 'menos', None],
        [eol, 'por', None],
        [eol, 'entre', None],
        [eol, 'tTRUE', None],
        [eol, 'tFALSE', None],
        [eol, 'tNOT', None],
        [eol, 'eof', None],
        [stmt, 'parenIzq', [expStmt,eol,stmt] ],
        [stmt, 'parenDer', None ],
        [stmt, 'comentarioL', [comment,stmt] ],
        [stmt, 'comentarioB', [comment,stmt] ],
        [stmt, 'inicioBloque', None],
        [stmt, 'finBloque', ['vacia']],
        [stmt, 'asignacion', [expStmt,eol,stmt]],
        [stmt, 'coma', None],
        [stmt, 'text', None],
        [stmt, 'digito', None],
        [stmt, 'tInt', [expStmt,eol,stmt]],
        [stmt, 'tChar', [expStmt,eol,stmt]],
        [stmt, 'tFloat', [expStmt,eol,stmt]],
        [stmt, 'tVoid', [expStmt,eol,stmt]],
        [stmt, 'tLong', [expStmt,eol,stmt]],
        [stmt, 'tDouble', [expStmt,eol,stmt]],
        [stmt, 'identificador', [var,expStmt,eol,stmt]],
        [stmt, 'finInstruccion', None],
        [stmt, 'tReturn', [returnStmt]],
        [stmt, 'tIf', [ifStmt,stmt]],
        [stmt, 'tElse', None],
        [stmt, 'tWhile', [iterStmt,stmt]],
        [stmt, 'tDo', [iterStmt,stmt]],
        [stmt, 'tFor', [iterStmt,stmt]],
        [stmt, 'lt', [expStmt,eol,stmt]],
        [stmt, 'le', [expStmt,eol,stmt]],
        [stmt, 'gt', [expStmt,eol,stmt]],
        [stmt, 'ge', [expStmt,eol,stmt]],
        [stmt, 'doubleEq', [expStmt,eol,stmt]],
        [stmt, 'tOR', [expStmt,eol,stmt]],
        [stmt, 'tAND', [expStmt,eol,stmt]],
        [stmt, 'mas', [expStmt,eol,stmt]],
        [stmt, 'menos', [expStmt,eol,stmt]],
        [stmt, 'por', [expStmt,eol,stmt]],
        [stmt, 'entre', [expStmt,eol,stmt]],
        [stmt, 'tTRUE', None],
        [stmt, 'tFALSE', None],
        [stmt, 'tNOT', None],
        [stmt, 'eof', None],
        [returnStmt, 'parenIzq', None ],
        [returnStmt, 'parenDer', None ],
        [returnStmt, 'comentarioL', None ],
        [returnStmt, 'comentarioB', None ],
        [returnStmt, 'inicioBloque', None],
        [returnStmt, 'finBloque', None],
        [returnStmt, 'asignacion', None],
        [returnStmt, 'coma', None],
        [returnStmt, 'text', None],
        [returnStmt, 'digito', None],
        [returnStmt, 'tInt', None],
        [returnStmt, 'tChar', None],
        [returnStmt, 'tFloat', None],
        [returnStmt, 'tVoid', None],
        [returnStmt, 'tLong', None],
        [returnStmt, 'tDouble', None],
        [returnStmt, 'identificador', None],
        [returnStmt, 'finInstruccion', None],
        [returnStmt, 'tReturn', ['tReturn',var_stmt,eol]],
        [returnStmt, 'tIf', None],
        [returnStmt, 'tElse', None],
        [returnStmt, 'tWhile', None],
        [returnStmt, 'tDo', None],
        [returnStmt, 'tFor', None],
        [returnStmt, 'lt', None],
        [returnStmt, 'le', None],
        [returnStmt, 'gt', None],
        [returnStmt, 'ge', None],
        [returnStmt, 'doubleEq', None],
        [returnStmt, 'tOR', None],
        [returnStmt, 'tAND', None],
        [returnStmt, 'mas', None],
        [returnStmt, 'menos', None],
        [returnStmt, 'por', None],
        [returnStmt, 'entre', None],
        [returnStmt, 'tTRUE', None],
        [returnStmt, 'tFALSE', None],
        [returnStmt, 'tNOT', None],
        [returnStmt, 'eof', None],
        [expStmt, 'parenIzq', [callF] ],
        [expStmt, 'parenDer', None ],
        [expStmt, 'comentarioL', None ],
        [expStmt, 'comentarioB', None ],
        [expStmt, 'inicioBloque', None],
        [expStmt, 'finBloque', None],
        [expStmt, 'asignacion', [op,expr]],
        [expStmt, 'coma', None],
        [expStmt, 'text', None],
        [expStmt, 'digito', None],
        [expStmt, 'tInt', [tipo,var,eq,var_stmt]],
        [expStmt, 'tChar', [tipo,var,eq,var_stmt]],
        [expStmt, 'tFloat', [tipo,var,eq,var_stmt]],
        [expStmt, 'tVoid', [tipo,var,eq,var_stmt]],
        [expStmt, 'tLong', [tipo,var,eq,var_stmt]],
        [expStmt, 'tDouble', [tipo,var,eq,var_stmt]],
        [expStmt, 'identificador', None],
        [expStmt, 'finInstruccion', None],
        [expStmt, 'tReturn', None],
        [expStmt, 'tIf', None],
        [expStmt, 'tElse', None],
        [expStmt, 'tWhile', None],
        [expStmt, 'tDo', None],
        [expStmt, 'tFor', None],
        [expStmt, 'lt', [op,expr]],
        [expStmt, 'le', [op,expr]],
        [expStmt, 'gt', [op,expr]],
        [expStmt, 'ge', [op,expr]],
        [expStmt, 'doubleEq', [op,expr]],
        [expStmt, 'tOR', [op,expr]],
        [expStmt, 'tAND', [op,expr]],
        [expStmt, 'mas', [op,expr]],
        [expStmt, 'menos', [op,expr]],
        [expStmt, 'por', [op,expr]],
        [expStmt, 'entre', [op,expr]],
        [expStmt, 'tTRUE', None],
        [expStmt, 'tFALSE', None],
        [expStmt, 'tNOT', None],
        [expStmt, 'eof', None],
        [var_stmt, 'parenIzq', [expStmt]],
        [var_stmt, 'parenDer', ['vacia'] ],
        [var_stmt, 'comentarioL', None ],
        [var_stmt, 'comentarioB', None ],
        [var_stmt, 'inicioBloque', None],
        [var_stmt, 'finBloque', None],
        [var_stmt, 'asignacion', [expStmt]],
        [var_stmt, 'coma', None],
        [var_stmt, 'text', ['text']],
        [var_stmt, 'digito', ['digito']],
        [var_stmt, 'tInt', [expStmt]],
        [var_stmt, 'tChar', [expStmt]],
        [var_stmt, 'tFloat', [expStmt]],
        [var_stmt, 'tVoid', [expStmt]],
        [var_stmt, 'tLong', [expStmt]],
        [var_stmt, 'tDouble', [expStmt]],
        [var_stmt, 'identificador', [var]],
        [var_stmt, 'finInstruccion', ['vacia']],
        [var_stmt, 'tReturn', None],
        [var_stmt, 'tIf', None],
        [var_stmt, 'tElse', None],
        [var_stmt, 'tWhile', None],
        [var_stmt, 'tDo', None],
        [var_stmt, 'tFor', None],
        [var_stmt, 'lt', [expStmt]],
        [var_stmt, 'le', [expStmt]],
        [var_stmt, 'gt', [expStmt]],
        [var_stmt, 'ge', [expStmt]],
        [var_stmt, 'doubleEq', [expStmt]],
        [var_stmt, 'tOR', [expStmt]],
        [var_stmt, 'tAND', [expStmt]],
        [var_stmt, 'mas', [expStmt]],
        [var_stmt, 'menos', [expStmt]],
        [var_stmt, 'por', [expStmt]],
        [var_stmt, 'entre', [expStmt]],
        [var_stmt, 'tTRUE', None],
        [var_stmt, 'tFALSE', None],
        [var_stmt, 'tNOT', None],
        [var_stmt, 'eof', None],
        [ifStmt, 'parenIzq', None ],
        [ifStmt, 'parenDer', None ],
        [ifStmt, 'comentarioL', None ],
        [ifStmt, 'comentarioB', None ],
        [ifStmt, 'inicioBloque', None],
        [ifStmt, 'finBloque', None],
        [ifStmt, 'asignacion', None],
        [ifStmt, 'coma', None],
        [ifStmt, 'text', None],
        [ifStmt, 'digito', None],
        [ifStmt, 'tInt', None],
        [ifStmt, 'tChar', None],
        [ifStmt, 'tFloat', None],
        [ifStmt, 'tVoid', None],
        [ifStmt, 'tLong', None],
        [ifStmt, 'tDouble', None],
        [ifStmt, 'identificador', None],
        [ifStmt, 'finInstruccion', None],
        [ifStmt, 'tReturn', None],
        [ifStmt, 'tIf', ['tIf','parenIzq',ASimpleExp,'parenDer','inicioBloque',stmt,'finBloque',els]],
        [ifStmt, 'tElse', None],
        [ifStmt, 'tWhile', None],
        [ifStmt, 'tDo', None],
        [ifStmt, 'tFor', None],
        [ifStmt, 'lt', None],
        [ifStmt, 'le', None],
        [ifStmt, 'gt', None],
        [ifStmt, 'ge', None],
        [ifStmt, 'doubleEq', None],
        [ifStmt, 'tOR', None],
        [ifStmt, 'tAND', None],
        [ifStmt, 'mas', None],
        [ifStmt, 'menos', None],
        [ifStmt, 'por', None],
        [ifStmt, 'entre', None],
        [ifStmt, 'tTRUE', None],
        [ifStmt, 'tFALSE', None],
        [ifStmt, 'tNOT', None],
        [ifStmt, 'eof', None],
        [els, 'parenIzq', ['vacia'] ],
        [els, 'parenDer', None ],
        [els, 'comentarioL', ['vacia'] ],
        [els, 'comentarioB', ['vacia'] ],
        [els, 'inicioBloque', None],
        [els, 'finBloque', ['vacia']],
        [els, 'asignacion', ['vacia']],
        [els, 'coma', None],
        [els, 'text', None],
        [els, 'digito', None],
        [els, 'tInt', ['vacia']],
        [els, 'tChar', ['vacia']],
        [els, 'tFloat', ['vacia']],
        [els, 'tVoid', ['vacia']],
        [els, 'tLong', ['vacia']],
        [els, 'tDouble', ['vacia']],
        [els, 'identificador', ['vacia']],
        [els, 'finInstruccion', None],
        [els, 'tReturn', ['vacia']],
        [els, 'tIf', ['vacia']],
        [els, 'tElse', ['tElse','inicioBloque',stmt,'finBloque']],
        [els, 'tWhile', ['vacia']],
        [els, 'tDo', ['vacia']],
        [els, 'tFor', ['vacia']],
        [els, 'lt', ['vacia']],
        [els, 'le', ['vacia']],
        [els, 'gt', ['vacia']],
        [els, 'ge', ['vacia']],
        [els, 'doubleEq', ['vacia']],
        [els, 'tOR', ['vacia']],
        [els, 'tAND', ['vacia']],
        [els, 'mas', ['vacia']],
        [els, 'menos', ['vacia']],
        [els, 'por', ['vacia']],
        [els, 'entre', ['vacia']],
        [els, 'tTRUE', None],
        [els, 'tFALSE', None],
        [els, 'tNOT', None],
        [els, 'eof', None],
        [iterStmt, 'parenIzq', None ],
        [iterStmt, 'parenDer', None ],
        [iterStmt, 'comentarioL', None ],
        [iterStmt, 'comentarioB', None ],
        [iterStmt, 'inicioBloque', None],
        [iterStmt, 'finBloque', None],
        [iterStmt, 'asignacion', None],
        [iterStmt, 'coma', None],
        [iterStmt, 'text', None],
        [iterStmt, 'digito', None],
        [iterStmt, 'tInt', None],
        [iterStmt, 'tChar', None],
        [iterStmt, 'tFloat', None],
        [iterStmt, 'tVoid', None],
        [iterStmt, 'tLong', None],
        [iterStmt, 'tDouble', None],
        [iterStmt, 'identificador', None],
        [iterStmt, 'finInstruccion', None],
        [iterStmt, 'tReturn', None],
        [iterStmt, 'tIf', None],
        [iterStmt, 'tElse', None],
        [iterStmt, 'tWhile', ['tWhile','parenIzq',ASimpleExp,'parenDer','inicioBloque',stmt,'finBloque']],
        [iterStmt, 'tDo', ['tDo','inicioBloque',stmt,'finBloque','tWhile','parenIzq',ASimpleExp,'parenDer',eol]],
        [iterStmt, 'tFor', ['tFor','parenIzq',ASimpleExp,'finInstruccion',ASimpleExp,'finInstruccion',ASimpleExp,'parenDer','inicioBloque',stmt,'finBloque']],
        [iterStmt, 'lt', None],
        [iterStmt, 'le', None],
        [iterStmt, 'gt', None],
        [iterStmt, 'ge', None],
        [iterStmt, 'doubleEq', None],
        [iterStmt, 'tOR', None],
        [iterStmt, 'tAND', None],
        [iterStmt, 'mas', None],
        [iterStmt, 'menos', None],
        [iterStmt, 'por', None],
        [iterStmt, 'entre', None],
        [iterStmt, 'tTRUE', None],
        [iterStmt, 'tFALSE', None],
        [iterStmt, 'tNOT', None],
        [iterStmt, 'eof', None],
        [op, 'parenIzq', None ],
        [op, 'parenDer', None ],
        [op, 'comentarioL', None ],
        [op, 'comentarioB', None ],
        [op, 'inicioBloque', None],
        [op, 'finBloque', None],
        [op, 'asignacion', ['asignacion']],
        [op, 'coma', None],
        [op, 'text', None],
        [op, 'digito', None],
        [op, 'tInt', None],
        [op, 'tChar', None],
        [op, 'tFloat', None],
        [op, 'tVoid', None],
        [op, 'tLong', None],
        [op, 'tDouble', None],
        [op, 'identificador', None],
        [op, 'finInstruccion', None],
        [op, 'tReturn', None],
        [op, 'tIf', None],
        [op, 'tElse', None],
        [op, 'tWhile', None],
        [op, 'tDo', None],
        [op, 'tFor', None],
        [op, 'lt', ['lt']],
        [op, 'le', ['le']],
        [op, 'gt', ['gt']],
        [op, 'ge', ['ge']],
        [op, 'doubleEq', ['doubleEq']],
        [op, 'tOR', ['tOR']],
        [op, 'tAND', ['tAND']],
        [op, 'mas', ['mas']],
        [op, 'menos', ['menos']],
        [op, 'por', ['por']],
        [op, 'entre', ['entre']],
        [op, 'tTRUE', None],
        [op, 'tFALSE', None],
        [op, 'tNOT', None],
        [op, 'eof', None],
        [expr, 'parenIzq', None ],
        [expr, 'parenDer', None ],
        [expr, 'comentarioL', None ],
        [expr, 'comentarioB', None ],
        [expr, 'inicioBloque', None],
        [expr, 'finBloque', None],
        [expr, 'asignacion', None],
        [expr, 'coma', None],
        [expr, 'text', ['text']],
        [expr, 'digito', ['digito']],
        [expr, 'tInt', None],
        [expr, 'tChar', None],
        [expr, 'tFloat', None],
        [expr, 'tVoid', None],
        [expr, 'tLong', None],
        [expr, 'tDouble', None],
        [expr, 'identificador', [var,expr_tail]],
        [expr, 'finInstruccion', None],
        [expr, 'tReturn', None],
        [expr, 'tIf', None],
        [expr, 'tElse', None],
        [expr, 'tWhile', None],
        [expr, 'tDo', None],
        [expr, 'tFor', None],
        [expr, 'lt', None],
        [expr, 'le', None],
        [expr, 'gt', None],
        [expr, 'ge', None],
        [expr, 'doubleEq', None],
        [expr, 'tOR', None],
        [expr, 'tAND', None],
        [expr, 'mas', None],
        [expr, 'menos', None],
        [expr, 'por', None],
        [expr, 'entre', None],
        [expr, 'tTRUE', ['tTRUE']],
        [expr, 'tFALSE', ['tFALSE']],
        [expr, 'tNOT', None],
        [expr, 'eof', None],
        [expr_tail, 'parenIzq', None ],
        [expr_tail, 'parenDer', ['vacia'] ],
        [expr_tail, 'comentarioL', None ],
        [expr_tail, 'comentarioB', None ],
        [expr_tail, 'inicioBloque', None],
        [expr_tail, 'finBloque', None],
        [expr_tail, 'asignacion', [op,expr]],
        [expr_tail, 'coma', None],
        [expr_tail, 'text', None],
        [expr_tail, 'digito', None],
        [expr_tail, 'tInt', None],
        [expr_tail, 'tChar', None],
        [expr_tail, 'tFloat', None],
        [expr_tail, 'tVoid', None],
        [expr_tail, 'tLong', None],
        [expr_tail, 'tDouble', None],
        [expr_tail, 'identificador', None],
        [expr_tail, 'finInstruccion', ['vacia']],
        [expr_tail, 'tReturn', None],
        [expr_tail, 'tIf', None],
        [expr_tail, 'tElse', None],
        [expr_tail, 'tWhile', None],
        [expr_tail, 'tDo', None],
        [expr_tail, 'tFor', None],
        [expr_tail, 'lt', [op,expr]],
        [expr_tail, 'le', [op,expr]],
        [expr_tail, 'gt', [op,expr]],
        [expr_tail, 'ge', [op,expr]],
        [expr_tail, 'doubleEq', [op,expr]],
        [expr_tail, 'tOR', [op,expr]],
        [expr_tail, 'tAND', [op,expr]],
        [expr_tail, 'mas', [op,expr]],
        [expr_tail, 'menos', [op,expr]],
        [expr_tail, 'por', [op,expr]],
        [expr_tail, 'entre', [op,expr]],
        [expr_tail, 'tTRUE', None],
        [expr_tail, 'tFALSE', None],
        [expr_tail, 'tNOT', None],
        [expr_tail, 'eof', None],
        [ASimpleExp, 'parenIzq', None ],
        [ASimpleExp, 'parenDer', None ],
        [ASimpleExp, 'comentarioL', None ],
        [ASimpleExp, 'comentarioB', None ],
        [ASimpleExp, 'inicioBloque', None],
        [ASimpleExp, 'finBloque', None],
        [ASimpleExp, 'asignacion', None],
        [ASimpleExp, 'coma', None],
        [ASimpleExp, 'text', [expr]],
        [ASimpleExp, 'digito', [expr]],
        [ASimpleExp, 'tInt', [simpleExp]],
        [ASimpleExp, 'tChar', [simpleExp]],
        [ASimpleExp, 'tFloat', [simpleExp]],
        [ASimpleExp, 'tVoid', [simpleExp]],
        [ASimpleExp, 'tLong', [simpleExp]],
        [ASimpleExp, 'tDouble', [simpleExp]],
        [ASimpleExp, 'identificador', [expr]],
        [ASimpleExp, 'finInstruccion', None],
        [ASimpleExp, 'tReturn', None],
        [ASimpleExp, 'tIf', None],
        [ASimpleExp, 'tElse', None],
        [ASimpleExp, 'tWhile', None],
        [ASimpleExp, 'tDo', None],
        [ASimpleExp, 'tFor', None],
        [ASimpleExp, 'lt', None],
        [ASimpleExp, 'le', None],
        [ASimpleExp, 'gt', None],
        [ASimpleExp, 'ge', None],
        [ASimpleExp, 'doubleEq', None],
        [ASimpleExp, 'tOR', None],
        [ASimpleExp, 'tAND', None],
        [ASimpleExp, 'mas', None],
        [ASimpleExp, 'menos', None],
        [ASimpleExp, 'por', None],
        [ASimpleExp, 'entre', None],
        [ASimpleExp, 'tTRUE', [expr]],
        [ASimpleExp, 'tFALSE', [expr]],
        [ASimpleExp, 'tNOT', ['tNOT','parenIzq',expr,'parenDer',expr_tail]],
        [ASimpleExp, 'eof', None],
        [simpleExp, 'parenIzq', None ],
        [simpleExp, 'parenDer', None ],
        [simpleExp, 'comentarioL', None ],
        [simpleExp, 'comentarioB', None ],
        [simpleExp, 'inicioBloque', None],
        [simpleExp, 'finBloque', None],
        [simpleExp, 'asignacion', None],
        [simpleExp, 'coma', None],
        [simpleExp, 'text', None],
        [simpleExp, 'digito', None],
        [simpleExp, 'tInt', [tipo,var,op,expr]],
        [simpleExp, 'tChar', [tipo,var,op,expr]],
        [simpleExp, 'tFloat', [tipo,var,op,expr]],
        [simpleExp, 'tVoid', [tipo,var,op,expr]],
        [simpleExp, 'tLong', [tipo,var,op,expr]],
        [simpleExp, 'tDouble', [tipo,var,op,expr]],
        [simpleExp, 'identificador', None],
        [simpleExp, 'finInstruccion', None],
        [simpleExp, 'tReturn', None],
        [simpleExp, 'tIf', None],
        [simpleExp, 'tElse', None],
        [simpleExp, 'tWhile', None],
        [simpleExp, 'tDo', None],
        [simpleExp, 'tFor', None],
        [simpleExp, 'lt', None],
        [simpleExp, 'le', None],
        [simpleExp, 'gt', None],
        [simpleExp, 'ge', None],
        [simpleExp, 'doubleEq', None],
        [simpleExp, 'tOR', None],
        [simpleExp, 'tAND', None],
        [simpleExp, 'mas', None],
        [simpleExp, 'menos', None],
        [simpleExp, 'por', None],
        [simpleExp, 'entre', None],
        [simpleExp, 'tTRUE', None],
        [simpleExp, 'tFALSE', None],
        [simpleExp, 'tNOT', None],
        [simpleExp, 'eof', None],
        ]

#Estado inicial del stack
stack = ['eof', 0]


# Creando el lexer
lexer = lex.lex()

#Funcion con logica del parser
def miParser():
    #Variables para utilizar la tabla de simbolos
    contador = 0
    root = None
    aux = None
    #File a utilizar
    f = open('prueba.c','r')
    lexer.input(f.read())

    tok=lexer.token()
    x=stack[-1]
    while True:
        #Fin de file, la logica se detiene
        if x == tok.type and x == 'eof':
            print("Cadena terminada exitosamente")
            print("******** Imprimiendo tabla de simbolos ********")
            printInorder(root)
            return #aceptar
        else:
            #Agregando nodos a la tabla de simbolos
            if root is None:
                root = Node(tokenInfo(contador,tok.type,tok.value,tok.lineno,tok.lexpos))
                aux = tok
                contador += 1
            else:
                if aux.lexpos != tok.lexpos :
                    root = insert(root, tokenInfo(contador,tok.type,tok.value,tok.lineno,tok.lexpos))
                    contador += 1
                    aux = tok
            #Final de camino de derivación
            if x == tok.type and x != 'eof':
                stack.pop()
                x=stack[-1]
                tok=lexer.token()
            #Error de token inesperado
            if x in tokens and x != tok.type:
                print("Error: se esperaba ", x)
                print('en la posicion: ', tok.lexpos)
                while True:
                    tok = lexer.token()
                    if tok.type == x: 
                        break
            #Caso de token siendo no terminal
            if x not in tokens: 
                celda=buscar_en_tabla(x,tok.type)
                if  celda is None:
                    #Si no se encuentra en tabla, error de sintaxis
                    print("Error: NO se esperaba", tok.type)
                    print('en la posicion: ', tok.lexpos)
                    print("Celda: ", celda)
                    return 0
                else:
                    #Resolucion de token no terminal
                    stack.pop()
                    agregar_pila(celda)
                    x=stack[-1]
        #Mostrar el estado actual del stack
        print(stack)

#Herramienta para buscar en tabla de gramatica
def buscar_en_tabla(no_terminal, terminal):
    for i in range(len(tabla2)):
        if( tabla2[i][0] == no_terminal and tabla2[i][1] == terminal):
            return tabla2[i][2]

#Logica de agregar elementos al stack del parser
def agregar_pila(produccion):
    for elemento in reversed(produccion):
        if elemento != 'vacia':
            stack.append(elemento)

#Llamar al parser
miParser()
