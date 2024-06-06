arr=[]
def push(data):
    arr.append(data)

def pop():
    if len(arr)>0:
        return arr.pop()
    else:
        print("Stack is empty")
def peek():
    return arr[-1]

val=input()
for i in val:
    if i=='{' or i=='[' or i=='(':
        push(i)
    else:
        val=peek()
        if ((i=='}') and (val=='{')) or ((i==']') and (val=='[')) or ((i==')') and (val=='(')):
            pop()
        else:
            print("Not balanced")
            break
        # lis=["{}",'[]','()']
        # res=''+val+i
        # print(res)
        # for i in lis:
        #     if res==i:
        #         pop()
        #     else:
        #         break
    #print(arr)
if(len(arr)==0):
    print("balanced")