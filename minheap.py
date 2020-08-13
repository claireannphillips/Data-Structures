
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


def driver():
	h = MinHeap()
	with open(sys.argv[1]) as f:
		x = int(f.readline().strip()) #number of commands 
		#count = 0
		for i in range (x):
			l1 = f.readline().strip().split()
			#count += 1
			if l1[0] == "insert":
				#print(l1)
				#print(count)
				h.insert(int(l1[1])) #actual data in the string
			elif l1[0] == "remove":
				print(h.remove())
			elif l1[0] == "print":
				print(h.to_string())
			elif l1[0] == "size":
				print(h.size())
			elif l1[0] == "best":
				print(h.look())




if __name__ == "__main__":
    driver()
