def dubbbleSort(lis):
    n=len(lis)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if lis[j]>lis[j+1]:
                temp=lis[j]
                lis[j]=lis[j+1]
                lis[j+1]=temp
    return lis

arr=list(map(int,input().split()))
print(dubbbleSort(arr))
