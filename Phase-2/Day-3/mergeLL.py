class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head1 = None
        self.head2 = None 
        self.head3 = None

    def insert1(self, data):
        if self.head1==None:
            self.head1 = Node(data)
        else:
            curr = self.head1
            while curr.next!= None:
                curr = curr.next
            curr.next = Node(data)
    def insert2(self, data):
        if self.head2==None:
            self.head2 = Node(data)
        else:
            curr = self.head2
            while curr.next!= None:
                curr = curr.next
            curr.next = Node(data)

    def printList1(self):
        curr = self.head1
        while curr!=None:
            print(curr.data,end="")
            if curr.next==None:
                break
            else:
                print("->",end="")
            curr = curr.next
    def printList2(self):
        curr = self.head2
        while curr!=None:
            print(curr.data,end="")
            if curr.next==None:
                break
            else:
                print("->",end="")
            curr = curr.next
    def sortList(self):
        curr1=self.head1
        curr2=self.head2
        while(curr1!=None and curr2!=None):
            if(curr1.data>curr2.data):
                newNode=Node(curr2)
                newNode.next=curr1.next
                curr1.next=newNode
                
            elif(curr2.data>curr1.data):
                newNode=Node(curr1)
                newNode.next=curr1.next
                curr1.next=newNode
            curr1=curr1.next
            curr2=curr2.next
    
    def mergeTwoLists(self):
        l1=self.head1
        l2=self.head2

        if l1.data < l2.data:
            self.head3 = l1
            l1 = l1.next
        else:
            self.head3 = l2
            l2 = l2.next

        current = self.head3
        while l1 is not None and l2 is not None:
            if l1.data < l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1 is not None:
            current.next = l1

        if l2 is not None:
            current.next = l2

    def merge(self):
        self.head3=Node(-1)
        curr1=self.head1
        curr2=self.head2
        curr3=self.head3
        while(curr1.next!=None and curr2.next!=None):
            if(curr1.data>curr2.data):
                newNode=Node(curr2.data)
                newNode.next=Node(curr1.data)
                while(curr3.next!=None):
                    curr3=curr3.next
                curr3.next=newNode
            else:
                newNode=Node(curr1.data)
                newNode.next=Node(curr2.data)
                while(curr3.next!=None):
                    curr3=curr3.next
                curr3.next=newNode
    def printListRes(self):
        curr = self.head3
        while curr!=None:
            print(curr.data,end="")
            if curr.next==None:
                break
            else:
                print("->",end="")
            curr = curr.next
    

lis=[11,22,33]
lis1=[12,21,34]
l=LinkedList()
for i in lis1:
    l.insert2(i)
    
for i in lis:
    l.insert1(i)

print()
print("Insert At endinning:")
l.printList1()
print()
print()
l.printList2()
print()
# l.mergeTwoLists()
print()
l.printListRes()
#MERGE TO UNSORTED LINKEDLIST
#create a duo