# ------------------------------------------------------------
# Lexer para C
# ------------------------------------------------------------
import ply.lex as lex

Start=0
comment=1
declare=2
branch=3
params=4
var_params=5
eq=6
cm=7
var_fin=8
tipo=9
var=10
eol=11
stmt=12
returnStmt=13
expStmt=14
var_stmt=15
ifStmt=16
els=17
iterStmt=18
op=19
expr=20
expr_tail=21
ASimpleExp=22
simpleExp=23

# List of token names.   This is always required
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
    'comentario',#Manejo de comentarios 
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
    'letterdigit',
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

#t_vacia= r'\'  

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

# Token para palabras reservadas especificas a c++
def t_palabraReservada(t):
    #Utilizado el maximo de 15 palabras, aunque siguen sin ser s
    # Tipos de datos: int, char, float.
    # Instrucciones: condicional if-else (hasta ahora solo las keywords) 
    # Palabras claves o reservadas: char, int, float, return, void, if, else (ojo esta return void tambien)
    # Instrucciones de iteración: do-while, while o for
    r'(return)|(if)|(else)|(do)|(while)|(for)'
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
    #return t

# Para comentarios de bloque
# Manejo de comentarios 
def t_comentario(t):
    r'\/\*(.|\n)*\*\/'
    #return t

# Manejo de errores
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    return t

def t_letterdigit(t):
    r'([a-z]|[A-Z]|\d)*'
    return t

