lis=[]
arr=[]
def push(array,data):
    array.append(data)
def PoP(array):
    # if not isempty(array):
    val=array.pop()
    return val
def top(lis):
    return lis[-1]

def isempty(array):
    if len(array)==0:
        return True
    return False
while(True):
    print("1.Push\t 2.PoP\t 3.Top\t 4.Display")
    n=int(input("Enter your choice:"))
    
    if(n==1):
        data=int(input("Enter the data:"))
        push(lis,data)
        print("Push the value into stack",data)
    if(n==2):
        PoP(lis)
        print("Pop the value",data)
    if(n==3):
        top(lis)
    if(n==4):
        while isempty(lis):
            arr.append(PoP(lis))
        print(arr)
    if(n>4):
        break

        
    

# 1 2 3 4 5 output: 1 2 3 4 5