# write a program to check the type of triangle where take input from user
# classify it according to equalateral and isosi 2 and scaler no two sides
a,b,c =list(map(int,input().split()))
if(a==b==c):
    print('equalateral')
elif((a==b)or(b==c)or(c==a)):
    print('isosceles')
else:
    print('scaler')