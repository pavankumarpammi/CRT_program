from collections import deque
dq =deque()
# dq.append(15)
# dq.appendleft(10)
# dq.append(25)
# dq.appendleft(100)
# print(dq)
# dq.pop()
# print(dq)
# dq.popleft()
# print(dq)

#3 2 1 4 5 6
lis=[1,2,3,4,5,6]
k=3
for i in lis:
    dq.append(i)
low=0
high=k-1
while(low<k//2):
    dq[low],dq[high]=dq[high],dq[low]
    low+=1
print(dq)