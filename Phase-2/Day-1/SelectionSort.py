def selectionSort(lis):
    n=len(lis)
    min_ind=0
    for i in range(0,n):
        min_ind=i
        j=0
        while(j<n):
            if lis[j]>lis[min_ind]:
                temp=lis[min_ind]
                lis[min_ind]=lis[j]
                lis[j]=temp
            #min_ind=j
            j+=1
    return lis
lis=list(map(int,input().split()))
print(selectionSort(lis))