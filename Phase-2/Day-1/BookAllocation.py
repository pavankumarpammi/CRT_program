def isPossible(s,pages,mid):
    sum1=0
    nos=1
    for i in range(0,len(pages)):
        if sum1+pages[i]<=mid:
            sum1+=pages[i]
        else:
            nos+=1
            if nos<=s or pages[i]>mid:
                return False
    return True
    
def bookAllocation(pages,total_sum,stu):
    low=0
    high=total_sum
    while(low<=high):
        mid=low+(high-low)//2
        if isPossible(stu,pages,mid):
            ans=mid
            high=mid-1
        else:
            low=mid+1
            mid=low+(high-low)//2
    return ans

pages=[10,20,30,40]
print(bookAllocation(pages,100,2))