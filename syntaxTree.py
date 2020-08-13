import sys
sys.setrecursionlimit(1000000)
class STNode:

    def __init__(self, x: str):
        self.key = x
        self.left = None
        self.right = None


class SyntaxTree:

    def init_helper(self, i: int, l):
        if i >= len(l):
            return None

        node = STNode(l[i])
        node.left = self.init_helper(2 * i + 1, l)
        node.right = self.init_helper(2 * i + 2, l)
        return node

    def __init__(self, l):
        self.root = self.init_helper(0, l)
    
    def __str__(self):
        #call some inorder traversal function
        
        result_list = self.to_list_inorder()
        return ''.join(result_list)

    def inorder(self, x, A):
        if x.left != None:
            A.append("(")
            self.inorder(x.left, A)
        #print(x.key)
        A.append(x.key)


        if x.right != None:
            self.inorder(x.right, A)
            A.append(")")

        #A.append(x.key)
        #print(A)
        #if x.left != None:
            #self.list_inorder(x.left, A)
        #A.append(x.key)
        #if x.right != None:
            #self.list_inorder(x.right, A)

    def to_list_inorder(self):
        A = []
        if self.root != None:
            self.inorder(self.root, A)
        return A

    def postorder_result(self):
        if self.root != None:
            return self.postorder_helper(self.root)
                

    def postorder_helper(self, x):
        if x.key == '*':
            return self.postorder_helper(x.left) * self.postorder_helper(x.right)
        if x.key == '+':
            return self.postorder_helper(x.left) + self.postorder_helper(x.right)
        if x.key == '-':
            return self.postorder_helper(x.left) - self.postorder_helper(x.right)
        return int(x.key)

def driver():
    with open(sys.argv[1]) as f:
        x = int(f.readline().strip()) #number of commands 
        symbol_list = f.readline().strip().split()
        syntax_tree = SyntaxTree(symbol_list)
        print(syntax_tree) #does the parenthesis 
        print(syntax_tree.postorder_result())
        #print(syntax_tree.evaluate()) #evaluates 


if __name__ == "__main__":
    driver()
