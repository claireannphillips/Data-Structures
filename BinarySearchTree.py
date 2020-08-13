import sys
sys.setrecursionlimit(1000000)

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.parent = None
		self.key = key


class BinarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, x):
		y = None
		m = self.root
		while m != None:
			y = m
			if x.key < m.key:
				m = m.left
			else:
				m = m.right
		x.parent = y
		if y == None:
			self.root = x #tree empty 
		elif x.key < y.key:
			y.left = x
		else:
			y.right = x
	
	def transplant(self, u, v):
		if u.parent == None:
			self.root = v
		elif u == u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		if v != None:
			v.parent = u.parent


	def remove(self, x): 
		if x == None:
			self.transplant(x, x.right)
		elif x.right == None:
			self.transplant(x, x.left)
		else:
			y = self.min(x.right)
			if y.parent != x:
				self.transplant(y, y.right)
				y.right = x.right
				y.right.parent = y
			self.transplant(x, y)
			y.left = x.left
			if y.left != None:
				y.left.parent = y
		return x


	def search(self, x, k):
		while x != None and k != x.key:
			if k < x.key:
				x = x.left
			else:
				x = x.right
		return x

	def max(self, x): 
		while x.right != None:
			x = x.right
		return x

	def min(self, x): 
		while x.left != None:
			x = x.left
		return x

	def successor(self, x):
		if x.right != None:
			return min(x.right)
		y = x.parent
		while y != None and x == y.right:
			x = y
			y = y.parent
		return y
	def list_preorder(self, x, A):
		A.append(x)
		if x.left != None:
			self.list_preorder(x.left, A)
		if x.right != None:
			self.list_preorder(x.right, A)

	def list_inorder(self, x, A):
		if x.left != None:
			self.list_inorder(x.left, A)
		A.append(x)
		if x.right != None:
			self.list_inorder(x.right, A)

	def list_postorder(self, x, A):
		if x.left != None:
			self.list_postorder(x.left, A)
		if x.right != None:
			self.list_postorder(x.right, A)
		A.append(x)			

	def to_list_preorder(self): #shoulnd't have x
		A = []
		if self.root != None:
			self.list_preorder(self.root, A)
		return A

	def to_list_inorder(self): #shoulnd't have x
		A = []
		if self.root != None:
			self.list_inorder(self.root, A)
		return A

	def to_list_postorder(self): #shouldn't have x 
		A = []
		if self.root != None:
			self.list_postorder(self.root, A)
		return A

def driver():
	h = BinarySearchTree()
	with open(sys.argv[1]) as f:
		x = int(f.readline().strip()) #number of commands 
		#count = 0
		for i in range (x):
			l1 = f.readline().strip().split()
			if l1[0] == "insert":
				h.insert(Node(int(l1[1]))) #actual data in the string
			elif l1[0] == "remove":
				toremove = h.search(h.root, int(l1[1]))
				if  toremove != None:
					h.remove(toremove).key
				else:
					print("TreeError")
			elif l1[0] == "max":
				if h.root != None:
					print(h.max(h.root).key)
				else:
					print("Empty")
			elif l1[0] == "min":
				if h.root != None:
					print(h.min(h.root).key)
				else:
					print("Empty")
				
			elif l1[0] == "search":
				if h.search(h.root, int(l1[1])) != None:
					print("Found")
				else:
					print("NotFound")
			elif l1[0] == "inprint":
				inorderlist = h.to_list_inorder()
				inorderlist = [str(x.key)for x in inorderlist]
				if len(inorderlist) == 0:
					print("Empty")
				else:
					print(' '.join(inorderlist))
				#inorderlist = h.to_list_inorder() 
				#for i in range (len(inorderlist)):
					#print(inorderlist[i].key)
			elif l1[0] == "preprint":
				#preorderlist = h.to_list_preorder() 
				#for i in range (len(inorderlist)):
					#print(preorderlist[i].key)
				preorderlist = h.to_list_preorder()
				preorderlist = [str(x.key)for x in preorderlist]
				if len(preorderlist) == 0:
					print("Empty")
				else:
					print(' '.join(preorderlist))
			elif l1[0] == "postprint":
				postorderlist = h.to_list_postorder()
				postorderlist = [str(x.key)for x in postorderlist]
				if len(postorderlist) == 0:
					print("Empty")
				else:
					print(' '.join(postorderlist))
				#print(h.to_list_postorder())
				#postorderlist = h.to_list_postorder() 
				#for i in range (len(postorderlist)):
					#print(postorderlist[i].key)

if __name__ == "__main__":
    driver()
