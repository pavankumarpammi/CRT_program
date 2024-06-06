#implement a stack using a linkedlist
#create a funtion push inserting to linkedlis funtion pop 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedListByStack:
    def __init__(self):
        self.head=None
        self.top=None
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
            self.top=self.head
        curr=self.head
        new_node=Node(data)
        while(curr.next!=None):
            curr=curr.next
        curr.next=new_node
        self.top=new_node
    def pop(self):
        if self.isempty():
            return "Underflow"
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            data=temp.data
            temp.next=None
            return data
    def isempty(self):
        return (self.head==None)
    def  peek(self):
        if self.isempty():
           return ("No element in the Stack")
        else :
            return self.top.data
        
s1=LinkedListByStack()
lis=[1,2,3,4,5]
for i in lis:
    s1.push(i)
for i in range(len(lis)):
    print(s1.pop())

