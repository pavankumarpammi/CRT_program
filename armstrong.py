n=int(input())
len_n=0
arm_sum=0
dup=n
n1=n
while(n>0):
    # rem=n%10
    len_n+=1
    n//=10
while(dup>0):
    rem=dup%10
    arm_sum+=rem**len_n
    dup//=10
if(arm_sum==n1):
    print("The number is an Armstrong")
else:
    print("not an armstrong number")