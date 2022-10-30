# Python3 program to for tree traversals

# A class that represents an individual node in a
# Binary Tree

#[Tipo: palabraReservada ] [Valor: int ] [Número de Línea: 2 ] [Posición en texto: 44 ]
class tokenInfo:
    def __init__(self,name,type,value):
        self.name = name
        self.type = type
        self.value = value

class Node:
	def __init__(self,tokenInfo):
		self.left = None
		self.right = None
        #el tipo de datos, el ámbito de cada variable, valor de la constante, etc. 
		self.tokenInfo = tokenInfo


# A function to do inorder tree traversal
def printPreorder(root):

	if root:
		# then print the data of node
		print("name: ",root.tokenInfo.name,"type: ",root.tokenInfo.type,"value: ",root.tokenInfo.value)

		# First recur on left child
		printPreorder(root.left)

		# now recur on right child
		printPreorder(root.right)

def insert(root, tokenInfo):
	if root is None:
		return Node(tokenInfo)
	else:
		if root.tokenInfo.name == tokenInfo.name:
			return root
		elif root.tokenInfo.name < tokenInfo.name:
			root.right = insert(root.right, tokenInfo)
		else:
			root.left = insert(root.left, tokenInfo)
	return root

# Driver code
if __name__ == "__main__":
	#creando nodo root
	root = Node(tokenInfo("first","tipo1","0"))
	#insertando a root
	insert(root, tokenInfo("b","tipo2","0"))
	insert(root, tokenInfo("anho","tipo3","0"))
	insert(root, tokenInfo("companhia","tipo4","0"))
	insert(root, tokenInfo("m","tipo5","0"))
	insert(root, tokenInfo("forma","tipo6","0"))
	insert(root, tokenInfo("x3","tipo7","0"))

	# Function call
	print("\nInorder traversal of binary tree is")
	printPreorder(root)