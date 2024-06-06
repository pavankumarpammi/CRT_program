class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
head=None
def insert(data):
    if head==None:
        newNode=Node(data)
        head =newNode
    else:
        curr = head
        while curr.next !=None:
            curr = curr.next
        newNode=Node(data)
        curr.next = newNode

def insertAtEnd(data):
    if(head==None):
        head=Node(data)
    temp=head
    while(temp.next!=None):
        temp=temp.next
    newNode=Node(data)
    temp.next=newNode

def printList():
    curr = head
    while curr!=None:
        print(curr.data,end="")
        curr = curr.next
        if curr.next==None:
            break
        else:
            print(end="->")
        

def reverseKnodes(self,head):
    curr=self.head
    prev=None
    nextptr=None
    
print("Enter elements:")
lis=list(map(int,input().split()))

for i in lis:
    insert(i)

print("Insert At endinning:")
printList()

print()
# reverseKnodes(3,None,None,0)
printList()



        
        

