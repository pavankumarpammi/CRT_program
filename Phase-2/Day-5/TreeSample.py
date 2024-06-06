class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Tree:
    def __init__(self):
        self.root=None
    def createTree(self,data):
        newNode=Node(data)
        if(self.root==None):
            root=newNode
        curr=root
        if curr.left==None:
            curr.right=Node(data)
        elif curr.right==None:
            curr.right=Node(data)
        elif curr.left!=None and curr.right!=None:
            print(None)
        print(curr.data)
    def display(self):
        temp=self.root
        temp1=self.root
        print("Left tree:")
        print(temp.data)
        while(temp!=None):
            print(temp.data,end="->")
            temp=temp.left
        while(temp1!=None):
            print(temp1.data,end="->")
            temp1=temp1.right
t=Tree()
lis=[1,2,3]
for i in lis:
    t.createTree(i)
t.display()


