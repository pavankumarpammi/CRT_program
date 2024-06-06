#link the four node display all of them in a funtion we has pass the head to funtion 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insert(head,data):
   head=None
   for i in lis:
        if head==None:
            head=Node(i)
        temp=head
        newNode=Node(i)
        while(temp.next!=None):
            temp=temp.next
        temp.next=newNode
    
def display(node):
    if(node==None):
        print("List is empty")
    #node=head
    while(node!=None):
        print(node.data,"->",end="")
        node=node.next

lis=list(map(int,input().split()))
head=Node(lis[0])
for i in range(1,len(lis)):
    insert(head,i)
display(head)
        