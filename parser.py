# ------------------------------------------------------------
# Lexer para C
# ------------------------------------------------------------
import ply.lex as lex

S=0
S2=1
T=2
T2=3
F=4

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
   'coma',
   'eof',
   'int',
   'float',
   'AND',
   'OR',
   'EQUALS'
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
t_eof= r'\$'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_EQUALS = r'\=\='

#t_vacia= r'\'  


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t
def t_int(t):
    r'(int)'
    return t

def t_float(t):
    r'(float)'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_keyword(t):
    r'(const)|(struct)|(double)|(int)|(float)|(char)|(return)|(if)|(else)|(do)|(while)|(for)|(void)|(include)'
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



tabla2 = [[S, 'identificador', [T,S2] ],
         [S, 'PLUS', None ],
         [S, 'TIMES', None ],
         [S, 'LPAREN', [T,S2]],
         [S, 'RPAREN', None],
         [S, 'eof', None],
         [S2, 'identificador', None ],
         [S2, 'PLUS', ['PLUS',T,S2] ],
         [S2, 'TIMES', None ],
         [S2, 'LPAREN', None],
         [S2, 'RPAREN', ['vacia']],
         [S2, 'eof', ['vacia']],
         [T, 'identificador', [F,T2] ],
         [T, 'PLUS', None ],
         [T, 'TIMES', None ],
         [T, 'LPAREN', [F,T2]],
         [T, 'RPAREN', None],
         [T, 'eof', None],
         [T2, 'identificador', None ],
         [T2, 'PLUS', ['vacia'] ],
         [T2, 'TIMES', ['TIMES',F,T2] ],
         [T2, 'LPAREN', None],
         [T2, 'RPAREN', ['vacia']],
         [T2, 'eof', ['vacia']],
         [F, 'identificador', ['identificador'] ],
         [F, 'PLUS', None ],
         [F, 'TIMES', None ],
         [F, 'LPAREN', ['LPAREN',S,'RPAREN']],
         [F, 'RPAREN', None],
         [F, 'eof', None],
         ]

stack = ['eof', 0]


# Build the lexer
lexer = lex.lex()

def miParser():
    #f = open('fuente.c','r')
    #lexer.input(f.read())
    lexer.input('+$')
    

    tok=lexer.token()
    x=stack[-1] #primer elemento de der a izq
    while True:
        print(tok.type)
        print(x)
        if x == tok.type and x == 'eof':
            print("Cadena reconocida exitosamente")
            return #aceptar
        else:
            if x == tok.type and x != 'eof':
                stack.pop()
                x=stack[-1]
                tok=lexer.token()                
            if x in tokens and x != tok.type:
                print("Error: se esperaba ", tok.type)
                print('en la posicion: ', tok.lexpos);
                return 0;
            if x not in tokens: #es no terminal      
                celda=buscar_en_tabla(x,tok.type)                            
                if  celda is None:
                    print("Error: NO se esperaba", tok.type)
                    print('en la posicion: ', tok.lexpos);
                    return 0;
                else:
                    stack.pop()
                    agregar_pila(celda)
                    x=stack[-1]
        print(stack)
        print()
        #FALTA AGREGAR LAS COSAS A LA TABLA DE SIMBOLOS

            
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
