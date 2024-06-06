def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return lis
lis=list(map(int,input().split()))
print(mergeSort(lis))

# def mergeSort(arr):
#     if arr>=1:
#         mid=len(arr)//2
#         L=mergeSort(arr[:mid])
#         R=mergeSort(arr[mid:])
#         i=j=0
#         res=[None]*(len(L)+len(R))
#         for k in range(len(res)):
#             if i==len(L):
#                 res[k]=R[j]
#                 j+=1
#             elif j==len(R):
#                 res[k]=L[i]
#                 i+=1
#             elif L[i]<R[j]:
#                 res[k]=L[i]
#                 i+=1
#             else:
#                 res[k]=R[j]
#                 j+=1
#         return res
#     else:
#         return [arr]
# print(mergeSort([3,6,8,10,1,2,1]))