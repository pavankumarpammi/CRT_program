def firstoccurenc(arr,mid):
        low=mid
        while(low>0 and arr[mid]==arr[low-1] ):
            low-=1
        return low
def lastoccurenc(arr,mid):
        high=mid
        while(high<len(arr)-1 and arr[mid]==arr[high+1]):
            # if(high+1<=len(arr)-1):
            high+=1
        return high
def firstAndLast(arr,target):
    low=0
    high=len(arr)-1
    
    while(low<=high):
        mid=low+(high-low)//2
        if(arr[mid]==target):
            return mid
        elif(target<arr[mid]):
            high-=1
        else:
            low+=1

lis=[1,4,4,4,9,13,15,15]
t=15
mid=firstAndLast(lis,t)
# print(mid)
first=-1
last=-1
if(mid==0):
     first=0
     last=lastoccurenc(lis,mid)
     print(first, last)
elif(mid==len(lis)-1):
     last=mid
     first=firstoccurenc(lis,mid)
     print(first,last)
     print("condition 2")
else:
    print(firstoccurenc(lis,mid))
    print(lastoccurenc(lis,mid))

