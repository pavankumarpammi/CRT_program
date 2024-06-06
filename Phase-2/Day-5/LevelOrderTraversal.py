from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.Checkinsert(self.root, data)

    def Checkinsert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.Checkinsert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.Checkinsert(node.right, data)
    def isempty(self,d):
        if len(d)<=0:
            return False
        return True
    def level_order_traversal(self):
        if self.root is None:
            return

        d = deque()
        d.append(self.root)

        while self.isempty(d):
            node = d.popleft()
            print(node.data,end=" ")

            if node.left!=None:
                d.append(node.left)

            if node.right!=None:
                d.append(node.right)
    def height_of_tree(self,root):
        curr=self.root
        if self.root is None:
            return 0
        lheight=self.height_of_tree(curr.left)
        rheight=self.height_of_tree(curr.right)
        return max(lheight,rheight)+1
t = Tree()
lis=list(map(int,input("Enter the values:").split()))
for i in lis:
    t.insert(i)
print(t.height_of_tree(t.root))
# t.insert(50)
# t.insert(30)
# t.insert(70)
# t.insert(20)
# t.insert(40)
# t.insert(60)
# t.insert(80)

#t.level_order_traversal()

