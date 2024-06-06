#1 2 3 4 5 6
#A tree is called as self balanced tree or a balanced tree 
#if the absolute difference between the left and right_height should be less than or equal to 1
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
    
    def left_height(self):
        if self.root==None:
            return 
        temp=self.root
        while temp.left!=None:
            temp=temp.left
            cnt+=1
        return cnt
    def right_height(self):
        if self.root==None:
            return 
        temp=self.root
        while temp.right!=None:
            temp=temp.right
            cnt+=1
        return cnt
    def height(self):
        if self.root is None:
            return 0
        else:
            return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return max(left_height, right_height) + 1
        
    def  checkbalance(self):
        left=self.left_height()
        right=self.right_height()
        if abs(left-right)<=1:
            return True
        else:
            return False
    def balance_tree(self,root):
        if root is None:
            return True
        self.balance_tree(root.left)
        self.balance_tree(root.right)
        lt=self.height(root.left)
        rt=self.height(root.right)
        bal=abs(lt-rt)
    def lca(self,root,n1,n2):
        if root is None:
            return
        if n1<root.data and n2<root.data:
            self.lca(root.left,n1,n2)
        elif n1>root.data and n2>root.data:
            self.lca(root.right,n1,n2)
        else:
            return root.data

t = Tree()
lis=list(map(int,input("Enter the values:").split()))
for i in lis:
    t.insert(i)
print(t.height())
#t.level_order_traversal()

