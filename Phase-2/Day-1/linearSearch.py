def search(arr,t):
    for i in range(0,len(arr)):
        if(arr[i]==t):
            return i
    return -1

lis=list(map(int,input().split()))
target=int(input("Enter the target:"))
print(search(lis,target))