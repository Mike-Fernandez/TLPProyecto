
# BST para organizar la tabla de Simbolos
# [Tipo: palabraReservada ] [Valor: int ] [Número de Línea: 2 ] [Posición en texto: 44 ]

#Informacion que se quiere guardar de los tokens
class tokenInfo:
    def __init__(self, order, tipo, value, lineno, lexpos):
        self.order = order
        self.type = tipo
        self.value = value
        self.lineno = lineno
        self.lexpos = lexpos

#Nodos del arbol
class Node:
    def __init__(self, tokenInfo):
        self.left = None
        self.right = None
    # el tipo de datos, el ámbito de cada variable, valor de la constante, etc.
        self.tokenInfo = tokenInfo

# Recorrido inorder
def printInorder(root):

    if root:
        printInorder(root.left)
        print("|order: ", root.tokenInfo.order, " | type: ", root.tokenInfo.type, " | value: ", root.tokenInfo.value," | line number: ", root.tokenInfo.lineno, " | lexer position: ", root.tokenInfo.lexpos)
        printInorder(root.right)

# Recorrido preorder
def printPreorder(root):

    if root:
        print("order: ", root.tokenInfo.order, "type: ", root.tokenInfo.type, "value: ", root.tokenInfo.value,"line number: ", root.tokenInfo.lineno, "lexer position: ", root.tokenInfo.lexpos)
        printPreorder(root.left)
        printPreorder(root.right)

# Imprimir la informacion de un nodo
def printNode(root):
    print("|order: ", root.tokenInfo.order, " | type: ", root.tokenInfo.type, " | value: ", root.tokenInfo.value," | line number: ", root.tokenInfo.lineno, " | lexer position: ", root.tokenInfo.lexpos)


#Insertar nodos al arbol
def insert(root, tokenInfo):
    if root is None:
        return Node(tokenInfo)
    else:
        if root.tokenInfo.order == tokenInfo.order:
            return root
        elif root.tokenInfo.order < tokenInfo.order:
            root.right = insert(root.right, tokenInfo)
        else:
            root.left = insert(root.left, tokenInfo)
    return root
