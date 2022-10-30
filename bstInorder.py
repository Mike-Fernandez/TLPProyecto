# Python3 program to for tree traversals

# A class that represents an individual node in a
# Binary Tree

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
	#root = Node(1)
	#root.left = Node(2)
	#root.right = Node(3)
	#root.left.left = Node(4)
	#root.left.right = Node(5)
	#r = Node(tokenInfo("first","tipo1","0"))
	root = Node(tokenInfo("first","tipo1","0"))
	insert(root, tokenInfo("b","tipo2","0"))
	insert(root, tokenInfo("anho","tipo3","0"))
	#r = insert(r, 40)
	#r = insert(r, 70)
	#r = insert(r, 60)
	#r = insert(r, 80)

	# Function call
	print("\nInorder traversal of binary tree is")
	printPreorder(root)
