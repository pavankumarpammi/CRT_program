#take an integer from user and check whether if the number is divisible by sum of digits or not
# n=int(input())
# sum=0
# dup=n
# while(n>0):
#     rem=n%10
#     n//=10
#     sum+=rem
# print(sum)
# if(dup%sum==0):
#     print('yes it is divisible')
# else:
#     print('Not divisible by sum')
#num input check if the sum of factors of that num is greater than or not
# n=int(input())
# i=1
# sum=0
# while(i<(n//2)+1):
#     if(n%i==0):
#         sum+=i
#     i=i+1
# if(sum>n):
#     print('yes it is greater than actual')
# else:
#     print('No it not greater than actual')
# #calculate the difference of sum of numbers that are divisible 6 and not divisible by 6 in
# #range of first 30 number
# div=0
# not_div=0
# for i in range(1,31):
#     if(i%6==0):
#         div+=i 
#     else:
#         not_div+=i
# print(div,"->",not_div)
# print(not_div-div)
n=int(input())
# rev=0
# rem=0
# dup=n
# while(n>0):
#     rem=n%10
#     n//=10
#     rev=rev*10+rem
# print(rev)
# if(rev==dup):
#     print('palindrome')
# else:
#     print('Not palindrome')
count=1
n_len=0
dup=n
while(n>0):
    # rem=n%10
    n//=10
    n_len+=1
print(n_len)
sum=0
while(dup>0 and n_len!=0):
    rem=dup%10
    sum+=rem**n_len
    # print(n_len)
    dup//=10
    n_len=n_len-1
print(sum)