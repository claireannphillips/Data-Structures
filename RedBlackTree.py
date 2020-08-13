import sys 
sys.setrecursionlimit(1000000)

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.parent = None
		self.key = key
		self.color = 'BLACK' 


class RedBlackTree:
	def __init__(self):
		self.root = None
		self.fakeNode = Node('fakeNode')
		self.fakeNode.left = self.root
		self.fakeNode.right = self.root
		self.fakeNode.parent = self.fakeNode

	def insert(self, z):
		#print('Starting insert on', z.key)
		y = None
		x= self.root
		while x != None:
			y = x
			if z.key < x.key:
				x = x.left
			else:
				x = x.right
		z.parent = y
		if y == None:
			self.root = z
			self.root.parent = self.fakeNode
			self.root.parent.left = self.root
			self.root.parent.right = self.root
		elif z.key < y.key:
			y.left = z
		else:
			y.right = z 
		z.left = None 
		z.right = None 
		z.color = 'RED' 
		self.RBfixup(z) 

	def left_rotate(self, x):
		#print('Starting left rotate on', x.key)
		#print(list(map(lambda x: x.key, self.to_list_inorder())))
		y = x.right
		x.right = y.left 
		if y.left != None:
			y.left.parent = x
		y.parent = x.parent
		if x.parent == self.fakeNode:
			self.root = y
			self.root.parent = self.fakeNode
			self.fakeNode.left = self.root
			self.fakeNode.right = self.root
		elif x==x.parent.left:
			x.parent.left = y
		else: 
			x.parent.right = y
		y.left = x
		x.parent = y
	
	def right_rotate(self, x):
		#print('Starting Right rotate on', x.key)
		#print(list(map(lambda x: x.key, self.to_list_inorder())))
		y = x.left
		x.left = y.right
		if y.right != None:
			y.right.parent = x
		y.parent = x.parent
		if x.parent == self.fakeNode:
			self.root = y
			self.root.parent = self.fakeNode
			self.fakeNode.left = self.root
			self.fakeNode.right = self.root
		elif x==x.parent.right:
			x.parent.right = y
		else: 
			x.parent.left = y
		y.right = x
		x.parent = y
		#print(list(map(lambda x: x.key, self.to_list_inorder())))



	def RBfixup(self, z):
		while z.parent.color == 'RED':
			if z.parent == z.parent.parent.left:
				y = z.parent.parent.right
				if y != None and y.color == 'RED': #added y!=None 
					z.parent.color = 'BLACK' 
					y.color = 'BLACK' 
					z.parent.parent.color = 'RED' 

				else: 
					if z == z.parent.right:
						z = z.parent 
						self.left_rotate(z) #left rotate on 2
					z.parent.color = 'BLACK' 
					z.parent.parent.color = 'RED' 
					self.right_rotate(z.parent.parent)
			else:
				y = z.parent.parent.left

				if y is not None and y.color == 'RED':

					z.parent.color = 'BLACK' 
					y.color = 'BLACK' 
					z.parent.parent.color = 'RED' 
					z = z.parent.parent

				else:
					if z == z.parent.left:
						z = z.parent 
						self.right_rotate(z)
					z.parent.color = 'BLACK' 
					z.parent.parent.color = 'RED' 
					self.left_rotate(z.parent.parent)
		self.root.color = 'BLACK' 

	def RB_transplant(self, u, v):
		if u.parent == self.fakeNode:
			self.root = v
			v.parent = self.fakeNode
			self.fakeNode.left = v 
			self.fakeNode.right = v
		elif u == u.parent.left:
			u.parent.left = v
		else: 
			u.parent.right = v
		if v != None:
			v.parent = u.parent 

	def search(self, x, k):
		while x != None and k != x.key:
			if k < x.key:
				x = x.left
			else:
				x = x.right
		return x

	def remove(self, z):
		y =z
		yoriginalcolor = y.color
		if z.left == None:
			x = z.right
			self.RB_transplant(z, z.right)
		elif z.right == None:
			x = z.left
			self.RB_transplant(z, z.left)
		else: 
			y = self.min(z.right)
			yoriginalcolor = y.color
			x = y.right
			if y.parent == z and x != None:
				x.parent = y
			else: 
				#print(y.key)
				#print(y.right.key)
				self.RB_transplant(y, y.right)
				y.right = z.right
				if y.right != None:
					y.right.parent = y
			self.RB_transplant(z, y)
			y.left = z.left
			y.left.parent = y
			y.color = z.color
		if yoriginalcolor == 'BLACK':
			self.RB_delete_fixup(x)

	def RB_delete_fixup(self, x):
		while x != None and x != self.fakeNode and x != self.root and x.color == 'BLACK' :
			if x == x.parent.left:
				w = x.parent.right
				if w.color == 'RED':
					w.color = 'BLACK'
					x.parent.color = 'RED'
					self.left_rotate(x.parent)
					w = x.parent.right
				if w.left.color == 'BLACK' and w.right.color == 'BLACK':
					w.color = 'RED' 
					x = x.parent
				elif w.right.color == 'BLACK':
					w.left.color = 'BLACK'
					w.color = 'RED' 
					self.right_rotate(w)
					w = x.parent.right
				w.color = x.parent.color
				x.parent.color = 'BLACK' 
				w.right.color = 'BLACK'
				self.left_rotate(x.parent)
		if x != None:	
			x.color = 'BLACK'

	def list_inorder(self, x, A):
		if x.left != None:
			self.list_inorder(x.left, A)
		A.append(x)
		if x.right != None:
			self.list_inorder(x.right, A)

	def to_list_inorder(self): 
		A = []
		if self.root != None:
			self.list_inorder(self.root, A)
		return A

	def max(self, x): 
		while x.right != None:
			x = x.right
		return x

	def min(self, x): 
		while x.left != None:
			x = x.left
		return x

def driver():
	h = RedBlackTree()
	with open(sys.argv[1]) as f:
		x = int(f.readline().strip()) #number of commands 
		#count = 0
		for i in range (x):
			l1 = f.readline().strip().split()
			if l1[0] == "insert":
				#print("INSERTING: ", l1[1])
				h.insert(Node(int(l1[1]))) #actual data in the string
			elif l1[0] == "remove":
				#print("REMOVING: ", l1[1])
				toremove = h.search(h.root, int(l1[1]))
				#print(toremove.key)
				if  toremove != None:
					#print(toremove.key)
					h.remove(toremove)
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

if __name__ == "__main__":
    driver()

