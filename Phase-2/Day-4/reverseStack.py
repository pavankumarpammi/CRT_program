lis=[1,2,3,4,5]
stack=[]
def push(lis):
    for i in lis:
        stack.append(i)
def isempty(s):
    if(len(s)==0):
        return  True
    else:
        return False
def top(s):
    return len(s)-1
def reverse(l):
    mid =top(l)//2
    high=top(l)
    i=0
    while i<mid:
        l[i],l[high]=l[high],l[i]
        i+=1
        high-=1
    return l

push(lis)
print(lis)
reverse(lis)
print(lis)

#valid parthensis 