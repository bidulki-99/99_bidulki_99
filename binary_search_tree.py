class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        global height
        self.cur = self.root

        while True:
            if value < self.cur.value:
                if self.cur.left == None:
                    self.cur.left = Node(value)
                    break
                else:
                    self.cur = self.cur.left
            else:
                if self.cur.right == None:
                    self.cur.right = Node(value)
                    break
                else:
                    self.cur = self.cur.right
            
bst = BST(Node(int(input())))
