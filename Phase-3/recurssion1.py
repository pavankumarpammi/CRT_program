def s(n,lis,i):
    if i>n:
        return 0
    return lis[i]+s(n,lis,i+1)
def maxi(n,lis,m):
    if n==0:
        return m
    m=max(lis[n],m)
    return maxi(n-1,lis,m)
def mini(n,lis,m):
    if n==0:
        return m
    m=min(lis[n],m)
    return mini(n-1,lis,m)
lis=[15,10,-5,81]
print(s(len(lis)-1,lis,0))
print(maxi(len(lis)-1,lis,-1))
print(mini(len(lis)-1,lis,float('+inf')))
