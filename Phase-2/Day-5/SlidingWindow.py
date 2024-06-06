# -4 -2  3 -5 -6 1
# i-d[0]>=w : d.popleft()
from  collections import deque
def find_first_negative(lis, w):
    n = len(lis)
    d = deque()

    for i in range(w):
        if lis[i] < 0:
            d.append(i)

    for i in range(w,n):
        if not d:
            print(0)
        else:
            print(lis[d[0]])
    while(d and i-d[0]>=w):
        d.popleft()
    if lis[i]<0:
        d.append(i)
    
# Test the function
lis = [-4, -2, 3, -5, -6, 1]
w = 3
print(find_first_negative(lis, w))  # Output: -5