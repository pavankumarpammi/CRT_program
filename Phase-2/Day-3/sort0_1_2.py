# 2,1,2,2,0,1,2,0,0,1,1  output 0 0 0 1 1 1 1 2 2 2 2
# lis=[2,1,2,2,0,1,2,0,0,1,1]
# count0=count1=count2=0
# print(lis)
# for i in lis:
#     if i==0:
#         count0+=1
#     elif i==1:
#         count1+=1
#     else:
#         count2+=1
# print()
# for i in range(0,count0):
#     lis[i]=0
# for j in range(count0,count1+count0):
#     lis[j]=1
# for k in range(count1+count0,count0+count1+count2):
#     lis[k]=2
# print(lis)

##optimal approach
def swap(arr,a,b):
    temp=arr[a]
    arr[b]=arr[a]
    arr[a]=temp
def sort_0_1_2(arr):
    low=0
    mid=0
    high=len(arr)-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
lis=[2,1,2,2,0,1,2,0,0,1,1]
print("Original List",lis)
print()
print(sort_0_1_2(lis))
