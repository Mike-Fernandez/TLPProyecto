# Python3 program to for tree traversals

# A class that represents an individual node in a
# Binary Tree

class tokenInfo:
    def __init__(self, name,type,value):
        self.name = name
        self.type = type
        self.value = value

class Node:
	def __init__(self, tokenInfo):
		self.left = None
		self.right = None
        #el tipo de datos, el ámbito de cada variable, valor de la constante, etc. 
		self.val = tokenInfo


# A function to do inorder tree traversal
def printPreorder(root):

	if root:
		# then print the data of node
		print(root.val),

		# First recur on left child
		printPreorder(root.left)

		# now recur on right child
		printPreorder(root.right)

def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val.name == key:
			return root
		elif root.val.name < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root

# Driver code
if __name__ == "__main__":
	#root = Node(1)
	#root.left = Node(2)
	#root.right = Node(3)
	#root.left.left = Node(4)
	#root.left.right = Node(5)
	r = Node(tokenInfo("first","tipo1","0"))
	r = insert(r, tokenInfo("b","tipo2","0"))
	r = insert(r, tokenInfo("anho","tipo3","0"))
	#r = insert(r, 40)
	#r = insert(r, 70)
	#r = insert(r, 60)
	#r = insert(r, 80)

	# Function call
	print("\nInorder traversal of binary tree is")
	printPreorder(r)
