import re

f = open('fuente.c','r')


#Lista de tipos de tokens
operators = { '=': 'Asignacion','+': 'Operador suma', '-' : 'Operador resta', '/' : 'Division Operador', '*': 'Multiplicacion Operador', '++' : 'Operador incremente', '--' : 'Operador decremento'}
optr_keys = operators.keys()

comments = {r'//' : 'Comentario de línea',r'/*' : 'Inicia comentario multilinea', r'*/' : 'Termina comentario multilinea', '/**/' : 'Comentario vacio'}
comment_keys = comments.keys()

header = {'.h': 'archivo de encabezado'}
header_keys = header.keys()

sp_header_files = {'<stdio.h>':'Standard Input Output Librería','<string.h>':'String Manipulation Libreria'}

macros = {r'#\w+' : 'macro'}
macros_keys = macros.keys()

datatype = {'int': 'Integer','float' : 'Floating Point', 'char': 'Character','long': 'long int'}
datatype_keys = datatype.keys()

keyword = {'return' : 'Palabra clave que retorna al SO'}
keyword_keys = keyword.keys()

delimiter = {';':'Fin de instruccion'}
delimiter_keys = delimiter.keys()

blocks = {'{' : 'Inicia bloque de instrucciones', '}':'Fin de bloque de instrucciones'}
block_keys = blocks.keys()

builtin_functions = {'printf':'Imprime en consola'}

non_identifiers = ['_','-','+','/','*','`','~','!','@','#','$','%','^','&','*','(',')','=','|','"',':',';','{'
,'}','[',']','<','>','?','/']

numerals = ['0','1','2','3','4','5','6','7','8','9','10']

# banderas
dataFlag = False


i = f.read()

count = 0
program =  i.split('\n')

for line in program:
    count = count+1
    print ("Line #",count,"\n",line)
    
     
    tokens = line.split(' ')#asumiendo el espacio //no deberia ser
    print ("Tokens son",tokens)
    print ("Linea #",count,'propiedades \n')
    for token in tokens:
        
        if '\r' in token:
            position = token.find('\r')
            token=token[:position]
        # print 1
        
        if token in block_keys:
            print (blocks[token])
        if token in optr_keys:
            print ("Operador es: ", operators[token])
        if token in comment_keys:
            print ("Comentario: ", comments[token])
        if token in macros_keys:
            print ("Macro es: ", macros[token])
        if '.h' in token:
            print ("Archivo de encabezado: ",token, sp_header_files[token])
        if '()' in token:
            print ("Función:", token)
        
        if dataFlag == True and (token not in non_identifiers) and ('()' not in token):
            print ("Identificador: ",token)
        if token in datatype_keys:
            print ("Tipo es: ", datatype[token])
            dataFlag = True
        
        if token in keyword_keys:
            print (keyword[token])
            
        if token in delimiter:
            print ("Delimitador" , delimiter[token])
        if '#' in token:
            match = re.search(r'#\w+', token)
            print ("Encabezado", match.group())
        if token in numerals:
            print (token,type(int(token)))
            
    dataFlag = False   
            
    
    print ("________________________")
    

f.close()
