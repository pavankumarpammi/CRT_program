class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
lis=list(map(int,input().split()))
for i in lis:
    if head==None:
        head=Node(i)
    temp=head
    newNode=Node(i)
    while(temp.next!=None):
        temp=temp.next
    temp.next=newNode
curr=head
while(curr!=None):
    print(curr.data,"->",end="")
    curr=curr.next
    


    
