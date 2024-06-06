class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoubleList:
    def __init__(self):
        self.head=None
    def insertAtEnd(self,data):
        if self.head==None:
            newNode=Node(data)
            self.head=newNode
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            newNode=Node(data)
            curr.next=newNode
            newNode.prev=curr

    def printList(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end="")
            if(curr.next==None):
                break
            else:
                print(end="->")
            curr=curr.next
    def printReverse(self):
        curr=self.head
        while(curr.next!= None ):
            curr = curr.next
        while(curr.prev!=None):
            print(curr.data,end="->")
            curr=curr.prev
            if(curr.prev == None):
                print(curr.data)
                break
    def insertAtBegin(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
    def deleteNode(self,data):
        curr=self.head

        while(curr!=None and curr.data!=data):
            if(curr.next==data):
                break
            curr=curr.next
        if curr.prev !=None:
            curr.prev.next = curr.next
        else:
            self.head = curr.next

        if curr.next !=None:
            curr.next.prev = curr.prev
        
d=DoubleList()
lis=list(map(int,input().split()))
for i in lis:
    d.insertAtEnd(i)
d.printList()
print()
d.printReverse()
n=int(input("enter element to insert at begin:"))
d.insertAtBegin(n)
d.printList()
print()
n=int(input("enter value to delete:"))
d.deleteNode(n)
d.printList()