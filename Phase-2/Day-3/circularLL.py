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
            newNode=Node(data)
            curr.next = newNode
            newNode.next=curr


    def printList(self):
        curr = self.head
        temp =self.head
        while curr.next!=None:
            print(curr.data,"->",end="")
            if(curr==temp):
                break
            curr = curr.next

    def insertAtBegin(self,data):
        if(self.head==None):
            self.head=data
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        

print("Enter elements:")
lis=list(map(int,input().split()))
l=LinkedList()
for i in lis:
    l.insert(i)
print("Insert At endinning:")
l.printList()
print()
