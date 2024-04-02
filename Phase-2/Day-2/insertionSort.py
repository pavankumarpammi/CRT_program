#insertion sort work on the principle of placing the element in correct position
def insertionSort(lis):
    for i in range(1,len(lis)):
        key=lis[i]
        j=i-1
        while j>0 and lis[j]>key:
            lis[j+1]=lis[j]
            j-=1
        lis[j+1]=key
            
    return lis
    
lis=list(map(int,input().split()))
print(insertionSort(lis))