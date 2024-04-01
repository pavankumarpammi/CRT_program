n=int(input())
count_digit=0
sum=0
mul_digit=1
while(n>0):
    rem =n%10
    count_digit+=1
    n//=10
    sum+=rem
    mul_digit*=rem
    print(rem)

print("No of digits:",count_digit)
print("Sum of digits:",sum)
print("Mul of digits:",mul_digit)

 