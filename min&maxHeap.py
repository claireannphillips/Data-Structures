import sys
sys.setrecursionlimit(100000000)
class MinHeap:
	def __init__(self):
		self.a = []
	def insert(self, x): 
		self.a.append(x) #adds to back of list so adds to end for us to heapify bottom up
		self.minheapifyup(self.size()-1) # last element of size

	def remove(self): #to delete had to heapify down 
		root = self.look()
		if root != "HeapError":
			var = self.a.pop()
			if self.size() > 0:
				self.a[0] = var #overwrite old root 
				self.minheapify(0) #give it the root 
		return root

	def look(self):
		if self.size() > 0:
			return self.a[0]
		return "HeapError"
	def size(self):
		return len(self.a)
	def is_empty(self):
		if self.size() == 0:
			return True 
		return False 
	def to_string(self):
		if self.is_empty():
			return "Empty"
		s = ""
		for i in range (self.size()):
			s += str(self.a[i])
			if i != self.size() -1: #not on the last thing
				s += " "
		return s


	def minheapify(self, i):
		l = self.left(i)
		r = self.right(i)
		smallest = i
		if l < self.size() and self.a[l] < self.a[i]:
			smallest = l
		if r < self.size() and self.a[r] < self.a[smallest]:
			smallest = r
		if smallest != i:
			temp = self.a[i]
			self.a[i] = self.a[smallest]
			self.a[smallest] = temp
			self.minheapify(smallest)

	def minheapifyup(self, i):
		p = self.parent(i)
		if self.a[i] < self.a[p]:
			temp = self.a[i]
			self.a[i] = self.a[p]
			self.a[p] = temp
			self.minheapifyup(p)



	def parent(self, i):
		if i == 0:
			return 0
		return ((i-1)//2)
	def left(self, i):
		return (2*i + 1)
	def right(self, i):
		return (2*i+2)
class MaxHeap:
	def __init__(self):
		self.a = []
	def insert(self, x): 
		self.a.append(x) #adds to back of list so adds to end for us to heapify bottom up
		self.maxheapifyup(self.size()-1) # last element of size

	def remove(self): #to delete had to heapify down 
		root = self.look()
		if root != "HeapError":
			var = self.a.pop()
			if self.size() > 0:
				self.a[0] = var #overwrite old root 
				self.maxheapify(0) #give it the root 
		return root

	def look(self):
		if self.size() > 0:
			return self.a[0]
		return "HeapError"
	def size(self):
		return len(self.a)
	def is_empty(self):
		if self.size() == 0:
			return True 
		return False 
	def to_string(self):
		if self.is_empty():
			return "Empty"
		s = ""
		for i in range (self.size()):
			s += str(self.a[i])
			if i != self.size() -1: #not on the last thing
				s += " "
		return s


	def maxheapify(self, i):
		l = self.left(i)
		r = self.right(i)
		largest = i
		if l < self.size() and self.a[l] > self.a[i]:
			largest = l
		if r < self.size() and self.a[r] > self.a[largest]:
			largest = r
		if largest != i:
			temp = self.a[i]
			self.a[i] = self.a[largest]
			self.a[largest] = temp
			self.maxheapify(largest)

	def maxheapifyup(self, i):
		p = self.parent(i)
		if self.a[i] > self.a[p]:
			temp = self.a[i]
			self.a[i] = self.a[p]
			self.a[p] = temp
			self.maxheapifyup(p)



	def parent(self, i):
		if i == 0:
			return 0
		return ((i-1)//2)
	def left(self, i):
		return (2*i + 1)
	def right(self, i):
		return (2*i+2)


#h = Median()
def Median():
	with open(sys.argv[1]) as f:
		x = int(f.readline().strip()) #number of commands 
		minh = MinHeap()
		maxh = MaxHeap()
		for i in range (x):
			l1 = int(f.readline().strip())
			if maxh.size() == 0:
				maxh.insert(l1)
			else:
				if l1 < maxh.look(): #larger values go in min heap 
					maxh.insert(l1)
				else:
					minh.insert(l1)
				diff = maxh.size()-minh.size()
				if diff > 1:
					minh.insert(maxh.remove()) #because want value in other tree
				elif diff < -1:
					maxh.insert(minh.remove())
			if maxh.size() > minh.size():
				med = maxh.look()
			elif minh.size() > maxh.size():
				med = minh.look()
			else:
				med = (minh.look() + maxh.look())/2
			print (med)

if __name__ == "__main__":
	Median()


