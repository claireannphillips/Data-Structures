
import sys
import copy
sys.setrecursionlimit(11000000)
#linked list class


# custom Underflow exception
class Underflow(Exception):
    pass  


class SingleLL(object):
    class LLNode(object):
        def __init__(self, data=None):
            self.data= data
            self.next= None
           

    def __init__(self):
        self.size= 0
        self.head= None
        self.tail= None
    def __len__(self):
        return self.size
    def search(self, key):
        x = self.head
        while x != None and x.data!= key:
            x = x.next
        return x 
    def insert(self, x):
        if self.size == 0:
            #base case if it's zero
            node = self.LLNode(x)
            self.size = self.size + 1 
            self.head= node
            self.tail = node
        elif self.size >= 1:
            node = self.LLNode(x)
            self.tail.next = node
            self.size = self.size + 1 
            self.tail = node

    def delete(self, x):
        y = self.head
        while y != None and y.next!= x:
            y = y.next
        if y != None:
            y.next= x.next
            self.size-= 1
    def deleteHead(self):
        if self.head == None:
            raise Underflow
        else:
            result = self.head.data
            self.head = self.head.next
        if self.head == None:
            self.tail = None
            self.size = 0
        return result



class Queue:

    # class constructor
    def __init__(self):
        self.ll = SingleLL()
        return

    # push method
    def enqueue(self, x):
        return self.ll.insert(x)

    # pop method
    def dequeue(self):
        return self.ll.deleteHead()

    # is_empty method
    def is_empty(self):
        x = self.ll.head
        return x == None



# TODO: implement the print function
# args: s, Stack
def print_queue(q):
    # only use s.push, s.pop, and s.is_empty
    t = []
    if q.is_empty() == False:
        while not q.is_empty():
            t.append(q.dequeue())
        tque = map(str, t)
        print(' '.join(tque))
        t.reverse()
        while t:
            q.enqueue(t.pop())
    else:
        print("Empty")
 

    return None



def driver():
    q = Queue()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "enqueue":
                value = int(value_option[0])
                q.enqueue(value)  
            elif action == "dequeue":
                try:
                    print(q.dequeue())
                except Underflow:
                    print("QueueError")

            elif action == "print":
                print_queue(q)



# this starter code should work with either python or python3
if __name__ == "__main__":
    driver()
    