tabla2 = [ [Start, 'comentario', [comment,Start] ],
        [Start, 'parenIzq', None ],
        [Start, 'parenDer', None ],
        [Start, 'inicioBloque', None],
        [Start, 'finBloque', None],
        [Start, 'asignacion', None],
        [Start, 'coma', None],
        [Start, 'letterdigit', None],
        [Start, 'tInt', [declare] ],
        [Start, 'tChar', [declare] ],
        [Start, 'tFloat', [declare] ],
        [Start, 'tVoid', [declare] ],
        [Start, 'tLong', [declare] ],
        [Start, 'tDouble', [declare] ],
        [Start, 'identificador', None],
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
        [Start, 'tTRUE', None],
        [Start, 'tFALSE', None],
        [Start, 'mas', None],
        [Start, 'menos', None],
        [Start, 'por', None],
        [Start, 'entre', None],
        [Start, 'tNOT', None],
        [Start, 'eof', None],
        [comment, 'comentario', ['comentario'] ],
        [comment, 'parenIzq', None ],
        [comment, 'parenDer', None ],
        [comment, 'inicioBloque', None],
        [comment, 'finBloque', None],
        [comment, 'asignacion', None],
        [comment, 'coma', None],
        [comment, 'letterdigit', None],
        [comment, 'tInt', None ],
        [comment, 'tChar', None ],
        [comment, 'tFloat', None ],
        [comment, 'tVoid', None ],
        [comment, 'tLong', None ],
        [comment, 'tDouble', None ],
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
        [comment, 'tTRUE', None],
        [comment, 'tFALSE', None],
        [comment, 'mas', None],
        [comment, 'menos', None],
        [comment, 'por', None],
        [comment, 'entre', None],
        [comment, 'tNOT', None],
        [comment, 'eof', None],
        [declare, 'comentario', None ],
        [declare, 'parenIzq', None ],
        [declare, 'parenDer', None ],
        [declare, 'inicioBloque', None],
        [declare, 'finBloque', None],
        [declare, 'asignacion', None],
        [declare, 'coma', None],
        [declare, 'letterdigit', None],
        [declare, 'tInt', [tipo,var,branch] ],
        [declare, 'tChar', [tipo,var,branch] ],
        [declare, 'tFloat', [tipo,var,branch] ],
        [declare, 'tVoid', [tipo,var,branch] ],
        [declare, 'tLong', [tipo,var,branch] ],
        [declare, 'tDouble', [tipo,var,branch] ],
        [declare, 'identificador', None],
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
        [declare, 'tTRUE', None],
        [declare, 'tFALSE', None],
        [declare, 'mas', None],
        [declare, 'menos', None],
        [declare, 'por', None],
        [declare, 'entre', None],
        [declare, 'tNOT', None],
        [declare, 'eof', None],
        [branch, 'comentario', None ],
        [branch, 'parenIzq', ['parenIzq', params , 'parenDer', 'inicioBloque', stmt, 'finBloque' ] ],
        [branch, 'parenDer', None ],
        [branch, 'inicioBloque', None],
        [branch, 'finBloque', None],
        [branch, 'asignacion', [eq, var_fin, eol]],
        [branch, 'coma', [eq, var_fin, eol]],
        [branch, 'letterdigit', None],
        [branch, 'tInt', None ],
        [branch, 'tChar', None ],
        [branch, 'tFloat', None ],
        [branch, 'tVoid', None ],
        [branch, 'tLong', None ],
        [branch, 'tDouble', None ],
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
        [branch, 'tTRUE', None],
        [branch, 'tFALSE', None],
        [branch, 'mas', None],
        [branch, 'menos', None],
        [branch, 'por', None],
        [branch, 'entre', None],
        [branch, 'tNOT', None],
        [branch, 'eof', None],
        [params, 'comentario', None ],
        [params, 'parenIzq', None ],
        [params, 'parenDer', ['vacia'] ],
        [params, 'inicioBloque', None],
        [params, 'finBloque', None],
        [params, 'asignacion', None],
        [params, 'coma', None],
        [params, 'letterdigit', None],
        [params, 'tInt', [tipo,var,cm,var_params] ],
        [params, 'tChar', [tipo,var,cm,var_params] ],
        [params, 'tFloat', [tipo,var,cm,var_params] ],
        [params, 'tVoid', [tipo,var,cm,var_params] ],
        [params, 'tLong', [tipo,var,cm,var_params] ],
        [params, 'tDouble', [tipo,var,cm,var_params] ],
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
        [params, 'tTRUE', None],
        [params, 'tFALSE', None],
        [params, 'mas', None],
        [params, 'menos', None],
        [params, 'por', None],
        [params, 'entre', None],
        [params, 'tNOT', None],
        [params, 'eof', None],
        [var_params, 'comentario', None ],
        [var_params, 'parenIzq', None ],
        [var_params, 'parenDer', [params] ],
        [var_params, 'inicioBloque', None],
        [var_params, 'finBloque', None],
        [var_params, 'asignacion', None],
        [var_params, 'coma', None],
        [var_params, 'letterdigit', None],
        [var_params, 'tInt', [params] ],
        [var_params, 'tChar', [params] ],
        [var_params, 'tFloat', [params] ],
        [var_params, 'tVoid', [params] ],
        [var_params, 'tLong', [params] ],
        [var_params, 'tDouble', [params] ],
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
        [var_params, 'tTRUE', None],
        [var_params, 'tFALSE', None],
        [var_params, 'mas', None],
        [var_params, 'menos', None],
        [var_params, 'por', None],
        [var_params, 'entre', None],
        [var_params, 'tNOT', None],
        [var_params, 'eof', None],
        [eq, 'comentario', None ],
        [eq, 'parenIzq', None ],
        [eq, 'parenDer', None ],
        [eq, 'inicioBloque', None],
        [eq, 'finBloque', None],
        [eq, 'asignacion', ['asignacion']],
        [eq, 'coma', ['coma']],
        [eq, 'letterdigit', None],
        [eq, 'tInt', None ],
        [eq, 'tChar', None ],
        [eq, 'tFloat', None ],
        [eq, 'tVoid', None ],
        [eq, 'tLong', None ],
        [eq, 'tDouble', None ],
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
        [eq, 'tTRUE', None],
        [eq, 'tFALSE', None],
        [eq, 'mas', None],
        [eq, 'menos', None],
        [eq, 'por', None],
        [eq, 'entre', None],
        [eq, 'tNOT', None],
        [eq, 'eof', None],
        [cm, 'comentario', None ],
        [cm, 'parenIzq', None ],
        [cm, 'parenDer', ['vacia'] ],
        [cm, 'inicioBloque', None],
        [cm, 'finBloque', None],
        [cm, 'asignacion', None],
        [cm, 'coma', ['coma']],
        [cm, 'letterdigit', None],
        [cm, 'tInt', ['vacia'] ],
        [cm, 'tChar', ['vacia'] ],
        [cm, 'tFloat', ['vacia'] ],
        [cm, 'tVoid', ['vacia'] ],
        [cm, 'tLong', ['vacia'] ],
        [cm, 'tDouble', ['vacia'] ],
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
        [cm, 'tTRUE', None],
        [cm, 'tFALSE', None],
        [cm, 'mas', None],
        [cm, 'menos', None],
        [cm, 'por', None],
        [cm, 'entre', None],
        [cm, 'tNOT', None],
        [cm, 'eof', None],
        [var_fin, 'comentario', None ],
        [var_fin, 'parenIzq', [branch] ],
        [var_fin, 'parenDer', None ],
        [var_fin, 'inicioBloque', None],
        [var_fin, 'finBloque', None],
        [var_fin, 'asignacion', [branch]],
        [var_fin, 'coma', [branch]],
        [var_fin, 'letterdigit', ['letterdigit']],
        [var_fin, 'tInt', None ],
        [var_fin, 'tChar', None ],
        [var_fin, 'tFloat', None ],
        [var_fin, 'tVoid', None ],
        [var_fin, 'tLong', None ],
        [var_fin, 'tDouble', None ],
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
        [var_fin, 'tTRUE', None],
        [var_fin, 'tFALSE', None],
        [var_fin, 'mas', None],
        [var_fin, 'menos', None],
        [var_fin, 'por', None],
        [var_fin, 'entre', None],
        [var_fin, 'tNOT', None],
        [var_fin, 'eof', None],
        [tipo, 'comentario', None ],
        [tipo, 'parenIzq', None ],
        [tipo, 'parenDer', None ],
        [tipo, 'inicioBloque', None],
        [tipo, 'finBloque', None],
        [tipo, 'asignacion', None],
        [tipo, 'coma', None],
        [tipo, 'letterdigit', None],
        [tipo, 'tInt', ['tInt'] ],
        [tipo, 'tChar', ['tChar'] ],
        [tipo, 'tFloat', ['tFloat'] ],
        [tipo, 'tVoid', ['tVoid'] ],
        [tipo, 'tLong', ['tLong'] ],
        [tipo, 'tDouble', ['tDouble'] ],
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
        [tipo, 'tTRUE', None],
        [tipo, 'tFALSE', None],
        [tipo, 'mas', None],
        [tipo, 'menos', None],
        [tipo, 'por', None],
        [tipo, 'entre', None],
        [tipo, 'tNOT', None],
        [tipo, 'eof', None],
        [var, 'comentario', None ],
        [var, 'parenIzq', None ],
        [var, 'parenDer', None ],
        [var, 'inicioBloque', None],
        [var, 'finBloque', None],
        [var, 'asignacion', None],
        [var, 'coma', None],
        [var, 'letterdigit', None],
        [var, 'tInt', None ],
        [var, 'tChar', None ],
        [var, 'tFloat', None ],
        [var, 'tVoid', None ],
        [var, 'tLong', None ],
        [var, 'tDouble', None ],
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
        [var, 'tTRUE', None],
        [var, 'tFALSE', None],
        [var, 'mas', None],
        [var, 'menos', None],
        [var, 'por', None],
        [var, 'entre', None],
        [var, 'tNOT', None],
        [var, 'eof', None],
        [eol, 'comentario', None ],
        [eol, 'parenIzq', None ],
        [eol, 'parenDer', None ],
        [eol, 'inicioBloque', None],
        [eol, 'finBloque', None],
        [eol, 'asignacion', None],
        [eol, 'coma', None],
        [eol, 'letterdigit', None],
        [eol, 'tInt', None ],
        [eol, 'tChar', None ],
        [eol, 'tFloat', None ],
        [eol, 'tVoid', None ],
        [eol, 'tLong', None ],
        [eol, 'tDouble', None ],
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
        [eol, 'tTRUE', None],
        [eol, 'tFALSE', None],
        [eol, 'mas', None],
        [eol, 'menos', None],
        [eol, 'por', None],
        [eol, 'entre', None],
        [eol, 'tNOT', None],
        [eol, 'eof', None],
        [stmt, 'comentario', None ],
        [stmt, 'parenIzq', None ],
        [stmt, 'parenDer', None ],
        [stmt, 'inicioBloque', None],
        [stmt, 'finBloque', None],
        [stmt, 'asignacion', None],
        [stmt, 'coma', None],
        [stmt, 'letterdigit', None],
        [stmt, 'tInt', [expStmt,eol] ],
        [stmt, 'tChar', [expStmt,eol] ],
        [stmt, 'tFloat', [expStmt,eol] ],
        [stmt, 'tVoid', [expStmt,eol] ],
        [stmt, 'tLong', [expStmt,eol] ],
        [stmt, 'tDouble', [expStmt,eol] ],
        [stmt, 'identificador', [expStmt,eol]],
        [stmt, 'finInstruccion', None],
        [stmt, 'tReturn', [returnStmt]],
        [stmt, 'tIf', [ifStmt]],
        [stmt, 'tElse', None],
        [stmt, 'tWhile', [iterStmt]],
        [stmt, 'tDo', [iterStmt]],
        [stmt, 'tFor', [iterStmt]],
        [stmt, 'lt', None],
        [stmt, 'le', None],
        [stmt, 'gt', None],
        [stmt, 'ge', None],
        [stmt, 'doubleEq', None],
        [stmt, 'tOR', None],
        [stmt, 'tAND', None],
        [stmt, 'tTRUE', None],
        [stmt, 'tFALSE', None],
        [stmt, 'mas', None],
        [stmt, 'menos', None],
        [stmt, 'por', None],
        [stmt, 'entre', None],
        [stmt, 'tNOT', None],
        [stmt, 'eof', None],
        [returnStmt, 'comentario', None ],
        [returnStmt, 'parenIzq', None ],
        [returnStmt, 'parenDer', None ],
        [returnStmt, 'inicioBloque', None],
        [returnStmt, 'finBloque', None],
        [returnStmt, 'asignacion', None],
        [returnStmt, 'coma', None],
        [returnStmt, 'letterdigit', None],
        [returnStmt, 'tInt', None ],
        [returnStmt, 'tChar', None ],
        [returnStmt, 'tFloat', None ],
        [returnStmt, 'tVoid', None ],
        [returnStmt, 'tLong', None ],
        [returnStmt, 'tDouble', None ],
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
        [returnStmt, 'tTRUE', None],
        [returnStmt, 'tFALSE', None],
        [returnStmt, 'mas', None],
        [returnStmt, 'menos', None],
        [returnStmt, 'por', None],
        [returnStmt, 'entre', None],
        [returnStmt, 'tNOT', None],
        [returnStmt, 'eof', None],
        [expStmt, 'comentario', None ],
        [expStmt, 'parenIzq', None ],
        [expStmt, 'parenDer', None ],
        [expStmt, 'inicioBloque', None],
        [expStmt, 'finBloque', None],
        [expStmt, 'asignacion', None],
        [expStmt, 'coma', None],
        [expStmt, 'letterdigit', None],
        [expStmt, 'tInt', [tipo,var,eq,var_stmt] ],
        [expStmt, 'tChar', [tipo,var,eq,var_stmt] ],
        [expStmt, 'tFloat', [tipo,var,eq,var_stmt] ],
        [expStmt, 'tVoid', [tipo,var,eq,var_stmt] ],
        [expStmt, 'tLong', [tipo,var,eq,var_stmt] ],
        [expStmt, 'tDouble', [tipo,var,eq,var_stmt] ],
        [expStmt, 'identificador', [var,op,expr]],
        [expStmt, 'finInstruccion', None],
        [expStmt, 'tReturn', None],
        [expStmt, 'tIf', None],
        [expStmt, 'tElse', None],
        [expStmt, 'tWhile', None],
        [expStmt, 'tDo', None],
        [expStmt, 'tFor', None],
        [expStmt, 'lt', None],
        [expStmt, 'le', None],
        [expStmt, 'gt', None],
        [expStmt, 'ge', None],
        [expStmt, 'doubleEq', None],
        [expStmt, 'tOR', None],
        [expStmt, 'tAND', None],
        [expStmt, 'tTRUE', None],
        [expStmt, 'tFALSE', None],
        [expStmt, 'mas', None],
        [expStmt, 'menos', None],
        [expStmt, 'por', None],
        [expStmt, 'entre', None],
        [expStmt, 'tNOT', None],
        [expStmt, 'eof', None],
        [var_stmt, 'comentario', None ],
        [var_stmt, 'parenIzq', None ],
        [var_stmt, 'parenDer', ['vacia'] ],
        [var_stmt, 'inicioBloque', None],
        [var_stmt, 'finBloque', None],
        [var_stmt, 'asignacion', None],
        [var_stmt, 'coma', None],
        [var_stmt, 'letterdigit', ['letterdigit']],
        [var_stmt, 'tInt', [expStmt] ],
        [var_stmt, 'tChar', [expStmt] ],
        [var_stmt, 'tFloat', [expStmt] ],
        [var_stmt, 'tVoid', [expStmt] ],
        [var_stmt, 'tLong', [expStmt] ],
        [var_stmt, 'tDouble', [expStmt] ],
        [var_stmt, 'identificador', [expStmt]],
        [var_stmt, 'finInstruccion', ['vacia']],
        [var_stmt, 'tReturn', None],
        [var_stmt, 'tIf', None],
        [var_stmt, 'tElse', None],
        [var_stmt, 'tWhile', None],
        [var_stmt, 'tDo', None],
        [var_stmt, 'tFor', None],
        [var_stmt, 'lt', None],
        [var_stmt, 'le', None],
        [var_stmt, 'gt', None],
        [var_stmt, 'ge', None],
        [var_stmt, 'doubleEq', None],
        [var_stmt, 'tOR', None],
        [var_stmt, 'tAND', None],
        [var_stmt, 'tTRUE', None],
        [var_stmt, 'tFALSE', None],
        [var_stmt, 'mas', None],
        [var_stmt, 'menos', None],
        [var_stmt, 'por', None],
        [var_stmt, 'entre', None],
        [var_stmt, 'tNOT', None],
        [var_stmt, 'eof', None],
        [ifStmt, 'comentario', None ],
        [ifStmt, 'parenIzq', None ],
        [ifStmt, 'parenDer', None ],
        [ifStmt, 'inicioBloque', None],
        [ifStmt, 'finBloque', None],
        [ifStmt, 'asignacion', None],
        [ifStmt, 'coma', None],
        [ifStmt, 'letterdigit', None],
        [ifStmt, 'tInt', None ],
        [ifStmt, 'tChar', None ],
        [ifStmt, 'tFloat', None ],
        [ifStmt, 'tVoid', None ],
        [ifStmt, 'tLong', None ],
        [ifStmt, 'tDouble', None ],
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
        [ifStmt, 'tTRUE', None],
        [ifStmt, 'tFALSE', None],
        [ifStmt, 'mas', None],
        [ifStmt, 'menos', None],
        [ifStmt, 'por', None],
        [ifStmt, 'entre', None],
        [ifStmt, 'tNOT', None],
        [ifStmt, 'eof', None],
        [els, 'comentario', None ],
        [els, 'parenIzq', None ],
        [els, 'parenDer', None ],
        [els, 'inicioBloque', None],
        [els, 'finBloque', ['vacia']],
        [els, 'asignacion', None],
        [els, 'coma', None],
        [els, 'letterdigit', None],
        [els, 'tInt', None ],
        [els, 'tChar', None ],
        [els, 'tFloat', None ],
        [els, 'tVoid', None ],
        [els, 'tLong', None ],
        [els, 'tDouble', None ],
        [els, 'identificador', None],
        [els, 'finInstruccion', None],
        [els, 'tReturn', None],
        [els, 'tIf', None],
        [els, 'tElse', ['tElse','inicioBloque',stmt,'finBloque']],
        [els, 'tWhile', None],
        [els, 'tDo', None],
        [els, 'tFor', None],
        [els, 'lt', None],
        [els, 'le', None],
        [els, 'gt', None],
        [els, 'ge', None],
        [els, 'doubleEq', None],
        [els, 'tOR', None],
        [els, 'tAND', None],
        [els, 'tTRUE', None],
        [els, 'tFALSE', None],
        [els, 'mas', None],
        [els, 'menos', None],
        [els, 'por', None],
        [els, 'entre', None],
        [els, 'tNOT', None],
        [els, 'eof', None],
        [iterStmt, 'comentario', None ],
        [iterStmt, 'parenIzq', None ],
        [iterStmt, 'parenDer', None ],
        [iterStmt, 'inicioBloque', None],
        [iterStmt, 'finBloque', None],
        [iterStmt, 'asignacion', None],
        [iterStmt, 'coma', None],
        [iterStmt, 'letterdigit', None],
        [iterStmt, 'tInt', None ],
        [iterStmt, 'tChar', None ],
        [iterStmt, 'tFloat', None ],
        [iterStmt, 'tVoid', None ],
        [iterStmt, 'tLong', None ],
        [iterStmt, 'tDouble', None ],
        [iterStmt, 'identificador', None],
        [iterStmt, 'finInstruccion', None],
        [iterStmt, 'tReturn', None],
        [iterStmt, 'tIf', None],
        [iterStmt, 'tElse', None],
        [iterStmt, 'tWhile', ['tWhile','parenIzq', ASimpleExp, 'parenDer', 'inicioBloque',stmt , 'finBloque']],
        [iterStmt, 'tDo', ['tDo','inicioBloque' , stmt , 'finBloque', 'tWhile', 'parenIzq', ASimpleExp, 'parenDer']],
        [iterStmt, 'tFor', ['tFor', 'parenIzq', expStmt, 'finInstruccion', expStmt, 'finInstruccion', expStmt, 'parenDer', 'inicioBloque', stmt, 'finBloque']],
        [iterStmt, 'lt', None],
        [iterStmt, 'le', None],
        [iterStmt, 'gt', None],
        [iterStmt, 'ge', None],
        [iterStmt, 'doubleEq', None],
        [iterStmt, 'tOR', None],
        [iterStmt, 'tAND', None],
        [iterStmt, 'tTRUE', None],
        [iterStmt, 'tFALSE', None],
        [iterStmt, 'mas', None],
        [iterStmt, 'menos', None],
        [iterStmt, 'por', None],
        [iterStmt, 'entre', None],
        [iterStmt, 'tNOT', None],
        [iterStmt, 'eof', None],
        [op, 'comentario', None ],
        [op, 'parenIzq', None ],
        [op, 'parenDer', None ],
        [op, 'inicioBloque', None],
        [op, 'finBloque', None],
        [op, 'asignacion', ['asignacion']],
        [op, 'coma', None],
        [op, 'letterdigit', None],
        [op, 'tInt', None ],
        [op, 'tChar', None ],
        [op, 'tFloat', None ],
        [op, 'tVoid', None ],
        [op, 'tLong', None ],
        [op, 'tDouble', None ],
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
        [op, 'tTRUE', None],
        [op, 'tFALSE', None],
        [op, 'mas', None],
        [op, 'menos', None],
        [op, 'por', None],
        [op, 'entre', None],
        [op, 'tNOT', None],
        [op, 'eof', None],
        [expr, 'comentario', None ],
        [expr, 'parenIzq', None ],
        [expr, 'parenDer', None ],
        [expr, 'inicioBloque', None],
        [expr, 'finBloque', None],
        [expr, 'asignacion', None],
        [expr, 'coma', None],
        [expr, 'letterdigit', ['letterdigit']],
        [expr, 'tInt', None ],
        [expr, 'tChar', None ],
        [expr, 'tFloat', None ],
        [expr, 'tVoid', None ],
        [expr, 'tLong', None ],
        [expr, 'tDouble', None ],
        [expr, 'identificador', [var, expr_tail]],
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
        [expr, 'tTRUE', ['tTRUE']],
        [expr, 'tFALSE', ['tFALSE']],
        [expr, 'mas', None],
        [expr, 'menos', None],
        [expr, 'por', None],
        [expr, 'entre', None],
        [expr, 'tNOT', None],
        [expr, 'eof', None],
        [expr_tail, 'comentario', None ],
        [expr_tail, 'parenIzq', None ],
        [expr_tail, 'parenDer', ['vacia'] ],
        [expr_tail, 'inicioBloque', None],
        [expr_tail, 'finBloque', None],
        [expr_tail, 'asignacion', None],
        [expr_tail, 'coma', None],
        [expr_tail, 'letterdigit', None],
        [expr_tail, 'tInt', None ],
        [expr_tail, 'tChar', None ],
        [expr_tail, 'tFloat', None ],
        [expr_tail, 'tVoid', None ],
        [expr_tail, 'tLong', None ],
        [expr_tail, 'tDouble', None ],
        [expr_tail, 'identificador', None],
        [expr_tail, 'finInstruccion', ['vacia']],
        [expr_tail, 'tReturn', None],
        [expr_tail, 'tIf', None],
        [expr_tail, 'tElse', None],
        [expr_tail, 'tWhile', None],
        [expr_tail, 'tDo', None],
        [expr_tail, 'tFor', None],
        [expr_tail, 'lt', None],
        [expr_tail, 'le', None],
        [expr_tail, 'gt', None],
        [expr_tail, 'ge', None],
        [expr_tail, 'doubleEq', None],
        [expr_tail, 'tOR', None],
        [expr_tail, 'tAND', None],
        [expr_tail, 'tTRUE', None],
        [expr_tail, 'tFALSE', None],
        [expr_tail, 'mas', ['mas',expr]],
        [expr_tail, 'menos', ['menos',expr]],
        [expr_tail, 'por', ['por',expr]],
        [expr_tail, 'entre', ['entre',expr]],
        [expr_tail, 'tNOT', None],
        [expr_tail, 'eof', None],
        [ASimpleExp, 'comentario', None ],
        [ASimpleExp, 'parenIzq', None ],
        [ASimpleExp, 'parenDer', None ],
        [ASimpleExp, 'inicioBloque', None],
        [ASimpleExp, 'finBloque', None],
        [ASimpleExp, 'asignacion', None],
        [ASimpleExp, 'coma', None],
        [ASimpleExp, 'letterdigit', [expr]],
        [ASimpleExp, 'tInt', None ],
        [ASimpleExp, 'tChar', None ],
        [ASimpleExp, 'tFloat', None ],
        [ASimpleExp, 'tVoid', None ],
        [ASimpleExp, 'tLong', None ],
        [ASimpleExp, 'tDouble', None ],
        [ASimpleExp, 'identificador', [simpleExp]],
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
        [ASimpleExp, 'tTRUE', [expr]],
        [ASimpleExp, 'tFALSE', [expr]],
        [ASimpleExp, 'mas', None],
        [ASimpleExp, 'menos', None],
        [ASimpleExp, 'por', None],
        [ASimpleExp, 'entre', None],
        [ASimpleExp, 'tNOT', ['tNOT','parenIzq',simpleExp ,'parenDer']],
        [ASimpleExp, 'eof', None],
        [simpleExp, 'comentario', None ],
        [simpleExp, 'parenIzq', None ],
        [simpleExp, 'parenDer', None ],
        [simpleExp, 'inicioBloque', None],
        [simpleExp, 'finBloque', None],
        [simpleExp, 'asignacion', None],
        [simpleExp, 'coma', None],
        [simpleExp, 'letterdigit', None],
        [simpleExp, 'tInt', None ],
        [simpleExp, 'tChar', None ],
        [simpleExp, 'tFloat', None ],
        [simpleExp, 'tVoid', None ],
        [simpleExp, 'tLong', None ],
        [simpleExp, 'tDouble', None ],
        [simpleExp, 'identificador', [var, op, expr]],
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
        [simpleExp, 'tTRUE', None],
        [simpleExp, 'tFALSE', None],
        [simpleExp, 'mas', None],
        [simpleExp, 'menos', None],
        [simpleExp, 'por', None],
        [simpleExp, 'entre', None],
        [simpleExp, 'tNOT', None],
        [simpleExp, 'eof', None],
        ]

