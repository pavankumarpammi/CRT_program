class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head==None:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next!= None:
                curr = curr.next
            curr.next = Node(data)

    def printList(self):
        curr = self.head
        while curr.next!=None:
            print(curr.data,"->",end="")
            # if curr.next==None:
            #     break
            curr = curr.next

    def insertAtBegin(self,data):
        if(self.head==None):
            self.head=data
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
    def deleteRange(self,skip,start):
        curr=self.head
        count=0
        while(curr.next!=None and count<skip):
            curr=curr.next
            count+=1
        end=curr
        while(curr.next!=None and start!=0):
            curr=curr.next
            start-=1
        end.next=curr.next
        

print("Enter elements:")
lis=list(map(int,input().split()))
l=LinkedList()
for i in lis:
    l.insert(i)
print("Insert At endinning:")
l.printList()
print()
skip,start=map(int,input("Enter values:").split())
l.deleteRange(skip,start)
l.printList()