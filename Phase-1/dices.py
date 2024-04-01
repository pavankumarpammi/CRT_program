def printPath(curr,dest,ans):
    if(curr>dest):
        return
    if(curr==dest):
        print(ans)
    printPath(curr+1,dest,ans+"1")
    printPath(curr+2,dest,ans+"2")
    printPath(curr+3,dest,ans+"3")
    printPath(curr+4,dest,ans+"4")
    printPath(curr+5,dest,ans+"5")
    printPath(curr+6,dest,ans+"6")
curr=0
dest=int(input())
ans=""
printPath(curr,dest,ans)

