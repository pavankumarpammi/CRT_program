class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertAtEnd(self,data):
        if(self.head==None):
            self.head=Node(data)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        newNode=Node(data)
        temp.next=newNode
    def printList(self):
        curr=self.head
        while(curr!=None):
            curr=curr.next
            print(curr.data,end="")
            if(curr.next==None):
                break
            else:
                print(end="->")
    def count(self):
        temp=self.head
        count=0
        while(temp!=None):
             temp=temp.next
             count+=1
        return count-1
    def printMiddleElement(self):
        curr=self.head
        val=(l.count())//2
        c=0
        while(curr.next!=None):
            c+=1
            if(c==val//2):
                return curr.data
            curr=curr.next
    def delete(self,data):
        #prev=None
        nextNode=None
        curr=self.head
        while(curr!=None):
            if(curr.next.data==data):
                 
                break
            curr=curr.next
        curr.next=curr.next.next
    def reverse(self):
        curr=self.head
        prev=None
        nextptr=None
        while(curr!=None):
            nextptr=curr.next
            curr.next=prev
            prev=curr
            curr=nextptr
        self.head=prev
l=LinkedList()
lis=list(map(int,input().split()))
for i in lis:
    l.insertAtEnd(i)
l.printList()
print()
# print("Number of element in linkedlist:",l.count())
# print()
# print("middle element:",l.printMiddleElement())
# n=int(input("Element to be deleted:"))
# l.delete(n)
# print()
# l.printList()
print()
l.reverse()
l.printList()
    
#count no of elements in linked lis and print middle element