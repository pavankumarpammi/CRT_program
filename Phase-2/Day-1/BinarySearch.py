# def binarySearch(arr,t)->int:
#     low,high =0,len(arr)-1
#     while(low<=high):
#         mid=low+(high-low)//2
#         if(t==arr[mid]):
#             return mid
#         elif(t<arr[mid]):
#             high-=1
#         else:
#             low+=1
#     return -1

# lis=list(map(int,input().split()))
# target=int(input("Enter the value of target:"))
# print(binarySearch(lis,target))
#1 4 4 4 9 13 15 15 using binary search find the first and last occurrence 4 and 15