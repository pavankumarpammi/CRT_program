#1,3,6,7,9,5,2
def peak(arr):
    low,high=1,len(arr)-1
    while(low<high):
        mid=low+(high-low)//2
        if(arr[mid]>arr[mid-1] and arr[mid+1]<arr[mid]):
            return arr[mid]
        elif(arr[mid]<arr[mid+1]):
            low+=1
        else:
            high-=1 
    return -1
lis=[1,3,6,7,9,5,2]
#lis=[1,3,6,7,9,10,11]
res=-1
val=peak(lis)
if(val!=res):
    print(val)
else:
    print(lis[len(lis)-1])

    

