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
        while curr!=None:
            print(curr.data,end="")
            if curr.next==None:
                break
            else:
                print("->",end="")
            curr = curr.next

    def sortLinkedList(self):
        self.count0=0
        self.count1=0
        self.count2=0
        curr=self.head
        while(curr!=None):
            if(curr.data==0):
                self.count0+=1
            elif(curr.data==1):
                self.count1+=1
            else:
                self.count2+=1
            curr=curr.next
        #print(self.count0,self.count1,self.count2)
    def reCreateList(self):
        newNode=Node(0)
        self.head=newNode
        curr=self.head
        while(self.count0!=1): 
            while curr.next!= None:
                curr = curr.next
            curr.next = Node(0)
            self.count0-=1
        while(self.count1!=0): 
            while curr.next!= None:
                curr = curr.next
            curr.next = Node(1)
            self.count1-=1
        while(self.count2!=0):
            while curr.next!= None:
                curr = curr.next
            curr.next = Node(2)
            self.count2-=1


lis=[2,1,2,2,0,1,2,0,0,1,1]
l=LinkedList()
# for i in lis:
#     l.insertAtBegin(i)
    
for i in lis:
    l.insert(i)
# print("Insert from Beginning:")
# l.printList()
print(lis)
print()
print("Insert At endinning:")
l.printList()
print()
l.sortLinkedList()
l.reCreateList()
print()
l.printList()