stack = ['eof', 0]


# Build the lexer
lexer = lex.lex()

def miParser():
    #f = open('fuente.c','r')
    #lexer.input(f.read())
    lexer.input('total_mujeres+total_hombres)$')
    

    tok=lexer.token()
    x=stack[-1] #primer elemento de der a izq
    while True:
        #print(tok.type)
        #print(x)
        if x == tok.type and x == 'eof':
            print("Cadena terminada exitosamente")
            return #aceptar
        else:
            if x == tok.type and x != 'eof':#llegué a un camino de derivación completo
                stack.pop()
                x=stack[-1]
                tok=lexer.token()                
            if x in tokens and x != tok.type:                
                print("Error: se esperaba ", x)
                print('en la posicion: ', tok.lexpos)
                #panic mode                
                while True:
                    tok = lexer.token()# Get the next token
                    if tok.type == x: 
                        break
                
            if x not in tokens: #es no terminal      
                celda=buscar_en_tabla(x,tok.type)                            
                if  celda is None:
                    print("Error: NO se esperaba", tok.type)
                    print('en la posicion: ', tok.lexpos)
                    return 0
                else:                    
                    stack.pop()
                    agregar_pila(celda)
                    x=stack[-1]
        print(stack)
        print()

            
        #if not tok:
            #break
        #print(tok)
        #print(tok.type, tok.value, tok.lineno, tok.lexpos)

def buscar_en_tabla(no_terminal, terminal):
    for i in range(len(tabla2)):
        if( tabla2[i][0] == no_terminal and tabla2[i][1] == terminal):
            return tabla2[i][2] #retorno la celda

def agregar_pila(produccion):
    for elemento in reversed(produccion):
        if elemento != 'vacia': #la vacía no la inserta
            stack.append(elemento)


miParser()