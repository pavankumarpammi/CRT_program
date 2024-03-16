#print out first 10 fibonanci series
#0 1 1 2 3 5 8 13  21
# a,b=0,1
# print(a,"\n",b)
# for i in range(8):
#     res=a+b
#     print(res)
#     a=b
#     b=res

#algorithtm initalize two variable a,b with respect 0,1
#For each and every step update the value of assign b value to a and assing a+b value to b
#loop the iteration to end

#prime or not
# n=int(input())
# flag=0
# if(n%2==0):
#     flag==1
#     #print("not prime") 
# else:
#     for i in range(2,int(n/2)):
#         if(n%i==0):
#             flag=1
#             break
# if(flag==1):
#     print('Not Prime')
# else:
#     print('Prime')

# #Calculate the sum of digit of a number which taken input from user
    
n=int(input())
res=0
while(n>1):
    rem=n%10
    res+=rem
    n=n//10
print(res)