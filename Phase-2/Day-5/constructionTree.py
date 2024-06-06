from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Tree:
    def __init__(self):
        self.root=None
        self.orgRoot=None
    def insert(self,root,key):
        if root is None:
            self.orgRoot=Node(key)
            return Node(key)
        if key<root.data:
            root.left=self.insert(root.left,key)
        elif key>=root.data:
            root.right=self.insert(root.right,key)
        return root
    def inorderTraversal(self,root):
        res=[]
        if root in None:
            return 
        self.inorderTraversal(root.left)
        print(root.data)
        self.inorderTraversal(root.right)
    
lis=[5,2,5,3,99]
t=Tree()
for i in lis:
    t.insert(t.orgRoot,i)
t.inorderTraversal(t.orgRoot)

#in order -> 20 30 40 50 60 70 90
#preorder -> 50 30 20 40 70 60 90
#postOrder-> 20 40 30 60 90 70 50
#levelorder->50 30 70 20 40 60 90