# def top(lis)->int:
#     val=lis[-1]
#     # print("top",val)
#     return val
# def push(array,data):
#     array.append(data)
# def  pop(array):
#     if len(array)>0:
#         array.pop()

# arr=[]
# greater=-1
# lis=[]
# dup=[2,14,16,1,4,12]
# for i in dup:
#     push(lis,i)
#     # top(lis)
# #print(lis)
# while(len(lis)>0):
    
#     if top(lis)>greater:
#         push(arr,top(lis))
#         greater=top(lis)
#         pop(lis)
#     else:
#         push(arr,-1)
#         greater=top
#         pop(lis)
# print(arr)

# 
# def top(stack):
#     return stack[-1]
# def pop():
#     if len(stack)>0:
#         stack.pop()
# def nextGreater(arr,stack,ans,n):
#     ans=[-1]*n
#     for i in range(0,n):
#         curr=arr[i]
#         while(top(stack)!=-1 and top(stack)<=curr):
#             pop(stack)
#         ans[i]=top(stack)
#         stack.append(curr)
#     return ans

# arr=[2,14,16,1,4,12]
# n=len(arr)
# stack=[-1]
# ans=[]
# nextGreater(arr,stack,ans,n)
# print(ans)


#aabcdab  output:a#b#c#d#
def uniqueChar(s):
    dit={}
    for i in s:
        if i not in dit:
            dit[i]=1
    for i in dit:
        print(i,end="#")

s="aabcdab"
uniqueChar(s)
