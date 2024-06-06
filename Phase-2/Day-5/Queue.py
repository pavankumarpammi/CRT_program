#list of integer -8 2 3 -6 10 for every two element find element
#slove using queues
from collections import deque
d=deque()
res=deque()
lis=[-8,2,3,-6,10]
for i in lis:
    d.append(i)
def findVal(d,k):
    pass
for i in range(0,len(lis)-1):
    if(len(d)>0):
        val1=d.popleft()
        if len(d)>0:
            val2=d.popleft()
        d.appendleft(val2)
        if val1<0:
            res.append(val1)
        elif val2<0:
            res.append(val2)
        else:
            res.append(0)
    
    print(val1," ",val2)
print(res)

